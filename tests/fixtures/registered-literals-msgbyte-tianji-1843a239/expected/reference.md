# Reference
## Ai
<details><summary><code>client.ai.<a href="src/fern/ai/client.py#L41-L113">classifysurvey</a>(...) -> AiClassifySurveyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

classify survey
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
from fern.ai import AiClassifySurveyRequestRunStrategy

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ai.classifysurvey(
    workspace_id="workspaceId",
    survey_id="surveyId",
    start_at=1.1,
    end_at=1.1,
    run_strategy=AiClassifySurveyRequestRunStrategy.SKIP_EXIST,
    payload_content_field="payloadContentField",
    suggestion_category=[
        "suggestionCategory"
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

**survey_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_at:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**end_at:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**run_strategy:** `AiClassifySurveyRequestRunStrategy` 
    
</dd>
</dl>

<dl>
<dd>

**payload_content_field:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**suggestion_category:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**language_strategy:** `typing.Optional[AiClassifySurveyRequestLanguageStrategy]` 
    
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

<details><summary><code>client.ai.<a href="src/fern/ai/client.py#L115-L182">translatesurvey</a>(...) -> AiTranslateSurveyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

translate survey
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
from fern.ai import AiTranslateSurveyRequestRunStrategy

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ai.translatesurvey(
    workspace_id="workspaceId",
    survey_id="surveyId",
    start_at=1.1,
    end_at=1.1,
    run_strategy=AiTranslateSurveyRequestRunStrategy.SKIP_EXIST,
    payload_content_field="payloadContentField",
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

**survey_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_at:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**end_at:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**run_strategy:** `AiTranslateSurveyRequestRunStrategy` 
    
</dd>
</dl>

<dl>
<dd>

**payload_content_field:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**language_strategy:** `typing.Optional[AiTranslateSurveyRequestLanguageStrategy]` 
    
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

<details><summary><code>client.ai.<a href="src/fern/ai/client.py#L184-L217">ai_gateway_info</a>(...) -> typing.Optional[AiGatewayInfoResponse]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.ai.ai_gateway_info(
    workspace_id="workspaceId",
    gateway_id="gatewayId",
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

**gateway_id:** `str` 
    
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

<details><summary><code>client.ai.<a href="src/fern/ai/client.py#L219-L283">ai_gateway_update</a>(...) -> AiGatewayUpdateResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.ai.ai_gateway_update(
    workspace_id="workspaceId",
    gateway_id="gatewayId",
    name="name",
    model_api_key=None,
    custom_model_base_url=None,
    custom_model_name=None,
    custom_model_input_price=None,
    custom_model_output_price=None,
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

**gateway_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**model_api_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_model_base_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_model_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_model_input_price:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_model_output_price:** `typing.Optional[float]` 
    
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

<details><summary><code>client.ai.<a href="src/fern/ai/client.py#L285-L318">ai_gateway_delete</a>(...) -> AiGatewayDeleteResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.ai.ai_gateway_delete(
    workspace_id="workspaceId",
    gateway_id="gatewayId",
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

**gateway_id:** `str` 
    
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

<details><summary><code>client.ai.<a href="src/fern/ai/client.py#L320-L371">ai_gateway_logs</a>(...) -> AiGatewayLogsResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.ai.ai_gateway_logs(
    workspace_id="workspaceId",
    gateway_id="gatewayId",
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

**gateway_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**log_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ai.<a href="src/fern/ai/client.py#L373-L412">ai_gateway_model_pricing</a>(...) -> AiGatewayModelPricingResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.ai.ai_gateway_model_pricing(
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

**workspace_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
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

<details><summary><code>client.ai.<a href="src/fern/ai/client.py#L414-L447">ai_gateway_quota_alert_get</a>(...) -> typing.Optional[AiGatewayQuotaAlertGetResponse]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.ai.ai_gateway_quota_alert_get(
    workspace_id="workspaceId",
    gateway_id="gatewayId",
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

**gateway_id:** `str` 
    
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

<details><summary><code>client.ai.<a href="src/fern/ai/client.py#L449-L502">ai_gateway_quota_alert_upsert</a>(...) -> AiGatewayQuotaAlertUpsertResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.ai.ai_gateway_quota_alert_upsert(
    workspace_id="workspaceId",
    gateway_id="gatewayId",
    daily_quota=1.1,
    enabled=True,
    notification_id=None,
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

**gateway_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**daily_quota:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**notification_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ai.<a href="src/fern/ai/client.py#L504-L537">ai_gateway_quota_alert_delete</a>(...) -> bool</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.ai.ai_gateway_quota_alert_delete(
    workspace_id="workspaceId",
    gateway_id="gatewayId",
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

**gateway_id:** `str` 
    
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

## Aigateway
<details><summary><code>client.aigateway.<a href="src/fern/aigateway/client.py">all</a>(...) -> typing.List[AiGatewayAllResponseItem]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.aigateway.all_(
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

**workspace_id:** `str` 
    
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

## Application
<details><summary><code>client.application.<a href="src/fern/application/client.py#L40-L99">ai_gateway_create</a>(...) -> AiGatewayCreateResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.application.ai_gateway_create(
    workspace_id="workspaceId",
    name="name",
    model_api_key=None,
    custom_model_base_url=None,
    custom_model_name=None,
    custom_model_input_price=None,
    custom_model_output_price=None,
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**model_api_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_model_base_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_model_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_model_input_price:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_model_output_price:** `typing.Optional[float]` 
    
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

<details><summary><code>client.application.<a href="src/fern/application/client.py">all</a>(...) -> typing.List[ApplicationAllResponseItem]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.application.all_(
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

**workspace_id:** `str` 
    
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

<details><summary><code>client.application.<a href="src/fern/application/client.py#L131-L162">info</a>(...) -> typing.Optional[ApplicationInfoResponse]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.application.info(
    workspace_id="workspaceId",
    application_id="applicationId",
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

**application_id:** `str` 
    
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

<details><summary><code>client.application.<a href="src/fern/application/client.py#L164-L207">create</a>(...) -> ApplicationCreateResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.application.create(
    workspace_id="workspaceId",
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

**workspace_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**appstore_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**playstore_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.application.<a href="src/fern/application/client.py#L209-L261">update</a>(...) -> ApplicationUpdateResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.application.update(
    workspace_id="workspaceId",
    application_id="applicationId",
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

**workspace_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**application_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**appstore_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**playstore_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.application.<a href="src/fern/application/client.py#L263-L294">delete</a>(...) -> ApplicationDeleteResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.application.delete(
    workspace_id="workspaceId",
    application_id="applicationId",
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

**application_id:** `str` 
    
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

<details><summary><code>client.application.<a href="src/fern/application/client.py#L296-L339">storeappsearch</a>(...) -> typing.List[ApplicationStoreAppSearchResponseItem]</code></summary>
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
from fern.application import ApplicationStoreAppSearchRequestStoreType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.application.storeappsearch(
    workspace_id="workspaceId",
    keyword="keyword",
    store_type=ApplicationStoreAppSearchRequestStoreType.APPSTORE,
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

**keyword:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**store_type:** `ApplicationStoreAppSearchRequestStoreType` 
    
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

<details><summary><code>client.application.<a href="src/fern/application/client.py#L341-L401">storeinfohistory</a>(...) -> typing.List[ApplicationStoreInfoHistoryResponseItem]</code></summary>
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
from fern.application import ApplicationStoreInfoHistoryRequestStoreType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.application.storeinfohistory(
    workspace_id="workspaceId",
    application_id="applicationId",
    store_type=ApplicationStoreInfoHistoryRequestStoreType.APPSTORE,
    start_at=1.1,
    end_at=1.1,
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

**application_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**store_type:** `ApplicationStoreInfoHistoryRequestStoreType` 
    
</dd>
</dl>

<dl>
<dd>

**start_at:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**end_at:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**store_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.application.<a href="src/fern/application/client.py#L403-L460">eventstats</a>(...) -> ApplicationEventStatsResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.application.eventstats(
    workspace_id="workspaceId",
    application_id="applicationId",
    start_at=1.1,
    end_at=1.1,
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

**application_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_at:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**end_at:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**unit:** `typing.Optional[ApplicationEventStatsRequestUnit]` 
    
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

## Global
<details><summary><code>client.global_.<a href="src/fern/global_/client.py#L26-L50">config</a>() -> GlobalConfigResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Tianji system global config
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
    environment=FernApiEnvironment.DEFAULT,
)

client.global_.config()

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

## User
<details><summary><code>client.user.<a href="src/fern/user/client.py#L31-L62">login</a>(...) -> UserLoginResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.user.login(
    username="username",
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

**username:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` 
    
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

<details><summary><code>client.user.<a href="src/fern/user/client.py#L64-L92">loginwithtoken</a>(...) -> UserLoginWithTokenResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.user.loginwithtoken(
    token="token",
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

**token:** `str` 
    
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

<details><summary><code>client.user.<a href="src/fern/user/client.py#L94-L125">register</a>(...) -> UserRegisterResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.user.register(
    username="username",
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

**username:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` 
    
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

## Workspace
<details><summary><code>client.workspace.<a href="src/fern/workspace/client.py#L36-L62">create</a>(...) -> WorkspaceCreateResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.workspace.create(
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

**name:** `str` 
    
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

<details><summary><code>client.workspace.<a href="src/fern/workspace/client.py#L64-L92">switch</a>(...) -> WorkspaceSwitchResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.workspace.switch(
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

**workspace_id:** `str` 
    
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

<details><summary><code>client.workspace.<a href="src/fern/workspace/client.py#L94-L125">rename</a>(...) -> WorkspaceRenameResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.workspace.rename(
    workspace_id="workspaceId",
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

**workspace_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
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

<details><summary><code>client.workspace.<a href="src/fern/workspace/client.py#L127-L153">delete</a>(...) -> typing.Any</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.workspace.delete(
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

**workspace_id:** `str` 
    
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

<details><summary><code>client.workspace.<a href="src/fern/workspace/client.py#L155-L183">members</a>(...) -> typing.List[WorkspaceMembersResponseItem]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.workspace.members(
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

**workspace_id:** `str` 
    
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

<details><summary><code>client.workspace.<a href="src/fern/workspace/client.py#L185-L220">updatesettings</a>(...) -> WorkspaceUpdateSettingsResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.workspace.updatesettings(
    workspace_id="workspaceId",
    settings={
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

**workspace_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Dict[str, typing.Any]` 
    
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

<details><summary><code>client.workspace.<a href="src/fern/workspace/client.py#L222-L262">invite</a>(...) -> typing.Any</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.workspace.invite(
    workspace_id="workspaceId",
    email_or_id="emailOrId",
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

**email_or_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[WorkspaceInviteRequestRole]` 
    
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

<details><summary><code>client.workspace.<a href="src/fern/workspace/client.py#L264-L297">tick</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Administrator kicks a user out of a workspace.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.workspace.tick(
    workspace_id="workspaceId",
    target_user_id="targetUserId",
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

**target_user_id:** `str` 
    
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

<details><summary><code>client.workspace.<a href="src/fern/workspace/client.py#L299-L344">updatememberrole</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update workspace member role
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
from fern.workspace import WorkspaceUpdateMemberRoleRequestRole

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.workspace.updatememberrole(
    workspace_id="workspaceId",
    user_id="userId",
    role=WorkspaceUpdateMemberRoleRequestRole.OWNER,
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

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**role:** `WorkspaceUpdateMemberRoleRequestRole` 
    
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

<details><summary><code>client.workspace.<a href="src/fern/workspace/client.py#L346-L374">getservicecount</a>(...) -> WorkspaceGetServiceCountResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.workspace.getservicecount(
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

**workspace_id:** `str` 
    
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

<details><summary><code>client.workspace.<a href="src/fern/workspace/client.py#L376-L406">recheckpausestatus</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manually trigger workspace pause status check based on usage limits
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
    environment=FernApiEnvironment.DEFAULT,
)

client.workspace.recheckpausestatus(
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

**workspace_id:** `str` 
    
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

## Website
<details><summary><code>client.website.<a href="src/fern/website/client.py#L47-L78">onlinecount</a>(...) -> float</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.website.onlinecount(
    workspace_id="workspaceId",
    website_id="websiteId",
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

<details><summary><code>client.website.<a href="src/fern/website/client.py">all</a>(...) -> typing.List[WebsiteAllResponseItem]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.website.all_(
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

**workspace_id:** `str` 
    
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

<details><summary><code>client.website.<a href="src/fern/website/client.py#L110-L138">alloverview</a>(...) -> typing.Dict[str, float]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.website.alloverview(
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

**workspace_id:** `str` 
    
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

<details><summary><code>client.website.<a href="src/fern/website/client.py#L140-L171">info</a>(...) -> typing.Optional[WebsiteInfoResponse]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.website.info(
    workspace_id="workspaceId",
    website_id="websiteId",
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

<details><summary><code>client.website.<a href="src/fern/website/client.py#L173-L266">stats</a>(...) -> WebsiteStatsResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.website.stats(
    workspace_id="workspaceId",
    website_id="websiteId",
    start_at=1.1,
    end_at=1.1,
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

**website_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_at:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**end_at:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**unit:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**city:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**referrer:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**os:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**browser:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**device:** `typing.Optional[str]` 
    
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

<details><summary><code>client.website.<a href="src/fern/website/client.py#L268-L313">geostats</a>(...) -> typing.List[WebsiteGeoStatsResponseItem]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.website.geostats(
    workspace_id="workspaceId",
    website_id="websiteId",
    start_at=1.1,
    end_at=1.1,
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

**website_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_at:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**end_at:** `float` 
    
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

<details><summary><code>client.website.<a href="src/fern/website/client.py#L315-L408">pageviews</a>(...) -> WebsitePageviewsResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.website.pageviews(
    workspace_id="workspaceId",
    website_id="websiteId",
    start_at=1.1,
    end_at=1.1,
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

**website_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_at:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**end_at:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**unit:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**city:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**referrer:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**os:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**browser:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**device:** `typing.Optional[str]` 
    
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

<details><summary><code>client.website.<a href="src/fern/website/client.py#L410-L530">metrics</a>(...) -> typing.List[WebsiteMetricsResponseItem]</code></summary>
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
from fern.website import WebsiteMetricsRequestType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.website.metrics(
    workspace_id="workspaceId",
    website_id="websiteId",
    type=WebsiteMetricsRequestType.URL,
    start_at=1.1,
    end_at=1.1,
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

**website_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `WebsiteMetricsRequestType` 
    
</dd>
</dl>

<dl>
<dd>

**start_at:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**end_at:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**referrer:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**os:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**browser:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**device:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**city:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**event:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**utm_source:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**utm_medium:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**utm_campaign:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**utm_term:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**utm_content:** `typing.Optional[str]` 
    
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

<details><summary><code>client.website.<a href="src/fern/website/client.py#L532-L566">add</a>(...) -> WebsiteAddResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.website.add(
    workspace_id="workspaceId",
    name="name",
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

**workspace_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

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

<details><summary><code>client.website.<a href="src/fern/website/client.py#L568-L599">delete</a>(...) -> WebsiteDeleteResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.website.delete(
    workspace_id="workspaceId",
    website_id="websiteId",
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

<details><summary><code>client.website.<a href="src/fern/website/client.py#L601-L649">updateinfo</a>(...) -> WebsiteUpdateInfoResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.website.updateinfo(
    workspace_id="workspaceId",
    website_id="websiteId",
    name="name",
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

**workspace_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**website_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**monitor_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.website.<a href="src/fern/website/client.py#L651-L687">generatelighthousereport</a>(...) -> str</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.website.generatelighthousereport(
    workspace_id="workspaceId",
    website_id="websiteId",
    url="url",
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

**website_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` 
    
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

<details><summary><code>client.website.<a href="src/fern/website/client.py#L689-L732">getlighthousereport</a>(...) -> WebsiteGetLighthouseReportResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.website.getlighthousereport(
    workspace_id="workspaceId",
    website_id="websiteId",
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

**website_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
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

<details><summary><code>client.website.<a href="src/fern/website/client.py#L734-L762">getlighthousejson</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.website.getlighthousejson(
    lighthouse_id="lighthouseId",
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

**lighthouse_id:** `str` 
    
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

<details><summary><code>client.website.<a href="src/fern/website/client.py#L764-L792">getpublicinfobyshareid</a>(...) -> WebsiteGetPublicInfoByShareIdResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.website.getpublicinfobyshareid(
    share_id="shareId",
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

**share_id:** `str` 
    
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

<details><summary><code>client.website.<a href="src/fern/website/client.py#L794-L828">getpublicstatsbyshareid</a>(...) -> WebsiteGetPublicStatsByShareIdResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.website.getpublicstatsbyshareid(
    share_id="shareId",
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

**share_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**range:** `typing.Optional[WebsiteGetPublicStatsByShareIdRequestRange]` 
    
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

<details><summary><code>client.website.<a href="src/fern/website/client.py#L830-L872">getpublicmetricsbyshareid</a>(...) -> typing.List[WebsiteGetPublicMetricsByShareIdResponseItem]</code></summary>
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
from fern.website import WebsiteGetPublicMetricsByShareIdRequestType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.website.getpublicmetricsbyshareid(
    share_id="shareId",
    type=WebsiteGetPublicMetricsByShareIdRequestType.URL,
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

**share_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `WebsiteGetPublicMetricsByShareIdRequestType` 
    
</dd>
</dl>

<dl>
<dd>

**range:** `typing.Optional[WebsiteGetPublicMetricsByShareIdRequestRange]` 
    
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

<details><summary><code>client.website.<a href="src/fern/website/client.py#L874-L905">createorenableshare</a>(...) -> WebsiteCreateOrEnableShareResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.website.createorenableshare(
    workspace_id="workspaceId",
    website_id="websiteId",
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

<details><summary><code>client.website.<a href="src/fern/website/client.py#L907-L938">disableshare</a>(...) -> WebsiteDisableShareResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.website.disableshare(
    workspace_id="workspaceId",
    website_id="websiteId",
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

## Monitor
<details><summary><code>client.monitor.<a href="src/fern/monitor/client.py">all</a>(...) -> typing.List[MonitorAllResponseItem]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.monitor.all_(
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

**workspace_id:** `str` 
    
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

<details><summary><code>client.monitor.<a href="src/fern/monitor/client.py#L72-L103">get</a>(...) -> typing.Optional[MonitorGetResponse]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.monitor.get(
    workspace_id="workspaceId",
    monitor_id="monitorId",
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

**monitor_id:** `str` 
    
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

<details><summary><code>client.monitor.<a href="src/fern/monitor/client.py#L105-L133">getpublicinfo</a>(...) -> typing.List[MonitorGetPublicInfoResponseItem]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.monitor.getpublicinfo(
    monitor_ids=[
        "monitorIds"
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

**monitor_ids:** `typing.List[str]` 
    
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

<details><summary><code>client.monitor.<a href="src/fern/monitor/client.py#L135-L216">upsert</a>(...) -> MonitorUpsertResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.monitor.upsert(
    workspace_id="workspaceId",
    name="name",
    type="type",
    payload={
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

**workspace_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**payload:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**interval:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_retries:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**trending_mode:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**notification_ids:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**up_message_template:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**down_message_template:** `typing.Optional[str]` 
    
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

<details><summary><code>client.monitor.<a href="src/fern/monitor/client.py#L218-L249">delete</a>(...) -> MonitorDeleteResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.monitor.delete(
    workspace_id="workspaceId",
    monitor_id="monitorId",
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

**monitor_id:** `str` 
    
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

<details><summary><code>client.monitor.<a href="src/fern/monitor/client.py#L251-L282">regeneratepushtoken</a>(...) -> str</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.monitor.regeneratepushtoken(
    workspace_id="workspaceId",
    monitor_id="monitorId",
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

**monitor_id:** `str` 
    
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

<details><summary><code>client.monitor.<a href="src/fern/monitor/client.py#L284-L315">triggermonitor</a>(...) -> typing.Any</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.monitor.triggermonitor(
    workspace_id="workspaceId",
    monitor_id="monitorId",
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

**monitor_id:** `str` 
    
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

<details><summary><code>client.monitor.<a href="src/fern/monitor/client.py#L317-L362">data</a>(...) -> typing.List[MonitorDataResponseItem]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.monitor.data(
    workspace_id="workspaceId",
    monitor_id="monitorId",
    start_at=1.1,
    end_at=1.1,
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

**monitor_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_at:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**end_at:** `float` 
    
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

<details><summary><code>client.monitor.<a href="src/fern/monitor/client.py#L364-L405">changeactive</a>(...) -> MonitorChangeActiveResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.monitor.changeactive(
    workspace_id="workspaceId",
    monitor_id="monitorId",
    active=True,
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

**monitor_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**active:** `bool` 
    
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

<details><summary><code>client.monitor.<a href="src/fern/monitor/client.py#L407-L446">recentdata</a>(...) -> typing.List[MonitorRecentDataResponseItem]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.monitor.recentdata(
    workspace_id="workspaceId",
    monitor_id="monitorId",
    take=1.1,
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

**monitor_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**take:** `float` 
    
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

<details><summary><code>client.monitor.<a href="src/fern/monitor/client.py#L448-L479">publicsummary</a>(...) -> typing.List[MonitorPublicSummaryResponseItem]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.monitor.publicsummary(
    workspace_id="workspaceId",
    monitor_id="monitorId",
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

**monitor_id:** `str` 
    
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

<details><summary><code>client.monitor.<a href="src/fern/monitor/client.py#L481-L512">publicdata</a>(...) -> typing.List[MonitorPublicDataResponseItem]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.monitor.publicdata(
    workspace_id="workspaceId",
    monitor_id="monitorId",
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

**monitor_id:** `str` 
    
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

<details><summary><code>client.monitor.<a href="src/fern/monitor/client.py#L514-L545">datametrics</a>(...) -> MonitorDataMetricsResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.monitor.datametrics(
    workspace_id="workspaceId",
    monitor_id="monitorId",
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

**monitor_id:** `str` 
    
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

<details><summary><code>client.monitor.<a href="src/fern/monitor/client.py#L547-L586">events</a>(...) -> typing.List[MonitorEventsResponseItem]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.monitor.events(
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

**workspace_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**monitor_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` 
    
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

<details><summary><code>client.monitor.<a href="src/fern/monitor/client.py#L588-L619">clearevents</a>(...) -> float</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.monitor.clearevents(
    workspace_id="workspaceId",
    monitor_id="monitorId",
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

**monitor_id:** `str` 
    
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

<details><summary><code>client.monitor.<a href="src/fern/monitor/client.py#L621-L652">cleardata</a>(...) -> float</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.monitor.cleardata(
    workspace_id="workspaceId",
    monitor_id="monitorId",
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

**monitor_id:** `str` 
    
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

<details><summary><code>client.monitor.<a href="src/fern/monitor/client.py#L654-L695">getstatus</a>(...) -> typing.Optional[MonitorGetStatusResponse]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.monitor.getstatus(
    workspace_id="workspaceId",
    monitor_id="monitorId",
    status_name="statusName",
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

**monitor_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**status_name:** `str` 
    
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

<details><summary><code>client.monitor.<a href="src/fern/monitor/client.py#L697-L734">server_status_public_info</a>(...) -> typing.Dict[str, ServerStatusPublicInfoResponseValue]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.monitor.server_status_public_info(
    workspace_id="workspaceId",
    server_names=[
        "serverNames"
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

**server_names:** `typing.List[str]` 
    
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

## Page
<details><summary><code>client.page.<a href="src/fern/page/client.py#L34-L68">getallpages</a>(...) -> typing.List[PageGetAllPagesResponseItem]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.page.getallpages(
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

**workspace_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[PageGetAllPagesRequestType]` 
    
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

<details><summary><code>client.page.<a href="src/fern/page/client.py#L70-L98">getpageinfo</a>(...) -> typing.Optional[PageGetPageInfoResponse]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.page.getpageinfo(
    slug="slug",
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

**slug:** `str` 
    
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

<details><summary><code>client.page.<a href="src/fern/page/client.py#L100-L128">createpage</a>(...) -> PageCreatePageResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.page.createpage(
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

**workspace_id:** `str` 
    
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

<details><summary><code>client.page.<a href="src/fern/page/client.py#L130-L197">editpage</a>(...) -> PageEditPageResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.page.editpage(
    workspace_id="workspaceId",
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

**workspace_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**domain:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**monitor_list:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**payload:** `typing.Optional[typing.Any]` 
    
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

<details><summary><code>client.page.<a href="src/fern/page/client.py#L199-L230">deletepage</a>(...) -> PageDeletePageResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.page.deletepage(
    workspace_id="workspaceId",
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

**workspace_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` 
    
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

## Telemetry
<details><summary><code>client.telemetry.<a href="src/fern/telemetry/client.py">all</a>(...) -> typing.List[TelemetryAllResponseItem]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.telemetry.all_(
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

**workspace_id:** `str` 
    
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

<details><summary><code>client.telemetry.<a href="src/fern/telemetry/client.py#L66-L97">info</a>(...) -> typing.Optional[TelemetryInfoResponse]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.telemetry.info(
    workspace_id="workspaceId",
    telemetry_id="telemetryId",
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

**telemetry_id:** `str` 
    
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

<details><summary><code>client.telemetry.<a href="src/fern/telemetry/client.py#L99-L127">alleventcount</a>(...) -> typing.Dict[str, float]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.telemetry.alleventcount(
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

**workspace_id:** `str` 
    
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

<details><summary><code>client.telemetry.<a href="src/fern/telemetry/client.py#L129-L162">eventcount</a>(...) -> float</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.telemetry.eventcount(
    workspace_id="workspaceId",
    telemetry_id="telemetryId",
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

**telemetry_id:** `str` 
    
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

<details><summary><code>client.telemetry.<a href="src/fern/telemetry/client.py#L164-L204">upsert</a>(...) -> TelemetryUpsertResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.telemetry.upsert(
    workspace_id="workspaceId",
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

**workspace_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**telemetry_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.telemetry.<a href="src/fern/telemetry/client.py#L206-L237">delete</a>(...) -> TelemetryDeleteResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.telemetry.delete(
    workspace_id="workspaceId",
    telemetry_id="telemetryId",
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

**telemetry_id:** `str` 
    
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

<details><summary><code>client.telemetry.<a href="src/fern/telemetry/client.py#L239-L312">pageviews</a>(...) -> TelemetryPageviewsResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.telemetry.pageviews(
    workspace_id="workspaceId",
    telemetry_id="telemetryId",
    start_at=1.1,
    end_at=1.1,
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

**telemetry_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_at:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**end_at:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**unit:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**city:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` 
    
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

<details><summary><code>client.telemetry.<a href="src/fern/telemetry/client.py#L314-L390">metrics</a>(...) -> typing.List[TelemetryMetricsResponseItem]</code></summary>
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
from fern.telemetry import TelemetryMetricsRequestType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.telemetry.metrics(
    workspace_id="workspaceId",
    telemetry_id="telemetryId",
    type=TelemetryMetricsRequestType.SOURCE,
    start_at=1.1,
    end_at=1.1,
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

**telemetry_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `TelemetryMetricsRequestType` 
    
</dd>
</dl>

<dl>
<dd>

**start_at:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**end_at:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**city:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` 
    
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

<details><summary><code>client.telemetry.<a href="src/fern/telemetry/client.py#L392-L465">stats</a>(...) -> TelemetryStatsResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.telemetry.stats(
    workspace_id="workspaceId",
    telemetry_id="telemetryId",
    start_at=1.1,
    end_at=1.1,
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

**telemetry_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_at:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**end_at:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**unit:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**city:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` 
    
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

## Survey
<details><summary><code>client.survey.<a href="src/fern/survey/client.py">all</a>(...) -> typing.List[SurveyAllResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all surveys
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
    environment=FernApiEnvironment.DEFAULT,
)

client.survey.all_(
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

**workspace_id:** `str` 
    
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

<details><summary><code>client.survey.<a href="src/fern/survey/client.py#L73-L106">get</a>(...) -> typing.Optional[SurveyGetResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific survey by ID
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
    environment=FernApiEnvironment.DEFAULT,
)

client.survey.get(
    workspace_id="workspaceId",
    survey_id="surveyId",
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

**survey_id:** `str` 
    
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

<details><summary><code>client.survey.<a href="src/fern/survey/client.py#L108-L141">count</a>(...) -> float</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the total count of survey results
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
    environment=FernApiEnvironment.DEFAULT,
)

client.survey.count(
    workspace_id="workspaceId",
    survey_id="surveyId",
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

**survey_id:** `str` 
    
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

<details><summary><code>client.survey.<a href="src/fern/survey/client.py#L143-L173">allresultcount</a>(...) -> typing.Dict[str, float]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get result counts for all surveys in the workspace
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
    environment=FernApiEnvironment.DEFAULT,
)

client.survey.allresultcount(
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

**workspace_id:** `str` 
    
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

<details><summary><code>client.survey.<a href="src/fern/survey/client.py#L175-L216">submit</a>(...) -> SurveySubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submit survey responses
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
    environment=FernApiEnvironment.DEFAULT,
)

client.survey.submit(
    workspace_id="workspaceId",
    survey_id="surveyId",
    payload={
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

**workspace_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**survey_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**payload:** `typing.Dict[str, typing.Any]` 
    
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

<details><summary><code>client.survey.<a href="src/fern/survey/client.py#L218-L297">create</a>(...) -> SurveyCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new survey with payload, feed channels and webhook configuration
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
from fern.survey import SurveyCreateRequestPayload, SurveyCreateRequestPayloadItemsItem, SurveyCreateRequestPayloadItemsItemType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.survey.create(
    workspace_id="workspaceId",
    name="name",
    payload=SurveyCreateRequestPayload(
        items=[
            SurveyCreateRequestPayloadItemsItem(
                label="label",
                name="name",
                type=SurveyCreateRequestPayloadItemsItemType.TEXT,
            )
        ],
    ),
    feed_channel_ids=[
        "feedChannelIds"
    ],
    feed_template="feedTemplate",
    webhook_url="webhookUrl",
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**payload:** `SurveyCreateRequestPayload` 
    
</dd>
</dl>

<dl>
<dd>

**feed_channel_ids:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**feed_template:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**desc:** `typing.Optional[str]` 
    
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

<details><summary><code>client.survey.<a href="src/fern/survey/client.py#L299-L364">update</a>(...) -> SurveyUpdateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing survey configuration
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
    environment=FernApiEnvironment.DEFAULT,
)

client.survey.update(
    workspace_id="workspaceId",
    survey_id="surveyId",
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

**survey_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**desc:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**payload:** `typing.Optional[SurveyUpdateRequestPayload]` 
    
</dd>
</dl>

<dl>
<dd>

**feed_channel_ids:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**feed_template:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` 
    
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

<details><summary><code>client.survey.<a href="src/fern/survey/client.py#L366-L399">delete</a>(...) -> SurveyDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a survey permanently
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
    environment=FernApiEnvironment.DEFAULT,
)

client.survey.delete(
    workspace_id="workspaceId",
    survey_id="surveyId",
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

**survey_id:** `str` 
    
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

<details><summary><code>client.survey.<a href="src/fern/survey/client.py#L401-L437">duplicate</a>(...) -> SurveyDuplicateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Duplicate an existing survey with a new name
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
    environment=FernApiEnvironment.DEFAULT,
)

client.survey.duplicate(
    workspace_id="workspaceId",
    survey_id="surveyId",
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

**workspace_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**survey_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
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

<details><summary><code>client.survey.<a href="src/fern/survey/client.py#L439-L472">getresult</a>(...) -> typing.Optional[SurveyGetResultResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific survey result by result ID
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
    environment=FernApiEnvironment.DEFAULT,
)

client.survey.getresult(
    workspace_id="workspaceId",
    result_id="resultId",
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

**result_id:** `str` 
    
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

<details><summary><code>client.survey.<a href="src/fern/survey/client.py#L474-L535">resultlist</a>(...) -> SurveyResultListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get paginated list of survey results with optional date range and filters
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
    environment=FernApiEnvironment.DEFAULT,
)

client.survey.resultlist(
    workspace_id="workspaceId",
    survey_id="surveyId",
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

**survey_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**start_at:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**end_at:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` 
    
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

<details><summary><code>client.survey.<a href="src/fern/survey/client.py#L537-L582">stats</a>(...) -> typing.List[SurveyStatsResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get survey submission statistics grouped by date
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
    environment=FernApiEnvironment.DEFAULT,
)

client.survey.stats(
    workspace_id="workspaceId",
    survey_id="surveyId",
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

**survey_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_at:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**end_at:** `typing.Optional[float]` 
    
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

<details><summary><code>client.survey.<a href="src/fern/survey/client.py#L584-L617">aicategorylist</a>(...) -> typing.List[SurveyAiCategoryListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get AI-categorized survey results with counts for each category
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
    environment=FernApiEnvironment.DEFAULT,
)

client.survey.aicategorylist(
    workspace_id="workspaceId",
    survey_id="surveyId",
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

**survey_id:** `str` 
    
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

## Auditlog
<details><summary><code>client.auditlog.<a href="src/fern/auditlog/client.py#L26-L67">fetchbycursor</a>(...) -> AuditLogFetchByCursorResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch workspace audit log
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
    environment=FernApiEnvironment.DEFAULT,
)

client.auditlog.fetchbycursor(
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

**workspace_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
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

<details><summary><code>client.auditlog.<a href="src/fern/auditlog/client.py#L69-L97">clear</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

clear all workspace audit log
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
    environment=FernApiEnvironment.DEFAULT,
)

client.auditlog.clear(
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

**workspace_id:** `str` 
    
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

## Billing
<details><summary><code>client.billing.<a href="src/fern/billing/client.py#L36-L79">usage</a>(...) -> BillingUsageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

get workspace usage
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
    environment=FernApiEnvironment.DEFAULT,
)

client.billing.usage(
    workspace_id="workspaceId",
    start_at=1.1,
    end_at=1.1,
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

**start_at:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**end_at:** `float` 
    
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

<details><summary><code>client.billing.<a href="src/fern/billing/client.py#L81-L111">limit</a>(...) -> BillingLimitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

get workspace subscription limit
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
    environment=FernApiEnvironment.DEFAULT,
)

client.billing.limit(
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

**workspace_id:** `str` 
    
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

<details><summary><code>client.billing.<a href="src/fern/billing/client.py#L113-L143">currenttier</a>(...) -> BillingCurrentTierResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

get workspace current tier
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
    environment=FernApiEnvironment.DEFAULT,
)

client.billing.currenttier(
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

**workspace_id:** `str` 
    
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

<details><summary><code>client.billing.<a href="src/fern/billing/client.py#L145-L175">currentsubscription</a>(...) -> typing.Optional[BillingCurrentSubscriptionResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

get workspace current subscription
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
    environment=FernApiEnvironment.DEFAULT,
)

client.billing.currentsubscription(
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

**workspace_id:** `str` 
    
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

<details><summary><code>client.billing.<a href="src/fern/billing/client.py#L177-L207">credit</a>(...) -> BillingCreditResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

get workspace credit balance
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
    environment=FernApiEnvironment.DEFAULT,
)

client.billing.credit(
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

**workspace_id:** `str` 
    
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

<details><summary><code>client.billing.<a href="src/fern/billing/client.py#L209-L250">creditbills</a>(...) -> BillingCreditBillsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

list workspace credit bills
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
    environment=FernApiEnvironment.DEFAULT,
)

client.billing.creditbills(
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

**workspace_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
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

<details><summary><code>client.billing.<a href="src/fern/billing/client.py#L252-L282">creditpacks</a>(...) -> typing.List[BillingCreditPacksResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

list available credit packs
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
    environment=FernApiEnvironment.DEFAULT,
)

client.billing.creditpacks(
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

**workspace_id:** `str` 
    
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

<details><summary><code>client.billing.<a href="src/fern/billing/client.py#L284-L326">creditcheckout</a>(...) -> BillingCreditCheckoutResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

create credit checkout session
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
    environment=FernApiEnvironment.DEFAULT,
)

client.billing.creditcheckout(
    workspace_id="workspaceId",
    pack_id="packId",
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

**pack_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` 
    
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

## Feed
<details><summary><code>client.feed.<a href="src/fern/feed/client.py#L44-L72">channels</a>(...) -> typing.List[FeedChannelsResponseItem]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.feed.channels(
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

**workspace_id:** `str` 
    
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

<details><summary><code>client.feed.<a href="src/fern/feed/client.py#L74-L105">channelinfo</a>(...) -> typing.Optional[FeedChannelInfoResponse]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.feed.channelinfo(
    workspace_id="workspaceId",
    channel_id="channelId",
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

**channel_id:** `str` 
    
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

<details><summary><code>client.feed.<a href="src/fern/feed/client.py#L107-L167">updatechannelinfo</a>(...) -> typing.Optional[FeedUpdateChannelInfoResponse]</code></summary>
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
from fern.feed import FeedUpdateChannelInfoRequestNotifyFrequency

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.feed.updatechannelinfo(
    workspace_id="workspaceId",
    channel_id="channelId",
    name="name",
    webhook_signature="webhookSignature",
    notify_frequency=FeedUpdateChannelInfoRequestNotifyFrequency.NONE,
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

**channel_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_signature:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**notify_frequency:** `FeedUpdateChannelInfoRequestNotifyFrequency` 
    
</dd>
</dl>

<dl>
<dd>

**notification_ids:** `typing.Optional[typing.List[str]]` 
    
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

<details><summary><code>client.feed.<a href="src/fern/feed/client.py#L169-L217">fetcheventsbycursor</a>(...) -> FeedFetchEventsByCursorResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch workspace feed channel events
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
    environment=FernApiEnvironment.DEFAULT,
)

client.feed.fetcheventsbycursor(
    workspace_id="workspaceId",
    channel_id="channelId",
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

**channel_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.feed.<a href="src/fern/feed/client.py#L219-L260">fetchpubliceventsbycursor</a>(...) -> FeedFetchPublicEventsByCursorResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch public feed channel events by shareId
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
    environment=FernApiEnvironment.DEFAULT,
)

client.feed.fetchpubliceventsbycursor(
    share_id="shareId",
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

**share_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
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

<details><summary><code>client.feed.<a href="src/fern/feed/client.py#L262-L292">getchannelbyshareid</a>(...) -> FeedGetChannelByShareIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch public feed channel info by shareId
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
    environment=FernApiEnvironment.DEFAULT,
)

client.feed.getchannelbyshareid(
    share_id="shareId",
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

**share_id:** `str` 
    
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

<details><summary><code>client.feed.<a href="src/fern/feed/client.py#L294-L344">createchannel</a>(...) -> FeedCreateChannelResponse</code></summary>
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
from fern.feed import FeedCreateChannelRequestNotifyFrequency

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.feed.createchannel(
    workspace_id="workspaceId",
    name="name",
    notify_frequency=FeedCreateChannelRequestNotifyFrequency.NONE,
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**notify_frequency:** `FeedCreateChannelRequestNotifyFrequency` 
    
</dd>
</dl>

<dl>
<dd>

**notification_ids:** `typing.Optional[typing.List[str]]` 
    
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

<details><summary><code>client.feed.<a href="src/fern/feed/client.py#L346-L379">refreshpublicshareid</a>(...) -> FeedRefreshPublicShareIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Regenerate public share id for feed channel
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
    environment=FernApiEnvironment.DEFAULT,
)

client.feed.refreshpublicshareid(
    workspace_id="workspaceId",
    channel_id="channelId",
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

**channel_id:** `str` 
    
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

<details><summary><code>client.feed.<a href="src/fern/feed/client.py#L381-L414">disablepublicshareid</a>(...) -> FeedDisablePublicShareIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disable public share for feed channel
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
    environment=FernApiEnvironment.DEFAULT,
)

client.feed.disablepublicshareid(
    workspace_id="workspaceId",
    channel_id="channelId",
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

**channel_id:** `str` 
    
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

<details><summary><code>client.feed.<a href="src/fern/feed/client.py#L416-L447">deletechannel</a>(...) -> FeedDeleteChannelResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.feed.deletechannel(
    workspace_id="workspaceId",
    channel_id="channelId",
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

**channel_id:** `str` 
    
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

<details><summary><code>client.feed.<a href="src/fern/feed/client.py#L449-L519">sendevent</a>(...) -> FeedSendEventResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.feed.sendevent(
    channel_id="channelId",
    event_name="eventName",
    event_content="eventContent",
    source="source",
    important=True,
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

**channel_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**event_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**event_content:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**source:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**important:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**sender_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sender_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**payload:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
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

<details><summary><code>client.feed.<a href="src/fern/feed/client.py#L521-L562">archiveevent</a>(...) -> typing.Any</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.feed.archiveevent(
    channel_id="channelId",
    event_id="eventId",
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

**channel_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` 
    
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

<details><summary><code>client.feed.<a href="src/fern/feed/client.py#L564-L605">unarchiveevent</a>(...) -> typing.Any</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.feed.unarchiveevent(
    channel_id="channelId",
    event_id="eventId",
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

**channel_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` 
    
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

<details><summary><code>client.feed.<a href="src/fern/feed/client.py#L607-L640">clearallarchivedevents</a>(...) -> float</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.feed.clearallarchivedevents(
    channel_id="channelId",
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

**channel_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` 
    
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

<details><summary><code>client.feed.<a href="src/fern/feed/client.py#L642-L670">integration_playground</a>(...) -> str</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.feed.integration_playground(
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

**workspace_id:** `str` 
    
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

<details><summary><code>client.feed.<a href="src/fern/feed/client.py#L672-L698">integration_github</a>(...) -> str</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.feed.integration_github(
    channel_id="channelId",
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

**channel_id:** `str` 
    
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

<details><summary><code>client.feed.<a href="src/fern/feed/client.py#L700-L726">integration_stripe</a>(...) -> str</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.feed.integration_stripe(
    channel_id="channelId",
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

**channel_id:** `str` 
    
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

<details><summary><code>client.feed.<a href="src/fern/feed/client.py#L728-L756">integration_tencentcloudalarm</a>(...) -> str</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.feed.integration_tencentcloudalarm(
    channel_id="channelId",
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

**channel_id:** `str` 
    
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

<details><summary><code>client.feed.<a href="src/fern/feed/client.py#L758-L784">integration_sentry</a>(...) -> str</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.feed.integration_sentry(
    channel_id="channelId",
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

**channel_id:** `str` 
    
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

<details><summary><code>client.feed.<a href="src/fern/feed/client.py#L786-L826">state_all</a>(...) -> typing.List[FeedStateAllResponseItem]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.feed.state_all(
    workspace_id="workspaceId",
    channel_id="channelId",
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

**channel_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` 
    
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

<details><summary><code>client.feed.<a href="src/fern/feed/client.py#L828-L904">state_upsert</a>(...) -> FeedStateUpsertResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.feed.state_upsert(
    channel_id="channelId",
    event_id="eventId",
    event_name="eventName",
    event_content="eventContent",
    tags=[
        "tags"
    ],
    source="source",
    important=True,
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

**channel_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**event_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**event_content:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**source:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**important:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**sender_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sender_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**payload:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
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

<details><summary><code>client.feed.<a href="src/fern/feed/client.py#L906-L947">state_resolve</a>(...) -> FeedStateResolveResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.feed.state_resolve(
    workspace_id="workspaceId",
    channel_id="channelId",
    state_id="stateId",
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

**channel_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**state_id:** `str` 
    
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

## Worker
<details><summary><code>client.worker.<a href="src/fern/worker/client.py">all</a>(...) -> typing.List[WorkerAllResponseItem]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.worker.all_(
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

**workspace_id:** `str` 
    
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

<details><summary><code>client.worker.<a href="src/fern/worker/client.py#L64-L95">get</a>(...) -> typing.Optional[WorkerGetResponse]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.worker.get(
    workspace_id="workspaceId",
    worker_id="workerId",
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

**worker_id:** `str` 
    
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

<details><summary><code>client.worker.<a href="src/fern/worker/client.py#L97-L161">upsert</a>(...) -> WorkerUpsertResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.worker.upsert(
    workspace_id="workspaceId",
    name="name",
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

**workspace_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**code:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**enable_cron:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**cron_expression:** `typing.Optional[str]` 
    
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

<details><summary><code>client.worker.<a href="src/fern/worker/client.py#L163-L194">delete</a>(...) -> WorkerDeleteResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.worker.delete(
    workspace_id="workspaceId",
    worker_id="workerId",
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

**worker_id:** `str` 
    
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

<details><summary><code>client.worker.<a href="src/fern/worker/client.py#L196-L237">toggleactive</a>(...) -> WorkerToggleActiveResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.worker.toggleactive(
    workspace_id="workspaceId",
    worker_id="workerId",
    active=True,
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

**worker_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**active:** `bool` 
    
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

<details><summary><code>client.worker.<a href="src/fern/worker/client.py#L239-L270">getrevisions</a>(...) -> typing.List[WorkerGetRevisionsResponseItem]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.worker.getrevisions(
    workspace_id="workspaceId",
    worker_id="workerId",
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

**worker_id:** `str` 
    
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

