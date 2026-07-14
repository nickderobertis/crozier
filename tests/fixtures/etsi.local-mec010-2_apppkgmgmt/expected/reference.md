# Reference
## app-pkgm
<details><summary><code>client.app_pkgm.<a href="src/fern/app_pkgm/client.py">app_packages_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

queries information relating to on-boarded application packages in the MEO
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi()
client.app_pkgm.app_packages_get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filter:** `typing.Optional[str]` — Attribute-based filtering parameters according to ETSI GS MEC 009
    
</dd>
</dl>

<dl>
<dd>

**all_fields:** `typing.Optional[str]` — Include all complex attributes in the response.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Complex attributes of AppPkgInfo to be included into the response
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[str]` — Complex attributes of AppPkgInfo to be excluded from the response.
    
</dd>
</dl>

<dl>
<dd>

**exclude_default:** `typing.Optional[str]` — Indicates to exclude the following complex attributes of AppPkgInfo from the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.app_pkgm.<a href="src/fern/app_pkgm/client.py">app_packages_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a resource for on-boarding an application package to a MEO
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import Checksum, FernApi

client = FernApi()
client.app_pkgm.app_packages_post(
    app_pkg_name="appPkgName",
    app_pkg_path="appPkgPath",
    app_pkg_version="appPkgVersion",
    checksum=Checksum(
        algorithm="algorithm",
        hash="hash",
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

**app_pkg_name:** `str` — Name of the application package to be onboarded.
    
</dd>
</dl>

<dl>
<dd>

**app_pkg_path:** `Uri` 
    
</dd>
</dl>

<dl>
<dd>

**app_pkg_version:** `str` 

Version of the application package to be onboarded.
The appPkgName with appPkgVersion can be used to uniquely identify the application package.
    
</dd>
</dl>

<dl>
<dd>

**checksum:** `Checksum` 
    
</dd>
</dl>

<dl>
<dd>

**app_provider:** `typing.Optional[str]` — The provider's name of the application package to be onboarded.
    
</dd>
</dl>

<dl>
<dd>

**user_defined_data:** `typing.Optional[KeyValuePairs]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.app_pkgm.<a href="src/fern/app_pkgm/client.py">app_package_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Queries the information related to individual application package resources
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi()
client.app_pkgm.app_package_get(
    app_pkg_id="appPkgId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_pkg_id:** `str` — Identifier of an individual application package resource
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.app_pkgm.<a href="src/fern/app_pkgm/client.py">app_package_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an individual application package resources
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi()
client.app_pkgm.app_package_delete(
    app_pkg_id="appPkgId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_pkg_id:** `str` — Identifier of an individual application package resource
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.app_pkgm.<a href="src/fern/app_pkgm/client.py">app_package_patch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the operational state of an individual application package resources
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import AppPkgInfoModificationsOperationState, FernApi

client = FernApi()
client.app_pkgm.app_package_patch(
    app_pkg_id="appPkgId",
    operation_state=AppPkgInfoModificationsOperationState.DISABLED,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_pkg_id:** `str` — Identifier of an individual application package resource
    
</dd>
</dl>

<dl>
<dd>

**operation_state:** `AppPkgInfoModificationsOperationState` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.app_pkgm.<a href="src/fern/app_pkgm/client.py">app_pkg_id_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reads the content of the AppD of on-boarded individual application package resources.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi()
client.app_pkgm.app_pkg_id_get(
    app_pkg_id="appPkgId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_pkg_id:** `str` — Identifier of an on-boarded individual application package
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` — Attribute-based filtering parameters according to ETSI GS MEC 009
    
</dd>
</dl>

<dl>
<dd>

**all_fields:** `typing.Optional[str]` — Include all complex attributes in the response.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Complex attributes of AppPkgInfo to be included into the response
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[str]` — Complex attributes of AppPkgInfo to be excluded from the response.
    
</dd>
</dl>

<dl>
<dd>

**exclude_default:** `typing.Optional[str]` — Indicates to exclude the following complex attributes of AppPkgInfo from the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.app_pkgm.<a href="src/fern/app_pkgm/client.py">app_pkg_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch the onboarded application package content identified by appPkgId or appDId.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi()
client.app_pkgm.app_pkg_get(
    app_pkg_id="appPkgId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_pkg_id:** `str` — Identifier of an on-boarded individual application package
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.app_pkgm.<a href="src/fern/app_pkgm/client.py">app_dget</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reads the content of the AppD of on-boarded individual application package resources.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi()
client.app_pkgm.app_dget(
    app_d_id="appDId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_d_id:** `str` — Identifier of an application descriptor
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` — Attribute-based filtering parameters according to ETSI GS MEC 009
    
</dd>
</dl>

<dl>
<dd>

**all_fields:** `typing.Optional[str]` — Include all complex attributes in the response.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Complex attributes of AppPkgInfo to be included into the response
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[str]` — Complex attributes of AppPkgInfo to be excluded from the response.
    
</dd>
</dl>

<dl>
<dd>

**exclude_default:** `typing.Optional[str]` — Indicates to exclude the following complex attributes of AppPkgInfo from the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.app_pkgm.<a href="src/fern/app_pkgm/client.py">app_d_id_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch the onboarded application package content identified by appPkgId or appDId.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi()
client.app_pkgm.app_d_id_get(
    app_d_id="appDId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_d_id:** `str` — Identifier of an application descriptor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.app_pkgm.<a href="src/fern/app_pkgm/client.py">subscriptions_get</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

used to retrieve the information of subscriptions to individual application package resource in MEO package
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi()
client.app_pkgm.subscriptions_get()

```
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

<details><summary><code>client.app_pkgm.<a href="src/fern/app_pkgm/client.py">subscriptions_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Subscribe to notifications about on-boarding an application package
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SubsctiptionTypeAppPkg

client = FernApi()
client.app_pkgm.subscriptions_post(
    callback_uri="callbackUri",
    subsctiption_type=SubsctiptionTypeAppPkg.APP_PACKAGE_ON_BOARDING,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**callback_uri:** `CallbackUri` 
    
</dd>
</dl>

<dl>
<dd>

**subsctiption_type:** `SubsctiptionTypeAppPkg` 
    
</dd>
</dl>

<dl>
<dd>

**app_pkg_filter:** `typing.Optional[typing.Sequence[AppPkgFilter]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.app_pkgm.<a href="src/fern/app_pkgm/client.py">individual_subscription_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to represent an individual subscription to notifications about application package changes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi()
client.app_pkgm.individual_subscription_get(
    subscription_id="subscriptionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — Identifier of an individual subscription to notifications about application package changes
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.app_pkgm.<a href="src/fern/app_pkgm/client.py">individual_subscription_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the individual subscription to notifications about application package changes in MEO.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi()
client.app_pkgm.individual_subscription_delete(
    subscription_id="subscriptionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — Identifier of an individual subscription to notifications about application package changes
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## app-pkgm-notifications
<details><summary><code>client.app_pkgm_notifications.<a href="src/fern/app_pkgm_notifications/client.py">app_pkg_notification_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Registers a notification endpoint to notify application package operations
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern.app_pkgm_notifications import AppPkgNotificationOperationalState

from fern import (
    AppPkgNotificationLinks,
    AppPkgNotificationType,
    FernApi,
    LinkType,
    TimeStamp,
)

client = FernApi()
client.app_pkgm_notifications.app_pkg_notification_post(
    links=AppPkgNotificationLinks(
        subscription=LinkType(
            href="href",
        ),
    ),
    app_d_id="appDId",
    app_pkg_id="appPkgId",
    id="id",
    notification_type=AppPkgNotificationType.APP_PACKAGE_ON_BOARDED,
    operational_state=AppPkgNotificationOperationalState.DISABLED,
    subscription_id="subscriptionId",
    time_stamp=TimeStamp(
        nano_seconds=1,
        seconds=1,
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

**links:** `AppPkgNotificationLinks` 
    
</dd>
</dl>

<dl>
<dd>

**app_d_id:** `AppDId` 
    
</dd>
</dl>

<dl>
<dd>

**app_pkg_id:** `AppPkgId` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `AppPkgNotificationId` 
    
</dd>
</dl>

<dl>
<dd>

**notification_type:** `AppPkgNotificationType` 
    
</dd>
</dl>

<dl>
<dd>

**operational_state:** `AppPkgNotificationOperationalState` 
    
</dd>
</dl>

<dl>
<dd>

**subscription_id:** `SubscriptionId` 
    
</dd>
</dl>

<dl>
<dd>

**time_stamp:** `TimeStamp` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

