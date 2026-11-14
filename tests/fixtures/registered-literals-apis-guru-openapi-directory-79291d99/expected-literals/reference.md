# Reference
## plaid
<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L410-L465">accounts_balance_get</a>(...) -> AccountsGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/accounts/balance/get` endpoint returns the real-time balance for each of an Item's accounts. While other endpoints may return a balance object, only `/accounts/balance/get` forces the available and current balance fields to be refreshed rather than cached. This endpoint can be used for existing Items that were added via any of Plaid’s other products. This endpoint can be used as long as Link has been initialized with any other product, `balance` itself is not a product that can be used to initialize Link. As this endpoint triggers a synchronous request for fresh data, latency may be higher than for other Plaid endpoints; if you encounter errors, you may find it necessary to adjust your timeout period when making requests.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AccountsBalanceGetRequestOptions
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.accounts_balance_get(
    access_token="string",
    client_id="string",
    options=AccountsBalanceGetRequestOptions(
        account_ids=[
            "string"
        ],
    ),
    secret="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[AccountsBalanceGetRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L467-L525">accounts_get</a>(...) -> AccountsGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/accounts/get` endpoint can be used to retrieve a list of accounts associated with any linked Item. Plaid will only return active bank accounts — that is, accounts that are not closed and are capable of carrying a balance.
For items that went through the updated account selection pane, this endpoint only returns accounts that were permissioned by the user when they initially created the Item. If a user creates a new account after the initial link, you can capture this event through the [`NEW_ACCOUNTS_AVAILABLE`](https://plaid.com/docs/api/items/#new_accounts_available) webhook and then use Link's [update mode](https://plaid.com/docs/link/update-mode/) to request that the user share this new account with you.

This endpoint retrieves cached information, rather than extracting fresh information from the institution. As a result, balances returned may not be up-to-date; for realtime balance information, use `/accounts/balance/get` instead. Note that some information is nullable.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AccountsGetRequestOptions
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.accounts_get(
    access_token="string",
    client_id="string",
    options=AccountsGetRequestOptions(
        account_ids=[
            "string"
        ],
    ),
    secret="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[AccountsGetRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L527-L572">application_get</a>(...) -> ApplicationGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Allows financial institutions to retrieve information about Plaid clients for the purpose of building control-tower experiences
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.application_get(
    application_id="application_id",
    client_id="client_id",
    secret="secret",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**application_id:** `ApplicationId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `ApiClientId` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `ApiSecret` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L574-L627">asset_report_audit_copy_create</a>(...) -> AssetReportAuditCopyCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Plaid can provide an Audit Copy of any Asset Report directly to a participating third party on your behalf. For example, Plaid can supply an Audit Copy directly to Fannie Mae on your behalf if you participate in the Day 1 Certainty™ program. An Audit Copy contains the same underlying data as the Asset Report.

To grant access to an Audit Copy, use the `/asset_report/audit_copy/create` endpoint to create an `audit_copy_token` and then pass that token to the third party who needs access. Each third party has its own `auditor_id`, for example `fannie_mae`. You’ll need to create a separate Audit Copy for each third party to whom you want to grant access to the Report.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.asset_report_audit_copy_create(
    asset_report_token="asset_report_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_report_token:** `AssetReportToken` 
    
</dd>
</dl>

<dl>
<dd>

**auditor_id:** `typing.Optional[str]` — The `auditor_id` of the third party with whom you would like to share the Asset Report.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L629-L673">asset_report_audit_copy_get</a>(...) -> AssetReportGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`/asset_report/audit_copy/get` allows auditors to get a copy of an Asset Report that was previously shared via the `/asset_report/audit_copy/create` endpoint.  The caller of `/asset_report/audit_copy/create` must provide the `audit_copy_token` to the auditor.  This token can then be used to call `/asset_report/audit_copy/create`.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.asset_report_audit_copy_get(
    audit_copy_token="audit_copy_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**audit_copy_token:** `str` — The `audit_copy_token` granting access to the Audit Copy you would like to get.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L675-L719">asset_report_audit_copy_remove</a>(...) -> AssetReportAuditCopyRemoveResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/asset_report/audit_copy/remove` endpoint allows you to remove an Audit Copy. Removing an Audit Copy invalidates the `audit_copy_token` associated with it, meaning both you and any third parties holding the token will no longer be able to use it to access Report data. Items associated with the Asset Report, the Asset Report itself and other Audit Copies of it are not affected and will remain accessible after removing the given Audit Copy.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.asset_report_audit_copy_remove(
    audit_copy_token="audit_copy_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**audit_copy_token:** `str` — The `audit_copy_token` granting access to the Audit Copy you would like to revoke.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L721-L788">asset_report_create</a>(...) -> AssetReportCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/asset_report/create` endpoint initiates the process of creating an Asset Report, which can then be retrieved by passing the `asset_report_token` return value to the `/asset_report/get` or `/asset_report/pdf/get` endpoints.

The Asset Report takes some time to be created and is not available immediately after calling `/asset_report/create`. When the Asset Report is ready to be retrieved using `/asset_report/get` or `/asset_report/pdf/get`, Plaid will fire a `PRODUCT_READY` webhook. For full details of the webhook schema, see [Asset Report webhooks](https://plaid.com/docs/api/products/assets/#webhooks).

The `/asset_report/create` endpoint creates an Asset Report at a moment in time. Asset Reports are immutable. To get an updated Asset Report, use the `/asset_report/refresh` endpoint.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.asset_report_create(
    days_requested=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**days_requested:** `int` 

The maximum integer number of days of history to include in the Asset Report. If using Fannie Mae Day 1 Certainty, `days_requested` must be at least 61 for new originations or at least 31 for refinancings.

An Asset Report requested with "Additional History" (that is, with more than 61 days of transaction history) will incur an Additional History fee.
    
</dd>
</dl>

<dl>
<dd>

**access_tokens:** `typing.Optional[typing.List[AccessToken]]` — An array of access tokens corresponding to the Items that will be included in the report. The `assets` product must have been initialized for the Items during link; the Assets product cannot be added after initialization.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[AssetReportCreateRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**user_token:** `typing.Optional[str]` — The user token associated with the User for which to create an asset report for. All items associated with the User will be included in the report.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L790-L848">asset_report_filter</a>(...) -> AssetReportFilterResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

By default, an Asset Report will contain all of the accounts on a given Item. In some cases, you may not want the Asset Report to contain all accounts. For example, you might have the end user choose which accounts are relevant in Link using the Account Select view, which you can enable in the dashboard. Or, you might always exclude certain account types or subtypes, which you can identify by using the `/accounts/get` endpoint. To narrow an Asset Report to only a subset of accounts, use the `/asset_report/filter` endpoint.

To exclude certain Accounts from an Asset Report, first use the `/asset_report/create` endpoint to create the report, then send the `asset_report_token` along with a list of `account_ids` to exclude to the `/asset_report/filter` endpoint, to create a new Asset Report which contains only a subset of the original Asset Report's data.

Because Asset Reports are immutable, calling `/asset_report/filter` does not alter the original Asset Report in any way; rather, `/asset_report/filter` creates a new Asset Report with a new token and id. Asset Reports created via `/asset_report/filter` do not contain new Asset data, and are not billed.

Plaid will fire a [`PRODUCT_READY`](https://plaid.com/docs/api/products/assets/#product_ready) webhook once generation of the filtered Asset Report has completed.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.asset_report_filter(
    account_ids_to_exclude=[
        "account_ids_to_exclude"
    ],
    asset_report_token="asset_report_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_ids_to_exclude:** `typing.List[str]` — The accounts to exclude from the Asset Report, identified by `account_id`.
    
</dd>
</dl>

<dl>
<dd>

**asset_report_token:** `AssetReportToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L850-L916">asset_report_get</a>(...) -> AssetReportGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/asset_report/get` endpoint retrieves the Asset Report in JSON format. Before calling `/asset_report/get`, you must first create the Asset Report using `/asset_report/create` (or filter an Asset Report using `/asset_report/filter`) and then wait for the [`PRODUCT_READY`](https://plaid.com/docs/api/products/assets/#product_ready) webhook to fire, indicating that the Report is ready to be retrieved.

By default, an Asset Report includes transaction descriptions as returned by the bank, as opposed to parsed and categorized by Plaid. You can also receive cleaned and categorized transactions, as well as additional insights like merchant name or location information. We call this an Asset Report with Insights. An Asset Report with Insights provides transaction category, location, and merchant information in addition to the transaction strings provided in a standard Asset Report.

If report_type was set to `VERIFICATION_OF_EMPLOYMENT` when the Asset Report was created in asset_report/create, debit transactions and transaction amounts won’t be included in the report.

To retrieve an Asset Report with Insights, call the `/asset_report/get` endpoint with `include_insights` set to `true`.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.asset_report_get(
    asset_report_token="asset_report_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_report_token:** `AssetReportToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**fast_report:** `typing.Optional[bool]` — `true` to fetch "fast" version of asset report. Defaults to false if omitted. Can only be used if `/asset_report/create` was called with `options.add_ons` set to `["fast_assets"]`.
    
</dd>
</dl>

<dl>
<dd>

**include_insights:** `typing.Optional[bool]` — `true` if you would like to retrieve the Asset Report with Insights, `false` otherwise. This field defaults to `false` if omitted.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[AssetReportGetRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L918-L961">asset_report_pdf_get</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/asset_report/pdf/get` endpoint retrieves the Asset Report in PDF format. Before calling `/asset_report/pdf/get`, you must first create the Asset Report using `/asset_report/create` (or filter an Asset Report using `/asset_report/filter`) and then wait for the [`PRODUCT_READY`](https://plaid.com/docs/api/products/assets/#product_ready) webhook to fire, indicating that the Report is ready to be retrieved.

The response to `/asset_report/pdf/get` is the PDF binary data. The `request_id`  is returned in the `Plaid-Request-ID` header.

If report_type was set to `VERIFICATION_OF_EMPLOYMENT` when the Asset Report was created in asset_report/create, debit transactions and transaction amounts won’t be included in the report.

[View a sample PDF Asset Report](https://plaid.com/documents/sample-asset-report.pdf).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.plaid.asset_report_pdf_get(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_report_token:** `AssetReportToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[AssetReportPdfGetRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L963-L1020">asset_report_refresh</a>(...) -> AssetReportRefreshResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

An Asset Report is an immutable snapshot of a user's assets. In order to "refresh" an Asset Report you created previously, you can use the `/asset_report/refresh` endpoint to create a new Asset Report based on the old one, but with the most recent data available.

The new Asset Report will contain the same Items as the original Report, as well as the same filters applied by any call to `/asset_report/filter`. By default, the new Asset Report will also use the same parameters you submitted with your original `/asset_report/create` request, but the original `days_requested` value and the values of any parameters in the `options` object can be overridden with new values. To change these arguments, simply supply new values for them in your request to `/asset_report/refresh`. Submit an empty string ("") for any previously-populated fields you would like set as empty.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.asset_report_refresh(
    asset_report_token="asset_report_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_report_token:** `AssetReportRefreshAssetReportToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**days_requested:** `typing.Optional[int]` — The maximum number of days of history to include in the Asset Report. Must be an integer. If not specified, the value from the original call to `/asset_report/create` will be used.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[AssetReportRefreshRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L1022-L1067">asset_report_remove</a>(...) -> AssetReportRemoveResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/item/remove` endpoint allows you to invalidate an `access_token`, meaning you will not be able to create new Asset Reports with it. Removing an Item does not affect any Asset Reports or Audit Copies you have already created, which will remain accessible until you remove them specifically.

The `/asset_report/remove` endpoint allows you to remove an Asset Report. Removing an Asset Report invalidates its `asset_report_token`, meaning you will no longer be able to use it to access Report data or create new Audit Copies. Removing an Asset Report does not affect the underlying Items, but does invalidate any `audit_copy_tokens` associated with the Asset Report.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.asset_report_remove(
    asset_report_token="asset_report_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_report_token:** `AssetReportToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L1069-L1123">auth_get</a>(...) -> AuthGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/auth/get` endpoint returns the bank account and bank identification numbers (such as routing numbers, for US accounts) associated with an Item's checking and savings accounts, along with high-level account data and balances when available.

Note: This request may take some time to complete if `auth` was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.

Versioning note: In API version 2017-03-08, the schema of the `numbers` object returned by this endpoint is substantially different. For details, see [Plaid API versioning](https://plaid.com/docs/api/versioning/#version-2018-05-22).
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.auth_get(
    access_token="access_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[AuthGetRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L1125-L1174">bank_transfer_balance_get</a>(...) -> BankTransferBalanceGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/bank_transfer/balance/get` endpoint to see the available balance in your bank transfer account. Debit transfers increase this balance once their status is posted. Credit transfers decrease this balance when they are created.

The transactable balance shows the amount in your account that you are able to use for transfers, and is essentially your available balance minus your minimum balance.

Note that this endpoint can only be used with FBO accounts, when using Bank Transfers in the Full Service configuration. It cannot be used on your own account when using Bank Transfers in the BTS Platform configuration.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.bank_transfer_balance_get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**origination_account_id:** `typing.Optional[str]` — If multiple origination accounts are available, `origination_account_id` must be used to specify the account for which balance will be returned.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L1176-L1219">bank_transfer_cancel</a>(...) -> BankTransferCancelResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/bank_transfer/cancel` endpoint to cancel a bank transfer.  A transfer is eligible for cancelation if the `cancellable` property returned by `/bank_transfer/get` is `true`.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.bank_transfer_cancel(
    bank_transfer_id="bank_transfer_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**bank_transfer_id:** `BankTransferId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L1221-L1330">bank_transfer_create</a>(...) -> BankTransferCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/bank_transfer/create` endpoint to initiate a new bank transfer.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, BankTransferUser
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.bank_transfer_create(
    access_token="access_token",
    account_id="account_id",
    amount="amount",
    description="description",
    idempotency_key="idempotency_key",
    iso_currency_code="iso_currency_code",
    network="ach",
    type="debit",
    user=BankTransferUser(
        legal_name="legal_name",
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

**access_token:** `BankTransferAccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `str` — The Plaid `account_id` for the account that will be debited or credited.
    
</dd>
</dl>

<dl>
<dd>

**amount:** `BankTransferAmount` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — The transfer description. Maximum of 10 characters.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `BankTransferIdempotencyKey` 
    
</dd>
</dl>

<dl>
<dd>

**iso_currency_code:** `str` — The currency of the transfer amount – should be set to "USD".
    
</dd>
</dl>

<dl>
<dd>

**network:** `BankTransferNetwork` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `BankTransferType` 
    
</dd>
</dl>

<dl>
<dd>

**user:** `BankTransferUser` 
    
</dd>
</dl>

<dl>
<dd>

**ach_class:** `typing.Optional[AchClass]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_tag:** `typing.Optional[str]` — An arbitrary string provided by the client for storage with the bank transfer. May be up to 100 characters.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[BankTransferMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**origination_account_id:** `typing.Optional[str]` — Plaid’s unique identifier for the origination account for this transfer. If you have more than one origination account, this value must be specified. Otherwise, this field should be left blank.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L1332-L1420">bank_transfer_event_list</a>(...) -> BankTransferEventListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/bank_transfer/event/list` endpoint to get a list of Plaid-initiated ACH or bank transfer events based on specified filter criteria. When using Auth with micro-deposit verification enabled, this endpoint can be used to fetch status updates on ACH micro-deposits. For more details, see [micro-deposit events](https://plaid.com/docs/auth/coverage/microdeposit-events/).
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.bank_transfer_event_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `typing.Optional[str]` — The account ID to get events for all transactions to/from an account.
    
</dd>
</dl>

<dl>
<dd>

**bank_transfer_id:** `typing.Optional[str]` — Plaid’s unique identifier for a bank transfer.
    
</dd>
</dl>

<dl>
<dd>

**bank_transfer_type:** `typing.Optional[BankTransferEventListBankTransferType]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The maximum number of bank transfer events to return. If the number of events matching the above parameters is greater than `count`, the most recent events will be returned.
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[BankTransferEventListDirection]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` — The end datetime of bank transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)
    
</dd>
</dl>

<dl>
<dd>

**event_types:** `typing.Optional[typing.List[BankTransferEventType]]` — Filter events by event type.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The offset into the list of bank transfer events. When `count`=25 and `offset`=0, the first 25 events will be returned. When `count`=25 and `offset`=25, the next 25 bank transfer events will be returned.
    
</dd>
</dl>

<dl>
<dd>

**origination_account_id:** `typing.Optional[str]` — The origination account ID to get events for transfers from a specific origination account.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` — The start datetime of bank transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L1422-L1470">bank_transfer_event_sync</a>(...) -> BankTransferEventSyncResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`/bank_transfer/event/sync` allows you to request up to the next 25 Plaid-initiated bank transfer events that happened after a specific `event_id`. When using Auth with micro-deposit verification enabled, this endpoint can be used to fetch status updates on ACH micro-deposits. For more details, see [micro-deposit events](https://www.plaid.com/docs/auth/coverage/microdeposit-events/).
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.bank_transfer_event_sync(
    after_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after_id:** `int` — The latest (largest) `event_id` fetched via the sync endpoint, or 0 initially.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The maximum number of bank transfer events to return.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L1472-L1515">bank_transfer_get</a>(...) -> BankTransferGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/bank_transfer/get` fetches information about the bank transfer corresponding to the given `bank_transfer_id`.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.bank_transfer_get(
    bank_transfer_id="bank_transfer_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**bank_transfer_id:** `BankTransferId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L1517-L1586">bank_transfer_list</a>(...) -> BankTransferListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/bank_transfer/list` endpoint to see a list of all your bank transfers and their statuses. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired bank transfers.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.bank_transfer_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The maximum number of bank transfers to return.
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[BankTransferDirection]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` — The end datetime of bank transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of bank transfers to skip before returning results.
    
</dd>
</dl>

<dl>
<dd>

**origination_account_id:** `typing.Optional[str]` — Filter bank transfers to only those originated through the specified origination account.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` — The start datetime of bank transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L1588-L1652">bank_transfer_migrate_account</a>(...) -> BankTransferMigrateAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

As an alternative to adding Items via Link, you can also use the `/bank_transfer/migrate_account` endpoint to migrate known account and routing numbers to Plaid Items.  Note that Items created in this way are not compatible with endpoints for other products, such as `/accounts/balance/get`, and can only be used with Bank Transfer endpoints.  If you require access to other endpoints, create the Item through Link instead.  Access to `/bank_transfer/migrate_account` is not enabled by default; to obtain access, contact your Plaid Account Manager.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.bank_transfer_migrate_account(
    account_number="account_number",
    account_type="account_type",
    routing_number="routing_number",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_number:** `str` — The user's account number.
    
</dd>
</dl>

<dl>
<dd>

**account_type:** `str` — The type of the bank account (`checking` or `savings`).
    
</dd>
</dl>

<dl>
<dd>

**routing_number:** `str` — The user's routing number.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**wire_routing_number:** `typing.Optional[str]` — The user's wire transfer routing number. This is the ABA number; for some institutions, this may differ from the ACH number used in `routing_number`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L1654-L1698">bank_transfer_sweep_get</a>(...) -> BankTransferSweepGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/bank_transfer/sweep/get` endpoint fetches information about the sweep corresponding to the given `sweep_id`.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.bank_transfer_sweep_get(
    sweep_id="sweep_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sweep_id:** `str` — Identifier of the sweep.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L1700-L1760">bank_transfer_sweep_list</a>(...) -> BankTransferSweepListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/bank_transfer/sweep/list` endpoint fetches information about the sweeps matching the given filters.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.bank_transfer_sweep_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The maximum number of sweeps to return.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[datetime.datetime]` — The end datetime of sweeps to return (RFC 3339 format).
    
</dd>
</dl>

<dl>
<dd>

**origination_account_id:** `typing.Optional[str]` — If multiple origination accounts are available, `origination_account_id` must be used to specify the account that the sweeps belong to.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[datetime.datetime]` — The start datetime of sweeps to return (RFC 3339 format).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L1762-L1805">credit_bank_employment_get</a>(...) -> CreditBankEmploymentGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`/credit/bank_employment/get` returns the employment report(s) derived from bank transaction data for a specified user.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.credit_bank_employment_get(
    user_token="user_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_token:** `UserToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L1807-L1876">transactions_rules_create</a>(...) -> TransactionsRulesCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/transactions/rules/v1/create` endpoint creates transaction categorization rules.

Rules will be applied on the Item's transactions returned in `/transactions/get` response.

The product is currently in beta. To request access, contact transactions-feedback@plaid.com.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TransactionsRuleDetails
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transactions_rules_create(
    access_token="access-sandbox-71e02f71-0960-4a27-abd2-5631e04f2175",
    client_id="7f57eb3d2a9j6480121fx361",
    personal_finance_category="FOOD_AND_DRINK_FAST_FOOD",
    rule_details=TransactionsRuleDetails(
        field="NAME",
        query="Burger Shack",
        type="SUBSTRING_MATCH",
    ),
    secret="79g03eoofwl8240v776r2h667442119",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**personal_finance_category:** `str` 

Personal finance detailed category.

See the [`taxonomy csv file`](https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv) for a full list of personal finance categories.
    
</dd>
</dl>

<dl>
<dd>

**rule_details:** `TransactionsRuleDetails` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L1878-L1923">transactions_rules_list</a>(...) -> TransactionsRulesListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/transactions/rules/v1/list` returns a list of transaction rules created for the Item associated with the access token.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transactions_rules_list(
    access_token="access-sandbox-71e02f71-0960-4a27-abd2-5631e04f2175",
    client_id="7f57eb3d2a9j6480121fx361",
    secret="79g03eoofwl8240v776r2h667442119",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L1925-L1979">transactions_rules_remove</a>(...) -> TransactionsRulesRemoveResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/transactions/rules/v1/remove` endpoint is used to remove a transaction rule.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transactions_rules_remove(
    access_token="access-sandbox-71e02f71-0960-4a27-abd2-5631e04f2175",
    client_id="7f57eb3d2a9j6480121fx361",
    rule_id="eVBnVMp7zdTJLkRNr33Rs6zr7KNJqBF",
    secret="79g03eoofwl8240v776r2h667442119",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**rule_id:** `str` — A rule's unique identifier
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L1981-L2043">transactions_enhance</a>(...) -> TransactionsEnhanceGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/beta/transactions/v1/enhance` endpoint enriches raw transaction data provided directly by clients.

The product is currently in beta.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ClientProvidedRawTransaction
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transactions_enhance(
    account_type="account_type",
    transactions=[
        ClientProvidedRawTransaction(
            amount=1.1,
            description="description",
            id="id",
            iso_currency_code="iso_currency_code",
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

**account_type:** `str` — The type of account for the requested transactions (`depository` or `credit`).
    
</dd>
</dl>

<dl>
<dd>

**transactions:** `typing.List[ClientProvidedRawTransaction]` — An array of raw transactions to be enhanced.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L2045-L2077">categories_get</a>(...) -> CategoriesGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send a request to the `/categories/get` endpoint to get detailed information on categories returned by Plaid. This endpoint does not require authentication.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.categories_get(
    request={
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

**request:** `CategoriesGetRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L2079-L2123">credit_asset_report_freddie_mac_get</a>(...) -> AssetReportFreddieGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `credit/asset_report/freddie_mac/get` endpoint retrieves the Asset Report in Freddie Mac's JSON format.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.credit_asset_report_freddie_mac_get(
    audit_copy_token="audit_copy_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**audit_copy_token:** `str` — A token that can be shared with a third party auditor to allow them to obtain access to the Asset Report. This token should be stored securely.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L2125-L2171">credit_audit_copy_token_create</a>(...) -> CreditAuditCopyTokenCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Plaid can create an Audit Copy token of an Asset Report and/or Income Report to share with participating Government Sponsored Entity (GSE). If you participate in the Day 1 Certainty™ program, Plaid can supply an Audit Copy token directly to Fannie Mae on your behalf. An Audit Copy token contains the same underlying data as the Asset Report and/or Income Report (result of /credit/payroll_income/get).

Use the `/credit/audit_copy_token/create` endpoint to create an `audit_copy_token` and then pass that token to the GSE who needs access.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.credit_audit_copy_token_create(
    report_tokens=[
        "report_tokens"
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

**report_tokens:** `typing.List[str]` — List of report tokens; can include at most one VOA/standard Asset Report tokens and one VOE Asset Report Token.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L2173-L2217">credit_report_audit_copy_remove</a>(...) -> CreditAuditCopyTokenRemoveResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/credit/audit_copy_token/remove` endpoint allows you to remove an Audit Copy. Removing an Audit Copy invalidates the `audit_copy_token` associated with it, meaning both you and any third parties holding the token will no longer be able to use it to access Report data. Items associated with the Report data and other Audit Copies of it are not affected and will remain accessible after removing the given Audit Copy.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.credit_report_audit_copy_remove(
    audit_copy_token="audit_copy_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**audit_copy_token:** `str` — The `audit_copy_token` granting access to the Audit Copy you would like to revoke.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L2219-L2272">credit_audit_copy_token_update</a>(...) -> CreditAuditCopyTokenUpdateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/credit/audit_copy_token/update` endpoint updates an existing  Audit Copy Token by adding the report tokens in the `report_tokens` field to the `audit_copy_token`. If the Audit Copy Token already contains a report of a certain type, it will be replaced with the token provided in the `report_tokens` field.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.credit_audit_copy_token_update(
    audit_copy_token="audit_copy_token",
    report_tokens=[
        "report_tokens"
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

**audit_copy_token:** `str` — The `audit_copy_token` you would like to update.
    
</dd>
</dl>

<dl>
<dd>

**report_tokens:** `typing.List[AssetReportToken]` — Array of tokens which the specified Audit Copy Token will be updated with. The types of token supported are asset report token and employment report token. There can be at most 1 of each token type in the array.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L2274-L2318">credit_bank_income_get</a>(...) -> CreditBankIncomeGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`/credit/bank_income/get` returns the bank income report(s) for a specified user.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.credit_bank_income_get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[CreditBankIncomeGetRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**user_token:** `typing.Optional[UserToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L2320-L2350">credit_bank_income_pdf_get</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`/credit/bank_income/pdf/get` returns the most recent bank income report for a specified user in PDF format.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.plaid.credit_bank_income_pdf_get(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_token:** `UserToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L2352-L2398">credit_bank_income_refresh</a>(...) -> CreditBankIncomeRefreshResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`/credit/bank_income/refresh` refreshes the bank income report data for a specific user.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.credit_bank_income_refresh(
    user_token="user_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_token:** `UserToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[CreditBankIncomeRefreshRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L2400-L2443">credit_employment_get</a>(...) -> CreditEmploymentGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`/credit/employment/get` returns a list of items with employment information from a user's payroll provider that was verified by an end user.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.credit_employment_get(
    user_token="user_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_token:** `UserToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L2445-L2489">credit_freddie_mac_reports_get</a>(...) -> CreditFreddieMacReportsGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `credit/asset_report/freddie_mac/get` endpoint retrieves the Verification of Assets and Verification of Employment reports.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.credit_freddie_mac_reports_get(
    audit_copy_token="audit_copy_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**audit_copy_token:** `str` — A token that can be shared with a third party auditor to allow them to obtain access to the Asset Report. This token should be stored securely.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L2491-L2532">credit_payroll_income_get</a>(...) -> CreditPayrollIncomeGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint gets payroll income information for a specific user, either as a result of the user connecting to their payroll provider or uploading a pay related document.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.credit_payroll_income_get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**user_token:** `typing.Optional[UserToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L2534-L2599">credit_payroll_income_precheck</a>(...) -> CreditPayrollIncomePrecheckResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`/credit/payroll_income/precheck` is an optional endpoint that can be called before initializing a Link session for income verification. It evaluates whether a given user is supportable by digital income verification. If the user is eligible for digital verification, that information will be associated with the user token, and in this way will generate a Link UI optimized for the end user and their specific employer. If the user cannot be confirmed as eligible, the user can still use the income verification flow, but they may be required to manually upload a paystub to verify their income.

While all request fields are optional, providing `employer` data will increase the chance of receiving a useful result.

When testing in Sandbox, you can control the results by providing special test values in the `employer` and `access_tokens` fields. `employer_good` and `employer_bad` will result in `HIGH` and `LOW` confidence values, respectively. `employer_multi` will result in a `HIGH` confidence with multiple payroll options. Likewise, `access_good` and `access_bad` will result in `HIGH` and `LOW` confidence values, respectively. Any other value for `employer` and `access_tokens` in Sandbox will result in `UNKNOWN` confidence.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.credit_payroll_income_precheck()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_tokens:** `typing.Optional[typing.List[AccessToken]]` — An array of access tokens corresponding to Items belonging to the user whose eligibility is being checked. Note that if the Items specified here are not already initialized with `transactions`, providing them in this field will cause these Items to be initialized with (and billed for) the Transactions product.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**employer:** `typing.Optional[IncomeVerificationPrecheckEmployer]` 
    
</dd>
</dl>

<dl>
<dd>

**payroll_institution:** `typing.Optional[IncomeVerificationPrecheckPayrollInstitution]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**us_military_info:** `typing.Optional[IncomeVerificationPrecheckMilitaryInfo]` 
    
</dd>
</dl>

<dl>
<dd>

**user_token:** `typing.Optional[UserToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L2601-L2647">credit_payroll_income_refresh</a>(...) -> CreditPayrollIncomeRefreshResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`/credit/payroll_income/refresh` refreshes a given digital payroll income verification.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.credit_payroll_income_refresh(
    user_token="user_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_token:** `UserToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[CreditPayrollIncomeRefreshRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L2649-L2709">credit_relay_create</a>(...) -> CreditRelayCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Plaid can share an Asset Report directly with a participating third party on your behalf. The shared Asset Report is the exact same Asset Report originally created in `/asset_report/create`.

To grant a third party access to an Asset Report, use the `/credit/relay/create` endpoint to create a `relay_token` and then pass that token to your third party. Each third party has its own `secondary_client_id`; for example, `ce5bd328dcd34123456`. You'll need to create a separate `relay_token` for each third party that needs access to the report on your behalf.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.credit_relay_create(
    report_tokens=[
        "report_tokens"
    ],
    secondary_client_id="secondary_client_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**report_tokens:** `typing.List[str]` — List of report token strings, with at most one token of each report type. Currently only Asset Report token is supported.
    
</dd>
</dl>

<dl>
<dd>

**secondary_client_id:** `str` — The `secondary_client_id` is the client id of the third party with whom you would like to share the relay token.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to which Plaid will send webhooks when the Secondary Client successfully retrieves an Asset Report by calling `/credit/relay/get`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L2711-L2763">credit_relay_get</a>(...) -> AssetReportGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`/credit/relay/get` allows third parties to receive a report that was shared with them, using a `relay_token` that was created by the report owner.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.credit_relay_get(
    relay_token="relay_token",
    report_type="assets",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**relay_token:** `str` — The `relay_token` granting access to the report you would like to get.
    
</dd>
</dl>

<dl>
<dd>

**report_type:** `ReportType` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L2765-L2822">credit_relay_refresh</a>(...) -> CreditRelayRefreshResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/credit/relay/refresh` endpoint allows third parties to refresh a report that was relayed to them, using a `relay_token` that was created by the report owner. A new report will be created with the original report parameters, but with the most recent data available based on the `days_requested` value of the original report.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.credit_relay_refresh(
    relay_token="relay_token",
    report_type="assets",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**relay_token:** `str` — The `relay_token` granting access to the report you would like to refresh.
    
</dd>
</dl>

<dl>
<dd>

**report_type:** `ReportType` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — The URL registered to receive webhooks when the report of a relay token has been refreshed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L2824-L2868">credit_relay_remove</a>(...) -> CreditRelayRemoveResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/credit/relay/remove` endpoint allows you to invalidate a `relay_token`. The third party holding the token will no longer be able to access or refresh the reports which the `relay_token` gives access to. The original report, associated Items, and other relay tokens that provide access to the same report are not affected and will remain accessible after removing the given `relay_token`.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.credit_relay_remove(
    relay_token="relay_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**relay_token:** `str` — The `relay_token` you would like to revoke.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L2870-L2915">credit_sessions_get</a>(...) -> CreditSessionsGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint can be used for your end users after they complete the Link flow. This endpoint returns a list of Link sessions that your user completed, where each session includes the results from the Link flow.

These results include details about the Item that was created and some product related metadata (showing, for example, whether the user finished the bank income verification step).
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.credit_sessions_get(
    user_token="user_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_token:** `UserToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L2917-L2960">dashboard_user_get</a>(...) -> DashboardUserGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve information about a dashboard user.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.dashboard_user_get(
    dashboard_user_id="54350110fedcbaf01234ffee",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dashboard_user_id:** `DashboardUserId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L2962-L3003">dashboard_user_list</a>(...) -> DashboardUserListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all dashboard users associated with your account.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.dashboard_user_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[Cursor]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L3005-L3075">deposit_switch_alt_create</a>(...) -> DepositSwitchAltCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint provides an alternative to `/deposit_switch/create` for customers who have not yet fully integrated with Plaid Exchange. Like `/deposit_switch/create`, it creates a deposit switch entity that will be persisted throughout the lifecycle of the switch.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, DepositSwitchTargetAccount, DepositSwitchTargetUser
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.deposit_switch_alt_create(
    target_account=DepositSwitchTargetAccount(
        account_name="account_name",
        account_number="account_number",
        account_subtype="checking",
        routing_number="routing_number",
    ),
    target_user=DepositSwitchTargetUser(
        email="email",
        family_name="family_name",
        given_name="given_name",
        phone="phone",
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

**target_account:** `DepositSwitchTargetAccount` 
    
</dd>
</dl>

<dl>
<dd>

**target_user:** `DepositSwitchTargetUser` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**country_code:** `typing.Optional[DepositSwitchAltCreateRequestCountryCode]` — ISO-3166-1 alpha-2 country code standard.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[DepositSwitchCreateRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L3077-L3139">deposit_switch_create</a>(...) -> DepositSwitchCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint creates a deposit switch entity that will be persisted throughout the lifecycle of the switch.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.deposit_switch_create(
    target_access_token="target_access_token",
    target_account_id="target_account_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**target_access_token:** `str` — Access token for the target Item, typically provided in the Import Item response. 
    
</dd>
</dl>

<dl>
<dd>

**target_account_id:** `str` — Plaid Account ID that specifies the target bank account. This account will become the recipient for a user's direct deposit.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**country_code:** `typing.Optional[DepositSwitchCreateRequestCountryCode]` — ISO-3166-1 alpha-2 country code standard.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[DepositSwitchCreateRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L3141-L3185">deposit_switch_get</a>(...) -> DepositSwitchGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint returns information related to how the user has configured their payroll allocation and the state of the switch. You can use this information to build logic related to the user's direct deposit allocation preferences.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.deposit_switch_get(
    deposit_switch_id="deposit_switch_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**deposit_switch_id:** `str` — The ID of the deposit switch
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L3187-L3231">deposit_switch_token_create</a>(...) -> DepositSwitchTokenCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

In order for the end user to take action, you will need to create a public token representing the deposit switch. This token is used to initialize Link. It can be used one time and expires after 30 minutes.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.deposit_switch_token_create(
    deposit_switch_id="deposit_switch_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**deposit_switch_id:** `str` — The ID of the deposit switch
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L3233-L3284">employers_search</a>(...) -> EmployersSearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`/employers/search` allows you the ability to search Plaid’s database of known employers, for use with Deposit Switch. You can use this endpoint to look up a user's employer in order to confirm that they are supported. Users with non-supported employers can then be routed out of the Deposit Switch flow.

The data in the employer database is currently limited. As the Deposit Switch and Income products progress through their respective beta periods, more employers are being regularly added. Because the employer database is frequently updated, we recommend that you do not cache or store data from this endpoint for more than a day.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.employers_search(
    products=[
        "products"
    ],
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**products:** `typing.List[str]` — The Plaid products the returned employers should support. Currently, this field must be set to `"deposit_switch"`.
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` — The employer name to be searched for.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L3286-L3331">employment_verification_get</a>(...) -> EmploymentVerificationGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`/employment/verification/get` returns a list of employments through a user payroll that was verified by an end user.

This endpoint has been deprecated; new integrations should use `/credit/employment/get` instead.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.employment_verification_get(
    access_token="access_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L3333-L3419">fdx_notifications</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A generic webhook receiver endpoint for FDX Event Notifications
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, FdxNotificationPayload, FdxParty
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    api_key="<value>",
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.fdx_notifications(
    category="SECURITY",
    notification_id="notificationId",
    notification_payload=FdxNotificationPayload(),
    publisher=FdxParty(
        name="name",
        type="DATA_ACCESS_PLATFORM",
    ),
    sent_on=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    type="CONSENT_REVOKED",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**category:** `FdxNotificationCategory` 
    
</dd>
</dl>

<dl>
<dd>

**notification_id:** `str` — Id of notification
    
</dd>
</dl>

<dl>
<dd>

**notification_payload:** `FdxNotificationPayload` 
    
</dd>
</dl>

<dl>
<dd>

**publisher:** `FdxParty` 
    
</dd>
</dl>

<dl>
<dd>

**sent_on:** `FdxTimestamp` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `FdxNotificationType` 
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[FdxNotificationPriority]` 
    
</dd>
</dl>

<dl>
<dd>

**severity:** `typing.Optional[FdxNotificationSeverity]` 
    
</dd>
</dl>

<dl>
<dd>

**subscriber:** `typing.Optional[FdxParty]` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[FdxHateoasLink]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L3421-L3475">identity_get</a>(...) -> IdentityGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/identity/get` endpoint allows you to retrieve various account holder information on file with the financial institution, including names, emails, phone numbers, and addresses. Only name data is guaranteed to be returned; other fields will be empty arrays if not provided by the institution.

This request may take some time to complete if identity was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.

Note: In API versions 2018-05-22 and earlier, the `owners` object is not returned, and instead identity information is returned in the top level `identity` object. For more details, see [Plaid API versioning](https://plaid.com/docs/api/versioning/#version-2019-05-29).
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.identity_get(
    access_token="access_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[IdentityGetRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L3477-L3537">identity_match</a>(...) -> IdentityMatchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/identity/match` endpoint generates a match score, which indicates how well the provided identity data matches the identity information on file with the account holder's financial institution.

This request may take some time to complete if Identity was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.identity_match(
    access_token="access_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**identity_verification_id:** `typing.Optional[IdentityMatchIdentityVerificationId]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[IdentityMatchRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**user:** `typing.Optional[IdentityMatchUser]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L3539-L3608">identity_verification_create</a>(...) -> IdentityVerificationCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new Identity Verification for the user specified by the `client_user_id` field. The requirements and behavior of the verification are determined by the `template_id` provided.
If you don't know whether the associated user already has an active Identity Verification, you can specify `"is_idempotent": true` in the request body. With idempotency enabled, a new Identity Verification will only be created if one does not already exist for the associated `client_user_id` and `template_id`. If an Identity Verification is found, it will be returned unmodified with an `200 OK` HTTP status code.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, IdentityVerificationRequestUser
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.identity_verification_create(
    gave_consent=True,
    is_shareable=True,
    template_id="idvtmp_4FrXJvfQU3zGUR",
    user=IdentityVerificationRequestUser(
        client_user_id="your-db-id-3b24110",
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

**gave_consent:** `IdentityVerificationConsent` 
    
</dd>
</dl>

<dl>
<dd>

**is_shareable:** `bool` — A flag specifying whether you would like Plaid to expose a shareable URL for the verification being created.
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `IdentityVerificationTemplateId` 
    
</dd>
</dl>

<dl>
<dd>

**user:** `IdentityVerificationRequestUser` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**is_idempotent:** `typing.Optional[IdempotencyFlag]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L3610-L3656">identity_verification_get</a>(...) -> IdentityVerificationGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a previously created identity verification.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.identity_verification_get(
    identity_verification_id="idv_52xR9LKo77r1Np",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identity_verification_id:** `IdentityVerificationId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L3658-L3713">identity_verification_list</a>(...) -> IdentityVerificationListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Filter and list Identity Verifications created by your account
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.identity_verification_list(
    client_user_id="your-db-id-3b24110",
    template_id="idvtmp_4FrXJvfQU3zGUR",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_user_id:** `ClientUserId` 
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `IdentityVerificationTemplateId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[Cursor]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L3715-L3775">identity_verification_retry</a>(...) -> IdentityVerificationRetryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Allow a customer to retry their identity verification
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.identity_verification_retry(
    client_user_id="your-db-id-3b24110",
    strategy="reset",
    template_id="idvtmp_4FrXJvfQU3zGUR",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_user_id:** `ClientUserId` 
    
</dd>
</dl>

<dl>
<dd>

**strategy:** `Strategy` 
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `IdentityVerificationTemplateId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**steps:** `typing.Optional[IdentityVerificationRetryRequestStepsObject]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L3777-L3833">income_verification_create</a>(...) -> IncomeVerificationCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`/income/verification/create` begins the income verification process by returning an `income_verification_id`. You can then provide the `income_verification_id` to `/link/token/create` under the `income_verification` parameter in order to create a Link instance that will prompt the user to go through the income verification flow. Plaid will fire an `INCOME` webhook once the user completes the Payroll Income flow, or when the uploaded documents in the Document Income flow have finished processing. 
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.income_verification_create(
    webhook="webhook",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook:** `str` — The URL endpoint to which Plaid should send webhooks related to the progress of the income verification process.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[IncomeVerificationCreateRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**precheck_id:** `typing.Optional[str]` — The ID of a precheck created with `/income/verification/precheck`. Will be used to improve conversion of the income verification flow.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L3835-L3886">income_verification_documents_download</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`/income/verification/documents/download` provides the ability to download the source documents associated with the verification.

If Document Income was used, the documents will be those the user provided in Link. For Payroll Income, the most recent files available
for download from the payroll provider will be available from this endpoint.

The response to `/income/verification/documents/download` is a ZIP file in binary data. If a `document_id` is passed, a single document will be contained in this file.
If not, the response will contain all documents associated with the verification.

The `request_id` is returned in the `Plaid-Request-ID` header.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.plaid.income_verification_documents_download(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `typing.Optional[AccessTokenNullable]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `typing.Optional[str]` — The document ID to download. If passed, a single document will be returned in the resulting zip file, rather than all document
    
</dd>
</dl>

<dl>
<dd>

**income_verification_id:** `typing.Optional[str]` — The ID of the verification.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L3888-L3939">income_verification_paystubs_get</a>(...) -> IncomeVerificationPaystubsGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`/income/verification/paystubs/get` returns the information collected from the paystubs that were used to verify an end user's income. It can be called once the status of the verification has been set to `VERIFICATION_STATUS_PROCESSING_COMPLETE`, as reported by the `INCOME: verification_status` webhook. Attempting to call the endpoint before verification has been completed will result in an error.

This endpoint has been deprecated; new integrations should use `/credit/payroll_income/get` instead.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.income_verification_paystubs_get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `typing.Optional[AccessTokenNullable]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**income_verification_id:** `typing.Optional[str]` — The ID of the verification for which to get paystub information.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L3941-L4010">income_verification_precheck</a>(...) -> IncomeVerificationPrecheckResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`/income/verification/precheck` is an optional endpoint that can be called before initializing a Link session for income verification. It evaluates whether a given user is supportable by digital income verification and returns a `precheck_id` that can be provided to `/link/token/create`. If the user is eligible for digital verification, providing the `precheck_id` in this way will generate a Link UI optimized for the end user and their specific employer. If the user cannot be confirmed as eligible, the `precheck_id` can still be provided to `/link/token/create` and the user can still use the income verification flow, but they may be required to manually upload a paystub to verify their income.

While all request fields are optional, providing either `employer` or `transactions_access_tokens` data will increase the chance of receiving a useful result.

This endpoint has been deprecated; new integrations should use `/credit/payroll_income/precheck` instead.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.income_verification_precheck()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**employer:** `typing.Optional[IncomeVerificationPrecheckEmployer]` 
    
</dd>
</dl>

<dl>
<dd>

**payroll_institution:** `typing.Optional[IncomeVerificationPrecheckPayrollInstitution]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**transactions_access_token:** `typing.Optional[AccessTokenNullable]` 
    
</dd>
</dl>

<dl>
<dd>

**transactions_access_tokens:** `typing.Optional[typing.List[AccessToken]]` — An array of access tokens corresponding to Items belonging to the user whose eligibility is being checked. Note that if the Items specified here are not already initialized with `transactions`, providing them in this field will cause these Items to be initialized with (and billed for) the Transactions product.
    
</dd>
</dl>

<dl>
<dd>

**us_military_info:** `typing.Optional[IncomeVerificationPrecheckMilitaryInfo]` 
    
</dd>
</dl>

<dl>
<dd>

**user:** `typing.Optional[IncomeVerificationPrecheckUser]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L4012-L4063">income_verification_taxforms_get</a>(...) -> IncomeVerificationTaxformsGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`/income/verification/taxforms/get` returns the information collected from forms that were used to verify an end user''s income. It can be called once the status of the verification has been set to `VERIFICATION_STATUS_PROCESSING_COMPLETE`, as reported by the `INCOME: verification_status` webhook. Attempting to call the endpoint before verification has been completed will result in an error.

This endpoint has been deprecated; new integrations should use `/credit/payroll_income/get` instead.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.income_verification_taxforms_get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `typing.Optional[AccessTokenNullable]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**income_verification_id:** `typing.Optional[str]` — The ID of the verification.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L4065-L4132">institutions_get</a>(...) -> InstitutionsGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a JSON response containing details on all financial institutions currently supported by Plaid. Because Plaid supports thousands of institutions, results are paginated.

If there is no overlap between an institution’s enabled products and a client’s enabled products, then the institution will be filtered out from the response. As a result, the number of institutions returned may not match the count specified in the call.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.institutions_get(
    count=1,
    country_codes=[
        "US"
    ],
    offset=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**count:** `int` — The total number of Institutions to return.
    
</dd>
</dl>

<dl>
<dd>

**country_codes:** `typing.List[CountryCode]` 

Specify an array of Plaid-supported country codes this institution supports, using the ISO-3166-1 alpha-2 country code standard.

In API versions 2019-05-29 and earlier, the `country_codes` parameter is an optional parameter within the `options` object and will default to `[US]` if it is not supplied.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `int` — The number of Institutions to skip.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[InstitutionsGetRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L4134-L4193">institutions_get_by_id</a>(...) -> InstitutionsGetByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a JSON response containing details on a specified financial institution currently supported by Plaid.

Versioning note: API versions 2019-05-29 and earlier allow use of the `public_key` parameter instead of the `client_id` and `secret` to authenticate to this endpoint. The `public_key` has been deprecated; all customers are encouraged to use `client_id` and `secret` instead.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.institutions_get_by_id(
    country_codes=[
        "US"
    ],
    institution_id="institution_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**country_codes:** `typing.List[CountryCode]` — Specify an array of Plaid-supported country codes this institution supports, using the ISO-3166-1 alpha-2 country code standard. In API versions 2019-05-29 and earlier, the `country_codes` parameter is an optional parameter within the `options` object and will default to `[US]` if it is not supplied.
    
</dd>
</dl>

<dl>
<dd>

**institution_id:** `str` — The ID of the institution to get details about
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[InstitutionsGetByIdRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L4195-L4259">institutions_search</a>(...) -> InstitutionsSearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a JSON response containing details for institutions that match the query parameters, up to a maximum of ten institutions per query.

Versioning note: API versions 2019-05-29 and earlier allow use of the `public_key` parameter instead of the `client_id` and `secret` parameters to authenticate to this endpoint. The `public_key` parameter has since been deprecated; all customers are encouraged to use `client_id` and `secret` instead.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.institutions_search(
    country_codes=[
        "US"
    ],
    products=None,
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**country_codes:** `typing.List[CountryCode]` — Specify an array of Plaid-supported country codes this institution supports, using the ISO-3166-1 alpha-2 country code standard. In API versions 2019-05-29 and earlier, the `country_codes` parameter is an optional parameter within the `options` object and will default to `[US]` if it is not supplied.
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` — The search query. Institutions with names matching the query are returned
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[InstitutionsSearchRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**products:** `typing.Optional[typing.List[Products]]` — Filter the Institutions based on whether they support all products listed in `products`. Provide `null` to get institutions regardless of supported products. Note that when `auth` is specified as a product, if you are enabled for Instant Match or Automated Micro-deposits, institutions that support those products will be returned even if `auth` is not present in their product array.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L4261-L4311">investments_holdings_get</a>(...) -> InvestmentsHoldingsGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/investments/holdings/get` endpoint allows developers to receive user-authorized stock position data for `investment`-type accounts.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.investments_holdings_get(
    access_token="access_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[InvestmentHoldingsGetRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L4313-L4387">investments_transactions_get</a>(...) -> InvestmentsTransactionsGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/investments/transactions/get` endpoint allows developers to retrieve up to 24 months of user-authorized transaction data for investment accounts.

Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and will not shift.

Due to the potentially large number of investment transactions associated with an Item, results are paginated. Manipulate the count and offset parameters in conjunction with the `total_investment_transactions` response body field to fetch all available investment transactions.

Note that Investments does not have a webhook to indicate when initial transaction data has loaded. Instead, if transactions data is not ready when `/investments/transactions/get` is first called, Plaid will wait for the data. For this reason, calling `/investments/transactions/get` immediately after Link may take up to one to two minutes to return.
</dd>
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
    api_key="<value>",
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.investments_transactions_get(
    access_token="access_token",
    end_date=datetime.date.fromisoformat("2023-01-15"),
    start_date=datetime.date.fromisoformat("2023-01-15"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `datetime.date` — The most recent date for which to fetch transaction history. Dates should be formatted as YYYY-MM-DD.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `datetime.date` — The earliest date for which to fetch transaction history. Dates should be formatted as YYYY-MM-DD.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[InvestmentsTransactionsGetRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L4389-L4434">item_access_token_invalidate</a>(...) -> ItemAccessTokenInvalidateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

By default, the `access_token` associated with an Item does not expire and should be stored in a persistent, secure manner.

You can use the `/item/access_token/invalidate` endpoint to rotate the `access_token` associated with an Item. The endpoint returns a new `access_token` and immediately invalidates the previous `access_token`.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.item_access_token_invalidate(
    access_token="access_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L4436-L4489">item_activity_list</a>(...) -> ItemActivityListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List a historical log of user consent events
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.item_activity_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `typing.Optional[AccessToken]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor used for pagination.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L4491-L4532">item_application_list</a>(...) -> ItemApplicationListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List a user’s connected applications
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.item_application_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `typing.Optional[AccessTokenNullable]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L4534-L4599">item_application_scopes_update</a>(...) -> ItemApplicationScopesUpdateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enable consumers to update product access on selected accounts for an application.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Scopes
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.item_application_scopes_update(
    access_token="access_token",
    application_id="application_id",
    context="ENROLLMENT",
    scopes=Scopes(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**application_id:** `ApplicationId` 
    
</dd>
</dl>

<dl>
<dd>

**context:** `ScopesContext` 
    
</dd>
</dl>

<dl>
<dd>

**scopes:** `Scopes` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[ScopesState]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L4601-L4644">item_get</a>(...) -> ItemGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information about the status of an Item.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.item_get(
    access_token="access_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L4646-L4707">item_import</a>(...) -> ItemImportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`/item/import` creates an Item via your Plaid Exchange Integration and returns an `access_token`. As part of an `/item/import` request, you will include a User ID (`user_auth.user_id`) and Authentication Token (`user_auth.auth_token`) that enable data aggregation through your Plaid Exchange API endpoints. These authentication principals are to be chosen by you.

Upon creating an Item via `/item/import`, Plaid will automatically begin an extraction of that Item through the Plaid Exchange infrastructure you have already integrated. This will automatically generate the Plaid native account ID for the account the user will switch their direct deposit to (`target_account_id`).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ItemImportRequestUserAuth
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.item_import(
    products=[
        "assets"
    ],
    user_auth=ItemImportRequestUserAuth(
        auth_token="auth_token",
        user_id="user_id",
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

**products:** `typing.List[Products]` — Array of product strings
    
</dd>
</dl>

<dl>
<dd>

**user_auth:** `ItemImportRequestUserAuth` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[ItemImportRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L4709-L4758">item_create_public_token</a>(...) -> ItemPublicTokenCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Note: As of July 2020, the `/item/public_token/create` endpoint is deprecated. Instead, use `/link/token/create` with an `access_token` to create a Link token for use with [update mode](https://plaid.com/docs/link/update-mode).

If you need your user to take action to restore or resolve an error associated with an Item, generate a public token with the `/item/public_token/create` endpoint and then initialize Link with that `public_token`.

A `public_token` is one-time use and expires after 30 minutes. You use a `public_token` to initialize Link in [update mode](https://plaid.com/docs/link/update-mode) for a particular Item. You can generate a `public_token` for an Item even if you did not use Link to create the Item originally.

The `/item/public_token/create` endpoint is **not** used to create your initial `public_token`. If you have not already received an `access_token` for a specific Item, use Link to obtain your `public_token` instead. See the [Quickstart](https://plaid.com/docs/quickstart) for more information.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.item_create_public_token(
    access_token="access_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L4760-L4806">item_public_token_exchange</a>(...) -> ItemPublicTokenExchangeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Exchange a Link `public_token` for an API `access_token`. Link hands off the `public_token` client-side via the `onSuccess` callback once a user has successfully created an Item. The `public_token` is ephemeral and expires after 30 minutes. An `access_token` does not expire, but can be revoked by calling `/item/remove`.

The response also includes an `item_id` that should be stored with the `access_token`. The `item_id` is used to identify an Item in a webhook. The `item_id` can also be retrieved by making an `/item/get` request.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.item_public_token_exchange(
    public_token="public_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**public_token:** `str` — Your `public_token`, obtained from the Link `onSuccess` callback or `/sandbox/item/public_token/create`.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L4808-L4857">item_remove</a>(...) -> ItemRemoveResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/item/remove` endpoint allows you to remove an Item. Once removed, the `access_token`, as well as any processor tokens or bank account tokens associated with the Item, is no longer valid and cannot be used to access any data that was associated with the Item.

Note that in the Development environment, issuing an `/item/remove`  request will not decrement your live credential count. To increase your credential account in Development, contact Support.

Also note that for certain OAuth-based institutions, an Item removed via `/item/remove` may still show as an active connection in the institution's OAuth permission manager.

API versions 2019-05-29 and earlier return a `removed` boolean as part of the response.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.item_remove(
    access_token="access_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L4859-L4910">item_webhook_update</a>(...) -> ItemWebhookUpdateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The POST `/item/webhook/update` allows you to update the webhook URL associated with an Item. This request triggers a [`WEBHOOK_UPDATE_ACKNOWLEDGED`](https://plaid.com/docs/api/items/#webhook_update_acknowledged) webhook to the newly specified webhook URL.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.item_webhook_update(
    access_token="access_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — The new webhook URL to associate with the Item. To remove a webhook from an Item, set to `null`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L4912-L4966">liabilities_get</a>(...) -> LiabilitiesGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/liabilities/get` endpoint returns various details about an Item with loan or credit accounts. Liabilities data is available primarily for US financial institutions, with some limited coverage of Canadian institutions. Currently supported account types are account type `credit` with account subtype `credit card` or `paypal`, and account type `loan` with account subtype `student` or `mortgage`. To limit accounts listed in Link to types and subtypes supported by Liabilities, you can use the `account_filters` parameter when [creating a Link token](https://plaid.com/docs/api/tokens/#linktokencreate).

The types of information returned by Liabilities can include balances and due dates, loan terms, and account details such as original loan amount and guarantor. Data is refreshed approximately once per day; the latest data can be retrieved by calling `/liabilities/get`.

Note: This request may take some time to complete if `liabilities` was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the additional data.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.liabilities_get(
    access_token="access_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[LiabilitiesGetRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L4968-L5013">link_oauth_correlation_id_exchange</a>(...) -> LinkOAuthCorrelationIdExchangeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Exchange an OAuth `link_correlation_id` for the corresponding `link_token`. The `link_correlation_id` is only available for 'payment_initiation' products and is provided to the client via the OAuth `redirect_uri` as a query parameter.
The `link_correlation_id` is ephemeral and expires in a brief period, after which it can no longer be exchanged for the 'link_token'.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.link_oauth_correlation_id_exchange(
    link_correlation_id="link_correlation_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**link_correlation_id:** `str` — A `link_correlation_id` from a received OAuth redirect URI callback
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L5015-L5214">link_token_create</a>(...) -> LinkTokenCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/link/token/create` endpoint creates a `link_token`, which is required as a parameter when initializing Link. Once Link has been initialized, it returns a `public_token`, which can then be exchanged for an `access_token` via `/item/public_token/exchange` as part of the main Link flow.

A `link_token` generated by `/link/token/create` is also used to initialize other Link flows, such as the update mode flow for tokens with expired credentials, or the Payment Initiation (Europe) flow.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, LinkTokenCreateRequestUser
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.link_token_create(
    client_name="client_name",
    country_codes=[
        "US"
    ],
    language="language",
    user=LinkTokenCreateRequestUser(
        client_user_id="client_user_id",
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

**client_name:** `str` — The name of your application, as it should be displayed in Link. Maximum length of 30 characters. If a value longer than 30 characters is provided, Link will display "This Application" instead.
    
</dd>
</dl>

<dl>
<dd>

**country_codes:** `typing.List[CountryCode]` 

Specify an array of Plaid-supported country codes using the ISO-3166-1 alpha-2 country code standard. Institutions from all listed countries will be shown. For a complete mapping of supported products by country, see https://plaid.com/global/.

If Link is launched with multiple country codes, only products that you are enabled for in all countries will be used by Link. Note that while all countries are enabled by default in Sandbox and Development, in Production only US and Canada are enabled by default. Access to European institutions requires additional compliance steps. To request access to European institutions in the Production environment, [file a product access Support ticket](https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/request-product-access) via the Plaid dashboard. If you initialize with a European country code, your users will see the European consent panel during the Link flow.

If using a Link customization, make sure the country codes in the customization match those specified in `country_codes`, or the customization may not be applied.

If using the Auth features Instant Match, Same-day Micro-deposits, or Automated Micro-deposits, `country_codes` must be set to `['US']`.
    
</dd>
</dl>

<dl>
<dd>

**language:** `str` 

The language that Link should be displayed in. When initializing with Identity Verification, this field is not used; for more details, see [Identity Verification supported languages](https://www.plaid.com/docs/identity-verification/#supported-languages).

Supported languages are:
- Danish (`'da'`)
- Dutch (`'nl'`)
- English (`'en'`)
- Estonian (`'et'`)
- French (`'fr'`)
- German (`'de'`)
- Italian (`'it'`)
- Latvian (`'lv'`)
- Lithuanian (`'lt'`)
- Norwegian (`'no'`)
- Polish (`'pl'`)
- Portuguese (`'pt'`)
- Romanian (`'ro'`)
- Spanish (`'es'`)
- Swedish (`'se'`)

When using a Link customization, the language configured here must match the setting in the customization, or the customization will not be applied.
    
</dd>
</dl>

<dl>
<dd>

**user:** `LinkTokenCreateRequestUser` 
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — The `access_token` associated with the Item to update or reference, used when updating, modifying, or accessing an existing `access_token`. Used when launching Link in update mode, when completing the Same-day (manual) Micro-deposit flow, or (optionally) when initializing Link for a returning user as part of the Transfer UI flow.
    
</dd>
</dl>

<dl>
<dd>

**account_filters:** `typing.Optional[LinkTokenAccountFilters]` 
    
</dd>
</dl>

<dl>
<dd>

**additional_consented_products:** `typing.Optional[typing.List[Products]]` 

(Beta) This field has no effect unless you are participating in the Product Scope Transparency beta program.
List of additional Plaid product(s) you wish to collect consent for. These products will not be billed until you start using them by calling the relevant endpoints.

`balance` is *not* a valid value, the Balance product does not require explicit initialization and will automatically have consent collected.

Institutions that do not support these products will still be shown in Link
    
</dd>
</dl>

<dl>
<dd>

**android_package_name:** `typing.Optional[str]` — The name of your app's Android package. Required if using the `link_token` to initialize Link on Android. Any package name specified here must also be added to the Allowed Android package names setting on the [developer dashboard](https://dashboard.plaid.com/team/api). When creating a `link_token` for initializing Link on other platforms, `android_package_name` must be left blank and `redirect_uri` should be used instead.
    
</dd>
</dl>

<dl>
<dd>

**auth:** `typing.Optional[LinkTokenCreateRequestAuth]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**deposit_switch:** `typing.Optional[LinkTokenCreateRequestDepositSwitch]` 
    
</dd>
</dl>

<dl>
<dd>

**employment:** `typing.Optional[LinkTokenCreateRequestEmployment]` 
    
</dd>
</dl>

<dl>
<dd>

**eu_config:** `typing.Optional[LinkTokenEuConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**identity_verification:** `typing.Optional[LinkTokenCreateRequestIdentityVerification]` 
    
</dd>
</dl>

<dl>
<dd>

**income_verification:** `typing.Optional[LinkTokenCreateRequestIncomeVerification]` 
    
</dd>
</dl>

<dl>
<dd>

**institution_data:** `typing.Optional[LinkTokenCreateInstitutionData]` 
    
</dd>
</dl>

<dl>
<dd>

**institution_id:** `typing.Optional[str]` — Used for certain Europe-only configurations, as well as certain legacy use cases in other regions.
    
</dd>
</dl>

<dl>
<dd>

**investments:** `typing.Optional[LinkTokenInvestments]` 
    
</dd>
</dl>

<dl>
<dd>

**link_customization_name:** `typing.Optional[str]` — The name of the Link customization from the Plaid Dashboard to be applied to Link. If not specified, the `default` customization will be used. When using a Link customization, the language in the customization must match the language selected via the `language` parameter, and the countries in the customization should match the country codes selected via `country_codes`.
    
</dd>
</dl>

<dl>
<dd>

**payment_initiation:** `typing.Optional[LinkTokenCreateRequestPaymentInitiation]` 
    
</dd>
</dl>

<dl>
<dd>

**products:** `typing.Optional[typing.List[Products]]` 

List of Plaid product(s) you wish to use. If launching Link in update mode, should be omitted (unless you are using update mode to add Income or Assets to an Item); required otherwise.

`balance` is *not* a valid value, the Balance product does not require explicit initialization and will automatically be initialized when any other product is initialized.

The products specified here will determine which institutions will be available to your users in Link. Only institutions that support *all* requested products can be selected; a if a user attempts to select an institution that does not support a listed product, a "Connectivity not supported" error message will appear in Link. To maximize the number of institutions available, initialize Link with the minimal product set required for your use case. Additional products can be added after Link initialization by calling the relevant endpoints. For details and exceptions, see [Choosing when to initialize products](https://plaid.com/docs/link/initializing-products/).

Note that, unless you have opted to disable Instant Match support, institutions that support Instant Match will also be shown in Link if `auth` is specified as a product, even though these institutions do not contain `auth` in their product array.

In Production, you will be billed for each product that you specify when initializing Link. Note that a product cannot be removed from an Item once the Item has been initialized with that product. To stop billing on an Item for subscription-based products, such as Liabilities, Investments, and Transactions, remove the Item via `/item/remove`.
    
</dd>
</dl>

<dl>
<dd>

**redirect_uri:** `typing.Optional[str]` — A URI indicating the destination where a user should be forwarded after completing the Link flow; used to support OAuth authentication flows when launching Link in the browser or via a webview. The `redirect_uri` should not contain any query parameters. When used in Production or Development, must be an https URI. To specify any subdomain, use `*` as a wildcard character, e.g. `https://*.example.com/oauth.html`. Note that any redirect URI must also be added to the Allowed redirect URIs list in the [developer dashboard](https://dashboard.plaid.com/team/api). If initializing on Android, `android_package_name` must be specified instead and `redirect_uri` should be left blank.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**transfer:** `typing.Optional[LinkTokenCreateRequestTransfer]` 
    
</dd>
</dl>

<dl>
<dd>

**update:** `typing.Optional[LinkTokenCreateRequestUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**user_token:** `typing.Optional[str]` — A user token generated using `/user/create`. Any Item created during the Link session will be associated with the user.
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — The destination URL to which any webhooks should be sent. Note that webhooks for Payment Initiation (e-wallet transactions only), Transfer, Bank Transfer (including Auth micro-deposit notification webhooks) and Identity Verification are configured via the Dashboard instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L5216-L5261">link_token_get</a>(...) -> LinkTokenGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/link/token/get` endpoint gets information about a previously-created `link_token` using the
`/link/token/create` endpoint. It can be useful for debugging purposes.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.link_token_get(
    link_token="link_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**link_token:** `str` — A `link_token` from a previous invocation of `/link/token/create`
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L5263-L5310">link_delivery_create</a>(...) -> LinkDeliveryCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/link_delivery/create` endpoint to create a Link Delivery session.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.link_delivery_create(
    link_token="link_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**link_token:** `str` — A `link_token` from a previous invocation of `/link/token/create` with Link Delivery enabled.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[LinkDeliveryOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L5312-L5359">link_delivery_get</a>(...) -> LinkDeliveryGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/link_delivery/get` endpoint to get the status of a Link Delivery session.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.link_delivery_get(
    link_delivery_session_id="link_delivery_session_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**link_delivery_session_id:** `str` — The ID for the Link Delivery session from a previous invocation of `/link_delivery/create`.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L5361-L5516">partner_customer_create</a>(...) -> PartnerCustomerCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/partner/customer/create` endpoint is used by reseller partners to create end customers.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PartnerEndCustomerAddress, PartnerEndCustomerBillingContact, PartnerEndCustomerCustomerSupportInfo, PartnerEndCustomerTechnicalContact
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.partner_customer_create(
    address=PartnerEndCustomerAddress(
        city="New York",
        country_code="US",
        postal_code="12345",
        region="NY",
        street="123 Main St",
    ),
    application_name="Plaid",
    billing_contact=PartnerEndCustomerBillingContact(
        email="bob.jones@example.com",
        family_name="Jones",
        given_name="Bob",
    ),
    client_id="7f57eb3d2a9j6480121fx361",
    company_name="Plaid",
    create_link_customization=True,
    customer_support_info=PartnerEndCustomerCustomerSupportInfo(
        contact_url="example.com/contact",
        email="support@example.com",
        link_update_url="example.com/update",
        phone_number="1234567890",
    ),
    is_bank_addendum_completed=True,
    is_diligence_attested=True,
    legal_entity_name="Plaid",
    products=[
        "auth",
        "identity"
    ],
    redirect_uris=[
        "http://localhost/oauth.html",
        "https://www.example.com/oauth.html",
        "https://*.example.com/oauth.html"
    ],
    secret="79g03eoofwl8240v776r2h667442119",
    technical_contact=PartnerEndCustomerTechnicalContact(
        email="alice.smith@example.com",
        family_name="Smith",
        given_name="Alice",
    ),
    website="plaid.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**address:** `PartnerEndCustomerAddress` 
    
</dd>
</dl>

<dl>
<dd>

**application_name:** `str` — The name of the end customer's application. This will be shown to end users when they go through the Plaid Link flow.
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `str` — The company name of the end customer being created. This will be used to display the end customer in the Plaid Dashboard. It will not be shown to end users.
    
</dd>
</dl>

<dl>
<dd>

**is_bank_addendum_completed:** `bool` — Denotes whether the partner has forwarded the Plaid bank addendum to the end customer.
    
</dd>
</dl>

<dl>
<dd>

**is_diligence_attested:** `bool` — Denotes whether or not the partner has completed attestation of diligence for the end customer to be created.
    
</dd>
</dl>

<dl>
<dd>

**legal_entity_name:** `str` — The end customer's legal name. This will be shared with financial institutions as part of the OAuth registration process. It will not be shown to end users.
    
</dd>
</dl>

<dl>
<dd>

**products:** `typing.List[Products]` — The products to be enabled for the end customer.
    
</dd>
</dl>

<dl>
<dd>

**website:** `str` — The end customer's website.
    
</dd>
</dl>

<dl>
<dd>

**assets_under_management:** `typing.Optional[PartnerEndCustomerAssetsUnderManagement]` 
    
</dd>
</dl>

<dl>
<dd>

**billing_contact:** `typing.Optional[PartnerEndCustomerBillingContact]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**create_link_customization:** `typing.Optional[bool]` — If `true`, the end customer's default Link customization will be set to match the partner's. You can always change the end customer's Link customization in the Plaid Dashboard. See the [Link Customization docs](https://plaid.com/docs/link/customization/) for more information.
    
</dd>
</dl>

<dl>
<dd>

**customer_support_info:** `typing.Optional[PartnerEndCustomerCustomerSupportInfo]` 
    
</dd>
</dl>

<dl>
<dd>

**logo:** `typing.Optional[str]` — Base64-encoded representation of the end customer's logo. Must be a PNG of size 1024x1024 under 4MB. The logo will be shared with financial institutions and shown to the end user during Link flows. A logo is required if `create_link_customization` is `true`. If `create_link_customization` is `false` and the logo is omitted, a stock logo will be used.
    
</dd>
</dl>

<dl>
<dd>

**redirect_uris:** `typing.Optional[typing.List[str]]` — A list of URIs indicating the destination(s) where a user can be forwarded after completing the Link flow; used to support OAuth authentication flows when launching Link in the browser or via a webview. URIs should not contain any query parameters. When used in Production or Development, URIs must use https. To specify any subdomain, use `*` as a wildcard character, e.g. `https://*.example.com/oauth.html`. To modify redirect URIs for an end customer after creating them, go to the end customer's [API page](https://dashboard.plaid.com/team/api) in the Dashboard.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**technical_contact:** `typing.Optional[PartnerEndCustomerTechnicalContact]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L5518-L5566">partner_customer_enable</a>(...) -> PartnerCustomerEnableResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/partner/customer/enable` endpoint is used by reseller partners to enable an end customer in the Production environment.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.partner_customer_enable(
    client_id="7f57eb3d2a9j6480121fx361",
    end_customer_client_id="7f57eb3d2a9j6480121fx361",
    secret="79g03eoofwl8240v776r2h667442119",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**end_customer_client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L5568-L5616">partner_customer_get</a>(...) -> PartnerCustomerGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/partner/customer/get` endpoint is used by reseller partners to retrieve data about a single end customer.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.partner_customer_get(
    client_id="7f57eb3d2a9j6480121fx361",
    end_customer_client_id="7f57eb3d2a9j6480121fx361",
    secret="79g03eoofwl8240v776r2h667442119",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**end_customer_client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L5618-L5666">partner_customer_oauth_institutions_get</a>(...) -> PartnerCustomerOAuthInstitutionsGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/partner/customer/oauth_institutions/get` endpoint is used by reseller partners to retrieve OAuth-institution registration information about a single end customer. To learn how to set up a webhook to listen to status update events, visit the [reseller documentation](https://plaid.com/docs/account/resellers/#enabling-end-customers).
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.partner_customer_oauth_institutions_get(
    client_id="7f57eb3d2a9j6480121fx361",
    end_customer_client_id="7f57eb3d2a9j6480121fx361",
    secret="79g03eoofwl8240v776r2h667442119",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**end_customer_client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L5668-L5716">partner_customer_remove</a>(...) -> PartnerCustomerRemoveResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/partner/customer/remove` endpoint is used by reseller partners to remove an end customer. Removing an end customer will remove it from view in the Plaid Dashboard and deactivate its API keys. This endpoint can only be used to remove an end customer that has not yet been enabled in Production.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.partner_customer_remove(
    client_id="7f57eb3d2a9j6480121fx361",
    end_customer_client_id="7f57eb3d2a9j6480121fx361",
    secret="79g03eoofwl8240v776r2h667442119",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**end_customer_client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L5718-L5808">payment_initiation_consent_create</a>(...) -> PaymentInitiationConsentCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/payment_initiation/consent/create` endpoint is used to create a payment consent, which can be used to initiate payments on behalf of the user. Payment consents are created with `UNAUTHORISED` status by default and must be authorised by the user before payments can be initiated.

Consents can be limited in time and scope, and have constraints that describe limitations for payments.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PaymentInitiationConsentConstraints, PaymentAmount, PaymentConsentPeriodicAmount
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.payment_initiation_consent_create(
    constraints=PaymentInitiationConsentConstraints(
        max_payment_amount=PaymentAmount(
            currency="GBP",
            value=1.1,
        ),
        periodic_amounts=[
            PaymentConsentPeriodicAmount(
                alignment="CALENDAR",
                amount=PaymentAmount(
                    currency="GBP",
                    value=1.1,
                ),
                interval="DAY",
            )
        ],
    ),
    recipient_id="recipient_id",
    reference="reference",
    scopes=[
        "ME_TO_ME"
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

**constraints:** `PaymentInitiationConsentConstraints` 
    
</dd>
</dl>

<dl>
<dd>

**recipient_id:** `str` — The ID of the recipient the payment consent is for. The created consent can be used to transfer funds to this recipient only.
    
</dd>
</dl>

<dl>
<dd>

**reference:** `str` — A reference for the payment consent. This must be an alphanumeric string with at most 18 characters and must not contain any special characters.
    
</dd>
</dl>

<dl>
<dd>

**scopes:** `typing.List[PaymentInitiationConsentScope]` — An array of payment consent scopes.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[ExternalPaymentInitiationConsentOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L5810-L5854">payment_initiation_consent_get</a>(...) -> PaymentInitiationConsentGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/payment_initiation/consent/get` endpoint can be used to check the status of a payment consent, as well as to receive basic information such as recipient and constraints.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.payment_initiation_consent_get(
    consent_id="consent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**consent_id:** `str` — The `consent_id` returned from `/payment_initiation/consent/create`.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L5856-L5916">payment_initiation_consent_payment_execute</a>(...) -> PaymentInitiationConsentPaymentExecuteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/payment_initiation/consent/payment/execute` endpoint can be used to execute payments using payment consent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PaymentAmount
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.payment_initiation_consent_payment_execute(
    amount=PaymentAmount(
        currency="GBP",
        value=1.1,
    ),
    consent_id="consent_id",
    idempotency_key="idempotency_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**amount:** `PaymentAmount` 
    
</dd>
</dl>

<dl>
<dd>

**consent_id:** `str` — The consent ID.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `ConsentPaymentIdempotencyKey` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L5918-L5962">payment_initiation_consent_revoke</a>(...) -> PaymentInitiationConsentRevokeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/payment_initiation/consent/revoke` endpoint can be used to revoke the payment consent. Once the consent is revoked, it is not possible to initiate payments using it.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.payment_initiation_consent_revoke(
    consent_id="consent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**consent_id:** `str` — The consent ID.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L5964-L6039">payment_initiation_payment_create</a>(...) -> PaymentInitiationPaymentCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

After creating a payment recipient, you can use the `/payment_initiation/payment/create` endpoint to create a payment to that recipient.  Payments can be one-time or standing order (recurring) and can be denominated in either EUR, GBP or other chosen [currency](https://plaid.com/docs/api/products/payment-initiation/#payment_initiation-payment-create-request-amount-currency).  If making domestic GBP-denominated payments, your recipient must have been created with BACS numbers. In general, EUR-denominated payments will be sent via SEPA Credit Transfer, GBP-denominated payments will be sent via the Faster Payments network and for non-Eurozone markets typically via the local payment scheme, but the payment network used will be determined by the institution. Payments sent via Faster Payments will typically arrive immediately, while payments sent via SEPA Credit Transfer or other local payment schemes will typically arrive in one business day.

Standing orders (recurring payments) must be denominated in GBP and can only be sent to recipients in the UK. Once created, standing order payments cannot be modified or canceled via the API. An end user can cancel or modify a standing order directly on their banking application or website, or by contacting the bank. Standing orders will follow the payment rules of the underlying rails (Faster Payments in UK). Payments can be sent Monday to Friday, excluding bank holidays. If the pre-arranged date falls on a weekend or bank holiday, the payment is made on the next working day. It is not possible to guarantee the exact time the payment will reach the recipient’s account, although at least 90% of standing order payments are sent by 6am.

In the Development environment, payments must be below 5 GBP or other chosen [currency](https://plaid.com/docs/api/products/payment-initiation/#payment_initiation-payment-create-request-amount-currency). For details on any payment limits in Production, contact your Plaid Account Manager.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PaymentAmount
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.payment_initiation_payment_create(
    amount=PaymentAmount(
        currency="GBP",
        value=1.1,
    ),
    recipient_id="recipient_id",
    reference="reference",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**amount:** `PaymentAmount` 
    
</dd>
</dl>

<dl>
<dd>

**recipient_id:** `str` — The ID of the recipient the payment is for.
    
</dd>
</dl>

<dl>
<dd>

**reference:** `str` 

A reference for the payment. This must be an alphanumeric string with at most 18 characters and must not contain any special characters (since not all institutions support them).
In order to track settlement via Payment Confirmation, each payment must have a unique reference. If the reference provided through the API is not unique, Plaid will adjust it.
Both the originally provided and automatically adjusted references (if any) can be found in the `reference` and `adjusted_reference` fields, respectively.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[ExternalPaymentOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[ExternalPaymentScheduleRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L6041-L6085">payment_initiation_payment_get</a>(...) -> PaymentInitiationPaymentGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/payment_initiation/payment/get` endpoint can be used to check the status of a payment, as well as to receive basic information such as recipient and payment amount. In the case of standing orders, the `/payment_initiation/payment/get` endpoint will provide information about the status of the overall standing order itself; the API cannot be used to retrieve payment status for individual payments within a standing order.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.payment_initiation_payment_get(
    payment_id="payment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_id:** `str` — The `payment_id` returned from `/payment_initiation/payment/create`.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L6087-L6142">payment_initiation_payment_list</a>(...) -> PaymentInitiationPaymentListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/payment_initiation/payment/list` endpoint can be used to retrieve all created payments. By default, the 10 most recent payments are returned. You can request more payments and paginate through the results using the optional `count` and `cursor` parameters.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.payment_initiation_payment_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**consent_id:** `typing.Optional[str]` — The consent ID. If specified, only payments, executed using this consent, will be returned.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The maximum number of payments to return. If `count` is not specified, a maximum of 10 payments will be returned, beginning with the most recent payment before the cursor (if specified).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[datetime.datetime]` — A string in RFC 3339 format (i.e. "2019-12-06T22:35:49Z"). Only payments created before the cursor will be returned.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L6144-L6215">payment_initiation_payment_reverse</a>(...) -> PaymentInitiationPaymentReverseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reverse a settled payment from a Plaid virtual account.

The original payment must be in a settled state to be refunded.
To refund partially, specify the amount as part of the request.
If the amount is not specified, the refund amount will be equal to all
of the remaining payment amount that has not been refunded yet.

The refund will go back to the source account that initiated the payment.
The original payment must have been initiated to a Plaid virtual account
so that this account can be used to initiate the refund.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.payment_initiation_payment_reverse(
    idempotency_key="idempotency_key",
    payment_id="payment_id",
    reference="reference",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `WalletTransactionIdempotencyKey` 
    
</dd>
</dl>

<dl>
<dd>

**payment_id:** `str` — The ID of the payment to reverse
    
</dd>
</dl>

<dl>
<dd>

**reference:** `str` — A reference for the refund. This must be an alphanumeric string with 6 to 18 characters and must not contain any special characters or spaces.
    
</dd>
</dl>

<dl>
<dd>

**amount:** `typing.Optional[PaymentAmountToRefund]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L6217-L6263">create_payment_token</a>(...) -> PaymentInitiationPaymentTokenCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/payment_initiation/payment/token/create` endpoint has been deprecated. New Plaid customers will be unable to use this endpoint, and existing customers are encouraged to migrate to the newer, `link_token`-based flow. The recommended flow is to provide the `payment_id` to `/link/token/create`, which returns a `link_token` used to initialize Link.

The `/payment_initiation/payment/token/create` is used to create a `payment_token`, which can then be used in Link initialization to enter a payment initiation flow. You can only use a `payment_token` once. If this attempt fails, the end user aborts the flow, or the token expires, you will need to create a new payment token. Creating a new payment token does not require end user input.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.create_payment_token(
    payment_id="payment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_id:** `str` — The `payment_id` returned from `/payment_initiation/payment/create`.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L6265-L6329">payment_initiation_recipient_create</a>(...) -> PaymentInitiationRecipientCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a payment recipient for payment initiation.  The recipient must be in Europe, within a country that is a member of the Single Euro Payment Area (SEPA) or a non-Eurozone country [supported](https://plaid.com/global) by Plaid. For a standing order (recurring) payment, the recipient must be in the UK.

It is recommended to use `bacs` in the UK and `iban` in EU.

The endpoint is idempotent: if a developer has already made a request with the same payment details, Plaid will return the same `recipient_id`.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.payment_initiation_recipient_create(
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

**name:** `str` — The name of the recipient. We recommend using strings of length 18 or less and avoid special characters to ensure compatibility with all institutions.
    
</dd>
</dl>

<dl>
<dd>

**address:** `typing.Optional[PaymentInitiationAddress]` 
    
</dd>
</dl>

<dl>
<dd>

**bacs:** `typing.Optional[RecipientBacsNullable]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**iban:** `typing.Optional[str]` — The International Bank Account Number (IBAN) for the recipient. If BACS data is not provided, an IBAN is required.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L6331-L6375">payment_initiation_recipient_get</a>(...) -> PaymentInitiationRecipientGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details about a payment recipient you have previously created.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.payment_initiation_recipient_get(
    recipient_id="recipient_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**recipient_id:** `str` — The ID of the recipient
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L6377-L6415">payment_initiation_recipient_list</a>(...) -> PaymentInitiationRecipientListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/payment_initiation/recipient/list` endpoint list the payment recipients that you have previously created.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.payment_initiation_recipient_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L6417-L6457">payment_profile_create</a>(...) -> PaymentProfileCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use `/payment_profile/create` endpoint to create a new payment profile.
To initiate the account linking experience, call `/link/token/create` and provide the `payment_profile_token` in the `transfer.payment_profile_token` field.
You can then use the `payment_profile_token` when creating transfers using `/transfer/authorization/create` and `/transfer/create`.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.payment_profile_create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L6459-L6505">payment_profile_get</a>(...) -> PaymentProfileGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use `/payment_profile/get` endpoint to get the status of a given Payment Profile.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.payment_profile_get(
    payment_profile_token="payment_profile_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_profile_token:** `PaymentProfileToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L6507-L6553">payment_profile_remove</a>(...) -> PaymentProfileRemoveResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/payment_profile/remove` endpoint to remove a given Payment Profile. Once it’s removed, it can no longer be used to create transfers.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.payment_profile_remove(
    payment_profile_token="payment_profile_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_profile_token:** `PaymentProfileToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L6555-L6607">processor_apex_processor_token_create</a>(...) -> ProcessorTokenCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to create a token suitable for sending to Apex to enable Plaid-Apex integrations.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.processor_apex_processor_token_create(
    access_token="access_token",
    account_id="account_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `str` — The `account_id` value obtained from the `onSuccess` callback in Link
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L6609-L6654">processor_auth_get</a>(...) -> ProcessorAuthGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/processor/auth/get` endpoint returns the bank account and bank identification number (such as the routing number, for US accounts), for a checking or savings account that''s associated with a given `processor_token`. The endpoint also returns high-level account data and balances when available.

Versioning note: API versions 2019-05-29 and earlier use a different schema for the `numbers` object returned by this endpoint. For details, see [Plaid API versioning](https://plaid.com/docs/api/versioning/#version-2020-09-14).
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.processor_auth_get(
    processor_token="processor_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**processor_token:** `ProcessorToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L6656-L6706">processor_balance_get</a>(...) -> ProcessorBalanceGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/processor/balance/get` endpoint returns the real-time balance for each of an Item's accounts. While other endpoints may return a balance object, only `/processor/balance/get` forces the available and current balance fields to be refreshed rather than cached. 
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.processor_balance_get(
    processor_token="processor_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**processor_token:** `ProcessorToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[ProcessorBalanceGetRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L6708-L6811">processor_bank_transfer_create</a>(...) -> ProcessorBankTransferCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/processor/bank_transfer/create` endpoint to initiate a new bank transfer as a processor
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, BankTransferUser
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.processor_bank_transfer_create(
    amount="amount",
    description="description",
    idempotency_key="idempotency_key",
    iso_currency_code="iso_currency_code",
    network="ach",
    processor_token="processor_token",
    type="debit",
    user=BankTransferUser(
        legal_name="legal_name",
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

**amount:** `BankTransferAmount` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — The transfer description. Maximum of 10 characters.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `BankTransferIdempotencyKey` 
    
</dd>
</dl>

<dl>
<dd>

**iso_currency_code:** `str` — The currency of the transfer amount – should be set to "USD".
    
</dd>
</dl>

<dl>
<dd>

**network:** `BankTransferNetwork` 
    
</dd>
</dl>

<dl>
<dd>

**processor_token:** `ProcessorToken` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `BankTransferType` 
    
</dd>
</dl>

<dl>
<dd>

**user:** `BankTransferUser` 
    
</dd>
</dl>

<dl>
<dd>

**ach_class:** `typing.Optional[AchClass]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_tag:** `typing.Optional[str]` — An arbitrary string provided by the client for storage with the bank transfer. May be up to 100 characters.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[BankTransferMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**origination_account_id:** `typing.Optional[str]` — Plaid’s unique identifier for the origination account for this transfer. If you have more than one origination account, this value must be specified.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L6813-L6856">processor_identity_get</a>(...) -> ProcessorIdentityGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/processor/identity/get` endpoint allows you to retrieve various account holder information on file with the financial institution, including names, emails, phone numbers, and addresses.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.processor_identity_get(
    processor_token="processor_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**processor_token:** `ProcessorToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L6858-L6938">processor_signal_decision_report</a>(...) -> ProcessorSignalDecisionReportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

After calling `/processor/signal/evaluate`, call `/processor/signal/decision/report` to report whether the transaction was initiated. This endpoint will return an [`INVALID_FIELD`](/docs/errors/invalid-request/#invalid_field) error if called a second time with a different value for `initiated`.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.processor_signal_decision_report(
    client_transaction_id="client_transaction_id",
    initiated=True,
    processor_token="processor_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_transaction_id:** `str` — Must be the same as the `client_transaction_id` supplied when calling `/signal/evaluate`
    
</dd>
</dl>

<dl>
<dd>

**initiated:** `bool` 

`true` if the ACH transaction was initiated, `false` otherwise.

This field must be returned as a boolean. If formatted incorrectly, this will result in an [`INVALID_FIELD`](/docs/errors/invalid-request/#invalid_field) error.
    
</dd>
</dl>

<dl>
<dd>

**processor_token:** `ProcessorToken` 
    
</dd>
</dl>

<dl>
<dd>

**amount_instantly_available:** `typing.Optional[float]` — The amount (in USD) made available to your customers instantly following the debit transaction. It could be a partial amount of the requested transaction (example: 102.05).
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**days_funds_on_hold:** `typing.Optional[int]` 

The actual number of days (hold time) since the ACH debit transaction that you wait before making funds available to your customers. The holding time could affect the ACH return rate.

For example, use 0 if you make funds available to your customers instantly or the same day following the debit transaction, or 1 if you make funds available the next day following the debit initialization.
    
</dd>
</dl>

<dl>
<dd>

**decision_outcome:** `typing.Optional[SignalDecisionOutcome]` 
    
</dd>
</dl>

<dl>
<dd>

**payment_method:** `typing.Optional[SignalPaymentMethod]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L6940-L7037">processor_signal_evaluate</a>(...) -> ProcessorSignalEvaluateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use `/processor/signal/evaluate` to evaluate a planned ACH transaction as a processor to get a return risk assessment (such as a risk score and risk tier) and additional risk signals.

In order to obtain a valid score for an ACH transaction, Plaid must have an access token for the account, and the Item must be healthy (receiving product updates) or have recently been in a healthy state. If the transaction does not meet eligibility requirements, an error will be returned corresponding to the underlying cause. If `/processor/signal/evaluate` is called on the same transaction multiple times within a 24-hour period, cached results may be returned. For more information please refer to our error documentation on [item errors](/docs/errors/item/) and [Link in Update Mode](/docs/link/update-mode/).

Note: This request may take some time to complete if Signal is being added to an existing Item. This is because Plaid must communicate directly with the institution when retrieving the data for the first time.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.processor_signal_evaluate(
    amount=1.1,
    client_transaction_id="client_transaction_id",
    processor_token="processor_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**amount:** `float` — The transaction amount, in USD (e.g. `102.05`)
    
</dd>
</dl>

<dl>
<dd>

**client_transaction_id:** `str` — The unique ID that you would like to use to refer to this transaction. For your convenience mapping your internal data, you could use your internal ID/identifier for this transaction. The max length for this field is 36 characters.
    
</dd>
</dl>

<dl>
<dd>

**processor_token:** `ProcessorToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**client_user_id:** `typing.Optional[str]` — A unique ID that identifies the end user in your system. This ID is used to correlate requests by a user with multiple Items. The max length for this field is 36 characters. Personally identifiable information, such as an email address or phone number, should not be used in the `client_user_id`.
    
</dd>
</dl>

<dl>
<dd>

**default_payment_method:** `typing.Optional[str]` 

The default ACH or non-ACH payment method to complete the transaction.
`SAME_DAY_ACH`: Same Day ACH by NACHA. The debit transaction is processed and settled on the same day
`NEXT_DAY_ACH`: Next Day ACH settlement for debit transactions, offered by some payment processors
`STANDARD_ACH`: standard ACH by NACHA
`REAL_TIME_PAYMENTS`: real-time payments such as RTP and FedNow
`DEBIT_CARD`: if the default payment is over debit card networks
`MULTIPLE_PAYMENT_METHODS`: if there is no default debit rail or there are multiple payment methods
Possible values:  `SAME_DAY_ACH`, `NEXT_DAY_ACH`, `STANDARD_ACH`, `REAL_TIME_PAYMENTS`, `DEBIT_CARD`, `MULTIPLE_PAYMENT_METHODS`
    
</dd>
</dl>

<dl>
<dd>

**device:** `typing.Optional[SignalDevice]` 
    
</dd>
</dl>

<dl>
<dd>

**is_recurring:** `typing.Optional[bool]` — **true** if the ACH transaction is a recurring transaction; **false** otherwise 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**user:** `typing.Optional[SignalUser]` 
    
</dd>
</dl>

<dl>
<dd>

**user_present:** `typing.Optional[bool]` — `true` if the end user is present while initiating the ACH transfer and the endpoint is being called; `false` otherwise (for example, when the ACH transfer is scheduled and the end user is not present, or you call this endpoint after the ACH transfer but before submitting the Nacha file for ACH processing).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L7039-L7104">processor_signal_return_report</a>(...) -> ProcessorSignalReturnReportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call the `/processor/signal/return/report` endpoint to report a returned transaction that was previously sent to the `/processor/signal/evaluate` endpoint. Your feedback will be used by the model to incorporate the latest risk trend in your portfolio.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.processor_signal_return_report(
    client_transaction_id="client_transaction_id",
    processor_token="processor_token",
    return_code="return_code",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_transaction_id:** `str` — Must be the same as the `client_transaction_id` supplied when calling `/processor/signal/evaluate`
    
</dd>
</dl>

<dl>
<dd>

**processor_token:** `ProcessorToken` 
    
</dd>
</dl>

<dl>
<dd>

**return_code:** `str` 

Must be a valid ACH return code (e.g. "R01")

If formatted incorrectly, this will result in an [`INVALID_FIELD`](/docs/errors/invalid-request/#invalid_field) error.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**returned_at:** `typing.Optional[datetime.datetime]` — Date and time when you receive the returns from your payment processors, in ISO 8601 format (`YYYY-MM-DDTHH:mm:ssZ`).
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L7106-L7163">processor_stripe_bank_account_token_create</a>(...) -> ProcessorStripeBankAccountTokenCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


Used to create a token suitable for sending to Stripe to enable Plaid-Stripe integrations. For a detailed guide on integrating Stripe, see [Add Stripe to your app](https://plaid.com/docs/auth/partnerships/stripe/).

Note that the Stripe bank account token is a one-time use token. To store bank account information for later use, you can use a Stripe customer object and create an associated bank account from the token, or you can use a Stripe Custom account and create an associated external bank account from the token. This bank account information should work indefinitely, unless the user's bank account information changes or they revoke Plaid's permissions to access their account. Stripe bank account information cannot be modified once the bank account token has been created. If you ever need to change the bank account details used by Stripe for a specific customer, have the user go through Link again and create a new bank account token from the new `access_token`.

Bank account tokens can also be revoked, using `/item/remove`.'
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.processor_stripe_bank_account_token_create(
    access_token="access_token",
    account_id="account_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `str` — The `account_id` value obtained from the `onSuccess` callback in Link
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L7165-L7223">processor_token_create</a>(...) -> ProcessorTokenCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to create a token suitable for sending to one of Plaid's partners to enable integrations. Note that Stripe partnerships use bank account tokens instead; see `/processor/stripe/bank_account_token/create` for creating tokens for use with Stripe integrations. Once created, a processor token for a given Item cannot be modified or updated. If the account must be linked to a new or different partner resource, create a new Item by having the user go through the Link flow again; a new processor token can then be created from the new `access_token`. Processor tokens can also be revoked, using `/item/remove`.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.processor_token_create(
    access_token="access_token",
    account_id="account_id",
    processor="dwolla",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `str` — The `account_id` value obtained from the `onSuccess` callback in Link
    
</dd>
</dl>

<dl>
<dd>

**processor:** `ProcessorTokenCreateRequestProcessor` — The processor you are integrating with.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L7225-L7269">sandbox_bank_transfer_fire_webhook</a>(...) -> SandboxBankTransferFireWebhookResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/sandbox/bank_transfer/fire_webhook` endpoint to manually trigger a Bank Transfers webhook in the Sandbox environment.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.sandbox_bank_transfer_fire_webhook(
    webhook="webhook",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook:** `str` — The URL to which the webhook should be sent.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L7271-L7335">sandbox_bank_transfer_simulate</a>(...) -> SandboxBankTransferSimulateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/sandbox/bank_transfer/simulate` endpoint to simulate a bank transfer event in the Sandbox environment.  Note that while an event will be simulated and will appear when using endpoints such as `/bank_transfer/event/sync` or `/bank_transfer/event/list`, no transactions will actually take place and funds will not move between accounts, even within the Sandbox.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.sandbox_bank_transfer_simulate(
    bank_transfer_id="bank_transfer_id",
    event_type="event_type",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**bank_transfer_id:** `BankTransferId` 
    
</dd>
</dl>

<dl>
<dd>

**event_type:** `str` 

The asynchronous event to be simulated. May be: `posted`, `failed`, or `reversed`.

An error will be returned if the event type is incompatible with the current transfer status. Compatible status --> event type transitions include:

`pending` --> `failed`

`pending` --> `posted`

`posted` --> `reversed`
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**failure_reason:** `typing.Optional[BankTransferFailure]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L7337-L7404">sandbox_income_fire_webhook</a>(...) -> SandboxIncomeFireWebhookResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/sandbox/income/fire_webhook` endpoint to manually trigger an Income webhook in the Sandbox environment.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.sandbox_income_fire_webhook(
    item_id="item_id",
    verification_status="VERIFICATION_STATUS_PROCESSING_COMPLETE",
    webhook="webhook",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**item_id:** `str` — The Item ID associated with the verification.
    
</dd>
</dl>

<dl>
<dd>

**verification_status:** `SandboxIncomeFireWebhookRequestVerificationStatus` 

`VERIFICATION_STATUS_PROCESSING_COMPLETE`: The income verification status processing has completed. If the user uploaded multiple documents, this webhook will fire when all documents have finished processing. Call the `/income/verification/paystubs/get` endpoint and check the document metadata to see which documents were successfully parsed.

`VERIFICATION_STATUS_PROCESSING_FAILED`: A failure occurred when attempting to process the verification documentation.

`VERIFICATION_STATUS_PENDING_APPROVAL`: (deprecated) The income verification has been sent to the user for review.
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `str` — The URL to which the webhook should be sent.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[UserId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L7406-L7474">sandbox_item_fire_webhook</a>(...) -> SandboxItemFireWebhookResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/sandbox/item/fire_webhook` endpoint is used to test that code correctly handles webhooks. This endpoint can trigger the following webhooks:

`DEFAULT_UPDATE`: Transactions update webhook to be fired for a given Sandbox Item. If the Item does not support Transactions, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.

`NEW_ACCOUNTS_AVAILABLE`: Webhook to be fired for a given Sandbox Item created with Account Select v2.

`AUTH_DATA_UPDATE`: Webhook to be fired for a given Sandbox Item created with Auth as an enabled product.

`RECURRING_TRANSACTIONS_UPDATE`: Recurring Transactions webhook to be fired for a given Sandbox Item. If the Item does not support Recurring Transactions, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.

`SYNC_UPDATES_AVAILABLE`: Transactions webhook to be fired for a given Sandbox Item.  If the Item does not support Transactions, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.

Note that this endpoint is provided for developer ease-of-use and is not required for testing webhooks; webhooks will also fire in Sandbox under the same conditions that they would in Production or Development.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.sandbox_item_fire_webhook(
    access_token="access_token",
    webhook_code="DEFAULT_UPDATE",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_code:** `SandboxItemFireWebhookRequestWebhookCode` — The webhook codes that can be fired by this test endpoint.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_type:** `typing.Optional[WebhookType]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L7476-L7522">sandbox_item_reset_login</a>(...) -> SandboxItemResetLoginResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`/sandbox/item/reset_login/` forces an Item into an `ITEM_LOGIN_REQUIRED` state in order to simulate an Item whose login is no longer valid. This makes it easy to test Link's [update mode](https://plaid.com/docs/link/update-mode) flow in the Sandbox environment.  After calling `/sandbox/item/reset_login`, You can then use Plaid Link update mode to restore the Item to a good state. An `ITEM_LOGIN_REQUIRED` webhook will also be fired after a call to this endpoint, if one is associated with the Item.


In the Sandbox, Items will transition to an `ITEM_LOGIN_REQUIRED` error state automatically after 30 days, even if this endpoint is not called.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.sandbox_item_reset_login(
    access_token="access_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L7524-L7586">sandbox_item_set_verification_status</a>(...) -> SandboxItemSetVerificationStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/sandbox/item/set_verification_status` endpoint can be used to change the verification status of an Item in in the Sandbox in order to simulate the Automated Micro-deposit flow.

Note that not all Plaid developer accounts are enabled for micro-deposit based verification by default. Your account must be enabled for this feature in order to test it in Sandbox. To enable this features or check your status, contact your account manager or [submit a product access Support ticket](https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/request-product-access).

For more information on testing Automated Micro-deposits in Sandbox, see [Auth full coverage testing](https://plaid.com/docs/auth/coverage/testing#).
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.sandbox_item_set_verification_status(
    access_token="access_token",
    account_id="account_id",
    verification_status="automatically_verified",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `str` — The `account_id` of the account whose verification status is to be modified
    
</dd>
</dl>

<dl>
<dd>

**verification_status:** `SandboxItemSetVerificationStatusRequestVerificationStatus` — The verification status to set the account to.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L7588-L7629">sandbox_oauth_select_accounts</a>(...) -> SandboxOauthSelectAccountsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Save the selected accounts when connecting to the Platypus Oauth institution
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.sandbox_oauth_select_accounts(
    accounts=[
        "accounts"
    ],
    oauth_state_id="oauth_state_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**accounts:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**oauth_state_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L7631-L7681">sandbox_payment_profile_reset_login</a>(...) -> SandboxPaymentProfileResetLoginResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`/sandbox/payment_profile/reset_login/` forces a Payment Profile into a state where the login is no longer valid. This makes it easy to test update mode for Payment Profile in the Sandbox environment.

 After calling `/sandbox/payment_profile/reset_login`, calls to the `/transfer/authorization/create` with the Payment Profile will result in a `decision_rationale` `PAYMENT_PROFILE_LOGIN_REQUIRED`. You can then use update mode for Payment Profile to restore it into a good state.

 In order to invoke this endpoint, you must first [create a Payment Profile](https://plaid.com/docs/transfer/add-to-app/#create-a-payment-profile-optional) and [go through the Link flow](https://plaid.com/docs/transfer/add-to-app/#create-a-link-token).
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.sandbox_payment_profile_reset_login(
    payment_profile_token="payment_profile_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_profile_token:** `PaymentProfileToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L7683-L7734">sandbox_processor_token_create</a>(...) -> SandboxProcessorTokenCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/sandbox/processor_token/create` endpoint to create a valid `processor_token` for an arbitrary institution ID and test credentials. The created `processor_token` corresponds to a new Sandbox Item. You can then use this `processor_token` with the `/processor/` API endpoints in Sandbox. You can also use `/sandbox/processor_token/create` with the [`user_custom` test username](https://plaid.com/docs/sandbox/user-custom) to generate a test account with custom data.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.sandbox_processor_token_create(
    institution_id="institution_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**institution_id:** `str` — The ID of the institution the Item will be associated with
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[SandboxProcessorTokenCreateRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L7736-L7797">sandbox_public_token_create</a>(...) -> SandboxPublicTokenCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/sandbox/public_token/create` endpoint to create a valid `public_token`  for an arbitrary institution ID, initial products, and test credentials. The created `public_token` maps to a new Sandbox Item. You can then call `/item/public_token/exchange` to exchange the `public_token` for an `access_token` and perform all API actions. `/sandbox/public_token/create` can also be used with the [`user_custom` test username](https://plaid.com/docs/sandbox/user-custom) to generate a test account with custom data. `/sandbox/public_token/create` cannot be used with OAuth institutions.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.sandbox_public_token_create(
    initial_products=[
        "assets"
    ],
    institution_id="institution_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**initial_products:** `typing.List[Products]` — The products to initially pull for the Item. May be any products that the specified `institution_id`  supports. This array may not be empty.
    
</dd>
</dl>

<dl>
<dd>

**institution_id:** `str` — The ID of the institution the Item will be associated with
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[SandboxPublicTokenCreateRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**user_token:** `typing.Optional[UserToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L7799-L7843">sandbox_transfer_fire_webhook</a>(...) -> SandboxTransferFireWebhookResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/sandbox/transfer/fire_webhook` endpoint to manually trigger a Transfer webhook in the Sandbox environment.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.sandbox_transfer_fire_webhook(
    webhook="webhook",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook:** `str` — The URL to which the webhook should be sent.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L7845-L7883">sandbox_transfer_repayment_simulate</a>(...) -> SandboxTransferRepaymentSimulateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/sandbox/transfer/repayment/simulate` endpoint to trigger the creation of a repayment. As a side effect of calling this route, a repayment is created that includes all unreimbursed returns of guaranteed transfers. If there are no such returns, an 400 error is returned.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.sandbox_transfer_repayment_simulate()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L7885-L7951">sandbox_transfer_simulate</a>(...) -> SandboxTransferSimulateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/sandbox/transfer/simulate` endpoint to simulate a transfer event in the Sandbox environment.  Note that while an event will be simulated and will appear when using endpoints such as `/transfer/event/sync` or `/transfer/event/list`, no transactions will actually take place and funds will not move between accounts, even within the Sandbox.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.sandbox_transfer_simulate(
    event_type="event_type",
    transfer_id="transfer_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**event_type:** `str` 

The asynchronous event to be simulated. May be: `posted`, `settled`, `failed`, or `returned`.

An error will be returned if the event type is incompatible with the current transfer status. Compatible status --> event type transitions include:

`pending` --> `failed`

`pending` --> `posted`

`posted` --> `returned`

`posted` --> `settled`
    
</dd>
</dl>

<dl>
<dd>

**transfer_id:** `TransferId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**failure_reason:** `typing.Optional[TransferFailure]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L7953-L7991">sandbox_transfer_sweep_simulate</a>(...) -> SandboxTransferSweepSimulateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/sandbox/transfer/sweep/simulate` endpoint to create a sweep and associated events in the Sandbox environment. Upon calling this endpoint, all `posted` or `pending` transfers with a sweep status of `unswept` will become `swept`, and all `returned` transfers with a sweep status of `swept` will become `return_swept`.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.sandbox_transfer_sweep_simulate()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L7993-L8056">sandbox_transfer_test_clock_advance</a>(...) -> SandboxTransferTestClockAdvanceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/sandbox/transfer/test_clock/advance` endpoint to advance a `test_clock` in the Sandbox environment.

A test clock object represents an independent timeline and has a `virtual_time` field indicating the current timestamp of the timeline. A test clock can be advanced by incrementing `virtual_time`, but may never go back to a lower `virtual_time`.

If a test clock is advanced, we will simulate the changes that ought to occur during the time that elapsed.
For instance, a client creates a weekly recurring transfer with a test clock set at t. When the client advances the test clock by setting `virtual_time` = t + 15 days, 2 new originations should be created, along with the webhook events.

The advancement of the test clock from its current `virtual_time` should be limited such that there are no more than 20 originations resulting from the advance operation on each `recurring_transfer` associated with the `test_clock`.
For instance, if the recurring transfer associated with this test clock originates once every 4 weeks, you can advance the `virtual_time` up to 80 weeks on each API call.
</dd>
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
    api_key="<value>",
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.sandbox_transfer_test_clock_advance(
    new_virtual_time=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    test_clock_id="test_clock_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**new_virtual_time:** `VirtualTime` 
    
</dd>
</dl>

<dl>
<dd>

**test_clock_id:** `TransferTestClockId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L8058-L8109">sandbox_transfer_test_clock_create</a>(...) -> SandboxTransferTestClockCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/sandbox/transfer/test_clock/create` endpoint to create a `test_clock` in the Sandbox environment.

A test clock object represents an independent timeline and has a `virtual_time` field indicating the current timestamp of the timeline. Test clocks are used for testing recurring transfers in Sandbox.

A test clock can be associated with up to 5 recurring transfers.
</dd>
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
    api_key="<value>",
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.sandbox_transfer_test_clock_create(
    virtual_time=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**virtual_time:** `VirtualTime` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L8111-L8154">sandbox_transfer_test_clock_get</a>(...) -> SandboxTransferTestClockGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/sandbox/transfer/test_clock/get` endpoint to get a `test_clock` in the Sandbox environment.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.sandbox_transfer_test_clock_get(
    test_clock_id="test_clock_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**test_clock_id:** `TransferTestClockId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L8156-L8216">sandbox_transfer_test_clock_list</a>(...) -> SandboxTransferTestClockListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/sandbox/transfer/test_clock/list` endpoint to see a list of all your test clocks in the Sandbox environment, by ascending `virtual_time`. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired test clocks.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.sandbox_transfer_test_clock_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The maximum number of test clocks to return.
    
</dd>
</dl>

<dl>
<dd>

**end_virtual_time:** `typing.Optional[datetime.datetime]` — The end virtual timestamp of test clocks to return. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of test clocks to skip before returning results.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**start_virtual_time:** `typing.Optional[datetime.datetime]` — The start virtual timestamp of test clocks to return. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L8218-L8293">signal_decision_report</a>(...) -> SignalDecisionReportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

After calling `/signal/evaluate`, call `/signal/decision/report` to report whether the transaction was initiated. This endpoint will return an [`INVALID_FIELD`](/docs/errors/invalid-request/#invalid_field) error if called a second time with a different value for `initiated`.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.signal_decision_report(
    client_transaction_id="client_transaction_id",
    initiated=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_transaction_id:** `str` — Must be the same as the `client_transaction_id` supplied when calling `/signal/evaluate`
    
</dd>
</dl>

<dl>
<dd>

**initiated:** `bool` 

`true` if the ACH transaction was initiated, `false` otherwise.

This field must be returned as a boolean. If formatted incorrectly, this will result in an [`INVALID_FIELD`](/docs/errors/invalid-request/#invalid_field) error.
    
</dd>
</dl>

<dl>
<dd>

**amount_instantly_available:** `typing.Optional[float]` — The amount (in USD) made available to your customers instantly following the debit transaction. It could be a partial amount of the requested transaction (example: 102.05).
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**days_funds_on_hold:** `typing.Optional[int]` 

The actual number of days (hold time) since the ACH debit transaction that you wait before making funds available to your customers. The holding time could affect the ACH return rate.

For example, use 0 if you make funds available to your customers instantly or the same day following the debit transaction, or 1 if you make funds available the next day following the debit initialization.
    
</dd>
</dl>

<dl>
<dd>

**decision_outcome:** `typing.Optional[SignalDecisionOutcome]` 
    
</dd>
</dl>

<dl>
<dd>

**payment_method:** `typing.Optional[SignalPaymentMethod]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L8295-L8400">signal_evaluate</a>(...) -> SignalEvaluateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use `/signal/evaluate` to evaluate a planned ACH transaction to get a return risk assessment (such as a risk score and risk tier) and additional risk signals.

In order to obtain a valid score for an ACH transaction, Plaid must have an access token for the account, and the Item must be healthy (receiving product updates) or have recently been in a healthy state. If the transaction does not meet eligibility requirements, an error will be returned corresponding to the underlying cause. If `/signal/evaluate` is called on the same transaction multiple times within a 24-hour period, cached results may be returned. For more information please refer to the error documentation on [Item errors](/docs/errors/item/) and [Link in Update Mode](/docs/link/update-mode/).

Note: This request may take some time to complete if Signal is being added to an existing Item. This is because Plaid must communicate directly with the institution when retrieving the data for the first time.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.signal_evaluate(
    access_token="access_token",
    account_id="account_id",
    amount=1.1,
    client_transaction_id="client_transaction_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `str` 

The Plaid `account_id` of the account that is the funding source for the proposed transaction. The `account_id` is returned in the `/accounts/get` endpoint as well as the [`onSuccess`](/docs/link/ios/#link-ios-onsuccess-linkSuccess-metadata-accounts-id) callback metadata.

This will return an [`INVALID_ACCOUNT_ID`](/docs/errors/invalid-input/#invalid_account_id) error if the account has been removed at the bank or if the `account_id` is no longer valid.
    
</dd>
</dl>

<dl>
<dd>

**amount:** `float` — The transaction amount, in USD (e.g. `102.05`)
    
</dd>
</dl>

<dl>
<dd>

**client_transaction_id:** `str` — The unique ID that you would like to use to refer to this transaction. For your convenience mapping your internal data, you could use your internal ID/identifier for this transaction. The max length for this field is 36 characters.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**client_user_id:** `typing.Optional[str]` — A unique ID that identifies the end user in your system. This ID is used to correlate requests by a user with multiple Items. The max length for this field is 36 characters. Personally identifiable information, such as an email address or phone number, should not be used in the `client_user_id`.
    
</dd>
</dl>

<dl>
<dd>

**default_payment_method:** `typing.Optional[str]` 

The default ACH or non-ACH payment method to complete the transaction.
`SAME_DAY_ACH`: Same Day ACH by NACHA. The debit transaction is processed and settled on the same day
`NEXT_DAY_ACH`: Next Day ACH settlement for debit transactions, offered by some payment processors
`STANDARD_ACH`: standard ACH by NACHA
`REAL_TIME_PAYMENTS`: real-time payments such as RTP and FedNow
`DEBIT_CARD`: if the default payment is over debit card networks
`MULTIPLE_PAYMENT_METHODS`: if there is no default debit rail or there are multiple payment methods
Possible values:  `SAME_DAY_ACH`, `NEXT_DAY_ACH`, `STANDARD_ACH`, `REAL_TIME_PAYMENTS`, `DEBIT_CARD`, `MULTIPLE_PAYMENT_METHODS`
    
</dd>
</dl>

<dl>
<dd>

**device:** `typing.Optional[SignalDevice]` 
    
</dd>
</dl>

<dl>
<dd>

**is_recurring:** `typing.Optional[bool]` — `true` if the ACH transaction is a recurring transaction; `false` otherwise 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**user:** `typing.Optional[SignalUser]` 
    
</dd>
</dl>

<dl>
<dd>

**user_present:** `typing.Optional[bool]` — `true` if the end user is present while initiating the ACH transfer and the endpoint is being called; `false` otherwise (for example, when the ACH transfer is scheduled and the end user is not present, or you call this endpoint after the ACH transfer but before submitting the Nacha file for ACH processing).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L8402-L8449">signal_prepare</a>(...) -> SignalPrepareResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

When Link is not initialized with Signal, call `/signal/prepare` to opt-in that Item to the Signal data collection process, developing a Signal score.

If you are using other Plaid products after Link, e.g. Identity or Assets, call `/signal/prepare` after those product calls are complete.

Example flow: Link is initialized with Auth, call `/auth/get` for the account and routing number, call `/identity/get` to retrieve bank ownership details, then call `/signal/prepare` to begin Signal data collection. Later, once you have obtained details about the proposed transaction from the user, call `/signal/evaluate` for a Signal score. For more information please see [Recommendations for initializing Link with specific product combinations](https://www.plaid.com/docs/link/initializing-products/#recommendations-for-initializing-link-with-specific-product-combinations).
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.signal_prepare(
    access_token="access_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L8451-L8511">signal_return_report</a>(...) -> SignalReturnReportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call the `/signal/return/report` endpoint to report a returned transaction that was previously sent to the `/signal/evaluate` endpoint. Your feedback will be used by the model to incorporate the latest risk trend in your portfolio.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.signal_return_report(
    client_transaction_id="client_transaction_id",
    return_code="return_code",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_transaction_id:** `str` — Must be the same as the `client_transaction_id` supplied when calling `/signal/evaluate`
    
</dd>
</dl>

<dl>
<dd>

**return_code:** `str` 

Must be a valid ACH return code (e.g. "R01")

If formatted incorrectly, this will result in an [`INVALID_FIELD`](/docs/errors/invalid-request/#invalid_field) error.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**returned_at:** `typing.Optional[datetime.datetime]` — Date and time when you receive the returns from your payment processors, in ISO 8601 format (`YYYY-MM-DDTHH:mm:ssZ`).
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L8513-L8580">transactions_enrich</a>(...) -> TransactionsEnrichGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/transactions/enrich` endpoint enriches raw transaction data generated by your own banking products or retrieved from other non-Plaid sources.

To request access to Enrich, reach out to your Plaid point of contact or send a note to enrich-feedback@plaid.com
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ClientProvidedTransaction
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transactions_enrich(
    account_type="account_type",
    transactions=[
        ClientProvidedTransaction(
            amount=1.1,
            description="description",
            direction="INFLOW",
            id="id",
            iso_currency_code="iso_currency_code",
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

**account_type:** `str` — The account type for the requested transactions (either `depository` or `credit`).
    
</dd>
</dl>

<dl>
<dd>

**transactions:** `typing.List[ClientProvidedTransaction]` — An array of transaction objects to be enriched by Plaid. Maximum of 100 transactions per request.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[TransactionsEnrichRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L8582-L8658">transactions_get</a>(...) -> TransactionsGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/transactions/get` endpoint allows developers to receive user-authorized transaction data for credit, depository, and some loan-type accounts (only those with account subtype `student`; coverage may be limited). For transaction history from investments accounts, use the [Investments endpoint](https://plaid.com/docs/api/products/investments/) instead. Transaction data is standardized across financial institutions, and in many cases transactions are linked to a clean name, entity type, location, and category. Similarly, account data is standardized and returned with a clean name, number, balance, and other meta information where available.

Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and will not shift.  Transactions are not immutable and can also be removed altogether by the institution; a removed transaction will no longer appear in `/transactions/get`.  For more details, see [Pending and posted transactions](https://plaid.com/docs/transactions/transactions-data/#pending-and-posted-transactions).

Due to the potentially large number of transactions associated with an Item, results are paginated. Manipulate the `count` and `offset` parameters in conjunction with the `total_transactions` response body field to fetch all available transactions.

Data returned by `/transactions/get` will be the data available for the Item as of the most recent successful check for new transactions. Plaid typically checks for new data multiple times a day, but these checks may occur less frequently, such as once a day, depending on the institution. An Item's `status.transactions.last_successful_update` field will show the timestamp of the most recent successful update. To force Plaid to check for new transactions, you can use the `/transactions/refresh` endpoint.

Note that data may not be immediately available to `/transactions/get`. Plaid will begin to prepare transactions data upon Item link, if Link was initialized with `transactions`, or upon the first call to `/transactions/get`, if it wasn't. To be alerted when transaction data is ready to be fetched, listen for the [`INITIAL_UPDATE`](https://plaid.com/docs/api/products/transactions/#initial_update) and [`HISTORICAL_UPDATE`](https://plaid.com/docs/api/products/transactions/#historical_update) webhooks. If no transaction history is ready when `/transactions/get` is called, it will return a `PRODUCT_NOT_READY` error.
</dd>
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
    api_key="<value>",
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transactions_get(
    access_token="access_token",
    end_date=datetime.date.fromisoformat("2023-01-15"),
    start_date=datetime.date.fromisoformat("2023-01-15"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `datetime.date` — The latest date for which data should be returned. Dates should be formatted as YYYY-MM-DD.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `datetime.date` — The earliest date for which data should be returned. Dates should be formatted as YYYY-MM-DD.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[TransactionsGetRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L8660-L8724">transactions_recurring_get</a>(...) -> TransactionsRecurringGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/transactions/recurring/get` endpoint allows developers to receive a summary of the recurring outflow and inflow streams (expenses and deposits) from a user’s checking, savings or credit card accounts. Additionally, Plaid provides key insights about each recurring stream including the category, merchant, last amount, and more. Developers can use these insights to build tools and experiences that help their users better manage cash flow, monitor subscriptions, reduce spend, and stay on track with bill payments.

This endpoint is offered as an add-on to Transactions. To request access to this endpoint, submit a [product access request](https://dashboard.plaid.com/team/products) or contact your Plaid account manager.

This endpoint can only be called on an Item that has already been initialized with Transactions (either during Link, by specifying it in `/link/token/create`; or after Link, by calling `/transactions/get` or `/transactions/sync`). Once all historical transactions have been fetched, call `/transactions/recurring/get` to receive the Recurring Transactions streams and subscribe to the [`RECURRING_TRANSACTIONS_UPDATE`](https://plaid.com/docs/api/products/transactions/#recurring_transactions_update) webhook. To know when historical transactions have been fetched, if you are using `/transactions/sync` listen for the [`SYNC_UPDATES_AVAILABLE`](https://plaid.com/docs/api/products/transactions/#SyncUpdatesAvailableWebhook-historical-update-complete) webhook and check that the `historical_update_complete` field in the payload is `true`. If using `/transactions/get`, listen for the [`HISTORICAL_UPDATE`](https://plaid.com/docs/api/products/transactions/#historical_update) webhook.

After the initial call, you can call `/transactions/recurring/get` endpoint at any point in the future to retrieve the latest summary of recurring streams. Listen to the [`RECURRING_TRANSACTIONS_UPDATE`](https://plaid.com/docs/api/products/transactions/#recurring_transactions_update) webhook to be notified when new updates are available.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transactions_recurring_get(
    access_token="access_token",
    account_ids=[
        "account_ids"
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

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**account_ids:** `typing.List[str]` 

A list of `account_ids` to retrieve for the Item

Note: An error will be returned if a provided `account_id` is not associated with the Item.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[TransactionsRecurringGetRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L8726-L8771">transactions_refresh</a>(...) -> TransactionsRefreshResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`/transactions/refresh` is an optional endpoint for users of the Transactions product. It initiates an on-demand extraction to fetch the newest transactions for an Item. This on-demand extraction takes place in addition to the periodic extractions that automatically occur multiple times a day for any Transactions-enabled Item. If changes to transactions are discovered after calling `/transactions/refresh`, Plaid will fire a webhook: for `/transactions/sync` users, [`SYNC_UPDATES_AVAILABLE`](https://plaid.com/docs/api/products/transactions/#sync_updates_available) will be fired if there are any transactions updated, added, or removed. For users of both `/transactions/sync` and `/transactions/get`, [`TRANSACTIONS_REMOVED`](https://plaid.com/docs/api/products/transactions/#transactions_removed) will be fired if any removed transactions are detected, and [`DEFAULT_UPDATE`](https://plaid.com/docs/api/products/transactions/#default_update) will be fired if any new transactions are detected. New transactions can be fetched by calling `/transactions/get` or `/transactions/sync`. Note that the `/transactions/refresh` endpoint is not supported for Capital One (`ins_128026`) and will result in a `PRODUCT_NOT_SUPPORTED` error if called on an Item from that institution.

`/transactions/refresh` is offered as an add-on to Transactions and has a separate [fee model](/docs/account/billing/#per-request-flat-fee). To request access to this endpoint, submit a [product access request](https://dashboard.plaid.com/team/products) or contact your Plaid account manager.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transactions_refresh(
    access_token="access_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L8773-L8853">transactions_sync</a>(...) -> TransactionsSyncResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint replaces `/transactions/get` and its associated webhooks for most common use-cases.

The `/transactions/sync` endpoint allows developers to subscribe to all transactions associated with an Item and get updates synchronously in a stream-like manner, using a cursor to track which updates have already been seen. `/transactions/sync` provides the same functionality as `/transactions/get` and can be used instead of `/transactions/get` to simplify the process of tracking transactions updates.

This endpoint provides user-authorized transaction data for `credit`, `depository`, and some loan-type accounts (only those with account subtype `student`; coverage may be limited). For transaction history from `investments` accounts, use `/investments/transactions/get` instead.

Returned transactions data is grouped into three types of update, indicating whether the transaction was added, removed, or modified since the last call to the API.

In the first call to `/transactions/sync` for an Item, the endpoint will return all historical transactions data associated with that Item up until the time of the API call (as "adds"), which then generates a `next_cursor` for that Item. In subsequent calls, send the `next_cursor` to receive only the changes that have occurred since the previous call.

Due to the potentially large number of transactions associated with an Item, results are paginated. The `has_more` field specifies if additional calls are necessary to fetch all available transaction updates. Call `/transactions/sync` with the new cursor, pulling all updates, until `has_more` is `false`.

When retrieving paginated updates, track both the `next_cursor` from the latest response and the original cursor from the first call in which `has_more` was `true`; if a call to `/transactions/sync` fails when retrieving a paginated update, which can occur as a result of the [`TRANSACTIONS_SYNC_MUTATION_DURING_PAGINATION`](https://plaid.com/docs/errors/transactions/#transactions_sync_mutation_during_pagination) error, the entire pagination request loop must be restarted beginning with the cursor for the first page of the update, rather than retrying only the single request that failed.

Whenever new or updated transaction data becomes available, `/transactions/sync` will provide these updates. Plaid typically checks for new data multiple times a day, but these checks may occur less frequently, such as once a day, depending on the institution. An Item's `status.transactions.last_successful_update` field will show the timestamp of the most recent successful update. To force Plaid to check for new transactions, use the `/transactions/refresh` endpoint.

Note that for newly created Items, data may not be immediately available to `/transactions/sync`. Plaid begins preparing transactions data when the Item is created, but the process can take anywhere from a few seconds to several minutes to complete, depending on the number of transactions available.

To be alerted when new data is available, listen for the [`SYNC_UPDATES_AVAILABLE`](https://plaid.com/docs/api/products/transactions/#sync_updates_available) webhook.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transactions_sync(
    access_token="access_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `AccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of transaction updates to fetch.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

The cursor value represents the last update requested. Providing it will cause the response to only return changes after this update.
If omitted, the entire history of updates will be returned, starting with the first-added transactions on the item.
Note: The upper-bound length of this cursor is 256 characters of base64.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[TransactionsSyncRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L8855-L8992">transfer_authorization_create</a>(...) -> TransferAuthorizationCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/transfer/authorization/create` endpoint to determine transfer failure risk.

In Plaid's Sandbox environment the decisions will be returned as follows:

  - To approve a transfer with null rationale code, make an authorization request with an `amount` less than the available balance in the account.

  - To approve a transfer with the rationale code `MANUALLY_VERIFIED_ITEM`, create an Item in Link through the [Same Day Micro-deposits flow](https://plaid.com/docs/auth/coverage/testing/#testing-same-day-micro-deposits).

  - To approve a transfer with the rationale code `ITEM_LOGIN_REQUIRED`, [reset the login for an Item](https://plaid.com/docs/sandbox/#item_login_required).

  - To decline a transfer with the rationale code `NSF`, the available balance on the account must be less than the authorization `amount`. See [Create Sandbox test data](https://plaid.com/docs/sandbox/user-custom/) for details on how to customize data in Sandbox.

  - To decline a transfer with the rationale code `RISK`, the available balance on the account must be exactly $0. See [Create Sandbox test data](https://plaid.com/docs/sandbox/user-custom/) for details on how to customize data in Sandbox.

`device.ip_address`, `device.user_agent` are required fields.

For [Guarantee](https://www.plaid.com/docs//transfer/guarantee/), the following fields are required : `idempotency_key`, `user.phone_number` (optional if `email_address` provided), `user.email_address` (optional if `phone_number` provided), `device.ip_address`, `device.user_agent`, and `user_present`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TransferAuthorizationUserInRequest
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_authorization_create(
    amount="amount",
    network="ach",
    type="debit",
    user=TransferAuthorizationUserInRequest(
        legal_name="legal_name",
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

**amount:** `TransferAmount` 
    
</dd>
</dl>

<dl>
<dd>

**network:** `TransferNetwork` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `TransferType` 
    
</dd>
</dl>

<dl>
<dd>

**user:** `TransferAuthorizationUserInRequest` 
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[TransferAccessToken]` 
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `typing.Optional[TransferAccountId]` 
    
</dd>
</dl>

<dl>
<dd>

**ach_class:** `typing.Optional[AchClass]` 
    
</dd>
</dl>

<dl>
<dd>

**beacon_session_id:** `typing.Optional[str]` — The unique identifier returned by Plaid's [beacon](https://plaid.com/docs/transfer/guarantee/#using-a-beacon) when it is run on your webpage. Required for Guarantee customers who are not using [Transfer UI](https://plaid.com/docs/transfer/using-transfer-ui/) and have a web checkout experience.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**device:** `typing.Optional[TransferAuthorizationDevice]` 
    
</dd>
</dl>

<dl>
<dd>

**funding_account_id:** `typing.Optional[TransferFundingAccountIdRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[TransferAuthorizationIdempotencyKey]` 
    
</dd>
</dl>

<dl>
<dd>

**iso_currency_code:** `typing.Optional[str]` — The currency of the transfer amount. The default value is "USD".
    
</dd>
</dl>

<dl>
<dd>

**origination_account_id:** `typing.Optional[str]` — Plaid's unique identifier for the origination account for this authorization. If not specified, the default account will be used.
    
</dd>
</dl>

<dl>
<dd>

**originator_client_id:** `typing.Optional[str]` — The Plaid client ID that is the originator of this transfer. Only needed if creating transfers on behalf of another client as a third-party sender (TPS).
    
</dd>
</dl>

<dl>
<dd>

**payment_profile_token:** `typing.Optional[TransferPaymentProfileToken]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**user_present:** `typing.Optional[bool]` — Required for Guarantee. If the end user is initiating the specific transfer themselves via an interactive UI, this should be `true`; for automatic recurring payments where the end user is not actually initiating each individual transfer, it should be `false`.
    
</dd>
</dl>

<dl>
<dd>

**with_guarantee:** `typing.Optional[bool]` — If set to `false`, Plaid will not offer a `guarantee_decision` for this request(Guarantee customers only).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L8994-L9045">transfer_cancel</a>(...) -> TransferCancelResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/transfer/cancel` endpoint to cancel a transfer.  A transfer is eligible for cancellation if the `cancellable` property returned by `/transfer/get` is `true`.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_cancel(
    transfer_id="transfer_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**transfer_id:** `TransferId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**originator_client_id:** `typing.Optional[str]` — The Plaid client ID of the transfer originator. Should only be present if `client_id` is a third-party sender (TPS).
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L9047-L9099">transfer_capabilities_get</a>(...) -> TransferCapabilitiesGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/transfer/capabilities/get` endpoint to determine the RTP eligibility information of a transfer.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_capabilities_get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `typing.Optional[TransferAccessToken]` 
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `typing.Optional[TransferAccountId]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**payment_profile_token:** `typing.Optional[PaymentProfileToken]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L9101-L9146">transfer_configuration_get</a>(...) -> TransferConfigurationGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/transfer/configuration/get` endpoint to view your transfer product configurations.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_configuration_get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**originator_client_id:** `typing.Optional[str]` — The Plaid client ID of the transfer originator. Should only be present if `client_id` is a third-party sender (TPS).
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L9148-L9251">transfer_create</a>(...) -> TransferCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/transfer/create` endpoint to initiate a new transfer.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_create(
    authorization_id="authorization_id",
    description="description",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization_id:** `str` — Plaid’s unique identifier for a transfer authorization. This parameter also serves the purpose of acting as an idempotency identifier.
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — The transfer description. Maximum of 10 characters. If reprocessing a returned transfer, please note that the `description` field must be `"Retry"` to indicate that it's a retry of a previously returned transfer. You may retry a transfer up to 2 times, within 180 days of creating the original transfer. Only transfers that were returned with code `R01` or `R09` may be retried. For a full listing of ACH return codes, see [Transfer errors](https://plaid.com/docs/errors/transfer/#ach-return-codes).
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[TransferAccessToken]` 
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `typing.Optional[TransferAccountId]` 
    
</dd>
</dl>

<dl>
<dd>

**ach_class:** `typing.Optional[AchClass]` 
    
</dd>
</dl>

<dl>
<dd>

**amount:** `typing.Optional[TransferAmount]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[TransferCreateIdempotencyKey]` 
    
</dd>
</dl>

<dl>
<dd>

**iso_currency_code:** `typing.Optional[str]` — The currency of the transfer amount. The default value is "USD".
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[TransferMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**network:** `typing.Optional[TransferNetwork]` 
    
</dd>
</dl>

<dl>
<dd>

**origination_account_id:** `typing.Optional[str]` — Plaid’s unique identifier for the origination account for this transfer. If you have more than one origination account, this value must be specified. Otherwise, this field should be left blank.
    
</dd>
</dl>

<dl>
<dd>

**payment_profile_token:** `typing.Optional[TransferPaymentProfileToken]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[TransferType]` 
    
</dd>
</dl>

<dl>
<dd>

**user:** `typing.Optional[TransferUserInRequestDeprecated]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L9253-L9352">transfer_event_list</a>(...) -> TransferEventListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/transfer/event/list` endpoint to get a list of transfer events based on specified filter criteria.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_event_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `typing.Optional[str]` — The account ID to get events for all transactions to/from an account.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The maximum number of transfer events to return. If the number of events matching the above parameters is greater than `count`, the most recent events will be returned.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` — The end datetime of transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)
    
</dd>
</dl>

<dl>
<dd>

**event_types:** `typing.Optional[typing.List[TransferEventType]]` — Filter events by event type.
    
</dd>
</dl>

<dl>
<dd>

**funding_account_id:** `typing.Optional[str]` — Filter transfer events to only those with the specified `funding_account_id`.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The offset into the list of transfer events. When `count`=25 and `offset`=0, the first 25 events will be returned. When `count`=25 and `offset`=25, the next 25 events will be returned.
    
</dd>
</dl>

<dl>
<dd>

**origination_account_id:** `typing.Optional[str]` — The origination account ID to get events for transfers from a specific origination account.
    
</dd>
</dl>

<dl>
<dd>

**originator_client_id:** `typing.Optional[str]` — Filter transfer events to only those with the specified originator client.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` — The start datetime of transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)
    
</dd>
</dl>

<dl>
<dd>

**sweep_id:** `typing.Optional[str]` — Plaid’s unique identifier for a sweep.
    
</dd>
</dl>

<dl>
<dd>

**transfer_id:** `typing.Optional[str]` — Plaid’s unique identifier for a transfer.
    
</dd>
</dl>

<dl>
<dd>

**transfer_type:** `typing.Optional[TransferEventListTransferType]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L9354-L9402">transfer_event_sync</a>(...) -> TransferEventSyncResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`/transfer/event/sync` allows you to request up to the next 25 transfer events that happened after a specific `event_id`. Use the `/transfer/event/sync` endpoint to guarantee you have seen all transfer events. When using Auth with micro-deposit verification enabled, this endpoint can be used to fetch status updates on ACH micro-deposits. For more details, see [micro-deposit events](https://www.plaid.com/docs/auth/coverage/microdeposit-events/).
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_event_sync(
    after_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after_id:** `int` — The latest (largest) `event_id` fetched via the sync endpoint, or 0 initially.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The maximum number of transfer events to return.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L9404-L9455">transfer_get</a>(...) -> TransferGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/transfer/get` endpoint fetches information about the transfer corresponding to the given `transfer_id`.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_get(
    transfer_id="transfer_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**transfer_id:** `TransferId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**originator_client_id:** `typing.Optional[str]` — The Plaid client ID of the transfer originator. Should only be present if `client_id` is a third-party sender (TPS).
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L9457-L9557">transfer_intent_create</a>(...) -> TransferIntentCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/transfer/intent/create` endpoint to generate a transfer intent object and invoke the Transfer UI.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TransferUserInRequest
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_intent_create(
    amount="amount",
    description="description",
    mode="PAYMENT",
    user=TransferUserInRequest(
        legal_name="legal_name",
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

**amount:** `TransferAmount` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — A description for the underlying transfer. Maximum of 8 characters.
    
</dd>
</dl>

<dl>
<dd>

**mode:** `TransferIntentCreateMode` 
    
</dd>
</dl>

<dl>
<dd>

**user:** `TransferUserInRequest` 
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `typing.Optional[str]` — The Plaid `account_id` corresponding to the end-user account that will be debited or credited.
    
</dd>
</dl>

<dl>
<dd>

**ach_class:** `typing.Optional[AchClass]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**funding_account_id:** `typing.Optional[TransferFundingAccountIdRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**iso_currency_code:** `typing.Optional[str]` — The currency of the transfer amount, e.g. "USD"
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[TransferMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**network:** `typing.Optional[TransferIntentCreateNetwork]` 
    
</dd>
</dl>

<dl>
<dd>

**origination_account_id:** `typing.Optional[str]` — Plaid’s unique identifier for the origination account for the intent. If not provided, the default account will be used.
    
</dd>
</dl>

<dl>
<dd>

**require_guarantee:** `typing.Optional[bool]` — When `true`, the transfer requires a `GUARANTEED` decision by Plaid to proceed (Guarantee customers only).
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L9559-L9603">transfer_intent_get</a>(...) -> TransferIntentGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/transfer/intent/get` endpoint to retrieve more information about a transfer intent.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_intent_get(
    transfer_intent_id="transfer_intent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**transfer_intent_id:** `str` — Plaid's unique identifier for a transfer intent object.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L9605-L9680">transfer_list</a>(...) -> TransferListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/transfer/list` endpoint to see a list of all your transfers and their statuses. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired transfers.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The maximum number of transfers to return.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` — The end datetime of transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)
    
</dd>
</dl>

<dl>
<dd>

**funding_account_id:** `typing.Optional[str]` — Filter transfers to only those with the specified `funding_account_id`.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of transfers to skip before returning results.
    
</dd>
</dl>

<dl>
<dd>

**origination_account_id:** `typing.Optional[str]` — Filter transfers to only those originated through the specified origination account.
    
</dd>
</dl>

<dl>
<dd>

**originator_client_id:** `typing.Optional[str]` — Filter transfers to only those with the specified originator client.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` — The start datetime of transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L9682-L9727">transfer_metrics_get</a>(...) -> TransferMetricsGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/transfer/metrics/get` endpoint to view your transfer product usage metrics.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_metrics_get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**originator_client_id:** `typing.Optional[str]` — The Plaid client ID of the transfer originator. Should only be present if `client_id` is a third-party sender (TPS).
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L9729-L9793">transfer_migrate_account</a>(...) -> TransferMigrateAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

As an alternative to adding Items via Link, you can also use the `/transfer/migrate_account` endpoint to migrate known account and routing numbers to Plaid Items.  Note that Items created in this way are not compatible with endpoints for other products, such as `/accounts/balance/get`, and can only be used with Transfer endpoints.  If you require access to other endpoints, create the Item through Link instead.  Access to `/transfer/migrate_account` is not enabled by default; to obtain access, contact your Plaid Account Manager.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_migrate_account(
    account_number="account_number",
    account_type="account_type",
    routing_number="routing_number",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_number:** `str` — The user's account number.
    
</dd>
</dl>

<dl>
<dd>

**account_type:** `str` — The type of the bank account (`checking` or `savings`).
    
</dd>
</dl>

<dl>
<dd>

**routing_number:** `str` — The user's routing number.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**wire_routing_number:** `typing.Optional[str]` — The user's wire transfer routing number. This is the ABA number; for some institutions, this may differ from the ACH number used in `routing_number`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L9795-L9839">transfer_originator_create</a>(...) -> TransferOriginatorCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/transfer/originator/create` endpoint to create a new originator and return an `originator_client_id`.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_originator_create(
    company_name="company_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_name:** `str` — The company name of the end customer being created. This will be displayed in public-facing surfaces, e.g. Plaid Dashboard.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L9841-L9888">transfer_originator_get</a>(...) -> TransferOriginatorGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/transfer/originator/get` endpoint gets status updates for an originator's onboarding process. This information is also available via the Transfer page on the Plaid dashboard.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_originator_get(
    originator_client_id="originator_client_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**originator_client_id:** `str` — Client ID of the end customer (i.e. the originator).
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L9890-L9936">transfer_originator_list</a>(...) -> TransferOriginatorListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/transfer/originator/list` endpoint gets status updates for all of your originators' onboarding. This information is also available via the Plaid dashboard.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_originator_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The maximum number of originators to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of originators to skip before returning results.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L9938-L9991">transfer_questionnaire_create</a>(...) -> TransferQuestionnaireCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/transfer/questionnaire/create` endpoint generates a Plaid-hosted onboarding UI URL. Redirect the originator to this URL to provide their due diligence information and agree to Plaid’s terms for ACH money movement.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_questionnaire_create(
    originator_client_id="originator_client_id",
    redirect_uri="redirect_uri",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**originator_client_id:** `str` — Client ID of the end customer.
    
</dd>
</dl>

<dl>
<dd>

**redirect_uri:** `str` — URL the end customer will be redirected to after completing questions in Plaid-hosted onboarding flow.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L9993-L10039">transfer_recurring_cancel</a>(...) -> TransferRecurringCancelResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/transfer/recurring/cancel` endpoint to cancel a recurring transfer.  Scheduled transfer that hasn't been submitted to bank will be cancelled.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_recurring_cancel(
    recurring_transfer_id="recurring_transfer_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**recurring_transfer_id:** `RecurringTransferId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L10041-L10175">transfer_recurring_create</a>(...) -> TransferRecurringCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/transfer/recurring/create` endpoint to initiate a new recurring transfer.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TransferDevice, TransferRecurringSchedule, TransferUserInRequest
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    api_key="<value>",
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_recurring_create(
    access_token="access_token",
    account_id="account_id",
    amount="amount",
    description="description",
    device=TransferDevice(
        ip_address="ip_address",
        user_agent="user_agent",
    ),
    idempotency_key="idempotency_key",
    network="ach",
    schedule=TransferRecurringSchedule(
        interval_count=1,
        interval_execution_day=1,
        interval_unit="week",
        start_date=datetime.date.fromisoformat("2023-01-15"),
    ),
    type="debit",
    user=TransferUserInRequest(
        legal_name="legal_name",
    ),
    user_present=None,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `TransferAccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `TransferAccountId` 
    
</dd>
</dl>

<dl>
<dd>

**amount:** `TransferAmount` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — The description of the recurring transfer.
    
</dd>
</dl>

<dl>
<dd>

**device:** `TransferDevice` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `TransferRecurringIdempotencyKey` 
    
</dd>
</dl>

<dl>
<dd>

**network:** `TransferNetwork` 
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `TransferRecurringSchedule` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `TransferType` 
    
</dd>
</dl>

<dl>
<dd>

**user:** `TransferUserInRequest` 
    
</dd>
</dl>

<dl>
<dd>

**ach_class:** `typing.Optional[AchClass]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**funding_account_id:** `typing.Optional[TransferFundingAccountIdRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**iso_currency_code:** `typing.Optional[str]` — The currency of the transfer amount. The default value is "USD".
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**test_clock_id:** `typing.Optional[str]` — Plaid’s unique identifier for a test clock.
    
</dd>
</dl>

<dl>
<dd>

**user_present:** `typing.Optional[bool]` — If the end user is initiating the specific transfer themselves via an interactive UI, this should be `true`; for automatic recurring payments where the end user is not actually initiating each individual transfer, it should be `false`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L10177-L10223">transfer_recurring_get</a>(...) -> TransferRecurringGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/transfer/recurring/get` fetches information about the recurring transfer corresponding to the given `recurring_transfer_id`.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_recurring_get(
    recurring_transfer_id="recurring_transfer_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**recurring_transfer_id:** `RecurringTransferId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L10225-L10290">transfer_recurring_list</a>(...) -> TransferRecurringListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/transfer/recurring/list` endpoint to see a list of all your recurring transfers and their statuses. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired recurring transfers.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_recurring_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The maximum number of recurring transfers to return.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[datetime.datetime]` — The end datetime of recurring transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)
    
</dd>
</dl>

<dl>
<dd>

**funding_account_id:** `typing.Optional[str]` — Filter recurring transfers to only those with the specified `funding_account_id`.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of recurring transfers to skip before returning results.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[datetime.datetime]` — The start datetime of recurring transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L10292-L10335">transfer_refund_cancel</a>(...) -> TransferRefundCancelResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/transfer/refund/cancel` endpoint to cancel a refund.  A refund is eligible for cancellation if it has not yet been submitted to the payment network.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_refund_cancel(
    refund_id="refund_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**refund_id:** `TransferRefundId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L10337-L10395">transfer_refund_create</a>(...) -> TransferRefundCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the `/transfer/refund/create` endpoint to create a refund for a transfer. A transfer can be refunded if the transfer was initiated in the past 180 days.

Processing of the refund will not occur until at least 3 business days following the transfer's settlement date, plus any hold/settlement delays. This 3-day window helps better protect your business from regular ACH returns. Consumer initiated returns (unauthorized returns) could still happen for about 60 days from the settlement date. If the original transfer is canceled, returned or failed, all pending refunds will automatically be canceled. Processed refunds cannot be revoked.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_refund_create(
    amount="amount",
    idempotency_key="idempotency_key",
    transfer_id="transfer_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**amount:** `TransferRefundAmount` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `TransferRefundIdempotencyKey` 
    
</dd>
</dl>

<dl>
<dd>

**transfer_id:** `TransferIdForRefund` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L10397-L10440">transfer_refund_get</a>(...) -> TransferRefundGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/transfer/refund/get` endpoint fetches information about the refund corresponding to the given `refund_id`.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_refund_get(
    refund_id="refund_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**refund_id:** `TransferRefundId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L10442-L10504">transfer_repayment_list</a>(...) -> TransferRepaymentListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/transfer/repayment/list` endpoint fetches repayments matching the given filters. Repayments are returned in reverse-chronological order (most recent first) starting at the given `start_time`.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_repayment_list(
    count=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The maximum number of repayments to return.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` — The end datetime of repayments to return (RFC 3339 format).
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of repayments to skip before returning results.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` — The start datetime of repayments to return (RFC 3339 format).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L10506-L10564">transfer_repayment_return_list</a>(...) -> TransferRepaymentReturnListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/transfer/repayment/return/list` endpoint retrieves the set of returns that were batched together into the specified repayment. The sum of amounts of returns retrieved by this request equals the amount of the repayment.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_repayment_return_list(
    count=1,
    repayment_id="d4bfce70-2470-4298-ae87-5e9b3e18bfaf",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**repayment_id:** `str` — Identifier of the repayment to query.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The maximum number of repayments to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of repayments to skip before returning results.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L10566-L10610">transfer_sweep_get</a>(...) -> TransferSweepGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/transfer/sweep/get` endpoint fetches a sweep corresponding to the given `sweep_id`.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_sweep_get(
    sweep_id="sweep_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sweep_id:** `str` — Plaid’s unique identifier for a sweep.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L10612-L10682">transfer_sweep_list</a>(...) -> TransferSweepListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/transfer/sweep/list` endpoint fetches sweeps matching the given filters.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.transfer_sweep_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The maximum number of sweeps to return.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` — The end datetime of sweeps to return (RFC 3339 format).
    
</dd>
</dl>

<dl>
<dd>

**funding_account_id:** `typing.Optional[str]` — Filter sweeps to only those with the specified `funding_account_id`.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of sweeps to skip before returning results.
    
</dd>
</dl>

<dl>
<dd>

**originator_client_id:** `typing.Optional[str]` — Filter sweeps to only those with the specified originator client.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` — The start datetime of sweeps to return (RFC 3339 format).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L10684-L10732">user_create</a>(...) -> UserCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint should be called for each of your end users before they begin a Plaid income flow. This provides you a single token to access all income data associated with the user. You should only create one per end user.

If you call the endpoint multiple times with the same `client_user_id`, the first creation call will succeed and the rest will fail with an error message indicating that the user has been created for the given `client_user_id`.

Ensure that you store the `user_token` along with your user's identifier in your database, as it is not possible to retrieve a previously created `user_token`.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.user_create(
    client_user_id="client_user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_user_id:** `str` — A unique ID representing the end user. Maximum of 128 characters. Typically this will be a user ID number from your application. Personally identifiable information, such as an email address or phone number, should not be used in the `client_user_id`.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L10734-L10777">wallet_create</a>(...) -> WalletCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an e-wallet. The response is the newly created e-wallet object.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.wallet_create(
    iso_currency_code="GBP",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**iso_currency_code:** `WalletIsoCurrencyCode` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L10779-L10823">wallet_get</a>(...) -> WalletGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch an e-wallet. The response includes the current balance.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.wallet_get(
    wallet_id="wallet_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**wallet_id:** `str` — The ID of the e-wallet
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L10825-L10879">wallet_list</a>(...) -> WalletListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint lists all e-wallets in descending order of creation.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.wallet_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of e-wallets to fetch
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — A base64 value representing the latest e-wallet that has already been requested. Set this to `next_cursor` received from the previous `/wallet/list` request. If provided, the response will only contain e-wallets created before that e-wallet. If omitted, the response will contain e-wallets starting from the most recent, and in descending order.
    
</dd>
</dl>

<dl>
<dd>

**iso_currency_code:** `typing.Optional[WalletIsoCurrencyCode]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L10881-L10963">wallet_transaction_execute</a>(...) -> WalletTransactionExecuteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a transaction using the specified e-wallet.
Specify the e-wallet to debit from, the counterparty to credit to, the idempotency key to prevent duplicate transactions, the amount and reference for the transaction.
Transactions will settle in seconds to several days, depending on the underlying payment rail.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, WalletTransactionAmount, WalletTransactionCounterparty, WalletTransactionCounterpartyNumbers
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.wallet_transaction_execute(
    amount=WalletTransactionAmount(
        iso_currency_code="GBP",
        value=1.1,
    ),
    counterparty=WalletTransactionCounterparty(
        name="name",
        numbers=WalletTransactionCounterpartyNumbers(),
    ),
    idempotency_key="idempotency_key",
    reference="reference",
    wallet_id="wallet_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**amount:** `WalletTransactionAmount` 
    
</dd>
</dl>

<dl>
<dd>

**counterparty:** `WalletTransactionCounterparty` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `WalletTransactionIdempotencyKey` 
    
</dd>
</dl>

<dl>
<dd>

**reference:** `str` 

A reference for the transaction. This must be an alphanumeric string with 6 to 18 characters and must not contain any special characters or spaces.
Ensure that the `reference` field is unique for each transaction.
    
</dd>
</dl>

<dl>
<dd>

**wallet_id:** `str` — The ID of the e-wallet to debit from
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L10965-L11009">wallet_transaction_get</a>(...) -> WalletTransactionGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch a specific e-wallet transaction
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.wallet_transaction_get(
    transaction_id="transaction_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**transaction_id:** `str` — The ID of the transaction to fetch
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L11011-L11072">wallet_transaction_list</a>(...) -> WalletTransactionListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint lists the latest transactions of the specified e-wallet. Transactions are returned in descending order by the `created_at` time.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.wallet_transaction_list(
    wallet_id="wallet_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**wallet_id:** `str` — The ID of the e-wallet to fetch transactions from
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of transactions to fetch
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — A base64 value representing the latest transaction that has already been requested. Set this to `next_cursor` received from the previous `/wallet/transaction/list` request. If provided, the response will only contain transactions created before that transaction. If omitted, the response will contain transactions starting from the most recent, and in descending order by the `created_at` time.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[WalletTransactionListRequestOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L11074-L11127">watchlist_screening_entity_create</a>(...) -> WatchlistScreeningEntityCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new entity watchlist screening to check your customer against watchlists defined in the associated entity watchlist program. If your associated program has ongoing screening enabled, this is the profile information that will be used to monitor your customer over time.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, EntityWatchlistSearchTerms
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.watchlist_screening_entity_create(
    search_terms=EntityWatchlistSearchTerms(
        entity_watchlist_program_id="entprg_2eRPsDnL66rZ7H",
        legal_name="Al-Qaida",
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

**search_terms:** `EntityWatchlistSearchTerms` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**client_user_id:** `typing.Optional[ClientUserId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L11129-L11175">watchlist_screening_entity_get</a>(...) -> WatchlistScreeningEntityGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve an entity watchlist screening.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.watchlist_screening_entity_get(
    entity_watchlist_screening_id="entscr_52xR9LKo77r1Np",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_watchlist_screening_id:** `EntityWatchlistScreeningId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L11177-L11227">watchlist_screening_entity_history_list</a>(...) -> WatchlistScreeningEntityHistoryListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all changes to the entity watchlist screening in reverse-chronological order. If the watchlist screening has not been edited, no history will be returned.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.watchlist_screening_entity_history_list(
    entity_watchlist_screening_id="entscr_52xR9LKo77r1Np",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_watchlist_screening_id:** `EntityWatchlistScreeningId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[Cursor]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L11229-L11279">watchlist_screening_entity_hit_list</a>(...) -> WatchlistScreeningEntityHitListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all hits for the entity watchlist screening.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.watchlist_screening_entity_hit_list(
    entity_watchlist_screening_id="entscr_52xR9LKo77r1Np",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_watchlist_screening_id:** `EntityWatchlistScreeningId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[Cursor]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L11281-L11343">watchlist_screening_entity_list</a>(...) -> WatchlistScreeningEntityListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all entity screenings.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.watchlist_screening_entity_list(
    entity_watchlist_program_id="entprg_2eRPsDnL66rZ7H",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_watchlist_program_id:** `EntityWatchlistProgramId` 
    
</dd>
</dl>

<dl>
<dd>

**assignee:** `typing.Optional[DashboardUserId]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**client_user_id:** `typing.Optional[ClientUserId]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[Cursor]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[WatchlistScreeningStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L11345-L11391">watchlist_screening_entity_program_get</a>(...) -> WatchlistScreeningEntityProgramGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an entity watchlist screening program
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.watchlist_screening_entity_program_get(
    entity_watchlist_program_id="entprg_2eRPsDnL66rZ7H",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_watchlist_program_id:** `EntityWatchlistProgramId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L11393-L11434">watchlist_screening_entity_program_list</a>(...) -> WatchlistScreeningEntityProgramListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all entity watchlist screening programs
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.watchlist_screening_entity_program_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[Cursor]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L11436-L11498">watchlist_screening_entity_review_create</a>(...) -> WatchlistScreeningEntityReviewCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a review for an entity watchlist screening. Reviews are compliance reports created by users in your organization regarding the relevance of potential hits found by Plaid.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.watchlist_screening_entity_review_create(
    confirmed_hits=[
        "enthit_52xR9LKo77r1Np"
    ],
    dismissed_hits=[
        "enthit_52xR9LKo77r1Np"
    ],
    entity_watchlist_screening_id="entscr_52xR9LKo77r1Np",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**confirmed_hits:** `typing.List[EntityWatchlistScreeningHitId]` — Hits to mark as a true positive after thorough manual review. These hits will never recur or be updated once dismissed. In most cases, confirmed hits indicate that the customer should be rejected.
    
</dd>
</dl>

<dl>
<dd>

**dismissed_hits:** `typing.List[EntityWatchlistScreeningHitId]` — Hits to mark as a false positive after thorough manual review. These hits will never recur or be updated once dismissed.
    
</dd>
</dl>

<dl>
<dd>

**entity_watchlist_screening_id:** `EntityWatchlistScreeningId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**comment:** `typing.Optional[ReviewComment]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L11500-L11550">watchlist_screening_entity_review_list</a>(...) -> WatchlistScreeningEntityReviewListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all reviews for a particular entity watchlist screening. Reviews are compliance reports created by users in your organization regarding the relevance of potential hits found by Plaid.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.watchlist_screening_entity_review_list(
    entity_watchlist_screening_id="entscr_52xR9LKo77r1Np",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_watchlist_screening_id:** `EntityWatchlistScreeningId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[Cursor]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L11552-L11618">watchlist_screening_entity_update</a>(...) -> WatchlistScreeningEntityUpdateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an entity watchlist screening.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.watchlist_screening_entity_update(
    entity_watchlist_screening_id="entscr_52xR9LKo77r1Np",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_watchlist_screening_id:** `EntityWatchlistScreeningId` 
    
</dd>
</dl>

<dl>
<dd>

**assignee:** `typing.Optional[DashboardUserId]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**client_user_id:** `typing.Optional[ClientUserId]` 
    
</dd>
</dl>

<dl>
<dd>

**reset_fields:** `typing.Optional[WatchlistScreeningEntityUpdateRequestResettableFieldList]` 
    
</dd>
</dl>

<dl>
<dd>

**search_terms:** `typing.Optional[UpdateEntityScreeningRequestSearchTerms]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[WatchlistScreeningStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L11620-L11673">watchlist_screening_individual_create</a>(...) -> WatchlistScreeningIndividualCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new Watchlist Screening to check your customer against watchlists defined in the associated Watchlist Program. If your associated program has ongoing screening enabled, this is the profile information that will be used to monitor your customer over time.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, WatchlistScreeningRequestSearchTerms
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.watchlist_screening_individual_create(
    search_terms=WatchlistScreeningRequestSearchTerms(
        legal_name="Aleksey Potemkin",
        watchlist_program_id="prg_2eRPsDnL66rZ7H",
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

**search_terms:** `WatchlistScreeningRequestSearchTerms` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**client_user_id:** `typing.Optional[ClientUserId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L11675-L11721">watchlist_screening_individual_get</a>(...) -> WatchlistScreeningIndividualGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a previously created individual watchlist screening
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.watchlist_screening_individual_get(
    watchlist_screening_id="scr_52xR9LKo77r1Np",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**watchlist_screening_id:** `WatchlistScreeningIndividualId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L11723-L11773">watchlist_screening_individual_history_list</a>(...) -> WatchlistScreeningIndividualHistoryListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all changes to the individual watchlist screening in reverse-chronological order. If the watchlist screening has not been edited, no history will be returned.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.watchlist_screening_individual_history_list(
    watchlist_screening_id="scr_52xR9LKo77r1Np",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**watchlist_screening_id:** `WatchlistScreeningIndividualId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[Cursor]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L11775-L11825">watchlist_screening_individual_hit_list</a>(...) -> WatchlistScreeningIndividualHitListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all hits found by Plaid for a particular individual watchlist screening.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.watchlist_screening_individual_hit_list(
    watchlist_screening_id="scr_52xR9LKo77r1Np",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**watchlist_screening_id:** `WatchlistScreeningIndividualId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[Cursor]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L11827-L11889">watchlist_screening_individual_list</a>(...) -> WatchlistScreeningIndividualListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List previously created watchlist screenings for individuals
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.watchlist_screening_individual_list(
    watchlist_program_id="prg_2eRPsDnL66rZ7H",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**watchlist_program_id:** `WatchlistProgramId` 
    
</dd>
</dl>

<dl>
<dd>

**assignee:** `typing.Optional[DashboardUserId]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**client_user_id:** `typing.Optional[ClientUserId]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[Cursor]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[WatchlistScreeningStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L11891-L11937">watchlist_screening_individual_program_get</a>(...) -> WatchlistScreeningIndividualProgramGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an individual watchlist screening program
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.watchlist_screening_individual_program_get(
    watchlist_program_id="prg_2eRPsDnL66rZ7H",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**watchlist_program_id:** `WatchlistProgramId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L11939-L11980">watchlist_screening_individual_program_list</a>(...) -> WatchlistScreeningIndividualProgramListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all individual watchlist screening programs
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.watchlist_screening_individual_program_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[Cursor]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L11982-L12044">watchlist_screening_individual_review_create</a>(...) -> WatchlistScreeningIndividualReviewCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a review for the individual watchlist screening. Reviews are compliance reports created by users in your organization regarding the relevance of potential hits found by Plaid.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.watchlist_screening_individual_review_create(
    confirmed_hits=[
        "scrhit_52xR9LKo77r1Np"
    ],
    dismissed_hits=[
        "scrhit_52xR9LKo77r1Np"
    ],
    watchlist_screening_id="scr_52xR9LKo77r1Np",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**confirmed_hits:** `typing.List[WatchlistScreeningHitId]` — Hits to mark as a true positive after thorough manual review. These hits will never recur or be updated once dismissed. In most cases, confirmed hits indicate that the customer should be rejected.
    
</dd>
</dl>

<dl>
<dd>

**dismissed_hits:** `typing.List[WatchlistScreeningHitId]` — Hits to mark as a false positive after thorough manual review. These hits will never recur or be updated once dismissed.
    
</dd>
</dl>

<dl>
<dd>

**watchlist_screening_id:** `WatchlistScreeningIndividualId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**comment:** `typing.Optional[ReviewComment]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L12046-L12096">watchlist_screening_individual_review_list</a>(...) -> WatchlistScreeningIndividualReviewListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all reviews for the individual watchlist screening.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.watchlist_screening_individual_review_list(
    watchlist_screening_id="scr_52xR9LKo77r1Np",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**watchlist_screening_id:** `WatchlistScreeningIndividualId` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[Cursor]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L12098-L12164">watchlist_screening_individual_update</a>(...) -> WatchlistScreeningIndividualUpdateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific individual watchlist screening. This endpoint can be used to add additional customer information, correct outdated information, add a reference id, assign the individual to a reviewer, and update which program it is associated with. Please note that you may not update `search_terms` and `status` at the same time since editing `search_terms` may trigger an automatic `status` change.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.watchlist_screening_individual_update(
    watchlist_screening_id="scr_52xR9LKo77r1Np",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**watchlist_screening_id:** `WatchlistScreeningIndividualId` 
    
</dd>
</dl>

<dl>
<dd>

**assignee:** `typing.Optional[DashboardUserId]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**client_user_id:** `typing.Optional[ClientUserId]` 
    
</dd>
</dl>

<dl>
<dd>

**reset_fields:** `typing.Optional[WatchlistScreeningIndividualUpdateRequestResettableFieldList]` 
    
</dd>
</dl>

<dl>
<dd>

**search_terms:** `typing.Optional[UpdateIndividualScreeningRequestSearchTerms]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[WatchlistScreeningStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plaid.<a href="src/fern/plaid/client.py#L12166-L12212">webhook_verification_key_get</a>(...) -> WebhookVerificationKeyGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Plaid signs all outgoing webhooks and provides JSON Web Tokens (JWTs) so that you can verify the authenticity of any incoming webhooks to your application. A message signature is included in the `Plaid-Verification` header.

The `/webhook_verification_key/get` endpoint provides a JSON Web Key (JWK) that can be used to verify a JWT.
</dd>
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
    plaid_version="<Plaid-Version>",
    plaid_secret="<PLAID-SECRET>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.plaid.webhook_verification_key_get(
    key_id="key_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key_id:** `str` — The key ID ( `kid` ) from the JWT header.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ApiClientId]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[ApiSecret]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

