# Reference
## Analytics
<details><summary><code>client.analytics.<a href="src/fern/analytics/client.py">get_analytics_histogram</a>(...) -> GetHistogramAnalyticsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.analytics.get_analytics_histogram(
    domain="domain",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` — The start date of the period to retrieve analytics for
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` — The end date of the period to retrieve analytics for
    
</dd>
</dl>

<dl>
<dd>

**group_by:** `typing.Optional[GroupBy]` — The field to group the analytics by
    
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

<details><summary><code>client.analytics.<a href="src/fern/analytics/client.py">generate_all_insights</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate insights for all domains with queries in the specified period.
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
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.analytics.generate_all_insights()

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

**start_date:** `typing.Optional[datetime.datetime]` — The start date of the period to generate insights for
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` — The end date of the period to generate insights for
    
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

<details><summary><code>client.analytics.<a href="src/fern/analytics/client.py">trigger_scheduled_insights_generation</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manually trigger the scheduled weekly insights generation job.
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
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.analytics.trigger_scheduled_insights_generation()

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

<details><summary><code>client.analytics.<a href="src/fern/analytics/client.py">get_query_insights</a>(...) -> GetInsightsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the most recent insights for a domain.
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
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.analytics.get_query_insights(
    domain="domain",
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

**domain:** `str` 
    
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

<details><summary><code>client.analytics.<a href="src/fern/analytics/client.py">get_scheduler_status</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the status of the scheduler and its jobs.
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
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.analytics.get_scheduler_status()

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

<details><summary><code>client.analytics.<a href="src/fern/analytics/client.py">get_conversation_resolution</a>(...) -> GetConversationResolutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get conversation resolution metrics for a domain in a given time period.
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
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.analytics.get_conversation_resolution(
    domain="domain",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` — The start date of the period to retrieve resolution metrics for
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` — The end date of the period to retrieve resolution metrics for
    
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

## Chat
<details><summary><code>client.chat.<a href="src/fern/chat/client.py">post_chat_completion</a>(...) -> PostChatCompletionResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ChatMessage, ChatMessageRole
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.chat.post_chat_completion(
    domain="domain",
    messages=[
        ChatMessage(
            role=ChatMessageRole.USER,
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.List[ChatMessage]` — The messages to use for the chat completion
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[LanguageModel]` — The model to use for the chat completion
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` — The maximum number of tokens to generate. Note: setting a token count lower than 2000 may result in incomplete responses. You can add a custom system prompt to control the verbosity of the response.
    
</dd>
</dl>

<dl>
<dd>

**system_prompt:** `typing.Optional[str]` — The system prompt to use for the chat completion
    
</dd>
</dl>

<dl>
<dd>

**rewrite_query:** `typing.Optional[bool]` — Whether to rewrite the query using query decomposition
    
</dd>
</dl>

<dl>
<dd>

**user_is_authed:** `typing.Optional[bool]` — Whether the requesting user is authenticated. When true, authed chunks are included in results.
    
</dd>
</dl>

<dl>
<dd>

**allowed_roles:** `typing.Optional[typing.List[str]]` — Roles the authenticated user has. Used to filter chunks by role-based access control.
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[str]` — The origin of the request (e.g. 'web', 'slack', 'api').
    
</dd>
</dl>

<dl>
<dd>

**basepaths:** `typing.Optional[typing.List[str]]` — Restrict retrieval to pages under these URL path prefixes (e.g. ['/my-product']). Matches the scoping the Ask AI widget applies when embedded under a product path. Omit to search the whole site.
    
</dd>
</dl>

<dl>
<dd>

**skip_save_query:** `typing.Optional[bool]` — Set to true for test or eval traffic. The request is answered (and billed) normally but is excluded from usage analytics.
    
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

## Code
<details><summary><code>client.code.<a href="src/fern/code/client.py">create_code_record</a>(...) -> typing.List[CreateCodeRecordResponse]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.code.create_code_record(
    domain="domain",
    request={"key": "value"},
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Any` 
    
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

<details><summary><code>client.code.<a href="src/fern/code/client.py">batch_create_code_records</a>(...) -> typing.List[CreateCodeRecordResponse]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.code.batch_create_code_records(
    domain="domain",
    request=[],
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[typing.Any]` 
    
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

<details><summary><code>client.code.<a href="src/fern/code/client.py">get_code_record_by_id</a>(...) -> GetCodeRecordResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.code.get_code_record_by_id(
    domain="domain",
    code_id="code_id",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**code_id:** `str` 
    
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

<details><summary><code>client.code.<a href="src/fern/code/client.py">get_code_records</a>(...) -> GetCodeRecordsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.code.get_code_records(
    domain="domain",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of code entries per page
    
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

<details><summary><code>client.code.<a href="src/fern/code/client.py">delete_code_record_by_id</a>(...) -> DeleteCodeRecordResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.code.delete_code_record_by_id(
    domain="domain",
    code_id="code_id",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**code_id:** `str` — The unique identifier of the code to delete
    
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

<details><summary><code>client.code.<a href="src/fern/code/client.py">delete_all_code_records</a>(...) -> DeleteCodeRecordResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.code.delete_all_code_records(
    domain="domain",
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

**domain:** `str` 
    
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

## Conversation
<details><summary><code>client.conversation.<a href="src/fern/conversation/client.py">get_conversation_by_id</a>(...) -> GetConversationResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.conversation.get_conversation_by_id(
    domain="domain",
    conversation_id="conversation_id",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**conversation_id:** `str` 
    
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

## Document
<details><summary><code>client.document.<a href="src/fern/document/client.py">create_document</a>(...) -> typing.List[CreateDocumentResponse]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.document.create_document(
    domain="domain",
    request={"key": "value"},
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Any` 
    
</dd>
</dl>

<dl>
<dd>

**fern_basepath:** `typing.Optional[str]` — The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.
    
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

<details><summary><code>client.document.<a href="src/fern/document/client.py">batch_create_document</a>(...) -> typing.List[CreateDocumentResponse]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.document.batch_create_document(
    domain="domain",
    request=[],
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**fern_basepath:** `typing.Optional[str]` — The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.
    
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

<details><summary><code>client.document.<a href="src/fern/document/client.py">get_document_by_id</a>(...) -> GetDocumentResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.document.get_document_by_id(
    domain="domain",
    document_id="document_id",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fern_basepath:** `typing.Optional[str]` — The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.
    
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

<details><summary><code>client.document.<a href="src/fern/document/client.py">delete_document</a>(...) -> DeleteDocumentResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.document.delete_document(
    domain="domain",
    document_id="document_id",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fern_basepath:** `typing.Optional[str]` — The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.
    
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

<details><summary><code>client.document.<a href="src/fern/document/client.py">update_document</a>(...) -> UpdateDocumentResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.document.update_document(
    domain="domain",
    document_id="document_id",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fern_basepath:** `typing.Optional[str]` — The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.
    
</dd>
</dl>

<dl>
<dd>

**document:** `typing.Optional[str]` — The updated content of the document that will be returned to Ask Fern during document retrieval. If not provided, this field will remain unchanged.
    
</dd>
</dl>

<dl>
<dd>

**chunk:** `typing.Optional[str]` — The updated textual content that should be vectorized when indexing the document. If not provided, this field will remain unchanged.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The updated title of the document. If not provided, this field will remain unchanged.
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — The updated url of the document. If not provided, this field will remain unchanged.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — The updated version of the document. If not provided, this field will remain unchanged.
    
</dd>
</dl>

<dl>
<dd>

**product:** `typing.Optional[str]` — The updated product of the document. If not provided, this field will remain unchanged.
    
</dd>
</dl>

<dl>
<dd>

**keywords:** `typing.Optional[typing.List[str]]` — The updated keywords of the document. If not provided, this field will remain unchanged.
    
</dd>
</dl>

<dl>
<dd>

**authed:** `typing.Optional[bool]` — The updated authed status of the document. If not provided, this field will remain unchanged.
    
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

<details><summary><code>client.document.<a href="src/fern/document/client.py">delete_document_by_id</a>(...) -> DeleteDocumentResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.document.delete_document_by_id(
    domain="domain",
    document_id="document_id",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `DeleteDocumentRequest` 
    
</dd>
</dl>

<dl>
<dd>

**fern_basepath:** `typing.Optional[str]` — The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.
    
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

<details><summary><code>client.document.<a href="src/fern/document/client.py">batch_delete_document</a>(...) -> DeleteDocumentResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, DeleteDocumentRequest
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.document.batch_delete_document(
    domain="domain",
    request=[
        DeleteDocumentRequest(
            document_id="document_id",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[DeleteDocumentRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**fern_basepath:** `typing.Optional[str]` — The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.
    
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

<details><summary><code>client.document.<a href="src/fern/document/client.py">get_documents</a>(...) -> GetDocumentsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.document.get_documents(
    domain="domain",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of documents per page
    
</dd>
</dl>

<dl>
<dd>

**fern_basepath:** `typing.Optional[str]` — The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.
    
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

<details><summary><code>client.document.<a href="src/fern/document/client.py">delete_documents</a>(...) -> DeleteDocumentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the documents of a domain, narrowed by the provided filters. Filters are combined with AND, so a document is
only deleted when it matches all of them. At least one filter is required, or pass `all=true` to delete every
document. The `x-fern-basepath` header narrows the deletion to a single basepath.
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
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.document.delete_documents(
    domain="domain",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**product:** `typing.Optional[str]` — Only delete documents whose product matches this value exactly.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Only delete documents whose version matches this value exactly.
    
</dd>
</dl>

<dl>
<dd>

**url_prefix:** `typing.Optional[str]` — Only delete documents whose url starts with this value.
    
</dd>
</dl>

<dl>
<dd>

**all:** `typing.Optional[bool]` — Delete every document in the domain and basepath. Cannot be combined with the product, version or url_prefix filters.
    
</dd>
</dl>

<dl>
<dd>

**fern_basepath:** `typing.Optional[str]` — The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.
    
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

<details><summary><code>client.document.<a href="src/fern/document/client.py">delete_all_documents</a>(...) -> DeleteDocumentResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.document.delete_all_documents(
    domain="domain",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fern_basepath:** `typing.Optional[str]` — The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.
    
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

## Feedback
<details><summary><code>client.feedback.<a href="src/fern/feedback/client.py">create_feedback</a>(...) -> CreateFeedbackResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.feedback.create_feedback(
    domain_path_param="domain",
    conversation_id="conversation_id",
    query_id="query_id",
    domain="domain",
    is_helpful=True,
    feedback_message=None,
    user_email=None,
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

**domain_path_param:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**conversation_id:** `str` — The ID of the conversation
    
</dd>
</dl>

<dl>
<dd>

**query_id:** `str` — The ID of the query
    
</dd>
</dl>

<dl>
<dd>

**domain:** `str` — The domain of the conversation
    
</dd>
</dl>

<dl>
<dd>

**is_helpful:** `bool` — Whether the conversation was helpful
    
</dd>
</dl>

<dl>
<dd>

**feedback_message:** `typing.Optional[str]` — The feedback message from the user
    
</dd>
</dl>

<dl>
<dd>

**user_email:** `typing.Optional[str]` — The email of the user
    
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

<details><summary><code>client.feedback.<a href="src/fern/feedback/client.py">get_feedback_by_id</a>(...) -> GetFeedbackResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.feedback.get_feedback_by_id(
    domain="domain",
    conversation_id="conversation_id",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**conversation_id:** `str` 
    
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

## Guidance
<details><summary><code>client.guidance.<a href="src/fern/guidance/client.py">create_guidance</a>(...) -> CreateGuidanceResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.guidance.create_guidance(
    domain="domain",
    context=[
        "context"
    ],
    document="document",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**context:** `typing.List[str]` — The context of the guidance document, as a list of strings, that will be indexed. Each string will be vectorized separately to generate a separate record.
    
</dd>
</dl>

<dl>
<dd>

**document:** `str` — The content of the guidance document that will be returned to Ask Fern during Ask Fern retrieval.
    
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

<details><summary><code>client.guidance.<a href="src/fern/guidance/client.py">get_guidance_by_id</a>(...) -> GetGuidanceResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.guidance.get_guidance_by_id(
    domain="domain",
    guidance_id="guidance_id",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**guidance_id:** `str` 
    
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

<details><summary><code>client.guidance.<a href="src/fern/guidance/client.py">delete_guidance_by_id</a>(...) -> DeleteGuidanceResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.guidance.delete_guidance_by_id(
    domain="domain",
    guidance_id="guidance_id",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**guidance_id:** `str` 
    
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

<details><summary><code>client.guidance.<a href="src/fern/guidance/client.py">update</a>(...) -> UpdateGuidanceResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.guidance.update(
    domain="domain",
    guidance_id="guidance_id",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**guidance_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**context:** `typing.Optional[typing.List[str]]` — The updated context of the guidance document, as a list of strings, that will be indexed. If not provided, this field will remain unchanged.
    
</dd>
</dl>

<dl>
<dd>

**document:** `typing.Optional[str]` — The updated content of the guidance document that will be returned to Ask Fern during Ask Fern retrieval. If not provided, this field will remain unchanged.
    
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

<details><summary><code>client.guidance.<a href="src/fern/guidance/client.py">get_guidances</a>(...) -> GetGuidancesResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.guidance.get_guidances(
    domain="domain",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of documents per page
    
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
<details><summary><code>client.health.<a href="src/fern/health/client.py">check</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Health check endpoint that returns the application status.
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
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
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

## Index
<details><summary><code>client.index.<a href="src/fern/index/client.py">reconstruct_query_index</a>(...) -> ReconstructIndexResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.index.reconstruct_query_index(
    domain="domain",
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

**domain:** `str` 
    
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

<details><summary><code>client.index.<a href="src/fern/index/client.py">sync_index_to_query_index</a>(...) -> SyncIndexResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.index.sync_index_to_query_index(
    domain="domain",
    index_name="index_name",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**index_name:** `str` — The name of the index to sync
    
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

<details><summary><code>client.index.<a href="src/fern/index/client.py">sync_index_to_query_index_incremental</a>(...) -> SyncIndexResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.index.sync_index_to_query_index_incremental(
    domain="domain",
    index_name="index_name",
    parent_ids=[
        "parent_ids"
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**index_name:** `str` — The name of the index to sync
    
</dd>
</dl>

<dl>
<dd>

**parent_ids:** `typing.List[str]` — List of parent_ids to incrementally sync
    
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

<details><summary><code>client.index.<a href="src/fern/index/client.py">get_job_status</a>(...) -> JobStatusResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.index.get_job_status(
    job_id="job_id",
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

**job_id:** `str` 
    
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

## Mcp
<details><summary><code>client.mcp.<a href="src/fern/mcp/client.py">get_mcp_semantic_query</a>(...) -> GetMcpSemanticQueryResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.mcp.get_mcp_semantic_query(
    domain="domain",
    semantic_query="semantic_query",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**semantic_query:** `str` — The semantic query to get the documents for
    
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

<details><summary><code>client.mcp.<a href="src/fern/mcp/client.py">get_mcp_bmf_query</a>(...) -> GetMcpBmfQueryResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.mcp.get_mcp_bmf_query(
    domain="domain",
    keywords="keywords",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**keywords:** `str` — The bm25 keywords to get the documents for
    
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

## Query
<details><summary><code>client.query.<a href="src/fern/query/client.py">create_query</a>(...) -> CreateQueryResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.query.create_query(
    domain="domain",
    query_id="query_id",
    conversation_id="conversation_id",
    domain="domain",
    text="text",
    role="role",
    source="source",
    created_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `Query` 
    
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

<details><summary><code>client.query.<a href="src/fern/query/client.py">get_recent_queries</a>(...) -> GetQueriesResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.query.get_recent_queries(
    domain="domain",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of queries per page
    
</dd>
</dl>

<dl>
<dd>

**cutoff_time:** `typing.Optional[datetime.datetime]` — Only return queries after this time
    
</dd>
</dl>

<dl>
<dd>

**include_assistant:** `typing.Optional[bool]` — Whether to include assistant responses in the results
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` — The start date of the period to retrieve analytics for
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` — The end date of the period to retrieve analytics for
    
</dd>
</dl>

<dl>
<dd>

**resolution:** `typing.Optional[ResolutionFilter]` — Only return queries whose conversation was resolved or unresolved. Conversations that have not been scored yet are excluded from both filters.
    
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

## Reindexing
<details><summary><code>client.reindexing.<a href="src/fern/reindexing/client.py">get_reindexing_job_status_by_domain</a>(...) -> ReindexingJobRecord</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the status of a reindexing job by domain
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
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.reindexing.get_reindexing_job_status_by_domain(
    domain="domain",
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

**domain:** `str` 
    
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

<details><summary><code>client.reindexing.<a href="src/fern/reindexing/client.py">update_reindexing_job_status</a>(...) -> UpdateReindexingJobStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the status of a reindexing job
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
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.reindexing.update_reindexing_job_status(
    domain="domain",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**memory_mb:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**retry_count:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**task_arn:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sqs_message_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**completed_at:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**duration_ms:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**num_inserted:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**error:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` 
    
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

<details><summary><code>client.reindexing.<a href="src/fern/reindexing/client.py">get_reindexing_job_status_by_task_arn</a>(...) -> ReindexingJobRecord</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the status of a reindexing job by task ARN
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
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.reindexing.get_reindexing_job_status_by_task_arn(
    task_arn="task_arn",
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

**task_arn:** `str` 
    
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

## Sdks
<details><summary><code>client.sdks.<a href="src/fern/sdks/client.py">analyze_commit_diff</a>(...) -> AnalyzeCommitDiffResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Analyzes a git diff and generates an AI-powered commit message with version bump recommendation.
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
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.sdks.analyze_commit_diff(
    diff="diff",
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

**diff:** `str` — The git diff to analyze for generating a commit message
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — The SDK programming language, e.g. 'typescript', 'python', 'java'. When provided, enables language-specific breaking change rules and behavioral analysis.
    
</dd>
</dl>

<dl>
<dd>

**previous_version:** `typing.Optional[str]` — The current published version before this change, e.g. '1.2.3'. Provided for context only — not included in the commit message.
    
</dd>
</dl>

<dl>
<dd>

**prior_changelog:** `typing.Optional[str]` — The last 3 changelog entries for this SDK. Used to match existing commit message style. Empty string or null if none.
    
</dd>
</dl>

<dl>
<dd>

**spec_commit_message:** `typing.Optional[str]` — The commit message from the API spec repository that triggered this SDK generation. Used as a hint for the intent of the change. Empty string or null if unavailable.
    
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

## Settings
<details><summary><code>client.settings.<a href="src/fern/settings/client.py">get_docs_settings</a>(...) -> GetSettingsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get settings for a domain and organization.
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
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.settings.get_docs_settings(
    domain="domain",
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

**domain:** `str` 
    
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

<details><summary><code>client.settings.<a href="src/fern/settings/client.py">enable_ask_ai</a>(...) -> EnableAskAiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enable Ask AI for multiple domains with specified locations and trigger reindex.

Args:
    request: Request containing domains, org_name, and locations to enable
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
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.settings.enable_ask_ai(
    domains=[
        "domains"
    ],
    org_name="org_name",
    locations=[
        "locations"
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

**domains:** `typing.List[str]` — List of domains to enable Ask AI for
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `str` — Organization name
    
</dd>
</dl>

<dl>
<dd>

**locations:** `typing.List[str]` — List of locations to enable (docs, slack)
    
</dd>
</dl>

<dl>
<dd>

**preview:** `typing.Optional[bool]` — Whether this is a preview domain
    
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

<details><summary><code>client.settings.<a href="src/fern/settings/client.py">toggle_ask_ai</a>(...) -> ToggleAskAiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Toggle Ask AI setting and return job_id for tracking.

Args:
    domain: Domain to toggle Ask AI for
    org_name: Organization name
    preview: Whether this is a preview deployment
    locations: Optional list of locations to enable. Valid values: docs, slack
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
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.settings.toggle_ask_ai(
    domain="domain",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**preview:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**locations:** `typing.Optional[typing.List[ToggleAskAiRequestLocationsItem]]` 
    
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

<details><summary><code>client.settings.<a href="src/fern/settings/client.py">reindex_ask_ai</a>(...) -> ToggleAskAiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manually trigger reindex for an already enabled Ask AI setup.

Args:
    domain: Domain to reindex
    org_name: Organization name (unused, kept for backwards compatibility)
    force_full_reindex: If True, deletes all existing data and performs a fresh full index
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
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.settings.reindex_ask_ai(
    domain="domain",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**force_full_reindex:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.settings.<a href="src/fern/settings/client.py">get_toggle_status</a>(...) -> ToggleStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the status of Ask AI toggle operation.
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
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.settings.get_toggle_status(
    domain="domain",
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

**domain:** `str` 
    
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

<details><summary><code>client.settings.<a href="src/fern/settings/client.py">reindex_callback</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Handle callback from SQS reindexing worker when reindex completes.
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
from fern.settings import ReindexCallbackRequestStatus

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.settings.reindex_callback(
    status=ReindexCallbackRequestStatus.SUCCESS,
    source_message_id="sourceMessageId",
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

**status:** `ReindexCallbackRequestStatus` 
    
</dd>
</dl>

<dl>
<dd>

**source_message_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` 
    
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

## SlackAskFern
<details><summary><code>client.slack_ask_fern.<a href="src/fern/slack_ask_fern/client.py">handle_slack_events</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.slack_ask_fern.handle_slack_events()

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

<details><summary><code>client.slack_ask_fern.<a href="src/fern/slack_ask_fern/client.py">handle_slack_slash_commands</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.slack_ask_fern.handle_slack_slash_commands()

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

<details><summary><code>client.slack_ask_fern.<a href="src/fern/slack_ask_fern/client.py">handle_slack_interactions</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.slack_ask_fern.handle_slack_interactions()

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

<details><summary><code>client.slack_ask_fern.<a href="src/fern/slack_ask_fern/client.py">handle_slack_oauth_callback</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.slack_ask_fern.handle_slack_oauth_callback(
    code="code",
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

**code:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[str]` 
    
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

<details><summary><code>client.slack_ask_fern.<a href="src/fern/slack_ask_fern/client.py">get_slack_install_link</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.slack_ask_fern.get_slack_install_link(
    domain="domain",
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

**domain:** `str` 
    
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

## SlackScribe
<details><summary><code>client.slack_scribe.<a href="src/fern/slack_scribe/client.py">handle_scribe_slack_events</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.slack_scribe.handle_scribe_slack_events()

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

<details><summary><code>client.slack_scribe.<a href="src/fern/slack_scribe/client.py">get_fern_writer_install_link</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.slack_scribe.get_fern_writer_install_link(
    github_repo="github_repo",
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

**github_repo:** `str` — The GitHub repository to install the Fern Writer for. Must have the `fern-api` bot installed. Must be in the format `owner/repo`. Example: `fern-api/docs`
    
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

<details><summary><code>client.slack_scribe.<a href="src/fern/slack_scribe/client.py">handle_scribe_slack_oauth_callback</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.slack_scribe.handle_scribe_slack_oauth_callback(
    code="code",
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

**code:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[str]` 
    
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

<details><summary><code>client.slack_scribe.<a href="src/fern/slack_scribe/client.py">handle_scribe_slash_commands</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.slack_scribe.handle_scribe_slash_commands()

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

## Website
<details><summary><code>client.website.<a href="src/fern/website/client.py">index_website</a>(...) -> IndexWebsiteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start crawling and indexing a website.
Returns a job_id to track the crawling progress.
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
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.website.index_website(
    domain="domain",
    base_url="base_url",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**base_url:** `str` — The base URL to start indexing from (e.g., 'https://docs.example.com')
    
</dd>
</dl>

<dl>
<dd>

**domain_filter:** `typing.Optional[str]` — Domain to filter crawling (e.g., 'docs.example.com'). Defaults to base_url domain.
    
</dd>
</dl>

<dl>
<dd>

**path_filter:** `typing.Optional[str]` — Path prefix to restrict crawling (e.g., '/docs'). Only URLs starting with this will be crawled.
    
</dd>
</dl>

<dl>
<dd>

**url_pattern:** `typing.Optional[str]` — Regex pattern to filter URLs (e.g., `https://example\.com/(docs|api)/.*`).
    
</dd>
</dl>

<dl>
<dd>

**chunk_size:** `typing.Optional[int]` — Size of text chunks for splitting documents
    
</dd>
</dl>

<dl>
<dd>

**chunk_overlap:** `typing.Optional[int]` — Overlap between consecutive chunks
    
</dd>
</dl>

<dl>
<dd>

**min_content_length:** `typing.Optional[int]` — Minimum content length to index a page
    
</dd>
</dl>

<dl>
<dd>

**max_pages:** `typing.Optional[int]` — Maximum number of pages to crawl. None means unlimited.
    
</dd>
</dl>

<dl>
<dd>

**delay:** `typing.Optional[float]` — Delay in seconds between requests
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Version to tag all indexed pages with
    
</dd>
</dl>

<dl>
<dd>

**product:** `typing.Optional[str]` — Product to tag all indexed pages with
    
</dd>
</dl>

<dl>
<dd>

**authed:** `typing.Optional[bool]` — Whether indexed pages should be auth-gated
    
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

<details><summary><code>client.website.<a href="src/fern/website/client.py">get_website_status</a>(...) -> GetWebsiteStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the status of a website crawling job.
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
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.website.get_website_status(
    domain="domain",
    job_id="job_id",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**job_id:** `str` — The job ID returned from the index endpoint
    
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

<details><summary><code>client.website.<a href="src/fern/website/client.py">get_website_by_id</a>(...) -> GetWebsiteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single indexed website page by ID.
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
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.website.get_website_by_id(
    domain="domain",
    website_id="website_id",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**website_id:** `str` 
    
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

<details><summary><code>client.website.<a href="src/fern/website/client.py">get_websites</a>(...) -> GetWebsitesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all indexed website pages for a domain with pagination.
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
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.website.get_websites(
    domain="domain",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of sources per page
    
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

<details><summary><code>client.website.<a href="src/fern/website/client.py">reindex_website</a>(...) -> ReindexWebsiteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Re-crawl a website by starting a new crawl job. The job will delete old pages before indexing.
Uses the configuration from the original index request.
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
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.website.reindex_website(
    domain="domain",
    base_url="base_url",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**base_url:** `str` — The base URL to re-crawl (will delete old pages and re-index)
    
</dd>
</dl>

<dl>
<dd>

**domain_filter:** `typing.Optional[str]` — Domain to filter crawling (e.g., 'docs.example.com'). If not provided, uses previous config.
    
</dd>
</dl>

<dl>
<dd>

**path_filter:** `typing.Optional[str]` — Path prefix to restrict crawling (e.g., '/docs'). If not provided, uses previous config.
    
</dd>
</dl>

<dl>
<dd>

**url_pattern:** `typing.Optional[str]` — Regex pattern to filter URLs (e.g., `https://example\.com/(docs|api)/.*`). If not provided, uses previous config.
    
</dd>
</dl>

<dl>
<dd>

**chunk_size:** `typing.Optional[int]` — Size of text chunks for splitting documents. If not provided, uses previous config.
    
</dd>
</dl>

<dl>
<dd>

**chunk_overlap:** `typing.Optional[int]` — Overlap between consecutive chunks. If not provided, uses previous config.
    
</dd>
</dl>

<dl>
<dd>

**min_content_length:** `typing.Optional[int]` — Minimum content length to index a page. If not provided, uses previous config.
    
</dd>
</dl>

<dl>
<dd>

**max_pages:** `typing.Optional[int]` — Maximum number of pages to crawl. If not provided, uses previous config.
    
</dd>
</dl>

<dl>
<dd>

**delay:** `typing.Optional[float]` — Delay in seconds between requests. If not provided, uses previous config.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Version to tag all indexed pages with. If not provided, uses previous config.
    
</dd>
</dl>

<dl>
<dd>

**product:** `typing.Optional[str]` — Product to tag all indexed pages with. If not provided, uses previous config.
    
</dd>
</dl>

<dl>
<dd>

**authed:** `typing.Optional[bool]` — Whether indexed pages should be auth-gated. If not provided, uses previous config.
    
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

<details><summary><code>client.website.<a href="src/fern/website/client.py">delete_website</a>(...) -> DeleteWebsiteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete all pages from a specific website by base URL.
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
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.website.delete_website(
    domain="domain",
    base_url="base_url",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**base_url:** `str` — The base URL of the website to delete (deletes all pages from this source)
    
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

<details><summary><code>client.website.<a href="src/fern/website/client.py">delete_all_websites</a>(...) -> DeleteAllWebsitesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete all indexed website pages for a domain.
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
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.website.delete_all_websites(
    domain="domain",
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

**domain:** `str` 
    
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

