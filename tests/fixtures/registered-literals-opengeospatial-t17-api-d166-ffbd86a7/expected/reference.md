# Reference
## Capabilities
<details><summary><code>client.capabilities.<a href="src/fern/capabilities/client.py">get_landing_page</a>() -> LandingPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The landing page provides links to the API definition, the conformance
statements and to the feature collections in this dataset.
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

client.capabilities.get_landing_page()

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

<details><summary><code>client.capabilities.<a href="src/fern/capabilities/client.py">get_conformance_declaration</a>() -> ConfClasses</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A list of all conformance classes specified in a standard that the
server conforms to.
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

client.capabilities.get_conformance_declaration()

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

<details><summary><code>client.capabilities.<a href="src/fern/capabilities/client.py">get_collections</a>() -> Collections</code></summary>
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

client.capabilities.get_collections()

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

<details><summary><code>client.capabilities.<a href="src/fern/capabilities/client.py">describe_collection</a>(...) -> Collection</code></summary>
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

client.capabilities.describe_collection(
    collection_id="collectionId",
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

**collection_id:** `str` — local identifier of a collection
    
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

## Data
<details><summary><code>client.data.<a href="src/fern/data/client.py">get_features</a>(...) -> FeatureCollectionGeoJson</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch features of the feature collection with id `collectionId`.

Every feature in a dataset belongs to a collection. A dataset may
consist of multiple feature collections. A feature collection is often a
collection of features of a similar type, based on a common schema.

Use content negotiation to request HTML or GeoJSON.
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

client.data.get_features(
    collection_id="collectionId",
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

**collection_id:** `str` — local identifier of a collection
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The optional limit parameter limits the number of items that are presented in the response document.

Only items are counted that are on the first level of the collection in the response document.
Nested objects contained within the explicitly requested items shall not be counted.

Minimum = 1. Maximum = 10000. Default = 10.
    
</dd>
</dl>

<dl>
<dd>

**bbox:** `typing.Optional[typing.Union[typing.Dict[str, typing.Any], typing.Sequence[typing.Dict[str, typing.Any]]]]` 

Only features that have a geometry that intersects the bounding box are selected.
The bounding box is provided as four or six numbers, depending on whether the
coordinate reference system includes a vertical axis (height or depth):

* Lower left corner, coordinate axis 1
* Lower left corner, coordinate axis 2
* Minimum value, coordinate axis 3 (optional)
* Upper right corner, coordinate axis 1
* Upper right corner, coordinate axis 2
* Maximum value, coordinate axis 3 (optional)

The coordinate reference system of the values is WGS 84 longitude/latitude
(http://www.opengis.net/def/crs/OGC/1.3/CRS84) unless a different coordinate
reference system is specified in the parameter `bbox-crs`.

For WGS 84 longitude/latitude the values are in most cases the sequence of
minimum longitude, minimum latitude, maximum longitude and maximum latitude.
However, in cases where the box spans the antimeridian the first value
(west-most box edge) is larger than the third value (east-most box edge).

If the vertical axis is included, the third and the sixth number are
the bottom and the top of the 3-dimensional bounding box.

If a feature has multiple spatial geometry properties, it is the decision of the
server whether only a single spatial geometry property is used to determine
the extent or all relevant geometries.
    
</dd>
</dl>

<dl>
<dd>

**datetime:** `typing.Optional[str]` 

Either a date-time or an interval, open or closed. Date and time expressions
adhere to RFC 3339. Open intervals are expressed using double-dots.

Examples:

* A date-time: "2018-02-12T23:20:50Z"
* A closed interval: "2018-02-12T00:00:00Z/2018-03-18T12:31:12Z"
* Open intervals: "2018-02-12T00:00:00Z/.." or "../2018-03-18T12:31:12Z"

Only features that have a temporal property that intersects the value of
`datetime` are selected.

If a feature has multiple temporal properties, it is the decision of the
server whether only a single temporal property is used to determine
the extent or all relevant temporal properties.
    
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

<details><summary><code>client.data.<a href="src/fern/data/client.py">get_feature</a>(...) -> FeatureGeoJson</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch the feature with id `featureId` in the feature collection
with id `collectionId`.

Use content negotiation to request HTML or GeoJSON.
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

client.data.get_feature(
    collection_id="collectionId",
    feature_id="featureId",
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

**collection_id:** `str` — local identifier of a collection
    
</dd>
</dl>

<dl>
<dd>

**feature_id:** `str` — local identifier of a feature
    
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

