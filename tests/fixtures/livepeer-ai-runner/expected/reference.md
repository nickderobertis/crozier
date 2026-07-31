# Reference
<details><summary><code>client.<a href="src/fern/client.py">health</a>() -> HealthCheck</code></summary>
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

<details><summary><code>client.<a href="src/fern/client.py">hardware_info</a>() -> HardwareInformation</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.hardware_info()

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

<details><summary><code>client.<a href="src/fern/client.py">hardware_stats</a>() -> HardwareStats</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.hardware_stats()

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

## Generate
<details><summary><code>client.generate.<a href="src/fern/generate/client.py">gen_text_to_image</a>(...) -> ImageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate images from text prompts.
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

client.generate.gen_text_to_image(
    prompt="prompt",
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

**prompt:** `str` — Text prompt(s) to guide image generation. Separate multiple prompts with '|' if supported by the model.
    
</dd>
</dl>

<dl>
<dd>

**model_id:** `typing.Optional[str]` — Hugging Face model ID used for image generation.
    
</dd>
</dl>

<dl>
<dd>

**loras:** `typing.Optional[str]` — A LoRA (Low-Rank Adaptation) model and its corresponding weight for image generation. Example: { "latent-consistency/lcm-lora-sdxl": 1.0, "nerijs/pixel-art-xl": 1.2}.
    
</dd>
</dl>

<dl>
<dd>

**height:** `typing.Optional[int]` — The height in pixels of the generated image.
    
</dd>
</dl>

<dl>
<dd>

**width:** `typing.Optional[int]` — The width in pixels of the generated image.
    
</dd>
</dl>

<dl>
<dd>

**guidance_scale:** `typing.Optional[float]` — Encourages model to generate images closely linked to the text prompt (higher values may reduce image quality).
    
</dd>
</dl>

<dl>
<dd>

**negative_prompt:** `typing.Optional[str]` — Text prompt(s) to guide what to exclude from image generation. Ignored if guidance_scale < 1.
    
</dd>
</dl>

<dl>
<dd>

**safety_check:** `typing.Optional[bool]` — Perform a safety check to estimate if generated images could be offensive or harmful.
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[int]` — Seed for random number generation.
    
</dd>
</dl>

<dl>
<dd>

**num_inference_steps:** `typing.Optional[int]` — Number of denoising steps. More steps usually lead to higher quality images but slower inference. Modulated by strength.
    
</dd>
</dl>

<dl>
<dd>

**num_images_per_prompt:** `typing.Optional[int]` — Number of images to generate per prompt.
    
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

<details><summary><code>client.generate.<a href="src/fern/generate/client.py">gen_image_to_image</a>(...) -> ImageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Apply image transformations to a provided image.
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

client.generate.gen_image_to_image(
    image="example_image",
    prompt="prompt",
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

**prompt:** `str` — Text prompt(s) to guide image generation.
    
</dd>
</dl>

<dl>
<dd>

**image:** `core.File` — Uploaded image to modify with the pipeline.
    
</dd>
</dl>

<dl>
<dd>

**model_id:** `typing.Optional[str]` — Hugging Face model ID used for image generation.
    
</dd>
</dl>

<dl>
<dd>

**loras:** `typing.Optional[str]` — A LoRA (Low-Rank Adaptation) model and its corresponding weight for image generation. Example: { "latent-consistency/lcm-lora-sdxl": 1.0, "nerijs/pixel-art-xl": 1.2}.
    
</dd>
</dl>

<dl>
<dd>

**strength:** `typing.Optional[float]` — Degree of transformation applied to the reference image (0 to 1).
    
</dd>
</dl>

<dl>
<dd>

**guidance_scale:** `typing.Optional[float]` — Encourages model to generate images closely linked to the text prompt (higher values may reduce image quality).
    
</dd>
</dl>

<dl>
<dd>

**image_guidance_scale:** `typing.Optional[float]` — Degree to which the generated image is pushed towards the initial image.
    
</dd>
</dl>

<dl>
<dd>

**negative_prompt:** `typing.Optional[str]` — Text prompt(s) to guide what to exclude from image generation. Ignored if guidance_scale < 1.
    
</dd>
</dl>

<dl>
<dd>

**safety_check:** `typing.Optional[bool]` — Perform a safety check to estimate if generated images could be offensive or harmful.
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[int]` — Seed for random number generation.
    
</dd>
</dl>

<dl>
<dd>

**num_inference_steps:** `typing.Optional[int]` — Number of denoising steps. More steps usually lead to higher quality images but slower inference. Modulated by strength.
    
</dd>
</dl>

<dl>
<dd>

**num_images_per_prompt:** `typing.Optional[int]` — Number of images to generate per prompt.
    
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

<details><summary><code>client.generate.<a href="src/fern/generate/client.py">gen_image_to_video</a>(...) -> VideoResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a video from a provided image.
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

client.generate.gen_image_to_video(
    image="example_image",
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

**image:** `core.File` — Uploaded image to generate a video from.
    
</dd>
</dl>

<dl>
<dd>

**model_id:** `typing.Optional[str]` — Hugging Face model ID used for video generation.
    
</dd>
</dl>

<dl>
<dd>

**height:** `typing.Optional[int]` — The height in pixels of the generated video.
    
</dd>
</dl>

<dl>
<dd>

**width:** `typing.Optional[int]` — The width in pixels of the generated video.
    
</dd>
</dl>

<dl>
<dd>

**fps:** `typing.Optional[int]` — The frames per second of the generated video.
    
</dd>
</dl>

<dl>
<dd>

**motion_bucket_id:** `typing.Optional[int]` — Used for conditioning the amount of motion for the generation. The higher the number the more motion will be in the video.
    
</dd>
</dl>

<dl>
<dd>

**noise_aug_strength:** `typing.Optional[float]` — Amount of noise added to the conditioning image. Higher values reduce resemblance to the conditioning image and increase motion.
    
</dd>
</dl>

<dl>
<dd>

**safety_check:** `typing.Optional[bool]` — Perform a safety check to estimate if generated images could be offensive or harmful.
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[int]` — Seed for random number generation.
    
</dd>
</dl>

<dl>
<dd>

**num_inference_steps:** `typing.Optional[int]` — Number of denoising steps. More steps usually lead to higher quality images but slower inference. Modulated by strength.
    
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

<details><summary><code>client.generate.<a href="src/fern/generate/client.py">gen_upscale</a>(...) -> ImageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upscale an image by increasing its resolution.
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

client.generate.gen_upscale(
    image="example_image",
    prompt="prompt",
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

**prompt:** `str` — Text prompt(s) to guide upscaled image generation.
    
</dd>
</dl>

<dl>
<dd>

**image:** `core.File` — Uploaded image to modify with the pipeline.
    
</dd>
</dl>

<dl>
<dd>

**model_id:** `typing.Optional[str]` — Hugging Face model ID used for upscaled image generation.
    
</dd>
</dl>

<dl>
<dd>

**safety_check:** `typing.Optional[bool]` — Perform a safety check to estimate if generated images could be offensive or harmful.
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[int]` — Seed for random number generation.
    
</dd>
</dl>

<dl>
<dd>

**num_inference_steps:** `typing.Optional[int]` — Number of denoising steps. More steps usually lead to higher quality images but slower inference. Modulated by strength.
    
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

<details><summary><code>client.generate.<a href="src/fern/generate/client.py">gen_audio_to_text</a>(...) -> TextResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Transcribe audio files to text.
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

client.generate.gen_audio_to_text(
    audio="example_audio",
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

**audio:** `core.File` — Uploaded audio file to be transcribed.
    
</dd>
</dl>

<dl>
<dd>

**model_id:** `typing.Optional[str]` — Hugging Face model ID used for transcription.
    
</dd>
</dl>

<dl>
<dd>

**return_timestamps:** `typing.Optional[str]` — Return timestamps for the transcribed text. Supported values: 'sentence', 'word', or a string boolean ('true' or 'false'). Default is 'true' ('sentence'). 'false' means no timestamps. 'word' means word-based timestamps.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[str]` — Additional job information to be passed to the pipeline.
    
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

<details><summary><code>client.generate.<a href="src/fern/generate/client.py">gen_segment_anything2</a>(...) -> MasksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Segment objects in an image.
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

client.generate.gen_segment_anything2(
    image="example_image",
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

**image:** `core.File` — Image to segment.
    
</dd>
</dl>

<dl>
<dd>

**model_id:** `typing.Optional[str]` — Hugging Face model ID used for image generation.
    
</dd>
</dl>

<dl>
<dd>

**point_coords:** `typing.Optional[str]` — Nx2 array of point prompts to the model, where each point is in (X,Y) in pixels.
    
</dd>
</dl>

<dl>
<dd>

**point_labels:** `typing.Optional[str]` — Labels for the point prompts, where 1 indicates a foreground point and 0 indicates a background point.
    
</dd>
</dl>

<dl>
<dd>

**box:** `typing.Optional[str]` — A length 4 array given as a box prompt to the model, in XYXY format.
    
</dd>
</dl>

<dl>
<dd>

**mask_input:** `typing.Optional[str]` — A low-resolution mask input to the model, typically from a previous prediction iteration, with the form 1xHxW (H=W=256 for SAM).
    
</dd>
</dl>

<dl>
<dd>

**multimask_output:** `typing.Optional[bool]` — If true, the model will return three masks for ambiguous input prompts, often producing better masks than a single prediction.
    
</dd>
</dl>

<dl>
<dd>

**return_logits:** `typing.Optional[bool]` — If true, returns un-thresholded mask logits instead of a binary mask.
    
</dd>
</dl>

<dl>
<dd>

**normalize_coords:** `typing.Optional[bool]` — If true, the point coordinates will be normalized to the range [0,1], with point_coords expected to be with respect to image dimensions.
    
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

<details><summary><code>client.generate.<a href="src/fern/generate/client.py">gen_llm</a>(...) -> LlmResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate text using a language model.
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
from fern import FernApi, LlmMessage
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.generate.gen_llm(
    messages=[
        LlmMessage(
            role="role",
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

**messages:** `typing.List[LlmMessage]` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**top_p:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**top_k:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.generate.<a href="src/fern/generate/client.py">gen_image_to_text</a>(...) -> ImageToTextResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Transform image files to text.
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

client.generate.gen_image_to_text(
    image="example_image",
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

**image:** `core.File` — Uploaded image to transform with the pipeline.
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `typing.Optional[str]` — Text prompt(s) to guide transformation.
    
</dd>
</dl>

<dl>
<dd>

**model_id:** `typing.Optional[str]` — Hugging Face model ID used for transformation.
    
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

<details><summary><code>client.generate.<a href="src/fern/generate/client.py">gen_live_video_to_video</a>(...) -> LiveVideoToVideoResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Apply transformations to a live video streamed to the returned endpoints.
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

client.generate.gen_live_video_to_video(
    subscribe_url="subscribe_url",
    publish_url="publish_url",
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

**subscribe_url:** `str` — Source URL of the incoming stream to subscribe to.
    
</dd>
</dl>

<dl>
<dd>

**publish_url:** `str` — Destination URL of the outgoing stream to publish.
    
</dd>
</dl>

<dl>
<dd>

**control_url:** `typing.Optional[str]` — URL for subscribing via Trickle protocol for updates in the live video-to-video generation params.
    
</dd>
</dl>

<dl>
<dd>

**events_url:** `typing.Optional[str]` — URL for publishing events via Trickle protocol for pipeline status and logs.
    
</dd>
</dl>

<dl>
<dd>

**model_id:** `typing.Optional[str]` — Name of the pipeline to run in the live video to video job. Notice that this is named model_id for consistency with other routes, but it does not refer to a Hugging Face model ID. The exact model(s) depends on the pipeline implementation and might be configurable via the `params` argument.
    
</dd>
</dl>

<dl>
<dd>

**params:** `typing.Optional[typing.Dict[str, typing.Any]]` — Initial parameters for the pipeline.
    
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

<details><summary><code>client.generate.<a href="src/fern/generate/client.py">gen_text_to_speech</a>(...) -> AudioResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a text-to-speech audio file based on the provided text input and speaker description.
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

client.generate.gen_text_to_speech()

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

**model_id:** `typing.Optional[str]` — Hugging Face model ID used for text to speech generation.
    
</dd>
</dl>

<dl>
<dd>

**text:** `typing.Optional[str]` — Text input for speech generation.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of speaker to steer text to speech generation.
    
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

