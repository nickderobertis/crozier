#!/usr/bin/env bash
# Spike harness (spike-shard-loss): one measurement of one Fern stage of one
# refusal probe under one memory ceiling.
#
#   tools/fern-refusals/measure-stage.sh <class> <check|generate> <ceiling> [options]
#
#   <ceiling>        a container --memory: `16g`, `12g`, ... or `infinity` (uncapped)
#   --heap MB        Node's --max-old-space-size (default 16384, as fern-refusals.py)
#   --timeout S      the stage's bound (default 900, the probe's), ended as
#                    fern-refusals.py ends it: SIGKILL to the session it leads
#   --cli V --sdk V  the Fern pair (default: assets/scaffolding/metadata.json)
#   --path DIR       prepend DIR to PATH (repeatable): a Node / Fern CLI toolchain
#   --out DIR        where the record goes (default: the spike's cache)
#
# The stage runs exactly as fern-refusals.py's `fern_run` runs it (same
# workspace files, env, NODE_OPTIONS, argv, new session, kill at the bound),
# inside an ubuntu:26.04 container (the runner's OS) whose --memory is the
# ceiling (swap off), under crozier's Fern generation lock. The kernel's own
# accounting gives the figures: the container cgroup's memory.peak,
# memory.events oom_kill and cpu.stat; any generator container's own
# memory.peak; what of the tree outlived the kill.
#
# Prints one line: class, stage, ceiling, heap, ending, peak, CPU, survivors,
# log bytes and the scrubbed log's sha256. The full record (JSON, the raw and
# scrubbed log, a 5-second memory timeline) is kept under --out.
set -euo pipefail

usage() { sed -n '2,21p' "$0" | sed 's/^# \{0,1\}//' >&2; exit 2; }
[ $# -ge 3 ] || usage
class=$1 stage=$2 ceiling=$3
shift 3
repo=$(CDPATH='' cd -- "$(dirname -- "$0")/../.." && pwd)
heap=16384 timeout=900 cli='' sdk='' extra_path='' out=''
while [ $# -gt 0 ]; do
    case $1 in
        --heap) heap=$2; shift 2 ;;
        --timeout) timeout=$2; shift 2 ;;
        --cli) cli=$2; shift 2 ;;
        --sdk) sdk=$2; shift 2 ;;
        --path) extra_path="$2:$extra_path"; shift 2 ;;
        --out) out=$2; shift 2 ;;
        *) echo "measure-stage: unknown option $1" >&2; usage ;;
    esac
done
case $stage in check|generate) ;; *) echo "measure-stage: stage must be check or generate, not $stage" >&2; exit 2 ;; esac
probe=$repo/docs/fern-refusals/$class/probe.yml
[ -f "$probe" ] || { echo "measure-stage: no probe document $probe; name a class under docs/fern-refusals/" >&2; exit 2; }
meta=$repo/assets/scaffolding/metadata.json
[ -n "$cli" ] || cli=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["cliVersion"])' "$meta")
[ -n "$sdk" ] || sdk=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["generatorVersion"])' "$meta")
cache=${XDG_CACHE_HOME:-$HOME/.cache}/crozier
[ -n "$out" ] || out=$cache/fern-byte-match/$cli-$sdk/shard-loss/runs
stamp=$(date -u +%Y%m%dT%H%M%SZ)
record=$out/$class.$stage.$ceiling.heap$heap.$stamp
mkdir -p "$record"

scratch=$(mktemp -d "${TMPDIR:-/tmp}/fern-refusals-probe-XXXXXX")
trap 'rm -rf "$scratch"' EXIT
workspace=$scratch/fern
mkdir -p "$workspace/openapi"
cp "$probe" "$workspace/openapi/openapi.yml"
printf '{"organization": "fern", "version": "%s"}\n' "$cli" > "$workspace/fern.config.json"
cat > "$workspace/generators.yml" <<EOF
api:
  path: openapi/openapi.yml
groups:
  python-sdk:
    generators:
      - name: fernapi/fern-python-sdk
        version: $sdk
        config:
          pydantic_config:
            enum_type: python_enums
        output:
          location: local-file-system
          path: ../generated/python
