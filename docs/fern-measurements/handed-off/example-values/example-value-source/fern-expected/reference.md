# Reference
## Charts
<details><summary><code>client.charts.<a href="src/fern/charts/client.py#L32-L74">upload_chart</a>(...) -> UploadChartResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A multipart text part's own example.
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

client.charts.upload_chart(
    sheet="example_sheet",
    title="title",
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

**sheet:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**revision:** `typing.Optional[str]` 
    
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

<details><summary><code>client.charts.<a href="src/fern/charts/client.py#L76-L109">print_chart</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A binary download's query parameter example.
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

client.charts.print_chart(
    chart_id="chartId",
    scale="scale",
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

**chart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**scale:** `str` 
    
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

<details><summary><code>client.charts.<a href="src/fern/charts/client.py#L111-L130">bundle_charts</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A top-level array body's media-type example on a binary download.
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
client.charts.bundle_charts(...)
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

**request:** `typing.List[str]` 
    
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

<details><summary><code>client.charts.<a href="src/fern/charts/client.py#L132-L176">set_chart_layers</a>(...) -> SetChartLayersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A scalar-or-list union property's declared example inside an array item.
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
from fern.charts import SetChartLayersRequestLayersItem

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.charts.set_chart_layers(
    chart_id="chartId",
    layers=[
        SetChartLayersRequestLayersItem(
            label="soundings",
            match="match",
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

**chart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layers:** `typing.List[SetChartLayersRequestLayersItem]` 
    
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

## Mirrors
<details><summary><code>client.mirrors.<a href="src/fern/mirrors/client.py#L29-L62">add_mirror</a>(...) -> AddMirrorResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A format uri and a pattern-only string.
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

client.mirrors.add_mirror(
    source="source",
    region="region",
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

**source:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `str` 
    
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

## Harbours
<details><summary><code>client.harbours.<a href="src/fern/harbours/client.py#L26-L59">get_berth</a>(...) -> GetBerthResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Path parameters beside one declaring an empty schema.
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

client.harbours.get_berth(
    harbour_slug="harbourSlug",
    berth_ref="berthRef",
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

**harbour_slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**berth_ref:** `typing.Any` 
    
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

## Markers
<details><summary><code>client.markers.<a href="src/fern/markers/client.py#L30-L63">place_marker</a>(...) -> PlaceMarkerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A union-typed property's declared example.
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
from fern import FernApi, BuoyMarker

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.markers.place_marker(
    marker=BuoyMarker(
        colour="colour",
        shape="shape",
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

**marker:** `PlaceMarkerRequestMarker` 
    
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

## Routes
<details><summary><code>client.routes.<a href="src/fern/routes/client.py#L29-L59">plan_routes</a>(...) -> PlanRoutesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

An array body's schema-level example.
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

client.routes.plan_routes(
    request=[
        "Mount\'s Bay",
        "Carrick Roads"
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

**request:** `typing.List[str]` 
    
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

## Drills
<details><summary><code>client.drills.<a href="src/fern/drills/client.py#L30-L67">start_drill</a>(...) -> StartDrillResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A map property's schema-level example.
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

client.drills.start_drill(
    crew="crew",
    settings={
        "night": True,
        "station": "Penlee"
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

**crew:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Dict[str, StartDrillRequestSettingsValue]` 
    
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

## Stations
<details><summary><code>client.stations.<a href="src/fern/stations/client.py#L25-L58">list_stations</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A required array query parameter's example.
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

client.stations.list_stations(
    codes=[
        "PLY",
        "FAL"
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

**codes:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
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

## Passes
<details><summary><code>client.passes.<a href="src/fern/passes/client.py#L33-L68">issue_pass</a>(...) -> IssuePassResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A media type's named example for an enum field.
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
from fern.passes import IssuePassRequestGrant

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.passes.issue_pass(
    grant=IssuePassRequestGrant.OVERNIGHT_STAY,
    holder="Kerensa",
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

**grant:** `IssuePassRequestGrant` 
    
</dd>
</dl>

<dl>
<dd>

**holder:** `str` 
    
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

<details><summary><code>client.passes.<a href="src/fern/passes/client.py#L70-L115">issue_form_pass</a>(...) -> IssueFormPassResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A form body's named example for an enum field.
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
from fern.passes import IssueFormPassRequestGrant, IssueFormPassRequestTier

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.passes.issue_form_pass(
    grant=IssueFormPassRequestGrant.OVERNIGHT_STAY,
    holder="Kerensa",
    tier=IssueFormPassRequestTier.STANDARD,
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

**grant:** `IssueFormPassRequestGrant` 
    
</dd>
</dl>

<dl>
<dd>

**holder:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tier:** `IssueFormPassRequestTier` 
    
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

## Ledger
<details><summary><code>client.ledger.<a href="src/fern/ledger/client.py#L26-L54">get_block</a>(...) -> GetBlockResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

An unsigned 64-bit integer's placeholder.
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

client.ledger.get_block(
    height=1000000,
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

**height:** `int` 
    
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

## Soundings
<details><summary><code>client.soundings.<a href="src/fern/soundings/client.py#L25-L63">list_soundings</a>(...) -> typing.List[float]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

An integer bounded by a minimum and a maximum.
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

client.soundings.list_soundings(
    depth=1,
    fathoms=1,
    cables=1,
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

**depth:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**fathoms:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**cables:** `int` 
    
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

<details><summary><code>client.soundings.<a href="src/fern/soundings/client.py#L65-L103">get_sounding_log</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bounded integers on an operation answering text.
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

client.soundings.get_sounding_log(
    depth=1024,
    fathoms=40,
    cables=5,
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

**depth:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**fathoms:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**cables:** `int` 
    
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

## Rosters
<details><summary><code>client.rosters.<a href="src/fern/rosters/client.py#L29-L71">add_roster_entry</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A required header on an operation whose body has no worked example.
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

client.rosters.add_roster_entry(
    id="id",
    watch_token="watchToken",
    request={"key": "value"},
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

**watch_token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `RosterEntry` 
    
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

## Beacons
<details><summary><code>client.beacons.<a href="src/fern/beacons/client.py#L25-L52">set_beacon_script</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

An inline path parameter's own example beside a text body.
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

client.beacons.set_beacon_script(
    beacon_code="bcn:west-4",
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

**beacon_code:** `str` 
    
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

<details><summary><code>client.beacons.<a href="src/fern/beacons/client.py#L54-L81">set_lantern_script</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A referenced path parameter's own example beside a text body.
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

client.beacons.set_lantern_script(
    lantern_code="ltn:east-2",
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

**lantern_code:** `str` 
    
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

<details><summary><code>client.beacons.<a href="src/fern/beacons/client.py#L83-L110">get_lantern_manual</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A referenced path parameter's own example beside an XML answer.
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

client.beacons.get_lantern_manual(
    lantern_code="ltn:east-2",
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

**lantern_code:** `str` 
    
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

## Galleys
<details><summary><code>client.galleys.<a href="src/fern/galleys/client.py#L29-L66">remove_galley_stores</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

An array body of referenced objects with a named example, on an operation answering text.
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
from fern import FernApi, StoreLine

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.galleys.remove_galley_stores(
    galley_id="galleyId",
    request=[
        StoreLine(),
        StoreLine()
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

**galley_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[StoreLine]` 
    
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

<details><summary><code>client.galleys.<a href="src/fern/galleys/client.py#L68-L105">append_galley_log</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A free-form map body with array named examples, on an operation answering text.
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

client.galleys.append_galley_log(
    galley_id="galleyId",
    request={
        "string": {"key": "value"}
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

**galley_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
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

<details><summary><code>client.galleys.<a href="src/fern/galleys/client.py#L107-L144">amend_galley_log</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

An array body of unknown items with an example, on an operation answering text.
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

client.galleys.amend_galley_log(
    galley_id="galleyId",
    request=[
        {"key": "value"},
        {"key": "value"}
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

**galley_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[typing.Any]` 
    
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

## Manifests
<details><summary><code>client.manifests.<a href="src/fern/manifests/client.py#L31-L72">import_manifest</a>(...) -> ImportManifestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A multipart object part whose property declares an example.
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
from fern.manifests import ImportManifestRequestTask

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.manifests.import_manifest(
    sheet="example_sheet",
    task=ImportManifestRequestTask(
        label="label",
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

**sheet:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**task:** `ImportManifestRequestTask` 
    
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

## Voyages
<details><summary><code>client.voyages.<a href="src/fern/voyages/client.py#L32-L68">set_voyage_watch</a>(...) -> SetVoyageWatchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A nested field the request example gives an empty array.
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
from fern import FernApi, WatchRota, WatchRotaCadence

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.voyages.set_voyage_watch(
    voyage_id="voyageId",
    rota=WatchRota(
        days=[
            1,
            3,
            5
        ],
        cadence=WatchRotaCadence.DAILY,
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

**voyage_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**rota:** `WatchRota` 
    
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

<details><summary><code>client.voyages.<a href="src/fern/voyages/client.py#L70-L109">plan_voyage_rota</a>(...) -> PlanVoyageRotaResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The same field left out of a referenced body's referenced named example.
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
from fern import FernApi, WatchRota, WatchRotaCadence

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.voyages.plan_voyage_rota(
    voyage_id="voyageId",
    crew="starboard",
    rota=WatchRota(
        days=[
            1,
            3,
            5
        ],
        cadence=WatchRotaCadence.DAILY,
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

**voyage_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**crew:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**rota:** `WatchRota` 
    
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

<details><summary><code>client.voyages.<a href="src/fern/voyages/client.py#L111-L157">file_customs_stamps</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

An array body of a referenced schema whose schema-level example writes unquoted YAML timestamps, on an int64 field and on a date-time field.
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
from fern import FernApi, CustomsStamp
import datetime

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.voyages.file_customs_stamps(
    voyage_id="voyageId",
    request=[
        CustomsStamp(
            port="Falmouth",
            punched_millis=1000000,
            inked_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
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

**voyage_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[CustomsStamp]` 
    
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

