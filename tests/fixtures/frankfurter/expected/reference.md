# Reference
<details><summary><code>client.<a href="src/fern/client.py">get_rates</a>(...) -> typing.List[Rate]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns exchange rates blended across providers. Without date params, returns the latest rates. Each record is a single currency pair. The response includes an identity record for the base currency (base equals quote, rate 1), subject to the quotes filter like any other record.
</dd>
</dl>
</dd>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_rates(
    date=datetime.date.fromisoformat("2024-01-15"),
    from_=datetime.date.fromisoformat("2024-01-01"),
    to=datetime.date.fromisoformat("2024-01-31"),
    base="USD",
    quotes="USD,GBP,JPY",
    providers="ECB,TCMB",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**date:** `typing.Optional[datetime.date]` — Specific date (YYYY-MM-DD). Cannot be combined with from/to.
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[datetime.date]` — Start of date range (YYYY-MM-DD)
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[datetime.date]` — End of date range (YYYY-MM-DD). Defaults to today.
    
</dd>
</dl>

<dl>
<dd>

**base:** `typing.Optional[str]` — Base currency (default: EUR)
    
</dd>
</dl>

<dl>
<dd>

**quotes:** `typing.Optional[str]` — Comma-separated list of quote currencies to include
    
</dd>
</dl>

<dl>
<dd>

**providers:** `typing.Optional[str]` — Comma-separated list of data providers to include
    
</dd>
</dl>

<dl>
<dd>

**group:** `typing.Optional[GetRatesRequestGroup]` — Downsample rates by time period. Only applies to date ranges.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[GetRatesRequestExpand]` — Comma-separated list of optional fields to include per record. Currently supports `providers`, which adds an array of `{ key, date, rate }` objects per record showing each provider's individual observation date and rate. Outliers excluded from the blend (and providers whose rate was overridden by a currency peg) are flagged with `excluded: true`. The field is omitted on synthesized peg rows where no provider published the quote. In CSV output, the `providers` column is encoded as `KEY:RATE` pairs joined by `|`, with a trailing `*` on excluded entries (e.g. `ECB:0.92|FED:1.50*`).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_rate</a>(...) -> Rate</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the blended exchange rate for a single currency pair. Without a date param, returns the latest rate. A same-currency pair returns the identity rate of 1.
</dd>
</dl>
</dd>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_rate(
    base="EUR",
    quote="USD",
    date=datetime.date.fromisoformat("2024-01-15"),
    providers="ECB,TCMB",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**base:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**quote:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**date:** `typing.Optional[datetime.date]` — Specific date (YYYY-MM-DD). Cannot be combined with from/to.
    
</dd>
</dl>

<dl>
<dd>

**providers:** `typing.Optional[str]` — Comma-separated list of data providers to include
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_currency</a>(...) -> CurrencyDetail</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details for a single currency, including provider information or peg metadata.
</dd>
</dl>
</dd>
</dl>

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

client.get_currency(
    code="USD",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**code:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_currencies</a>(...) -> typing.List[Currency]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns available currencies with their names and date ranges. By default, only active currencies are included.
</dd>
</dl>
</dd>
</dl>

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

client.get_currencies(
    providers="ECB,TCMB",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scope:** `typing.Optional[GetCurrenciesRequestScope]` — Set to 'all' to include legacy currencies
    
</dd>
</dl>

<dl>
<dd>

**providers:** `typing.Optional[str]` — Comma-separated list of data providers to include
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_providers</a>() -> typing.List[Provider]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns available exchange rate data providers with their base currency.
</dd>
</dl>
</dd>
</dl>

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

client.get_providers()

```
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

