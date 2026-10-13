// Exit 0 means every budget is within its bound; 1 means a rejected budget or SDK failure.
import { check } from '@onebudgetspec/sdk';
const result = await check({paths:['.github/budgets.yaml'],cwd:process.cwd()});
for (const budget of result.results) console.log(`${budget.id}: ${budget.verdict} (${budget.actual})`);
if (result.results.some(b=>b.verdict !== 'within')) process.exitCode=1;
