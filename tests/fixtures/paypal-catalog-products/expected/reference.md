# Reference
## products
<details><summary><code>client.products.<a href="src/fern/products/client.py">list</a>(...) -> ProductCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists products.
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

client.products.list()

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

**page_size:** `typing.Optional[int]` — The number of items to return in the response.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — A non-zero integer which is the start index of the entire list of items that are returned in the response. So, the combination of `page=1` and `page_size=20` returns the first 20 items. The combination of `page=2` and `page_size=20` returns the next 20 items.
    
</dd>
</dl>

<dl>
<dd>

**total_required:** `typing.Optional[bool]` — Indicates whether to show the total items and total pages in the response.
    
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

<details><summary><code>client.products.<a href="src/fern/products/client.py">create</a>(...) -> Product</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a product.
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
from fern import FernApi, ProductCategory
from fern.environment import FernApiEnvironment
from fern.products import ProductRequestPostType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.products.create(
    prefer="return=minimal",
    name="Video Streaming Service",
    description="Video streaming service",
    type=ProductRequestPostType.SERVICE,
    category=ProductCategory.SOFTWARE,
    image_url="https://example.com/streaming.jpg",
    home_url="https://example.com/home",
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

**prefer:** `typing.Literal` — The preferred server response upon successful completion of the request. Value is:<ul><li><code>return=minimal</code>. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the <code>id</code>, <code>status</code> and HATEOAS links.</li><li><code>return=representation</code>. The server returns a complete resource representation, including the current state of the resource.</li></ul>
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The product name.
    
</dd>
</dl>

<dl>
<dd>

**type:** `ProductRequestPostType` — The product type. Indicates whether the product is physical or digital goods, or a service.
    
</dd>
</dl>

<dl>
<dd>

**pay_pal_request_id:** `typing.Optional[str]` — The server stores keys for 72 hours.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — The ID of the product. You can specify the SKU for the product. If you omit the ID, the system generates it. System-generated IDs have the `PROD-` prefix.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The product description.
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[ProductCategory]` 
    
</dd>
</dl>

<dl>
<dd>

**image_url:** `typing.Optional[str]` — The image URL for the product.
    
</dd>
</dl>

<dl>
<dd>

**home_url:** `typing.Optional[str]` — The home page URL for the product.
    
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

<details><summary><code>client.products.<a href="src/fern/products/client.py">get</a>(...) -> Product</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Shows details for a product, by ID.
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

client.products.get(
    product_id="product_id",
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

**product_id:** `str` — The product ID.
    
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

<details><summary><code>client.products.<a href="src/fern/products/client.py">patch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a product, by ID. You can patch these attributes and objects:<table><thead><tr><th>Attribute or object</th><th>Operations</th></tr></thead><tbody><tr><td><code>description</code></td><td>add, replace, remove</td></tr><tr><td><code>category</code></td><td>add, replace, remove</td></tr><tr><td><code>image_url</code></td><td>add, replace, remove</td></tr><tr><td><code>home_url</code></td><td>add, replace, remove</td></tr></tbody></table>
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
from fern import FernApi, Patch, PatchOp
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.products.patch(
    product_id="product_id",
    request=[
        Patch(
            op=PatchOp.REPLACE,
            path="/description",
            value="Premium video streaming service",
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

**product_id:** `str` — The product ID.
    
</dd>
</dl>

<dl>
<dd>

**request:** `PatchRequest` 
    
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

