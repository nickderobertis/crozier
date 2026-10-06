# Reference
## CardResource
<details><summary><code>client.card_resource.<a href="src/fern/card_resource/client.py">post_card_change_pin</a>(...) -> ChangePinResponse</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.card_resource.post_card_change_pin()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**card_handle:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**pin_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.card_resource.<a href="src/fern/card_resource/client.py">get_card_pin_status</a>(...) -> GetPinStatusResponse</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.card_resource.get_card_pin_status()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**card_handle:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**pin_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.card_resource.<a href="src/fern/card_resource/client.py">post_card_unblock_pin</a>() -> UnblockPinResponse</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.card_resource.post_card_unblock_pin()

```
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

<details><summary><code>client.card_resource.<a href="src/fern/card_resource/client.py">post_card_verify_pin</a>() -> VerifyPinResponse</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.card_resource.post_card_verify_pin()

```
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

## UserConfigurationsResource
<details><summary><code>client.user_configurations_resource.<a href="src/fern/user_configurations_resource/client.py">get_config</a>()</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.user_configurations_resource.get_config()

```
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

<details><summary><code>client.user_configurations_resource.<a href="src/fern/user_configurations_resource/client.py">put_config</a>(...)</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.user_configurations_resource.put_config()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**erixa_hotfolder:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**erixa_drugstore_email:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**erixa_user_email:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**erixa_user_password:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**erixa_api_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**extractor_template_profile:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**connector_base_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**connector_mandant_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**connector_workplace_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**connector_client_system_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**connector_user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**connector_version:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**connector_tv_mode:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**connector_client_certificate:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**connector_client_certificate_password:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**connector_basic_auth_username:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**connector_basic_auth_password:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**kbv_pruefnummer:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## DocumentResource
<details><summary><code>client.document_resource.<a href="src/fern/document_resource/client.py">post_document_bundles</a>()</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.document_resource.post_document_bundles()

```
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

## XsltResource
<details><summary><code>client.xslt_resource.<a href="src/fern/xslt_resource/client.py">post_kbv_transform</a>()</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.xslt_resource.post_kbv_transform()

```
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

## PharmacyResource
<details><summary><code>client.pharmacy_resource.<a href="src/fern/pharmacy_resource/client.py">get_pharmacy_accept</a>(...) -> Bundle</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.pharmacy_resource.get_pharmacy_accept()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**token:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pharmacy_resource.<a href="src/fern/pharmacy_resource/client.py">get_pharmacy_task</a>(...) -> Bundle</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.pharmacy_resource.get_pharmacy_task()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**egk_handle:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**smcb_handle:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PreviewResource
<details><summary><code>client.preview_resource.<a href="src/fern/preview_resource/client.py">post_preview_generate</a>() -> str</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.preview_resource.post_preview_generate()

```
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

## StatusResource
<details><summary><code>client.status_resource.<a href="src/fern/status_resource/client.py">get_status</a>()</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.status_resource.get_status()

```
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

## PrescriptionBundleValidatorResource
<details><summary><code>client.prescription_bundle_validator_resource.<a href="src/fern/prescription_bundle_validator_resource/client.py">post_validate</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, JsonValue

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.prescription_bundle_validator_resource.post_validate(
    request={
        "key": JsonValue()
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

**request:** `typing.Dict[str, JsonValue]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ERezeptWorkflowResource
<details><summary><code>client.e_rezept_workflow_resource.<a href="src/fern/e_rezept_workflow_resource/client.py">post_workflow_abort</a>(...)</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.e_rezept_workflow_resource.post_workflow_abort()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**access_code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.e_rezept_workflow_resource.<a href="src/fern/e_rezept_workflow_resource/client.py">post_workflow_batch_sign</a>()</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.e_rezept_workflow_resource.post_workflow_batch_sign()

```
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

<details><summary><code>client.e_rezept_workflow_resource.<a href="src/fern/e_rezept_workflow_resource/client.py">get_workflow_cards</a>() -> GetCardsResponse</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.e_rezept_workflow_resource.get_workflow_cards()

```
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

<details><summary><code>client.e_rezept_workflow_resource.<a href="src/fern/e_rezept_workflow_resource/client.py">post_workflow_comfortsignature_activate</a>()</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.e_rezept_workflow_resource.post_workflow_comfortsignature_activate()

```
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

<details><summary><code>client.e_rezept_workflow_resource.<a href="src/fern/e_rezept_workflow_resource/client.py">post_workflow_comfortsignature_deactivate</a>()</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.e_rezept_workflow_resource.post_workflow_comfortsignature_deactivate()

```
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

<details><summary><code>client.e_rezept_workflow_resource.<a href="src/fern/e_rezept_workflow_resource/client.py">get_workflow_comfortsignature_user_id</a>()</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.e_rezept_workflow_resource.get_workflow_comfortsignature_user_id()

```
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

<details><summary><code>client.e_rezept_workflow_resource.<a href="src/fern/e_rezept_workflow_resource/client.py">post_workflow_comfortsignature_user_id</a>()</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.e_rezept_workflow_resource.post_workflow_comfortsignature_user_id()

```
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

<details><summary><code>client.e_rezept_workflow_resource.<a href="src/fern/e_rezept_workflow_resource/client.py">get_workflow_idp_token</a>() -> str</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.e_rezept_workflow_resource.get_workflow_idp_token()

```
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

<details><summary><code>client.e_rezept_workflow_resource.<a href="src/fern/e_rezept_workflow_resource/client.py">post_workflow_sign</a>()</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.e_rezept_workflow_resource.post_workflow_sign()

```
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

<details><summary><code>client.e_rezept_workflow_resource.<a href="src/fern/e_rezept_workflow_resource/client.py">get_workflow_signature_mode</a>() -> GetSignatureModeResponseEvent</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.e_rezept_workflow_resource.get_workflow_signature_mode()

```
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

<details><summary><code>client.e_rezept_workflow_resource.<a href="src/fern/e_rezept_workflow_resource/client.py">post_workflow_task</a>(...)</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.e_rezept_workflow_resource.post_workflow_task()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**flowtype:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.e_rezept_workflow_resource.<a href="src/fern/e_rezept_workflow_resource/client.py">post_workflow_test_prescription</a>()</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.e_rezept_workflow_resource.post_workflow_test_prescription()

```
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

<details><summary><code>client.e_rezept_workflow_resource.<a href="src/fern/e_rezept_workflow_resource/client.py">post_workflow_update</a>(...)</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.e_rezept_workflow_resource.post_workflow_update()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**access_code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**signed_bytes:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## XmlPrescriptionResource
<details><summary><code>client.xml_prescription_resource.<a href="src/fern/xml_prescription_resource/client.py">post_xml_prescription</a>()</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.xml_prescription_resource.post_xml_prescription()

```
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

