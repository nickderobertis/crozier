# Reference
## External
<details><summary><code>client.external.<a href="src/fern/external/client.py">github_org_members</a>(...) -> GithubOrgMembersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all members of a GitHub organization.

Lists every member of the organization (any role) using the GitHub API
token resolved from Vault. Results are cached for performance (TTL
configured in settings).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.external.github_org_members(
    secret_manager_url="secret_manager_url",
    path="path",
    org_name="org_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**secret_manager_url:** `str` — Secret Manager URL
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Path to the secret
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `str` — GitHub organization name
    
</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Specific field within the secret
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` — Version of the secret
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.external.<a href="src/fern/external/client.py">ldap_github_usernames</a>(...) -> LdapGithubUsernamesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resolve GitHub usernames to LDAP uids via the rhatSocialURL attribute.

Maps each requested GitHub username to the app-interface org_username (LDAP
uid) of the user whose rhatSocialURL points at that GitHub account. The
full map is cached for performance; unresolved logins are omitted from the
response.

Args:
    request: GitHub usernames to resolve and the Vault secret reference
    cache: Cache dependency
    secret_manager: Secret manager dependency

Returns:
    LdapGithubUsernamesResponse with resolved username -> org_username pairs
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, LdapDirectSecret

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.external.ldap_github_usernames(
    logins=[
        "logins"
    ],
    secret=LdapDirectSecret(
        base_dn="base_dn",
        path="path",
        secret_manager_url="secret_manager_url",
        server_url="server_url",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**logins:** `typing.List[str]` — GitHub usernames to resolve to LDAP uids
    
</dd>
</dl>

<dl>
<dd>

**secret:** `LdapDirectSecret` — Vault secret reference for LDAP credentials
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.external.<a href="src/fern/external/client.py">ldap_users_check</a>(...) -> LdapUsersCheckResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check which usernames exist in LDAP (cached, FreeIPA-authenticated).

Queries LDAP directly using FreeIPA service account credentials
resolved from Vault. Results are cached for performance.

Args:
    request: Request with usernames to check and Vault secret reference
    cache: Cache dependency
    secret_manager: Secret manager dependency

Returns:
    LdapUsersCheckResponse with existence status per username
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, LdapDirectSecret

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.external.ldap_users_check(
    secret=LdapDirectSecret(
        base_dn="base_dn",
        path="path",
        secret_manager_url="secret_manager_url",
        server_url="server_url",
    ),
    usernames=[
        "usernames"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**secret:** `LdapDirectSecret` — Vault secret reference for LDAP credentials
    
</dd>
</dl>

<dl>
<dd>

**usernames:** `typing.List[str]` — Usernames to check
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.external.<a href="src/fern/external/client.py">ocm_clusters</a>(...) -> OcmClustersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Discover OCM clusters with subscription/organization labels matching a prefix.

Returns raw cluster info plus a flat dict of matching labels, merged with
subscription-level labels winning over organization-level labels on key
collisions. Label *interpretation* is left entirely to the caller. Results
are cached (TTL configured in settings).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.external.ocm_clusters(
    secret_manager_url="secret_manager_url",
    path="path",
    ocm_url="ocm_url",
    access_token_url="access_token_url",
    access_token_client_id="access_token_client_id",
    label_key_prefix="label_key_prefix",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**secret_manager_url:** `str` — Secret Manager URL
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Path to the secret
    
</dd>
</dl>

<dl>
<dd>

**ocm_url:** `str` — OCM environment base URL
    
</dd>
</dl>

<dl>
<dd>

**access_token_url:** `str` — OAuth2 token endpoint (client-credentials grant)
    
</dd>
</dl>

<dl>
<dd>

**access_token_client_id:** `str` — OAuth2 client id
    
</dd>
</dl>

<dl>
<dd>

**label_key_prefix:** `str` — Subscription/organization label key prefix to search for (e.g. 'sre-capabilities.rhidp'); matched with a trailing '%' wildcard
    
</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Specific field within the secret
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` — Version of the secret
    
</dd>
</dl>

<dl>
<dd>

**org_ids:** `typing.Optional[typing.List[str]]` — Optional list of organization ids to restrict results to. Omit to include all matching organizations.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.external.<a href="src/fern/external/client.py">pagerduty_escalation_policy_users</a>(...) -> EscalationPolicyUsersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get users in a PagerDuty escalation policy.

Fetches all users across all escalation rules in the policy.
Results are cached for performance (TTL configured in settings).

Args:
    policy_id: PagerDuty escalation policy ID
    instance: PagerDuty instance name

Returns:
    EscalationPolicyUsersResponse with list of users

Raises:
    HTTPException:
        - 500 Internal Server Error: If PagerDuty API call fails

Example:
    GET /api/v1/external/pagerduty/escalation-policies/XYZ789/users?instance=app-sre
    Response:
    {
        "users": [
            {"username": "jsmith"},
            {"username": "mdoe"}
        ]
    }
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.external.pagerduty_escalation_policy_users(
    policy_id="policy_id",
    secret_manager_url="secret_manager_url",
    path="path",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**policy_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**secret_manager_url:** `str` — Secret Manager URL
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Path to the secret
    
</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Specific field within the secret
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` — Version of the secret
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.external.<a href="src/fern/external/client.py">pagerduty_schedule_users</a>(...) -> ScheduleUsersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get users currently on-call in a PagerDuty schedule.

Fetches users from the specified schedule using a time window of now + 60 seconds.
Results are cached for performance (TTL configured in settings).

Args:
    schedule_id: PagerDuty schedule ID
    instance: PagerDuty instance name

Returns:
    ScheduleUsersResponse with list of users

Raises:
    HTTPException:
        - 500 Internal Server Error: If PagerDuty API call fails

Example:
    GET /api/v1/external/pagerduty/schedules/ABC123/users?instance=app-sre
    Response:
    {
        "users": [
            {"username": "jsmith"},
            {"username": "mdoe"}
        ]
    }
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.external.pagerduty_schedule_users(
    schedule_id="schedule_id",
    secret_manager_url="secret_manager_url",
    path="path",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**schedule_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**secret_manager_url:** `str` — Secret Manager URL
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Path to the secret
    
</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Specific field within the secret
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` — Version of the secret
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.external.<a href="src/fern/external/client.py">slack_chat_post_message</a>(...) -> ChatResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Post a message to a Slack channel or send a DM to a user.

Exactly one of `channel` or `user` must be set in the request:
- `channel`: post to a Slack channel by name
- `user`: send a DM to a user by org_username

Args:
    request: Chat request with channel/user, text, and credentials

Returns:
    ChatResponse with ts, channel, and optional thread_ts

Raises:
    HTTPException:
        - 404 Not Found: Channel or user not found
        - 502 Bad Gateway: If Slack API call fails
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Secret

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.external.slack_chat_post_message(
    secret=Secret(
        path="path",
        secret_manager_url="secret_manager_url",
    ),
    text="text",
    workspace_name="workspace_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**secret:** `Secret` — Secret reference for Slack bot token
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — Message text
    
</dd>
</dl>

<dl>
<dd>

**workspace_name:** `str` — Slack workspace name
    
</dd>
</dl>

<dl>
<dd>

**channel:** `typing.Optional[str]` — Channel name to post to (e.g., 'sd-app-sre-reconcile')
    
</dd>
</dl>

<dl>
<dd>

**icon_emoji:** `typing.Optional[str]` — Emoji to use as the message icon (e.g., ':robot_face:')
    
</dd>
</dl>

<dl>
<dd>

**icon_url:** `typing.Optional[str]` — URL to an image to use as the message icon
    
</dd>
</dl>

<dl>
<dd>

**thread_ts:** `typing.Optional[str]` — Optional thread timestamp for replies
    
</dd>
</dl>

<dl>
<dd>

**user:** `typing.Optional[str]` — org_username to send a DM to (e.g., 'jsmith@redhat.com')
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` — Bot username to display
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.external.<a href="src/fern/external/client.py">vcs_file_sync</a>(...) -> FileSyncResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reconcile file states in a VCS repository.

Creates a merge request with the given file operations,
deduplicating by MR title. Does not read current file state —
relies on GitLab/GitHub for validation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Secret
from fern.external import FileSyncRequestFileOperationsItem_Create

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.external.vcs_file_sync(
    file_operations=[
        FileSyncRequestFileOperationsItem_Create(
            commit_message="commit_message",
            content="content",
            path="path",
        )
    ],
    repo_url="repo_url",
    target_branch="target_branch",
    title="title",
    token=Secret(
        path="path",
        secret_manager_url="secret_manager_url",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_operations:** `typing.List[FileSyncRequestFileOperationsItem]` — File operations to reconcile
    
</dd>
</dl>

<dl>
<dd>

**repo_url:** `str` — Repository URL (e.g., https://gitlab.com/group/project)
    
</dd>
</dl>

<dl>
<dd>

**target_branch:** `str` — Target branch name
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` — Merge request title (used for deduplication)
    
</dd>
</dl>

<dl>
<dd>

**token:** `Secret` — Secret reference for VCS API token
    
</dd>
</dl>

<dl>
<dd>

**auto_merge:** `typing.Optional[bool]` — Whether to enable auto-merge
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Merge request description
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[typing.List[str]]` — Labels to apply to the MR
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.external.<a href="src/fern/external/client.py">vcs_get_file</a>(...) -> GetFileResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read a file from a VCS repository.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.external.vcs_get_file(
    secret_manager_url="secret_manager_url",
    path="path",
    repo_url="repo_url",
    file_path="file_path",
    ref="ref",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**secret_manager_url:** `str` — Secret Manager URL
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Path to the secret
    
</dd>
</dl>

<dl>
<dd>

**repo_url:** `str` — Repository URL (e.g., https://gitlab.com/group/project)
    
</dd>
</dl>

<dl>
<dd>

**file_path:** `str` — File path in the repository
    
</dd>
</dl>

<dl>
<dd>

**ref:** `str` — Git reference (branch, tag, SHA)
    
</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Specific field within the secret
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` — Version of the secret
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.external.<a href="src/fern/external/client.py">vcs_repo_owners</a>(...) -> RepoOwnersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get OWNERS file data from a Git repository.

Fetches OWNERS file approvers and reviewers from GitHub or GitLab repositories.
Results are cached for performance (TTL configured in settings).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.external.vcs_repo_owners(
    secret_manager_url="secret_manager_url",
    path="path",
    repo_url="repo_url",
    ref="ref",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**secret_manager_url:** `str` — Secret Manager URL
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Path to the secret
    
</dd>
</dl>

<dl>
<dd>

**repo_url:** `str` — Repository URL (e.g., https://github.com/owner/repo)
    
</dd>
</dl>

<dl>
<dd>

**ref:** `str` — Git reference (branch, tag, commit SHA)
    
</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Specific field within the secret
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` — Version of the secret
    
</dd>
</dl>

<dl>
<dd>

**owners_file:** `typing.Optional[str]` — Path to OWNERS file in the repository (e.g., /OWNERS or /path/to/OWNERS)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Integrations
<details><summary><code>client.integrations.<a href="src/fern/integrations/client.py">github_owners</a>(...) -> GithubOwnersTaskResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Queue a GitHub owners reconciliation task.

This endpoint always queues a background task and returns immediately
with a task_id. Use GET /reconcile/{task_id} to retrieve the result.

Args:
    reconcile_request: Reconciliation request with desired owner state
    current_user: Authenticated user (from JWT token)
    request: FastAPI Request object (used to generate status_url)

Returns:
    GithubOwnersTaskResponse with task_id and status_url
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GithubOrgDesiredState, Secret

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.integrations.github_owners(
    organizations=[
        GithubOrgDesiredState(
            org_name="org_name",
            owners=[
                "owners"
            ],
            token=Secret(
                path="path",
                secret_manager_url="secret_manager_url",
            ),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organizations:** `typing.List[GithubOrgDesiredState]` — List of GitHub organizations with their desired owner membership
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — If True, only calculate actions without executing. Default: True (safety first!)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/fern/integrations/client.py">github_owners_task_status</a>(...) -> GithubOwnersTaskResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the reconciliation result (blocking or non-blocking).

**Non-blocking mode (default):** Returns immediate status (pending/success/failed)
**Blocking mode (with timeout):** Waits up to timeout seconds, returns 408 if still pending

Args:
    task_id: Task ID from POST /reconcile response
    current_user: Authenticated user (from JWT token)
    timeout: Maximum seconds to wait (default: None = non-blocking)

Returns:
    GithubOwnersTaskResult with status, actions, applied_count, and errors

Raises:
    HTTPException:
        - 404 Not Found: Task ID not found
        - 408 Request Timeout: Task still pending after timeout (blocking mode only)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.integrations.github_owners_task_status(
    task_id="task_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**timeout:** `typing.Optional[int]` — Optional: Block up to N seconds for completion. Omit for immediate status check.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/fern/integrations/client.py">glitchtip_project_alerts</a>(...) -> GlitchtipProjectAlertsTaskResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Queue Glitchtip project alerts reconciliation task.

This endpoint always queues a background task and returns immediately
with a task_id. Use GET /reconcile/{task_id} to retrieve the result.

Args:
    reconcile_request: Reconciliation request with desired state
    current_user: Authenticated user (from JWT token)
    request: FastAPI Request object (used to generate status_url)

Returns:
    GlitchtipProjectAlertsTaskResponse with task_id and status_url
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GlitchtipInstance, Secret

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.integrations.glitchtip_project_alerts(
    instances=[
        GlitchtipInstance(
            console_url="console_url",
            name="name",
            token=Secret(
                path="path",
                secret_manager_url="secret_manager_url",
            ),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**instances:** `typing.List[GlitchtipInstance]` — List of Glitchtip instances to reconcile
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — If True, only calculate actions without executing. Default: True (safety first!)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/fern/integrations/client.py">glitchtip_project_alerts_task_status</a>(...) -> GlitchtipProjectAlertsTaskResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve reconciliation result (blocking or non-blocking).

**Non-blocking mode (default):** Returns immediate status (pending/success/failed)
**Blocking mode (with timeout):** Waits up to timeout seconds, returns 408 if still pending

Args:
    task_id: Task ID from POST /reconcile response
    current_user: Authenticated user (from JWT token)
    timeout: Maximum seconds to wait (default: None = non-blocking)

Returns:
    GlitchtipProjectAlertsTaskResult with status, actions, applied_count, and errors

Raises:
    HTTPException:
        - 404 Not Found: Task ID not found
        - 408 Request Timeout: Task still pending after timeout (blocking mode only)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.integrations.glitchtip_project_alerts_task_status(
    task_id="task_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**timeout:** `typing.Optional[int]` — Optional: Block up to N seconds for completion. Omit for immediate status check.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/fern/integrations/client.py">glitchtip</a>(...) -> GlitchtipTaskResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Queue Glitchtip reconciliation task.

This endpoint always queues a background task and returns immediately
with a task_id. Use GET /reconcile/{task_id} to retrieve the result.

Args:
    reconcile_request: Reconciliation request with desired state
    current_user: Authenticated user (from JWT token)
    request: FastAPI Request object (used to generate status_url)

Returns:
    GlitchtipTaskResponse with task_id and status_url
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GiInstance, Secret

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.integrations.glitchtip(
    instances=[
        GiInstance(
            automation_user_email=Secret(
                path="path",
                secret_manager_url="secret_manager_url",
            ),
            console_url="console_url",
            name="name",
            token=Secret(
                path="path",
                secret_manager_url="secret_manager_url",
            ),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**instances:** `typing.List[GiInstance]` — List of Glitchtip instances to reconcile
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — If True, only calculate actions without executing. Default: True (safety first!)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/fern/integrations/client.py">glitchtip_task_status</a>(...) -> GlitchtipTaskResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve reconciliation result (blocking or non-blocking).

**Non-blocking mode (default):** Returns immediate status
**Blocking mode (with timeout):** Waits up to timeout seconds

Args:
    task_id: Task ID from POST /reconcile response
    current_user: Authenticated user (from JWT token)
    timeout: Maximum seconds to wait (default: None = non-blocking)

Returns:
    GlitchtipTaskResult with status, actions, applied_count, and errors
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.integrations.glitchtip_task_status(
    task_id="task_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**timeout:** `typing.Optional[int]` — Optional: Block up to N seconds for completion. Omit for immediate status check.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/fern/integrations/client.py">managed_sso_client</a>(...) -> ManagedSsoClientTaskResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Queue a managed-sso-client reconciliation task.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ManagedSsoClientDesiredState, KeycloakInstanceRef, Secret

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.integrations.managed_sso_client(
    desired_clients=[
        ManagedSsoClientDesiredState(
            client_id="client_id",
            keycloak_instance=KeycloakInstanceRef(
                initial_access_token=Secret(
                    path="path",
                    secret_manager_url="secret_manager_url",
                ),
                url="url",
            ),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**desired_clients:** `typing.List[ManagedSsoClientDesiredState]` — All tenant-declared managed SSO clients across app-interface
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — If True, only calculate actions without executing. Default: True (safety first!)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/fern/integrations/client.py">managed_sso_client_task_status</a>(...) -> ManagedSsoClientTaskResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the reconciliation result (blocking or non-blocking).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.integrations.managed_sso_client_task_status(
    task_id="task_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**timeout:** `typing.Optional[int]` — Optional: Block up to N seconds for completion. Omit for immediate status check.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/fern/integrations/client.py">ocm_groups</a>(...) -> OcmGroupsTaskResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Queue OCM groups reconciliation task.

This endpoint always queues a background task and returns immediately with a
task_id. Use GET /reconcile/{task_id} to retrieve the result.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, OcmGroupsCluster, OcmGroupUser, OcmConnectionParams

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.integrations.ocm_groups(
    clusters=[
        OcmGroupsCluster(
            cluster_id="cluster_id",
            name="name",
        )
    ],
    desired_state=[
        OcmGroupUser(
            cluster="cluster",
            group="group",
            user="user",
        )
    ],
    ocm_connection=OcmConnectionParams(
        access_token_client_id="access_token_client_id",
        access_token_url="access_token_url",
        ocm_url="ocm_url",
        path="path",
        secret_manager_url="secret_manager_url",
    ),
    ocm_environment="ocm_environment",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**clusters:** `typing.List[OcmGroupsCluster]` — Clusters with their managed groups
    
</dd>
</dl>

<dl>
<dd>

**desired_state:** `typing.List[OcmGroupUser]` — Desired group memberships (from GraphQL roles)
    
</dd>
</dl>

<dl>
<dd>

**ocm_connection:** `OcmConnectionParams` — OCM connection details for cluster group CRUD
    
</dd>
</dl>

<dl>
<dd>

**ocm_environment:** `str` — OCM environment name (metric label only)
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — If True, only calculate actions without executing. Default: True (safety first!)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/fern/integrations/client.py">ocm_groups_task_status</a>(...) -> OcmGroupsTaskResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve reconciliation result (blocking or non-blocking).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.integrations.ocm_groups_task_status(
    task_id="task_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**timeout:** `typing.Optional[int]` — Optional: Block up to N seconds for completion. Omit for immediate status check.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/fern/integrations/client.py">ocm_oidc_idp</a>(...) -> OcmOidcIdpTaskResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Queue OCM OIDC identity provider reconciliation task.

This endpoint always queues a background task and returns immediately with a
task_id. Use GET /reconcile/{task_id} to retrieve the result.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, OcmOidcIdpCluster, OcmOidcIdpAuth, OcmConnectionParams, Secret

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.integrations.ocm_oidc_idp(
    clusters=[
        OcmOidcIdpCluster(
            auth=OcmOidcIdpAuth(
                enforced=True,
                issuer="issuer",
                name="name",
                oidc_enabled=True,
            ),
            cluster_id="cluster_id",
            name="name",
            organization_id="organization_id",
        )
    ],
    ocm_connection=OcmConnectionParams(
        access_token_client_id="access_token_client_id",
        access_token_url="access_token_url",
        ocm_url="ocm_url",
        path="path",
        secret_manager_url="secret_manager_url",
    ),
    ocm_environment="ocm_environment",
    vault_target=Secret(
        path="path",
        secret_manager_url="secret_manager_url",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**clusters:** `typing.List[OcmOidcIdpCluster]` — All RHIDP-labeled clusters discovered for this environment
    
</dd>
</dl>

<dl>
<dd>

**ocm_connection:** `OcmConnectionParams` — OCM connection details, needed for identity provider CRUD
    
</dd>
</dl>

<dl>
<dd>

**ocm_environment:** `str` — OCM environment name (metric label only)
    
</dd>
</dl>

<dl>
<dd>

**vault_target:** `Secret` — Vault location sso_client stores per-cluster SSO client secrets under (field/version unused)
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — If True, only calculate actions without executing. Default: True (safety first!)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/fern/integrations/client.py">ocm_oidc_idp_task_status</a>(...) -> OcmOidcIdpTaskResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve reconciliation result (blocking or non-blocking).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.integrations.ocm_oidc_idp_task_status(
    task_id="task_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**timeout:** `typing.Optional[int]` — Optional: Block up to N seconds for completion. Omit for immediate status check.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/fern/integrations/client.py">openshift_namespaces</a>(...) -> OpenShiftNamespacesTaskResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Queue openshift-namespaces reconciliation task.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ClusterNamespaces, Secret

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.integrations.openshift_namespaces(
    clusters=[
        ClusterNamespaces(
            automation_token=Secret(
                path="path",
                secret_manager_url="secret_manager_url",
            ),
            cluster_name="cluster_name",
            server_url="server_url",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**clusters:** `typing.List[ClusterNamespaces]` — Clusters with desired namespaces
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — If True, only calculate actions without executing
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/fern/integrations/client.py">openshift_namespaces_task_status</a>(...) -> OpenShiftNamespacesTaskResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve reconciliation result (blocking or non-blocking).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.integrations.openshift_namespaces_task_status(
    task_id="task_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**timeout:** `typing.Optional[int]` — Optional: Block up to N seconds for completion.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/fern/integrations/client.py">quay_repos</a>(...) -> QuayReposTaskResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Queue Quay repos reconciliation task.

Always queues a background task and returns immediately with a task_id.
Use GET /reconcile/{task_id} to retrieve the result.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, QuayOrgConfig, Secret

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.integrations.quay_repos(
    orgs=[
        QuayOrgConfig(
            automation_token=Secret(
                path="path",
                secret_manager_url="secret_manager_url",
            ),
            base_url="base_url",
            instance="instance",
            managed_repos=True,
            org_name="org_name",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**orgs:** `typing.List[QuayOrgConfig]` — List of Quay organizations to reconcile
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — If True, only calculate actions without executing. Default: True (safety first!)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/fern/integrations/client.py">quay_repos_task_status</a>(...) -> QuayReposTaskResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve reconciliation result (blocking or non-blocking).

Args:
    task_id: Task ID from POST /reconcile response
    timeout: Maximum seconds to wait (default: non-blocking)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.integrations.quay_repos_task_status(
    task_id="task_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**timeout:** `typing.Optional[int]` — Optional: Block up to N seconds for completion. Omit for immediate status check.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/fern/integrations/client.py">quay_robot_accounts</a>(...) -> QuayRobotAccountsTaskResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Queue a quay-robot-accounts reconciliation task.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, QuayOrgDesiredState, Secret

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.integrations.quay_robot_accounts(
    organizations=[
        QuayOrgDesiredState(
            instance_name="instance_name",
            instance_url="instance_url",
            org_name="org_name",
            token=Secret(
                path="path",
                secret_manager_url="secret_manager_url",
            ),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organizations:** `typing.List[QuayOrgDesiredState]` — Quay organizations with desired robot-account state
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — If True, only calculate actions without executing. Default: True (safety first!)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/fern/integrations/client.py">quay_robot_accounts_task_status</a>(...) -> QuayRobotAccountsTaskResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the reconciliation result (blocking or non-blocking).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.integrations.quay_robot_accounts_task_status(
    task_id="task_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**timeout:** `typing.Optional[int]` — Optional: Block up to N seconds for completion. Omit for immediate status check.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/fern/integrations/client.py">slack_usergroups</a>(...) -> SlackUsergroupsTaskResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Queue Slack usergroups reconciliation task.

This endpoint always queues a background task and returns immediately
with a task_id. Use GET /reconcile/{task_id} to retrieve the result.

Args:
    reconcile_request: Reconciliation request with desired state
    current_user: Authenticated user (from JWT token)
    request: FastAPI Request object (used to generate status_url)

Returns:
    SlackUsergroupsTaskResponse with task_id and status_url
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SlackWorkspace, Secret, SlackUsergroup, SlackUsergroupConfig

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.integrations.slack_usergroups(
    workspaces=[
        SlackWorkspace(
            managed_usergroups=[
                "managed_usergroups"
            ],
            name="name",
            token=Secret(
                path="path",
                secret_manager_url="secret_manager_url",
            ),
            usergroups=[
                SlackUsergroup(
                    config=SlackUsergroupConfig(),
                    handle="handle",
                )
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workspaces:** `typing.List[SlackWorkspace]` — List of Slack workspaces with their usergroups
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — If True, only calculate actions without executing. Default: True (safety first!)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/fern/integrations/client.py">slack_usergroups_task_status</a>(...) -> SlackUsergroupsTaskResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve reconciliation result (blocking or non-blocking).

**Non-blocking mode (default):** Returns immediate status (pending/success/failed)
**Blocking mode (with timeout):** Waits up to timeout seconds, returns 408 if still pending

Args:
    task_id: Task ID from POST /reconcile response
    current_user: Authenticated user (from JWT token)
    timeout: Maximum seconds to wait (default: None = non-blocking)

Returns:
    SlackUsergroupsTaskResult with status, actions, applied_count, and errors

Raises:
    HTTPException:
        - 404 Not Found: Task ID not found
        - 408 Request Timeout: Task still pending after timeout (blocking mode only)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.integrations.slack_usergroups_task_status(
    task_id="task_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**timeout:** `typing.Optional[int]` — Optional: Block up to N seconds for completion. Omit for immediate status check.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/fern/integrations/client.py">sso_client</a>(...) -> SsoClientTaskResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Queue RHIDP SSO client reconciliation task.

This endpoint always queues a background task and returns immediately with a
task_id. Use GET /reconcile/{task_id} to retrieve the result.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SsoClientCluster, SsoClientAuth, KeycloakInstanceSecret, Secret

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.integrations.sso_client(
    clusters=[
        SsoClientCluster(
            auth=SsoClientAuth(
                issuer="issuer",
                name="name",
            ),
            name="name",
            organization_id="organization_id",
            rhidp_enabled=True,
        )
    ],
    keycloak_secrets=[
        KeycloakInstanceSecret(
            secret=Secret(
                path="path",
                secret_manager_url="secret_manager_url",
            ),
            url="url",
        )
    ],
    ocm_environment="ocm_environment",
    vault_target=Secret(
        path="path",
        secret_manager_url="secret_manager_url",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**clusters:** `typing.List[SsoClientCluster]` — All RHIDP-labeled clusters discovered for this environment
    
</dd>
</dl>

<dl>
<dd>

**keycloak_secrets:** `typing.List[KeycloakInstanceSecret]` — One entry per Keycloak instance (issuer URL + its Vault IAT secret reference)
    
</dd>
</dl>

<dl>
<dd>

**ocm_environment:** `str` — OCM environment name (metric label only)
    
</dd>
</dl>

<dl>
<dd>

**vault_target:** `Secret` — Vault location to store/list/delete SSO client secrets under (field/version unused)
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — If True, only calculate actions without executing. Default: True (safety first!)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/fern/integrations/client.py">sso_client_task_status</a>(...) -> SsoClientTaskResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve reconciliation result (blocking or non-blocking).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.integrations.sso_client_task_status(
    task_id="task_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**timeout:** `typing.Optional[int]` — Optional: Block up to N seconds for completion. Omit for immediate status check.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Health
<details><summary><code>client.health.<a href="src/fern/health/client.py">liveness</a>() -> typing.Dict[str, str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Liveness probe - returns 200 if service is running.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.health.liveness()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.health.<a href="src/fern/health/client.py">readiness</a>() -> HealthResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Readiness probe - returns 200 if service is ready to accept requests.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.health.readiness()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

