# Reference
## Boards
<details><summary><code>client.boards.<a href="src/fern/boards/client.py">create_board</a>(...) -> Board</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Panel, PanelReading_Sensors, SensorReadingChannelsItem, Window, SensorReadingBench, SensorReadingChecksItem_Threshold
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.boards.create_board(
    title="title",
    panel=Panel(
        title="title",
        reading=PanelReading_Sensors(
            channels=[
                SensorReadingChannelsItem.AIR_TEMPERATURE,
                SensorReadingChannelsItem.HUMIDITY
            ],
            window=Window.DAILY,
            bench=SensorReadingBench(
                row=4,
                side="west",
            ),
            checks=[
                SensorReadingChecksItem_Threshold(
                    limit=80,
                )
            ],
        ),
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

**request:** `Board` 
    
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

<details><summary><code>client.boards.<a href="src/fern/boards/client.py">preview_board</a>(...) -> Board</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Panel, PanelReading_Sensors, SensorReadingChannelsItem, Window, SensorReadingBench, SensorReadingChecksItem_Threshold
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.boards.preview_board(
    title="Propagation house",
    panel=Panel(
        title="Bench humidity",
        reading=PanelReading_Sensors(
            channels=[
                SensorReadingChannelsItem.AIR_TEMPERATURE,
                SensorReadingChannelsItem.HUMIDITY
            ],
            window=Window.DAILY,
            bench=SensorReadingBench(
                row=4,
                side="west",
            ),
            checks=[
                SensorReadingChecksItem_Threshold(
                    limit=80,
                )
            ],
        ),
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

**request:** `Board` 
    
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

