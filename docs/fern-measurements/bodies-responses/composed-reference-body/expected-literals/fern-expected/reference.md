# Reference
## Weaves
<details><summary><code>client.weaves.<a href="src/fern/weaves/client.py#L34-L60">get_weave</a>(...) -> Weave</code></summary>
<dl>
<dd>

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

client.weaves.get_weave(
    weave_id="weave_id",
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

**weave_id:** `str` 
    
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

<details><summary><code>client.weaves.<a href="src/fern/weaves/client.py#L62-L145">start_weave</a>(...) -> Weave</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, WeavePlanPattern_Plain, WeavePlanThreadsItem_Warp, Knot, BeadRef_Glass, WeaveFinishDelivery

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.weaves.start_weave(
    pattern=WeavePlanPattern_Plain(),
    threads=[
        WeavePlanThreadsItem_Warp()
    ],
    knots=[
        Knot(
            bead=BeadRef_Glass(
                glass_id="glassId",
            ),
        )
    ],
    finish="MATTE",
    shelf_id="shelfId",
    label="label",
    delivery=WeaveFinishDelivery(),
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

**pattern:** `WeavePlanPattern` — The weave's pattern.
    
</dd>
</dl>

<dl>
<dd>

**threads:** `typing.List[WeavePlanThreadsItem]` — The threads, in order.
    
</dd>
</dl>

<dl>
<dd>

**knots:** `typing.List[Knot]` — The knots tied along the selvedge.
    
</dd>
</dl>

<dl>
<dd>

**finish:** `WeavePlanFinish` — How the cloth is finished.
    
</dd>
</dl>

<dl>
<dd>

**shelf_id:** `str` — The shelf the cloth goes to.
    
</dd>
</dl>

<dl>
<dd>

**label:** `str` — The cloth's label.
    
</dd>
</dl>

<dl>
<dd>

**delivery:** `WeaveFinishDelivery` 
    
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

<details><summary><code>client.weaves.<a href="src/fern/weaves/client.py#L147-L208">check_weave</a>(...) -> Weave</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, WeavePlanPattern_Plain, WeavePlanThreadsItem_Warp, Knot, BeadRef_Glass

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.weaves.check_weave(
    pattern=WeavePlanPattern_Plain(),
    threads=[
        WeavePlanThreadsItem_Warp()
    ],
    knots=[
        Knot(
            bead=BeadRef_Glass(
                glass_id="glassId",
            ),
        )
    ],
    finish="MATTE",
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

**request:** `WeavePlan` 
    
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

