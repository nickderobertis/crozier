# Reference
<details><summary><code>client.<a href="src/fern/client.py">favico_favicon_ico_get</a>() -> typing.Any</code></summary>
<dl>
<dd>

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

client.favico_favicon_ico_get()

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

<details><summary><code>client.<a href="src/fern/client.py">pong_ping_get</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sanity check.
This will let the user know that the service is operational.
And this path operation will:
* show a lifesign
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

client.pong_ping_get()

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

## V1
<details><summary><code>client.v1.<a href="src/fern/v1/client.py">cities_getv1</a>(...) -> OpenAqCitiesResult</code></summary>
<dl>
<dd>

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

client.v1.cities_getv1()

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

**limit:** `typing.Optional[int]` — Change the number of results returned.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Paginate through results.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[Sort]` — Define sort order.
    
</dd>
</dl>

<dl>
<dd>

**country_id:** `typing.Optional[str]` 


        Limit results by a certain country using two letter country code.
        (ex. /US)
        
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 


        Limit results by a certain country using two letter country code.
        (ex. ?country=US or ?country=US&country=MX)
        
    
</dd>
</dl>

<dl>
<dd>

**city:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 


        Limit results by a certain city or cities.
        (ex. ?city=Chicago or ?city=Chicago&city=Boston)
        
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[CitiesOrder]` — Order by a field
    
</dd>
</dl>

<dl>
<dd>

**entity:** `typing.Optional[str]` 
    
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

<details><summary><code>client.v1.<a href="src/fern/v1/client.py">countries_getv1</a>(...) -> OpenAqCountriesResult</code></summary>
<dl>
<dd>

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

client.v1.countries_getv1()

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

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Paginate through results.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[Sort]` — Define sort order.
    
</dd>
</dl>

<dl>
<dd>

**country_id:** `typing.Optional[str]` 


        Limit results by a certain country using two letter country code.
        (ex. /US)
        
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 


        Limit results by a certain country using two letter country code.
        (ex. ?country=US or ?country=US&country=MX)
        
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[CountriesOrder]` 
    
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

<details><summary><code>client.v1.<a href="src/fern/v1/client.py">countries_get</a>(...) -> OpenAqCountriesResult</code></summary>
<dl>
<dd>

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

