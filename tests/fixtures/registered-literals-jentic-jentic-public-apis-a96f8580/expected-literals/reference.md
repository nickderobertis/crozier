# Reference
## Workflows
<details><summary><code>client.workflows.<a href="src/fern/workflows/client.py">listall</a>(...) -> WorkflowsListAllResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all workflows in your Ironclad account.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.workflows.listall(
    filter="Equals([counterpartyName], \'Harley Quinn\')",
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

**page:** `typing.Optional[int]` — The page number used when paginating through a list of results.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — A limit of the number of results to return.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[WorkflowsListAllRequestStatus]` — Filter the workflows that are listed based on their status. If this parameter is omitted, `active` workflows will be returned. Active workflows include workflows in the Create, Review, Sign, and Archive stages.
    
</dd>
</dl>

<dl>
<dd>

**template:** `typing.Optional[str]` — Filter workflows to a specific Template ID.
    
</dd>
</dl>

<dl>
<dd>

**last_updated:** `typing.Optional[str]` — Retrieve workflows that have been updated since a UTC date.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` 

Filter workflows using a formula. The workflow attribute ID should be enclosed in brackets `[ ]` and the value should be enclosed in single quotes `' '`.

Workflow attributes for a specific workflow design can be identified using the [List All Workflow Schemas](https://developer.ironcladapp.com/reference/list-all-workflow-schemas) endpoint.

Supported formula operations include:

<ul>
  <li><code>Equals</code></li>
  <li><code>Contains</code></li>
  <li><code>And</code></li>
  <li><code>Or</code></li>
</ul>
For more information on writing formulas, please refer to
<a href="https://ironcladapp.com/formulas/#company%20display%20name">this article</a>.
    
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

<details><summary><code>client.workflows.<a href="src/fern/workflows/client.py">createsyncworkflow</a>(...) -> LaunchedWorkflowModel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Launch a new Workflow synchronously.
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
from fern import FernApi, CreatorEmailModel, AttributesModel
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.workflows.createsyncworkflow(
    template="600b296c3e15a234ab88f884",
    creator=CreatorEmailModel(),
    attributes=AttributesModel(
        counterparty_name="Example Company",
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

**request:** `WorkflowRequestModel` 
    
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

<details><summary><code>client.workflows.<a href="src/fern/workflows/client.py">launchasynchronously</a>(...) -> WorkflowsLaunchAsynchronouslyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Launch a new Workflow asynchronously for non-blocking performance, which is helpful when/if you provide files to the Workflow.
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
from fern import FernApi, CreatorEmailModel, AttributesModel
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.workflows.launchasynchronously(
    template="600b296c3e15a234ab88f884",
    creator=CreatorEmailModel(),
    attributes=AttributesModel(
        counterparty_name="Example Company",
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

**request:** `WorkflowRequestModel` 
    
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

<details><summary><code>client.workflows.<a href="src/fern/workflows/client.py">getasyncjobstatus</a>(...) -> WorkflowsGetAsyncJobStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check the status of a Workflow you created while using the [Create a Workflow Async](https://developer.ironcladapp.com/reference/create-a-workflow-sync-vs-async#create-a-new-workflow-async) route.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.workflows.getasyncjobstatus(
    async_job_id="asyncJobId",
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

**async_job_id:** `str` — The identifier provided in the response of creating a Workflow asynchronously.
    
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

<details><summary><code>client.workflows.<a href="src/fern/workflows/client.py">getworkflow</a>(...) -> WorkflowResponseModel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

View the data associated with a specific workflow
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.workflows.getworkflow(
    id="abcd1234",
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

**id:** `str` — The unique identifier or Ironclad ID of a workflow.
    
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

<details><summary><code>client.workflows.<a href="src/fern/workflows/client.py">listapprovals</a>(...) -> WorkflowsListApprovalsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of approvals for the workflow. The `approvalGroups` property will display only triggered approvals (i.e. conditional approvals that have not been triggered will not appear).
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.workflows.listapprovals(
    id="abcd1234",
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

**id:** `str` — The unique identifier or Ironclad ID of a workflow.
    
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

<details><summary><code>client.workflows.<a href="src/fern/workflows/client.py">getapprovalrequests</a>(...) -> WorkflowsGetApprovalRequestsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of approval requests that have taken place on the workflow.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.workflows.getapprovalrequests(
    id="id",
    actor_details=False,
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

**id:** `str` — The unique identifier or Ironclad ID of a workflow.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number used when paginating through a list of results.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — A limit of the number of results to return.
    
</dd>
</dl>

<dl>
<dd>

**actor_details:** `typing.Optional[bool]` — An optional boolean parameter that adds additional information about the actor to each item in the response. Defaults to false.
    
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

<details><summary><code>client.workflows.<a href="src/fern/workflows/client.py">updateapprovalstatus</a>(...) -> WorkflowsUpdateApprovalStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an approval to the specified status. Approvals can only be updated during the Review step.
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
from fern.workflows import WorkflowsUpdateApprovalStatusRequestUser

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.workflows.updateapprovalstatus(
    id="abcd1234",
    role_id="roleId",
    user=WorkflowsUpdateApprovalStatusRequestUser(),
    status="approved",
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

**id:** `str` — The unique identifier or Ironclad ID of a workflow.
    
</dd>
</dl>

<dl>
<dd>

**role_id:** `str` — The unique identifier of the approver role whose status should be changed. This identifier can be retrieved using the `GET /workflows/{id}/approvals` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**user:** `WorkflowsUpdateApprovalStatusRequestUser` — The Ironclad user approving the workflow. The user must be currently assigned as the approver.
    
</dd>
</dl>

<dl>
<dd>

**status:** `WorkflowsUpdateApprovalStatusRequestStatus` — The new approval status.
    
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

<details><summary><code>client.workflows.<a href="src/fern/workflows/client.py">getturnhistory</a>(...) -> WorkflowsGetTurnHistoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

An array of objects for each turn on a workflow.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.workflows.getturnhistory(
    id="id",
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

**id:** `str` — The unique identifier or Ironclad ID of a workflow.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number used when paginating through a list of results.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — A limit of the number of results to return.
    
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

<details><summary><code>client.workflows.<a href="src/fern/workflows/client.py">listsignatures</a>(...) -> WorkflowsListSignaturesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of workflow signers and the status of their signature.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.workflows.listsignatures(
    id="id",
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

**id:** `str` — The unique identifier or Ironclad ID of a workflow.
    
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

<details><summary><code>client.workflows.<a href="src/fern/workflows/client.py">listallparticipants</a>(...) -> WorkflowsListAllParticipantsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of workflow participants.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.workflows.listallparticipants(
    id="id",
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

**id:** `str` — The unique identifier or Ironclad ID of a workflow.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number used when paginating through a list of results.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — A limit of the number of results to return.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — The Ironclad user's email address.
    
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

<details><summary><code>client.workflows.<a href="src/fern/workflows/client.py">reverttoreview</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reverts a workflow to the Review step. Only workflows sourced from Workflow Designer and in the Sign step can be reverted.
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
from fern.workflows import WorkflowsRevertToReviewRequestUser

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.workflows.reverttoreview(
    id="id",
    as_user_email="jane.doe@test.com",
    as_user_id="5f0375c4cdc1927a3c5edcd3",
    user=WorkflowsRevertToReviewRequestUser(),
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

**id:** `str` — The unique identifier or Ironclad ID of a workflow.
    
</dd>
</dl>

<dl>
<dd>

**user:** `WorkflowsRevertToReviewRequestUser` — The Ironclad user reverting the workflow to the Review step. The user must be a participant on the workflow.
    
</dd>
</dl>

<dl>
<dd>

**as_user_email:** `typing.Optional[str]` — Filters the list of workflow schemas based on the permissions of a user associated with the specified user email. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions
    
</dd>
</dl>

<dl>
<dd>

**as_user_id:** `typing.Optional[str]` — Filters the list of workflow schemas based on the permissions of a user associated with the specified user id. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions
    
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

<details><summary><code>client.workflows.<a href="src/fern/workflows/client.py">createcomment</a>(...) -> BaseActivityFeedItemModel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a comment in the specified workflow's activity feed.
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
from fern import FernApi, CreatorEmailModel
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.workflows.createcomment(
    id="id",
    creator=CreatorEmailModel(),
    comment="comment",
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

**id:** `str` — The unique identifier or Ironclad ID of a workflow.
    
</dd>
</dl>

<dl>
<dd>

**creator:** `CreatorEmailModel` 
    
</dd>
</dl>

<dl>
<dd>

**comment:** `str` — The comment text to add, accepts user mentions in the form of <@user_id_or_email>.
    
</dd>
</dl>

<dl>
<dd>

**add_users_to_workflow:** `typing.Optional[bool]` — Must be set to true if mentioning users who are not participants on the workflow.
    
</dd>
</dl>

<dl>
<dd>

**replied_to_activity_feed_message_id:** `typing.Optional[str]` — Use to specify the comment to reply to
    
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

<details><summary><code>client.workflows.<a href="src/fern/workflows/client.py">updatemetadata</a>(...) -> WorkflowsUpdateMetadataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The workflow must be in the Review step in order for its data to be updated. Use the `remove` action to clear field values and the `set` action to add or modify values. Form validation is enforced; required fields cannot be removed and any required fields triggered by conditions must be populated.
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
from fern.workflows import WorkflowsUpdateMetadataRequestUpdatesItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.workflows.updatemetadata(
    id="id",
    as_user_email="jane.doe@test.com",
    as_user_id="5f0375c4cdc1927a3c5edcd3",
    updates=[
        WorkflowsUpdateMetadataRequestUpdatesItem(
            action="set",
            path="counterpartyName",
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

**id:** `str` — The unique identifier or Ironclad ID of a workflow.
    
</dd>
</dl>

<dl>
<dd>

**updates:** `typing.List[WorkflowsUpdateMetadataRequestUpdatesItem]` 
    
</dd>
</dl>

<dl>
<dd>

**as_user_email:** `typing.Optional[str]` — Filters the list of workflow schemas based on the permissions of a user associated with the specified user email. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions
    
</dd>
</dl>

<dl>
<dd>

**as_user_id:** `typing.Optional[str]` — Filters the list of workflow schemas based on the permissions of a user associated with the specified user id. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions
    
</dd>
</dl>

<dl>
<dd>

**comment:** `typing.Optional[str]` — A comment that explains the updates you are making to the workflow.
    
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

<details><summary><code>client.workflows.<a href="src/fern/workflows/client.py">getdocumentbykey</a>(...) -> WorkflowsGetDocumentByKeyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download a document associated with a specific workflow via a reference to its document key
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.workflows.getdocumentbykey(
    id="id",
    key="key",
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

**id:** `str` — The unique identifier or Ironclad ID of a workflow.
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — The unique identifier for the attachment. This key can be located using the [Retrieve a Workflow](https://developer.ironcladapp.com/reference/retrieve-a-workflow) endpoint. In the response, locate the file attribute (e.g., `draft`) and look at its `download` parameter. The download parameter includes the key at the end of the URL `.../document/{ATTACHMENT_KEY}/download`
    
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

<details><summary><code>client.workflows.<a href="src/fern/workflows/client.py">getemailthreads</a>(...) -> WorkflowsGetEmailThreadsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all email threads in the specified workflow
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.workflows.getemailthreads(
    id="id",
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

**id:** `str` — The unique identifier of a workflow
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number used when paginating through a list of results.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — A limit of the number of results to return.
    
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

<details><summary><code>client.workflows.<a href="src/fern/workflows/client.py">getemailthread</a>(...) -> EmailResponseModel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List a single email thread for a specified workflow
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.workflows.getemailthread(
    id="id",
    email_thread_id="emailThreadId",
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

**id:** `str` — The unique identifier of a workflow
    
</dd>
</dl>

<dl>
<dd>

**email_thread_id:** `str` — The unique identifier of an email thread
    
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

<details><summary><code>client.workflows.<a href="src/fern/workflows/client.py">getattachmentfromemailthread</a>(...) -> WorkflowsGetAttachmentFromEmailThreadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve an attachment from the specified email thread
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.workflows.getattachmentfromemailthread(
    id="id",
    email_thread_id="emailThreadId",
    attachment_id="attachmentId",
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

**id:** `str` — The unique identifier of a workflow
    
</dd>
</dl>

<dl>
<dd>

**email_thread_id:** `str` — The unique identifier of an email thread
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `str` — The unique identifier for the attachment. This key can be located using the [Retrieve email threads from workflow](https://developer.ironcladapp.com/reference/retrieve-emails) endpoint. In the response, locate the file attribute (e.g., `attachments`) and look at its `download` parameter. The download parameter includes the key at the end of the URL `...emails/{emailThreadId}/attachment/{ATTACHMENT_ID}`
    
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

<details><summary><code>client.workflows.<a href="src/fern/workflows/client.py">listallworkflowschemas</a>(...) -> WorkflowsListAllWorkflowSchemasResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of workflow schemas. Each schema specifies the fields used in the workflow's launch form.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.workflows.listallworkflowschemas(
    form="form",
    as_user_email="jane.doe@test.com",
    as_user_id="5f0375c4cdc1927a3c5edcd3",
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

**form:** `str` — The launch form is the only form supported at this time.
    
</dd>
</dl>

<dl>
<dd>

**as_user_email:** `typing.Optional[str]` — Filters the list of workflow schemas based on the permissions of a user associated with the specified user email. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions
    
</dd>
</dl>

<dl>
<dd>

**as_user_id:** `typing.Optional[str]` — Filters the list of workflow schemas based on the permissions of a user associated with the specified user id. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions
    
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

<details><summary><code>client.workflows.<a href="src/fern/workflows/client.py">getworkflowschema</a>(...) -> WorkflowsGetWorkflowSchemaResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the fields used in the workflow's launch form.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.workflows.getworkflowschema(
    id="id",
    as_user_email="jane.doe@test.com",
    as_user_id="5f0375c4cdc1927a3c5edcd3",
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

**id:** `str` — The unique identifier of a schema (see explanation of [Template ID](https://developer.ironcladapp.com/reference/getting-started-api)). A list of identifiers can be retrieved using the `GET /workflow-schemas` endpoint. Only published workflows will have an identifier. 
    
</dd>
</dl>

<dl>
<dd>

**form:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**as_user_email:** `typing.Optional[str]` — Filters the list of workflow schemas based on the permissions of a user associated with the specified user email. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions
    
</dd>
</dl>

<dl>
<dd>

**as_user_id:** `typing.Optional[str]` — Filters the list of workflow schemas based on the permissions of a user associated with the specified user id. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions
    
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

## Records
<details><summary><code>client.records.<a href="src/fern/records/client.py">listall</a>(...) -> RecordsListAllResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

View all records in the company, with filtering available via query parameters
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.records.listall(
    types="mutualNDA,consultingAgreement",
    last_updated="2018-03-10T00:00:00.000Z",
    filter="Equals([counterpartyName], \'Test LLC\')",
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

**page:** `typing.Optional[int]` — The page number used when paginating through a list of results.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — A limit of the number of results to return.
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[str]` — Comma separated (no spaces) record types to export. Use the [Retrieve Records Schema](https://developer.ironcladapp.com/reference/list-all-records-metadata) endpoint to retrieve a list of types.
    
</dd>
</dl>

<dl>
<dd>

**last_updated:** `typing.Optional[str]` — Get records updated since (UTC)
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` — Filter records for those that contain (1) the specified property with (2) the specified value. The record property ID should be enclosed in brackets `[ ]` and the value should be enclosed in single quotes `' '`.
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[RecordsListAllRequestSortField]` — The field to sort Records. Only one field is supported in the sort operation.
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[RecordsListAllRequestSortDirection]` — The direction the records are sorted by in correlation with the `sortField`.
    
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

<details><summary><code>client.records.<a href="src/fern/records/client.py">createrecord</a>(...) -> RecordModel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a contract record by specifying its intended metadata properties
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
from fern.records import RecordsCreateRecordRequestProperties

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.records.createrecord(
    type="type",
    name="name",
    properties=RecordsCreateRecordRequestProperties(),
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

**type:** `str` — The type of record to be created. You can view available record types by retrieving records metadata.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the record.
    
</dd>
</dl>

<dl>
<dd>

**properties:** `RecordsCreateRecordRequestProperties` — Object containing key/value pairs of metadata attached to the record. The key you specify must have a value with a supported type as outlined in the Supported Property Types section.
    
</dd>
</dl>

<dl>
<dd>

**links:** `typing.Optional[typing.List[RecordPropertyLinkModel]]` 
    
</dd>
</dl>

<dl>
<dd>

**parent:** `typing.Optional[RecordsCreateRecordRequestParent]` — Object containing Record IDs or Ironclad IDs to be set as the parent of the current record.
    
</dd>
</dl>

<dl>
<dd>

**children:** `typing.Optional[typing.List[RecordPropertyLinkModel]]` — List of objects containing the Record IDs or Ironclad IDs of the records to be set as child records of the current record.
    
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

<details><summary><code>client.records.<a href="src/fern/records/client.py">getpredictions</a>(...) -> RecordsGetPredictionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve status of predictions of specific smart import record or all records in an import, one of Record Id or Import Id is required.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.records.getpredictions()

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

**record_id:** `typing.Optional[str]` — The ID of the Record for prediction status.
    
</dd>
</dl>

<dl>
<dd>

**import_id:** `typing.Optional[str]` — The ID of the Import for prediction statuses.
    
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

<details><summary><code>client.records.<a href="src/fern/records/client.py">uploadsmartimportrecord</a>(...) -> RecordsUploadSmartImportRecordResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a file to create a record with smart import and predictions.  Provide none of recordType, newRecordTypeId, or newRecordTypeDisplayName to default to Imported type.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.records.uploadsmartimportrecord(
    attachment="example_attachment",
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

**attachment:** `core.File` — Must be a binary. Base64 is not accepted at this time.
    
</dd>
</dl>

<dl>
<dd>

**record_type:** `typing.Optional[str]` — Upload a smart import record as an existing record type.  Cannot provide alongside newRecordTypeId and newRecordTypeDisplayName. Defaults to Imported.
    
</dd>
</dl>

<dl>
<dd>

**new_record_type_id:** `typing.Optional[str]` — The record type ID for a not-yet-existing record type.  Must be provided along with a newRecordTypeDisplayName
    
</dd>
</dl>

<dl>
<dd>

**new_record_type_display_name:** `typing.Optional[str]` — The display name of the new record type to create.
    
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

<details><summary><code>client.records.<a href="src/fern/records/client.py">uploadsmartimportrecordwithpredictions</a>(...) -> RecordsUploadSmartImportRecordWithPredictionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a file to an existing import and create a record with smart import and predictions.  Provide none of recordType, newRecordTypeId, or newRecordTypeDisplayName to default to Imported type.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.records.uploadsmartimportrecordwithpredictions(
    import_id="importId",
    attachment="example_attachment",
    record_type="recordType",
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

**import_id:** `str` — The Import Id. You can upload a record to an existing import in the repository. 
    
</dd>
</dl>

<dl>
<dd>

**attachment:** `core.File` — Must be a binary. Base64 is not accepted at this time.
    
</dd>
</dl>

<dl>
<dd>

**record_type:** `str` — Upload a smart import record as an existing record type.  Cannot provide alongside newRecordTypeId and newRecordTypeDisplayName. Defaults to Imported.
    
</dd>
</dl>

<dl>
<dd>

**new_record_type_id:** `typing.Optional[str]` — The record type ID for a not-yet-existing record type.  Must be provided along with a newRecordTypeDisplayName
    
</dd>
</dl>

<dl>
<dd>

**new_record_type_display_name:** `typing.Optional[str]` — The display name of the new record type to create.
    
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

<details><summary><code>client.records.<a href="src/fern/records/client.py">getrecorddata</a>(...) -> RecordModel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

View a specific record and its associated data
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.records.getrecorddata(
    id="id",
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

**id:** `str` — The ID or Ironclad ID of the Record.
    
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

<details><summary><code>client.records.<a href="src/fern/records/client.py">replacemetadata</a>(...) -> RecordModel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing record with a new set of metadata
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
from fern.records import RecordsReplaceMetadataRequestProperties

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.records.replacemetadata(
    id="id",
    type="type",
    name="name",
    properties=RecordsReplaceMetadataRequestProperties(),
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

**id:** `str` — The ID or Ironclad ID of the Record.
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — The type of record to be created. You can view available record types by retrieving records metadata.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the record.
    
</dd>
</dl>

<dl>
<dd>

**properties:** `RecordsReplaceMetadataRequestProperties` — Object containing key/value pairs of metadata attached to the record. The key you specify must have a value with a supported type as outlined in the Supported Property Types section.
    
</dd>
</dl>

<dl>
<dd>

**parent:** `typing.Optional[RecordsReplaceMetadataRequestParent]` — Object containing Record IDs or Ironclad IDs to be set as the parent of the current record.
    
</dd>
</dl>

<dl>
<dd>

**children:** `typing.Optional[typing.List[RecordPropertyLinkModel]]` — List of objects containing the Record IDs or Ironclad IDs of the records to be set as child records of the current record.
    
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

<details><summary><code>client.records.<a href="src/fern/records/client.py">deleterecord</a>(...) -> RecordsDeleteRecordResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an existing record
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.records.deleterecord(
    id="id",
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

**id:** `str` — The ID or Ironclad ID of the Record.
    
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

<details><summary><code>client.records.<a href="src/fern/records/client.py">updatemetadata</a>(...) -> RecordModel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update specific fields on a record
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
from fern import FernApi, RecordPropertyLinkModel
from fern.environment import FernApiEnvironment
from fern.records import RecordsUpdateMetadataRequestAddProperties, RecordsUpdateMetadataRequestAddPropertiesCounterpartyName, RecordsUpdateMetadataRequestAddPropertiesAgreementDate

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.records.updatemetadata(
    id="id",
    type="consultingAgreement",
    name="Consulting Agreement with Jane Doe",
    add_properties=RecordsUpdateMetadataRequestAddProperties(
        counterparty_name=RecordsUpdateMetadataRequestAddPropertiesCounterpartyName(
            type="string",
            value="Jane Doe",
        ),
        agreement_date=RecordsUpdateMetadataRequestAddPropertiesAgreementDate(
            type="date",
            value="2018-05-08T00:00:00-07:00",
        ),
    ),
    remove_properties=[
        "counterpartySigner"
    ],
    add_links=[
        RecordPropertyLinkModel(
            record_id="df1c2805-f5a3-4a14-9386-c28d950dff49",
        )
    ],
    remove_links=[
        RecordPropertyLinkModel(
            record_id="df1c2805-f5a3-4a14-9386-c28d950dff49",
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

**id:** `str` — The ID or Ironclad ID of the Record.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — The type of Record.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the Record.
    
</dd>
</dl>

<dl>
<dd>

**add_properties:** `typing.Optional[RecordsUpdateMetadataRequestAddProperties]` — A key:value map of properties to add. The two below are examples.
    
</dd>
</dl>

<dl>
<dd>

**remove_properties:** `typing.Optional[typing.List[str]]` — List of record property ids to be removed (e.g., ['counterpartyAddress', 'agreementExpirationDate'])
    
</dd>
</dl>

<dl>
<dd>

**add_links:** `typing.Optional[typing.List[RecordPropertyLinkModel]]` — List of objects containing the Record IDs or Ironclad IDs of the records to link. For an explanation of Record IDs or Ironclad IDs and how to find them, see [Getting Started](https://developer.ironcladapp.com/reference/getting-started-api).
    
</dd>
</dl>

<dl>
<dd>

**remove_links:** `typing.Optional[typing.List[RecordPropertyLinkModel]]` — List of objects containing the Record IDs or Ironclad IDs of the record links to remove. For an explanation of Record IDs or Ironclad IDs and how to find them, see [Getting Started](https://developer.ironcladapp.com/reference/getting-started-api).
    
</dd>
</dl>

<dl>
<dd>

**set_parent:** `typing.Optional[RecordsUpdateMetadataRequestSetParent]` — Object containing Record IDs or Ironclad IDs to be set as the parent of the current record.
    
</dd>
</dl>

<dl>
<dd>

**add_children:** `typing.Optional[typing.List[RecordPropertyLinkModel]]` — List of objects containing the Record IDs or Ironclad IDs of the records to be set as child records of the current record.
    
</dd>
</dl>

<dl>
<dd>

**remove_parent:** `typing.Optional[bool]` — Boolean flag to indicate if the parent id should be removed for the current record.
    
</dd>
</dl>

<dl>
<dd>

**remove_children:** `typing.Optional[typing.List[RecordPropertyLinkModel]]` — List of objects containing the Record IDs or Ironclad IDs of the child records to be removed from the current record.
    
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

<details><summary><code>client.records.<a href="src/fern/records/client.py">getschema</a>() -> RecordsGetSchemaResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

View the schema associated with contract records, including available record types and metadata properties.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.records.getschema()

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

<details><summary><code>client.records.<a href="src/fern/records/client.py">getattachment</a>(...) -> RecordsGetAttachmentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

View an attachment associated with a specific record
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.records.getattachment(
    id="id",
    key="key",
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

**id:** `str` — The ID or Ironclad ID of the Record.
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — The attachment key.
    
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

<details><summary><code>client.records.<a href="src/fern/records/client.py">createattachment</a>(...) -> RecordsCreateAttachmentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an attachment on a specified record at the specified attachment key.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.records.createattachment(
    id="id",
    key="key",
    attachment="example_attachment",
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

**id:** `str` — The ID or Ironclad ID of the Record. For an explanation of Record IDs or Ironclad IDs and how to find them, see [Getting Started](https://developer.ironcladapp.com/reference/getting-started-api).
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — The attachment key. You can retrieve a list of available attachment keys with the [Retrieve Records Schema](https://developer.ironcladapp.com/reference/list-all-records-metadata) endpoint.
    
</dd>
</dl>

<dl>
<dd>

**attachment:** `typing.Optional[core.File]` — Must be a binary. Base64 is not accepted at this time.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[RecordsCreateAttachmentRequestMetadata]` — The `metadata` property's value must be `{"filename": "[YOUR_FILE_NAME]"}`
    
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

<details><summary><code>client.records.<a href="src/fern/records/client.py">removeattachment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove an attachment associated with a specific record
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.records.removeattachment(
    id="id",
    key="key",
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

**id:** `str` — The ID or Ironclad ID of the Record.
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — The attachment key.
    
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

<details><summary><code>client.records.<a href="src/fern/records/client.py">getxlsxexportfile</a>(...) -> RecordsGetXlsxExportFileResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Export a records report with filtering available via query parameters
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.records.getxlsxexportfile()

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

**types:** `typing.Optional[str]` — Comma separated list of record types to export. Example: `mutualNDA,NDA`
    
</dd>
</dl>

<dl>
<dd>

**properties:** `typing.Optional[str]` — IDs of properties to export, comma separated. Example: `counterpartyName,agreementDate`
    
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

## Webhooks
<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">listall</a>(...) -> WebhooksListAllResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

View all webhooks associated with a specific company with filtering available via query parameters
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.listall()

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

**page:** `typing.Optional[int]` — The page number used when paginating through a list of results.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — A limit of the number of results to return.
    
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

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">createnew</a>(...) -> WebhooksCreateNewResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a webhook for the specified events. Send separate requests if you need to create webhooks for multiple target URLs. Each target URL may only have one active registration.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.createnew(
    events=[
        "*"
    ],
    target_url="targetURL",
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

**events:** `typing.List[WebhookEventTypeValue]` — The event type(s) to trigger the webhook. Note: you can use `*` to receive events for all events, although we don't recommend this path, especially for environments with higher volume.
    
</dd>
</dl>

<dl>
<dd>

**target_url:** `str` — The URL to send the webhook event payload to.
    
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

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">getdata</a>(...) -> WebhooksGetDataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

View the data associated with a specific webhook
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.getdata(
    id="id",
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

**id:** `str` — The ID of the webhook.
    
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

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">deletespecific</a>(...) -> WebhooksDeleteSpecificResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a specific webhook
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.deletespecific(
    id="id",
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

**id:** `str` — The ID of the webhook.
    
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

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">updatewebhookdata</a>(...) -> WebhooksUpdateWebhookDataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the data associated with a specific webhook
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.updatewebhookdata(
    id="id",
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

**id:** `str` — The ID of the webhook.
    
</dd>
</dl>

<dl>
<dd>

**events:** `typing.Optional[typing.List[str]]` — The type of events that will trigger a notification to the target URL.
    
</dd>
</dl>

<dl>
<dd>

**target_url:** `typing.Optional[str]` — The URL of where the notification gets sent.
    
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

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">getverificationkey</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

View the verification key for webhook security implementations
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.getverificationkey()

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

