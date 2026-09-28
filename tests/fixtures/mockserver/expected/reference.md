# Reference
## Expectation
<details><summary><code>client.expectation.<a href="src/fern/expectation/client.py">create_expectation</a>(...) -> typing.List[Expectation]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.expectation.create_expectation(
    request={"httpRequest": {"method": "GET", "path": "/api/users", "queryStringParameters": {"page": ["1"], "limit": ["10"]}}, "httpResponse": {"statusCode": 200, "headers": {"Content-Type": ["application/json"]}, "body": "{\"users\":[{\"id\":1,\"name\":\"John Doe\"}],\"total\":1}"}},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `Expectations` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.expectation.<a href="src/fern/expectation/client.py">create_expectations_from_open_api_or_swagger</a>(...) -> typing.List[Expectation]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, OpenApiExpectation
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.expectation.create_expectations_from_open_api_or_swagger(
    request=OpenApiExpectation(
        spec_url_or_payload="https://raw.githubusercontent.com/mock-server/mockserver-monorepo/master/mockserver/mockserver-integration-testing/src/main/resources/org/mockserver/openapi/openapi_petstore_example.json",
        operations_and_responses={
            "listPets": "200",
            "showPetById": "200"
        },
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

**request:** `OpenApiExpectations` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.expectation.<a href="src/fern/expectation/client.py">generate_expectation_suggestion_s_from_an_unmatched_request</a>(...) -> PutMockserverGenerateExpectationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates one or more suggested expectations for an unmatched HttpRequest. When 'preview' is true (the default) the suggestions are only returned; when false they are also added. If an LLM backend is configured it is used, otherwise a simple template-based stub is generated.
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
from fern import FernApi, HttpRequest
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.expectation.generate_expectation_suggestion_s_from_an_unmatched_request(
    request=HttpRequest(
        method="POST",
        path="/api/orders",
    ),
    preview=True,
    limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `HttpRequest` 
    
</dd>
</dl>

<dl>
<dd>

**preview:** `typing.Optional[bool]` — when true (default) only return suggestions; when false also add them
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — maximum number of suggestions to generate (1-5)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.expectation.<a href="src/fern/expectation/client.py">create_expectations_from_a_wsdl</a>() -> typing.List[Expectation]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

generates expectations from a WSDL document (the request body is the raw WSDL) and adds them
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

client.expectation.create_expectations_from_a_wsdl()

```
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

<details><summary><code>client.expectation.<a href="src/fern/expectation/client.py">create_expectations_from_a_graph_ql_schema</a>(...) -> typing.List[Expectation]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates expectations from a GraphQL schema (the request body is a GraphQL SDL document or an introspection JSON result) and adds them. One expectation is created per root operation type (query / mutation / subscription); each matches any operation of that kind and synthesizes a schema-valid response per request. The optional "path" query parameter overrides the default "/graphql" request path the generated expectations match.
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

client.expectation.create_expectations_from_a_graph_ql_schema()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**path:** `typing.Optional[str]` — request path the generated GraphQL expectations match (default "/graphql")
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.expectation.<a href="src/fern/expectation/client.py">create_http_expectations_from_an_async_api_spec</a>(...) -> typing.List[Expectation]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates HTTP expectations from an AsyncAPI 2.x/3.x spec (JSON/YAML, or a {spec, channelPathPrefix} wrapper) so each channel's example message can be served over plain HTTP without a live broker. One GET expectation is created per channel returning that channel's schema-aware example payload. This is distinct from PUT /mockserver/asyncapi, which loads a spec into the broker-publishing mock. Requires the mockserver-async module on the classpath (501 otherwise).
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

client.expectation.create_http_expectations_from_an_async_api_spec(
    request={
        "spec": "asyncapi: 2.6.0\ninfo:\n  title: Test Service\n  version: 1.0.0\nchannels:\n  user/signedup:\n    publish:\n      message:\n        payload:\n          type: object\n          properties:\n            userId:\n              type: string",
        "channelPathPrefix": "/events"
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

**request:** `typing.Dict[str, typing.Any]` — AsyncAPI spec (JSON/YAML) or a {spec, channelPathPrefix} wrapper
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Control
<details><summary><code>client.control.<a href="src/fern/control/client.py">clears_expectations_and_recorded_requests_that_match_the_request_matcher</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ExpectationId
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.control.clears_expectations_and_recorded_requests_that_match_the_request_matcher(
    request=ExpectationId(
        id="id",
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

**request:** `PutMockserverClearRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[PutMockserverClearRequestType]` — specifies the type of information to clear, default if not specified is "all", supported values are "all", "log", "expectations"
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.control.<a href="src/fern/control/client.py">clears_all_expectations_and_recorded_requests</a>()</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.control.clears_all_expectations_and_recorded_requests()

```
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

<details><summary><code>client.control.<a href="src/fern/control/client.py">retrieve_recorded_requests_active_expectations_recorded_expectations_or_log_messages</a>(...) -> PutMockserverRetrieveResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ExpectationId
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.control.retrieve_recorded_requests_active_expectations_recorded_expectations_or_log_messages(
    request=ExpectationId(
        id="id",
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

**request:** `PutMockserverRetrieveRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[PutMockserverRetrieveRequestFormat]` — changes response format, default if not specified is "json". Not every format is valid for every "type" - the combinations are constrained, and an inapplicable pairing is rejected: the code-generation formats ("java", "javascript", "python", "go", "csharp", "ruby", "rust", "php") apply to "recorded_expectations" and "active_expectations" only and are rejected for "requests" and "request_responses"; the export formats ("openapi", "postman", "bruno") apply to "active_expectations" only; "curl" applies to "requests" and "request_responses" only. "json", "log_entries" and "har" are unconstrained.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[PutMockserverRetrieveRequestType]` — specifies the type of object that is retrieve, default if not specified is "requests", supported values are "logs", "requests", "request_responses", "recorded_expectations", "active_expectations", "metrics"
    
</dd>
</dl>

<dl>
<dd>

**correlation_id:** `typing.Optional[str]` — only return entries whose log correlation id matches this value
    
</dd>
</dl>

<dl>
<dd>

**namespace:** `typing.Optional[str]` — tenant filter applied to "active_expectations" retrieval - returns only that namespace's expectations plus global (no-namespace) expectations. When omitted the namespace is taken from the request header named by the matchNamespaceHeader configuration property, if set; when neither is present the retrieval spans all namespaces.
    
</dd>
</dl>

<dl>
<dd>

**fan_in_local_only:** `typing.Optional[bool]` — when true serve only this node's log rather than aggregating peers. Set by peer nodes on cluster fan-in queries as an infinite-recursion guard; callers do not normally set it. Only affects "requests" and "request_responses" retrieval, and only when cluster fan-in is enabled and configured.
    
</dd>
</dl>

<dl>
<dd>

**forward_unmatched_to:** `typing.Optional[str]` — arms record-and-forward for the session - subsequent requests matching no expectation are forwarded to this upstream and captured as recorded expectations, which this and later retrievals return in the requested format. Only arms recording; it does not synthesise traffic, so a retrieval made before any traffic arrives returns nothing.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.control.<a href="src/fern/control/client.py">return_listening_ports</a>() -> Ports</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.control.return_listening_ports()

```
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

<details><summary><code>client.control.<a href="src/fern/control/client.py">bind_additional_listening_ports</a>(...) -> Ports</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

only supported on Netty version
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

client.control.bind_additional_listening_ports(
    ports=[
        1090
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

**request:** `Ports` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.control.<a href="src/fern/control/client.py">retrieve_the_open_api_specification_for_mock_server</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

returns the OpenAPI specification describing the MockServer REST API in YAML format
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

client.control.retrieve_the_open_api_specification_for_mock_server()

```
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

<details><summary><code>client.control.<a href="src/fern/control/client.py">retrieve_the_current_configuration</a>() -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

returns the current MockServer configuration as JSON
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

client.control.retrieve_the_current_configuration()

```
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

<details><summary><code>client.control.<a href="src/fern/control/client.py">update_the_current_configuration</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

updates MockServer configuration properties at runtime, only non-null fields in the request body are applied
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

client.control.update_the_current_configuration(
    request={
        "logLevel": "INFO"
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

**request:** `typing.Dict[str, typing.Any]` — JSON object containing the configuration properties to update
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.control.<a href="src/fern/control/client.py">retrieve_the_current_server_clock_status</a>() -> ClockStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current instant, epoch milliseconds, and whether the clock is frozen.
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

client.control.retrieve_the_current_server_clock_status()

```
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

<details><summary><code>client.control.<a href="src/fern/control/client.py">control_the_server_clock_for_deterministic_time_based_testing</a>(...) -> ClockResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Freeze, advance, or reset MockServer's internal clock. The controllable clock affects response template date/time helpers (now_iso_8601, now_epoch, now_rfc_1123, dates.*) and expectation TimeToLive expiry. Event-log timestamps and JWT issuance are not affected.
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
from fern.control import ClockRequestAction
import datetime

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.control.control_the_server_clock_for_deterministic_time_based_testing(
    action=ClockRequestAction.FREEZE,
    instant=datetime.datetime.fromisoformat("2026-01-15T10:00:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `ClockRequestAction` — freeze: freeze the clock at the given instant (or current time if instant is omitted); advance: advance the frozen clock by durationMillis (freezes first if not already frozen); reset: reset the clock to real wall-clock time
    
</dd>
</dl>

<dl>
<dd>

**instant:** `typing.Optional[datetime.datetime]` — ISO-8601 instant to freeze at (only used with action 'freeze'; omit to freeze at current time)
    
</dd>
</dl>

<dl>
<dd>

**duration_millis:** `typing.Optional[int]` — number of milliseconds to advance the clock by (required when action is 'advance')
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.control.<a href="src/fern/control/client.py">retrieve_the_current_proxy_mock_operating_mode</a>() -> GetMockserverModeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

returns the current operating mode and whether unmatched requests are proxied
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

client.control.retrieve_the_current_proxy_mock_operating_mode()

```
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

<details><summary><code>client.control.<a href="src/fern/control/client.py">set_the_proxy_mock_operating_mode</a>(...) -> PutMockserverModeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets the operating mode that controls how unmatched requests are handled. SIMULATE matches expectations and returns a 404 for unmatched requests; SPY matches expectations but forwards (and records) unmatched requests to the real downstream; CAPTURE forwards and records all traffic (the same proxy-on-no-match behaviour as SPY).
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
from fern.control import PutMockserverModeRequestMode

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.control.set_the_proxy_mock_operating_mode(
    mode=PutMockserverModeRequestMode.SIMULATE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**mode:** `PutMockserverModeRequestMode` — the operating mode to set
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.control.<a href="src/fern/control/client.py">list_registered_cassettes</a>() -> GetMockserverCassettesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

returns all registered cassettes held in the in-memory cassette registry
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

client.control.list_registered_cassettes()

```
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

<details><summary><code>client.control.<a href="src/fern/control/client.py">register_or_update_a_record_replay_cassette</a>(...) -> PutMockserverCassettesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Registers (or updates) a cassette entry in the in-memory cassette registry from a JSON body. The 'path' field is required; 'filename', 'expectationCount' and 'origin' are optional.
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

client.control.register_or_update_a_record_replay_cassette(
    path="/api/users",
    filename="users-cassette.json",
    expectation_count=3,
    origin="test",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**path:** `str` — cassette path (required, used as the registry key)
    
</dd>
</dl>

<dl>
<dd>

**filename:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**expectation_count:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**origin:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.control.<a href="src/fern/control/client.py">remove_a_registered_cassette</a>(...) -> DeleteMockserverCassettesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

removes a cassette by path, supplied either as the 'path' query parameter or a JSON body with a 'path' field
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

client.control.remove_a_registered_cassette(
    delete_mockserver_cassettes_request_path="/api/users",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**path:** `typing.Optional[str]` — path of the cassette to remove (alternatively supply 'path' in the request body)
    
</dd>
</dl>

<dl>
<dd>

**delete_mockserver_cassettes_request_path:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.control.<a href="src/fern/control/client.py">replay_a_previously_recorded_request_to_its_original_target</a>(...) -> HttpResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Re-issues a previously recorded or proxied HTTP request to its upstream target and returns the upstream response. The target host/port is resolved from the socketAddress field or the Host header in the submitted HttpRequest JSON. Subject to the SSRF policy (mockserver.forwardProxyBlockPrivateNetworks) and a 10 MB body-size cap on both the outbound request and the upstream response.
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
from fern import FernApi, KeyToMultiValueZeroItem
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.control.replay_a_previously_recorded_request_to_its_original_target(
    method="PUT",
    path="/mockserver/status",
    headers=[
        KeyToMultiValueZeroItem()
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

**request:** `HttpRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.control.<a href="src/fern/control/client.py">register_a_breakpoint_matcher</a>(...) -> PutMockserverBreakpointMatcherResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Registers a request matcher that activates breakpoints for forwarded/proxied exchanges. When a proxied request matches the httpRequest definition, the exchange is paused at each specified phase. Returns the assigned matcher id and the registered phases. The clientId field is required — paused items are dispatched over the callback WebSocket (/_mockserver_callback_websocket) to the owning client for interactive resolution.
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
from fern import FernApi, HttpRequest
from fern.environment import FernApiEnvironment
from fern.control import PutMockserverBreakpointMatcherRequestPhasesItem

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.control.register_a_breakpoint_matcher(
    http_request=HttpRequest(
        method="GET",
        path="/api/test",
    ),
    phases=[
        PutMockserverBreakpointMatcherRequestPhasesItem.REQUEST
    ],
    client_id="test-client-123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**http_request:** `HttpRequest` — request matcher — same fields as an expectation request matcher
    
</dd>
</dl>

<dl>
<dd>

**phases:** `typing.List[PutMockserverBreakpointMatcherRequestPhasesItem]` — phases at which matching exchanges will be paused
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — Required. The callback WebSocket client id to dispatch paused items to for interactive resolution. Must be a connected callback client.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.control.<a href="src/fern/control/client.py">list_all_registered_breakpoint_matchers</a>() -> GetMockserverBreakpointMatchersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all currently registered breakpoint matchers. Each entry includes the matcher id, the httpRequest definition, the set of phases, and the clientId.
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

client.control.list_all_registered_breakpoint_matchers()

```
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

<details><summary><code>client.control.<a href="src/fern/control/client.py">list_all_registered_breakpoint_matchers_put_variant</a>() -> PutMockserverBreakpointMatchersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Same as GET /mockserver/breakpoint/matchers. The PUT variant exists for consistency with other control-plane endpoints that use PUT for idempotent queries.
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

client.control.list_all_registered_breakpoint_matchers_put_variant()

```
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

<details><summary><code>client.control.<a href="src/fern/control/client.py">remove_a_registered_breakpoint_matcher</a>(...) -> PutMockserverBreakpointMatcherRemoveResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes a previously registered breakpoint matcher by id. Returns status "removed" on success or 404 if no matcher with the given id exists.
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

client.control.remove_a_registered_breakpoint_matcher(
    id="78fa44ff-5989-467a-ba44-ff5989667a71",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — the matcher id to remove
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.control.<a href="src/fern/control/client.py">remove_all_registered_breakpoint_matchers</a>() -> PutMockserverBreakpointMatcherClearResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes all registered breakpoint matchers. After this call, no exchanges will be paused at breakpoints until new matchers are registered. Returns the number of matchers cleared.
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

client.control.remove_all_registered_breakpoint_matchers()

```
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

<details><summary><code>client.control.<a href="src/fern/control/client.py">stop_running_process</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

only supported on Netty version
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

client.control.stop_running_process()

```
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

<details><summary><code>client.control.<a href="src/fern/control/client.py">readiness_probe</a>() -> GetMockserverReadyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Readiness probe, distinct from the liveness/status endpoints, which answer 200 the instant the port binds. Stays 503 until the synchronous expectation initializers and any OpenAPI seeding have completed, so an orchestrator does not route traffic before the seeded expectations exist. This is the one control-plane endpoint with no authentication gate, so it remains usable as a Kubernetes readiness probe on an instance whose control plane requires credentials.
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

client.control.readiness_probe()

```
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

<details><summary><code>client.control.<a href="src/fern/control/client.py">retrieve_the_effective_configuration</a>() -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns every configuration property with its resolved value and the source tier that supplied it, so an operator can see which of the property file, system properties, environment variables or defaults won. Values detected as sensitive are redacted. Distinct from `/mockserver/configuration`, which reads and writes the mutable runtime configuration.
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

client.control.retrieve_the_effective_configuration()

```
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

<details><summary><code>client.control.<a href="src/fern/control/client.py">retrieve_client_proxy_setup_details</a>() -> GetMockserverProxyConfigurationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns everything a client needs to route through this instance as a proxy: the CA certificate (path and PEM), the proxy URL, and ready-to-paste environment-variable snippets for Unix shells and PowerShell. Send `Accept: text/plain` to get the copy-paste snippet on its own instead of the JSON document.
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

client.control.retrieve_client_proxy_setup_details()

```
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

<details><summary><code>client.control.<a href="src/fern/control/client.py">retrieve_experimental_http3quic_listener_status</a>() -> GetMockserverHttp3StatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reports whether the experimental HTTP/3 listener is enabled, the UDP port it is bound to, and how many QUIC connections are currently active. When the running server is not an HTTP/3-capable instance, `enabled` is false and `port` is -1.
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

client.control.retrieve_experimental_http3quic_listener_status()

```
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

## Verify
<details><summary><code>client.verify.<a href="src/fern/verify/client.py">verify_a_request_has_been_received_a_specific_number_of_times</a>(...)</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.verify.verify_a_request_has_been_received_a_specific_number_of_times(
    request={"httpRequest": {"method": "GET", "path": "/api/users"}, "times": {"atLeast": 1}},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `Verification` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.verify.<a href="src/fern/verify/client.py">verify_a_sequence_of_request_has_been_received_in_the_specific_order</a>(...)</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.verify.verify_a_sequence_of_request_has_been_received_in_the_specific_order(
    request={"httpRequests": [{"method": "POST", "path": "/api/login"}, {"method": "GET", "path": "/api/dashboard"}]},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `VerificationSequence` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.verify.<a href="src/fern/verify/client.py">compare_two_http_requests_field_by_field</a>(...) -> PutMockserverDiffResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Diffs an 'expected' against an 'actual' HttpRequest and returns the per-field differences, a total diff count and whether the two requests are identical.
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
from fern import FernApi, HttpRequest, KeyToMultiValueZeroItem
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.verify.compare_two_http_requests_field_by_field(
    expected=HttpRequest(
        method="GET",
        path="/api/pets",
        headers=[
            KeyToMultiValueZeroItem()
        ],
    ),
    actual=HttpRequest(
        method="GET",
        path="/api/pets",
        headers=[
            KeyToMultiValueZeroItem()
        ],
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

**expected:** `HttpRequest` 
    
</dd>
</dl>

<dl>
<dd>

**actual:** `HttpRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Import
<details><summary><code>client.import_.<a href="src/fern/import_/client.py">import_expectations_from_a_har_or_postman_collection_or_re_import_recorded_traffic</a>(...) -> typing.List[Expectation]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Converts an HTTP Archive (HAR) export or a Postman collection into MockServer expectations and adds them. The format is auto-detected from the document structure or can be forced with the format query parameter.

With format=recording this instead re-imports a persisted NDJSON archive of recorded request/response pairs (one per line) back into the event log, so they become retrievable like in-memory recordings. That mode creates log entries rather than expectations.
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

client.import_.import_expectations_from_a_har_or_postman_collection_or_re_import_recorded_traffic(
    request={
        "log": {"version": "1.2", "entries": [{"request": {"method": "GET", "url": "http://example.com/api/users"}, "response": {"status": 200, "content": {"text": "{\"users\":[{\"id\":1,\"name\":\"Alice\"}]}"}}}]}
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

**request:** `typing.Dict[str, typing.Any]` — a HAR export or Postman collection JSON document
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[PutMockserverImportRequestFormat]` — forces the import format, supported values are "har", "postman" and "recording"; when omitted the format is auto-detected from the request body. "recording" selects the recorded-traffic NDJSON re-import rather than expectation import.
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[PutMockserverImportRequestSource]` — only used with format=recording. When "disk" - or whenever the request body is empty - the NDJSON archive is read from the path configured by persistedRecordedRequestsPath instead of from the request body; a missing archive file is a 400.
    
</dd>
</dl>

<dl>
<dd>

**redact_sensitive_data:** `typing.Optional[bool]` — redact sensitive headers and body fields from the imported document; enabled unless set to the literal "false"
    
</dd>
</dl>

<dl>
<dd>

**additional_redacted_headers:** `typing.Optional[str]` — comma-separated header names to redact in addition to the built-in set
    
</dd>
</dl>

<dl>
<dd>

**additional_redacted_body_fields:** `typing.Optional[str]` — comma-separated body field names to redact in addition to the built-in set
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.import_.<a href="src/fern/import_/client.py">promote_recorded_traffic_to_active_expectations</a>(...) -> typing.List[Expectation]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves recorded (forwarded) exchanges matching an optional request-matcher filter, consolidates them into reusable mocks and ACTIVATES them by adding them to the expectation set. Redaction is on by default so promoted mocks never carry captured credentials; consolidation and parameterization are also on by default, so a single recorded id does not pin the mock. The request body is optional — omit it to promote every recorded exchange.
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
from fern import FernApi, HttpRequest
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.import_.promote_recorded_traffic_to_active_expectations(
    request=HttpRequest(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `RequestDefinition` 
    
</dd>
</dl>

<dl>
<dd>

**consolidate:** `typing.Optional[bool]` — collapse matching exchanges into unlimited-times expectations; set false to promote verbatim
    
</dd>
</dl>

<dl>
<dd>

**parameterize:** `typing.Optional[bool]` — generalise volatile path, query, header and body values
    
</dd>
</dl>

<dl>
<dd>

**redact_sensitive_data:** `typing.Optional[bool]` — redact credentials captured in the recorded traffic
    
</dd>
</dl>

<dl>
<dd>

**additional_redacted_headers:** `typing.Optional[str]` — comma-separated additional header names to redact
    
</dd>
</dl>

<dl>
<dd>

**additional_redacted_body_fields:** `typing.Optional[str]` — comma-separated additional body field names to redact
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Crud
<details><summary><code>client.crud.<a href="src/fern/crud/client.py">register_a_generated_crud_data_store</a>(...) -> PutMockserverCrudResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Registers a REST resource backed by an in-memory data store that automatically handles list, read, create, update and delete operations under the supplied base path.
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
from fern.crud import CrudExpectationsDefinitionIdStrategy

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.crud.register_a_generated_crud_data_store(
    base_path="/api/users",
    id_field="id",
    id_strategy=CrudExpectationsDefinitionIdStrategy.AUTO_INCREMENT,
    initial_data=[
        {
            "id": 1,
            "name": "Alice",
            "email": "alice@example.com"
        },
        {
            "id": 2,
            "name": "Bob",
            "email": "bob@example.com"
        }
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

**base_path:** `str` — base path the CRUD resource is served under (e.g. /api/users)
    
</dd>
</dl>

<dl>
<dd>

**id_field:** `typing.Optional[str]` — name of the field used as the resource identifier
    
</dd>
</dl>

<dl>
<dd>

**id_strategy:** `typing.Optional[CrudExpectationsDefinitionIdStrategy]` — strategy used to generate identifiers for newly created resources
    
</dd>
</dl>

<dl>
<dd>

**initial_data:** `typing.Optional[typing.List[typing.Dict[str, typing.Any]]]` — initial records to seed the data store with
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Files
<details><summary><code>client.files.<a href="src/fern/files/client.py">store_a_file_in_the_file_store</a>(...) -> PutMockserverFilesStoreResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

stores a file (text or base64-encoded binary) under the supplied name in the in-memory file store
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

client.files.store_a_file_in_the_file_store(
    name="template.json",
    content="{\"status\":\"ok\"}",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — name to store the file under
    
</dd>
</dl>

<dl>
<dd>

**content:** `str` — file content, either plain text or base64-encoded when base64 is true
    
</dd>
</dl>

<dl>
<dd>

**base64:** `typing.Optional[bool]` — when true, content is treated as base64-encoded binary data
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/fern/files/client.py">retrieve_a_file_from_the_file_store</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

returns the raw bytes of a previously stored file
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

client.files.retrieve_a_file_from_the_file_store(
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">list_files_in_the_file_store</a>() -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

returns the names of all files currently held in the in-memory file store
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

client.files.list_files_in_the_file_store()

```
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">delete_a_file_from_the_file_store</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

removes a previously stored file from the in-memory file store
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

client.files.delete_a_file_from_the_file_store(
    name="template.json",
)

```
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

## Chaos
<details><summary><code>client.chaos.<a href="src/fern/chaos/client.py">list_registered_service_scoped_http_chaos</a>() -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

returns all registered service-scoped chaos profiles keyed by host, plus any remaining time-to-live
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

client.chaos.list_registered_service_scoped_http_chaos()

```
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

<details><summary><code>client.chaos.<a href="src/fern/chaos/client.py">register_remove_or_clear_service_scoped_http_chaos</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Registers an HTTP chaos / fault-injection profile for a downstream host, removes a host's profile, or clears all service-scoped chaos. Supply a 'host' with a 'chaos' object to register, 'host' with 'remove':true (or no 'chaos') to remove a single host, or 'clear':true to clear all.
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

client.chaos.register_remove_or_clear_service_scoped_http_chaos(
    host="payments.internal:8443",
    chaos={
        "errorStatus": 503,
        "errorProbability": 0.3,
        "latency": {"timeUnit": "MILLISECONDS", "value": 200}
    },
    ttl_millis=60000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ServiceChaosRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chaos.<a href="src/fern/chaos/client.py">update_an_existing_service_scoped_http_chaos_profile_json_merge_patch</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Applies a JSON Merge Patch to an already-registered service-scoped chaos profile for a host, updating only the supplied fields and leaving the rest unchanged.
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

client.chaos.update_an_existing_service_scoped_http_chaos_profile_json_merge_patch(
    host="payments.internal:8443",
    chaos={
        "errorProbability": 0.5
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

**request:** `ServiceChaosRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chaos.<a href="src/fern/chaos/client.py">list_registered_tcp_chaos</a>() -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

returns all registered TCP chaos profiles keyed by host, plus any remaining time-to-live
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

client.chaos.list_registered_tcp_chaos()

```
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

<details><summary><code>client.chaos.<a href="src/fern/chaos/client.py">register_remove_or_clear_tcp_chaos</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Registers a TCP-layer chaos / fault-injection profile for a downstream host, removes a host's profile, or clears all TCP chaos. Supply a 'host' with a 'chaos' object to register, 'host' with 'remove':true (or no 'chaos') to remove a single host, or 'clear':true to clear all.
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

client.chaos.register_remove_or_clear_tcp_chaos(
    request={
        "host": "slow-api.example.com",
        "chaos": {"bandwidthBytesPerSec": 1024, "latencyMs": 50},
        "ttlMillis": 30000
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

**request:** `typing.Dict[str, typing.Any]` — TCP chaos registration, removal or clear instruction with 'host', optional 'chaos', 'remove', 'clear' and 'ttlMillis' fields
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chaos.<a href="src/fern/chaos/client.py">update_an_existing_tcp_chaos_profile_json_merge_patch</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Applies a JSON Merge Patch to an already-registered TCP chaos profile for a host, updating only the supplied fields and leaving the rest unchanged.
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

client.chaos.update_an_existing_tcp_chaos_profile_json_merge_patch(
    request={
        "host": "slow-api.example.com",
        "chaos": {"slicerChunkSize": 256}
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

**request:** `typing.Dict[str, typing.Any]` — JSON Merge Patch with 'host' and the TCP chaos fields to update
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chaos.<a href="src/fern/chaos/client.py">list_registered_g_rpc_chaos</a>() -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

returns all registered gRPC chaos profiles keyed by service, plus any remaining time-to-live
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

client.chaos.list_registered_g_rpc_chaos()

```
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

<details><summary><code>client.chaos.<a href="src/fern/chaos/client.py">register_remove_or_clear_g_rpc_chaos</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Registers a gRPC chaos / fault-injection profile for a service, removes a service's profile, or clears all gRPC chaos. Supply a 'service' with a 'chaos' object to register, 'service' with 'remove':true (or no 'chaos') to remove a single service, or 'clear':true to clear all.
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

client.chaos.register_remove_or_clear_g_rpc_chaos(
    request={
        "service": "com.example.OrderService",
        "chaos": {"errorStatusCode": "UNAVAILABLE", "errorMessage": "service maintenance", "errorProbability": 0.5, "latencyMs": 100}
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

**request:** `typing.Dict[str, typing.Any]` — gRPC chaos registration, removal or clear instruction with 'service', optional 'chaos', 'remove', 'clear' and 'ttlMillis' fields
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chaos.<a href="src/fern/chaos/client.py">update_an_existing_g_rpc_chaos_profile_json_merge_patch</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Applies a JSON Merge Patch to an already-registered gRPC chaos profile for a service, updating only the supplied fields and leaving the rest unchanged.
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

client.chaos.update_an_existing_g_rpc_chaos_profile_json_merge_patch(
    request={
        "service": "com.example.OrderService",
        "chaos": {"errorProbability": 0.8}
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

**request:** `typing.Dict[str, typing.Any]` — JSON Merge Patch with 'service' and the gRPC chaos fields to update
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chaos.<a href="src/fern/chaos/client.py">get_the_status_of_the_current_chaos_experiment</a>() -> GetMockserverChaosExperimentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current experiment status including name, running status (running/completed/halted_by_auto_halt/stopped), current stage index, total stages, elapsed/remaining time, loop iteration count, and the full experiment definition. Returns null/empty when no experiment is or was recently active.
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

client.chaos.get_the_status_of_the_current_chaos_experiment()

```
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

<details><summary><code>client.chaos.<a href="src/fern/chaos/client.py">start_a_scheduled_multi_stage_chaos_experiment</a>(...) -> PutMockserverChaosExperimentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Starts a chaos experiment with an ordered sequence of stages, each applying service-scoped chaos profiles to one or more hosts for a specified duration. Stages progress automatically. Only one experiment may be active at a time; starting a new one stops the previous one. Safety limits: max 50 stages, max 24h per stage duration, auto-halt integration.
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
from fern import FernApi, HttpChaosProfile
from fern.environment import FernApiEnvironment
from fern.chaos import PutMockserverChaosExperimentRequestStagesItem

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.chaos.start_a_scheduled_multi_stage_chaos_experiment(
    name="gradual-degradation",
    stages=[
        PutMockserverChaosExperimentRequestStagesItem(
            duration_millis=10000,
            profiles={
                "api.example.com": HttpChaosProfile(
                    error_status=500,
                    error_probability=0.1,
                )
            },
        ),
        PutMockserverChaosExperimentRequestStagesItem(
            duration_millis=10000,
            profiles={
                "api.example.com": HttpChaosProfile(
                    error_status=500,
                    error_probability=0.5,
                )
            },
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

**name:** `str` — human-readable experiment name
    
</dd>
</dl>

<dl>
<dd>

**stages:** `typing.List[PutMockserverChaosExperimentRequestStagesItem]` — ordered sequence of stages
    
</dd>
</dl>

<dl>
<dd>

**loop:** `typing.Optional[bool]` — whether to loop back to stage 0 after the last stage completes (default false)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chaos.<a href="src/fern/chaos/client.py">stop_the_current_chaos_experiment</a>() -> DeleteMockserverChaosExperimentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stops the current experiment and clears all chaos from the service registry. Idempotent — no-op if no experiment is running.
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

client.chaos.stop_the_current_chaos_experiment()

```
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

<details><summary><code>client.chaos.<a href="src/fern/chaos/client.py">retrieve_the_current_preemption_status</a>() -> PreemptionStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current cordon/drain status: state (inactive / draining / drained), the number of in-flight requests, the remaining drain window in milliseconds and the active signalling mode.
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

client.chaos.retrieve_the_current_preemption_status()

```
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

<details><summary><code>client.chaos.<a href="src/fern/chaos/client.py">cordon_and_drain_the_server_preemption_simulation</a>(...) -> PreemptionStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Simulates a connection-lifecycle preemption (e.g. a Kubernetes node drain or spot reclamation). While cordoned, new exchanges are signalled to back off — by a 503 + Connection: close, an HTTP/2 GOAWAY frame, or both — while in-flight requests are allowed to drain. The simulation is server-scoped and does not stop the JVM. An empty body uses defaults (mode "both", drainMillis from stopDrainMillis, no TTL). drainMillis and ttlMillis are clamped to preemptionSimulationMaxDrainMillis.
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
from fern.chaos import PreemptionRequestMode

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.chaos.cordon_and_drain_the_server_preemption_simulation(
    mode=PreemptionRequestMode.BOTH,
    drain_millis=10000,
    ttl_millis=60000,
    last_stream_id=3,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**mode:** `typing.Optional[PreemptionRequestMode]` — how draining is signalled: reject503 = 503 + Connection: close; goaway = HTTP/2 GOAWAY frame; both = both
    
</dd>
</dl>

<dl>
<dd>

**drain_millis:** `typing.Optional[int]` — how long in-flight requests are allowed to drain; defaults to the stopDrainMillis property, clamped to preemptionSimulationMaxDrainMillis
    
</dd>
</dl>

<dl>
<dd>

**ttl_millis:** `typing.Optional[int]` — auto-uncordon after this many milliseconds (dead-man's switch); 0 (default) means no auto-uncordon
    
</dd>
</dl>

<dl>
<dd>

**last_stream_id:** `typing.Optional[int]` — HTTP/2 GOAWAY last_stream_id to advertise; -1 (default) lets the server choose
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chaos.<a href="src/fern/chaos/client.py">uncordon_the_server_clear_preemption</a>() -> DeleteMockserverPreemptionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Explicitly clears any active preemption simulation, returning the server to normal operation. Idempotent — returns 200 whether or not a simulation was active.
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

client.chaos.uncordon_the_server_clear_preemption()

```
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

<details><summary><code>client.chaos.<a href="src/fern/chaos/client.py">list_saved_chaos_profile_names</a>() -> GetMockserverChaosExperimentProfilesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

returns the names of all saved chaos experiment profiles, sorted ascending
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

client.chaos.list_saved_chaos_profile_names()

```
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

<details><summary><code>client.chaos.<a href="src/fern/chaos/client.py">retrieve_a_saved_chaos_profile</a>(...) -> ChaosExperiment</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

returns the full saved chaos experiment definition stored under the given name
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

client.chaos.retrieve_a_saved_chaos_profile(
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

**name:** `str` — the profile name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chaos.<a href="src/fern/chaos/client.py">save_a_chaos_experiment_profile</a>(...) -> PutMockserverChaosExperimentProfilesNameResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Saves a chaos experiment definition (the same body shape as PUT /mockserver/chaosExperiment) under the given name so it can be applied later with POST /mockserver/chaosExperiment/apply/{name}. The name in the path is authoritative; any name field in the body is ignored. The name must be 1-128 characters of letters, digits, space, dot, underscore or hyphen with no leading/trailing space.
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
from fern import FernApi, ChaosExperimentStagesItem, HttpChaosProfile
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.chaos.save_a_chaos_experiment_profile(
    name_="name",
    stages=[
        ChaosExperimentStagesItem(
            duration_millis=30000,
            profiles={
                "payments.svc": HttpChaosProfile(
                    error_status=503,
                    error_probability=0.5,
                )
            },
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

**name:** `str` — the profile name to save under
    
</dd>
</dl>

<dl>
<dd>

**request:** `ChaosExperiment` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chaos.<a href="src/fern/chaos/client.py">delete_a_saved_chaos_profile</a>(...) -> DeleteMockserverChaosExperimentProfilesNameResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes the saved chaos profile with the given name. Idempotent — returns 200 with status "deleted" when the profile existed, or "absent" when it did not.
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

client.chaos.delete_a_saved_chaos_profile(
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

**name:** `str` — the profile name to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chaos.<a href="src/fern/chaos/client.py">apply_a_saved_chaos_profile</a>(...) -> PostMockserverChaosExperimentApplyNameResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Starts the chaos experiment previously saved under the given name (as if its definition had been sent to PUT /mockserver/chaosExperiment). The request body is ignored.
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

client.chaos.apply_a_saved_chaos_profile(
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

**name:** `str` — the saved profile name to apply
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chaos.<a href="src/fern/chaos/client.py">retrieve_completed_chaos_experiment_history</a>() -> GetMockserverChaosExperimentHistoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the record of chaos experiments that have run, most recent first, bounded by a fixed in-memory history size that is not caller-controllable.
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

client.chaos.retrieve_completed_chaos_experiment_history()

```
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

## Drift
<details><summary><code>client.drift.<a href="src/fern/drift/client.py">retrieve_recorded_mock_drift</a>(...) -> GetMockserverDriftResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns recorded drift records (differences between expectations and observed responses), optionally filtered by expectation id and limited in count.
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

client.drift.retrieve_recorded_mock_drift()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**expectation_id:** `typing.Optional[str]` — only return drift records for the given expectation id
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — maximum number of recent drift records to return (default 50, capped at 500), ignored when expectationId is supplied
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.drift.<a href="src/fern/drift/client.py">clear_all_recorded_mock_drift</a>() -> PutMockserverDriftClearResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

removes all recorded drift records
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

client.drift.clear_all_recorded_mock_drift()

```
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

## Audit
<details><summary><code>client.audit.<a href="src/fern/audit/client.py">retrieve_the_control_plane_audit_log</a>(...) -> typing.List[GetMockserverAuditResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the most-recent control-plane audit entries (one per authorised control-plane mutation, newest first). Off by default — enable with controlPlaneAuditEnabled. Each entry records redacted, structural metadata only (method, control-plane path with query string dropped, logical operation, source address, best-effort principal, outcome); it never contains request headers or bodies.
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

client.audit.retrieve_the_control_plane_audit_log()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — maximum number of recent audit entries to return (default 200, capped at 1000)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Scenario
<details><summary><code>client.scenario.<a href="src/fern/scenario/client.py">list_all_scenarios_and_their_current_state</a>() -> GetMockserverScenarioResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns every known stateful scenario and its current state. Scenarios are created implicitly by registering expectations with a scenarioName / scenarioState, or explicitly via PUT /mockserver/scenario/{name}. All scenario state is reset when MockServer is reset.
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

client.scenario.list_all_scenarios_and_their_current_state()

```
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

<details><summary><code>client.scenario.<a href="src/fern/scenario/client.py">get_the_current_state_of_one_scenario</a>(...) -> GetMockserverScenarioNameResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current state of the named scenario (null when the scenario has no state yet).
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

client.scenario.get_the_current_state_of_one_scenario(
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

**name:** `str` — the scenario name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.scenario.<a href="src/fern/scenario/client.py">set_a_scenarios_state_optionally_scheduling_a_timed_auto_transition</a>(...) -> PutMockserverScenarioNameResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets the named scenario to the given state immediately. Optionally schedules a timed auto-transition to nextState after transitionAfterMs milliseconds; the transition only fires if the scenario is still in the set state when the timer expires, and scheduling a new transition cancels any pending one.
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

client.scenario.set_a_scenarios_state_optionally_scheduling_a_timed_auto_transition(
    name="name",
    state="Pending",
    transition_after_ms=5000,
    next_state="Completed",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — the scenario name
    
</dd>
</dl>

<dl>
<dd>

**state:** `str` — the state to set immediately
    
</dd>
</dl>

<dl>
<dd>

**transition_after_ms:** `typing.Optional[int]` — delay in milliseconds before auto-transitioning to nextState (requires nextState)
    
</dd>
</dl>

<dl>
<dd>

**next_state:** `typing.Optional[str]` — the state to auto-transition to after transitionAfterMs (requires transitionAfterMs)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.scenario.<a href="src/fern/scenario/client.py">externally_trigger_a_scenario_state_transition</a>(...) -> PutMockserverScenarioNameTriggerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Advances the named scenario to newState immediately. Intended for driving a scenario forward from a test harness or CI pipeline.
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

client.scenario.externally_trigger_a_scenario_state_transition(
    name="name",
    new_state="Failed",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — the scenario name
    
</dd>
</dl>

<dl>
<dd>

**new_state:** `str` — the state to transition the scenario to
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## oidc
<details><summary><code>client.oidc.<a href="src/fern/oidc/client.py">mock_oidc_provider</a>(...) -> typing.List[Expectation]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates a set of expectations that emulate an OpenID Connect / OAuth2 provider (discovery document, JWKS, token, authorize, userinfo and related endpoints) and adds them. An empty body uses the default provider configuration.
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

client.oidc.mock_oidc_provider(
    issuer="http://localhost:1080",
    client_id="my-app",
    scopes=[
        "openid",
        "profile",
        "email"
    ],
    token_expiry_seconds=7200,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issuer:** `typing.Optional[str]` — issuer URL advertised in the discovery document and token claims
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — OAuth2 client identifier
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `typing.Optional[str]` — OAuth2 client secret
    
</dd>
</dl>

<dl>
<dd>

**private_key_pem:** `typing.Optional[str]` — PEM-encoded signing private key (never serialized back in responses)
    
</dd>
</dl>

<dl>
<dd>

**scopes:** `typing.Optional[typing.List[str]]` — supported OAuth2 / OIDC scopes
    
</dd>
</dl>

<dl>
<dd>

**token_expiry_seconds:** `typing.Optional[int]` — lifetime of issued access tokens in seconds
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## saml
<details><summary><code>client.saml.<a href="src/fern/saml/client.py">mock_saml_provider</a>(...) -> typing.List[Expectation]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates a set of expectations that emulate a SAML 2.0 identity provider (metadata, single sign-on and single logout endpoints) and adds them. An empty body uses the default provider configuration.
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

client.saml.mock_saml_provider(
    idp_entity_id="http://localhost:1080/saml/idp",
    sp_entity_id="urn:my-app:sp",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idp_entity_id:** `typing.Optional[str]` — identity provider entity ID advertised in metadata
    
</dd>
</dl>

<dl>
<dd>

**sp_entity_id:** `typing.Optional[str]` — service provider entity ID the assertions are issued for
    
</dd>
</dl>

<dl>
<dd>

**signing_certificate_pem:** `typing.Optional[str]` — PEM-encoded X.509 certificate used to verify signed assertions
    
</dd>
</dl>

<dl>
<dd>

**signing_private_key_pem:** `typing.Optional[str]` — PEM-encoded private key used to sign assertions
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## scim
<details><summary><code>client.scim.<a href="src/fern/scim/client.py">mock_scim_provider</a>(...) -> typing.List[Expectation]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates a set of expectations that emulate a SCIM 2.0 provisioning provider (Users, Groups and ServiceProviderConfig endpoints) and adds them. An empty body uses the default provider configuration.
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

client.scim.mock_scim_provider(
    base_path="/scim/v2",
    require_bearer_token=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**base_path:** `typing.Optional[str]` — base path the SCIM endpoints are served under
    
</dd>
</dl>

<dl>
<dd>

**require_bearer_token:** `typing.Optional[bool]` — whether requests must present a bearer token
    
</dd>
</dl>

<dl>
<dd>

**expected_bearer_token:** `typing.Optional[str]` — bearer token that incoming requests must present when required
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Asyncapi
<details><summary><code>client.asyncapi.<a href="src/fern/asyncapi/client.py">retrieve_async_api_mock_status</a>() -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

returns the status of the currently loaded AsyncAPI mock. Requires the mockserver-async module on the classpath.
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

client.asyncapi.retrieve_async_api_mock_status()

```
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

<details><summary><code>client.asyncapi.<a href="src/fern/asyncapi/client.py">load_an_async_api_specification</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Loads an AsyncAPI specification (JSON or YAML), or a { spec, brokerConfig } document, to mock the described message broker. Requires the mockserver-async module on the classpath.
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

client.asyncapi.load_an_async_api_specification(
    request={
        "spec": "asyncapi: 2.6.0\ninfo:\n  title: Test Service\n  version: 1.0.0\nchannels:\n  user/signedup:\n    publish:\n      message:\n        payload:\n          type: object\n          properties:\n            userId:\n              type: string"
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

**request:** `typing.Dict[str, typing.Any]` — an AsyncAPI specification (JSON/YAML) or a { spec, brokerConfig } document
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.asyncapi.<a href="src/fern/asyncapi/client.py">verify_async_api_messages</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verifies that messages were published/received against the loaded AsyncAPI mock. Requires the mockserver-async module on the classpath.
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

client.asyncapi.verify_async_api_messages(
    request={
        "channel": "user/signedup",
        "count": {"atLeast": 0}
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

**request:** `typing.Dict[str, typing.Any]` — AsyncAPI message verification request
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Wasm
<details><summary><code>client.wasm.<a href="src/fern/wasm/client.py">list_loaded_web_assembly_modules</a>() -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

returns the names of all currently loaded WebAssembly custom rule modules
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

client.wasm.list_loaded_web_assembly_modules()

```
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

<details><summary><code>client.wasm.<a href="src/fern/wasm/client.py">load_a_web_assembly_custom_rule_module</a>(...) -> PutMockserverWasmModulesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

stores a compiled WebAssembly module (raw .wasm bytes) under the name supplied in the query parameter
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
client.wasm.load_a_web_assembly_custom_rule_module(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — name to register the WASM module under
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` — Binary upload of a compiled WebAssembly module. Disabled by default — enable with `MOCKSERVER_WASM_ENABLED=true` (or `-Dmockserver.wasmEnabled=true`). Requires the `?name=<moduleName>` query parameter. Send the raw .wasm bytes with Content-Type application/octet-stream.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.wasm.<a href="src/fern/wasm/client.py">unload_a_web_assembly_custom_rule_module</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes the named WebAssembly custom rule module from the module store. Succeeds with an empty body; the module name is required as a query parameter.
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

client.wasm.unload_a_web_assembly_custom_rule_module(
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

**name:** `str` — name of the WASM module to unload
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.wasm.<a href="src/fern/wasm/client.py">evaluate_a_web_assembly_custom_rule_against_a_sample_request</a>(...) -> PostMockserverWasmTestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Runs a WebAssembly custom rule module against a sample request and reports whether it matched, without registering an expectation. Supply the module either inline as base64 ("module") or by the name of an already-loaded module ("moduleName"); when both are present "module" wins. When a "response" object is also supplied the ABI v3 `shape_response` hook runs and the shaped response is returned alongside the match result.
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
from fern.wasm import PostMockserverWasmTestRequestRequest

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.wasm.evaluate_a_web_assembly_custom_rule_against_a_sample_request(
    module_name="header-rule",
    request=PostMockserverWasmTestRequestRequest(
        method="GET",
        path="/api/orders",
        headers={
            "x-tenant": [
                "acme"
            ]
        },
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

**module:** `typing.Optional[str]` — base64-encoded compiled WebAssembly module bytes
    
</dd>
</dl>

<dl>
<dd>

**module_name:** `typing.Optional[str]` — name of an already-loaded WASM module to evaluate instead of an inline module
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[PostMockserverWasmTestRequestRequest]` — the sample request the rule is evaluated against
    
</dd>
</dl>

<dl>
<dd>

**response:** `typing.Optional[typing.Dict[str, typing.Any]]` — optional sample response; when present the ABI v3 shape_response hook runs and the shaped response is returned with the match result
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Grpc
<details><summary><code>client.grpc.<a href="src/fern/grpc/client.py">load_ag_rpc_proto_descriptor_set</a>(...) -> PutMockserverGrpcDescriptorsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

loads a compiled protobuf FileDescriptorSet (raw bytes) so gRPC services can be matched and mocked
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
client.grpc.load_ag_rpc_proto_descriptor_set(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` — Binary upload of a compiled protobuf FileDescriptorSet (the .desc file produced by `protoc --descriptor_set_out`). Send the raw bytes with Content-Type application/octet-stream.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.grpc.<a href="src/fern/grpc/client.py">retrieve_g_rpc_health_serving_statuses</a>() -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

returns the configured gRPC health serving status for each service (the default is reported under "_default")
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

client.grpc.retrieve_g_rpc_health_serving_statuses()

```
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

<details><summary><code>client.grpc.<a href="src/fern/grpc/client.py">set_ag_rpc_health_serving_status</a>(...) -> PutMockserverGrpcHealthResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets the gRPC health-checking serving status for a service (an empty service name sets the default), or removes a service override with 'remove':true.
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
from fern.grpc import PutMockserverGrpcHealthRequestStatus

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.grpc.set_ag_rpc_health_serving_status(
    service="helloworld.Greeter",
    status=PutMockserverGrpcHealthRequestStatus.SERVING,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service:** `typing.Optional[str]` — gRPC service name; an empty string sets the overall server status (the empty service name defined by the gRPC health checking protocol), rather than the status of any named service
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[PutMockserverGrpcHealthRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**remove:** `typing.Optional[bool]` — when true, removes the service override
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.grpc.<a href="src/fern/grpc/client.py">list_loaded_g_rpc_services</a>() -> typing.List[PutMockserverGrpcServicesResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the gRPC services available from the loaded proto descriptor set, each with its methods and their input/output types and streaming flags.
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

client.grpc.list_loaded_g_rpc_services()

```
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

<details><summary><code>client.grpc.<a href="src/fern/grpc/client.py">reset_the_g_rpc_descriptor_store</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

clears all loaded gRPC proto descriptors and the services derived from them
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

client.grpc.reset_the_g_rpc_descriptor_store()

```
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

## Troubleshooting
<details><summary><code>client.troubleshooting.<a href="src/fern/troubleshooting/client.py">explain_why_recent_requests_did_not_match_any_expectation</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a diagnostic report for recently recorded unmatched requests, including the closest-matching expectations and the per-field differences that prevented a match. An optional 'limit' in the body bounds how many unmatched requests are analysed (default 10).
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

client.troubleshooting.explain_why_recent_requests_did_not_match_any_expectation(
    limit=5,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — maximum number of recent unmatched requests to analyse
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.troubleshooting.<a href="src/fern/troubleshooting/client.py">return_per_expectation_mismatch_debug_information_for_a_request</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Evaluates the supplied HttpRequest against every active expectation and returns, for each, whether it matched and the per-field differences, plus a closest match. Only HttpRequest definitions are supported (not OpenAPI definitions).
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
from fern import FernApi, HttpRequest
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.troubleshooting.return_per_expectation_mismatch_debug_information_for_a_request(
    request=HttpRequest(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `RequestDefinition` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.troubleshooting.<a href="src/fern/troubleshooting/client.py">diff_a_baseline_set_of_expectations_against_another</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compares a "baseline" array of expectations against a "current" array and returns a structured diff of what was added, removed and changed. When "current" is omitted the baseline is diffed against the instance's live active expectations, which makes this usable as a drift check against a committed baseline.
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

client.troubleshooting.diff_a_baseline_set_of_expectations_against_another(
    baseline=[
        {"httpRequest": {"method": "GET", "path": "/api/orders"}, "httpResponse": {"statusCode": 200, "body": "{\"orders\":[]}"}}
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

**baseline:** `typing.List[Expectation]` 
    
</dd>
</dl>

<dl>
<dd>

**current:** `typing.Optional[typing.List[Expectation]]` — optional; when omitted the live active expectations are used
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.troubleshooting.<a href="src/fern/troubleshooting/client.py">validate_recorded_traffic_against_an_open_api_specification</a>(...) -> PutMockserverTrafficValidateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validates the request/response pairs already recorded in the event log against an OpenAPI specification, and reports per-exchange which operation it matched and any request or response violations. Supply the spec as a URL, file path or inline JSON/YAML under "spec" (or its alias "specUrlOrPayload"). A spec fetched by URL is subject to the SSRF policy (forwardProxyBlockPrivateNetworks). The traffic validated comes from the recorded event log, not from the request body.
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

client.troubleshooting.validate_recorded_traffic_against_an_open_api_specification(
    spec="{\"openapi\":\"3.0.0\",\"info\":{\"title\":\"orders\",\"version\":\"1.0.0\"},\"paths\":{\"/api/orders\":{\"get\":{\"responses\":{\"200\":{\"description\":\"orders\"}}}}}}",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**spec:** `typing.Optional[str]` — OpenAPI spec as a URL, file path or inline JSON/YAML
    
</dd>
</dl>

<dl>
<dd>

**spec_url_or_payload:** `typing.Optional[str]` — accepted alias for "spec"
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Pact
<details><summary><code>client.pact.<a href="src/fern/pact/client.py">export_active_expectations_as_a_pact_contract</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Exports the current active expectations as a Pact consumer-driven contract (JSON). The optional 'consumer' and 'provider' query parameters set the contract's consumer and provider names.
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

client.pact.export_active_expectations_as_a_pact_contract()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**consumer:** `typing.Optional[str]` — consumer name to record in the exported Pact contract
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — provider name to record in the exported Pact contract
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pact.<a href="src/fern/pact/client.py">verify_active_expectations_against_a_pact_contract</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verifies the supplied Pact contract (JSON) against the current expectations and returns the verification result. Returns 202 when verification passes and 406 when it fails.
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

client.pact.verify_active_expectations_against_a_pact_contract(
    request={
        "consumer": {"name": "web-app"},
        "provider": {"name": "api-service"},
        "interactions": [{"description": "a health check request", "request": {"method": "GET", "path": "/api/health"}, "response": {"status": 200, "headers": {"content-type": "application/json"}, "body": {"status": "ok"}}}]
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

**request:** `typing.Dict[str, typing.Any]` — Pact contract document to verify against
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pact.<a href="src/fern/pact/client.py">import_a_pact_contract_as_expectations</a>(...) -> typing.List[Expectation]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Parses a Pact v3 consumer-driven contract and adds the interactions it describes to the active expectation set. Redaction is applied on import so credentials present in the contract are not retained.
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

client.pact.import_a_pact_contract_as_expectations(
    request={
        "consumer": {"name": "checkout-service"},
        "provider": {"name": "orders-service"},
        "interactions": [{"description": "a request for all orders", "request": {"method": "GET", "path": "/api/orders"}, "response": {"status": 200, "headers": {"Content-Type": "application/json"}, "body": {}}}],
        "metadata": {"pactSpecification": {"version": "3.0.0"}}
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

**request:** `typing.Dict[str, typing.Any]` — Pact v3 consumer-driven contract document
    
</dd>
</dl>

<dl>
<dd>

**redact_sensitive_data:** `typing.Optional[bool]` — redact credentials found in the imported contract
    
</dd>
</dl>

<dl>
<dd>

**additional_redacted_headers:** `typing.Optional[str]` — comma-separated additional header names to redact
    
</dd>
</dl>

<dl>
<dd>

**additional_redacted_body_fields:** `typing.Optional[str]` — comma-separated additional body field names to redact
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Loadgen
<details><summary><code>client.loadgen.<a href="src/fern/loadgen/client.py">list_all_registered_load_scenarios</a>() -> GetMockserverLoadScenarioResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists every registered load scenario with its lifecycle state (LOADED / PENDING / RUNNING / COMPLETED / STOPPED), startDelayMillis, full definition, and — when active or recently run — the live status fields (stage, virtual users, request counts, latency percentiles, run id, timestamps).
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

client.loadgen.list_all_registered_load_scenarios()

```
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

<details><summary><code>client.loadgen.<a href="src/fern/loadgen/client.py">load_register_a_load_scenario_into_the_registry</a>(...) -> PutMockserverLoadScenarioResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Loads (registers) an API load scenario into the named registry under its "name" (the unique registry key). Loading does NOT run the scenario — it is staged in the LOADED state, ready to be triggered by PUT /mockserver/loadScenario/start. Loading the same name replaces the prior definition. A scenario is an ordered list of templated request steps driven through a sequence of stages (a load profile): a stage holds/ramps virtual users (VU, closed model), holds/ramps an arrival rate in iterations/second (RATE, open model), or pauses; an optional startDelayMillis defers the start after a trigger. Loading is allowed even when loadGenerationEnabled is false (no traffic is generated). Hard caps validated at load time: max 50 virtual users, max 5000 iterations/second, max 20 stages, max 50 steps, max 1h total duration.
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
from fern import FernApi, LoadScenarioTemplateType, LoadProfile, LoadStage, LoadStageType, RampCurve, LoadStep, HttpRequest, KeyToMultiValueZeroItem, SocketAddress, SocketAddressScheme, LoadStepThinkTime
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.loadgen.load_register_a_load_scenario_into_the_registry(
    name="checkout-load",
    template_type=LoadScenarioTemplateType.VELOCITY,
    max_requests=5000,
    start_delay_millis=0,
    profile=LoadProfile(
        stages=[
            LoadStage(
                type=LoadStageType.VU,
                duration_millis=30000,
                curve=RampCurve.LINEAR,
                start_vus=1,
                end_vus=10,
            ),
            LoadStage(
                type=LoadStageType.VU,
                duration_millis=60000,
                vus=10,
            )
        ],
    ),
    steps=[
        LoadStep(
            request=HttpRequest(
                method="GET",
                path="/api/item/$iteration.index",
                headers=[
                    KeyToMultiValueZeroItem()
                ],
                socket_address=SocketAddress(
                    host="target.svc",
                    port=8080,
                    scheme=SocketAddressScheme.HTTP,
                ),
            ),
            think_time=LoadStepThinkTime(
                time_unit="MILLISECONDS",
                value=20,
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

**request:** `LoadScenario` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loadgen.<a href="src/fern/loadgen/client.py">clear_the_load_scenario_registry</a>() -> DeleteMockserverLoadScenarioResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes ALL registered load scenarios, stopping any that are running. Idempotent.
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

client.loadgen.clear_the_load_scenario_registry()

```
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

<details><summary><code>client.loadgen.<a href="src/fern/loadgen/client.py">retrieve_one_registered_load_scenario</a>(...) -> LoadScenarioListEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single registered load scenario (definition + state + live/terminal status). 404 if not registered.
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

client.loadgen.retrieve_one_registered_load_scenario(
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

**name:** `str` — the registered load scenario name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loadgen.<a href="src/fern/loadgen/client.py">remove_one_registered_load_scenario</a>(...) -> DeleteMockserverLoadScenarioNameResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes a single load scenario from the registry, stopping it first if it is running.
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

client.loadgen.remove_one_registered_load_scenario(
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

**name:** `str` — the registered load scenario name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loadgen.<a href="src/fern/loadgen/client.py">end_of_run_summary_report_for_a_load_scenario_run</a>(...) -> LoadScenarioReport</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an end-of-run summary report derived from the run's status snapshot — the live snapshot while running, or the retained terminal snapshot once finished. The default JSON form carries counts, latency percentiles, the threshold verdict and per-threshold results. With ?format=junit the same data is rendered as a JUnit-XML <testsuite> (one <testcase> per threshold, a <failure> per breach, plus a "run completed" testcase) so CI consumers render per-threshold pass/fail. 404 if the scenario never ran.
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

client.loadgen.end_of_run_summary_report_for_a_load_scenario_run(
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

**name:** `str` — the load scenario name
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[GetMockserverLoadScenarioNameReportRequestFormat]` — report format. Omit (or any value other than "junit") for the JSON report; "junit" returns a JUnit-XML <testsuite> (Content-Type application/xml) so a load run becomes a first-class CI test artifact.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loadgen.<a href="src/fern/loadgen/client.py">seed_a_load_scenario_from_an_open_api_specification</a>(...) -> PutMockserverLoadScenarioGenerateFromOpenApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates an editable load scenario from an OpenAPI spec and loads (registers) it into the registry under "name" in the LOADED state — exactly like PUT /mockserver/loadScenario, it generates no traffic and is allowed even when loadGenerationEnabled is false. One step is produced per OpenAPI operation (in a stable path-then-method order), each with the operation's method and server-prefixed path, a representative request-body example, and a Content-Type header. The spec is accepted identically to PUT /mockserver/openapi/expectation — an inline JSON/YAML payload, a URL, or a file/classpath reference. Target precedence for where each request is sent (carried as the request's Host header and secure flag): an explicit "target" wins, else the spec's servers[0] URL, else the request is left path-only for the operator to edit. When no "profile" is supplied a conservative default is applied (one short constant-VU stage) so the scenario is immediately runnable yet safe — the operator edits it before scaling up. The generated scenario is returned so a client/UI can show and edit it before triggering a run.
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
from fern.loadgen import PutMockserverLoadScenarioGenerateFromOpenApiRequestTarget, PutMockserverLoadScenarioGenerateFromOpenApiRequestTargetScheme

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.loadgen.seed_a_load_scenario_from_an_open_api_specification(
    name="petstore-load",
    spec_url_or_payload="openapi: 3.0.0\ninfo:\n  title: Petstore\n  version: 1.0.0\npaths:\n  /pets:\n    get:\n      operationId: listPets\n      responses:\n        \"200\":\n          description: a list of pets",
    target=PutMockserverLoadScenarioGenerateFromOpenApiRequestTarget(
        host="petstore.svc",
        port=8080,
        scheme=PutMockserverLoadScenarioGenerateFromOpenApiRequestTargetScheme.HTTP,
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

**name:** `str` — the generated scenario name (the unique registry key)
    
</dd>
</dl>

<dl>
<dd>

**spec_url_or_payload:** `str` — the OpenAPI spec as an inline JSON/YAML payload, a URL, or a file/classpath reference
    
</dd>
</dl>

<dl>
<dd>

**target:** `typing.Optional[PutMockserverLoadScenarioGenerateFromOpenApiRequestTarget]` — explicit network target for every generated step (overrides the spec's servers[0])
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[LoadProfile]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loadgen.<a href="src/fern/loadgen/client.py">seed_a_load_scenario_from_recorded_proxy_traffic</a>(...) -> PutMockserverLoadScenarioGenerateFromRecordingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates an editable load scenario from traffic previously recorded by MockServer in proxy/recording mode (the requests held by the event log) and loads (registers) it into the registry under "name" in the LOADED state — exactly like PUT /mockserver/loadScenario, it generates no traffic and is allowed even when loadGenerationEnabled is false. Two modes control how recorded requests become steps. VERBATIM (the default) emits one step per recorded request, in recorded order, preserving the concrete path, body and headers — with an optional "maxSteps" cap. TEMPLATIZED deduplicates recorded requests by (method, templatised-path) — id-shaped path segments such as /orders/123 collapse to /orders/{id} — keeping one representative example per unique route, ordered by descending hit frequency (most-hit routes first); each step's "weight" is set to its route's observed hit count and the scenario uses "stepSelection": "WEIGHTED" so replay reproduces the recorded traffic mix. An optional "requestFilter" (an HttpRequest matcher) selects which recorded requests to include; absent means all recorded requests. An optional "target" is applied to every step (overriding each recorded request's own Host/secure routing); absent leaves each recorded request's routing untouched. When no "profile" is supplied a conservative default is applied (one short constant-VU stage) so the scenario is immediately runnable yet safe — the operator edits it before scaling up. The generated scenario is returned so a client/UI can show and edit it before triggering a run.
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
from fern.loadgen import PutMockserverLoadScenarioGenerateFromRecordingRequestMode, PutMockserverLoadScenarioGenerateFromRecordingRequestTarget, PutMockserverLoadScenarioGenerateFromRecordingRequestTargetScheme

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.loadgen.seed_a_load_scenario_from_recorded_proxy_traffic(
    name="replay-prod-traffic",
    mode=PutMockserverLoadScenarioGenerateFromRecordingRequestMode.TEMPLATIZED,
    target=PutMockserverLoadScenarioGenerateFromRecordingRequestTarget(
        host="staging.svc",
        port=8080,
        scheme=PutMockserverLoadScenarioGenerateFromRecordingRequestTargetScheme.HTTP,
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

**name:** `str` — the generated scenario name (the unique registry key)
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[PutMockserverLoadScenarioGenerateFromRecordingRequestMode]` — VERBATIM = one step per recorded request; TEMPLATIZED = one step per unique (method, templatised-path) route, ordered by descending frequency
    
</dd>
</dl>

<dl>
<dd>

**request_filter:** `typing.Optional[HttpRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**max_steps:** `typing.Optional[int]` — optional cap on the number of VERBATIM steps (keeps the first N recorded requests)
    
</dd>
</dl>

<dl>
<dd>

**target:** `typing.Optional[PutMockserverLoadScenarioGenerateFromRecordingRequestTarget]` — explicit network target applied to every generated step (overrides each recorded request's own Host/secure routing)
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[LoadProfile]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loadgen.<a href="src/fern/loadgen/client.py">trigger_registered_load_scenario_s_to_run</a>(...) -> PutMockserverLoadScenarioStartResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Triggers one or more registered load scenarios to start running concurrently. Each gets a fresh run id and honours its own startDelayMillis (a positive delay → the scenario is PENDING until the delay elapses, then RUNNING). Requires loadGenerationEnabled=true (else 403). 404 if a name is not registered. Rejected with 400 if it would exceed loadGenerationMaxConcurrentScenarios (default 10). Re-triggering an already-active name replaces that run.
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

client.loadgen.trigger_registered_load_scenario_s_to_run(
    names=[
        "checkout-load",
        "background-poller"
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

**names:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loadgen.<a href="src/fern/loadgen/client.py">stop_running_load_scenario_s</a>(...) -> PutMockserverLoadScenarioStopResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stops one or more running load scenarios. Body is {"names":[...]}, {"all":true}, or an empty body (stop all running). Stopped scenarios stay registered (state STOPPED) and can be re-triggered.
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

client.loadgen.stop_running_load_scenario_s(
    names=[
        "checkout-load"
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

**names:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**all:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Slo
<details><summary><code>client.slo.<a href="src/fern/slo/client.py">verify_a_service_level_objective_over_a_window</a>(...) -> SloVerdict</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Evaluates a named set of objectives (latency percentiles, error rate) over a time window against the recorded forward-path SLI samples and returns a PASS / FAIL / INCONCLUSIVE verdict. The HTTP status encodes the verdict so a CI or chaos gate can assert on the status code alone: 200 when the verdict is PASS or INCONCLUSIVE, 406 when it is FAIL. A criteria PASSes only when all objectives hold (logical AND); it is INCONCLUSIVE when an indicator cannot be computed or the window holds fewer than minimumSampleCount samples. Off by default — returns 400 until sloTrackingEnabled=true.
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
from fern import FernApi, SloObjective, SloObjectiveSli, SloObjectiveComparator, SloObjectiveScope
from fern.environment import FernApiEnvironment
from fern.slo import SloCriteriaWindow, SloCriteriaWindowType

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.slo.verify_a_service_level_objective_over_a_window(
    name="checkout-slo",
    window=SloCriteriaWindow(
        type=SloCriteriaWindowType.LOOKBACK,
        lookback_millis=60000,
    ),
    minimum_sample_count=20,
    upstream_hosts=[
        "payments.svc"
    ],
    objectives=[
        SloObjective(
            sli=SloObjectiveSli.LATENCY_P95,
            comparator=SloObjectiveComparator.LESS_THAN,
            threshold=250,
            scope=SloObjectiveScope.FORWARD,
        ),
        SloObjective(
            sli=SloObjectiveSli.ERROR_RATE,
            comparator=SloObjectiveComparator.LESS_THAN_OR_EQUAL,
            threshold=0.01,
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

**objectives:** `typing.List[SloObjective]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — human-readable criteria name, echoed back in the verdict
    
</dd>
</dl>

<dl>
<dd>

**window:** `typing.Optional[SloCriteriaWindow]` — the time window to evaluate over
    
</dd>
</dl>

<dl>
<dd>

**minimum_sample_count:** `typing.Optional[int]` — minimum samples required in the window; below this the verdict is INCONCLUSIVE
    
</dd>
</dl>

<dl>
<dd>

**upstream_hosts:** `typing.Optional[typing.List[str]]` — optional list of upstream hosts to restrict the evaluation to
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Contract
<details><summary><code>client.contract.<a href="src/fern/contract/client.py">run_an_open_api_spec_as_a_contract_test_against_a_live_service</a>(...) -> ContractTestReport</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Runs each operation of an OpenAPI specification against a live service and validates that the actual responses conform to the spec. Supply the spec as a URL, file path or inline JSON/YAML ("spec", or its alias "specUrlOrPayload"), the base URL of the service under test ("baseUrl"), and optionally a single "operationId" to restrict the run. The target host is subject to the SSRF policy (forwardProxyBlockPrivateNetworks). Returns a per-operation pass/fail report.
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

client.contract.run_an_open_api_spec_as_a_contract_test_against_a_live_service(
    spec="openapi: 3.0.0\ninfo:\n  title: Petstore\n  version: 1.0.0\npaths:\n  /pets:\n    get:\n      operationId: listPets\n      responses:\n        \"200\":\n          description: a list of pets",
    base_url="http://localhost:8080",
    operation_id="listPets",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**spec:** `str` — the OpenAPI spec as a URL, file path, or inline JSON/YAML (alias: specUrlOrPayload)
    
</dd>
</dl>

<dl>
<dd>

**base_url:** `str` — base URL of the live service under test; any path prefix is prepended to each operation path
    
</dd>
</dl>

<dl>
<dd>

**spec_url_or_payload:** `typing.Optional[str]` — alias for spec
    
</dd>
</dl>

<dl>
<dd>

**operation_id:** `typing.Optional[str]` — optional — restrict the run to a single operation; when absent all operations are tested
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Metrics
<details><summary><code>client.metrics.<a href="src/fern/metrics/client.py">scrape_prometheus_metrics</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Serves the Prometheus metrics exposition when `metricsEnabled` is set, negotiating the text or OpenMetrics format from the Accept header. Returns 404 when metrics are disabled. Unlike its sibling control-plane endpoints this path has deliberately NO bare `/metrics` alias, because `/metrics` is a plausible path for a user's own mocked API and reserving it would shadow their expectation. It is gated by control-plane authentication like every neighbouring endpoint; since control-plane authentication is off by default an unauthenticated scrape keeps working on a default instance.
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

client.metrics.scrape_prometheus_metrics()

```
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

## Cluster
<details><summary><code>client.cluster.<a href="src/fern/cluster/client.py">retrieve_cluster_membership_status</a>() -> GetMockserverClusterResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reports whether this instance is running clustered, its node id, whether it is the coordinator, and the current member list. `clusterName` is omitted entirely when the instance is not clustered.
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

client.cluster.retrieve_cluster_membership_status()

```
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

## Llm
<details><summary><code>client.llm.<a href="src/fern/llm/client.py">retrieve_the_llm_optimisation_report</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Analyses captured LLM traffic and reports optimisation signals (cost, latency, token usage, prompt and response characteristics) with an overall verdict. The report can also be emitted in evaluation-dataset formats for downstream tooling. An empty capture is a 200 with an empty report, not an error.
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

client.llm.retrieve_the_llm_optimisation_report()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**format:** `typing.Optional[GetMockserverLlmOptimisationReportRequestFormat]` — output format; defaults to json. The dataset formats also accept the aliases `evals` (openai-evals) and `finetune` (fine-tune), and underscores in place of hyphens.
    
</dd>
</dl>

<dl>
<dd>

**session:** `typing.Optional[str]` — restrict the report to a single captured session
    
</dd>
</dl>

<dl>
<dd>

**host:** `typing.Optional[str]` — restrict the report to a single upstream host
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — restrict the report to a single LLM provider
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.llm.<a href="src/fern/llm/client.py">diff_two_captured_llm_agent_runs</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compares two captured agent runs, each selected by session, host and/or provider, and reports where they diverge. Normalization options control which incidental differences are ignored before comparing. The request body is optional — an empty body is treated as an empty filter on both sides.
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
from fern.llm import PutMockserverLlmDiffRunsRequestBefore, PutMockserverLlmDiffRunsRequestAfter

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.llm.diff_two_captured_llm_agent_runs(
    before=PutMockserverLlmDiffRunsRequestBefore(
        session="run-1",
    ),
    after=PutMockserverLlmDiffRunsRequestAfter(
        session="run-2",
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

**before:** `typing.Optional[PutMockserverLlmDiffRunsRequestBefore]` 
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[PutMockserverLlmDiffRunsRequestAfter]` 
    
</dd>
</dl>

<dl>
<dd>

**normalization:** `typing.Optional[typing.Dict[str, typing.Any]]` — options controlling which incidental differences are ignored
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.mcp.<a href="src/fern/mcp/client.py">not_supported</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Documented so the behaviour is not mistaken for SSE support: MockServer's MCP endpoint does not implement the server-initiated SSE stream, and a GET is always refused.
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

client.mcp.not_supported()

```
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

<details><summary><code>client.mcp.<a href="src/fern/mcp/client.py">mcp_model_context_protocol_json_rpc_endpoint</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Streamable-HTTP MCP endpoint, letting AI agents and LLM tooling drive MockServer as an MCP server. The body is a JSON-RPC 2.0 request object or a batch array. Call `initialize` first; the response carries a new session id in the `Mcp-Session-Id` response header, which subsequent calls must send back in the `Mcp-Session-Id` request header. Protocol versions 2025-06-18 (default), 2025-03-26 and 2024-11-05 are negotiated. Note that a missing or invalid session is reported as a JSON-RPC error inside a 200 response, not as a 4xx. Unlike its sibling endpoints this path has no bare `/mcp` alias, and sub-paths under `/mockserver/mcp/` also route here.
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

client.mcp.mcp_model_context_protocol_json_rpc_endpoint(
    request={
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "example-client", "version": "1.0.0"}}
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

**request:** `typing.Dict[str, typing.Any]` — a JSON-RPC 2.0 request object, or an array of them for a batch
    
</dd>
</dl>

<dl>
<dd>

**mcp_session_id:** `typing.Optional[str]` — session id returned by a previous `initialize` call; omit on `initialize` itself
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mcp.<a href="src/fern/mcp/client.py">end_an_mcp_session</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes the MCP session identified by the `Mcp-Session-Id` request header.
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

client.mcp.end_an_mcp_session(
    mcp_session_id="Mcp-Session-Id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**mcp_session_id:** `str` — the session to end
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

