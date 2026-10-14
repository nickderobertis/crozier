#!/usr/bin/env bash
# Exit 0 means all tests passed; propagate Node nonzero status on test/runner failure.
set -euo pipefail
# llmlint: ignore[shell_test_tiers_stay_split] The manager-approved task fixes this workload as node --test .github/tests/*.test.mjs, including real-Git classifier subprocess journeys and actual-workflow graph resolution; all new tooling tests and the telemetry recorder must stay inside .github rather than split into another tier.
node --test .github/tests/*.test.mjs
