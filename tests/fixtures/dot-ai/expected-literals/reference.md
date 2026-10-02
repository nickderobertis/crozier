# Reference
## McpProtocol
<details><summary><code>client.mcp_protocol.<a href="src/fern/mcp_protocol/client.py">open_mcp_sse_stream</a>() -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Opens a Server-Sent Events (SSE) stream for Model Context Protocol communication. This endpoint allows the server to push messages to the client without the client first sending data.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.mcp_protocol.open_mcp_sse_stream()

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

<details><summary><code>client.mcp_protocol.<a href="src/fern/mcp_protocol/client.py">send_mcp_json_rpc_message</a>(...) -> McpJsonRpcResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send a JSON-RPC message using Model Context Protocol. Used for tool calls, initialization, and other MCP operations. The server may respond with either a JSON object or open an SSE stream.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.mcp_protocol.send_mcp_json_rpc_message(
    jsonrpc="2.0",
    id=1,
    method="initialize",
    params={
        "protocolVersion": "2024-11-05",
        "capabilities": {},
        "clientInfo": {"name": "example-client", "version": "1.0.0"}
    },
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

**jsonrpc:** `McpJsonRpcRequestJsonrpc` — JSON-RPC version
    
</dd>
</dl>

<dl>
<dd>

**method:** `str` — Method name (e.g., initialize, tools/call, tools/list)
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[McpJsonRpcRequestId]` — Request identifier
    
</dd>
</dl>

<dl>
<dd>

**params:** `typing.Optional[typing.Dict[str, typing.Any]]` — Method parameters
    
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

## Intelligence
<details><summary><code>client.intelligence.<a href="src/fern/intelligence/client.py">execute_impact_analysis_tool</a>(...) -> ToolExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Analyze the blast radius of a proposed Kubernetes operation. Accepts free-text input: kubectl commands (e.g., "kubectl delete pvc data-postgres-0 -n production"), YAML manifests, or plain-English descriptions (e.g., "what happens if I delete the postgres database?"). Returns whether the operation is safe and a detailed dependency analysis with confidence levels.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.intelligence.execute_impact_analysis_tool(
    input="example input",
    interaction_id="example interaction_id",
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

**input:** `str` — The operation to analyze. Accepts kubectl commands, YAML manifests, or plain-English descriptions.
    
</dd>
</dl>

<dl>
<dd>

**interaction_id:** `typing.Optional[str]` — INTERNAL ONLY - Do not populate. Used for evaluation dataset generation.
    
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

<details><summary><code>client.intelligence.<a href="src/fern/intelligence/client.py">execute_query_tool</a>(...) -> ToolExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Natural language query interface for Kubernetes cluster intelligence. Ask any questions about your cluster resources, capabilities, and status in plain English. Examples: "What databases are running?", "Describe the nginx deployment", "Show me pods in the kube-system namespace", "What operators are installed?", "Is my-postgres healthy?"
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.intelligence.execute_query_tool(
    intent="deploy web application with PostgreSQL database",
    interaction_id="example interaction_id",
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

**intent:** `str` — Natural language query about the cluster
    
</dd>
</dl>

<dl>
<dd>

**interaction_id:** `typing.Optional[str]` — INTERNAL ONLY - Do not populate. Used for evaluation dataset generation.
    
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

## Knowledge
<details><summary><code>client.knowledge.<a href="src/fern/knowledge/client.py">execute_manage_knowledge_tool</a>(...) -> ToolExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the knowledge base: ingest documents, search with natural language, or delete chunks. Use "ingest" to store organizational documentation, "search" to find relevant content semantically, or "deleteByUri" to remove all chunks for a document. TIP: For complex questions, you can call search multiple times with different phrasings to gather comprehensive information before synthesizing your answer.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.knowledge.execute_manage_knowledge_tool(
    operation="ingest",
    content="example content",
    uri="example uri",
    metadata={
        "key": "value"
    },
    query="example query",
    limit=42,
    uri_filter="example uriFilter",
    interaction_id="example interaction_id",
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

**operation:** `ManageKnowledgeRequestOperation` — Operation to perform: "ingest" to add documents, "search" for semantic search, "deleteByUri" to remove all chunks for a document.
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — Document content to ingest (required for ingest operation).
    
</dd>
</dl>

<dl>
<dd>

**uri:** `typing.Optional[str]` — Full URL identifying the document (required for ingest and deleteByUri). E.g., https://github.com/org/repo/blob/main/docs/guide.md
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Optional metadata to store with chunks
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Natural language search query (required for search operation).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — Maximum number of results to return for search (default: 20).
    
</dd>
</dl>

<dl>
<dd>

**uri_filter:** `typing.Optional[str]` — Optional URL prefix to filter search results (e.g., "https://github.com/org/repo/").
    
</dd>
</dl>

<dl>
<dd>

**interaction_id:** `typing.Optional[str]` — INTERNAL ONLY - Do not populate.
    
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

<details><summary><code>client.knowledge.<a href="src/fern/knowledge/client.py">delete_all_knowledge_base_chunks_for_a_source_identifier_used_by_controller_for_git_knowledge_source_cleanup</a>(...) -> KnowledgeSourceSourceIdentifierDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete all knowledge base chunks for a source identifier. Used by controller for GitKnowledgeSource cleanup.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.knowledge.delete_all_knowledge_base_chunks_for_a_source_identifier_used_by_controller_for_git_knowledge_source_cleanup(
    source_identifier="sourceIdentifier",
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

**source_identifier:** `str` — Source identifier (e.g., namespace/name of GitKnowledgeSource CR)
    
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

<details><summary><code>client.knowledge.<a href="src/fern/knowledge/client.py">ask_a_question_and_receive_an_ai_synthesized_answer_from_the_knowledge_base_uses_an_agentic_approach_that_can_search_multiple_times_with_different_phrasings_for_comprehensive_answers</a>(...) -> KnowledgeAskPostResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ask a question and receive an AI-synthesized answer from the knowledge base. Uses an agentic approach that can search multiple times with different phrasings for comprehensive answers.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.knowledge.ask_a_question_and_receive_an_ai_synthesized_answer_from_the_knowledge_base_uses_an_agentic_approach_that_can_search_multiple_times_with_different_phrasings_for_comprehensive_answers(
    query="query",
    limit=1.1,
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

**query:** `str` — The question to answer from the knowledge base
    
</dd>
</dl>

<dl>
<dd>

**limit:** `float` — Maximum chunks to retrieve per search (default: 20)
    
</dd>
</dl>

<dl>
<dd>

**uri_filter:** `typing.Optional[str]` — Optional: filter searches to specific document URI
    
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

## Management
<details><summary><code>client.management.<a href="src/fern/management/client.py">execute_manage_org_data_tool</a>(...) -> ToolExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Tool for managing cluster resource capabilities. Supports scan, list, get, search, delete, deleteAll, and progress operations for cluster resource capability discovery and management. Use dataType="capabilities" to manage cluster capabilities. NOTE: Organizational patterns and policies are now managed via manageKnowledge tool (ingest documents, search, deleteByUri) with automatic AI classification.
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
from fern.environment import FernApiEnvironment
from fern.management import ManageOrgDataRequestResource

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.management.execute_manage_org_data_tool(
    data_type="capabilities",
    operation="list",
    session_id="example sessionId",
    step="example step",
    response="example response",
    id="example id",
    limit=42,
    identity_only=False,
    resource=ManageOrgDataRequestResource(
        kind="example kind",
        group="example group",
        api_version="example apiVersion",
    ),
    resource_list="example resourceList",
    mode="full",
    collection="example collection",
    interaction_id="example interaction_id",
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

**data_type:** `ManageOrgDataRequestDataType` — Type of cluster data to manage: "capabilities" for resource capabilities. (Note: organizational knowledge/patterns/policies are managed via manageKnowledge tool)
    
</dd>
</dl>

<dl>
<dd>

**operation:** `ManageOrgDataRequestOperation` — Operation to perform on the cluster data
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `typing.Optional[str]` — Session ID (required for continuing workflow steps, optional for progress - uses latest session if omitted)
    
</dd>
</dl>

<dl>
<dd>

**step:** `typing.Optional[str]` — Current workflow step (required when sessionId is provided)
    
</dd>
</dl>

<dl>
<dd>

**response:** `typing.Optional[str]` — User response to previous workflow step question
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — Capability ID (required for get/delete operations) or search query (required for search operations)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return (must be an integer; default: 10, maximum: 10000). The response carries an explicit truncated flag, the authoritative completeness signal; totalCount equals returnedCount when not truncated and is a best-effort figure otherwise.
    
</dd>
</dl>

<dl>
<dd>

**identity_only:** `typing.Optional[bool]` — For list: return only identity fields (id, resourceName) instead of full capability records. Keeps the payload proportional to the number of resources for machine consumers such as the controller.
    
</dd>
</dl>

<dl>
<dd>

**resource:** `typing.Optional[ManageOrgDataRequestResource]` — Kubernetes resource reference (for capabilities operations)
    
</dd>
</dl>

<dl>
<dd>

**resource_list:** `typing.Optional[str]` — Comma-separated list of resources to scan (format: Kind.group or Kind for core resources). When provided without sessionId, triggers a fire-and-forget targeted scan.
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[ManageOrgDataRequestMode]` — Scan mode: "full" triggers a fire-and-forget full cluster scan that returns immediately and scans all resources in the cluster. Mutually exclusive with resourceList.
    
</dd>
</dl>

<dl>
<dd>

**collection:** `typing.Optional[str]` — Collection name for capabilities operations (default: "capabilities", use "capabilities-policies" for pre-populated test data)
    
</dd>
</dl>

<dl>
<dd>

**interaction_id:** `typing.Optional[str]` — INTERNAL ONLY - Do not populate. Used for evaluation dataset generation.
    
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

## Operations
<details><summary><code>client.operations.<a href="src/fern/operations/client.py">execute_operate_tool</a>(...) -> ToolExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

AI-powered Kubernetes application operations tool for Day 2 operations. Handles updates, scaling, enhancements, rollbacks, and deletions through natural language intents. Analyzes current state, applies organizational patterns and policies, validates changes via dry-run, and executes approved operations safely.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.operations.execute_operate_tool(
    intent="deploy web application with PostgreSQL database",
    evidence="example evidence",
    session_id="example sessionId",
    execute_choice=42,
    refined_intent="deploy web application with PostgreSQL database",
    interaction_id="example interaction_id",
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

**intent:** `typing.Optional[str]` — What the operator is asking for, in their own words: "update X to Y", "scale Z", "make W HA", etc. This is the authoritative instruction for the operation. Telemetry, logs or manifests quoted from elsewhere belong in `evidence`, not here.
    
</dd>
</dl>

<dl>
<dd>

**evidence:** `typing.Optional[str]` — OPTIONAL. Supporting material quoted from somewhere else — log lines, events, a manifest, an alert payload — that the caller did not write themselves. It is composed into the prompt inside an untrusted-content boundary and analyzed as data; instructions appearing in it are never followed. Callers that cannot tell instruction from quoted evidence at capture time should keep sending `intent` alone, which behaves exactly as it always has.
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `typing.Optional[str]` — Session ID from previous operate call
    
</dd>
</dl>

<dl>
<dd>

**execute_choice:** `typing.Optional[float]` — Execute approved changes (1=execute)
    
</dd>
</dl>

<dl>
<dd>

**refined_intent:** `typing.Optional[str]` — Clarified intent if user wants to provide more details
    
</dd>
</dl>

<dl>
<dd>

**interaction_id:** `typing.Optional[str]` — INTERNAL ONLY - Do not populate. Used for evaluation dataset generation.
    
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

## ProjectSetup
<details><summary><code>client.project_setup.<a href="src/fern/project_setup/client.py">execute_project_setup_tool</a>(...) -> ToolExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Setup project, audit repository, or generate repository files. Use this when user wants to: setup project, audit repo, check missing files, create README, add LICENSE, generate CONTRIBUTING.md, add CI/CD workflows, initialize documentation, setup governance files. Analyzes local repositories and generates missing configuration, documentation, and governance files. Does NOT handle Kubernetes deployments - use recommend for those.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.project_setup.execute_project_setup_tool(
    step="discover",
    session_id="example sessionId",
    existing_files=[
        "example item"
    ],
    selected_scopes=[
        "example item"
    ],
    scope="example scope",
    answers={
        "key": "value"
    },
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

**step:** `typing.Optional[ProjectSetupRequestStep]` — Workflow step: "discover" (default) starts new session and returns file list, "reportScan" analyzes scan results, "generateScope" generates all files in a scope. Defaults to "discover" if omitted.
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `typing.Optional[str]` — Session ID from previous step (required for reportScan and generateScope steps)
    
</dd>
</dl>

<dl>
<dd>

**existing_files:** `typing.Optional[typing.List[str]]` — List of files that exist in the repository (required for first reportScan call, optional for subsequent calls with selectedScopes)
    
</dd>
</dl>

<dl>
<dd>

**selected_scopes:** `typing.Optional[typing.List[str]]` — Scopes user chose to setup (e.g., ["readme", "legal", "github-community"]) (required for reportScan step after initial scan)
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Scope to generate (e.g., "github-community") (required for generateScope step)
    
</dd>
</dl>

<dl>
<dd>

**answers:** `typing.Optional[typing.Dict[str, typing.Any]]` — Answers to ALL questions for the scope (required for generateScope step)
    
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

## Deployment
<details><summary><code>client.deployment.<a href="src/fern/deployment/client.py">execute_recommend_tool</a>(...) -> ToolExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deploy applications, infrastructure, and services using Kubernetes resources with AI recommendations. Supports cloud resources via operators like Crossplane, cluster management via CAPI, and traditional Kubernetes workloads. Describe what you want to deploy. Does NOT handle policy creation, organizational patterns, or resource capabilities - use manageOrgData for those.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.deployment.execute_recommend_tool(
    stage="example stage",
    intent="deploy web application with PostgreSQL database",
    final=False,
    solution_id="example solutionId",
    answers={
        "key": "value"
    },
    timeout=30,
    repo_url="https://example.com",
    target_path="example targetPath",
    branch="example branch",
    pull_request=False,
    commit_message="example commitMessage",
    author_name="example authorName",
    author_email="user@example.com",
    interaction_id="example interaction_id",
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

**stage:** `typing.Optional[str]` — Deployment workflow stage: "recommend" (default), "chooseSolution", "answerQuestion:required", "answerQuestion:basic", "answerQuestion:advanced", "answerQuestion:open", "generateManifests", "pushToGit", "deployManifests". Defaults to "recommend" if omitted.
    
</dd>
</dl>

<dl>
<dd>

**intent:** `typing.Optional[str]` — What the user wants to deploy, create, setup, install, or run on Kubernetes. Examples: "deploy web application", "create PostgreSQL database", "setup Redis cache", "install Prometheus monitoring", "configure Ingress controller", "provision storage volumes", "launch MongoDB operator", "run Node.js API", "setup CI/CD pipeline", "create load balancer", "install Grafana dashboard", "deploy React frontend"
    
</dd>
</dl>

<dl>
<dd>

**final:** `typing.Optional[bool]` — Set to true to skip intent clarification and proceed directly with recommendations. If false or omitted, the tool will analyze the intent and provide clarification questions to help improve recommendation quality.
    
</dd>
</dl>

<dl>
<dd>

**solution_id:** `typing.Optional[str]` — Solution ID for chooseSolution, answerQuestion, generateManifests, pushToGit, and deployManifests stages
    
</dd>
</dl>

<dl>
<dd>

**answers:** `typing.Optional[typing.Dict[str, typing.Any]]` — User answers for answerQuestion stage
    
</dd>
</dl>

<dl>
<dd>

**timeout:** `typing.Optional[float]` — Deployment timeout in seconds for deployManifests stage
    
</dd>
</dl>

<dl>
<dd>

**repo_url:** `typing.Optional[str]` — Git repository URL for pushToGit stage (HTTPS)
    
</dd>
</dl>

<dl>
<dd>

**target_path:** `typing.Optional[str]` — Path within repository for pushToGit stage (e.g., "apps/postgresql/")
    
</dd>
</dl>

<dl>
<dd>

**branch:** `typing.Optional[str]` — Git branch for pushToGit stage (default: main). With pullRequest: true this is the BASE branch the pull request targets, which is never written to
    
</dd>
</dl>

<dl>
<dd>

**pull_request:** `typing.Optional[bool]` — For pushToGit stage: when true, commit to a server-generated branch and open a pull request against `branch` instead of pushing to it directly. Required for repositories with branch protection. The head branch name is chosen by the server and cannot be supplied
    
</dd>
</dl>

<dl>
<dd>

**commit_message:** `typing.Optional[str]` — Commit message for pushToGit stage (also the pull request title when pullRequest: true)
    
</dd>
</dl>

<dl>
<dd>

**author_name:** `typing.Optional[str]` — Git author name for pushToGit stage (ignored when the request carries an authenticated user identity, which is then the commit author)
    
</dd>
</dl>

<dl>
<dd>

**author_email:** `typing.Optional[str]` — Git author email for pushToGit stage (ignored when the request carries an authenticated user identity, which is then the commit author)
    
</dd>
</dl>

<dl>
<dd>

**interaction_id:** `typing.Optional[str]` — INTERNAL ONLY - Do not populate. Used for evaluation dataset generation.
    
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

## Troubleshooting
<details><summary><code>client.troubleshooting.<a href="src/fern/troubleshooting/client.py">execute_remediate_tool</a>(...) -> ToolExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

AI-powered Kubernetes issue analysis that provides root cause identification and actionable remediation steps. Unlike basic kubectl commands, this tool performs multi-step investigation, correlates cluster data, and generates intelligent solutions. Use when users want to understand WHY something is broken, not just see raw status. Ideal for: troubleshooting failures, diagnosing performance issues, analyzing pod problems, investigating networking/storage issues, or any "what's wrong" questions.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.troubleshooting.execute_remediate_tool(
    issue="example issue",
    evidence="example evidence",
    mode="manual",
    confidence_threshold=42,
    max_risk_level="low",
    execute_choice=42,
    session_id="example sessionId",
    executed_commands=[
        "example item"
    ],
    interaction_id="example interaction_id",
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

**mode:** `RemediateRequestMode` — Execution mode: manual requires user approval, automatic executes based on thresholds
    
</dd>
</dl>

<dl>
<dd>

**confidence_threshold:** `float` — For automatic mode: minimum confidence required for execution (default: 0.8)
    
</dd>
</dl>

<dl>
<dd>

**max_risk_level:** `RemediateRequestMaxRiskLevel` — For automatic mode: maximum risk level allowed for execution (default: low)
    
</dd>
</dl>

<dl>
<dd>

**issue:** `typing.Optional[str]` — What the operator is asking for, in their own words. This is the authoritative instruction for the investigation. Telemetry, logs or manifests quoted from elsewhere belong in `evidence`, not here.
    
</dd>
</dl>

<dl>
<dd>

**evidence:** `typing.Optional[str]` — OPTIONAL. Supporting material quoted from somewhere else — log lines, events, a manifest, an alert payload — that the caller did not write themselves. It is composed into the prompt inside an untrusted-content boundary and analyzed as data; instructions appearing in it are never followed. Callers that cannot tell instruction from quoted evidence at capture time should keep sending `issue` alone, which behaves exactly as it always has.
    
</dd>
</dl>

<dl>
<dd>

**execute_choice:** `typing.Optional[float]` — Execute a previously generated choice (1=Execute via MCP, 2=Execute via agent)
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `typing.Optional[str]` — Session ID from previous remediate call when executing a choice
    
</dd>
</dl>

<dl>
<dd>

**executed_commands:** `typing.Optional[typing.List[str]]` — Commands that were executed to remediate the issue
    
</dd>
</dl>

<dl>
<dd>

**interaction_id:** `typing.Optional[str]` — INTERNAL ONLY - Do not populate. Used for evaluation dataset generation.
    
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

## System
<details><summary><code>client.system.<a href="src/fern/system/client.py">execute_version_tool</a>(...) -> ToolExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get comprehensive system health and diagnostics
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.system.execute_version_tool(
    interaction_id="example interaction_id",
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

**interaction_id:** `typing.Optional[str]` — INTERNAL ONLY - Do not populate. Used for evaluation dataset generation.
    
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

## Tools
<details><summary><code>client.tools.<a href="src/fern/tools/client.py">discover_available_tools_with_optional_filtering_by_category_tag_or_search_term</a>(...) -> ToolsGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Discover available tools with optional filtering by category, tag, or search term
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.tools.discover_available_tools_with_optional_filtering_by_category_tag_or_search_term()

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

**category:** `typing.Optional[str]` — Filter tools by category
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[str]` — Filter tools by tag
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search tools by name or description
    
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

<details><summary><code>client.tools.<a href="src/fern/tools/client.py">execute_a_tool_with_the_provided_parameters</a>(...) -> ToolsToolNamePostResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a tool with the provided parameters
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.tools.execute_a_tool_with_the_provided_parameters(
    tool_name="toolName",
    request={
        "key": "value"
    },
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

**tool_name:** `str` — Name of the tool to execute
    
</dd>
</dl>

<dl>
<dd>

**request:** `ToolsToolNamePostRequest` 
    
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

## Documentation
<details><summary><code>client.documentation.<a href="src/fern/documentation/client.py">get_the_open_api30specification_for_this_api</a>() -> OpenapiGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the OpenAPI 3.0 specification for this API
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.documentation.get_the_open_api30specification_for_this_api()

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

## Resources
<details><summary><code>client.resources.<a href="src/fern/resources/client.py">list_resources_filtered_by_kind_and_optional_namespace</a>(...) -> ResourcesGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List resources filtered by kind and optional namespace
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.resources.list_resources_filtered_by_kind_and_optional_namespace(
    kind="kind",
    api_version="apiVersion",
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

**kind:** `str` — Resource kind (e.g., Pod, Deployment)
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `str` — API version (e.g., v1, apps/v1)
    
</dd>
</dl>

<dl>
<dd>

**namespace:** `typing.Optional[str]` — Filter by namespace
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — Maximum results to return
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[float]` — Offset for pagination
    
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

<details><summary><code>client.resources.<a href="src/fern/resources/client.py">list_all_resource_kinds_available_in_the_cluster_with_counts</a>(...) -> ResourcesKindsGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all resource kinds available in the cluster with counts
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.resources.list_all_resource_kinds_available_in_the_cluster_with_counts()

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

**namespace:** `typing.Optional[str]` — Filter kinds by namespace
    
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

<details><summary><code>client.resources.<a href="src/fern/resources/client.py">search_for_resources_using_semantic_search</a>(...) -> ResourcesSearchGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for resources using semantic search
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.resources.search_for_resources_using_semantic_search(
    q="q",
    limit=1.1,
    offset=1.1,
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

**q:** `str` — Search query
    
</dd>
</dl>

<dl>
<dd>

**limit:** `float` — Maximum results to return
    
</dd>
</dl>

<dl>
<dd>

**offset:** `float` — Offset for pagination
    
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

<details><summary><code>client.resources.<a href="src/fern/resources/client.py">sync_resources_from_the_kubernetes_controller</a>(...) -> ResourcesSyncPostResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sync resources from the Kubernetes controller
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.resources.sync_resources_from_the_kubernetes_controller()

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

**upserts:** `typing.Optional[typing.List[typing.Dict[str, typing.Any]]]` — Resources to upsert
    
</dd>
</dl>

<dl>
<dd>

**deletes:** `typing.Optional[typing.List[typing.Dict[str, typing.Any]]]` — Resources to delete (requires namespace, name, kind, apiVersion)
    
</dd>
</dl>

<dl>
<dd>

**is_resync:** `typing.Optional[bool]` — When true, performs full reconciliation - deletes resources not in upserts list
    
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

<details><summary><code>client.resources.<a href="src/fern/resources/client.py">get_a_single_resource_with_full_details_including_live_status</a>(...) -> ResourceGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single resource with full details including live status
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.resources.get_a_single_resource_with_full_details_including_live_status(
    kind="kind",
    api_version="apiVersion",
    name="name",
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

**kind:** `str` — Resource kind
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `str` — API version
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Resource name
    
</dd>
</dl>

<dl>
<dd>

**namespace:** `typing.Optional[str]` — Namespace (for namespaced resources)
    
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

<details><summary><code>client.resources.<a href="src/fern/resources/client.py">list_all_namespaces_in_the_cluster</a>() -> NamespacesGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all namespaces in the cluster
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.resources.list_all_namespaces_in_the_cluster()

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

## Observability
<details><summary><code>client.observability.<a href="src/fern/observability/client.py">get_kubernetes_events_for_a_specific_resource</a>(...) -> EventsGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Kubernetes events for a specific resource
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.observability.get_kubernetes_events_for_a_specific_resource(
    name="name",
    kind="kind",
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

**name:** `str` — Resource name
    
</dd>
</dl>

<dl>
<dd>

**kind:** `str` — Resource kind
    
</dd>
</dl>

<dl>
<dd>

**namespace:** `typing.Optional[str]` — Resource namespace
    
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

<details><summary><code>client.observability.<a href="src/fern/observability/client.py">get_container_logs_from_a_pod</a>(...) -> LogsGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get container logs from a pod
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.observability.get_container_logs_from_a_pod(
    name="name",
    namespace="namespace",
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

**name:** `str` — Pod name
    
</dd>
</dl>

<dl>
<dd>

**namespace:** `str` — Pod namespace
    
</dd>
</dl>

<dl>
<dd>

**container:** `typing.Optional[str]` — Container name (defaults to first container)
    
</dd>
</dl>

<dl>
<dd>

**tail_lines:** `typing.Optional[float]` — Number of lines from end
    
</dd>
</dl>

<dl>
<dd>

**previous:** `typing.Optional[bool]` — Get logs from previous container instance
    
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

## Prompts
<details><summary><code>client.prompts.<a href="src/fern/prompts/client.py">list_all_available_prompts</a>(...) -> PromptsGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all available prompts
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.prompts.list_all_available_prompts()

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

**source:** `typing.Optional[str]` — Enumerate a previously-ingested (CLI-uploaded) source by its identifier with no git clone (PRD #647). An unknown/evicted identifier returns 400 with re-upload guidance. Takes precedence over repo/path/branch.
    
</dd>
</dl>

<dl>
<dd>

**repo:** `typing.Optional[str]` — Per-request git repository URL override (PRD #581)
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[str]` — Subdirectory within the override repo (PRD #621)
    
</dd>
</dl>

<dl>
<dd>

**branch:** `typing.Optional[str]` — Branch of the override repo (PRD #621)
    
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

<details><summary><code>client.prompts.<a href="src/fern/prompts/client.py">force_refresh_the_prompts_cache_by_pulling_latest_from_the_git_repository</a>() -> PromptsRefreshPostResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Force-refresh the prompts cache by pulling latest from the git repository
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.prompts.force_refresh_the_prompts_cache_by_pulling_latest_from_the_git_repository()

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

<details><summary><code>client.prompts.<a href="src/fern/prompts/client.py">ingest_upload_a_skill_source_the_server_caches_and_renders_via_post_api_v1prompts_prompt_name_source_identifier_with_no_git_clone_prd647</a>(...) -> PromptsSourcesPostResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ingest (upload) a skill source the server caches and renders via POST /api/v1/prompts/:promptName?source=<identifier> with no git clone (PRD #647)
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
from fern.environment import FernApiEnvironment
from fern.prompts import PromptsSourcesPostRequestFilesItem

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.prompts.ingest_upload_a_skill_source_the_server_caches_and_renders_via_post_api_v1prompts_prompt_name_source_identifier_with_no_git_clone_prd647(
    source="source",
    files=[
        PromptsSourcesPostRequestFilesItem(
            path="path",
            content="content",
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

**source:** `str` — Stable source identifier (e.g., "local:team-dev" or a git URL the server cannot reach)
    
</dd>
</dl>

<dl>
<dd>

**files:** `typing.List[PromptsSourcesPostRequestFilesItem]` — Uploaded files with base64-encoded content
    
</dd>
</dl>

<dl>
<dd>

**content_hash:** `typing.Optional[str]` — CLI-computed content hash (enables future re-upload dedup)
    
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

<details><summary><code>client.prompts.<a href="src/fern/prompts/client.py">get_a_prompt_with_rendered_template_arguments</a>(...) -> PromptsPromptNamePostResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a prompt with rendered template arguments
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.prompts.get_a_prompt_with_rendered_template_arguments(
    prompt_name="promptName",
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

**prompt_name:** `str` — Name of the prompt
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[str]` — Render a previously-ingested (CLI-uploaded) source by its identifier with no git clone (PRD #647). Takes precedence over repo/path/branch.
    
</dd>
</dl>

<dl>
<dd>

**repo:** `typing.Optional[str]` — Per-request git repository URL override (PRD #581)
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[str]` — Subdirectory within the override repo (PRD #621)
    
</dd>
</dl>

<dl>
<dd>

**branch:** `typing.Optional[str]` — Branch of the override repo (PRD #621)
    
</dd>
</dl>

<dl>
<dd>

**arguments:** `typing.Optional[typing.Dict[str, typing.Any]]` — Arguments to pass to the prompt
    
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

## Visualization
<details><summary><code>client.visualization.<a href="src/fern/visualization/client.py">get_structured_visualization_data_for_a_session</a>(...) -> VisualizeSessionIdGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get structured visualization data for a session
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.visualization.get_structured_visualization_data_for_a_session(
    session_id="sessionId",
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

**session_id:** `str` — Session ID
    
</dd>
</dl>

<dl>
<dd>

**reload:** `typing.Optional[bool]` — Force regeneration of visualization
    
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

## Sessions
<details><summary><code>client.sessions.<a href="src/fern/sessions/client.py">list_sessions_with_optional_status_filtering_and_pagination</a>(...) -> SessionsGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List sessions with optional status filtering and pagination
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.sessions.list_sessions_with_optional_status_filtering_and_pagination(
    limit=1,
    offset=1,
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

**limit:** `int` — Max results per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `int` — Pagination offset
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — Filter by session status (e.g., analysis_complete, failed, investigating)
    
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

<details><summary><code>client.sessions.<a href="src/fern/sessions/client.py">get_raw_session_data_for_any_tool_type_remediate_query_recommend_etc</a>(...) -> SessionsSessionIdGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get raw session data for any tool type (remediate, query, recommend, etc.)
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.sessions.get_raw_session_data_for_any_tool_type_remediate_query_recommend_etc(
    session_id="sessionId",
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

**session_id:** `str` — Session ID
    
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

<details><summary><code>client.sessions.<a href="src/fern/sessions/client.py">sse_stream_for_real_time_remediation_session_events_returns_text_event_stream</a>() -> EventsRemediationsGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

SSE stream for real-time remediation session events. Returns text/event-stream.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.sessions.sse_stream_for_real_time_remediation_session_events_returns_text_event_stream()

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

## Embeddings
<details><summary><code>client.embeddings.<a href="src/fern/embeddings/client.py">migrate_embedding_vectors_when_switching_between_embedding_providers_re_embeds_all_data_using_the_current_provider</a>(...) -> EmbeddingsMigratePostResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Migrate embedding vectors when switching between embedding providers. Re-embeds all data using the current provider.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.embeddings.migrate_embedding_vectors_when_switching_between_embedding_providers_re_embeds_all_data_using_the_current_provider()

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

**collection:** `typing.Optional[str]` — Collection name to migrate. If omitted, migrates all collections.
    
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

## Users
<details><summary><code>client.users.<a href="src/fern/users/client.py">list_all_dex_static_users_emails_only</a>() -> UsersGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all Dex static users (emails only)
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.users.list_all_dex_static_users_emails_only()

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

<details><summary><code>client.users.<a href="src/fern/users/client.py">create_a_new_dex_static_user</a>(...) -> UsersPostResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new Dex static user
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.users.create_a_new_dex_static_user(
    email="email",
    password="password",
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

**email:** `str` — User email address
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` — User password (minimum 8 characters)
    
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

<details><summary><code>client.users.<a href="src/fern/users/client.py">delete_a_dex_static_user_by_email</a>(...) -> UsersEmailDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a Dex static user by email
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.users.delete_a_dex_static_user_by_email(
    email="email",
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

**email:** `str` — User email address
    
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

