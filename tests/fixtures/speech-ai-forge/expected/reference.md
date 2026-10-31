# Reference
## System
<details><summary><code>client.system.<a href="src/fern/system/client.py">ping</a>() -> BaseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Health check
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

client.system.ping()

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

<details><summary><code>client.system.<a href="src/fern/system/client.py">get_versions</a>() -> BaseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get versions
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

client.system.get_versions()

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

<details><summary><code>client.system.<a href="src/fern/system/client.py">get_audio_formats</a>() -> BaseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get audio encoder formats
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

client.system.get_audio_formats()

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

## Models
<details><summary><code>client.models.<a href="src/fern/models/client.py">reload_models</a>() -> BaseResponse</code></summary>
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

client.models.reload_models()

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

<details><summary><code>client.models.<a href="src/fern/models/client.py">unload_models</a>() -> BaseResponse</code></summary>
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

client.models.unload_models()

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

## Style
<details><summary><code>client.style.<a href="src/fern/style/client.py">list_styles</a>() -> BaseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**DEPRECATED**
This API is deprecated and will be removed in the future. We will replace it with the speaker system and prompt system.
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

client.style.list_styles()

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

## Speaker
<details><summary><code>client.speaker.<a href="src/fern/speaker/client.py">list_speakers</a>(...) -> BaseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all available speakers with optional pagination and detail control.

- `detailed`: If true, returns complete metadata including references and embeddings.
- `offset` / `limit`: Support for paginated speaker listing.
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

client.speaker.list_speakers()

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

**detailed:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
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

<details><summary><code>client.speaker.<a href="src/fern/speaker/client.py">refresh_speakers</a>() -> BaseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Force reload of all speaker metadata from disk.  
Use this when files are modified externally or newly added.
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

client.speaker.refresh_speakers()

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

<details><summary><code>client.speaker.<a href="src/fern/speaker/client.py">update_speakers</a>(...) -> BaseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Batch update multiple speakers by providing a list of speaker JSON configs.

Each speaker must already exist (matched by ID).  
Will overwrite corresponding fields and persist changes to disk.
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

