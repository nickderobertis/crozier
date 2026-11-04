# Reference
## ScorecardService
<details><summary><code>client.scorecard_service.<a href="src/fern/scorecard_service/client.py">get_five_factor_scorecard</a>(...) -> GetFiveFactorScorecardResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

PRO-gated. Requires entitlement tier >= 1.
</dd>
</dl>
</dd>
</dl>

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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.scorecard_service.get_five_factor_scorecard(
    country_code="US",
    jmespath="keys(@)",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**country_code:** `str` — ISO 3166-1 alpha-2 country code for the requested scorecard.
    
</dd>
</dl>

<dl>
<dd>

**jmespath:** `typing.Optional[str]` — Optional JMESPath expression applied server-side to project or reduce the JSON response before it is returned (mirrors the MCP jmespath argument). Invalid expressions, expressions larger than 1024 UTF-8 bytes, or projections that exceed the 256 KB output cap return HTTP 400 with a {_jmespath_error, original_keys} envelope. Grammar and worked examples: https://www.worldmonitor.app/docs/mcp-jmespath.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.scorecard_service.<a href="src/fern/scorecard_service/client.py">list_five_factor_scorecards</a>(...) -> ListFiveFactorScorecardsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

PRO-gated. Requires entitlement tier >= 1.
</dd>
</dl>
</dd>
</dl>

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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.scorecard_service.list_five_factor_scorecards(
    jmespath="keys(@)",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**jmespath:** `typing.Optional[str]` — Optional JMESPath expression applied server-side to project or reduce the JSON response before it is returned (mirrors the MCP jmespath argument). Invalid expressions, expressions larger than 1024 UTF-8 bytes, or projections that exceed the 256 KB output cap return HTTP 400 with a {_jmespath_error, original_keys} envelope. Grammar and worked examples: https://www.worldmonitor.app/docs/mcp-jmespath.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.scorecard_service.<a href="src/fern/scorecard_service/client.py">get_bloc_scorecard</a>(...) -> GetBlocScorecardResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

PRO-gated. Requires entitlement tier >= 1.
</dd>
</dl>
</dd>
</dl>

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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.scorecard_service.get_bloc_scorecard(
    preset="NATO",
    jmespath="keys(@)",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**preset:** `typing.Optional[str]` — Official bloc preset: USMCA, EU27, BRICS, GCC, ASEAN, or NATO. Values are case-sensitive. Omit when members is provided.
    
</dd>
</dl>

<dl>
<dd>

**members:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Custom list of 2-30 unique uppercase ISO 3166-1 alpha-2 members. Provide either preset or members; do not provide both.
    
</dd>
</dl>

<dl>
<dd>

**jmespath:** `typing.Optional[str]` — Optional JMESPath expression applied server-side to project or reduce the JSON response before it is returned (mirrors the MCP jmespath argument). Invalid expressions, expressions larger than 1024 UTF-8 bytes, or projections that exceed the 256 KB output cap return HTTP 400 with a {_jmespath_error, original_keys} envelope. Grammar and worked examples: https://www.worldmonitor.app/docs/mcp-jmespath.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

