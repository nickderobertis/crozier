# Reference
<details><summary><code>client.<a href="src/fern/client.py">get_cancel_job</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation cancels a specified job. Only the job owner can cancel it. The operation fails if the job has already started or is complete.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetCancelJobRequestAction, GetCancelJobRequestVersion, GetCancelJobRequestOperation
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_cancel_job(
    aws_access_key_id="AWSAccessKeyId",
    action=GetCancelJobRequestAction.CANCEL_JOB,
    signature_method="SignatureMethod",
    signature_version="SignatureVersion",
    timestamp="Timestamp",
    version=GetCancelJobRequestVersion.TWO_THOUSAND_TEN0601,
    signature="Signature",
    job_id="JobId",
    operation=GetCancelJobRequestOperation.CANCEL_JOB,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**aws_access_key_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetCancelJobRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**signature_method:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**signature_version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**timestamp:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetCancelJobRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**signature:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**job_id:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**operation:** `GetCancelJobRequestOperation` 
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_cancel_job</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation cancels a specified job. Only the job owner can cancel it. The operation fails if the job has already started or is complete.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostCancelJobRequestAction, PostCancelJobRequestVersion, PostCancelJobRequestOperation
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_cancel_job(
    aws_access_key_id="AWSAccessKeyId",
    action=PostCancelJobRequestAction.CANCEL_JOB,
    signature_method="SignatureMethod",
    signature_version="SignatureVersion",
    timestamp="Timestamp",
    version=PostCancelJobRequestVersion.TWO_THOUSAND_TEN0601,
    signature="Signature",
    operation=PostCancelJobRequestOperation.CANCEL_JOB,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**aws_access_key_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**action:** `PostCancelJobRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**signature_method:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**signature_version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**timestamp:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostCancelJobRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**signature:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**operation:** `PostCancelJobRequestOperation` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_create_job</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation initiates the process of scheduling an upload or download of your data. You include in the request a manifest that describes the data transfer specifics. The response to the request includes a job ID, which you can use in other operations, a signature that you use to identify your storage device, and the address where you should ship your storage device.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetCreateJobRequestAction, GetCreateJobRequestVersion, GetCreateJobRequestJobType, GetCreateJobRequestOperation
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_create_job(
    aws_access_key_id="AWSAccessKeyId",
    action=GetCreateJobRequestAction.CREATE_JOB,
    signature_method="SignatureMethod",
    signature_version="SignatureVersion",
    timestamp="Timestamp",
    version=GetCreateJobRequestVersion.TWO_THOUSAND_TEN0601,
    signature="Signature",
    job_type=GetCreateJobRequestJobType.IMPORT,
    manifest="Manifest",
    validate_only=True,
    operation=GetCreateJobRequestOperation.CREATE_JOB,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**aws_access_key_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetCreateJobRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**signature_method:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**signature_version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**timestamp:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetCreateJobRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**signature:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**job_type:** `GetCreateJobRequestJobType` — 
    
</dd>
</dl>

<dl>
<dd>

**manifest:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**validate_only:** `bool` — 
    
</dd>
</dl>

<dl>
<dd>

**operation:** `GetCreateJobRequestOperation` 
    
</dd>
</dl>

<dl>
<dd>

**manifest_addendum:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_create_job</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation initiates the process of scheduling an upload or download of your data. You include in the request a manifest that describes the data transfer specifics. The response to the request includes a job ID, which you can use in other operations, a signature that you use to identify your storage device, and the address where you should ship your storage device.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostCreateJobRequestAction, PostCreateJobRequestVersion, PostCreateJobRequestOperation
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_create_job(
    aws_access_key_id="AWSAccessKeyId",
    action=PostCreateJobRequestAction.CREATE_JOB,
    signature_method="SignatureMethod",
    signature_version="SignatureVersion",
    timestamp="Timestamp",
    version=PostCreateJobRequestVersion.TWO_THOUSAND_TEN0601,
    signature="Signature",
    operation=PostCreateJobRequestOperation.CREATE_JOB,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**aws_access_key_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**action:** `PostCreateJobRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**signature_method:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**signature_version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**timestamp:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostCreateJobRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**signature:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**operation:** `PostCreateJobRequestOperation` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_get_shipping_label</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation generates a pre-paid UPS shipping label that you will use to ship your device to AWS for processing.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetGetShippingLabelRequestAction, GetGetShippingLabelRequestVersion, GetGetShippingLabelRequestOperation
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_get_shipping_label(
    aws_access_key_id="AWSAccessKeyId",
    action=GetGetShippingLabelRequestAction.GET_SHIPPING_LABEL,
    signature_method="SignatureMethod",
    signature_version="SignatureVersion",
    timestamp="Timestamp",
    version=GetGetShippingLabelRequestVersion.TWO_THOUSAND_TEN0601,
    signature="Signature",
    operation=GetGetShippingLabelRequestOperation.GET_SHIPPING_LABEL,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**aws_access_key_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetGetShippingLabelRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**signature_method:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**signature_version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**timestamp:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetGetShippingLabelRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**signature:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**operation:** `GetGetShippingLabelRequestOperation` 
    
</dd>
</dl>

<dl>
<dd>

**job_ids:** `typing.Optional[typing.Union[GenericString, typing.Sequence[GenericString]]]` — 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**state_or_province:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**city:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**postal_code:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**street1:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**street2:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**street3:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_get_shipping_label</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation generates a pre-paid UPS shipping label that you will use to ship your device to AWS for processing.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostGetShippingLabelRequestAction, PostGetShippingLabelRequestVersion, PostGetShippingLabelRequestOperation
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_get_shipping_label(
    aws_access_key_id="AWSAccessKeyId",
    action=PostGetShippingLabelRequestAction.GET_SHIPPING_LABEL,
    signature_method="SignatureMethod",
    signature_version="SignatureVersion",
    timestamp="Timestamp",
    version=PostGetShippingLabelRequestVersion.TWO_THOUSAND_TEN0601,
    signature="Signature",
    operation=PostGetShippingLabelRequestOperation.GET_SHIPPING_LABEL,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**aws_access_key_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**action:** `PostGetShippingLabelRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**signature_method:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**signature_version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**timestamp:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostGetShippingLabelRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**signature:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**operation:** `PostGetShippingLabelRequestOperation` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_get_status</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation returns information about a job, including where the job is in the processing pipeline, the status of the results, and the signature value associated with the job. You can only return information about jobs you own.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetGetStatusRequestAction, GetGetStatusRequestVersion, GetGetStatusRequestOperation
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_get_status(
    aws_access_key_id="AWSAccessKeyId",
    action=GetGetStatusRequestAction.GET_STATUS,
    signature_method="SignatureMethod",
    signature_version="SignatureVersion",
    timestamp="Timestamp",
    version=GetGetStatusRequestVersion.TWO_THOUSAND_TEN0601,
    signature="Signature",
    job_id="JobId",
    operation=GetGetStatusRequestOperation.GET_STATUS,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**aws_access_key_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetGetStatusRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**signature_method:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**signature_version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**timestamp:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetGetStatusRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**signature:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**job_id:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**operation:** `GetGetStatusRequestOperation` 
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_get_status</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation returns information about a job, including where the job is in the processing pipeline, the status of the results, and the signature value associated with the job. You can only return information about jobs you own.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostGetStatusRequestAction, PostGetStatusRequestVersion, PostGetStatusRequestOperation
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_get_status(
    aws_access_key_id="AWSAccessKeyId",
    action=PostGetStatusRequestAction.GET_STATUS,
    signature_method="SignatureMethod",
    signature_version="SignatureVersion",
    timestamp="Timestamp",
    version=PostGetStatusRequestVersion.TWO_THOUSAND_TEN0601,
    signature="Signature",
    operation=PostGetStatusRequestOperation.GET_STATUS,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**aws_access_key_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**action:** `PostGetStatusRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**signature_method:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**signature_version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**timestamp:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostGetStatusRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**signature:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**operation:** `PostGetStatusRequestOperation` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_list_jobs</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation returns the jobs associated with the requester. AWS Import/Export lists the jobs in reverse chronological order based on the date of creation. For example if Job Test1 was created 2009Dec30 and Test2 was created 2010Feb05, the ListJobs operation would return Test2 followed by Test1.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetListJobsRequestAction, GetListJobsRequestVersion, GetListJobsRequestOperation
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_list_jobs(
    aws_access_key_id="AWSAccessKeyId",
    action=GetListJobsRequestAction.LIST_JOBS,
    signature_method="SignatureMethod",
    signature_version="SignatureVersion",
    timestamp="Timestamp",
    version=GetListJobsRequestVersion.TWO_THOUSAND_TEN0601,
    signature="Signature",
    operation=GetListJobsRequestOperation.LIST_JOBS,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**aws_access_key_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetListJobsRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**signature_method:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**signature_version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**timestamp:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetListJobsRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**signature:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**operation:** `GetListJobsRequestOperation` 
    
</dd>
</dl>

<dl>
<dd>

**max_jobs:** `typing.Optional[int]` — 
    
</dd>
</dl>

<dl>
<dd>

**marker:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_list_jobs</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation returns the jobs associated with the requester. AWS Import/Export lists the jobs in reverse chronological order based on the date of creation. For example if Job Test1 was created 2009Dec30 and Test2 was created 2010Feb05, the ListJobs operation would return Test2 followed by Test1.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostListJobsRequestAction, PostListJobsRequestVersion, PostListJobsRequestOperation
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_list_jobs(
    aws_access_key_id="AWSAccessKeyId",
    action=PostListJobsRequestAction.LIST_JOBS,
    signature_method="SignatureMethod",
    signature_version="SignatureVersion",
    timestamp="Timestamp",
    version=PostListJobsRequestVersion.TWO_THOUSAND_TEN0601,
    signature="Signature",
    operation=PostListJobsRequestOperation.LIST_JOBS,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**aws_access_key_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**action:** `PostListJobsRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**signature_method:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**signature_version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**timestamp:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostListJobsRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**signature:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**operation:** `PostListJobsRequestOperation` 
    
</dd>
</dl>

<dl>
<dd>

**max_jobs:** `typing.Optional[str]` — Pagination limit
    
</dd>
</dl>

<dl>
<dd>

**marker:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_update_job</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You use this operation to change the parameters specified in the original manifest file by supplying a new manifest file. The manifest file attached to this request replaces the original manifest file. You can only use the operation after a CreateJob request but before the data transfer starts and you can only use it on jobs you own.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetUpdateJobRequestAction, GetUpdateJobRequestVersion, GetUpdateJobRequestJobType, GetUpdateJobRequestOperation
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_update_job(
    aws_access_key_id="AWSAccessKeyId",
    action=GetUpdateJobRequestAction.UPDATE_JOB,
    signature_method="SignatureMethod",
    signature_version="SignatureVersion",
    timestamp="Timestamp",
    version=GetUpdateJobRequestVersion.TWO_THOUSAND_TEN0601,
    signature="Signature",
    job_id="JobId",
    manifest="Manifest",
    job_type=GetUpdateJobRequestJobType.IMPORT,
    validate_only=True,
    operation=GetUpdateJobRequestOperation.UPDATE_JOB,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**aws_access_key_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetUpdateJobRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**signature_method:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**signature_version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**timestamp:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetUpdateJobRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**signature:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**job_id:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**manifest:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**job_type:** `GetUpdateJobRequestJobType` — 
    
</dd>
</dl>

<dl>
<dd>

**validate_only:** `bool` — 
    
</dd>
</dl>

<dl>
<dd>

**operation:** `GetUpdateJobRequestOperation` 
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_update_job</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You use this operation to change the parameters specified in the original manifest file by supplying a new manifest file. The manifest file attached to this request replaces the original manifest file. You can only use the operation after a CreateJob request but before the data transfer starts and you can only use it on jobs you own.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostUpdateJobRequestAction, PostUpdateJobRequestVersion, PostUpdateJobRequestOperation
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_update_job(
    aws_access_key_id="AWSAccessKeyId",
    action=PostUpdateJobRequestAction.UPDATE_JOB,
    signature_method="SignatureMethod",
    signature_version="SignatureVersion",
    timestamp="Timestamp",
    version=PostUpdateJobRequestVersion.TWO_THOUSAND_TEN0601,
    signature="Signature",
    operation=PostUpdateJobRequestOperation.UPDATE_JOB,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**aws_access_key_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**action:** `PostUpdateJobRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**signature_method:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**signature_version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**timestamp:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostUpdateJobRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**signature:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**operation:** `PostUpdateJobRequestOperation` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

