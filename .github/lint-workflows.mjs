// actionlint is a local focused check. Hosted CI installs the same binary before
// the project runs; missing tooling is an error, never a silently skipped lint.
import { spawnSync } from 'node:child_process';
const run=spawnSync('actionlint',['.github/workflows/ci.yml','.github/workflows/release.yml'],{stdio:'inherit'});
if (run.error) console.error(`actionlint unavailable: install it before github-workflows:lint (${run.error.message})`);
process.exitCode=run.status ?? 1;
