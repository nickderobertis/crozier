# Reference
## OnChain
<details><summary><code>client.on_chain.<a href="src/fern/on_chain/client.py">get_a_bitcoin_address</a>() -> AddressResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a new Bitcoin address from the internal BDK wallet
</dd>
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

client.on_chain.get_a_bitcoin_address()

```
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

<details><summary><code>client.on_chain.<a href="src/fern/on_chain/client.py">get_the_btc_balance</a>(...) -> BtcBalanceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the node's bitcoin balance for the vanilla and colored wallets
</dd>
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

client.on_chain.get_the_btc_balance(
    skip_sync=False,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**skip_sync:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.on_chain.<a href="src/fern/on_chain/client.py">get_fee_estimation</a>(...) -> EstimateFeeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get on-chain fee estimation
</dd>
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

client.on_chain.get_fee_estimation(
    blocks=7,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**blocks:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.on_chain.<a href="src/fern/on_chain/client.py">list_transactions</a>(...) -> ListTransactionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the node's on-chain transactions
</dd>
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

client.on_chain.list_transactions(
    skip_sync=False,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**skip_sync:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.on_chain.<a href="src/fern/on_chain/client.py">list_unspents</a>(...) -> ListUnspentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the unspent outputs of the internal BDK wallet
</dd>
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

client.on_chain.list_unspents(
    settled_only=False,
    skip_sync=False,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**settled_only:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**skip_sync:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.on_chain.<a href="src/fern/on_chain/client.py">send_btc</a>(...) -> SendBtcResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send bitcoins on-chain
</dd>
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

client.on_chain.send_btc(
    amount=16900,
    address="bcrt1qwxht5tut39dws8tjcf649tp908r8fr2j75c94k",
    fee_rate=5,
    skip_sync=False,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**amount:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**address:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fee_rate:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**skip_sync:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Rgb
<details><summary><code>client.rgb.<a href="src/fern/rgb/client.py">get_the_balance_of_an_asset</a>(...) -> AssetBalanceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the balance for the provided RGB asset
</dd>
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

client.rgb.get_the_balance_of_an_asset(
    asset_id="rgb:CJkb4YZw-jRiz2sk-~PARPio-wtVYI1c-XAEYCqO-wTfvRZ8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.rgb.<a href="src/fern/rgb/client.py">get_the_metadata_of_an_asset</a>(...) -> AssetMetadataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the metadata for the provided RGB asset
</dd>
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

client.rgb.get_the_metadata_of_an_asset(
    asset_id="rgb:CJkb4YZw-jRiz2sk-~PARPio-wtVYI1c-XAEYCqO-wTfvRZ8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.rgb.<a href="src/fern/rgb/client.py">create_utx_os</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create UTXOs to be used for RGB operations
</dd>
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

client.rgb.create_utx_os(
    up_to=False,
    fee_rate=5,
    skip_sync=False,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**up_to:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**fee_rate:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**skip_sync:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**num:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.rgb.<a href="src/fern/rgb/client.py">decode_an_rgb_invoice</a>(...) -> DecodeRgbInvoiceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Decode the provided RGB invoice string
</dd>
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

client.rgb.decode_an_rgb_invoice(
    invoice="rgb:icfqnK9y-wObZKTu-XJcDL98-sKbE5Mh-OuDJhiI-brRJrzE/RWhwUfTMpuP2Zfx1~j4nswCANGeJrYOqDcKelaMV4zU/~/bcrt:utxob:cbgHUJ4e-7QyKY4U-Jsj5AZw-oI0gxZh-7fxQY2_-tFFUAZN-4CgpX?expiry=1749906951&endpoints=rpcs://proxy.iriswallet.com/0.2/json-rpc",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.rgb.<a href="src/fern/rgb/client.py">fail_rgb_transfers</a>(...) -> FailTransfersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set the status for eligible RGB transfers to `TransferStatus::Failed`.
</dd>
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

client.rgb.fail_rgb_transfers(
    no_asset_only=False,
    skip_sync=False,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**no_asset_only:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**skip_sync:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**batch_transfer_idx:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.rgb.<a href="src/fern/rgb/client.py">get_an_asset_media</a>(...) -> GetAssetMediaResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the hex string of the media bytes of the provided media digest
</dd>
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

client.rgb.get_an_asset_media(
    digest="5891b5b522d5df086d0ff0b110fbd9d21bb4fc7163af34d08286a2e846f6be03",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**digest:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.rgb.<a href="src/fern/rgb/client.py">get_a_send_consignment</a>(...) -> GetConsignmentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the hex string of the consignment bytes for a send transfer, identified by its asset ID and txid. Useful to hand the consignment to the counterparty out-of-band when the node filesystem is not accessible from the API caller.
</dd>
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

client.rgb.get_a_send_consignment(
    asset_id="rgb:2dkSTbr-jFhznbPmo-TQafzswCN-av4gTsJjX-ttx6CNou5-M98k8Zt",
    txid="33cf3e42fb1c6faa0d47e6a498a9d4e5c56e8a06ea0d295c6d90e2b6c85f7a1e",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_id:** `str` 
    
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

<details><summary><code>client.rgb.<a href="src/fern/rgb/client.py">inflate_rgb_assets</a>(...) -> InflateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Inflate RGB assets on-chain
</dd>
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

client.rgb.inflate_rgb_assets(
    asset_id="rgb:CJkb4YZw-jRiz2sk-~PARPio-wtVYI1c-XAEYCqO-wTfvRZ8",
    inflation_amounts=[
        100,
        50
    ],
    fee_rate=5,
    min_confirmations=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inflation_amounts:** `typing.List[int]` 
    
</dd>
</dl>

<dl>
<dd>

**fee_rate:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**min_confirmations:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.rgb.<a href="src/fern/rgb/client.py">issue_an_rgb_cfa_asset</a>(...) -> IssueAssetCfaResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Issue an RGB CFA asset. To provide a media first call the /postassetmedia API.
</dd>
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

client.rgb.issue_an_rgb_cfa_asset(
    amounts=[
        1000,
        600
    ],
    name="Tether",
    precision=0,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**amounts:** `typing.List[int]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**precision:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**details:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**file_digest:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.rgb.<a href="src/fern/rgb/client.py">issue_an_rgb_ifa_asset</a>(...) -> IssueAssetIfaResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Issue an RGB IFA asset
