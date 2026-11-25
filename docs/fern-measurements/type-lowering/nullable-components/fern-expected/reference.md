# Reference
## Feedback
<details><summary><code>client.feedback.<a href="src/fern/feedback/client.py#L30-L64">send_feedback</a>(...) -> FeedbackSettings</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, FeedbackQuery

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.feedback.send_feedback(
    queries=[
        FeedbackQuery()
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

**queries:** `typing.List[FeedbackQuery]` 
    
</dd>
</dl>

<dl>
<dd>

**primary:** `typing.Optional[FeedbackQuery]` 
    
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