client.v1.countries_get(
    country_id="country_id",
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

**country_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Paginate through results.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[Sort]` — Define sort order.
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 


        Limit results by a certain country using two letter country code.
        (ex. ?country=US or ?country=US&country=MX)
        
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[CountriesOrder]` 
    
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

<details><summary><code>client.v1.<a href="src/fern/v1/client.py">latest_v1get</a>(...) -> OpenAqResult</code></summary>
<dl>
<dd>

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

client.v1.latest_v1get(
    location_id=1,
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

**location_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Change the number of results returned.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Paginate through results.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[Sort]` — Sort Direction
    
</dd>
</dl>

<dl>
<dd>

**has_geo:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**parameter_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**parameter:** `typing.Optional[typing.Union[LatestV1GetV1LatestLocationIdGetRequestParameterItem, typing.Sequence[LatestV1GetV1LatestLocationIdGetRequestParameterItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**unit:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**coordinates:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**radius:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**country_id:** `typing.Optional[str]` 


        Limit results by a certain country using two letter country code.
        (ex. /US)
        
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 


        Limit results by a certain country using two letter country code.
        (ex. ?country=US or ?country=US&country=MX)
        
    
</dd>
</dl>

<dl>
<dd>

**city:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 


        Limit results by a certain city or cities.
        (ex. ?city=Chicago or ?city=Chicago&city=Boston)
        
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[typing.Union[LatestV1GetV1LatestLocationIdGetRequestLocationItem, typing.Sequence[LatestV1GetV1LatestLocationIdGetRequestLocationItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[LocationsOrder]` — Order by a field
    
</dd>
</dl>

<dl>
<dd>

**is_mobile:** `typing.Optional[bool]` — Location is mobile
    
</dd>
</dl>

<dl>
<dd>

**is_analysis:** `typing.Optional[bool]` — Data is the product of a previous analysis/aggregation and not raw measurements
    
</dd>
</dl>

<dl>
<dd>

**source_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Name of the data source
    
</dd>
</dl>

<dl>
<dd>

**entity:** `typing.Optional[EntityTypes]` — Source entity type.
    
</dd>
</dl>

<dl>
<dd>

**sensor_type:** `typing.Optional[SensorTypes]` — Type of Sensor
    
</dd>
</dl>

<dl>
<dd>

**model_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Model Name of Sensor
    
</dd>
</dl>

<dl>
<dd>

**manufacturer_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Manufacturer of Sensor
    
</dd>
</dl>

<dl>
<dd>

**dump_raw:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.v1.<a href="src/fern/v1/client.py">locationsv1get</a>(...) -> OpenAqResult</code></summary>
<dl>
<dd>

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

client.v1.locationsv1get(
    location_id=1,
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

**location_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Change the number of results returned.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Paginate through results.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[Sort]` — Sort Direction
    
</dd>
</dl>

<dl>
<dd>

**has_geo:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**parameter_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**parameter:** `typing.Optional[typing.Union[Locationsv1GetV1LocationsLocationIdGetRequestParameterItem, typing.Sequence[Locationsv1GetV1LocationsLocationIdGetRequestParameterItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**unit:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**coordinates:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**radius:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**country_id:** `typing.Optional[str]` 


        Limit results by a certain country using two letter country code.
        (ex. /US)
        
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 


        Limit results by a certain country using two letter country code.
        (ex. ?country=US or ?country=US&country=MX)
        
    
</dd>
</dl>

<dl>
<dd>

**city:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 


        Limit results by a certain city or cities.
        (ex. ?city=Chicago or ?city=Chicago&city=Boston)
        
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[typing.Union[Locationsv1GetV1LocationsLocationIdGetRequestLocationItem, typing.Sequence[Locationsv1GetV1LocationsLocationIdGetRequestLocationItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[LocationsOrder]` — Order by a field
    
</dd>
</dl>

<dl>
<dd>

**is_mobile:** `typing.Optional[bool]` — Location is mobile
    
</dd>
</dl>

<dl>
<dd>

**is_analysis:** `typing.Optional[bool]` — Data is the product of a previous analysis/aggregation and not raw measurements
    
</dd>
</dl>

<dl>
<dd>

**source_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Name of the data source
    
</dd>
</dl>

<dl>
<dd>

**entity:** `typing.Optional[EntityTypes]` — Source entity type.
    
</dd>
</dl>

<dl>
<dd>

**sensor_type:** `typing.Optional[SensorTypes]` — Type of Sensor
    
</dd>
</dl>

<dl>
<dd>

**model_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Model Name of Sensor
    
</dd>
</dl>

<dl>
<dd>

**manufacturer_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Manufacturer of Sensor
    
</dd>
</dl>

<dl>
<dd>

**dump_raw:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.v1.<a href="src/fern/v1/client.py">measurements_get_v1</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

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

client.v1.measurements_get_v1()

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

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**date_from:** `typing.Optional[MeasurementsGetV1V1MeasurementsGetRequestDateFrom]` 
    
</dd>
</dl>

<dl>
<dd>

**date_to:** `typing.Optional[MeasurementsGetV1V1MeasurementsGetRequestDateTo]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Change the number of results returned.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Paginate through results.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[Sort]` 
    
</dd>
</dl>

<dl>
<dd>

**has_geo:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**parameter_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**parameter:** `typing.Optional[typing.Union[MeasurementsGetV1V1MeasurementsGetRequestParameterItem, typing.Sequence[MeasurementsGetV1V1MeasurementsGetRequestParameterItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**unit:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**coordinates:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**radius:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**country_id:** `typing.Optional[str]` 


        Limit results by a certain country using two letter country code.
        (ex. /US)
        
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 


        Limit results by a certain country using two letter country code.
        (ex. ?country=US or ?country=US&country=MX)
        
    
</dd>
</dl>

<dl>
<dd>

**city:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 


        Limit results by a certain city or cities.
        (ex. ?city=Chicago or ?city=Chicago&city=Boston)
        
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[typing.Union[MeasurementsGetV1V1MeasurementsGetRequestLocationItem, typing.Sequence[MeasurementsGetV1V1MeasurementsGetRequestLocationItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[MeasOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**is_mobile:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**is_analysis:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**project:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**entity:** `typing.Optional[EntityTypes]` 
    
</dd>
</dl>

<dl>
<dd>

**sensor_type:** `typing.Optional[SensorTypes]` 
    
</dd>
</dl>

<dl>
<dd>

**value_from:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**value_to:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[str]` 
    
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

<details><summary><code>client.v1.<a href="src/fern/v1/client.py">parameters_getv1</a>(...) -> OpenAqParametersResult</code></summary>
<dl>
<dd>

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

client.v1.parameters_getv1()

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

**limit:** `typing.Optional[int]` — Change the number of results returned.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Paginate through results.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[Sort]` — Define sort order.
    
</dd>
</dl>

<dl>
<dd>

**source_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` 
    
</dd>
</dl>

<dl>
<dd>

**source_slug:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` 
    
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

<details><summary><code>client.v1.<a href="src/fern/v1/client.py">sources_v1get</a>(...) -> OpenAqResult</code></summary>
<dl>
<dd>

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

client.v1.sources_v1get()

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

**limit:** `typing.Optional[int]` — Change the number of results returned.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Paginate through results.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[Sort]` — Define sort order.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[SourcesV1Order]` 
    
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

## V2
<details><summary><code>client.v2.<a href="src/fern/v2/client.py">averages_v2get</a>(...) -> OpenAqResult</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Spatial, Temporal
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.v2.averages_v2get(
    spatial=Spatial.COUNTRY,
    temporal=Temporal.DAY,
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

**spatial:** `Spatial` 
    
</dd>
</dl>

<dl>
<dd>

**temporal:** `Temporal` 
    
</dd>
</dl>

<dl>
<dd>

**date_from:** `typing.Optional[AveragesV2GetV2AveragesGetRequestDateFrom]` 
    
</dd>
</dl>

<dl>
<dd>

**date_to:** `typing.Optional[AveragesV2GetV2AveragesGetRequestDateTo]` 
    
</dd>
</dl>

<dl>
<dd>

**parameter_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**parameter:** `typing.Optional[typing.Union[AveragesV2GetV2AveragesGetRequestParameterItem, typing.Sequence[AveragesV2GetV2AveragesGetRequestParameterItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**unit:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**project:** `typing.Optional[typing.Union[AveragesV2GetV2AveragesGetRequestProjectItem, typing.Sequence[AveragesV2GetV2AveragesGetRequestProjectItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**country_id:** `typing.Optional[str]` 


        Limit results by a certain country using two letter country code.
        (ex. /US)
        
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 


        Limit results by a certain country using two letter country code.
        (ex. ?country=US or ?country=US&country=MX)
        
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Change the number of results returned.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Paginate through results.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[Sort]` — Define sort order.
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**group:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.v2.<a href="src/fern/v2/client.py">cities_get</a>(...) -> OpenAqCitiesResult</code></summary>
<dl>
<dd>

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

client.v2.cities_get()

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

**limit:** `typing.Optional[int]` — Change the number of results returned.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Paginate through results.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[Sort]` — Define sort order.
    
</dd>
</dl>

<dl>
<dd>

**country_id:** `typing.Optional[str]` 


        Limit results by a certain country using two letter country code.
        (ex. /US)
        
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 


        Limit results by a certain country using two letter country code.
        (ex. ?country=US or ?country=US&country=MX)
        
    
</dd>
</dl>

<dl>
<dd>

**city:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 


        Limit results by a certain city or cities.
        (ex. ?city=Chicago or ?city=Chicago&city=Boston)
        
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[CitiesOrder]` — Order by a field
    
</dd>
</dl>

<dl>
<dd>

**entity:** `typing.Optional[str]` 
    
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

<details><summary><code>client.v2.<a href="src/fern/v2/client.py">countries_get</a>(...) -> OpenAqCountriesResult</code></summary>
<dl>
<dd>

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

client.v2.countries_get(
    country_id="country_id",
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

**country_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Paginate through results.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[Sort]` — Define sort order.
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 


        Limit results by a certain country using two letter country code.
        (ex. ?country=US or ?country=US&country=MX)
        
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[CountriesOrder]` 
    
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

<details><summary><code>client.v2.<a href="src/fern/v2/client.py">latest_get</a>(...) -> OpenAqResult</code></summary>
<dl>
<dd>

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

client.v2.latest_get(
    location_id=1,
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

**location_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Change the number of results returned.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Paginate through results.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[Sort]` — Sort Direction
    
</dd>
</dl>

<dl>
<dd>

**has_geo:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**parameter_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**parameter:** `typing.Optional[typing.Union[LatestGetV2LatestLocationIdGetRequestParameterItem, typing.Sequence[LatestGetV2LatestLocationIdGetRequestParameterItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**unit:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**coordinates:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**radius:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**country_id:** `typing.Optional[str]` 


        Limit results by a certain country using two letter country code.
        (ex. /US)
        
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 


        Limit results by a certain country using two letter country code.
        (ex. ?country=US or ?country=US&country=MX)
        
    
</dd>
</dl>

<dl>
<dd>

**city:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 


        Limit results by a certain city or cities.
        (ex. ?city=Chicago or ?city=Chicago&city=Boston)
        
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[typing.Union[LatestGetV2LatestLocationIdGetRequestLocationItem, typing.Sequence[LatestGetV2LatestLocationIdGetRequestLocationItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[LocationsOrder]` — Order by a field
    
</dd>
</dl>

<dl>
<dd>

**is_mobile:** `typing.Optional[bool]` — Location is mobile
    
</dd>
</dl>

<dl>
<dd>

**is_analysis:** `typing.Optional[bool]` — Data is the product of a previous analysis/aggregation and not raw measurements
    
</dd>
</dl>

<dl>
<dd>

**source_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Name of the data source
    
</dd>
</dl>

<dl>
<dd>

**entity:** `typing.Optional[EntityTypes]` — Source entity type.
    
</dd>
</dl>

<dl>
<dd>

**sensor_type:** `typing.Optional[SensorTypes]` — Type of Sensor
    
</dd>
</dl>

<dl>
<dd>

**model_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Model Name of Sensor
    
</dd>
</dl>

<dl>
<dd>

**manufacturer_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Manufacturer of Sensor
    
</dd>
</dl>

<dl>
<dd>

**dump_raw:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.v2.<a href="src/fern/v2/client.py">locations_get</a>(...) -> OpenAqResult</code></summary>
<dl>
<dd>

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

client.v2.locations_get(
    location_id=1,
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

**location_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Change the number of results returned.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Paginate through results.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[Sort]` — Sort Direction
    
</dd>
</dl>

<dl>
<dd>

**has_geo:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**parameter_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**parameter:** `typing.Optional[typing.Union[LocationsGetV2LocationsLocationIdGetRequestParameterItem, typing.Sequence[LocationsGetV2LocationsLocationIdGetRequestParameterItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**unit:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**coordinates:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**radius:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**country_id:** `typing.Optional[str]` 


        Limit results by a certain country using two letter country code.
        (ex. /US)
        
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 


        Limit results by a certain country using two letter country code.
        (ex. ?country=US or ?country=US&country=MX)
        
    
</dd>
</dl>

<dl>
<dd>

**city:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 


        Limit results by a certain city or cities.
        (ex. ?city=Chicago or ?city=Chicago&city=Boston)
        
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[typing.Union[LocationsGetV2LocationsLocationIdGetRequestLocationItem, typing.Sequence[LocationsGetV2LocationsLocationIdGetRequestLocationItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[LocationsOrder]` — Order by a field
    
</dd>
</dl>

<dl>
<dd>

**is_mobile:** `typing.Optional[bool]` — Location is mobile
    
</dd>
</dl>

<dl>
<dd>

**is_analysis:** `typing.Optional[bool]` — Data is the product of a previous analysis/aggregation and not raw measurements
    
</dd>
</dl>

<dl>
<dd>

**source_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Name of the data source
    
</dd>
</dl>

<dl>
<dd>

**entity:** `typing.Optional[EntityTypes]` — Source entity type.
    
</dd>
</dl>

<dl>
<dd>

**sensor_type:** `typing.Optional[SensorTypes]` — Type of Sensor
    
</dd>
</dl>

<dl>
<dd>

**model_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Model Name of Sensor
    
</dd>
</dl>

<dl>
<dd>

**manufacturer_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Manufacturer of Sensor
    
</dd>
</dl>

<dl>
<dd>

**dump_raw:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.v2.<a href="src/fern/v2/client.py">mobilegentilejson</a>() -> TileJson</code></summary>
<dl>
<dd>

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

client.v2.mobilegentilejson()

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

<details><summary><code>client.v2.<a href="src/fern/v2/client.py">get_mobilegentile</a>(...)</code></summary>
<dl>
<dd>

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

client.v2.get_mobilegentile(
    z=1,
    x=1,
    y=1,
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

**z:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**x:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**y:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**parameter:** `typing.Optional[GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestParameter]` 
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` — limit data to location id
    
</dd>
</dl>

<dl>
<dd>

**last_updated_from:** `typing.Optional[GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestLastUpdatedFrom]` 
    
</dd>
</dl>

<dl>
<dd>

**last_updated_to:** `typing.Optional[GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestLastUpdatedTo]` 
    
</dd>
</dl>

<dl>
<dd>

**is_mobile:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**project:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**is_analysis:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.v2.<a href="src/fern/v2/client.py">mobiletilejson</a>() -> TileJson</code></summary>
<dl>
<dd>

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

client.v2.mobiletilejson()

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

<details><summary><code>client.v2.<a href="src/fern/v2/client.py">get_mobiletile</a>(...)</code></summary>
<dl>
<dd>

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

client.v2.get_mobiletile(
    z=1,
    x=1,
    y=1,
    date_from=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    date_to=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
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

**z:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**x:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**y:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**date_from:** `GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestDateFrom` 
    
</dd>
</dl>

<dl>
<dd>

**date_to:** `GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestDateTo` 
    
</dd>
</dl>

<dl>
<dd>

**parameter:** `typing.Optional[GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestParameter]` 
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` — limit data to location id
    
</dd>
</dl>

<dl>
<dd>

**last_updated_from:** `typing.Optional[GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestLastUpdatedFrom]` 
    
</dd>
</dl>

<dl>
<dd>

**last_updated_to:** `typing.Optional[GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestLastUpdatedTo]` 
    
</dd>
</dl>

<dl>
<dd>

**is_mobile:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**project:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**is_analysis:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.v2.<a href="src/fern/v2/client.py">tilejson</a>() -> TileJson</code></summary>
<dl>
<dd>

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

client.v2.tilejson()

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

<details><summary><code>client.v2.<a href="src/fern/v2/client.py">demo</a>() -> str</code></summary>
<dl>
<dd>

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

client.v2.demo()

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

<details><summary><code>client.v2.<a href="src/fern/v2/client.py">get_tile</a>(...)</code></summary>
<dl>
<dd>

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

client.v2.get_tile(
    z=1,
    x=1,
    y=1,
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

**z:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**x:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**y:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**parameter:** `typing.Optional[GetTileV2LocationsTilesZxyPbfGetRequestParameter]` 
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` — limit data to location id
    
</dd>
</dl>

<dl>
<dd>

**last_updated_from:** `typing.Optional[GetTileV2LocationsTilesZxyPbfGetRequestLastUpdatedFrom]` 
    
</dd>
</dl>

<dl>
<dd>

**last_updated_to:** `typing.Optional[GetTileV2LocationsTilesZxyPbfGetRequestLastUpdatedTo]` 
    
</dd>
</dl>

<dl>
<dd>

**is_mobile:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**project:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**is_analysis:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.v2.<a href="src/fern/v2/client.py">mfr_get</a>() -> OpenAqResult</code></summary>
<dl>
<dd>

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

client.v2.mfr_get()

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

<details><summary><code>client.v2.<a href="src/fern/v2/client.py">measurements_get</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

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

client.v2.measurements_get()

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

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**date_from:** `typing.Optional[MeasurementsGetV2MeasurementsGetRequestDateFrom]` 
    
</dd>
</dl>

<dl>
<dd>

**date_to:** `typing.Optional[MeasurementsGetV2MeasurementsGetRequestDateTo]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Change the number of results returned.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Paginate through results.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[Sort]` 
    
</dd>
</dl>

<dl>
<dd>

**has_geo:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**parameter_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**parameter:** `typing.Optional[typing.Union[MeasurementsGetV2MeasurementsGetRequestParameterItem, typing.Sequence[MeasurementsGetV2MeasurementsGetRequestParameterItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**unit:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**coordinates:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**radius:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**country_id:** `typing.Optional[str]` 


        Limit results by a certain country using two letter country code.
        (ex. /US)
        
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 


        Limit results by a certain country using two letter country code.
        (ex. ?country=US or ?country=US&country=MX)
        
    
</dd>
</dl>

<dl>
<dd>

**city:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 


        Limit results by a certain city or cities.
        (ex. ?city=Chicago or ?city=Chicago&city=Boston)
        
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[typing.Union[MeasurementsGetV2MeasurementsGetRequestLocationItem, typing.Sequence[MeasurementsGetV2MeasurementsGetRequestLocationItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[MeasOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**is_mobile:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**is_analysis:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**project:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**entity:** `typing.Optional[EntityTypes]` 
    
</dd>
</dl>

<dl>
<dd>

**sensor_type:** `typing.Optional[SensorTypes]` 
    
</dd>
</dl>

<dl>
<dd>

**value_from:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**value_to:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[str]` 
    
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

<details><summary><code>client.v2.<a href="src/fern/v2/client.py">model_get</a>() -> OpenAqResult</code></summary>
<dl>
<dd>

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

client.v2.model_get()

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

<details><summary><code>client.v2.<a href="src/fern/v2/client.py">parameters_get</a>(...) -> OpenAqParametersResult</code></summary>
<dl>
<dd>

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

client.v2.parameters_get()

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

**limit:** `typing.Optional[int]` — Change the number of results returned.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Paginate through results.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[Sort]` — Define sort order.
    
</dd>
</dl>

<dl>
<dd>

**source_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` 
    
</dd>
</dl>

<dl>
<dd>

**source_slug:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` 
    
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

<details><summary><code>client.v2.<a href="src/fern/v2/client.py">projects_get</a>(...) -> OpenAqProjectsResult</code></summary>
<dl>
<dd>

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

client.v2.projects_get(
    project_id=1,
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

**project_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**country_id:** `typing.Optional[str]` 


        Limit results by a certain country using two letter country code.
        (ex. /US)
        
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 


        Limit results by a certain country using two letter country code.
        (ex. ?country=US or ?country=US&country=MX)
        
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Change the number of results returned.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Paginate through results.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[Sort]` — Define sort order.
    
</dd>
</dl>

<dl>
<dd>

**parameter_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**parameter:** `typing.Optional[typing.Union[ProjectsGetV2ProjectsProjectIdGetRequestParameterItem, typing.Sequence[ProjectsGetV2ProjectsProjectIdGetRequestParameterItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**unit:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**project:** `typing.Optional[typing.Union[ProjectsGetV2ProjectsProjectIdGetRequestProjectItem, typing.Sequence[ProjectsGetV2ProjectsProjectIdGetRequestProjectItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ProjectsOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**is_mobile:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**is_analysis:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**entity:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sensor_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**source_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
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

<details><summary><code>client.v2.<a href="src/fern/v2/client.py">sources_get</a>(...) -> OpenAqResult</code></summary>
<dl>
<dd>

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

client.v2.sources_get()

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

**limit:** `typing.Optional[int]` — Change the number of results returned.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Paginate through results.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[Sort]` — Define sort order.
    
</dd>
</dl>

<dl>
<dd>

**source_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` 
    
</dd>
</dl>

<dl>
<dd>

**source_slug:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[SourcesOrder]` 
    
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

<details><summary><code>client.v2.<a href="src/fern/v2/client.py">readme_get</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

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

client.v2.readme_get(
    slug="slug",
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

**slug:** `str` 
    
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

<details><summary><code>client.v2.<a href="src/fern/v2/client.py">summary_get</a>() -> OpenAqResult</code></summary>
<dl>
<dd>

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

client.v2.summary_get()

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