</dd>
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

client.rgb.issue_an_rgb_ifa_asset(
    amounts=[
        1000,
        600
    ],
    inflation_amounts=[
        100,
        50
    ],
    ticker="USDT",
    name="Tether",
    precision=0,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**amounts:** `typing.List[int]` 
    
</dd>
</dl>

<dl>
<dd>

**inflation_amounts:** `typing.List[int]` 
    
</dd>
</dl>

<dl>
<dd>

**ticker:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**precision:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**reject_list_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.rgb.<a href="src/fern/rgb/client.py">issue_an_rgb_nia_asset</a>(...) -> IssueAssetNiaResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Issue an RGB NIA asset
</dd>
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

client.rgb.issue_an_rgb_nia_asset(
    amounts=[
        1000,
        600
    ],
    ticker="USDT",
    name="Tether",
    precision=0,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**amounts:** `typing.List[int]` 
    
</dd>
</dl>

<dl>
<dd>

**ticker:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**precision:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.rgb.<a href="src/fern/rgb/client.py">issue_an_rgb_uda_asset</a>(...) -> IssueAssetUdaResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Issue an RGB UDA asset. To provide a media first call the /postassetmedia API.
</dd>
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

client.rgb.issue_an_rgb_uda_asset(
    ticker="UNI",
    name="Unique",
    precision=0,
    attachments_file_digests=[
        "5891b5b522d5df086d0ff0b110fbd9d21bb4fc7163af34d08286a2e846f6be03",
        "d7516e3a27cdf35aa9dcb323b5f556344ef7f57570be30b88de2bfd4ba339b1a"
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

**ticker:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**precision:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**attachments_file_digests:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**details:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**media_file_digest:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.rgb.<a href="src/fern/rgb/client.py">list_assets</a>(...) -> ListAssetsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the node's RGB assets
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AssetSchema
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.rgb.list_assets(
    filter_asset_schemas=[
        AssetSchema.NIA,
        AssetSchema.UDA,
        AssetSchema.CFA,
        AssetSchema.IFA
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

**filter_asset_schemas:** `typing.List[AssetSchema]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.rgb.<a href="src/fern/rgb/client.py">list_transfers</a>(...) -> ListTransfersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the node's on-chain RGB transfers
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AssetFilter_AnyOrNone
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.rgb.list_transfers(
    asset_filter=AssetFilter_AnyOrNone(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_filter:** `AssetFilter` 
    
</dd>
</dl>

<dl>
<dd>

**txid:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.rgb.<a href="src/fern/rgb/client.py">post_an_asset_media</a>(...) -> PostAssetMediaResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Save the provided media
</dd>
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

client.rgb.post_an_asset_media(
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.rgb.<a href="src/fern/rgb/client.py">provide_an_out_of_band_ack</a>(...) -> ProvideOutOfBandAckResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Record the out-of-band ACK received from a recipient of an outgoing transfer
</dd>
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

client.rgb.provide_an_out_of_band_ack(
    recipient_id="utxob:2Bwv2Vx-t7VD8XjTh-9EMbpBFKh-J5HDFY4pj-eywu4tKKk-hjTvzJa",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**recipient_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.rgb.<a href="src/fern/rgb/client.py">provide_an_out_of_band_consignment</a>(...) -> ProvideOutOfBandConsignmentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provide a consignment received out-of-band, as a binary upload, along with any media files it references (one `media` field per file) The consignment is validated and the matching incoming transfer(s) are processed.
</dd>
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

client.rgb.provide_an_out_of_band_consignment(
    file="example_file",
    media=["example_media"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**media:** `typing.Optional[typing.List[core.File]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.rgb.<a href="src/fern/rgb/client.py">refresh_transfers</a>(...) -> RefreshResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Refresh RGB pending transfers
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, RefreshFilter, RefreshTransferStatus
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.rgb.refresh_transfers(
    filter=[
        RefreshFilter(
            status=RefreshTransferStatus.WAITING_COUNTERPARTY,
            incoming=True,
        )
    ],
    skip_sync=False,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filter:** `typing.List[RefreshFilter]` 
    
</dd>
</dl>

<dl>
<dd>

**skip_sync:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**asset_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.rgb.<a href="src/fern/rgb/client.py">get_an_rgb_invoice</a>(...) -> RgbInvoiceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an RGB invoice to receive assets on-chain
</dd>
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

client.rgb.get_an_rgb_invoice(
    min_confirmations=1,
    expiration_timestamp=1695811760,
    witness=False,
    transport_endpoints=[
        "rpc://127.0.0.1:3000/json-rpc"
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

**min_confirmations:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**expiration_timestamp:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**witness:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**transport_endpoints:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**asset_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**assignment:** `typing.Optional[Assignment]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.rgb.<a href="src/fern/rgb/client.py">send_rgb_assets</a>(...) -> SendRgbResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send RGB assets on-chain, supporting batch transfers to multiple recipients and/or multiple assets in a single transaction
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Recipient, Assignment_Fungible
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.rgb.send_rgb_assets(
    donation=False,
    fee_rate=5,
    min_confirmations=1,
    expiration_timestamp=1695811760,
    recipient_map={
        "rgb:CJkb4YZw-jRiz2sk-~PARPio-wtVYI1c-XAEYCqO-wTfvRZ8": [
            Recipient(
                recipient_id="utxob:2FjRqgQ-eEWCVHY5-zmpFtYzT-gGm3MdR-sTnxNcS-7RtUbY9-4NYuuh",
                assignment=Assignment_Fungible(
                    value=42,
                ),
                transport_endpoints=[
                    "rpc://127.0.0.1:3000/json-rpc"
                ],
            ),
            Recipient(
                recipient_id="utxob:3GkRrhR-fFXDLIZ6-0anqGuzU-hHn4NeS-tUoyOdT-8SuVcZ0-5OZvvi",
                assignment=Assignment_Fungible(
                    value=42,
                ),
                transport_endpoints=[
                    "rpc://127.0.0.1:3000/json-rpc"
                ],
            )
        ],
        "rgb:d8qDVS5X-ICVG2uM-CPr3yO4-lfBhgjt-7FN1EPE-ApY1LcM": [
            Recipient(
                recipient_id="utxob:4HlSsiS-gGYEMKA7-1borHvaV-iIo5OfT-uVpzPeU-9TvWdA1-6PAwwj",
                assignment=Assignment_Fungible(
                    value=42,
                ),
                transport_endpoints=[
                    "rpc://127.0.0.1:3000/json-rpc"
                ],
            )
        ]
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

**donation:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**fee_rate:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**min_confirmations:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**expiration_timestamp:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**recipient_map:** `typing.Dict[str, typing.List[Recipient]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.rgb.<a href="src/fern/rgb/client.py">sync_the_rgb_wallet</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sync the RGB wallet
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SyncOptions, SyncKeychainZero, SyncStrategy
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.rgb.sync_the_rgb_wallet(
    options=SyncOptions(
        keychain=SyncKeychainZero.COLORED,
        strategy=SyncStrategy.FAST_SYNC,
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

**options:** `SyncOptions` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Other
<details><summary><code>client.other.<a href="src/fern/other/client.py">backup_the_node</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a backup of the node's data
</dd>
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

client.other.backup_the_node(
    backup_path="/path/where/to/save/the/backup/file",
    password="nodepassword",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**backup_path:** `str` 
    
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

<details><summary><code>client.other.<a href="src/fern/other/client.py">change_the_password</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Change the node's password
</dd>
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

client.other.change_the_password(
    old_password="nodepassword",
    new_password="nodenewpassword",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**old_password:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**new_password:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.other.<a href="src/fern/other/client.py">check_an_indexer_url</a>(...) -> CheckIndexerUrlResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check the given indexer URL is valid
</dd>
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

client.other.check_an_indexer_url(
    indexer_url="127.0.0.1:50001",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**indexer_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.other.<a href="src/fern/other/client.py">check_a_proxy_endpoint</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check the given proxy endpoint is valid
</dd>
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

client.other.check_a_proxy_endpoint(
    proxy_endpoint="rpc://127.0.0.1:3000/json-rpc",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**proxy_endpoint:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.other.<a href="src/fern/other/client.py">init_the_node</a>(...) -> InitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initialize a new node, optionally providing a mnemonic. If no mnemonic is provided a new one is generated. Note that a mnemonic alone is not sufficient to recover RGB state, which also requires client-side data.
</dd>
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

client.other.init_the_node(
    password="nodepassword",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**password:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**mnemonic:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.other.<a href="src/fern/other/client.py">lock_the_node</a>() -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lock an unlocked node
</dd>
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

client.other.lock_the_node()

```
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

<details><summary><code>client.other.<a href="src/fern/other/client.py">get_network_info</a>() -> NetworkInfoResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get info on the Bitcoin network where the LN is running
</dd>
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

client.other.get_network_info()

```
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

<details><summary><code>client.other.<a href="src/fern/other/client.py">get_node_info</a>() -> NodeInfoResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the LN node's info
</dd>
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

client.other.get_node_info()

```
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

<details><summary><code>client.other.<a href="src/fern/other/client.py">restore_the_node</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restore a node from a backup file
</dd>
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

client.other.restore_the_node(
    backup_path="/path/to/the/backup/file",
    password="nodepassword",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**backup_path:** `str` 
    
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

<details><summary><code>client.other.<a href="src/fern/other/client.py">revoke_a_token</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke an authentication token
</dd>
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

client.other.revoke_a_token(
    token="EnYKDBgDIggKBggGEgIYDRIkCAASICqCgqtFMIJ1eLCM3raDzqg9UqV-6nJWzGjjJG0S5IIUGkBpF-itmppHcdcSrSCiKklz9VZT4UmIND_0RFc32Imq3bLR_Y7GYaSpJo5lJfU1cA2BG_hy7P1UN4g5jKTKS88GIiIKIAUKXrrx0Ca-rMZa537VOFw2X8q_KVQ6OC4Z0ztro0sQ",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.other.<a href="src/fern/other/client.py">send_an_onion_message</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send an onion message via the LN
</dd>
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

client.other.send_an_onion_message(
    node_ids=[
        "03b79a4bc1ec365524b4fab9a39eb133753646babb5a1da5c4bc94c53110b7795d"
    ],
    tlv_type=77,
    data="message to send",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_ids:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**tlv_type:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.other.<a href="src/fern/other/client.py">shutdown_the_node</a>() -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gracefully shutdown the node
</dd>
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

client.other.shutdown_the_node()

```
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

<details><summary><code>client.other.<a href="src/fern/other/client.py">sign_a_message</a>(...) -> SignMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sign the provided message
</dd>
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

client.other.sign_a_message(
    message="message to sign",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**message:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.other.<a href="src/fern/other/client.py">unlock_the_node</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unlock a locked node
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, LdkChainSync_BlockSync, LdkChainSyncBlockSyncConfig
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.other.unlock_the_node(
    password="nodepassword",
    ldk_chain_sync=LdkChainSync_BlockSync(
        config=LdkChainSyncBlockSyncConfig(
            bitcoind_rpc_username="user",
            bitcoind_rpc_password="password",
            bitcoind_rpc_host="localhost",
            bitcoind_rpc_port=18443,
        ),
    ),
    indexer_url="127.0.0.1:50001",
    announce_addresses=[
        "pub.addr.example.com:9735"
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

**password:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**ldk_chain_sync:** `LdkChainSync` 
    
</dd>
</dl>

<dl>
<dd>

**indexer_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**announce_addresses:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**announce_alias:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Channels
<details><summary><code>client.channels.<a href="src/fern/channels/client.py">close_a_channel</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Close a LN channel cooperatively or forcibly
</dd>
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

client.channels.close_a_channel(
    channel_id="8129afe1b1d7cf60d5e1bf4c04b09bec925ed4df5417ceee0484e24f816a105a",
    peer_pubkey="03b79a4bc1ec365524b4fab9a39eb133753646babb5a1da5c4bc94c53110b7795d",
    force=False,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**channel_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**peer_pubkey:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**force:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">get_a_channels_id</a>(...) -> GetChannelIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a channel's ID from its former temporary channel ID
</dd>
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

client.channels.get_a_channels_id(
    temporary_channel_id="a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**temporary_channel_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">list_channels</a>() -> ListChannelsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the node's LN channels
</dd>
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

client.channels.list_channels()

```
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

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">open_a_channel</a>(...) -> OpenChannelResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Open a new LN channel (RGB-enabled when both asset_id and asset_amount are specified). You can optionally provide a 32 bytes temporary channel ID as a hex-encoded string.
</dd>
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

client.channels.open_a_channel(
    peer_pubkey_and_opt_addr="03b79a4bc1ec365524b4fab9a39eb133753646babb5a1da5c4bc94c53110b7795d@localhost:9736",
    capacity_sat=30010,
    push_msat=1394000,
    public=True,
    with_anchors=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**peer_pubkey_and_opt_addr:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**capacity_sat:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**push_msat:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**public:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**with_anchors:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**asset_amount:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**asset_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**push_asset_amount:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**fee_base_msat:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**fee_proportional_millionths:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**temporary_channel_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Peers
<details><summary><code>client.peers.<a href="src/fern/peers/client.py">connect_to_a_peer</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Connect to the provided LN peer
</dd>
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

client.peers.connect_to_a_peer(
    peer_pubkey_and_addr="03b79a4bc1ec365524b4fab9a39eb133753646babb5a1da5c4bc94c53110b7795d@localhost:9736",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**peer_pubkey_and_addr:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.peers.<a href="src/fern/peers/client.py">disconnect_from_a_peer</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disconnect from the provided LN peer
</dd>
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

client.peers.disconnect_from_a_peer(
    peer_pubkey="03b79a4bc1ec365524b4fab9a39eb133753646babb5a1da5c4bc94c53110b7795d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**peer_pubkey:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.peers.<a href="src/fern/peers/client.py">list_peers</a>() -> ListPeersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the node's LN peers
</dd>
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

client.peers.list_peers()

```
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

## Invoices
<details><summary><code>client.invoices.<a href="src/fern/invoices/client.py">decode_a_ln_invoice</a>(...) -> DecodeLnInvoiceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Decode the provided LN invoice string
</dd>
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

client.invoices.decode_a_ln_invoice(
    invoice="lnbcrt30u1pjv6yzndqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qdpc280eur52luxppv6f3nnj8l6vnd9g2hnv3qv6mjhmhvlzf6327pp5tjjasx6g9dqptea3fhm6yllq5wxzycnnvp8l6wcq3d6j2uvpryuqsp5l8az8x3g8fe05dg7cmgddld3da09nfjvky8xftwsk4cj8p2l7kfq9qyysgqcqpcxqzdylzlwfnkyw3jv344x4rzwgkk53ng0fhxy5rdduk4g5tpvea8xa6rfckkza35va28xjn2tqkhgarcxep5umm4x5k56wfcdvu95eq7qzp20vrl4xz76syapsa3c09j7lg5gerkaj63llj0ark7ph8hfketn6fkqzm8laf66dhsncm23wkwm5l5377we9e8lnlknnkwje5eefkccusqm6rqt8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/fern/invoices/client.py">get_an_invoice_status</a>(...) -> InvoiceStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the status of the provided LN invoice
</dd>
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

client.invoices.get_an_invoice_status(
    invoice="lnbcrt30u1pjv6yzndqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qdpc280eur52luxppv6f3nnj8l6vnd9g2hnv3qv6mjhmhvlzf6327pp5tjjasx6g9dqptea3fhm6yllq5wxzycnnvp8l6wcq3d6j2uvpryuqsp5l8az8x3g8fe05dg7cmgddld3da09nfjvky8xftwsk4cj8p2l7kfq9qyysgqcqpcxqzdylzlwfnkyw3jv344x4rzwgkk53ng0fhxy5rdduk4g5tpvea8xa6rfckkza35va28xjn2tqkhgarcxep5umm4x5k56wfcdvu95eq7qzp20vrl4xz76syapsa3c09j7lg5gerkaj63llj0ark7ph8hfketn6fkqzm8laf66dhsncm23wkwm5l5377we9e8lnlknnkwje5eefkccusqm6rqt8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/fern/invoices/client.py">get_a_ln_invoice</a>(...) -> LnInvoiceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a LN invoice to receive a payment. The description and description_hash fields are mutually exclusive.
</dd>
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

client.invoices.get_a_ln_invoice(
    expiry_sec=420,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**expiry_sec:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**amt_msat:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**asset_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**asset_amount:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description_hash:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Swaps
<details><summary><code>client.swaps.<a href="src/fern/swaps/client.py">decode_a_swapstring</a>(...) -> DecodeSwapstringResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Decode the provided swapstring
</dd>
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

client.swaps.decode_a_swapstring(
    swapstring="30/rgb:CJkb4YZw-jRiz2sk-~PARPio-wtVYI1c-XAEYCqO-wTfvRZ8/10/rgb:icfqnK9y-wObZKTu-XJcDL98-sKbE5Mh-OuDJhiI-brRJrzE/1715896416/9d342c6ba006e24abee84a2e034a22d5e30c1f2599fb9c3574d46d3cde3d65a2",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**swapstring:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.swaps.<a href="src/fern/swaps/client.py">get_a_swap</a>(...) -> GetSwapResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a swap by its payment hash
</dd>
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

client.swaps.get_a_swap(
    payment_hash="5ca5d81b482b4015e7b14df7a27fe0a38c226273604ffd3b008b752571811938",
    taker=False,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_hash:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**taker:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.swaps.<a href="src/fern/swaps/client.py">list_swaps</a>() -> ListSwapsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the node's swaps
</dd>
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

client.swaps.list_swaps()

```
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

<details><summary><code>client.swaps.<a href="src/fern/swaps/client.py">execute_a_maker_swap</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a swap on the maker side
</dd>
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

client.swaps.execute_a_maker_swap(
    swapstring="30/rgb:CJkb4YZw-jRiz2sk-~PARPio-wtVYI1c-XAEYCqO-wTfvRZ8/10/rgb:icfqnK9y-wObZKTu-XJcDL98-sKbE5Mh-OuDJhiI-brRJrzE/1715896416/9d342c6ba006e24abee84a2e034a22d5e30c1f2599fb9c3574d46d3cde3d65a2",
    payment_secret="777a7756c620868199ed5fdc35bee4095b5709d543e5c2bf0494396bf27d2ea2",
    taker_pubkey="02270dadcd6e7ba0ef707dac72acccae1a3607453a8dd2aef36ff3be4e0d31f043",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**swapstring:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**payment_secret:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**taker_pubkey:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.swaps.<a href="src/fern/swaps/client.py">init_a_maker_swap</a>(...) -> MakerInitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Init a swap on the maker side
</dd>
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

client.swaps.init_a_maker_swap(
    qty_from=30,
    qty_to=10,
    timeout_sec=100,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**qty_from:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**qty_to:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**timeout_sec:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**from_asset:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**to_asset:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.swaps.<a href="src/fern/swaps/client.py">accept_a_swap</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Accept a swap on the taker side
</dd>
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

client.swaps.accept_a_swap(
    swapstring="30/rgb:CJkb4YZw-jRiz2sk-~PARPio-wtVYI1c-XAEYCqO-wTfvRZ8/10/rgb:icfqnK9y-wObZKTu-XJcDL98-sKbE5Mh-OuDJhiI-brRJrzE/1715896416/9d342c6ba006e24abee84a2e034a22d5e30c1f2599fb9c3574d46d3cde3d65a2",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**swapstring:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Payments
<details><summary><code>client.payments.<a href="src/fern/payments/client.py">get_a_payment</a>(...) -> GetPaymentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a payment by its payment hash
</dd>
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

client.payments.get_a_payment(
    payment_hash="5ca5d81b482b4015e7b14df7a27fe0a38c226273604ffd3b008b752571811938",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_hash:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payments.<a href="src/fern/payments/client.py">send_to_a_peer_spontaneously</a>(...) -> KeysendResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send bitcoins and RGB assets to a LN peer spontaneously (without a LN invoice)
</dd>
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

client.payments.send_to_a_peer_spontaneously(
    dest_pubkey="03b79a4bc1ec365524b4fab9a39eb133753646babb5a1da5c4bc94c53110b7795d",
    amt_msat=3000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dest_pubkey:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**amt_msat:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**asset_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**asset_amount:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payments.<a href="src/fern/payments/client.py">list_payments</a>() -> ListPaymentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the node's LN payments
</dd>
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

client.payments.list_payments()

```
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

<details><summary><code>client.payments.<a href="src/fern/payments/client.py">send_a_payment</a>(...) -> SendPaymentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Pay the provided LN invoice
</dd>
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

client.payments.send_a_payment(
    invoice="lnbcrt30u1pjv6yzndqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qdpc280eur52luxppv6f3nnj8l6vnd9g2hnv3qv6mjhmhvlzf6327pp5tjjasx6g9dqptea3fhm6yllq5wxzycnnvp8l6wcq3d6j2uvpryuqsp5l8az8x3g8fe05dg7cmgddld3da09nfjvky8xftwsk4cj8p2l7kfq9qyysgqcqpcxqzdylzlwfnkyw3jv344x4rzwgkk53ng0fhxy5rdduk4g5tpvea8xa6rfckkza35va28xjn2tqkhgarcxep5umm4x5k56wfcdvu95eq7qzp20vrl4xz76syapsa3c09j7lg5gerkaj63llj0ark7ph8hfketn6fkqzm8laf66dhsncm23wkwm5l5377we9e8lnlknnkwje5eefkccusqm6rqt8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**amt_msat:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**asset_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**asset_amount:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

