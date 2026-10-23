# Reference
<details><summary><code>client.<a href="src/fern/client.py">me</a>() -> MeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches the Workspaces and organizations associated with the API key.
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

client.me()

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

## ClientApiResponse
<details><summary><code>client.client_api_response.<a href="src/fern/client_api_response/client.py">update_response</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing response for example when you want to mark a response as finished or you want to change an existing response's value. Note - Environments are deprecated. Use Workspace/workspaceId terminology.
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

client.client_api_response.update_response(
    workspace_id="workspaceId",
    response_id="responseId",
    request={
        "data": {"tcgls0063n8ri7dtrbnepcmz": "Who? Who? Who?"},
        "finished": True
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

**workspace_id:** `str` — The ID of the Workspace. Deprecated alias `environmentId`.
    
</dd>
</dl>

<dl>
<dd>

**response_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
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

<details><summary><code>client.client_api_response.<a href="src/fern/client_api_response/client.py">create_response</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a response for a survey and its fields with the user's responses. The userId & meta here is optional. Note - Environments are deprecated. Use Workspace/workspaceId terminology.
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

client.client_api_response.create_response(
    workspace_id="workspaceId",
    request={
        "surveyId": "survey123",
        "responses": {}
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

**workspace_id:** `str` — The ID of the Workspace. Deprecated alias `environmentId`.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
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

## ClientApiDisplay
<details><summary><code>client.client_api_display.<a href="src/fern/client_api_display/client.py">create_display</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new display for a valid survey ID. If a userId is passed, the display is linked to the user. Note - Environments are deprecated. Use Workspace/workspaceId terminology.
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

client.client_api_display.create_display(
    workspace_id="workspaceId",
    request={
        "surveyId": "survey123",
        "userId": "user123"
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

**workspace_id:** `str` — The ID of the Workspace. Deprecated alias `environmentId`.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
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

## ClientApiWorkspace
<details><summary><code>client.client_api_workspace.<a href="src/fern/client_api_workspace/client.py">get_workspace_state</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the Workspace state to be used in Formbricks SDKs. Note - Environments are deprecated. Use Workspace/workspaceId terminology. **Cache Behavior**: This endpoint uses server-side caching with a **5-minute TTL (Time To Live)**. Any changes to surveys, action classes, Workspace settings, or other Workspace data will take up to 5 minutes to reflect in the API response. This caching is implemented to improve performance for high-frequency SDK requests.
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

client.client_api_workspace.get_workspace_state(
    workspace_id="workspaceId",
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

**workspace_id:** `str` — The ID of the Workspace. Deprecated alias `environmentId`.
    
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

## ClientApiUser
<details><summary><code>client.client_api_user.<a href="src/fern/client_api_user/client.py">create_or_identify_user</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint for creating or identifying a user within the specified Workspace. If the user already exists, this will identify them and potentially update user attributes. If they don't exist, it will create a new user. Note - Environments are deprecated. Use Workspace/workspaceId terminology.
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

client.client_api_user.create_or_identify_user(
    workspace_id="workspaceId",
    request={
        "userId": "user123",
        "attributes": {}
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

**workspace_id:** `str` — The ID of the Workspace. Deprecated alias `environmentId`.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
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

## ClientApiFileUpload
<details><summary><code>client.client_api_file_upload.<a href="src/fern/client_api_file_upload/client.py">upload_private_file</a>(...) -> PostClientWorkspaceIdStorageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

API endpoint for uploading private files. Uploaded files are kept private so that only users with access to the specified Workspace can retrieve them. The endpoint validates the survey ID, file name, and file type from the request body, and returns a signed URL for S3 uploads along with a local upload URL. Note - Environments are deprecated. Use Workspace/workspaceId terminology.
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

client.client_api_file_upload.upload_private_file(
    workspace_id="workspaceId",
    survey_id="cm7pr0x2y004o192zmit8cjvb",
    file_name="example.jpg",
    file_type="image/jpeg",
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

**workspace_id:** `str` — The ID of the Workspace. Deprecated alias `environmentId`.
    
</dd>
</dl>

<dl>
<dd>

**survey_id:** `str` — The ID of the survey associated with the file.
    
</dd>
</dl>

<dl>
<dd>

**file_name:** `str` — The name of the file to be uploaded.
    
</dd>
</dl>

<dl>
<dd>

**file_type:** `str` — The MIME type of the file.
    
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
<details><summary><code>client.health.<a href="src/fern/health/client.py">check</a>() -> HealthCheckResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check the health status of critical application dependencies including database and cache.
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

client.health.check()

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

## Roles
<details><summary><code>client.roles.<a href="src/fern/roles/client.py">get_roles</a>() -> GetRolesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets roles from the database.
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

client.roles.get_roles()

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

## Management API - Responses
<details><summary><code>client.management_api_responses.<a href="src/fern/management_api_responses/client.py">get_responses</a>(...) -> GetResponsesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets responses from the database.
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

client.management_api_responses.get_responses()

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

**limit:** `typing.Optional[float]` — Number of items to return
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[float]` — Number of items to skip
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[GetResponsesRequestSortBy]` — Sort by field
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetResponsesRequestOrder]` — Sort order
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — Start date
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — End date
    
</dd>
</dl>

<dl>
<dd>

**filter_date_field:** `typing.Optional[GetResponsesRequestFilterDateField]` — Date field to filter by
    
</dd>
</dl>

<dl>
<dd>

**survey_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.management_api_responses.<a href="src/fern/management_api_responses/client.py">create_response</a>(...) -> CreateResponseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a response in the database. This will trigger the response pipeline, including webhooks, integrations, follow-up emails, and other configured actions.
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

client.management_api_responses.create_response(
    survey_id="surveyId",
    finished=True,
    data={
        "question1": "answer1",
        "question2": 2,
        "question3": [
            "answer3",
            "answer4"
        ],
        "question4": {
            "subquestion1": "answer5"
        }
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

**survey_id:** `str` — The ID of the survey
    
</dd>
</dl>

<dl>
<dd>

**finished:** `bool` — Whether the response is finished
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Dict[str, CreateResponseRequestDataValue]` — The data of the response
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[str]` — The date and time the response was created
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[str]` — The date and time the response was last updated
    
</dd>
</dl>

<dl>
<dd>

**display_id:** `typing.Optional[str]` — The display ID of the response
    
</dd>
</dl>

<dl>
<dd>

**single_use_id:** `typing.Optional[str]` — The single use ID of the response
    
</dd>
</dl>

<dl>
<dd>

**ending_id:** `typing.Optional[str]` — The ID of the ending
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — The language of the response
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, CreateResponseRequestVariablesValue]]` — The variables of the response
    
</dd>
</dl>

<dl>
<dd>

**ttc:** `typing.Optional[typing.Dict[str, float]]` — The TTC of the response
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[CreateResponseRequestMeta]` — The meta data of the response
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.management_api_responses.<a href="src/fern/management_api_responses/client.py">get_response</a>(...) -> GetResponseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a response from the database.
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

client.management_api_responses.get_response(
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

**id:** `ResponseId` — The ID of the response
    
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

<details><summary><code>client.management_api_responses.<a href="src/fern/management_api_responses/client.py">update_response</a>(...) -> UpdateResponseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a response in the database. This will trigger the response pipeline, including webhooks, integrations, follow-up emails (if the response is marked as finished), and other configured actions.
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

client.management_api_responses.update_response(
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

**id:** `ResponseId` — The ID of the response
    
</dd>
</dl>

<dl>
<dd>

**finished:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**ending_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Optional[typing.Dict[str, UpdateResponseRequestDataValue]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, UpdateResponseRequestVariablesValue]]` 
    
</dd>
</dl>

<dl>
<dd>

**ttc:** `typing.Optional[typing.Dict[str, float]]` 
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` 
    
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

<details><summary><code>client.management_api_responses.<a href="src/fern/management_api_responses/client.py">delete_response</a>(...) -> DeleteResponseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a response from the database.
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

client.management_api_responses.delete_response(
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

**id:** `ResponseId` — The ID of the response
    
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

## Management API - Contacts
<details><summary><code>client.management_api_contacts.<a href="src/fern/management_api_contacts/client.py">upload_bulk_contacts</a>(...) -> UploadBulkContactsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Uploads contacts in bulk. This endpoint expects the bulk request shape: `contacts` must be an array, and each contact item must contain an `attributes` array of `{ attributeKey, value }` objects. Unlike `POST /management/contacts`, this endpoint does not accept a top-level `attributes` object. Each contact must include an `email` attribute in its `attributes` array, and that email must be valid. Note - Environments are deprecated. Use Workspace/workspaceId terminology.
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
from fern.management_api_contacts import UploadBulkContactsRequestContactsItem, UploadBulkContactsRequestContactsItemAttributesItem, UploadBulkContactsRequestContactsItemAttributesItemAttributeKey

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.management_api_contacts.upload_bulk_contacts(
    workspace_id="ws_01h2xce9q8p3w4x5y6z7a8b9c0",
    contacts=[
        UploadBulkContactsRequestContactsItem(
            attributes=[
                UploadBulkContactsRequestContactsItemAttributesItem(
                    attribute_key=UploadBulkContactsRequestContactsItemAttributesItemAttributeKey(
                        key="email",
                        name="Email Address",
                    ),
                    value="john.doe@example.com",
                ),
                UploadBulkContactsRequestContactsItemAttributesItem(
                    attribute_key=UploadBulkContactsRequestContactsItemAttributesItemAttributeKey(
                        key="firstName",
                        name="First Name",
                    ),
                    value="John",
                ),
                UploadBulkContactsRequestContactsItemAttributesItem(
                    attribute_key=UploadBulkContactsRequestContactsItemAttributesItemAttributeKey(
                        key="lastName",
                        name="Last Name",
                    ),
                    value="Doe",
                )
            ],
        ),
        UploadBulkContactsRequestContactsItem(
            attributes=[
                UploadBulkContactsRequestContactsItemAttributesItem(
                    attribute_key=UploadBulkContactsRequestContactsItemAttributesItemAttributeKey(
                        key="email",
                        name="Email Address",
                    ),
                    value="jane.smith@example.com",
                ),
                UploadBulkContactsRequestContactsItemAttributesItem(
                    attribute_key=UploadBulkContactsRequestContactsItemAttributesItemAttributeKey(
                        key="firstName",
                        name="First Name",
                    ),
                    value="Jane",
                ),
                UploadBulkContactsRequestContactsItemAttributesItem(
                    attribute_key=UploadBulkContactsRequestContactsItemAttributesItemAttributeKey(
                        key="lastName",
                        name="Last Name",
                    ),
                    value="Smith",
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

**workspace_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**contacts:** `typing.List[UploadBulkContactsRequestContactsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**environment_id:** `typing.Optional[str]` — Deprecated alias for workspaceId.
    
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

<details><summary><code>client.management_api_contacts.<a href="src/fern/management_api_contacts/client.py">create_contact</a>(...) -> CreateContactResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a single contact in the database. This endpoint expects a top-level `attributes` object. For bulk uploads, use `PUT /management/contacts/bulk`, which expects `contacts[].attributes[]` instead. Each contact must have a valid email address in the attributes. All attribute keys must already exist in the Workspace. The email is used as the unique identifier along with the Workspace. Note - Environments are deprecated. Use Workspace/workspaceId terminology.
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

client.management_api_contacts.create_contact(
    workspace_id="ws_01h2xce9q8p3w4x5y6z7a8b9c0",
    attributes={
        "email": "john.doe@example.com",
        "firstName": "John",
        "lastName": "Doe",
        "userId": "h2xce9q8p3w4x5y6z7a8b9c1"
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

**workspace_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Dict[str, str]` 
    
</dd>
</dl>

<dl>
<dd>

**environment_id:** `typing.Optional[str]` — Deprecated alias for workspaceId.
    
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

## Management API - Contact Attribute Keys
<details><summary><code>client.management_api_contact_attribute_keys.<a href="src/fern/management_api_contact_attribute_keys/client.py">get_contact_attribute_keys</a>(...) -> GetContactAttributeKeysResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets contact attribute keys from the database. Note - Environments are deprecated. Use Workspace/workspaceId terminology.
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

client.management_api_contact_attribute_keys.get_contact_attribute_keys()

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

**limit:** `typing.Optional[float]` — Number of items to return
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[float]` — Number of items to skip
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[GetContactAttributeKeysRequestSortBy]` — Sort by field
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetContactAttributeKeysRequestOrder]` — Sort order
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — Start date
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — End date
    
</dd>
</dl>

<dl>
<dd>

**filter_date_field:** `typing.Optional[GetContactAttributeKeysRequestFilterDateField]` — Date field to filter by
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `typing.Optional[str]` — The Workspace ID to filter by
    
</dd>
</dl>

<dl>
<dd>

**environment_id:** `typing.Optional[str]` — Deprecated alias for workspaceId
    
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

<details><summary><code>client.management_api_contact_attribute_keys.<a href="src/fern/management_api_contact_attribute_keys/client.py">create_contact_attribute_key</a>(...) -> CreateContactAttributeKeyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a contact attribute key in the database. Note - Environments are deprecated. Use Workspace/workspaceId terminology.
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

client.management_api_contact_attribute_keys.create_contact_attribute_key(
    key="email",
    name="Email Address",
    description="The user\'s email address",
    workspace_id="workspaceId",
    environment_id="environmentId",
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

**key:** `str` — The attribute identifier used in the system
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — The ID of the Workspace this attribute belongs to
    
</dd>
</dl>

<dl>
<dd>

**environment_id:** `str` — Deprecated alias for workspaceId.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Display name for the attribute
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the attribute
    
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

<details><summary><code>client.management_api_contact_attribute_keys.<a href="src/fern/management_api_contact_attribute_keys/client.py">get_contact_attribute_key</a>(...) -> GetContactAttributeKeyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a contact attribute key from the database.
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

client.management_api_contact_attribute_keys.get_contact_attribute_key(
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

**id:** `ContactAttributeKeyId` — The ID of the contact attribute key
    
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

<details><summary><code>client.management_api_contact_attribute_keys.<a href="src/fern/management_api_contact_attribute_keys/client.py">update_contact_attribute_key</a>(...) -> UpdateContactAttributeKeyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a contact attribute key in the database.
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

client.management_api_contact_attribute_keys.update_contact_attribute_key(
    id="id",
    name="Email Address",
    description="The user\'s email address",
    key="email",
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

**id:** `ContactAttributeKeyId` — The ID of the contact attribute key
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — The attribute identifier used in the system
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Display name for the attribute
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the attribute
    
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

<details><summary><code>client.management_api_contact_attribute_keys.<a href="src/fern/management_api_contact_attribute_keys/client.py">delete_contact_attribute_key</a>(...) -> DeleteContactAttributeKeyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a contact attribute key from the database.
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

client.management_api_contact_attribute_keys.delete_contact_attribute_key(
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

**id:** `ContactAttributeKeyId` — The ID of the contact attribute key
    
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

## Management API - Surveys - Contact Links
<details><summary><code>client.management_api_surveys_contact_links.<a href="src/fern/management_api_surveys_contact_links/client.py">get_personalized_survey_link</a>(...) -> GetPersonalizedSurveyLinkResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a personalized link for a specific survey.
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

client.management_api_surveys_contact_links.get_personalized_survey_link(
    survey_id="surveyId",
    contact_id="contactId",
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

**survey_id:** `str` — The ID of the survey
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `str` — The ID of the contact
    
</dd>
</dl>

<dl>
<dd>

**expiration_days:** `typing.Optional[int]` — Number of days until the generated JWT expires. If not provided, there is no expiration.
    
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

<details><summary><code>client.management_api_surveys_contact_links.<a href="src/fern/management_api_surveys_contact_links/client.py">get_contact_links_by_segment</a>(...) -> GetContactLinksBySegmentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates personalized survey links for contacts in a segment.
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

client.management_api_surveys_contact_links.get_contact_links_by_segment(
    survey_id="surveyId",
    segment_id="segmentId",
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

**survey_id:** `str` — The ID of the survey
    
</dd>
</dl>

<dl>
<dd>

**segment_id:** `str` — The ID of the segment
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — Number of items to return
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[float]` — Number of items to skip
    
</dd>
</dl>

<dl>
<dd>

**expiration_days:** `typing.Optional[float]` — Number of days until the generated JWT expires. If not provided, there is no expiration.
    
</dd>
</dl>

<dl>
<dd>

**attribute_keys:** `typing.Optional[str]` — Comma-separated list of contact attribute keys to include in the response. You can have max 20 keys. If not provided, no attributes will be included.
    
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

## Management API - Webhooks
<details><summary><code>client.management_api_webhooks.<a href="src/fern/management_api_webhooks/client.py">get_webhooks</a>(...) -> GetWebhooksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets webhooks from the database. Note - Environments are deprecated. Use Workspace/workspaceId terminology.
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

client.management_api_webhooks.get_webhooks()

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

**limit:** `typing.Optional[float]` — Number of items to return
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[float]` — Number of items to skip
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[GetWebhooksRequestSortBy]` — Sort by field
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetWebhooksRequestOrder]` — Sort order
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — Start date
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — End date
    
</dd>
</dl>

<dl>
<dd>

**filter_date_field:** `typing.Optional[GetWebhooksRequestFilterDateField]` — Date field to filter by
    
</dd>
</dl>

<dl>
<dd>

**survey_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
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

<details><summary><code>client.management_api_webhooks.<a href="src/fern/management_api_webhooks/client.py">create_webhook</a>(...) -> CreateWebhookResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a webhook in the database. Note - Environments are deprecated. Use Workspace/workspaceId terminology.
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
from fern.management_api_webhooks import CreateWebhookRequestSource, CreateWebhookRequestTriggersItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.management_api_webhooks.create_webhook(
    name=None,
    url="url",
    source=CreateWebhookRequestSource.USER,
    workspace_id="workspaceId",
    triggers=[
        CreateWebhookRequestTriggersItem.RESPONSE_FINISHED
    ],
    survey_ids=[
        "surveyIds"
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

**url:** `str` — The URL of the webhook
    
</dd>
</dl>

<dl>
<dd>

**source:** `CreateWebhookRequestSource` — The source of the webhook
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — The ID of the Workspace
    
</dd>
</dl>

<dl>
<dd>

**triggers:** `typing.List[CreateWebhookRequestTriggersItem]` — The triggers of the webhook
    
</dd>
</dl>

<dl>
<dd>

**survey_ids:** `typing.List[str]` — The IDs of the surveys 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the webhook
    
</dd>
</dl>

<dl>
<dd>

**environment_id:** `typing.Optional[str]` — Deprecated alias for workspaceId.
    
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

<details><summary><code>client.management_api_webhooks.<a href="src/fern/management_api_webhooks/client.py">get_webhook</a>(...) -> GetWebhookResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a webhook from the database. Note - Environments are deprecated. Use Workspace/workspaceId terminology.
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

client.management_api_webhooks.get_webhook(
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

**id:** `WebhookId` — The ID of the webhook
    
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

<details><summary><code>client.management_api_webhooks.<a href="src/fern/management_api_webhooks/client.py">update_webhook</a>(...) -> UpdateWebhookResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a webhook in the database. Note - Environments are deprecated. Use Workspace/workspaceId terminology.
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
from fern.management_api_webhooks import UpdateWebhookRequestSource, UpdateWebhookRequestTriggersItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.management_api_webhooks.update_webhook(
    id="id",
    name=None,
    url="url",
    source=UpdateWebhookRequestSource.USER,
    workspace_id="workspaceId",
    triggers=[
        UpdateWebhookRequestTriggersItem.RESPONSE_FINISHED
    ],
    survey_ids=[
        "surveyIds"
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

**id:** `WebhookId` — The ID of the webhook
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — The URL of the webhook
    
</dd>
</dl>

<dl>
<dd>

**source:** `UpdateWebhookRequestSource` — The source of the webhook
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — The ID of the Workspace
    
</dd>
</dl>

<dl>
<dd>

**triggers:** `typing.List[UpdateWebhookRequestTriggersItem]` — The triggers of the webhook
    
</dd>
</dl>

<dl>
<dd>

**survey_ids:** `typing.List[str]` — The IDs of the surveys 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the webhook
    
</dd>
</dl>

<dl>
<dd>

**environment_id:** `typing.Optional[str]` — Deprecated alias for workspaceId.
    
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

<details><summary><code>client.management_api_webhooks.<a href="src/fern/management_api_webhooks/client.py">delete_webhook</a>(...) -> DeleteWebhookResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a webhook from the database. Note - Environments are deprecated. Use Workspace/workspaceId terminology.
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

client.management_api_webhooks.delete_webhook(
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

**id:** `WebhookId` — The ID of the webhook
    
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

## Organizations API - Teams
<details><summary><code>client.organizations_api_teams.<a href="src/fern/organizations_api_teams/client.py">get_teams</a>(...) -> GetTeamsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets teams from the database.
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

client.organizations_api_teams.get_teams(
    organization_id="organizationId",
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

**organization_id:** `OrganizationId` — The ID of the organization
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — Number of items to return
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[float]` — Number of items to skip
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[GetTeamsRequestSortBy]` — Sort by field
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetTeamsRequestOrder]` — Sort order
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — Start date
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — End date
    
</dd>
</dl>

<dl>
<dd>

**filter_date_field:** `typing.Optional[GetTeamsRequestFilterDateField]` — Date field to filter by
    
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

<details><summary><code>client.organizations_api_teams.<a href="src/fern/organizations_api_teams/client.py">create_team</a>(...) -> CreateTeamResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a team in the database.
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

client.organizations_api_teams.create_team(
    organization_id="organizationId",
    name="My team",
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

**organization_id:** `OrganizationId` — The ID of the organization
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the team
    
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

<details><summary><code>client.organizations_api_teams.<a href="src/fern/organizations_api_teams/client.py">get_team</a>(...) -> GetTeamResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a team from the database.
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

client.organizations_api_teams.get_team(
    organization_id="organizationId",
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

**organization_id:** `OrganizationId` — The ID of the organization
    
</dd>
</dl>

<dl>
<dd>

**id:** `TeamId` — The ID of the team
    
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

<details><summary><code>client.organizations_api_teams.<a href="src/fern/organizations_api_teams/client.py">update_team</a>(...) -> UpdateTeamResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a team in the database.
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

client.organizations_api_teams.update_team(
    organization_id="organizationId",
    id="id",
    name="My team",
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

**organization_id:** `OrganizationId` — The ID of the organization
    
</dd>
</dl>

<dl>
<dd>

**id:** `TeamId` — The ID of the team
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the team
    
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

<details><summary><code>client.organizations_api_teams.<a href="src/fern/organizations_api_teams/client.py">delete_team</a>(...) -> DeleteTeamResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a team from the database.
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

client.organizations_api_teams.delete_team(
    organization_id="organizationId",
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

**organization_id:** `OrganizationId` — The ID of the organization
    
</dd>
</dl>

<dl>
<dd>

**id:** `TeamId` — The ID of the team
    
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

## Organizations API - Workspace Teams
<details><summary><code>client.organizations_api_workspace_teams.<a href="src/fern/organizations_api_workspace_teams/client.py">get_workspace_teams</a>(...) -> GetWorkspaceTeamsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets workspace teams from the database.
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

client.organizations_api_workspace_teams.get_workspace_teams(
    organization_id="organizationId",
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

**organization_id:** `OrganizationId` — The ID of the organization
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — Number of items to return
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[float]` — Number of items to skip
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[GetWorkspaceTeamsRequestSortBy]` — Sort by field
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetWorkspaceTeamsRequestOrder]` — Sort order
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — Start date
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — End date
    
</dd>
</dl>

<dl>
<dd>

**filter_date_field:** `typing.Optional[GetWorkspaceTeamsRequestFilterDateField]` — Date field to filter by
    
</dd>
</dl>

<dl>
<dd>

**team_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `typing.Optional[str]` — The ID of the Workspace to filter by
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — Deprecated alias for workspaceId.
    
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

<details><summary><code>client.organizations_api_workspace_teams.<a href="src/fern/organizations_api_workspace_teams/client.py">create_workspace_team</a>(...) -> CreateWorkspaceTeamResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a Workspace team in the database.
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
from fern.organizations_api_workspace_teams import CreateWorkspaceTeamRequestPermission

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.organizations_api_workspace_teams.create_workspace_team(
    organization_id="organizationId",
    team_id="teamId",
    permission=CreateWorkspaceTeamRequestPermission.READ,
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

**organization_id:** `OrganizationId` — The ID of the organization
    
</dd>
</dl>

<dl>
<dd>

**team_id:** `str` — The ID of the team
    
</dd>
</dl>

<dl>
<dd>

**permission:** `CreateWorkspaceTeamRequestPermission` — Level of access granted to the Workspace
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `typing.Optional[str]` — The ID of the Workspace
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — Deprecated alias for workspaceId.
    
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

<details><summary><code>client.organizations_api_workspace_teams.<a href="src/fern/organizations_api_workspace_teams/client.py">update_workspace_team</a>(...) -> UpdateWorkspaceTeamResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a Workspace team in the database.
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
from fern.organizations_api_workspace_teams import UpdateWorkspaceTeamRequestPermission

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.organizations_api_workspace_teams.update_workspace_team(
    organization_id="organizationId",
    team_id="teamId",
    permission=UpdateWorkspaceTeamRequestPermission.READ,
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

**organization_id:** `OrganizationId` — The ID of the organization
    
</dd>
</dl>

<dl>
<dd>

**team_id:** `str` — The ID of the team
    
</dd>
</dl>

<dl>
<dd>

**permission:** `UpdateWorkspaceTeamRequestPermission` — Level of access granted to the Workspace
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `typing.Optional[str]` — The ID of the Workspace
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — Deprecated alias for workspaceId.
    
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

<details><summary><code>client.organizations_api_workspace_teams.<a href="src/fern/organizations_api_workspace_teams/client.py">delete_workspace_team</a>(...) -> DeleteWorkspaceTeamResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a Workspace team from the database.
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

client.organizations_api_workspace_teams.delete_workspace_team(
    organization_id="organizationId",
    team_id="teamId",
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

**organization_id:** `OrganizationId` — The ID of the organization
    
</dd>
</dl>

<dl>
<dd>

**team_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `typing.Optional[str]` — The ID of the Workspace
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — Deprecated alias for workspaceId.
    
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

## Organizations API - Users
<details><summary><code>client.organizations_api_users.<a href="src/fern/organizations_api_users/client.py">get_users</a>(...) -> GetUsersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets users from the database.<br />Only available for self-hosted Formbricks.
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

client.organizations_api_users.get_users(
    organization_id="organizationId",
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

**organization_id:** `OrganizationId` — The ID of the organization
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — Number of items to return
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[float]` — Number of items to skip
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[GetUsersRequestSortBy]` — Sort by field
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetUsersRequestOrder]` — Sort order
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — Start date
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — End date
    
</dd>
</dl>

<dl>
<dd>

**filter_date_field:** `typing.Optional[GetUsersRequestFilterDateField]` — Date field to filter by
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` 
    
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

<details><summary><code>client.organizations_api_users.<a href="src/fern/organizations_api_users/client.py">create_user</a>(...) -> CreateUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new user in the database.<br />Only available for self-hosted Formbricks.
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
from fern.organizations_api_users import CreateUserRequestRole

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.organizations_api_users.create_user(
    organization_id="organizationId",
    name="John Doe",
    email="example@example.com",
    role=CreateUserRequestRole.OWNER,
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

**organization_id:** `OrganizationId` — The ID of the organization
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the user
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — The email of the user
    
</dd>
</dl>

<dl>
<dd>

**role:** `CreateUserRequestRole` — The role of the user in the organization
    
</dd>
</dl>

<dl>
<dd>

**is_active:** `typing.Optional[bool]` — Whether the user is active
    
</dd>
</dl>

<dl>
<dd>

**teams:** `typing.Optional[typing.List[str]]` — The list of teams the user is a member of
    
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

<details><summary><code>client.organizations_api_users.<a href="src/fern/organizations_api_users/client.py">update_user</a>(...) -> UpdateUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing user in the database.<br />Only available for self-hosted Formbricks.
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

client.organizations_api_users.update_user(
    organization_id="organizationId",
    email="example@example.com",
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

**organization_id:** `OrganizationId` — The ID of the organization
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — The email of the user
    
</dd>
</dl>

<dl>
<dd>

**is_active:** `typing.Optional[bool]` — Whether the user is active
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[UpdateUserRequestRole]` — The role of the user in the organization
    
</dd>
</dl>

<dl>
<dd>

**teams:** `typing.Optional[typing.List[str]]` — The list of teams the user is a member of
    
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

