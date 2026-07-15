#!/usr/bin/env bash
set -euo pipefail

root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$root"

audit=docs/batch2-coverage-audit.md
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT

for file in emit ir openapi naming; do
    test_start=$(rg -n '^#\[cfg\(test\)\]' "src/$file.rs" | head -n1 | cut -d: -f1)
    git diff --unified=0 origin/main..HEAD -- "src/$file.rs" | awk -v file="src/$file.rs" -v test_start="$test_start" '
        /^@@/ {
            if (match($0, /\+[0-9]+/)) line = substr($0, RSTART + 1, RLENGTH - 1) + 0
            next
        }
        /^\+\+\+/ { next }
        /^\+/ {
            text = substr($0, 2)
            control = text ~ /^[[:space:]]*(if|else([[:space:]]+if)?|match|for|while|loop|return|break|continue)[[:space:]({]/ \
                || text ~ /^[[:space:]]*(pub[[:space:]]+)?fn[[:space:]]/ \
                || text ~ /\.(or_else|and_then|is_some_and|filter|find|find_map|map_or_else|then|then_some)\(/ \
                || text ~ /=>/ \
                || text ~ /\?([,;.)]|$)/
            if (line < test_start && control) print file ":" line
            line++
            next
        }
        /^ / { line++ }
    ' >> "$tmp/constructs"
done
sort -u "$tmp/constructs" -o "$tmp/constructs"

awk '
    /^## (emit|ir|openapi|naming)\.rs$/ { file="src/" substr($2, 1, length($2)); next }
    file != "" && /^\| [0-9]/ {
        cell=$0; sub(/^\| /, "", cell); sub(/ \|.*$/, "", cell)
        while (match(cell, /[0-9]+(-[0-9]+)?/)) {
            token=substr(cell, RSTART, RLENGTH); cell=substr(cell, RSTART + RLENGTH)
            split(token, bounds, "-"); start=bounds[1]+0; finish=(bounds[2] == "" ? start : bounds[2]+0)
            for (line=start; line<=finish; line++) print file ":" line
        }
    }
' "$audit" | sort -u > "$tmp/inventory-lines"

comm -23 "$tmp/constructs" "$tmp/inventory-lines" > "$tmp/missing"
if [[ -s "$tmp/missing" ]]; then
    echo "audit misses added control-flow constructs:" >&2
    cat "$tmp/missing" >&2
    exit 1
fi

if rg -n '\bsame test\b|\bsame (two|pointer|ownership|union)|\bnear [0-9]|throughout the suite|ordinary named refs|camel-case/tag package generation tests|subprocess-only' "$audit"; then
    echo "audit contains vague or subprocess coverage evidence" >&2
    exit 1
fi

if rg -n '`[^`]*e2e[^`]*`|tests/e2e\.rs' "$audit"; then
    echo "audit cites subprocess e2e as coverage evidence" >&2
    exit 1
fi

rg -o '^[[:space:]]*fn [A-Za-z_][A-Za-z0-9_]*\(\)' src tests \
    | sed -E 's/.*fn ([A-Za-z_][A-Za-z0-9_]*)\(\)/\1/' \
    | sort -u > "$tmp/tests"
while IFS= read -r row; do
    classification=$(printf '%s\n' "$row" | cut -d'|' -f3)
    evidence=$(printf '%s\n' "$row" | cut -d'|' -f4)
    rationale=$(printf '%s\n' "$row" | cut -d'|' -f5)
    if [[ $classification == *D* ]] && ! printf '%s\n' "$rationale" \
        | rg -qi 'because|enforc|bounds|before|after|derived|defensive'; then
        echo "defensive row does not cite its enforcing invariant: $row" >&2
        exit 1
    fi
    if [[ $classification == *C* ]] && ! printf '%s\n' "$rationale" \
        | rg -qi 'converg|same|shared|both|otherwise|missing|fallback|ordinary|absen|invalid'; then
        echo "convergent row does not identify convergence/shared result: $row" >&2
        exit 1
    fi
    found=false
    while IFS= read -r token; do
        if grep -qx "$token" "$tmp/tests"; then
            found=true
            break
        fi
    done < <(printf '%s\n' "$evidence" \
        | rg -o '`([A-Za-z_][A-Za-z0-9_]*::)*[A-Za-z_][A-Za-z0-9_]*`' \
        | tr -d '`' \
        | sed 's/.*:://')
    if [[ $found == false ]]; then
        echo "audit row has no existing coverage-measured test: $row" >&2
        exit 1
    fi
    ranges=0
    while IFS= read -r reference; do
        ranges=$((ranges + 1))
        if [[ $reference == src/* ]]; then
            file=${reference%%:*}
            span=${reference#*:}
        else
            file=tests/generation.rs
            span=$reference
        fi
        start=${span%-*}
        finish=${span#*-}
        [[ $finish == "$span" ]] && finish=$start
        if ! sed -n "${start},${finish}p" "$file" | rg -q 'assert|expect_err|panic!'; then
            echo "audit evidence range contains no assertion: $file:$span" >&2
            exit 1
        fi
    done < <(printf '%s\n' "$evidence" \
        | rg -o '(src/(emit|ir|openapi|naming)\.rs:)?[0-9]+(-[0-9]+)?')
    if [[ $ranges -eq 0 ]]; then
        echo "audit row has no assertion range: $row" >&2
        exit 1
    fi
done < <(rg '^\| [0-9]' "$audit")

printf '%-12s %10s %10s %10s\n' file constructs inventoried remainder
for file in src/emit.rs src/ir.rs src/openapi.rs src/naming.rs; do
    constructs=$(grep -c "^$file:" "$tmp/constructs" || true)
    inventoried=$(grep "^$file:" "$tmp/constructs" | grep -Fxf "$tmp/inventory-lines" | wc -l)
    printf '%-12s %10d %10d %10d\n' "$file" "$constructs" "$inventoried" "$((constructs - inventoried))"
done
