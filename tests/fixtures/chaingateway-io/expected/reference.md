# Reference
## Transaction Requests
<details><summary><code>client.transaction_requests.<a href="src/fern/transaction_requests/client.py">clear_address</a>(...) -> ClearAddress</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sends all available ethereum funds of an address to a specified receiver address.
</dd>
</dl>
</dd>
</dl>

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

client.transaction_requests.clear_address(
    authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
    ethereumaddress="0x3a32c4c31fe8d2a89976af5d284a94a040b44aa8",
    newaddress="0xef4943d727e34280a2efa0b3352dfd61f508ee48",
    password="padN39QkRA2hJ",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — API Key
    
</dd>
</dl>

<dl>
<dd>

**ethereumaddress:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**newaddress:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transaction_requests.<a href="src/fern/transaction_requests/client.py">send_ethereum</a>(...) -> SendEthereum</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sends ethereum from an address controlled by the account to a specified receiver address.
</dd>
</dl>
</dd>
</dl>

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

client.transaction_requests.send_ethereum(
    authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
    amount=0.01,
    from_="0x3a32c4c31fe8d2a89976af5d284a94a040b44aa8",
    password="padN39QkRA2hJ",
    to="0xef4943d727e34280a2efa0b3352dfd61f508ee48",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — API Key
    
</dd>
</dl>

<dl>
<dd>

**amount:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**from:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transaction_requests.<a href="src/fern/transaction_requests/client.py">send_token</a>(...) -> SendToken</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sends ERC20 tokens from an address controlled by the account to a specified receiver address. The token contract address is needed to specify the token. The use of the identifier parameter is recommend and awaits an unique string. Whenever a transaction is beeing sent, the identifier is checked and the transaction gets dropped if there is one with that identifier already.
</dd>
</dl>
</dd>
</dl>

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

client.transaction_requests.send_token(
    authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
    amount=5,
    contractaddress="0xdac17f958d2ee523a2206206994597c13d831ec7",
    from_="0x3a32c4c31fe8d2a89976af5d284a94a040b44aa8",
    identifier="CN562",
    password="padN39QkRA2hJ",
    to="0xef4943d727e34280a2efa0b3352dfd61f508ee48",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — API Key
    
</dd>
</dl>

<dl>
<dd>

**amount:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**contractaddress:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**from:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**identifier:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Address Requests
<details><summary><code>client.address_requests.<a href="src/fern/address_requests/client.py">delete_address</a>(...) -> DeleteAddress</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing ethereum address. Be careful when using this function.
</dd>
</dl>
</dd>
</dl>

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

client.address_requests.delete_address(
    authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
    ethereumaddress="0x71892689ed0d79d88ab6ea3783b571b8ece9bee3",
    password="padN39QkRA2hJ",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — API Key
    
</dd>
</dl>

<dl>
<dd>

**ethereumaddress:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.address_requests.<a href="src/fern/address_requests/client.py">export_address</a>(...) -> ExportAddress</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all ethereum addresses created with an account.
</dd>
</dl>
</dd>
</dl>

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

client.address_requests.export_address(
    authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
    ethaddress="0x71892889ed4d79d88ab6ea3783b571b8ece9bef4",
    password="padN39QkRA2hJ",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — API Key
    
</dd>
</dl>

<dl>
<dd>

**ethaddress:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.address_requests.<a href="src/fern/address_requests/client.py">import_address</a>(...) -> ImportAddress</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all ethereum addresses created with an account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Content, Crypto, Cipherparams, Kdfparams
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.address_requests.import_address(
    authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
    content=Content(
        address="71892889ed4d79d88ab6ea3783b571b8ece9bef4",
        crypto=Crypto(
            cipher="aes-128-ctr",
            cipherparams=Cipherparams(
                iv="76e6f2497b9f2a8e024fc752a5418a6d",
            ),
            ciphertext="9d74262517b984f9b0560b8f23b5e3340f7be0f56b70cd91ff445dcaf5b1968f",
            kdf="scrypt",
            kdfparams=Kdfparams(
                dklen=32,
                n=131072,
                p=1,
                r=8,
                salt="d11d996a7cc4bfad730d4c9b9057eff2c0fb3940b5bfc59db62ae218c14a54f4",
            ),
            mac="dcc342bbbbb8eea97c89b47bafc23de568fc1a48e0bd21ae8d776a95c4704ac9",
        ),
        id="85b790ff-408e-42b8-b123-bec9523964dc",
        version=3,
    ),
    filename="UTC--2020-09-19T10-42-26.196Z--71892889ed4d79d88ab6ea3783b571b8ece9bef4",
    password="padN39QkRA2hJ",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — API Key
    
</dd>
</dl>

<dl>
<dd>

**content:** `Content` 
    
</dd>
</dl>

<dl>
<dd>

**filename:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.address_requests.<a href="src/fern/address_requests/client.py">list_addresses</a>(...) -> ListAddresses</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all ethereum addresses created with an account.
</dd>
</dl>
</dd>
</dl>

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

client.address_requests.list_addresses(
    authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — API Key
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.address_requests.<a href="src/fern/address_requests/client.py">new_address</a>(...) -> NewAddress</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates a new ethereum addresses you can use to send or receive funds. Do not lose the password! We can't restore access to an address if you lose it.
</dd>
</dl>
</dd>
</dl>

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

client.address_requests.new_address(
    authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
    password="padN39QkRA2hJ",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — API Key
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Info Requests
<details><summary><code>client.info_requests.<a href="src/fern/info_requests/client.py">get_block</a>(...) -> GetBlock</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information of an ethereum block with or without transactions
</dd>
</dl>
</dd>
</dl>

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

client.info_requests.get_block(
    authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
    block="5000000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — API Key
    
</dd>
</dl>

<dl>
<dd>

**block:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.info_requests.<a href="src/fern/info_requests/client.py">get_ethereum_balance</a>(...) -> GetEthereumBalance</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the ethereum balance of a given address.
</dd>
</dl>
</dd>
</dl>

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

client.info_requests.get_ethereum_balance(
    authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
    ethereumaddress="0xa1f36016221d48ce7f15cde7b826a4fbe09bacce",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — API Key
    
</dd>
</dl>

<dl>
<dd>

**ethereumaddress:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.info_requests.<a href="src/fern/info_requests/client.py">get_exchange_rate</a>(...) -> GetExchangeRate</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current Ethereum price in Euro or US Dollar.
</dd>
</dl>
</dd>
</dl>

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

client.info_requests.get_exchange_rate(
    authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
    currency="eur",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — API Key
    
</dd>
</dl>

<dl>
<dd>

**currency:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.info_requests.<a href="src/fern/info_requests/client.py">get_gas_price</a>(...) -> GetGasPrice</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current gas price in GWEI.
</dd>
</dl>
</dd>
</dl>

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

client.info_requests.get_gas_price(
    authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — API Key
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.info_requests.<a href="src/fern/info_requests/client.py">get_last_block_number</a>(...) -> GetLastBlockNumber</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the block number of the last mined ethereum block.
</dd>
</dl>
</dd>
</dl>

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

client.info_requests.get_last_block_number(
    authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — API Key
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.info_requests.<a href="src/fern/info_requests/client.py">get_token</a>(...) -> GetToken</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information about a specific ERC20 token like name, symbol, decimal places and total supply.
</dd>
</dl>
</dd>
</dl>

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

client.info_requests.get_token(
    authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
    contractaddress="0x5b86a33f0c232fe909eb4602a9d039072869d915",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — API Key
    
</dd>
</dl>

<dl>
<dd>

**contractaddress:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.info_requests.<a href="src/fern/info_requests/client.py">get_token_balance</a>(...) -> GetTokenBalance</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the token balance of a given address.
</dd>
</dl>
</dd>
</dl>

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

client.info_requests.get_token_balance(
    authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
    contractaddress="0x5b86a33f0c232fe909eb4602a9d039072869d915",
    ethereumaddress="0xa1f36016221d48ce7f15cde7b826a4fbe09bacce",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — API Key
    
</dd>
</dl>

<dl>
<dd>

**contractaddress:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**ethereumaddress:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.info_requests.<a href="src/fern/info_requests/client.py">get_transactions</a>(...) -> GetTransactions</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information like confirmations, token contract address, amount, gas price and more of a given transaction.
</dd>
</dl>
</dd>
</dl>

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

client.info_requests.get_transactions(
    authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
    txid="0x8ab5543bc103bdd908681da501d03c2c495afd7fde5ed104935ba97b1550d65b",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — API Key
    
</dd>
</dl>

<dl>
<dd>

**txid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Subscription/IPN Requests
<details><summary><code>client.subscription_ipn_requests.<a href="src/fern/subscription_ipn_requests/client.py">list_failed_ip_ns</a>(...) -> ListFailedIpNs</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all subscriptions/IPNs created with an account.
</dd>
</dl>
</dd>
</dl>

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

client.subscription_ipn_requests.list_failed_ip_ns(
    authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — API Key
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscription_ipn_requests.<a href="src/fern/subscription_ipn_requests/client.py">list_subscribed_addresses</a>(...) -> ListSubscribedAddresses</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all subscriptions/IPNs created with an account.
</dd>
</dl>
</dd>
</dl>

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

client.subscription_ipn_requests.list_subscribed_addresses(
    authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — API Key
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscription_ipn_requests.<a href="src/fern/subscription_ipn_requests/client.py">resend_failed_ipn</a>(...) -> ResendFailedIpn</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all subscriptions/IPNs created with an account.
</dd>
</dl>
</dd>
</dl>

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

client.subscription_ipn_requests.resend_failed_ipn(
    authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
    id=17766,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — API Key
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscription_ipn_requests.<a href="src/fern/subscription_ipn_requests/client.py">subscribe_address</a>(...) -> SubscribeAddress</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new subscription/IPN for the given address (and contractaddress). You will receive a notification to the given url every time a deposit is received. Unsubscribe the address before sending tokens/ETH from it or you won't get reliable notifications anymore.
</dd>
</dl>
</dd>
</dl>

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

client.subscription_ipn_requests.subscribe_address(
    authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
    contractaddress="0x514910771af9ca656af840dff83e8264ecf986ca",
    ethereumaddress="0xa2107fa5b38d9bbd2c461d6edf11b11a50f6b974",
    url="https://yoururl.com/ipnreceiver.php",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — API Key
    
</dd>
</dl>

<dl>
<dd>

**contractaddress:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**ethereumaddress:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscription_ipn_requests.<a href="src/fern/subscription_ipn_requests/client.py">unsubscribe_address</a>(...) -> UnsubscribeAddress</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing subscription/IPN for the given address (and contractaddress).
</dd>
</dl>
</dd>
</dl>

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

client.subscription_ipn_requests.unsubscribe_address(
    authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
    contractaddress="0x514910771af9ca656af840dff83e8264ecf986ca",
    ethereumaddress="0xa2107fa5b38d9bbd2c461d6edf11b11a50f6b974",
    url="https://yoururl.com/ipnreceiver.php",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — API Key
    
</dd>
</dl>

<dl>
<dd>

**contractaddress:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**ethereumaddress:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

