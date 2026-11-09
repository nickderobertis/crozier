# Reference
## Dashboards
<details><summary><code>client.dashboards.<a href="src/fern/dashboards/client.py">list</a>(...) -> DashboardsListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a paginated list of dashboards that your account has access to.
</dd>
</dl>
</dd>
</dl>

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

client.dashboards.list(
    page_size=10,
    page_number=1,
    sort="created_at desc",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of items to include per page. The last page of a collection may include fewer items.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — Determines which page of the entities to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[DashboardFilterParameters]` — Filters dashboards in the response.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dashboards.<a href="src/fern/dashboards/client.py">create</a>(...) -> DashboardResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new dashboard from the provided definition.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Dashboard, Tile_Chart, ChartTileLayout, ChartTileLayoutPosition, ChartTileLayoutSize, ChartTileDefinition, ChartTileDefinitionQuery_ApiUsage, AdvancedFiltersItem_ControlPlane, TimeRange_Relative, Chart_Donut
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.dashboards.create(
    name="Single Tile, Timeseries Line",
    definition=Dashboard(
        tiles=[
            Tile_Chart(
                layout=ChartTileLayout(
                    position=ChartTileLayoutPosition(
                        col=3,
                        row=0,
                    ),
                    size=ChartTileLayoutSize(
                        cols=3,
                        rows=1,
                    ),
                ),
                definition=ChartTileDefinition(
                    query=ChartTileDefinitionQuery_ApiUsage(
                        metrics=[
                            "request_count",
                            "response_latency_p99"
                        ],
                        dimensions=[
                            "time",
                            "gateway_service"
                        ],
                        filters=[
                            AdvancedFiltersItem_ControlPlane(
                                operator="in",
                                value=[
                                    "d5ac5d88-efed-4e10-9dfe-0b0a6646c219"
                                ],
                            )
                        ],
                        granularity="hourly",
                        time_range=TimeRange_Relative(
                            time_range="15m",
                        ),
                    ),
                    chart=Chart_Donut(),
                ),
            )
        ],
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

**request:** `DashboardUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dashboards.<a href="src/fern/dashboards/client.py">get</a>(...) -> DashboardResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a dashboard that your account has access to.
</dd>
</dl>
</dd>
</dl>

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

client.dashboards.get(
    dashboard_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dashboard_id:** `str` — The dashboard's ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dashboards.<a href="src/fern/dashboards/client.py">update</a>(...) -> DashboardResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing dashboard, replacing its definition with the provided one.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Dashboard, Tile_Chart, ChartTileLayout, ChartTileLayoutPosition, ChartTileLayoutSize, ChartTileDefinition, ChartTileDefinitionQuery_ApiUsage, AdvancedFiltersItem_ControlPlane, TimeRange_Relative, Chart_Donut
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.dashboards.update(
    dashboard_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
    name="Single Tile, Timeseries Line",
    definition=Dashboard(
        tiles=[
            Tile_Chart(
                layout=ChartTileLayout(
                    position=ChartTileLayoutPosition(
                        col=3,
                        row=0,
                    ),
                    size=ChartTileLayoutSize(
                        cols=3,
                        rows=1,
                    ),
                ),
                definition=ChartTileDefinition(
                    query=ChartTileDefinitionQuery_ApiUsage(
                        metrics=[
                            "request_count",
                            "response_latency_p99"
                        ],
                        dimensions=[
                            "time",
                            "gateway_service"
                        ],
                        filters=[
                            AdvancedFiltersItem_ControlPlane(
                                operator="in",
                                value=[
                                    "d5ac5d88-efed-4e10-9dfe-0b0a6646c219"
                                ],
                            )
                        ],
                        granularity="hourly",
                        time_range=TimeRange_Relative(
                            time_range="15m",
                        ),
                    ),
                    chart=Chart_Donut(),
                ),
            )
        ],
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

**dashboard_id:** `str` — The dashboard's ID.
    
</dd>
</dl>

<dl>
<dd>

**request:** `DashboardUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dashboards.<a href="src/fern/dashboards/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an existing dashboard.
</dd>
</dl>
</dd>
</dl>

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

client.dashboards.delete(
    dashboard_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dashboard_id:** `str` — The dashboard's ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