EOF
if [ "$stage" = check ]; then
    argv=(fern check)
else
    argv=(fern generate --group python-sdk --local --preview --output "$scratch/preview" --force)
fi

# The container's main process: start the stage in a session of its own, end
# that session at the bound as fern_run does, then read the cgroup's accounting
# while still inside it and list what outlived the kill. The container ending
# with it clears whatever did.
cat > "$scratch/supervise.sh" <<'EOF'
#!/usr/bin/env bash
set -u
record=$1 timeout=$2; shift 2
cg=/sys/fs/cgroup
start=$(date +%s.%N)
setsid "$@" > "$record/stage.log" 2>&1 &
leader=$!
ending=''
while kill -0 "$leader" 2>/dev/null; do
    if [ $(( $(date +%s) - ${start%.*} )) -ge "$timeout" ]; then
        ending=timeout
        kill -9 -- "-$leader" 2>/dev/null
        break
    fi
    sleep 1
done
wait "$leader"; status=$?
end=$(date +%s.%N)
[ -n "$ending" ] || ending="exit:$status"
sleep 2
# Everything still in the container but this supervisor outlived the session kill.
# Read with a builtin, so the listing forks nothing that would list itself.
mapfile -t procs < "$cg/cgroup.procs"
: > "$record/survivors"
for pid in "${procs[@]}"; do
    [ "$pid" != "$$" ] || continue
    [ -r "/proc/$pid/cmdline" ] || continue
    printf '%s %s\n' "$pid" "$(tr '\0' ' ' < "/proc/$pid/cmdline" | cut -c1-200)" >> "$record/survivors"
done
{
    echo "ending=$ending"
    echo "status=$status"
    echo "seconds=$(awk -v a="$start" -v b="$end" 'BEGIN{printf "%.1f", b-a}')"
    echo "memory_peak=$(cat "$cg/memory.peak")"
    echo "memory_max=$(cat "$cg/memory.max")"
    echo "swap_peak=$(cat "$cg/memory.swap.peak" 2>/dev/null || echo 0)"
    sed 's/^/events_/; s/ /=/' "$cg/memory.events"
    sed 's/^/cpu_/; s/ /=/' "$cg/cpu.stat" | grep -E 'cpu_(usage|user|system)_usec'
} > "$record/accounting"
echo done > "$record/supervised"
EOF
chmod +x "$scratch/supervise.sh"

lock=$cache/fern-generation.lock
mkdir -p "$(dirname "$lock")" "$scratch/home"
limits=()
[ "$ceiling" = infinity ] || limits=(--memory "$ceiling" --memory-swap "$ceiling")
mounts=(-v "$scratch:$scratch" -v "$record:$record" -v /usr/bin/docker:/usr/bin/docker:ro
    -v /var/run/docker.sock:/var/run/docker.sock --group-add "$(stat -c %g /var/run/docker.sock)")
IFS=: read -r -a dirs <<< "$extra_path"
for dir in "${dirs[@]}"; do
    [ -n "$dir" ] || continue
    root=$(dirname "$dir")
    mounts+=(-v "$root:$root:ro")
done
cidfile=$scratch/cid
load_before=$(cut -d" " -f1-3 /proc/loadavg | tr " " /)
before_df=$(df -B1 --output=used "${TMPDIR:-/tmp}" "$HOME" | tail -n +2 | tr '\n' ' ')
flock "$lock" docker run --rm --init=false --cidfile "$cidfile" --user "$(id -u):$(id -g)" \
    "${limits[@]}" "${mounts[@]}" -w "$workspace" \
    -e HOME="$scratch/home" -e PATH="${extra_path}/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin" \
    -e FERN_TOKEN=preview-only-no-publish -e CI=true -e GITHUB_ACTIONS=true \
    -e NODE_OPTIONS="--max-old-space-size=$heap" \
    ubuntu:26.04 "$scratch/supervise.sh" "$record" "$timeout" "${argv[@]}" > "$record/docker-run.log" 2>&1 &
runner=$!

