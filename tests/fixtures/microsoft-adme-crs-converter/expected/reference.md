# Reference
## HealthCheck
<details><summary><code>client.health_check.<a href="src/fern/health_check/client.py">liveness_check</a>() -> typing.Dict[str, typing.Any]</code></summary>
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
    token="<token>",
    data_partition_id="<data-partition-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.health_check.liveness_check()

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

<details><summary><code>client.health_check.<a href="src/fern/health_check/client.py">readiness_check</a>() -> typing.Dict[str, typing.Any]</code></summary>
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
    token="<token>",
    data_partition_id="<data-partition-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.health_check.readiness_check()

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

## CrsConverterApiV2
<details><summary><code>client.crs_converter_api_v2.<a href="src/fern/crs_converter_api_v2/client.py">convert_point1</a>(...) -> ConvertPointsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Point
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    data_partition_id="<data-partition-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.crs_converter_api_v2.convert_point1(
    from_crs="fromCRS",
    points=[
        Point(
            x=1.1,
            y=1.1,
            z=1.1,
        )
    ],
    to_crs="toCRS",
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

**request:** `ConvertPointsRequest` 
    
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

<details><summary><code>client.crs_converter_api_v2.<a href="src/fern/crs_converter_api_v2/client.py">convert_geo_json1</a>(...) -> ConvertGeoJsonResponse</code></summary>
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
    token="<token>",
    data_partition_id="<data-partition-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.crs_converter_api_v2.convert_geo_json1(
    to_crs="toCRS",
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

**request:** `ConvertGeoJsonRequest` 
    
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

<details><summary><code>client.crs_converter_api_v2.<a href="src/fern/crs_converter_api_v2/client.py">convert_trajectory1</a>(...) -> ConvertTrajectoryResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TrajectoryStationIn
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    data_partition_id="<data-partition-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.crs_converter_api_v2.convert_trajectory1(
    azimuth_reference="azimuthReference",
    input_stations=[
        TrajectoryStationIn(
            azimuth=1.1,
            inclination=1.1,
            md=1.1,
        )
    ],
    method="method",
    trajectory_crs="trajectoryCRS",
    unit_z="unitZ",
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

**request:** `ConvertTrajectoryRequest` 
    
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

## InfoApi
<details><summary><code>client.info_api.<a href="src/fern/info_api/client.py">info</a>() -> VersionInfo</code></summary>
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
    token="<token>",
    data_partition_id="<data-partition-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.info_api.info()

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

<details><summary><code>client.info_api.<a href="src/fern/info_api/client.py">info1</a>() -> VersionInfo</code></summary>
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
    token="<token>",
    data_partition_id="<data-partition-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.info_api.info1()

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

## CrsConverterApiV3
<details><summary><code>client.crs_converter_api_v3.<a href="src/fern/crs_converter_api_v3/client.py">convert_point</a>(...) -> ConvertPointsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Point
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    data_partition_id="<data-partition-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.crs_converter_api_v3.convert_point(
    from_crs="fromCRS",
    points=[
        Point(
            x=1.1,
            y=1.1,
            z=1.1,
        )
    ],
    to_crs="toCRS",
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

**request:** `ConvertPointsRequest` 
    
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

<details><summary><code>client.crs_converter_api_v3.<a href="src/fern/crs_converter_api_v3/client.py">convert_bin_grid</a>(...) -> ConvertBinGridResponse</code></summary>
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
    token="<token>",
    data_partition_id="<data-partition-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.crs_converter_api_v3.convert_bin_grid()

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

**in_bin_grid:** `typing.Optional[AbstractBinGrid]` 
    
</dd>
</dl>

<dl>
<dd>

**to_crs:** `typing.Optional[str]` 
    
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

<details><summary><code>client.crs_converter_api_v3.<a href="src/fern/crs_converter_api_v3/client.py">convert_geo_json</a>(...) -> ConvertGeoJsonResponse</code></summary>
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
    token="<token>",
    data_partition_id="<data-partition-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.crs_converter_api_v3.convert_geo_json(
    to_crs="toCRS",
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

**request:** `ConvertGeoJsonRequest` 
    
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

<details><summary><code>client.crs_converter_api_v3.<a href="src/fern/crs_converter_api_v3/client.py">convert_trajectory</a>(...) -> ConvertTrajectoryResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TrajectoryStationIn
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    data_partition_id="<data-partition-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.crs_converter_api_v3.convert_trajectory(
    azimuth_reference="azimuthReference",
    input_stations=[
        TrajectoryStationIn(
            azimuth=1.1,
            inclination=1.1,
            md=1.1,
        )
    ],
    method="method",
    trajectory_crs="trajectoryCRS",
    unit_z="unitZ",
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

**request:** `ConvertTrajectoryRequest` 
    
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

