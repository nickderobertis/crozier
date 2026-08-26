# Reference
## AccessibilityV2
<details><summary><code>client.accessibility_v2.<a href="src/fern/accessibility_v2/client.py">get_accessibility_as_geo_json</a>(...) -> AccessibilityResponseGeoJson</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AreaRequest_Municipality, Location, VehicleCharacteristics, VehicleType, EmissionClass, FuelType, Exclusions, EmissionZoneType
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.accessibility_v2.get_accessibility_as_geo_json(
    accept_encoding="gzip",
    area=AreaRequest_Municipality(
        id="GM0344",
    ),
    destination=Location(
        latitude=52.093784,
        longitude=5.15289,
    ),
    vehicle=VehicleCharacteristics(
        type=VehicleType.TRUCK,
        width=2,
        height=2.5,
        weight=20,
        length=5.2,
        axle_load=4,
        has_trailer=False,
        emission_class=EmissionClass.EURO6,
        fuel_types=[
            FuelType.PETROL
        ],
    ),
    exclusions=Exclusions(
        emission_zone_types=[
            EmissionZoneType.LOW_EMISSION_ZONE
        ],
        emission_zone_ids=[
            "NDW11_63a0104e-0b70-4b01-ad72-1ec692b41c47"
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

**area:** `AreaRequest` 
    
</dd>
</dl>

<dl>
<dd>

**vehicle:** `VehicleCharacteristics` 
    
</dd>
</dl>

<dl>
<dd>

**accept_encoding:** `typing.Optional[str]` — The HTTP Accept-Encoding request and response header indicates the content encoding (usually a compression algorithm) that the sender can understand.
    
</dd>
</dl>

<dl>
<dd>

**include_accessible_road_sections:** `typing.Optional[bool]` — Directive to include accessible road sections in the response.
    
</dd>
</dl>

<dl>
<dd>

**include_inaccessible_road_sections:** `typing.Optional[bool]` — Directive to include inaccessible road sections in the response.
    
</dd>
</dl>

<dl>
<dd>

**effectively_accessible:** `typing.Optional[bool]` — Effective accessibility means that you can reach the road section segment from at least one direction
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[Location]` 
    
</dd>
</dl>

<dl>
<dd>

**destination:** `typing.Optional[Location]` 
    
</dd>
</dl>

<dl>
<dd>

**visiting_window:** `typing.Optional[VisitingWindow]` 
    
</dd>
</dl>

<dl>
<dd>

**exclusions:** `typing.Optional[Exclusions]` 
    
</dd>
</dl>

<dl>
<dd>

**restrictions:** `typing.Optional[typing.List[AccessibilityRequestRestriction]]` 
    
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

## MunicipalitiesV2
<details><summary><code>client.municipalities_v2.<a href="src/fern/municipalities_v2/client.py">get_municipalities</a>() -> MunicipalityFeatureCollection</code></summary>
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

client.municipalities_v2.get_municipalities()

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

## RoadOperatorsV2
<details><summary><code>client.road_operators_v2.<a href="src/fern/road_operators_v2/client.py">get_road_operators</a>() -> RoadOperators</code></summary>
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

client.road_operators_v2.get_road_operators()

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

