

ResourceId = str
"""
Resource identifier. Requires to be encoded when in path.

##### Examples:

- `myapp-01` -> `myapp-01` (unchanged)
- `alice@devops` -> `alice%40devops`
- `prod/aws/db-password` -> `prod%2Faws%2Fdb-password`
- `research+development` -> `research%2Bdevelopment`
- `sales&marketing` -> `sales%26marketing`
"""