client.speaker.update_speakers(
    speakers=[
        {
            "key": "value"
        }
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

**speakers:** `typing.List[typing.Dict[str, typing.Any]]` 
    
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

<details><summary><code>client.speaker.<a href="src/fern/speaker/client.py">create_speaker</a>(...) -> BaseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new speaker profile with optional reference audios.

- `name` is required and used as unique identifier.
- `wavs` is a list of audio samples (base64-encoded) and reference texts for embedding.
- `save_file`: If true, the speaker will be saved to disk and available after refresh.
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

client.speaker.create_speaker(
    name="name",
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**gender:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**author:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**desc:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**wavs:** `typing.Optional[typing.List[AudioReference]]` 
    
</dd>
</dl>

<dl>
<dd>

**save_file:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.speaker.<a href="src/fern/speaker/client.py">update_speaker</a>(...) -> BaseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a single speaker's configuration by full JSON override.

The speaker must already exist (matched by ID).  
Fields like name, gender, refs, etc., will be updated accordingly.
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

client.speaker.update_speaker()

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

**json:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
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

<details><summary><code>client.speaker.<a href="src/fern/speaker/client.py">speaker_detail</a>(...) -> BaseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch metadata of a specific speaker by ID.

- `with_emb`: If true, includes embedding vectors and all reference data.
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

client.speaker.speaker_detail(
    id="id",
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**with_emb:** `typing.Optional[bool]` 
    
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

## Tts
<details><summary><code>client.tts.<a href="src/fern/tts/client.py">synthesize_tts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**Text-to-Speech Synthesis API (v1 - GET)**

This endpoint converts text into speech using GET request parameters.
It offers various options for customizing the voice, style, audio output, and processing.

**Mandatory Parameter**:
*   `text`: The text string to be synthesized.

**Speaker and Style Customization**:
*   `spk`: Specify the speaker by name or seed (e.g., "female2").
*   `style`: Define the speaking style (e.g., "chat").

**Generation Control**:
*   `temperature`: Sampling temperature (0.0-1.0, e.g., 0.3). Controls randomness.
*   `top_p`: Nucleus sampling probability (0.0-1.0, e.g., 0.5).
*   `top_k`: Limits sampling to the K most likely next tokens (e.g., 20).
*   `seed`: Seed for reproducible generation (e.g., 42).
*   `prompt`, `prompt1`, `prompt2`: Optional text prompts to guide inference.
*   `prefix`: Optional text prefix for inference.
*   `bs` (batch_size): Batch size for processing (e.g., "8").
*   `thr` (threshold): Sentence splitter threshold (e.g., "100").
*   `eos`: End-of-sentence marker (e.g., "[uv_break]").

**Output Audio Configuration**:
*   `format`: Desired audio output format. Supported: "mp3", "wav", "raw" (default).
*   `bitrate`: Audio bitrate for compressed formats (e.g., "64k").

**Audio Adjustments**:
*   `speed`: Playback speed multiplier (e.g., 1.0 for normal).
*   `pitch`: Pitch adjustment (e.g., 0 for no change).
*   `volume_gain`: Volume gain in dB (e.g., 0 for no change).

**Enhancements**:
*   `enhance`: Boolean to enable audio enhancement (default: false).
*   `denoise`: Boolean to enable audio denoising (default: false).

**Streaming Output**:
*   `stream`: Boolean to enable streaming audio generation (default: false).
*   `chunk_size`: Size of chunks for streaming (e.g., 64, if stream is true).

**Caching**:
*   `no_cache`: Boolean or "on"/"off" to disable caching (default: false).

**Model Selection**:
*   `model`: Specify the TTS model ID to use (e.g., "chat-tts", "cosy-voice").

**Response**:
*   **Success**: An audio file stream (`FileResponse`).
*   **Failure**: A JSON object detailing the error (e.g., validation errors, internal server error).

**Note**: This v1 endpoint does *not* support voice cloning via reference audio. For voice cloning, please refer to the v2 API. Parameters like temperature, top_p, top_k, seed, prompts, and prefix might be overridden by specific speaker (`spk`) or style (`style`) configurations.
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

client.tts.synthesize_tts(
    text="text",
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

**text:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**spk:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**style:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**temperature:** `typing.Optional[float]` 
    
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

**seed:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**bitrate:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**prompt1:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**prompt2:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**prefix:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**bs:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**thr:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**eos:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**enhance:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**denoise:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**speed:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**pitch:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**volume_gain:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**chunk_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**no_cache:** `typing.Optional[SynthesizeTtsV1TtsGetRequestNoCache]` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` 
    
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

## Ssml
<details><summary><code>client.ssml.<a href="src/fern/ssml/client.py">synthesize_ssml_api</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Synthesize speech from SSML-formatted input using a specified TTS model.

This endpoint supports multi-speaker, multi-style speech synthesis based on structured SSML input.
It can return audio in various formats (e.g., `raw`, `wav`, `mp3`), with optional enhancements and prosody adjustments.

### Supported Features
- Multiple speakers via `<voice spk="...">`
- Arbitrary text segmentation with sentence break markers (e.g., `eos="[uv_break]"`)
- Streaming or full-response audio
- Audio enhancement & pitch/speed adjustment via `EnhancerConfig` / `AdjustConfig`
- Custom batch size & segment length control via `batch_size` / `spliter_thr`

### Parameters
- `ssml` (str): SSML XML string containing structured speech content (required)
- `format` (str): Output audio format. One of: `raw`, `wav`, `mp3` (default: `raw`)
- `batch_size` (int): Batch size for internal TTS inference, must be > 0
- `eos` (str): End-of-sentence token for segmentation (default: `[uv_break]`)
- `model` (str): TTS model identifier to be used (default: `chat-tts`)
- `spliter_thr` (int): Threshold to split long texts (default: 100, minimum: 50)
- `enhancer` (EnhancerConfig): Optional audio enhancer settings
- `adjuster` (AdjustConfig): Optional pitch/speed/volume control
- `stream` (bool): If true, returns a streaming response; otherwise, file response

### Example SSML Input

```xml
<speak version="0.1">
    <voice spk="mona">ChatTTS 用于合成多角色多情感的有声书示例</voice>
    <voice spk="mona">黛玉冷笑道：</voice>
    <voice spk="doubao" emotion="happy">我说呢，亏了绊住，不然，早就飞起来了。</voice>
    <voice spk="mona">宝玉道：</voice>
    <voice spk="mona">“只许和你玩，替你解闷。不过偶然到他那里，就说这些闲话。”</voice>
    <voice spk="doubao" emotion="angry">“好没意思的话！ 去不去，关我什么事儿？ 又没叫你替我解闷儿 ，还许你不理我呢”</voice>
    <voice spk="mona">说着，便赌气回房去了。</voice>
</speak>
````

The endpoint returns a synthesized audio file or stream based on the provided SSML and configuration.
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

client.ssml.synthesize_ssml_api(
    ssml="ssml",
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

**ssml:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[AudioFormat]` 
    
</dd>
</dl>

<dl>
<dd>

**batch_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**eos:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**spliter_thr:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**enhancer:** `typing.Optional[EnhancerConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**adjuster:** `typing.Optional[AdjustConfig]` 
    
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

## GoogleApi
<details><summary><code>client.google_api.<a href="src/fern/google_api/client.py">google_text_synthesize</a>(...) -> GoogleTextSynthesizeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

google api document: <br/>
[https://cloud.google.com/text-to-speech/docs/reference/rest/v1/text/synthesize](https://cloud.google.com/text-to-speech/docs/reference/rest/v1/text/synthesize)

- 多个属性在本系统中无用仅仅是为了兼容google api
- voice 中的 topP, topK, temperature 为本系统中的参数
- voice.name 即 speaker name （或者speaker seed）
- voice.seed 为 infer seed （可在webui中测试具体作用）

- 编码格式影响的是 audioContent 的二进制格式，所以所有format都是返回带有base64数据的json
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
from fern import FernApi, SynthesisInput, VoiceSelectionParams, AudioConfig
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.google_api.google_text_synthesize(
    input=SynthesisInput(),
    voice=VoiceSelectionParams(),
    audio_config=AudioConfig(),
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

**input:** `SynthesisInput` 
    
</dd>
</dl>

<dl>
<dd>

**voice:** `VoiceSelectionParams` 
    
</dd>
</dl>

<dl>
<dd>

**audio_config:** `AudioConfig` 
    
</dd>
</dl>

<dl>
<dd>

**enhancer_config:** `typing.Optional[EnhancerConfig]` 
    
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

<details><summary><code>client.google_api.<a href="src/fern/google_api/client.py">speech_recognize</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Performs synchronous speech recognition: receive results after all audio has been sent and processed.
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

client.google_api.speech_recognize()

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

<details><summary><code>client.google_api.<a href="src/fern/google_api/client.py">long_running_recognize</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Performs asynchronous speech recognition: receive results via the google.longrunning.Operations interface.
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

client.google_api.long_running_recognize()

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

## OpenAiApi
<details><summary><code>client.open_ai_api.<a href="src/fern/open_ai_api/client.py">openai_speech_api</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

openai api document: 
[https://platform.openai.com/docs/guides/text-to-speech](https://platform.openai.com/docs/guides/text-to-speech)

以下属性为本系统自定义属性，不在openai文档中：
- batch_size: 是否开启batch合成，小于等于1表示不使用batch （不推荐）
- spliter_threshold: 开启batch合成时，句子分割的阈值
- style: 风格

> model 可填任意值
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

client.open_ai_api.openai_speech_api(
    input="input",
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

**input:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**voice:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**response_format:** `typing.Optional[AudioFormat]` 
    
</dd>
</dl>

<dl>
<dd>

**speed:** `typing.Optional[float]` — Speed of the audio
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**top_k:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**top_p:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**style:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**batch_size:** `typing.Optional[int]` — Batch size
    
</dd>
</dl>

<dl>
<dd>

**spliter_threshold:** `typing.Optional[float]` — Threshold for sentence spliter
    
</dd>
</dl>

<dl>
<dd>

**eos:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**enhance:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**denoise:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**bitrate:** `typing.Optional[str]` 
    
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

<details><summary><code>client.open_ai_api.<a href="src/fern/open_ai_api/client.py">transcribe</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Transcribes audio into the input language.
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

client.open_ai_api.transcribe(
    file="example_file",
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

**file:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**response_format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**timestamp_granularities:** `typing.Optional[typing.List[str]]` 
    
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

## Text
<details><summary><code>client.text.<a href="src/fern/text/client.py">refiner_prompt_post</a>(...) -> BaseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**DeprecationWarning**

This endpoint is deprecated and will be removed in the future.

Requirements:
- `chattts` model
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

client.text.refiner_prompt_post(
    text="text",
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

**text:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[int]` 
    
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

**temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**repetition_penalty:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_new_token:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**spliter_threshold:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**normalize:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.text.<a href="src/fern/text/client.py">text_normalize_post</a>(...) -> BaseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Normalize raw input text using a selected Text Normalization (TN) pipeline.

This endpoint supports different TN implementations to perform text normalization 
(e.g., expanding numbers, abbreviations, adding pauses or prosodic markers for TTS, etc.).

### Parameters

- `text` (str): The raw text to normalize.
- `pipe_id` (str): The TN pipeline to use. Available options:
  - `base`
  - `chat-tts`
  - `cosy-voice`
  - `fish-speech`
  - `f5-tts`
  - `index-tts`
  - `spark-tts`
- `config` (TNConfig, optional): Optional configuration to customize TN behavior for specific pipelines.

### Returns

A normalized version of the input text, suitable for use in speech synthesis or downstream NLP tasks.
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

client.text.text_normalize_post(
    text="text",
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

**text:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**pipe_id:** `typing.Optional[TextNormalizeRequestPipeId]` 
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[TnConfig]` 
    
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

## Xtts
<details><summary><code>client.xtts.<a href="src/fern/xtts/client.py">speakers</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[[Click To XTTS_V2 API Document]](https://github.com/lenML/Speech-AI-Forge/blob/main/docs/api_xtts.md)

[[Learn More About Documents]](https://github.com/lenML/Speech-AI-Forge/issues/240)
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

client.xtts.speakers()

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

<details><summary><code>client.xtts.<a href="src/fern/xtts/client.py">tts_to_audio</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[[Click To XTTS_V2 API Document]](https://github.com/lenML/Speech-AI-Forge/blob/main/docs/api_xtts.md)

[[Learn More About Documents]](https://github.com/lenML/Speech-AI-Forge/issues/240)
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

client.xtts.tts_to_audio(
    text="text",
    speaker_wav="speaker_wav",
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

**text:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**speaker_wav:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` 
    
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

<details><summary><code>client.xtts.<a href="src/fern/xtts/client.py">tts_stream</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[[Click To XTTS_V2 API Document]](https://github.com/lenML/Speech-AI-Forge/blob/main/docs/api_xtts.md)

[[Learn More About Documents]](https://github.com/lenML/Speech-AI-Forge/issues/240)
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

client.xtts.tts_stream(
    text="text",
    speaker_wav="speaker_wav",
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

**text:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**speaker_wav:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**no_cache:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.xtts.<a href="src/fern/xtts/client.py">set_tts_settings</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[[Click To XTTS_V2 API Document]](https://github.com/lenML/Speech-AI-Forge/blob/main/docs/api_xtts.md)

[[Learn More About Documents]](https://github.com/lenML/Speech-AI-Forge/issues/240)
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

client.xtts.set_tts_settings(
    stream_chunk_size=1,
    temperature=1.1,
    speed=1.1,
    length_penalty=1.1,
    repetition_penalty=1.1,
    top_p=1.1,
    top_k=1,
    enable_text_splitting=True,
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

**stream_chunk_size:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**temperature:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**speed:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**length_penalty:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**repetition_penalty:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**top_p:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**top_k:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**enable_text_splitting:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**batch_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**eos:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**infer_seed:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**use_decoder:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**prompt1:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**prompt2:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**prefix:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**spliter_threshold:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**style:** `typing.Optional[str]` 
    
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

## Stt
<details><summary><code>client.stt.<a href="src/fern/stt/client.py">transcribe</a>(...) -> TranscriptionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Transcribes audio into the input language.
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

client.stt.transcribe(
    file="example_file",
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

**file:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**prefix:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**sample_len:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**best_of:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**beam_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**patience:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**length_penalty:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[SttOutputFormat]` 
    
</dd>
</dl>

<dl>
<dd>

**highlight_words:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**max_line_count:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_line_width:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_words_per_line:** `typing.Optional[int]` 
    
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

<details><summary><code>client.stt.<a href="src/fern/stt/client.py">transcribe_stream</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Transcribes audio into the input language in real-time.

* Not implemented yet (WIP)
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

client.stt.transcribe_stream(
    file="example_file",
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

**file:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**prefix:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**sample_len:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**best_of:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**beam_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**patience:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**length_penalty:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[SttOutputFormat]` 
    
</dd>
</dl>

<dl>
<dd>

**highlight_words:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**max_line_count:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_line_width:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_words_per_line:** `typing.Optional[int]` 
    
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

## VoiceClone
<details><summary><code>client.voice_clone.<a href="src/fern/voice_clone/client.py">voice_clone</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Voice cloning API

**Deprecated**
This API is deprecated and will be removed in the future.
Please use the `TTS API` instead.
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

client.voice_clone.voice_clone(
    src_audio="example_src_audio",
    ref_audio="example_ref_audio",
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

**src_audio:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**ref_spk:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**spk_emotion:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**tau:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ref_audio:** `typing.Optional[core.File]` 
    
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

## ForgeV2
<details><summary><code>client.forge_v2.<a href="src/fern/forge_v2/client.py">forge_text_synthesize</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**Text-to-Speech Synthesis API (v2)**

This endpoint converts text into speech, offering a wide range of customization options.
It accepts JSON formatted data in the request body.

**Core Functionality**:
*   Synthesizes speech from various text inputs.
*   Supports voice cloning by directly uploading a reference audio.

**Input Flexibility**:
*   Provide text via one of these mutually exclusive fields:
    *   `text`: A single string of text.
    *   `texts`: A list of strings for batch processing.
    *   `ssml`: Text formatted using Speech Synthesis Markup Language (SSML).

**Speaker Customization (`spk`)**:
*   Use pre-defined speakers via `spk.from_spk_id` or `spk.from_spk_name`.
*   **Voice Cloning**: Provide reference audio for voice cloning:
    *   `spk.from_ref.wav_b64`: Base64 encoded WAV audio data.
    *   `spk.from_ref.text`: The transcript corresponding to the reference audio.

**Audio Processing & Control**:
*   **Adjustments (`adjust`)**:
    *   `pitch`: Modify audio pitch.
    *   `speed_rate`: Adjust speaking rate.
    *   `volume_gain_db`: Change audio volume.
    *   `normalize`: Apply volume normalization.
    *   `remove_silence`: Trim silence from audio ends.
*   **Encoding (`encoder`)**:
    *   `format`: Output audio format (e.g., "mp3", "wav").
    *   `bitrate`: Audio bitrate (e.g., "64k").
    *   `acodec`: Audio codec (e.g., "libmp3lame").
*   **Enhancement (`enhance`)**:
    *   `enabled`: Toggle audio enhancement.
    *   `model`: Select enhancement model.
    *   Additional parameters like `nfe`, `solver`, `lambd`, `tau` for fine-tuning.
*   **Inference (`infer`)**:
    *   `batch_size`, `spliter_threshold`, `eos` for text processing.
    *   `seed`: For reproducible outputs.
    *   `stream`, `stream_chunk_size`: Enable and configure streaming output.
    *   `no_cache`, `sync_gen`: Control caching and generation mode.
*   **Text Normalization (`tn`)**:
    *   `enabled`/`disabled`: Specify text normalization rules.
*   **TTS Model Parameters (`tts`)**:
    *   `mid`: TTS model ID (e.g., "cosy-voice").
    *   `style`, `emotion`: Control speaking style and emotion.
    *   `temperature`, `top_p`, `top_k`: Adjust sampling parameters for generation.
    *   Deprecated: `prompt`, `prompt1`, `prompt2`, `prefix`.
*   **Voice Cloning (`vc`)** (Note: Potentially deprecated, mainly for OpenVoice):
    *   `enabled`, `mid`, `emotion`, `tau`.

**Response**:
*   **Success**: An audio file stream (`FileResponse`).
*   **Failure**: A JSON object detailing the error.

**Key Considerations**:
1.  Ensure only one of `text`, `texts`, or `ssml` is provided.
2.  For voice cloning, use high-quality reference audio (3-5 seconds recommended).
3.  Enabling audio enhancement may increase generation latency.
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

client.forge_v2.forge_text_synthesize()

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

**adjust:** `typing.Optional[AdjustConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**encoder:** `typing.Optional[EncoderConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**enhance:** `typing.Optional[EnhancerConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**infer:** `typing.Optional[InferConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**vc:** `typing.Optional[VcConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**tn:** `typing.Optional[TnConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**tts:** `typing.Optional[TtsConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**spk:** `typing.Optional[SpeakerConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**texts:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**ssml:** `typing.Optional[str]` 
    
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

<details><summary><code>client.forge_v2.<a href="src/fern/forge_v2/client.py">transcribe_v2</a>(...) -> TranscriptionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Transcribes audio using base64 or URL input. Stateless interface.
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
from fern import FernApi, InputAudio
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.forge_v2.transcribe_v2(
    input_audio=InputAudio(),
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

**input_audio:** `InputAudio` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — ASR 模型名称，如 whisper.base、whisper.large
    
</dd>
</dl>

<dl>
<dd>

**refrence_transcript:** `typing.Optional[str]` — 参考文案
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `typing.Optional[str]` — 提示词，用于引导模型
    
</dd>
</dl>

<dl>
<dd>

**prefix:** `typing.Optional[str]` — 对话历史或固定开头
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — 语言代码，如 'en', 'zh' 等
    
</dd>
</dl>

<dl>
<dd>

**temperature:** `typing.Optional[float]` — 采样温度，控制多样性，范围 0~1
    
</dd>
</dl>

<dl>
<dd>

**sample_len:** `typing.Optional[int]` — 采样长度，必须 >= 1
    
</dd>
</dl>

<dl>
<dd>

**best_of:** `typing.Optional[int]` — 在 temperature > 0 时采样 n 次取最佳结果
    
</dd>
</dl>

<dl>
<dd>

**beam_size:** `typing.Optional[int]` — beam search 的宽度，推荐 5~10
    
</dd>
</dl>

<dl>
<dd>

**patience:** `typing.Optional[float]` — beam search 的 patience 参数，越大越宽松
    
</dd>
</dl>

<dl>
<dd>

**length_penalty:** `typing.Optional[float]` — 对生成文本长度的惩罚，负值鼓励短输出
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[SttOutputFormat]` — 输出格式，如 txt, json, srt, vtt
    
</dd>
</dl>

<dl>
<dd>

**highlight_words:** `typing.Optional[bool]` — 是否高亮每个识别的单词（如 JSON 格式）
    
</dd>
</dl>

<dl>
<dd>

**max_line_count:** `typing.Optional[int]` — 最大行数限制（用于格式化输出）
    
</dd>
</dl>

<dl>
<dd>

**max_line_width:** `typing.Optional[int]` — 最大每行字符数（用于 txt 格式）
    
</dd>
</dl>

<dl>
<dd>

**max_words_per_line:** `typing.Optional[int]` — 每行最多几个词（用于格式化输出）
    
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

