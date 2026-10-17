# Reference
## Query
<details><summary><code>client.query.<a href="src/fern/query/client.py">get_thermo_metrics</a>(...) -> GetThermoMetricsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Query thermometer metrics data from time series database
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.query.get_thermo_metrics(
    system_id="system_id",
    time_start={"key": "value"},
    time_end={"key": "value"},
    interval=1.1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**system_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**time_start:** `GetThermoMetricsRequestTimeStart` 
    
</dd>
</dl>

<dl>
<dd>

**time_end:** `GetThermoMetricsRequestTimeEnd` 
    
</dd>
</dl>

<dl>
<dd>

**interval:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**channels:** `typing.Optional[typing.Union[float, typing.Sequence[float]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.query.<a href="src/fern/query/client.py">get_heater_metrics</a>(...) -> GetHeaterMetricsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Query heater metrics data from time series database
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.query.get_heater_metrics(
    system_id="system_id",
    time_start={"key": "value"},
    time_end={"key": "value"},
    interval=1.1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**system_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**time_start:** `GetHeaterMetricsRequestTimeStart` 
    
</dd>
</dl>

<dl>
<dd>

**time_end:** `GetHeaterMetricsRequestTimeEnd` 
    
</dd>
</dl>

<dl>
<dd>

**interval:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**channels:** `typing.Optional[typing.Union[float, typing.Sequence[float]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Scrape
<details><summary><code>client.scrape.<a href="src/fern/scrape/client.py">get_all_scrape_metrics</a>() -> typing.List[GetAllScrapeMetricsResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve scraping metrics for all active systems, including per-system error counts and success totals
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.scrape.get_all_scrape_metrics()

```
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

<details><summary><code>client.scrape.<a href="src/fern/scrape/client.py">get_system_scrape_metrics</a>(...) -> GetSystemScrapeMetricsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve scraping metrics for a specific system by its ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.scrape.get_system_scrape_metrics(
    system_id="systemId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**system_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.scrape.<a href="src/fern/scrape/client.py">get_all_scrape_status</a>() -> typing.List[GetAllScrapeStatusResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve windowed scrape status (success/error counts in last 1m, 10m, and since start) for all active systems
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.scrape.get_all_scrape_status()

```
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

<details><summary><code>client.scrape.<a href="src/fern/scrape/client.py">get_system_scrape_status</a>(...) -> GetSystemScrapeStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve windowed scrape status for a specific system by its ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.scrape.get_system_scrape_status(
    system_id="systemId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**system_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Systems
<details><summary><code>client.systems.<a href="src/fern/systems/client.py">list_systems</a>() -> typing.List[ListSystemsResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all registered systems with their thermometers and heaters
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.systems.list_systems()

```
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

<details><summary><code>client.systems.<a href="src/fern/systems/client.py">create_system</a>(...) -> CreateSystemResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Register a new system with thermometers and heaters
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.systems import CreateSystemRequestThermosItem, CreateSystemRequestHeatersItem

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.systems.create_system(
    id="id",
    display_name="displayName",
    thermo_url="thermoUrl",
    heater_url="heaterUrl",
    thermos=[
        CreateSystemRequestThermosItem(
            channel=1.1,
        )
    ],
    heaters=[
        CreateSystemRequestHeatersItem(
            channel=1.1,
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

**id:** `str` — Unique system slug
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `str` — Human-readable name
    
</dd>
</dl>

<dl>
<dd>

**thermo_url:** `str` — Base URL to thermo/ls-api
    
</dd>
</dl>

<dl>
<dd>

**heater_url:** `str` — Base URL to heater-api
    
</dd>
</dl>

<dl>
<dd>

**thermos:** `typing.List[CreateSystemRequestThermosItem]` 
    
</dd>
</dl>

<dl>
<dd>

**heaters:** `typing.List[CreateSystemRequestHeatersItem]` 
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[str]` — Physical location
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.systems.<a href="src/fern/systems/client.py">get_system</a>(...) -> GetSystemResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single system by ID with its thermometers and heaters
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.systems.get_system(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.systems.<a href="src/fern/systems/client.py">update_system</a>(...) -> UpdateSystemResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing system. Thermos/heaters are replaced if provided.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.systems.update_system(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**thermo_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**heater_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**thermos:** `typing.Optional[typing.List[UpdateSystemRequestThermosItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**heaters:** `typing.Optional[typing.List[UpdateSystemRequestHeatersItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.systems.<a href="src/fern/systems/client.py">delete_system</a>(...) -> DeleteSystemResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a system and all its associated thermometers and heaters
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.systems.delete_system(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Experiments
<details><summary><code>client.experiments.<a href="src/fern/experiments/client.py">list_experiments</a>(...) -> ListExperimentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List experiments with optional filters by system, channel, status, name, and start-time range. Sorted by startedAt desc.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.experiments.list_experiments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**system_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**channel:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListExperimentsRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**name_contains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**started_after:** `typing.Optional[ListExperimentsRequestStartedAfter]` 
    
</dd>
</dl>

<dl>
<dd>

**started_before:** `typing.Optional[ListExperimentsRequestStartedBefore]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.experiments.<a href="src/fern/experiments/client.py">start_experiment</a>(...) -> StartExperimentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an experiment and start the PID loop. Captures setpoint and Kp/Ki/Kd as the experiment's start snapshot. Refuses if PID is already active or another experiment is running on the same channel.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.experiments.start_experiment(
    name="name",
    system_id="systemId",
    channel=1.1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Experiment name
    
</dd>
</dl>

<dl>
<dd>

**system_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**channel:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.experiments.<a href="src/fern/experiments/client.py">get_active_experiment</a>(...) -> GetActiveExperimentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the currently running experiment for a given (systemId, channel), or null if none.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.experiments.get_active_experiment(
    system_id="systemId",
    channel=1.1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**system_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**channel:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.experiments.<a href="src/fern/experiments/client.py">get_experiment</a>(...) -> GetExperimentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single experiment by id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.experiments.get_experiment(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.experiments.<a href="src/fern/experiments/client.py">delete_experiment</a>(...) -> DeleteExperimentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a non-running experiment. Refuses to delete a running one.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.experiments.delete_experiment(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.experiments.<a href="src/fern/experiments/client.py">update_experiment</a>(...) -> UpdateExperimentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an experiment's name or notes (no other fields).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.experiments.update_experiment(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.experiments.<a href="src/fern/experiments/client.py">stop_experiment</a>(...) -> StopExperimentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stop a running experiment. Calls the heater PID stop endpoint and finalizes the experiment row.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.experiments.stop_experiment(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

