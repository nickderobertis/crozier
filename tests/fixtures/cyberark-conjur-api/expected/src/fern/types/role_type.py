

RoleType = str
"""
##### Kinds of roles:

- User: one unique wonderful human
- Host: a single logical machine (in the broad sense, not just physical)
- Layer: a collection of hosts that have the same privileges
- Group: a collection of users and groups that have the same privileges
- Policy: a role which owns of a set of related object

Any identifier included in the URL must be URL-encoded to be recognized by the Conjur API.

##### Resource Identifiers:

- `myapp-01` -> `myapp-01` (unchanged)
- `alice@devops` -> `alice%40devops`
- `prod/aws/db-password` -> `prod%2Faws%2Fdb-password`
- `research+development` -> `research%2Bdevelopment`
- `sales&marketing` -> `sales%26marketing`
"""
