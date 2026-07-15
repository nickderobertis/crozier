#!/usr/bin/env bash
set -euo pipefail

root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$root"

audit=${CROZIER_AUDIT_FILE:-docs/batch2-coverage-audit.md}
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT

extract_constructs() {
    local file=$1 excluded=${2:-}
    awk -v file="$file" -v excluded="$excluded" '
        BEGIN {
            count = split(excluded, spans, ",")
            for (i = 1; i <= count; i++) {
                split(spans[i], bounds, "-")
                excluded_start[i] = bounds[1] + 0
                excluded_end[i] = bounds[2] + 0
            }
        }
        function is_excluded(candidate, i) {
            for (i = 1; i <= count; i++) {
                if (candidate >= excluded_start[i] && candidate <= excluded_end[i]) return 1
            }
            return 0
        }
        function code_only(source, i, ch, next_ch, output, quoted, escaped) {
            output = ""; quoted = 0; escaped = 0
            for (i = 1; i <= length(source); i++) {
                ch = substr(source, i, 1); next_ch = substr(source, i + 1, 1)
                if (!quoted && ch == "/" && next_ch == "/") break
                if (!escaped && ch == "\"") {
                    quoted = !quoted
                    output = output " "
                } else if (quoted) {
                    escaped = !escaped && ch == "\\"
                    output = output " "
                } else {
                    escaped = 0
                    output = output ch
                }
            }
            return output
        }
        /^@@/ {
            if (match($0, /\+[0-9]+/)) line = substr($0, RSTART + 1, RLENGTH - 1) + 0
            next
        }
        /^\+\+\+/ { next }
        /^\+/ {
            text = code_only(substr($0, 2))
            inside_macro = macro_depth > 0
            if (text ~ /\.map_or_else\(/) expected_closures = 2
            else if (text ~ /\.unwrap_or_else\(/) expected_closures = 1
            named_closure = text ~ /^[[:space:]]*\|[^|]+\|/ \
                || text ~ /[(,][[:space:]]*\|[^|]+\|/
            zero_closure = expected_closures > 0 \
                && (text ~ /^[[:space:]]*\|\|/ || text ~ /[(,][[:space:]]*\|\|/)
            control = text ~ /^[[:space:]]*(if|match)[[:space:]({]/ \
                || text ~ /[=;}][[:space:]]+(if|else([[:space:]]+if)?|match)[[:space:]({]/ \
                || text ~ /^[[:space:]]*}[[:space:]]*else([[:space:]]+if)?[[:space:]({]/ \
                || text ~ /^[[:space:]]*(for|while|loop|return|break|continue)[[:space:]({;]/ \
                || text ~ /^[[:space:]]*(pub(\([^)]*\))?[[:space:]]+)?(async[[:space:]]+)?(const[[:space:]]+)?(unsafe[[:space:]]+)?fn[[:space:]]/ \
                || text ~ /\.(or_else|and_then|is_some_and|filter|find|find_map|flat_map|map|map_or|map_or_else|unwrap_or_else|any|all|then|then_some)(::<[^>]+>)?\(/ \
                || named_closure \
                || zero_closure \
                || text ~ /=>/ \
                || text ~ /\?([,;.)]|$)/
            if (!is_excluded(line) && control && !inside_macro) print file ":" line
            if (expected_closures > 0 && (named_closure || zero_closure)) expected_closures--
            if (expected_closures > 0 && text ~ /^[[:space:]]*\)/) expected_closures = 0
            if (text ~ /matches!\(/) macro_depth = 1
            if (macro_depth > 0) {
                opens = text; open_count = gsub(/\(/, "", opens)
                closes = text; close_count = gsub(/\)/, "", closes)
                macro_depth += open_count - close_count
                if (text ~ /matches!\(/) macro_depth--
            }
            line++
            next
        }
        /^ / { line++ }
    '
}

extract_inventory_lines() {
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
    '
}

mappings_are_exact() {
    local constructs=$1 inventory=$2 construct count
    while IFS= read -r construct; do
        count=$(grep -cFx "$construct" "$inventory" || true)
        [[ $count -eq 1 ]] || return 1
    done < "$constructs"
}

if [[ ${1:-} == --self-test ]]; then
    synthetic='@@ -0,0 +10,14 @@
+fn multiline(value: Option<u8>) -> Option<u8> {
+    if value
+        .is_some_and(
+            |item| item > 0,
+        )
+    {
+        return value.and_then(
+            |item| Some(item + 1),
+        );
+    }
+    match value {
+        Some(item) => Some(item),
+        None => None,
+    }
+}'
    actual=$(printf '%s\n' "$synthetic" | extract_constructs src/sample.rs "")
    expected='src/sample.rs:10
src/sample.rs:11
src/sample.rs:12
src/sample.rs:13
src/sample.rs:16
src/sample.rs:17
src/sample.rs:20
src/sample.rs:21
src/sample.rs:22'
    [[ $actual == "$expected" ]] || {
        printf 'multiline extraction mismatch\nexpected:\n%s\nactual:\n%s\n' "$expected" "$actual" >&2
        exit 1
    }
    lexical='@@ -0,0 +100,18 @@
+fn production(value: Option<u8>) -> Option<u8> {
+    // if match return |comment| => ?
+    let text = "if match return |string| => ?";
+    fake!(if true { return None; });
+    let output = value
+        .map::<u8>(
+            |item| item + 1,
+        )?;
+    match output {
+        Some(item)
+            => Some(item),
+        None => None,
+    }
+}
+#[cfg(test)]
+mod tests { fn ignored() { if true {} } }
+fn later_production() { return; }
+'
    lexical_actual=$(printf '%s\n' "$lexical" | extract_constructs src/sample.rs "114-115")
    lexical_expected='src/sample.rs:100
src/sample.rs:105
src/sample.rs:106
src/sample.rs:107
src/sample.rs:108
src/sample.rs:110
src/sample.rs:111
src/sample.rs:116'
    [[ $lexical_actual == "$lexical_expected" ]] || {
        printf 'lexical extraction mismatch\nexpected:\n%s\nactual:\n%s\n' \
            "$lexical_expected" "$lexical_actual" >&2
        exit 1
    }
    synthetic_audit='## emit.rs
| Production lines and selection | Class | Test and assertion | Why distinctive |
|---|---|---|---|
| 10-11: valid group | P | `measured`, 20 | assertion |
| 11: duplicate mapping | P | `measured`, 20 | assertion |

## ir.rs
| Production lines and selection | Class | Test and assertion | Why distinctive |
|---|---|---|---|
| 30: orphan mapping | P | `measured`, 20 | assertion |'
    printf '%s\n' "$synthetic_audit" | extract_inventory_lines > "$tmp/synthetic-inventory"
    printf '%s\n' src/emit.rs:10 src/emit.rs:11 src/emit.rs:12 > "$tmp/synthetic-constructs"
    [[ $(grep -c '^src/emit.rs:10$' "$tmp/synthetic-inventory") -eq 1 ]]
    [[ $(grep -c '^src/emit.rs:11$' "$tmp/synthetic-inventory") -eq 2 ]]
    ! grep -q '^src/emit.rs:12$' "$tmp/synthetic-inventory"
    grep -qx 'src/ir.rs:30' "$tmp/synthetic-inventory"
    ! mappings_are_exact "$tmp/synthetic-constructs" "$tmp/synthetic-inventory"
    echo "batch2 coverage audit checker self-tests: ok"
    exit 0
fi

for file in emit ir openapi naming; do
    test_ranges=$(cargo run --quiet --example audit_syntax -- "src/$file.rs" | paste -sd, -)
    git diff --unified=0 origin/main..HEAD -- "src/$file.rs" \
        | extract_constructs "src/$file.rs" "$test_ranges" >> "$tmp/constructs"
done
sort -u "$tmp/constructs" -o "$tmp/constructs"

if [[ ${1:-} == --dump-constructs ]]; then
    cat "$tmp/constructs"
    exit 0
fi

extract_inventory_lines < "$audit" > "$tmp/inventory-lines-raw"
sort -u "$tmp/inventory-lines-raw" > "$tmp/inventory-lines"

while IFS= read -r construct; do
    count=$(grep -cFx "$construct" "$tmp/inventory-lines-raw" || true)
    if [[ $count -ne 1 ]]; then
        echo "construct must map to exactly one inventory entry ($count found): $construct" >&2
        exit 1
    fi
done < "$tmp/constructs"

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

rg -o '^[[:space:]]*fn [A-Za-z_][A-Za-z0-9_]*\(\)' src tests/generation.rs tests/cli.rs \
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
    mapfile -t cited_tests < <(printf '%s\n' "$evidence" \
        | rg -o '`([A-Za-z_][A-Za-z0-9_]*::)*[A-Za-z_][A-Za-z0-9_]*`' \
        | tr -d '`' \
        | sed 's/.*:://' \
        | grep -Fxf "$tmp/tests" || true)
    mapfile -t cited_ranges < <(printf '%s\n' "$evidence" \
        | rg -o '(src/(emit|ir|openapi|naming)\.rs:)?[0-9]+(-[0-9]+)?')
    if [[ ${#cited_tests[@]} -ne ${#cited_ranges[@]} ]]; then
        echo "audit evidence must pair each measured test with one assertion range: $row" >&2
        exit 1
    fi
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
    for index in "${!cited_ranges[@]}"; do
        reference=${cited_ranges[$index]}
        test=${cited_tests[$index]}
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
        file_lines=$(wc -l < "$file")
        if [[ $start -lt 1 || $finish -lt $start || $finish -gt $file_lines ]]; then
            echo "audit evidence range is outside file bounds: $file:$span" >&2
            exit 1
        fi
        if ! sed -n "${start},${finish}p" "$file" | rg -q 'assert|expect_err|panic!'; then
            echo "audit evidence range contains no assertion: $file:$span" >&2
            exit 1
        fi
        test_line=$(rg -n "^[[:space:]]*fn ${test}\(\)" "$file" | head -n1 | cut -d: -f1)
        if [[ -z $test_line || $start -lt $test_line ]]; then
            echo "assertion range is not inside cited test $test: $file:$span" >&2
            exit 1
        fi
        next_test=$(awk -v start="$test_line" 'NR > start && /^[[:space:]]*fn [A-Za-z_][A-Za-z0-9_]*\(\)/ { print NR; exit }' "$file")
        if [[ -n $next_test && $finish -ge $next_test ]]; then
            echo "assertion range crosses out of cited test $test: $file:$span" >&2
            exit 1
        fi
    done
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