# Outside the container: a timeline of its memory, and the peak of every
# generator container this workspace starts (accounted to a cgroup of its own,
# but on a runner it is the same VM's memory).
: > "$record/timeline.tsv"
: > "$record/containers"
declare -A generator_peak=()
t0=$(date +%s)
while kill -0 "$runner" 2>/dev/null; do
    if [ -s "$cidfile" ] && [ ! -e "$record/supervised" ]; then
        cur=$(cat "/sys/fs/cgroup/system.slice/docker-$(cat "$cidfile").scope/memory.current" 2>/dev/null || echo '')
        [ -z "$cur" ] || printf '%s\t%s\n' "$(( $(date +%s) - t0 ))" "$cur" >> "$record/timeline.tsv"
    fi
    if [ "$stage" = generate ]; then
        for id in $(docker ps -q --no-trunc 2>/dev/null); do
            [ "$id" != "$(cat "$cidfile" 2>/dev/null)" ] || continue
            if [ -z "${generator_peak[$id]+x}" ]; then
                docker inspect --format '{{range .Mounts}}{{.Source}} {{end}}' "$id" 2>/dev/null | grep -q "$scratch" || continue
                echo "$id" >> "$record/containers"
                generator_peak[$id]=0
            fi
            peak=$(cat "/sys/fs/cgroup/system.slice/docker-$id.scope/memory.peak" 2>/dev/null || echo 0)
            [ "$peak" -le "${generator_peak[$id]}" ] || generator_peak[$id]=$peak
        done
    fi
    sleep 5
done
wait "$runner" || true
load_after=$(cut -d" " -f1-3 /proc/loadavg | tr " " /)
scratch_bytes=$(du -sb "$scratch" | cut -f1)
after_df=$(df -B1 --output=used "${TMPDIR:-/tmp}" "$HOME" | tail -n +2 | tr '\n' ' ')

container_note=none
if [ -s "$record/containers" ]; then
    container_note=''
    while read -r id; do
        running=$(docker inspect --format '{{.State.Running}}' "$id" 2>/dev/null || echo removed)
        container_note="$container_note${id:0:12}(peak=$(( ${generator_peak[$id]} / 1048576 ))MiB,after_bound=$running) "
        # This workspace's own generator, identified by its mount: clear it.
        [ "$running" != true ] || docker rm -f "$id" > /dev/null
    done < "$record/containers"
fi

[ -e "$record/supervised" ] || { echo "measure-stage: the container never reported; see $record/docker-run.log" >&2; exit 1; }
# shellcheck disable=SC1091
. "$record/accounting"
python3 - "$repo" "$record" <<'EOF'
import hashlib, importlib.util, sys
from pathlib import Path
repo, record = Path(sys.argv[1]), Path(sys.argv[2])
spec = importlib.util.spec_from_file_location("fern_refusals", repo / "tools/fern-refusals/fern-refusals.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
log = (record / "stage.log").read_text(encoding="utf-8", errors="replace")
scrubbed = module.scrub(log)
(record / "stage.scrubbed.log").write_text(scrubbed, encoding="utf-8")
(record / "scrubbed.sha256").write_text(hashlib.sha256(scrubbed.encode()).hexdigest() + "\n")
EOF
survivors=$(wc -l < "$record/survivors")
mib() { awk -v b="$1" 'BEGIN{printf "%.0f MiB", b/1048576}'; }
cpu_s=$(awk -v u="$cpu_usage_usec" 'BEGIN{printf "%.0f", u/1e6}')
line="class=$class stage=$stage pair=$cli/$sdk ceiling=$ceiling heap=${heap}MB ending=$ending seconds=$seconds"
line="$line peak=$(mib "$memory_peak") oom_kill=$events_oom_kill cpu=${cpu_s}s survivors=$survivors"
line="$line containers=$container_note log_bytes=$(wc -c < "$record/stage.scrubbed.log") scrubbed_sha256=$(cut -c1-12 "$record/scrubbed.sha256")"
line="$line load=$load_before..$load_after scratch=$(( scratch_bytes / 1048576 ))MiB host_disk_used_delta=$(awk -v a="$before_df" -v b="$after_df" 'BEGIN{split(a,x," ");split(b,y," ");printf "%+.0fMiB/%+.0fMiB", (y[1]-x[1])/1048576, (y[2]-x[2])/1048576}') record=$record"
echo "$line" | tee "$record/summary"
