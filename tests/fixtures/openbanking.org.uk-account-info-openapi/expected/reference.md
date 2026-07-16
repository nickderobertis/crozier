# Reference
## AccountAccess
<details><summary><code>client.account_access.<a href="src/fern/account_access/client.py">create_account_access_consents</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern.account_access import (
    ObReadConsent1Data,
    ObReadConsent1DataPermissionsItem,
)

from fern import FernApi, ObRisk2

client = FernApi(
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.account_access.create_account_access_consents(
    data=ObReadConsent1Data(
        permissions=[ObReadConsent1DataPermissionsItem.READ_ACCOUNTS_BASIC],
    ),
    risk=ObRisk2(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**data:** `ObReadConsent1Data` 
    
</dd>
</dl>

<dl>
<dd>

**risk:** `ObRisk2` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.account_access.<a href="src/fern/account_access/client.py">get_account_access_consents_consent_id</a>(...)</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.account_access.get_account_access_consents_consent_id(
    consent_id="ConsentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**consent_id:** `str` — ConsentId
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.account_access.<a href="src/fern/account_access/client.py">delete_account_access_consents_consent_id</a>(...)</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.account_access.delete_account_access_consents_consent_id(
    consent_id="ConsentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**consent_id:** `str` — ConsentId
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Accounts
<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">get_accounts</a>()</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.accounts.get_accounts()

```
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

<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">get_accounts_account_id</a>(...)</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.accounts.get_accounts_account_id(
    account_id="AccountId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — AccountId
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Balances
<details><summary><code>client.balances.<a href="src/fern/balances/client.py">get_accounts_account_id_balances</a>(...)</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.balances.get_accounts_account_id_balances(
    account_id="AccountId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — AccountId
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.balances.<a href="src/fern/balances/client.py">get_balances</a>()</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.balances.get_balances()

```
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

## Beneficiaries
<details><summary><code>client.beneficiaries.<a href="src/fern/beneficiaries/client.py">get_accounts_account_id_beneficiaries</a>(...)</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.beneficiaries.get_accounts_account_id_beneficiaries(
    account_id="AccountId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — AccountId
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beneficiaries.<a href="src/fern/beneficiaries/client.py">get_beneficiaries</a>()</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.beneficiaries.get_beneficiaries()

```
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

## DirectDebits
<details><summary><code>client.direct_debits.<a href="src/fern/direct_debits/client.py">get_accounts_account_id_direct_debits</a>(...)</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.direct_debits.get_accounts_account_id_direct_debits(
    account_id="AccountId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — AccountId
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.direct_debits.<a href="src/fern/direct_debits/client.py">get_direct_debits</a>()</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.direct_debits.get_direct_debits()

```
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

## Offers
<details><summary><code>client.offers.<a href="src/fern/offers/client.py">get_accounts_account_id_offers</a>(...)</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.offers.get_accounts_account_id_offers(
    account_id="AccountId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — AccountId
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.offers.<a href="src/fern/offers/client.py">get_offers</a>()</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.offers.get_offers()

```
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

## Parties
<details><summary><code>client.parties.<a href="src/fern/parties/client.py">get_accounts_account_id_parties</a>(...)</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.parties.get_accounts_account_id_parties(
    account_id="AccountId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — AccountId
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.parties.<a href="src/fern/parties/client.py">get_accounts_account_id_party</a>(...)</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.parties.get_accounts_account_id_party(
    account_id="AccountId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — AccountId
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.parties.<a href="src/fern/parties/client.py">get_party</a>()</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.parties.get_party()

```
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

## Products
<details><summary><code>client.products.<a href="src/fern/products/client.py">get_accounts_account_id_product</a>(...)</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.products.get_accounts_account_id_product(
    account_id="AccountId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — AccountId
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.products.<a href="src/fern/products/client.py">get_products</a>()</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.products.get_products()

```
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

## ScheduledPayments
<details><summary><code>client.scheduled_payments.<a href="src/fern/scheduled_payments/client.py">get_accounts_account_id_scheduled_payments</a>(...)</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.scheduled_payments.get_accounts_account_id_scheduled_payments(
    account_id="AccountId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — AccountId
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.scheduled_payments.<a href="src/fern/scheduled_payments/client.py">get_scheduled_payments</a>()</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.scheduled_payments.get_scheduled_payments()

```
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

## StandingOrders
<details><summary><code>client.standing_orders.<a href="src/fern/standing_orders/client.py">get_accounts_account_id_standing_orders</a>(...)</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.standing_orders.get_accounts_account_id_standing_orders(
    account_id="AccountId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — AccountId
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.standing_orders.<a href="src/fern/standing_orders/client.py">get_standing_orders</a>()</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.standing_orders.get_standing_orders()

```
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

## Statements
<details><summary><code>client.statements.<a href="src/fern/statements/client.py">get_accounts_account_id_statements</a>(...)</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.statements.get_accounts_account_id_statements(
    account_id="AccountId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — AccountId
    
</dd>
</dl>

<dl>
<dd>

**from_statement_date_time:** `typing.Optional[dt.datetime]` 

The UTC ISO 8601 Date Time to filter statements FROM
NB Time component is optional - set to 00:00:00 for just Date.
If the Date Time contains a timezone, the ASPSP must ignore the timezone component.
    
</dd>
</dl>

<dl>
<dd>

**to_statement_date_time:** `typing.Optional[dt.datetime]` 

The UTC ISO 8601 Date Time to filter statements TO
NB Time component is optional - set to 00:00:00 for just Date.
If the Date Time contains a timezone, the ASPSP must ignore the timezone component.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.statements.<a href="src/fern/statements/client.py">get_accounts_account_id_statements_statement_id</a>(...)</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.statements.get_accounts_account_id_statements_statement_id(
    account_id="AccountId",
    statement_id="StatementId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — AccountId
    
</dd>
</dl>

<dl>
<dd>

**statement_id:** `str` — StatementId
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.statements.<a href="src/fern/statements/client.py">get_accounts_account_id_statements_statement_id_file</a>(...)</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.statements.get_accounts_account_id_statements_statement_id_file(
    account_id="AccountId",
    statement_id="StatementId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — AccountId
    
</dd>
</dl>

<dl>
<dd>

**statement_id:** `str` — StatementId
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.statements.<a href="src/fern/statements/client.py">get_statements</a>(...)</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.statements.get_statements()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**from_statement_date_time:** `typing.Optional[dt.datetime]` 

The UTC ISO 8601 Date Time to filter statements FROM
NB Time component is optional - set to 00:00:00 for just Date.
If the Date Time contains a timezone, the ASPSP must ignore the timezone component.
    
</dd>
</dl>

<dl>
<dd>

**to_statement_date_time:** `typing.Optional[dt.datetime]` 

The UTC ISO 8601 Date Time to filter statements TO
NB Time component is optional - set to 00:00:00 for just Date.
If the Date Time contains a timezone, the ASPSP must ignore the timezone component.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Transactions
<details><summary><code>client.transactions.<a href="src/fern/transactions/client.py">get_accounts_account_id_statements_statement_id_transactions</a>(...)</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.transactions.get_accounts_account_id_statements_statement_id_transactions(
    account_id="AccountId",
    statement_id="StatementId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — AccountId
    
</dd>
</dl>

<dl>
<dd>

**statement_id:** `str` — StatementId
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/fern/transactions/client.py">get_accounts_account_id_transactions</a>(...)</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.transactions.get_accounts_account_id_transactions(
    account_id="AccountId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — AccountId
    
</dd>
</dl>

<dl>
<dd>

**from_booking_date_time:** `typing.Optional[dt.datetime]` 

The UTC ISO 8601 Date Time to filter transactions FROM
NB Time component is optional - set to 00:00:00 for just Date.
If the Date Time contains a timezone, the ASPSP must ignore the timezone component.
    
</dd>
</dl>

<dl>
<dd>

**to_booking_date_time:** `typing.Optional[dt.datetime]` 

The UTC ISO 8601 Date Time to filter transactions TO
NB Time component is optional - set to 00:00:00 for just Date.
If the Date Time contains a timezone, the ASPSP must ignore the timezone component.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/fern/transactions/client.py">get_transactions</a>(...)</code></summary>
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
    fapi_auth_date="YOUR_FAPI_AUTH_DATE",
    fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
    fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
    customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
    token="YOUR_TOKEN",
)
client.transactions.get_transactions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**from_booking_date_time:** `typing.Optional[dt.datetime]` 

The UTC ISO 8601 Date Time to filter transactions FROM
NB Time component is optional - set to 00:00:00 for just Date.
If the Date Time contains a timezone, the ASPSP must ignore the timezone component.
    
</dd>
</dl>

<dl>
<dd>

**to_booking_date_time:** `typing.Optional[dt.datetime]` 

The UTC ISO 8601 Date Time to filter transactions TO
NB Time component is optional - set to 00:00:00 for just Date.
If the Date Time contains a timezone, the ASPSP must ignore the timezone component.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

