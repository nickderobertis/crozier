# Reference
<details><summary><code>client.<a href="src/fern/client.py">createresponse</a>(...) -> ResponseResource</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a response.
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

client.createresponse()

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

**model:** `typing.Optional[str]` — The model to use for this request, e.g. 'gpt-5.2'.
    
</dd>
</dl>

<dl>
<dd>

**input:** `typing.Optional[CreateResponseBodyInput]` — Context to provide to the model for the scope of this request. May either be a string or an array of input items. If a string is provided, it is interpreted as a user message.
    
</dd>
</dl>

<dl>
<dd>

**previous_response_id:** `typing.Optional[str]` — The ID of the response to use as the prior turn for this request.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.List[IncludeEnum]]` 
    
</dd>
</dl>

<dl>
<dd>

**tools:** `typing.Optional[typing.List[ResponsesToolParam]]` — A list of tools that the model may call while generating the response.
    
</dd>
</dl>

<dl>
<dd>

**tool_choice:** `typing.Optional[CreateResponseBodyToolChoice]` — Controls which tool the model should use, if any.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 

Set of 16 key-value pairs that can be attached to an object. This can be         useful for storing additional information about the object in a structured         format, and querying for objects via API or the dashboard.
        Keys are strings with a maximum length of 64 characters. Values are strings         with a maximum length of 512 characters.
    
</dd>
</dl>

<dl>
<dd>

**text:** `typing.Optional[CreateResponseBodyText]` — Configuration options for text output.
    
</dd>
</dl>

<dl>
<dd>

**temperature:** `typing.Optional[float]` — Sampling temperature to use, between 0 and 2. Higher values make the output more random.
    
</dd>
</dl>

<dl>
<dd>

**top_p:** `typing.Optional[float]` — Nucleus sampling parameter, between 0 and 1. The model considers only the tokens with the top cumulative probability.
    
</dd>
</dl>

<dl>
<dd>

**presence_penalty:** `typing.Optional[float]` — Penalizes new tokens based on whether they appear in the text so far.
    
</dd>
</dl>

<dl>
<dd>

**frequency_penalty:** `typing.Optional[float]` — Penalizes new tokens based on their frequency in the text so far.
    
</dd>
</dl>

<dl>
<dd>

**parallel_tool_calls:** `typing.Optional[bool]` — Whether the model may call multiple tools in parallel.
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Optional[bool]` — Whether to stream response events as server-sent events.
    
</dd>
</dl>

<dl>
<dd>

**stream_options:** `typing.Optional[CreateResponseBodyStreamOptions]` — Options that control streamed response behavior.
    
</dd>
</dl>

<dl>
<dd>

**background:** `typing.Optional[bool]` — Whether to run the request in the background and return immediately.
    
</dd>
</dl>

<dl>
<dd>

**max_output_tokens:** `typing.Optional[int]` — The maximum number of tokens the model may generate for this response.
    
</dd>
</dl>

<dl>
<dd>

**max_tool_calls:** `typing.Optional[int]` — The maximum number of tool calls the model may make while generating the response.
    
</dd>
</dl>

<dl>
<dd>

**reasoning:** `typing.Optional[CreateResponseBodyReasoning]` — Configuration options for reasoning behavior.
    
</dd>
</dl>

<dl>
<dd>

**safety_identifier:** `typing.Optional[str]` — A stable identifier used for safety monitoring and abuse detection.
    
</dd>
</dl>

<dl>
<dd>

**prompt_cache_key:** `typing.Optional[str]` — A key to use when reading from or writing to the prompt cache.
    
</dd>
</dl>

<dl>
<dd>

**truncation:** `typing.Optional[CreateResponseBodyTruncation]` — Controls how the service truncates the input when it exceeds the model context window.
    
</dd>
</dl>

<dl>
<dd>

**instructions:** `typing.Optional[str]` — Additional instructions to guide the model for this request.
    
</dd>
</dl>

<dl>
<dd>

**store:** `typing.Optional[bool]` — Whether to store the response so it can be retrieved later.
    
</dd>
</dl>

<dl>
<dd>

**service_tier:** `typing.Optional[CreateResponseBodyServiceTier]` — The service tier to use for this request.
    
</dd>
</dl>

<dl>
<dd>

**top_logprobs:** `typing.Optional[int]` — The number of most likely tokens to return at each position, along with their log probabilities.
    
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

