import { readdirSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
for (const folder of ['.github','.github/tests']) {
  for (const file of readdirSync(folder).filter(n=>n.endsWith('.mjs'))) execFileSync(process.execPath,['--check',`${folder}/${file}`],{stdio:'inherit'});
}
