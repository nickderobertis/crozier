# Reference
## Risk Coverages
<details><summary><code>client.risk_coverages.<a href="src/fern/risk_coverages/client.py">get_pension_risk_coverages</a>(...) -> OkResponseRiskCoveragePension</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Método para obter informações de Previdência de Cobertura de Riscos.
</dd>
</dl>
</dd>
</dl>

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

client.risk_coverages.get_pension_risk_coverages()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Número da página que está sendo requisitada (o valor da primeira página é 1).
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Quantidade total de registros por páginas.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Survival Coverages
<details><summary><code>client.survival_coverages.<a href="src/fern/survival_coverages/client.py">get_pension_survival_coverages</a>(...) -> OkResponseSurvivalCoveragePension</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Método para obter informações de Previdência de Cobertura de Sobrevivência.
</dd>
</dl>
</dd>
</dl>

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

client.survival_coverages.get_pension_survival_coverages()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Número da página que está sendo requisitada (o valor da primeira página é 1).
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Quantidade total de registros por páginas.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

