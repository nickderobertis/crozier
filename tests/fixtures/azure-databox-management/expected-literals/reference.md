# Reference
## Operations
<details><summary><code>client.operations.<a href="src/fern/operations/client.py">list</a>(...) -> OperationList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This method gets all the operations.
</dd>
</dl>
</dd>
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

client.operations.list(
    api_version="api-version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_version:** `str` — The API Version
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Jobs
<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">list</a>(...) -> JobResourceList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all the jobs available under the subscription.
</dd>
</dl>
</dd>
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

client.jobs.list(
    subscription_id="subscriptionId",
    api_version="api-version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The Subscription Id
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `str` — The API Version
    
</dd>
</dl>

<dl>
<dd>

**skip_token:** `typing.Optional[str]` — $skipToken is supported on Get list of jobs, which provides the next page in the list of jobs.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">listbyresourcegroup</a>(...) -> JobResourceList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all the jobs available under the given resource group.
</dd>
</dl>
</dd>
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

client.jobs.listbyresourcegroup(
    subscription_id="subscriptionId",
    resource_group_name="resourceGroupName",
    api_version="api-version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The Subscription Id
    
</dd>
</dl>

<dl>
<dd>

**resource_group_name:** `str` — The Resource Group Name
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `str` — The API Version
    
</dd>
</dl>

<dl>
<dd>

**skip_token:** `typing.Optional[str]` — $skipToken is supported on Get list of jobs, which provides the next page in the list of jobs.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">get</a>(...) -> JobResource</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets information about the specified job.
</dd>
</dl>
</dd>
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

client.jobs.get(
    subscription_id="subscriptionId",
    resource_group_name="resourceGroupName",
    job_name="jobName",
    api_version="api-version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The Subscription Id
    
</dd>
</dl>

<dl>
<dd>

**resource_group_name:** `str` — The Resource Group Name
    
</dd>
</dl>

<dl>
<dd>

**job_name:** `str` — The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `str` — The API Version
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[str]` — $expand is supported on details parameter for job, which provides details on the job stages.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">create</a>(...) -> JobResource</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new job with the specified parameters. Existing job cannot be updated with this API and should instead be updated with the Update job API.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Sku, JobProperties
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.create(
    subscription_id="subscriptionId",
    resource_group_name="resourceGroupName",
    job_name="jobName",
    api_version="api-version",
    location="location",
    sku=Sku(
        name="DataBox",
    ),
    properties=JobProperties(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The Subscription Id
    
</dd>
</dl>

<dl>
<dd>

**resource_group_name:** `str` — The Resource Group Name
    
</dd>
</dl>

<dl>
<dd>

**job_name:** `str` — The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `str` — The API Version
    
</dd>
</dl>

<dl>
<dd>

**request:** `JobResource` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a job.
</dd>
</dl>
</dd>
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

client.jobs.delete(
    subscription_id="subscriptionId",
    resource_group_name="resourceGroupName",
    job_name="jobName",
    api_version="api-version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The Subscription Id
    
</dd>
</dl>

<dl>
<dd>

**resource_group_name:** `str` — The Resource Group Name
    
</dd>
</dl>

<dl>
<dd>

**job_name:** `str` — The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `str` — The API Version
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">update</a>(...) -> JobResource</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the properties of an existing job.
</dd>
</dl>
</dd>
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

client.jobs.update(
    subscription_id="subscriptionId",
    resource_group_name="resourceGroupName",
    job_name="jobName",
    api_version="api-version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The Subscription Id
    
</dd>
</dl>

<dl>
<dd>

**resource_group_name:** `str` — The Resource Group Name
    
</dd>
</dl>

<dl>
<dd>

**job_name:** `str` — The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `str` — The API Version
    
</dd>
</dl>

<dl>
<dd>

**if_match:** `typing.Optional[str]` — Defines the If-Match condition. The patch will be performed only if the ETag of the job on the server matches this value.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Dict[str, str]]` — The list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups).
    
</dd>
</dl>

<dl>
<dd>

**properties:** `typing.Optional[UpdateJobProperties]` — Properties of a job to be updated.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">bookshipmentpickup</a>(...) -> ShipmentPickUpResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Book shipment pick up.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.bookshipmentpickup(
    subscription_id="subscriptionId",
    resource_group_name="resourceGroupName",
    job_name="jobName",
    api_version="api-version",
    end_time=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    shipment_location="shipmentLocation",
    start_time=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The Subscription Id
    
</dd>
</dl>

<dl>
<dd>

**resource_group_name:** `str` — The Resource Group Name
    
</dd>
</dl>

<dl>
<dd>

**job_name:** `str` — The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `str` — The API Version
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `datetime.datetime` — Maximum date before which the pick up should commence, this must be in local time of pick up area.
    
</dd>
</dl>

<dl>
<dd>

**shipment_location:** `str` — Shipment Location in the pickup place. Eg.front desk
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `datetime.datetime` — Minimum date after which the pick up should commence, this must be in local time of pick up area.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">cancel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

CancelJob.
</dd>
</dl>
</dd>
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

client.jobs.cancel(
    subscription_id="subscriptionId",
    resource_group_name="resourceGroupName",
    job_name="jobName",
    api_version="api-version",
    reason="reason",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The Subscription Id
    
</dd>
</dl>

<dl>
<dd>

**resource_group_name:** `str` — The Resource Group Name
    
</dd>
</dl>

<dl>
<dd>

**job_name:** `str` — The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `str` — The API Version
    
</dd>
</dl>

<dl>
<dd>

**reason:** `str` — Reason for cancellation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">listcredentials</a>(...) -> UnencryptedCredentialsList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This method gets the unencrypted secrets related to the job.
</dd>
</dl>
</dd>
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

client.jobs.listcredentials(
    subscription_id="subscriptionId",
    resource_group_name="resourceGroupName",
    job_name="jobName",
    api_version="api-version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The Subscription Id
    
</dd>
</dl>

<dl>
<dd>

**resource_group_name:** `str` — The Resource Group Name
    
</dd>
</dl>

<dl>
<dd>

**job_name:** `str` — The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `str` — The API Version
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Service
<details><summary><code>client.service.<a href="src/fern/service/client.py">listavailableskus</a>(...) -> AvailableSkusResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This method provides the list of available skus for the given subscription and location.
</dd>
</dl>
</dd>
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

client.service.listavailableskus(
    subscription_id="subscriptionId",
    location_="location",
    api_version="api-version",
    country="country",
    location="location",
    transfer_type="ImportToAzure",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The Subscription Id
    
</dd>
</dl>

<dl>
<dd>

**location:** `str` — The location of the resource
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `str` — The API Version
    
</dd>
</dl>

<dl>
<dd>

**request:** `AvailableSkuRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service.<a href="src/fern/service/client.py">regionconfiguration</a>(...) -> RegionConfigurationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API provides configuration details specific to given region/location.
</dd>
</dl>
</dd>
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

client.service.regionconfiguration(
    subscription_id="subscriptionId",
    location="location",
    api_version="api-version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The Subscription Id
    
</dd>
</dl>

<dl>
<dd>

**location:** `str` — The location of the resource
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `str` — The API Version
    
</dd>
</dl>

<dl>
<dd>

**schedule_availability_request:** `typing.Optional[ScheduleAvailabilityRequest]` — Request body to get the availability for scheduling orders.
    
</dd>
</dl>

<dl>
<dd>

**transport_availability_request:** `typing.Optional[TransportAvailabilityRequest]` — Request body to get the transport availability for given sku.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service.<a href="src/fern/service/client.py">validateaddress</a>(...) -> AddressValidationOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[DEPRECATED NOTICE: This operation will soon be removed] This method validates the customer shipping address and provide alternate addresses if any.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ShippingAddress
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.service.validateaddress(
    subscription_id="subscriptionId",
    location="location",
    api_version="api-version",
    validation_type="ValidateAddress",
    device_type="DataBox",
    shipping_address=ShippingAddress(
        country="country",
        postal_code="postalCode",
        street_address1="streetAddress1",
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

**subscription_id:** `str` — The Subscription Id
    
</dd>
</dl>

<dl>
<dd>

**location:** `str` — The location of the resource
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `str` — The API Version
    
</dd>
</dl>

<dl>
<dd>

**validation_type:** `ValidationInputRequestValidationType` — Identifies the type of validation request.
    
</dd>
</dl>

<dl>
<dd>

**device_type:** `ValidateAddressDeviceType` — Device type to be used for the job.
    
</dd>
</dl>

<dl>
<dd>

**shipping_address:** `ShippingAddress` — Shipping address of the customer.
    
</dd>
</dl>

<dl>
<dd>

**transport_preferences:** `typing.Optional[TransportPreferences]` — Preferences related to the shipment logistics of the sku.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service.<a href="src/fern/service/client.py">validateinputs</a>(...) -> ValidationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This method does all necessary pre-job creation validation under subscription.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ValidationInputRequest
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.service.validateinputs(
    subscription_id="subscriptionId",
    location="location",
    api_version="api-version",
    individual_request_details=[
        ValidationInputRequest(
            validation_type="ValidateAddress",
        )
    ],
    validation_category="JobCreationValidation",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The Subscription Id
    
</dd>
</dl>

<dl>
<dd>

**location:** `str` — The location of the resource
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `str` — The API Version
    
</dd>
</dl>

<dl>
<dd>

**request:** `ValidationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service.<a href="src/fern/service/client.py">listavailableskusbyresourcegroup</a>(...) -> AvailableSkusResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This method provides the list of available skus for the given subscription, resource group and location.
</dd>
</dl>
</dd>
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

client.service.listavailableskusbyresourcegroup(
    subscription_id="subscriptionId",
    resource_group_name="resourceGroupName",
    location_="location",
    api_version="api-version",
    country="country",
    location="location",
    transfer_type="ImportToAzure",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The Subscription Id
    
</dd>
</dl>

<dl>
<dd>

**resource_group_name:** `str` — The Resource Group Name
    
</dd>
</dl>

<dl>
<dd>

**location:** `str` — The location of the resource
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `str` — The API Version
    
</dd>
</dl>

<dl>
<dd>

**request:** `AvailableSkuRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service.<a href="src/fern/service/client.py">validateinputsbyresourcegroup</a>(...) -> ValidationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This method does all necessary pre-job creation validation under resource group.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ValidationInputRequest
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.service.validateinputsbyresourcegroup(
    subscription_id="subscriptionId",
    resource_group_name="resourceGroupName",
    location="location",
    api_version="api-version",
    individual_request_details=[
        ValidationInputRequest(
            validation_type="ValidateAddress",
        )
    ],
    validation_category="JobCreationValidation",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The Subscription Id
    
</dd>
</dl>

<dl>
<dd>

**resource_group_name:** `str` — The Resource Group Name
    
</dd>
</dl>

<dl>
<dd>

**location:** `str` — The location of the resource
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `str` — The API Version
    
</dd>
</dl>

<dl>
<dd>

**request:** `ValidationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

