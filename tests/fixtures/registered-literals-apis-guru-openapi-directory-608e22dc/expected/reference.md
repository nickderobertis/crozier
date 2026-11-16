# Reference
## Transfers
<details><summary><code>client.transfers.<a href="src/fern/transfers/client.py#L33-L83">retrieve_balance_transfers</a>(...) -> ListBalanceTransfersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of balance transfers that have taken place for a primary account within a specified time period.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.transfers.retrieve_balance_transfers(
    api_key="api_key",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — ID of the primary account.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Start of the retrieval period.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — End of the retrieval period. If absent then all transfers until now is returned.
    
</dd>
</dl>

<dl>
<dd>

**subaccount:** `typing.Optional[str]` — Subaccount to filter by. You may send this multiple times to filter on multiple subaccounts
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transfers.<a href="src/fern/transfers/client.py#L85-L137">transfer_balance</a>(...) -> TransferBalanceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Transfer balance between a primary account and one of its subaccounts. Note that balance_available_for_transfer = |account_balance - credit_limit| of the source account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.transfers.transfer_balance(
    api_key="api_key",
    amount=1.1,
    from_="7c9738e6",
    to="ad6dc56f",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — ID of the primary account
    
</dd>
</dl>

<dl>
<dd>

**request:** `TransferBalanceOrCreditRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transfers.<a href="src/fern/transfers/client.py#L139-L189">retrieve_credit_transfers</a>(...) -> ListCreditTransfersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of credit transfers that have taken place for a primary account within a specified time period.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.transfers.retrieve_credit_transfers(
    api_key="api_key",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — ID of the primary account.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Start of the retrieval period.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — End of the retrieval period. If absent then all transfers until now is returned.
    
</dd>
</dl>

<dl>
<dd>

**subaccount:** `typing.Optional[str]` — Subaccount to filter by. You may send this multiple times to filter on multiple subaccounts
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transfers.<a href="src/fern/transfers/client.py#L191-L243">transfer_credit</a>(...) -> TransferCreditResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Transfer credit limit between a primary account and one of its subaccounts.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.transfers.transfer_credit(
    api_key="api_key",
    amount=1.1,
    from_="7c9738e6",
    to="ad6dc56f",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — ID of the primary account
    
</dd>
</dl>

<dl>
<dd>

**request:** `TransferBalanceOrCreditRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transfers.<a href="src/fern/transfers/client.py#L245-L294">transfer_number</a>(...) -> TransferNumberResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Transfer number from one account to another.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.transfers.transfer_number(
    api_key="api_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — ID of the primary account.
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**number:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Subaccount Management
<details><summary><code>client.subaccount_management.<a href="src/fern/subaccount_management/client.py#L31-L63">retrieve_subaccounts_list</a>(...) -> SubaccountsAllResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the information of all the subaccounts owned by the primary account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.subaccount_management.retrieve_subaccounts_list(
    api_key="api_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — ID of the primary account
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subaccount_management.<a href="src/fern/subaccount_management/client.py#L65-L116">create_sub_account</a>(...) -> SubaccountCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a subaccount for a given primary account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.subaccount_management.create_sub_account(
    api_key="api_key",
    name="Subaccount department A",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — ID of the primary account
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**use_primary_account_balance:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subaccount_management.<a href="src/fern/subaccount_management/client.py#L118-L154">retrieve_subaccount</a>(...) -> SubaccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the information of a subaccount specified with its API key.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.subaccount_management.retrieve_subaccount(
    api_key="api_key",
    subaccount_key="subaccount_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — ID of the primary account
    
</dd>
</dl>

<dl>
<dd>

**subaccount_key:** `str` — ID of the subaccount
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subaccount_management.<a href="src/fern/subaccount_management/client.py#L156-L212">modify_subaccount</a>(...) -> SubaccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Change one or more properties of a subaccount.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.subaccount_management.modify_subaccount(
    api_key="api_key",
    subaccount_key="subaccount_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — ID of the primary account
    
</dd>
</dl>

<dl>
<dd>

**subaccount_key:** `str` — ID of the subaccount
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**suspended:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**use_primary_account_balance:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

