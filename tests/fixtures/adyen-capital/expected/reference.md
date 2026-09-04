# Reference
## Dynamic offers
<details><summary><code>client.dynamic_offers.<a href="src/fern/dynamic_offers/client.py">get_dynamic_offers</a>(...) -> GetDynamicOffersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all [dynamic offers](https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/) available for `accountHolderId` specified as a query parameter.
</dd>
</dl>
</dd>
</dl>

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

client.dynamic_offers.get_dynamic_offers(
    account_holder_id="accountHolderId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_holder_id:** `str` — The unique identifier of the account holder that the dynamic offer is for.
    
</dd>
</dl>

<dl>
<dd>

**financing_type:** `typing.Optional[FinancingType]` 

The type of financing that the offer is for. If the value is not specified, returns all available types.

Possible values: **businessFinancing**
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dynamic_offers.<a href="src/fern/dynamic_offers/client.py">post_dynamic_offers_id_calculate</a>(...) -> CalculatedGrantOffer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Calculates a preliminary offer for the financing amount that the user selected from a [dynamic offer](https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/). The preliminary offer is for informational purposes only and cannot be used to initiate a grant.

Requests to this endpoint are subject to rate limits:

- Live environments: 120 requests per minute.

- Test environments: 120 requests per minute.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Amount
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.dynamic_offers.post_dynamic_offers_id_calculate(
    id="id",
    amount=Amount(
        currency="currency",
        value=1000000,
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

**id:** `str` — The unique identifier of the dynamic offer from which the user selected the financing amount.
    
</dd>
</dl>

<dl>
<dd>

**amount:** `Amount` — The financing amount that the user selected from a dynamic offer. Adyen uses this amount to calculate a preliminary offer.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dynamic_offers.<a href="src/fern/dynamic_offers/client.py">post_dynamic_offers_id_grant_offer</a>(...) -> GrantOffer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a static offer for the financing amount that the user selected from the [dynamic offer](https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/).

Requests to this endpoint are subject to rate limits:

- Live environments: 30 requests per minute.

- Test environments: 30 requests per minute.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Amount
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.dynamic_offers.post_dynamic_offers_id_grant_offer(
    id="id",
    amount=Amount(
        currency="currency",
        value=1000000,
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

**id:** `str` — The unique identifier of the dynamic offer from which the user selected the financing amount.
    
</dd>
</dl>

<dl>
<dd>

**amount:** `Amount` — The financing amount that the user selected from the dynamic offer. Adyen uses this amount to create a static offer.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Grant accounts
<details><summary><code>client.grant_accounts.<a href="src/fern/grant_accounts/client.py">get_grant_accounts_id</a>(...) -> GrantAccount</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the details of the specified grant account. This account tracks existing grants in your marketplace or platform.
</dd>
</dl>
</dd>
</dl>

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

client.grant_accounts.get_grant_accounts_id(
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

**id:** `str` — The unique identifier of the grant account.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Grant offers
<details><summary><code>client.grant_offers.<a href="src/fern/grant_offers/client.py">get_grant_offers</a>(...) -> GrantOffers</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all [static offers](https://docs.adyen.com/capital/get-grant-offers/static-offers) available for `accountHolderId` specified as a query parameter. This also includes static offers created for financing amounts that the user selected from [dynamic offers](https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/).
</dd>
</dl>
</dd>
</dl>

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

client.grant_offers.get_grant_offers(
    account_holder_id="accountHolderId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_holder_id:** `str` — The unique identifier of the account holder for which you want to get the available static offers.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.grant_offers.<a href="src/fern/grant_offers/client.py">get_grant_offers_id</a>(...) -> GrantOffer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the details of the specified static offer.
</dd>
</dl>
</dd>
</dl>

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

client.grant_offers.get_grant_offers_id(
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

**id:** `str` — The unique identifier of the static offer.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Grants
<details><summary><code>client.grants.<a href="src/fern/grants/client.py">get_grants</a>(...) -> Grants</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all the grants of a specific account holder.
</dd>
</dl>
</dd>
</dl>

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

client.grants.get_grants(
    counterparty_account_holder_id="counterpartyAccountHolderId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**counterparty_account_holder_id:** `str` — The unique identifier of the account holder that received the grants.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.grants.<a href="src/fern/grants/client.py">post_grants</a>(...) -> Grant</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Make a request for a grant on behalf of an account holder.
</dd>
</dl>
</dd>
</dl>

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

client.grants.post_grants(
    grant_account_id="grantAccountId",
    grant_offer_id="grantOfferId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**grant_account_id:** `str` — The unique identifier of the grant account that tracks this grant.
    
</dd>
</dl>

<dl>
<dd>

**grant_offer_id:** `str` — The unique identifier of the selected offer. Adyen uses the details of the selected offer to create a grant.
    
</dd>
</dl>

<dl>
<dd>

**counterparty:** `typing.Optional[GrantInfoCounterparty]` — Contains the details of the party that receives the grant.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.grants.<a href="src/fern/grants/client.py">get_grants_grant_id</a>(...) -> Grant</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the details of the specified grant.
</dd>
</dl>
</dd>
</dl>

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

client.grants.get_grants_grant_id(
    grant_id="grantId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**grant_id:** `str` — The unique identifier of the grant reference.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.grants.<a href="src/fern/grants/client.py">get_grants_grant_id_disbursements</a>(...) -> Disbursements</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the disbursements of a specified grant.
</dd>
</dl>
</dd>
</dl>

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

client.grants.get_grants_grant_id_disbursements(
    grant_id="grantId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**grant_id:** `str` — The unique identifier of the grant reference.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.grants.<a href="src/fern/grants/client.py">get_grants_grant_id_disbursements_disbursement_id</a>(...) -> Disbursement</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the details of a disbursement specified in the path.
</dd>
</dl>
</dd>
</dl>

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

client.grants.get_grants_grant_id_disbursements_disbursement_id(
    grant_id="grantId",
    disbursement_id="disbursementId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**grant_id:** `str` — The unique identifier of the grant reference.
    
</dd>
</dl>

<dl>
<dd>

**disbursement_id:** `str` — The unique identifier of the disbursement.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.grants.<a href="src/fern/grants/client.py">patch_grants_grant_id_disbursements_disbursement_id</a>(...) -> Disbursement</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the percentage of your user's net income that is deducted for repaying the grant.
</dd>
</dl>
</dd>
</dl>

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

client.grants.patch_grants_grant_id_disbursements_disbursement_id(
    grant_id="grantId",
    disbursement_id="disbursementId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**grant_id:** `str` — The unique identifier of the grant reference.
    
</dd>
</dl>

<dl>
<dd>

**disbursement_id:** `str` — The unique identifier of the disbursement.
    
</dd>
</dl>

<dl>
<dd>

**repayment:** `typing.Optional[DisbursementRepaymentInfoUpdate]` — Contains information about the basis points configured for repaying the disbursement.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

