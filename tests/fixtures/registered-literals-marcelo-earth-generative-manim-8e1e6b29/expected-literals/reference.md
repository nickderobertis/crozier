# Reference
<details><summary><code>client.<a href="src/fern/client.py">health</a>() -> HealthResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the health status of the API and which LLM provider API keys are configured.
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

client.health()

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

<details><summary><code>client.<a href="src/fern/client.py">health_v1</a>() -> HealthResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Alias for /health.
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

client.health_v1()

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

<details><summary><code>client.<a href="src/fern/client.py">list_models</a>() -> ModelsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all supported engines with their available model IDs, defaults, and whether the corresponding API key is configured.
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

client.list_models()

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

<details><summary><code>client.<a href="src/fern/client.py">generate_code</a>(...) -> CodeGenerationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates Manim Python code from a natural-language prompt using the specified LLM engine.
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

client.generate_code(
    prompt="Draw a blue circle and animate its creation.",
    engine="openai",
    model="gpt-4o",
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

**prompt:** `typing.Optional[str]` — Natural-language description of the animation to generate.
    
</dd>
</dl>

<dl>
<dd>

**engine:** `typing.Optional[CodeGenerationRequestEngine]` — LLM provider to use.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — Model ID for the chosen engine. Defaults to the engine's recommended model if omitted.
    
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

<details><summary><code>client.<a href="src/fern/client.py">chat_generation</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Streams Manim code and explanations through a multi-turn conversation. Supports OpenAI, Anthropic, Gemini, Featherless, and LiteLLM engines.
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
from fern import FernApi, ChatMessage
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.chat_generation(
    messages=[
        ChatMessage(
            role="user",
            content="content",
        ),
        ChatMessage(
            role="user",
            content="content",
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

**messages:** `typing.List[ChatMessage]` — Conversation history.
    
</dd>
</dl>

<dl>
<dd>

**engine:** `typing.Optional[ChatGenerationRequestEngine]` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — Model ID override. Defaults to the engine's recommended model.
    
</dd>
</dl>

<dl>
<dd>

**global_prompt:** `typing.Optional[str]` — Additional system-level instruction injected at the beginning.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**project_title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**scenes:** `typing.Optional[typing.List[typing.Dict[str, typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_scenes:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**is_for_platform:** `typing.Optional[bool]` — When true, the response uses the Vercel AI data stream format with Transfer-Encoding chunked.
    
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

<details><summary><code>client.<a href="src/fern/client.py">render_video</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Executes Manim Python code and returns a rendered MP4 video URL. Supports streaming progress updates.
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

client.render_video(
    code="from manim import *\nclass GenScene(Scene):\n    def construct(self):\n        self.play(Create(Circle()))",
    file_class="GenScene",
    aspect_ratio="16:9",
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

**code:** `str` — Manim Python code to render.
    
</dd>
</dl>

<dl>
<dd>

**file_class:** `typing.Optional[str]` — Name of the Manim Scene subclass to render. Defaults to GenScene.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — User identifier used in the output file name.
    
</dd>
</dl>

<dl>
<dd>

**project_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**iteration:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**aspect_ratio:** `typing.Optional[VideoRenderingRequestAspectRatio]` 
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Optional[bool]` — If true, returns a 207 streaming response with per-animation progress.
    
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

<details><summary><code>client.<a href="src/fern/client.py">generate_video</a>(...) -> VideoRenderingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates Manim code from a prompt, then renders it to a video in one request.
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

client.generate_video(
    prompt="Animate a bouncing ball with gravity.",
    engine="openai",
    aspect_ratio="16:9",
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

**prompt:** `str` — Natural-language description of the animation to generate and render.
    
</dd>
</dl>

<dl>
<dd>

**engine:** `typing.Optional[VideoGenerationRequestEngine]` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**aspect_ratio:** `typing.Optional[VideoGenerationRequestAspectRatio]` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**project_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**iteration:** `typing.Optional[int]` 
    
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

