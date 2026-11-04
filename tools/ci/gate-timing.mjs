#!/usr/bin/env node
// Stable maintainer-tool entry point and exported schema-1 contract.
export * from "./gate-timing/core.mjs";
import { main } from "./gate-timing/core.mjs";
import { existsSync, realpathSync } from "node:fs";
import { fileURLToPath } from "node:url";

if (process.argv[1] && existsSync(process.argv[1]) && realpathSync(process.argv[1]) === fileURLToPath(import.meta.url)) await main();
