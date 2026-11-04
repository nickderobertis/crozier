# Reference
## Components
<details><summary><code>client.components.<a href="src/fern/components/client.py">get_api_components_id_usages</a>(...) -> typing.List[ComponentUsagesInScenario]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.components.get_api_components_id_usages(
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

<details><summary><code>client.components.<a href="src/fern/components/client.py">get_api_components</a>(...) -> typing.List[ComponentListElement]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.components.get_api_components()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**skip_usages:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**skip_fragments:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Deployments
<details><summary><code>client.deployments.<a href="src/fern/deployments/client.py">get_api_actioninfo_scenarioname_parameters</a>(...) -> UiActionParametersDto</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.deployments.get_api_actioninfo_scenarioname_parameters(
    scenario_name="scenarioName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deployments.<a href="src/fern/deployments/client.py">get_api_deployments_deploymentid_status</a>(...) -> GetDeploymentStatusResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.deployments.get_api_deployments_deploymentid_status(
    deployment_id="a9a1e269-0b71-4582-a948-603482d27298",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**deployment_id:** `str` — Identifier in the UUID format that will be used for the verification of deployment's status
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deployments.<a href="src/fern/deployments/client.py">put_api_deployments_deploymentid</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.deployments.put_api_deployments_deploymentid(
    deployment_id="a9a1e269-0b71-4582-a948-603482d27298",
    scenario_name="scenario1",
    nodes_deployment_data={
        "sourceNodeId1": "field1 = \'value\'"
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

**deployment_id:** `str` — Identifier in the UUID format that will be used for the verification of deployment's status
    
</dd>
</dl>

<dl>
<dd>

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**nodes_deployment_data:** `MapNodeIdString` 
    
</dd>
</dl>

<dl>
<dd>

**comment:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## App
<details><summary><code>client.app.<a href="src/fern/app/client.py">get_api_app_healthcheck</a>() -> HealthCheckProcessSuccessResponseDto</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.app.get_api_app_healthcheck()

```
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

<details><summary><code>client.app.<a href="src/fern/app/client.py">get_api_app_leader</a>() -> LeaderResponseDto</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.app.get_api_app_leader()

```
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

<details><summary><code>client.app.<a href="src/fern/app/client.py">get_api_app_buildinfo</a>() -> BuildInfoDto</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.app.get_api_app_buildinfo()

```
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

<details><summary><code>client.app.<a href="src/fern/app/client.py">post_api_app_processingtype_reload</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.app.post_api_app_processingtype_reload()

```
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

<details><summary><code>client.app.<a href="src/fern/app/client.py">post_api_app_model_reload</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.app.post_api_app_model_reload()

```
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

<details><summary><code>client.app.<a href="src/fern/app/client.py">get_api_app_healthcheck_process_deployment</a>() -> HealthCheckProcessSuccessResponseDto</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.app.get_api_app_healthcheck_process_deployment()

```
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

<details><summary><code>client.app.<a href="src/fern/app/client.py">get_api_app_healthcheck_process_validation</a>() -> HealthCheckProcessSuccessResponseDto</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.app.get_api_app_healthcheck_process_validation()

```
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

<details><summary><code>client.app.<a href="src/fern/app/client.py">get_api_app_config</a>() -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.app.get_api_app_config()

```
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

<details><summary><code>client.app.<a href="src/fern/app/client.py">get_api_app_config_categorieswithprocessingtype</a>() -> MapString</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.app.get_api_app_config_categorieswithprocessingtype()

```
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

<details><summary><code>client.app.<a href="src/fern/app/client.py">get_api_scenarioparameterscombinations</a>() -> ScenarioParametersCombinationWithEngineErrors</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.app.get_api_scenarioparameterscombinations()

```
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

## Dictionary
<details><summary><code>client.dictionary.<a href="src/fern/dictionary/client.py">get_api_processdefinitiondata_processingtype_dicts_dictid_entrybykey</a>(...) -> DictEntry</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.dictionary.get_api_processdefinitiondata_processingtype_dicts_dictid_entrybykey(
    processing_type="processingType",
    dict_id="dictId",
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

**processing_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**dict_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dictionary.<a href="src/fern/dictionary/client.py">get_api_processdefinitiondata_processingtype_dicts_dictid_entry</a>(...) -> typing.List[DictEntry]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.dictionary.get_api_processdefinitiondata_processingtype_dicts_dictid_entry(
    processing_type="processingType",
    dict_id="dictId",
    label="label",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**processing_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**dict_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**label:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dictionary.<a href="src/fern/dictionary/client.py">post_api_processdefinitiondata_processingtype_dicts</a>(...) -> typing.List[DictDto]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.dictionary.post_api_processdefinitiondata_processingtype_dicts(
    processing_type="processingType",
    expected_type={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**processing_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expected_type:** `typing.Any` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Migrations
<details><summary><code>client.migrations.<a href="src/fern/migrations/client.py">post_api_migrate</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.migrations.post_api_migrate(
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

**request:** `MigrateScenarioRequestDto` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.migrations.<a href="src/fern/migrations/client.py">get_api_migration_scenario_description_version</a>() -> ApiVersion</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.migrations.get_api_migration_scenario_description_version()

```
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

## Nodes
<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">post_api_nodes_scenarioname_additionalinfo</a>(...) -> typing.Optional[AdditionalInfo]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, NodeData_Enricher, ServiceRef, Parameter, Expression

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.nodes.post_api_nodes_scenarioname_additionalinfo(
    scenario_name="scenarioName",
    request=NodeData_Enricher(
        id="99ae6a31-a55d-4d52-89af-58f471e7143d",
        output="out",
        service=ServiceRef(
            id="paramService",
            parameters=[
                Parameter(
                    name="id",
                    expression=Expression(
                        language="spel",
                        expression="\'a\'",
                    ),
                )
            ],
        ),
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

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `NodeData` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">post_api_nodes_scenarioname_validation</a>(...) -> NodeValidationResultDto</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, NodeData_Filter, Expression, MapTypingResultInJsonValue_TypedClass

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.nodes.post_api_nodes_scenarioname_validation(
    scenario_name="scenarioName",
    node_data=NodeData_Filter(
        expression=Expression(
            language="spel",
            expression="#longValue > 1",
        ),
        id="99ae6a31-a55d-4d52-89af-58f471e7143d",
    ),
    variable_types={
        "existButString": MapTypingResultInJsonValue_TypedClass(
            ref_clazz_name="refClazzName",
        ),
        "longValue": MapTypingResultInJsonValue_TypedClass(
            ref_clazz_name="refClazzName",
        )
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

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**node_data:** `NodeData` 
    
</dd>
</dl>

<dl>
<dd>

**variable_types:** `MapTypingResultInJson` 
    
</dd>
</dl>

<dl>
<dd>

**branch_variable_types:** `typing.Optional[MapMapStringTypingResultInJson]` 
    
</dd>
</dl>

<dl>
<dd>

**outgoing_edges:** `typing.Optional[typing.List[Edge]]` 
    
</dd>
</dl>

<dl>
<dd>

**test_cases:** `typing.Optional[MapNodeTestCase]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">post_api_parameters_processingtype_suggestions</a>(...) -> typing.List[ExpressionSuggestionDto]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Expression, CaretPosition2D, MapTypingResultInJsonValue_TypedObjectTypingResult, TypingResult_TypedClass

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.nodes.post_api_parameters_processingtype_suggestions(
    processing_type="processingType",
    expression=Expression(
        language="spel",
        expression="#inpu",
    ),
    caret_position2d=CaretPosition2D(
        row=0,
        column=5,
    ),
    variable_types={
        "input": MapTypingResultInJsonValue_TypedObjectTypingResult(
            fields={
                "key": TypingResult_TypedClass(
                    ref_clazz_name="refClazzName",
                )
            },
            ref_clazz_name="refClazzName",
        )
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

**processing_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expression:** `Expression` 
    
</dd>
</dl>

<dl>
<dd>

**caret_position2d:** `CaretPosition2D` 
    
</dd>
</dl>

<dl>
<dd>

**variable_types:** `MapTypingResultInJson` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">post_api_parameters_processingtype_validate</a>(...) -> ParametersValidationResultDto</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, UiValueParameterDto, UiValueParameterDtoTyp_TypedClass, Expression, MapTypingResultInJsonValue_TypedObjectTypingResult, TypingResult_TypedClass

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.nodes.post_api_parameters_processingtype_validate(
    processing_type="processingType",
    parameters=[
        UiValueParameterDto(
            name="condition",
            typ=UiValueParameterDtoTyp_TypedClass(
                ref_clazz_name="refClazzName",
            ),
            expression=Expression(
                language="spel",
                expression="#input.amount > 2",
            ),
        )
    ],
    variable_types={
        "input": MapTypingResultInJsonValue_TypedObjectTypingResult(
            fields={
                "key": TypingResult_TypedClass(
                    ref_clazz_name="refClazzName",
                )
            },
            ref_clazz_name="refClazzName",
        )
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

**processing_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**variable_types:** `MapTypingResultInJson` 
    
</dd>
</dl>

<dl>
<dd>

**parameters:** `typing.Optional[typing.List[UiValueParameterDto]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">post_api_properties_scenarioname_additionalinfo</a>(...) -> typing.Optional[AdditionalInfo]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.nodes.post_api_properties_scenarioname_additionalinfo(
    scenario_name="scenarioName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">post_api_properties_scenarioname_validation</a>(...) -> NodeValidationResultDto</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ProcessAdditionalFields

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.nodes.post_api_properties_scenarioname_validation(
    scenario_name="scenarioName",
    additional_fields=ProcessAdditionalFields(
        properties={
            "parallelism": "",
            "checkpointIntervalInSeconds": "",
            "numberOfThreads": "2",
            "spillStateToDisk": "true",
            "environment": "test",
            "useAsyncInterpretation": ""
        },
        meta_data_type="StreamMetaData",
        show_description=False,
    ),
    name="test",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**additional_fields:** `ProcessAdditionalFields` 
    
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

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">post_api_nodes_scenarioname_records</a>(...) -> str</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, NodeData_Variable, VariableOperationSchemaType, Expression

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.nodes.post_api_nodes_scenarioname_records(
    scenario_name="scenarioName",
    node_data=NodeData_Variable(
        id="id",
        operation=VariableOperationSchemaType.SET,
        var_name="varName",
        value=Expression(
            language="language",
            expression="expression",
        ),
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

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**node_data:** `NodeData` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the number of records returned
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">post_api_parameters_processingtype_testcase_additionalvariables</a>(...) -> TestCaseAdditionalVariablesResponseDto</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, MapTypingResultInJsonValue_TypedClass

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.nodes.post_api_parameters_processingtype_testcase_additionalvariables(
    processing_type="processingType",
    variable_types={
        "amount": MapTypingResultInJsonValue_TypedClass(
            ref_clazz_name="refClazzName",
        ),
        "name": MapTypingResultInJsonValue_TypedClass(
            ref_clazz_name="refClazzName",
        )
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

**processing_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**variable_types:** `MapTypingResultInJson` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">post_api_nodes_scenarioname_testcase_enrichermock</a>(...) -> typing.Optional[GenerateEnricherMockResponseDto]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, MapTypingResultInJsonValue_TypedClass, ServiceRef, Parameter, Expression, NodeTypes2
from fern.nodes import GenerateEnricherMockRequestDtoEnricher

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.nodes.post_api_nodes_scenarioname_testcase_enrichermock(
    scenario_name="scenarioName",
    variable_types={
        "amount": MapTypingResultInJsonValue_TypedClass(
            ref_clazz_name="refClazzName",
        ),
        "name": MapTypingResultInJsonValue_TypedClass(
            ref_clazz_name="refClazzName",
        )
    },
    enricher=GenerateEnricherMockRequestDtoEnricher(
        id="99ae6a31-a55d-4d52-89af-58f471e7143d",
        output="out",
        service=ServiceRef(
            id="paramService",
            parameters=[
                Parameter(
                    name="param",
                    expression=Expression(
                        language="spel",
                        expression="#input.id",
                    ),
                )
            ],
        ),
        type=NodeTypes2.ENRICHER,
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

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**variable_types:** `MapTypingResultInJson` 
    
</dd>
</dl>

<dl>
<dd>

**enricher:** `GenerateEnricherMockRequestDtoEnricher` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Notifications
<details><summary><code>client.notifications.<a href="src/fern/notifications/client.py">get_api_notifications</a>(...) -> typing.List[Notification]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.notifications.get_api_notifications()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scenario_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ScenarioLabels
<details><summary><code>client.scenario_labels.<a href="src/fern/scenario_labels/client.py">get_api_scenariolabels</a>() -> ScenarioLabels</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.scenario_labels.get_api_scenariolabels()

```
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

<details><summary><code>client.scenario_labels.<a href="src/fern/scenario_labels/client.py">post_api_scenariolabels_validation</a>(...) -> ScenarioLabelsValidationResponseDto</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.scenario_labels.post_api_scenariolabels_validation(
    labels=[
        "Label_1",
        "Label_2"
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

**labels:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Statistics
<details><summary><code>client.statistics.<a href="src/fern/statistics/client.py">post_api_statistic</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.statistics.post_api_statistic()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**statistics:** `typing.Optional[typing.List[StatisticDto]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.statistics.<a href="src/fern/statistics/client.py">get_api_statistic_usage</a>() -> StatisticUrlResponseDto</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.statistics.get_api_statistic_usage()

```
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
<details><summary><code>client.user.<a href="src/fern/user/client.py">get_api_user</a>() -> DisplayableUser</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.user.get_api_user()

```
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

## VersionControl
<details><summary><code>client.version_control.<a href="src/fern/version_control/client.py">post_api_versioncontrol_scenarioname_versionvalidation</a>(...) -> ProcessVersionValidationResponseDto</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.version_control.post_api_versioncontrol_scenarioname_versionvalidation(
    scenario_name="scenarioName",
    local_version=24,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**local_version:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Activities
<details><summary><code>client.activities.<a href="src/fern/activities/client.py">post_api_processes_scenarioname_versionid_activity_attachments</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.activities.post_api_processes_scenarioname_versionid_activity_attachments(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**version_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.activities.<a href="src/fern/activities/client.py">post_api_processes_scenarioname_versionid_activity_comment</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.activities.post_api_processes_scenarioname_versionid_activity_comment(
    scenario_name="scenarioName",
    version_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**version_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.activities.<a href="src/fern/activities/client.py">get_api_processes_scenarioname_activity_attachments</a>(...) -> ScenarioAttachments</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.activities.get_api_processes_scenarioname_activity_attachments(
    scenario_name="scenarioName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.activities.<a href="src/fern/activities/client.py">get_api_processes_scenarioname_activity_attachments_attachmentid</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.activities.get_api_processes_scenarioname_activity_attachments_attachmentid(
    scenario_name="scenarioName",
    attachment_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.activities.<a href="src/fern/activities/client.py">delete_api_processes_scenarioname_activity_attachments_attachmentid</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.activities.delete_api_processes_scenarioname_activity_attachments_attachmentid(
    scenario_name="scenarioName",
    attachment_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.activities.<a href="src/fern/activities/client.py">put_api_processes_scenarioname_activity_comment_scenarioactivityid</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.activities.put_api_processes_scenarioname_activity_comment_scenarioactivityid(
    scenario_name="scenarioName",
    scenario_activity_id="scenarioActivityId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**scenario_activity_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.activities.<a href="src/fern/activities/client.py">delete_api_processes_scenarioname_activity_comment_scenarioactivityid</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.activities.delete_api_processes_scenarioname_activity_comment_scenarioactivityid(
    scenario_name="scenarioName",
    scenario_activity_id="scenarioActivityId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**scenario_activity_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.activities.<a href="src/fern/activities/client.py">post_api_processes_scenarioname_versionid_activity_comments</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.activities.post_api_processes_scenarioname_versionid_activity_comments(
    scenario_name="scenarioName",
    version_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**version_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.activities.<a href="src/fern/activities/client.py">delete_api_processes_scenarioname_activity_comments_commentid</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.activities.delete_api_processes_scenarioname_activity_comments_commentid(
    scenario_name="scenarioName",
    comment_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**comment_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.activities.<a href="src/fern/activities/client.py">get_api_processes_scenarioname_activity</a>(...) -> ProcessActivity</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.activities.get_api_processes_scenarioname_activity(
    scenario_name="scenarioName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.activities.<a href="src/fern/activities/client.py">get_api_processes_scenarioname_activity_activities</a>(...) -> ScenarioActivities</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.activities.get_api_processes_scenarioname_activity_activities(
    scenario_name="scenarioName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.activities.<a href="src/fern/activities/client.py">get_api_processes_scenarioname_activity_activities_metadata</a>(...) -> ScenarioActivitiesMetadata</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.activities.get_api_processes_scenarioname_activity_activities_metadata(
    scenario_name="scenarioName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## LiveData
<details><summary><code>client.live_data.<a href="src/fern/live_data/client.py">get_api_livedata_scenarioname</a>(...) -> typing.Optional[ResultsWithCountsDto]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.live_data.get_api_livedata_scenarioname(
    scenario_name="scenarioName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Testing
<details><summary><code>client.testing.<a href="src/fern/testing/client.py">post_api_scenariotesting_scenarioname_performmultipletestcases</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TestCase, EnricherMock, Expression, ExpressionAssertion

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.testing.post_api_scenariotesting_scenarioname_performmultipletestcases(
    scenario_name="scenarioName",
    scenario_graph={
        "key": "value"
    },
    test_cases=[
        TestCase(
            id="id",
            name="name",
            inputs="inputs",
            mocks={
                "key": EnricherMock(
                    expression=Expression(
                        language="language",
                        expression="expression",
                    ),
                    enabled=True,
                )
            },
            assertions={
                "key": [
                    ExpressionAssertion(
                        expression=Expression(
                            language="language",
                            expression="expression",
                        ),
                    )
                ]
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

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**scenario_graph:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**test_cases:** `typing.List[TestCase]` 
    
</dd>
</dl>

<dl>
<dd>

**skip_results_per_node:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**skip_results_per_transition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.testing.<a href="src/fern/testing/client.py">post_api_scenariotesting_scenarioname_capabilities</a>(...) -> ScenarioTestCapabilities</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.testing.post_api_scenariotesting_scenarioname_capabilities(
    scenario_name="scenarioName",
    request={
        "properties": {"additionalFields": {"properties": {"parallelism": "", "spillStateToDisk": "true", "useAsyncInterpretation": "", "checkpointIntervalInSeconds": ""}, "metaDataType": "StreamMetaData", "showDescription": False}}
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

**scenario_name:** `str` 
    
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

<details><summary><code>client.testing.<a href="src/fern/testing/client.py">post_api_scenariotesting_scenarioname_performtestcase</a>(...) -> ResultsWithCountsDto</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TestCase, EnricherMock, Expression, ExpressionAssertion

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.testing.post_api_scenariotesting_scenarioname_performtestcase(
    scenario_name="scenarioName",
    scenario_graph={
        "key": "value"
    },
    test_case=TestCase(
        id="id",
        name="name",
        inputs="inputs",
        mocks={
            "key": EnricherMock(
                expression=Expression(
                    language="language",
                    expression="expression",
                ),
                enabled=True,
            )
        },
        assertions={
            "key": [
                ExpressionAssertion(
                    expression=Expression(
                        language="language",
                        expression="expression",
                    ),
                )
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

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**scenario_graph:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**test_case:** `TestCase` 
    
</dd>
</dl>

<dl>
<dd>

**skip_results_per_node:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**skip_results_per_transition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.testing.<a href="src/fern/testing/client.py">post_api_scenariotesting_scenarioname_performtest</a>(...) -> ResultsWithCountsDto</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, WithLiveData

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.testing.post_api_scenariotesting_scenarioname_performtest(
    scenario_name="scenarioName",
    scenario_graph={
        "key": "value"
    },
    test_data=WithLiveData(
        number_of_samples=1,
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

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**scenario_graph:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**test_data:** `ScenarioTestData` 
    
</dd>
</dl>

<dl>
<dd>

**skip_results_per_node:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**skip_results_per_transition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.testing.<a href="src/fern/testing/client.py">post_api_scenariotesting_scenarioname_generatedtestdata</a>(...) -> str</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.testing.post_api_scenariotesting_scenarioname_generatedtestdata(
    scenario_name="scenarioName",
    scenario_graph={
        "scenarioGraph": {"key": "value"}
    },
    number_of_samples=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**scenario_graph:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**number_of_samples:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.testing.<a href="src/fern/testing/client.py">post_api_scenariotesting_scenarioname_validate</a>(...) -> ParametersValidationResultDto</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, WithParameters, TestSourceParameters, Expression

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.testing.post_api_scenariotesting_scenarioname_validate(
    scenario_name="scenarioName",
    scenario_graph={
        "properties": {"additionalFields": {"properties": {"parallelism": "", "spillStateToDisk": "true", "useAsyncInterpretation": "", "checkpointIntervalInSeconds": ""}, "metaDataType": "StreamMetaData", "showDescription": False}}
    },
    test_data=WithParameters(
        source_parameters=TestSourceParameters(
            source_id="source",
            parameter_expressions={
                "name": Expression(
                    language="spel",
                    expression="\'Amadeus\'",
                )
            },
        ),
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

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**scenario_graph:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**test_data:** `ScenarioTestData` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.testing.<a href="src/fern/testing/client.py">post_api_scenariotesting_scenarioname_sourcecapabilities</a>(...) -> SourceTestCapabilities</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, NodeData_Variable, VariableOperationSchemaType, Expression

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.testing.post_api_scenariotesting_scenarioname_sourcecapabilities(
    scenario_name="scenarioName",
    node_data=NodeData_Variable(
        id="id",
        operation=VariableOperationSchemaType.SET,
        var_name="varName",
        value=Expression(
            language="language",
            expression="expression",
        ),
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

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**node_data:** `NodeData` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.testing.<a href="src/fern/testing/client.py">post_api_scenariotesting_scenarioname_sourcevalidate</a>(...) -> ParametersValidationResultDto</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, NodeData_Variable, VariableOperationSchemaType, Expression, TestSourceParameters

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.testing.post_api_scenariotesting_scenarioname_sourcevalidate(
    scenario_name="scenarioName",
    node_data=NodeData_Variable(
        id="id",
        operation=VariableOperationSchemaType.SET,
        var_name="varName",
        value=Expression(
            language="language",
            expression="expression",
        ),
    ),
    source_parameters=TestSourceParameters(
        source_id="sourceId",
        parameter_expressions={
            "key": Expression(
                language="language",
                expression="expression",
            )
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

**scenario_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**node_data:** `NodeData` 
    
</dd>
</dl>

<dl>
<dd>

**source_parameters:** `TestSourceParameters` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

