# Reference
## Text-to-Speech
<details><summary><code>client.text_to_speech.<a href="src/fern/text_to_speech/client.py">synthesize</a>(...) -> SynthesizeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate speech synchronously from text or SSML. Returns complete audio as base64.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.text_to_speech.synthesize(
    voice_uuid="55592656",
    data="Hello from Resemble!",
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

**voice_uuid:** `str` — Voice UUID to use for synthesis
    
</dd>
</dl>

<dl>
<dd>

**data:** `str` — Text or SSML to synthesize (max 3,000 characters)
    
</dd>
</dl>

<dl>
<dd>

**project_uuid:** `typing.Optional[str]` — Optional project UUID to store the clip
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Optional title for the generated clip
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — Model to use for synthesis. Pass `chatterbox-turbo` to use the Turbo model for lower latency and paralinguistic tag support. If not specified, defaults to Chatterbox or Chatterbox Multilingual based on the voice. Note - Chatterbox-Turbo is supported by all Rapid English voices and Pre Built Library voices.
    
</dd>
</dl>

<dl>
<dd>

**precision:** `typing.Optional[SynthesizeRequestPrecision]` — Audio precision for WAV output
    
</dd>
</dl>

<dl>
<dd>

**output_format:** `typing.Optional[SynthesizeRequestOutputFormat]` — Audio output format
    
</dd>
</dl>

<dl>
<dd>

**sample_rate:** `typing.Optional[int]` — Audio sample rate in Hz
    
</dd>
</dl>

<dl>
<dd>

**use_hd:** `typing.Optional[bool]` — Enable HD synthesis with small latency trade-off
    
</dd>
</dl>

<dl>
<dd>

**apply_custom_pronunciations:** `typing.Optional[bool]` — When true, automatically applies your team's custom pronunciations to matching words in the input text. Defaults to false.
    
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

<details><summary><code>client.text_to_speech.<a href="src/fern/text_to_speech/client.py">stream_synthesize</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stream audio as it's generated. Returns chunked WAV data for progressive playback.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.text_to_speech.stream_synthesize(
    voice_uuid="voice_uuid",
    data="data",
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

**voice_uuid:** `str` — Voice UUID to use for synthesis
    
</dd>
</dl>

<dl>
<dd>

**data:** `str` — Text or SSML to synthesize (max 2000 characters)
    
</dd>
</dl>

<dl>
<dd>

**project_uuid:** `typing.Optional[str]` — Optional project UUID to store the clip
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — Model to use for synthesis. Pass `chatterbox-turbo` to use the Turbo model for lower latency and paralinguistic tag support. If not specified, defaults to Chatterbox or Chatterbox Multilingual based on the voice. Note - Chatterbox-Turbo is supported by all Rapid English voices and Pre Built Library voices.
    
</dd>
</dl>

<dl>
<dd>

**precision:** `typing.Optional[StreamSynthesizeRequestPrecision]` — Audio precision
    
</dd>
</dl>

<dl>
<dd>

**sample_rate:** `typing.Optional[int]` — Audio sample rate in Hz
    
</dd>
</dl>

<dl>
<dd>

**use_hd:** `typing.Optional[bool]` — Enable HD synthesis with small latency trade-off
    
</dd>
</dl>

<dl>
<dd>

**apply_custom_pronunciations:** `typing.Optional[bool]` — When true, automatically applies your team's custom pronunciations to matching words in the input text. Defaults to false.
    
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

## Speech-to-Text
<details><summary><code>client.speech_to_text.<a href="src/fern/speech_to_text/client.py">list_transcripts</a>(...) -> ListTranscriptsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve paginated list of transcript jobs
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.speech_to_text.list_transcripts(
    page=1,
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

**page:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` 
    
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

<details><summary><code>client.speech_to_text.<a href="src/fern/speech_to_text/client.py">create_transcript</a>(...) -> CreateTranscriptResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submit audio or video for transcription
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.speech_to_text.create_transcript()

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

**audio_token:** `typing.Optional[str]` — Signed ActiveStorage token
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — HTTPS URL to audio/video file
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Optional intelligence question
    
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

<details><summary><code>client.speech_to_text.<a href="src/fern/speech_to_text/client.py">get_transcript</a>(...) -> GetTranscriptResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve transcript status, text, and timestamps
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.speech_to_text.get_transcript(
    uuid_="uuid",
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

**uuid:** `str` 
    
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

<details><summary><code>client.speech_to_text.<a href="src/fern/speech_to_text/client.py">ask_transcript_question</a>(...) -> AskTranscriptQuestionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submit a question about a completed transcript
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.speech_to_text.ask_transcript_question(
    uuid_="uuid",
    query="What action items were mentioned?",
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

**uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` — Question to ask about the transcript
    
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

<details><summary><code>client.speech_to_text.<a href="src/fern/speech_to_text/client.py">list_transcript_questions</a>(...) -> ListTranscriptQuestionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all questions asked about a transcript
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.speech_to_text.list_transcript_questions(
    uuid_="uuid",
    page=1,
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

**uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` 
    
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

<details><summary><code>client.speech_to_text.<a href="src/fern/speech_to_text/client.py">get_transcript_question</a>(...) -> GetTranscriptQuestionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check the status of a specific question
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.speech_to_text.get_transcript_question(
    uuid_="uuid",
    question_uuid="question_uuid",
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

**uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**question_uuid:** `str` 
    
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

## Audio Edit
<details><summary><code>client.audio_edit.<a href="src/fern/audio_edit/client.py">list_audio_edits</a>(...) -> ListAudioEditsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve paginated list of audio edits
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.audio_edit.list_audio_edits(
    page=1,
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

**page:** `int` 
    
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

<details><summary><code>client.audio_edit.<a href="src/fern/audio_edit/client.py">create_audio_edit</a>(...) -> CreateAudioEditResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Edit audio segments using voice synthesis
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.audio_edit.create_audio_edit(
    input_audio="example_input_audio",
    original_transcript="original_transcript",
    target_transcript="target_transcript",
    voice_uuid="voice_uuid",
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

**input_audio:** `core.File` — WAV, MP3, M4A, or WMA file (< 20 seconds)
    
</dd>
</dl>

<dl>
<dd>

**original_transcript:** `str` — Accurate transcript of the uploaded audio
    
</dd>
</dl>

<dl>
<dd>

**target_transcript:** `str` — Desired replacement text
    
</dd>
</dl>

<dl>
<dd>

**voice_uuid:** `str` — Voice used to render the edited segment
    
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

<details><summary><code>client.audio_edit.<a href="src/fern/audio_edit/client.py">get_audio_edit</a>(...) -> GetAudioEditResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get status and result of an audio edit
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.audio_edit.get_audio_edit(
    audio_edit_uuid="audio_edit_uuid",
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

**audio_edit_uuid:** `str` 
    
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

## Audio Enhancement
<details><summary><code>client.audio_enhancement.<a href="src/fern/audio_enhancement/client.py">list_audio_enhancements</a>(...) -> ListAudioEnhancementsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of all audio enhancements for your team, ordered by most recent first.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.audio_enhancement.list_audio_enhancements(
    page=1,
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

**page:** `int` — Page number (starting from 1).
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Items per page (10 to 1000). Default 10.
    
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

<details><summary><code>client.audio_enhancement.<a href="src/fern/audio_enhancement/client.py">create_audio_enhancement</a>(...) -> CreateAudioEnhancementResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submit an audio file for enhancement. Processing happens asynchronously in the background.
The API defaults to the v2 enhancement engine. The v1 engine is legacy and will be sunset in a future release.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.audio_enhancement.create_audio_enhancement(
    audio_file="example_audio_file",
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

**audio_file:** `core.File` — Audio file to enhance (WAV, MP3, M4A, MP4, OGG, AAC, FLAC). Max 150 MB.
    
</dd>
</dl>

<dl>
<dd>

**enhancement_engine:** `typing.Optional[CreateAudioEnhancementRequestEnhancementEngine]` — Enhancement engine to use. Default is v2.
    
</dd>
</dl>

<dl>
<dd>

**remove_noise:** `typing.Optional[bool]` — Remove background noise. Engine v2 only.
    
</dd>
</dl>

<dl>
<dd>

**normalize:** `typing.Optional[bool]` — Normalize audio levels. Engine v2 only.
    
</dd>
</dl>

<dl>
<dd>

**studio_sound:** `typing.Optional[bool]` — Apply studio-quality enhancement. Engine v2 only.
    
</dd>
</dl>

<dl>
<dd>

**enhancement_level:** `typing.Optional[float]` — Enhancement intensity (0.0 to 1.0). Engine v1 only (legacy).
    
</dd>
</dl>

<dl>
<dd>

**loudness_target_level:** `typing.Optional[int]` — Target loudness in LUFS. Engine v1 only (legacy).
    
</dd>
</dl>

<dl>
<dd>

**loudness_peak_limit:** `typing.Optional[int]` — Peak limit in dBTP. Engine v1 only (legacy).
    
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

<details><summary><code>client.audio_enhancement.<a href="src/fern/audio_enhancement/client.py">get_audio_enhancement</a>(...) -> GetAudioEnhancementResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Poll this endpoint to check the status of an enhancement job and retrieve the download URL when complete.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.audio_enhancement.get_audio_enhancement(
    enhancement_uuid="enhancement_uuid",
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

**enhancement_uuid:** `str` — The UUID returned from the create endpoint.
    
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

## Agents
<details><summary><code>client.agents.<a href="src/fern/agents/client.py">list_agents</a>(...) -> ListAgentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all agents for the authenticated team
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agents.list_agents()

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

**phone_number:** `typing.Optional[str]` — Filter by associated phone number
    
</dd>
</dl>

<dl>
<dd>

**advanced:** `typing.Optional[bool]` — Include detailed configuration
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">create_agent</a>(...) -> CreateAgentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new voice agent
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agents.create_agent(
    name="name",
    voice_uuid="voice_uuid",
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

**voice_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**phone_number_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**languages:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**dynamic_variables:** `typing.Optional[typing.Dict[str, CreateAgentRequestDynamicVariablesValue]]` 
    
</dd>
</dl>

<dl>
<dd>

**asr:** `typing.Optional[CreateAgentRequestAsr]` 
    
</dd>
</dl>

<dl>
<dd>

**turn:** `typing.Optional[CreateAgentRequestTurn]` 
    
</dd>
</dl>

<dl>
<dd>

**llm:** `typing.Optional[CreateAgentRequestLlm]` 
    
</dd>
</dl>

<dl>
<dd>

**search_mode:** `typing.Optional[CreateAgentRequestSearchMode]` — RAG search strategy - speed (faster) or accuracy (more thorough)
    
</dd>
</dl>

<dl>
<dd>

**max_chunks_per_query:** `typing.Optional[int]` — Number of relevant chunks to retrieve per query for RAG
    
</dd>
</dl>

<dl>
<dd>

**webhooks:** `typing.Optional[typing.List[typing.Dict[str, typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**system_tools:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">get_agent</a>(...) -> GetAgentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific agent's details
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agents.get_agent(
    uuid_="uuid",
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

**uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**advanced:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">delete_agent</a>(...) -> DeleteAgentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an agent and all its configurations
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agents.delete_agent(
    uuid_="uuid",
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

**uuid:** `str` 
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">update_agent</a>(...) -> UpdateAgentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing agent's configuration
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agents.update_agent(
    uuid_="uuid",
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

**uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**voice_uuid:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**phone_number_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**languages:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**dynamic_variables:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**asr:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**turn:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**llm:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**search_mode:** `typing.Optional[UpdateAgentRequestSearchMode]` — RAG search strategy
    
</dd>
</dl>

<dl>
<dd>

**max_chunks_per_query:** `typing.Optional[int]` — Number of chunks to retrieve per query for RAG
    
</dd>
</dl>

<dl>
<dd>

**webhooks:** `typing.Optional[typing.List[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**system_tools:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">dispatch_agent</a>(...) -> DispatchAgentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Make an outbound call with an agent
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agents.dispatch_agent(
    uuid_="uuid",
    phone_number="phone_number",
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

**uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `str` — Destination phone number
    
</dd>
</dl>

<dl>
<dd>

**dynamic_variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Runtime variable overrides
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">get_agent_capabilities</a>() -> GetAgentCapabilitiesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List supported ASR and LLM providers and models
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agents.get_agent_capabilities()

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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">get_system_tools</a>() -> GetSystemToolsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List available system tools
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agents.get_system_tools()

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

## Agent Tools
<details><summary><code>client.agent_tools.<a href="src/fern/agent_tools/client.py">list_agent_tools</a>(...) -> ListAgentToolsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all tools for an agent
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agent_tools.list_agent_tools(
    agent_uuid="agent_uuid",
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

**agent_uuid:** `str` 
    
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

<details><summary><code>client.agent_tools.<a href="src/fern/agent_tools/client.py">create_agent_tool</a>(...) -> CreateAgentToolResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new tool for an agent
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agent_tools.create_agent_tool(
    agent_uuid="agent_uuid",
    name="name",
    description="description",
    tool_type="webhook",
    tool_config={
        "key": "value"
    },
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

**agent_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tool_type:** `CreateAgentToolRequestToolType` 
    
</dd>
</dl>

<dl>
<dd>

**tool_config:** `typing.Dict[str, typing.Any]` 
    
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

<details><summary><code>client.agent_tools.<a href="src/fern/agent_tools/client.py">get_agent_tool</a>(...) -> GetAgentToolResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a specific tool
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agent_tools.get_agent_tool(
    agent_uuid="agent_uuid",
    tool_uuid="tool_uuid",
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

**agent_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tool_uuid:** `str` 
    
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

<details><summary><code>client.agent_tools.<a href="src/fern/agent_tools/client.py">delete_agent_tool</a>(...) -> DeleteAgentToolResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a tool
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agent_tools.delete_agent_tool(
    agent_uuid="agent_uuid",
    tool_uuid="tool_uuid",
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

**agent_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tool_uuid:** `str` 
    
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

<details><summary><code>client.agent_tools.<a href="src/fern/agent_tools/client.py">update_agent_tool</a>(...) -> UpdateAgentToolResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing tool
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agent_tools.update_agent_tool(
    agent_uuid="agent_uuid",
    tool_uuid="tool_uuid",
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

**agent_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tool_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**tool_config:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
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

## Agent Webhooks
<details><summary><code>client.agent_webhooks.<a href="src/fern/agent_webhooks/client.py">list_agent_webhooks</a>(...) -> ListAgentWebhooksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all webhooks for an agent
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agent_webhooks.list_agent_webhooks(
    agent_uuid="agent_uuid",
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

**agent_uuid:** `str` 
    
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

<details><summary><code>client.agent_webhooks.<a href="src/fern/agent_webhooks/client.py">create_agent_webhook</a>(...) -> CreateAgentWebhookResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new webhook for an agent
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agent_webhooks.create_agent_webhook(
    agent_uuid="agent_uuid",
    webhook_type="pre_call",
    webhook_config={
        "key": "value"
    },
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

**agent_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_type:** `CreateAgentWebhookRequestWebhookType` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_config:** `typing.Dict[str, typing.Any]` 
    
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

<details><summary><code>client.agent_webhooks.<a href="src/fern/agent_webhooks/client.py">get_agent_webhook</a>(...) -> GetAgentWebhookResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a specific webhook
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agent_webhooks.get_agent_webhook(
    agent_uuid="agent_uuid",
    webhook_uuid="webhook_uuid",
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

**agent_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_uuid:** `str` 
    
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

<details><summary><code>client.agent_webhooks.<a href="src/fern/agent_webhooks/client.py">delete_agent_webhook</a>(...) -> DeleteAgentWebhookResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a webhook
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agent_webhooks.delete_agent_webhook(
    agent_uuid="agent_uuid",
    webhook_uuid="webhook_uuid",
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

**agent_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_uuid:** `str` 
    
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

<details><summary><code>client.agent_webhooks.<a href="src/fern/agent_webhooks/client.py">update_agent_webhook</a>(...) -> UpdateAgentWebhookResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing webhook
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agent_webhooks.update_agent_webhook(
    agent_uuid="agent_uuid",
    webhook_uuid="webhook_uuid",
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

**agent_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_config:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
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

## Agent Phone Numbers
<details><summary><code>client.agent_phone_numbers.<a href="src/fern/agent_phone_numbers/client.py">list_phone_numbers</a>() -> ListPhoneNumbersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all agent phone numbers
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agent_phone_numbers.list_phone_numbers()

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

<details><summary><code>client.agent_phone_numbers.<a href="src/fern/agent_phone_numbers/client.py">create_phone_number</a>(...) -> CreatePhoneNumberResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new agent phone number
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agent_phone_numbers.create_phone_number(
    phone_number="phone_number",
    label="label",
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

**phone_number:** `str` — E.164 formatted phone number
    
</dd>
</dl>

<dl>
<dd>

**label:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**supports_inbound:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**supports_outbound:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[CreatePhoneNumberRequestProvider]` 
    
</dd>
</dl>

<dl>
<dd>

**twilio_account_sid:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**twilio_auth_token:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**outbound_trunk:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**inbound_trunk:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
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

<details><summary><code>client.agent_phone_numbers.<a href="src/fern/agent_phone_numbers/client.py">get_phone_number</a>(...) -> GetPhoneNumberResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get agent phone number details
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agent_phone_numbers.get_phone_number(
    id=1,
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

**id:** `int` 
    
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

<details><summary><code>client.agent_phone_numbers.<a href="src/fern/agent_phone_numbers/client.py">delete_phone_number</a>(...) -> DeletePhoneNumberResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an agent phone number
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agent_phone_numbers.delete_phone_number(
    id=1,
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

**id:** `int` 
    
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

<details><summary><code>client.agent_phone_numbers.<a href="src/fern/agent_phone_numbers/client.py">force_delete_phone_number</a>(...) -> ForceDeletePhoneNumberResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Force delete an agent phone number even if linked to agent
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agent_phone_numbers.force_delete_phone_number(
    id=1,
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

**id:** `int` 
    
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

## Agent Knowledge Base
<details><summary><code>client.agent_knowledge_base.<a href="src/fern/agent_knowledge_base/client.py">list_knowledge_items</a>(...) -> ListKnowledgeItemsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all knowledge items belonging to the authenticated user's team
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agent_knowledge_base.list_knowledge_items()

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

**status:** `typing.Optional[ListKnowledgeItemsRequestStatus]` — Filter by status
    
</dd>
</dl>

<dl>
<dd>

**source_type:** `typing.Optional[ListKnowledgeItemsRequestSourceType]` — Filter by source type
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Items per page
    
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

<details><summary><code>client.agent_knowledge_base.<a href="src/fern/agent_knowledge_base/client.py">create_knowledge_item</a>(...) -> CreateKnowledgeItemResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new knowledge item and queues it for ingestion processing
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agent_knowledge_base.create_knowledge_item(
    title="title",
    description="description",
    source_type="document",
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

**title:** `str` — Title of the knowledge item
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — Description of the knowledge item
    
</dd>
</dl>

<dl>
<dd>

**source_type:** `CreateKnowledgeItemRequestSourceType` — Type of knowledge source
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — Required when source_type is url
    
</dd>
</dl>

<dl>
<dd>

**raw_text:** `typing.Optional[str]` — Required when source_type is text
    
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

<details><summary><code>client.agent_knowledge_base.<a href="src/fern/agent_knowledge_base/client.py">get_knowledge_item</a>(...) -> GetKnowledgeItemResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a single knowledge item with detailed information including attached agents
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agent_knowledge_base.get_knowledge_item(
    uuid_="uuid",
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

**uuid:** `str` — The UUID of the knowledge item
    
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

<details><summary><code>client.agent_knowledge_base.<a href="src/fern/agent_knowledge_base/client.py">delete_knowledge_item</a>(...) -> DeleteKnowledgeItemResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a knowledge item and cleans up associated data
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agent_knowledge_base.delete_knowledge_item(
    uuid_="uuid",
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

**uuid:** `str` — The UUID of the knowledge item
    
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

<details><summary><code>client.agent_knowledge_base.<a href="src/fern/agent_knowledge_base/client.py">reingest_knowledge_item</a>(...) -> ReingestKnowledgeItemResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Re-runs the ingestion pipeline for an existing knowledge item
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agent_knowledge_base.reingest_knowledge_item(
    uuid_="uuid",
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

**uuid:** `str` — The UUID of the knowledge item
    
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

<details><summary><code>client.agent_knowledge_base.<a href="src/fern/agent_knowledge_base/client.py">list_agent_knowledge_items</a>(...) -> ListAgentKnowledgeItemsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all knowledge items attached to a specific agent
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agent_knowledge_base.list_agent_knowledge_items(
    agent_uuid="agent_uuid",
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

**agent_uuid:** `str` — The UUID of the agent
    
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

<details><summary><code>client.agent_knowledge_base.<a href="src/fern/agent_knowledge_base/client.py">attach_knowledge_item_to_agent</a>(...) -> AttachKnowledgeItemToAgentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attaches an existing knowledge item to an agent
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agent_knowledge_base.attach_knowledge_item_to_agent(
    agent_uuid="agent_uuid",
    knowledge_item_uuid="knowledge_item_uuid",
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

**agent_uuid:** `str` — The UUID of the agent
    
</dd>
</dl>

<dl>
<dd>

**knowledge_item_uuid:** `str` — The UUID of the knowledge item to attach
    
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

<details><summary><code>client.agent_knowledge_base.<a href="src/fern/agent_knowledge_base/client.py">detach_knowledge_item_from_agent</a>(...) -> DetachKnowledgeItemFromAgentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes a knowledge item from an agent
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.agent_knowledge_base.detach_knowledge_item_from_agent(
    agent_uuid="agent_uuid",
    knowledge_item_uuid="knowledge_item_uuid",
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

**agent_uuid:** `str` — The UUID of the agent
    
</dd>
</dl>

<dl>
<dd>

**knowledge_item_uuid:** `str` — The UUID of the knowledge item to detach
    
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

## Deepfake Detection
<details><summary><code>client.deepfake_detection.<a href="src/fern/deepfake_detection/client.py">list_detections</a>(...) -> ListDetectionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a paginated list of all detect objects for the authenticated user's team
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.deepfake_detection.list_detections(
    page=1,
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

**page:** `int` — Page number (must be >= 1)
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of items per page (10-1000)
    
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

<details><summary><code>client.deepfake_detection.<a href="src/fern/deepfake_detection/client.py">create_detection</a>(...) -> CreateDetectionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Analyze audio, image, and video for deepfake detection
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.deepfake_detection.create_detection(
    url="url",
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

**url:** `str` — HTTPS URL to audio, image, or video file
    
</dd>
</dl>

<dl>
<dd>

**callback_url:** `typing.Optional[str]` — POST destination when analysis completes
    
</dd>
</dl>

<dl>
<dd>

**visualize:** `typing.Optional[bool]` — Generate visualization artifacts
    
</dd>
</dl>

<dl>
<dd>

**frame_length:** `typing.Optional[int]` — Window size in seconds (audio/video)
    
</dd>
</dl>

<dl>
<dd>

**start_region:** `typing.Optional[float]` — Start of segment to analyze (seconds)
    
</dd>
</dl>

<dl>
<dd>

**end_region:** `typing.Optional[float]` — End of segment to analyze (seconds)
    
</dd>
</dl>

<dl>
<dd>

**max_video_fps:** `typing.Optional[float]` — Downsample high-frame-rate media
    
</dd>
</dl>

<dl>
<dd>

**max_video_secs:** `typing.Optional[float]` — Cap processed duration
    
</dd>
</dl>

<dl>
<dd>

**model_types:** `typing.Optional[CreateDetectionRequestModelTypes]` — Use talking_head for face-swaps
    
</dd>
</dl>

<dl>
<dd>

**intelligence:** `typing.Optional[bool]` — Run multimodal intelligence analysis on the media
    
</dd>
</dl>

<dl>
<dd>

**audio_source_tracing:** `typing.Optional[bool]` — Enable audio source tracing to identify synthetic audio origin
    
</dd>
</dl>

<dl>
<dd>

**use_reverse_search:** `typing.Optional[bool]` — Enable reverse image search to improve detection accuracy for image files. Searches the web for matching images and uses AI to classify whether the match indicates a known fake. Only applies to image detections.
    
</dd>
</dl>

<dl>
<dd>

**use_ood_detector:** `typing.Optional[bool]` — Enable out-of-distribution detection
    
</dd>
</dl>

<dl>
<dd>

**zero_retention_mode:** `typing.Optional[bool]` — Enable Zero Retention Mode to automatically delete submitted media after detection completes. When enabled, media URLs are redacted and the filename is tokenized.
    
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

<details><summary><code>client.deepfake_detection.<a href="src/fern/deepfake_detection/client.py">get_detection</a>(...) -> GetDetectionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get deepfake detection result by UUID
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.deepfake_detection.get_detection(
    uuid_="uuid",
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

**uuid:** `str` — The UUID of the detect object
    
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

## Intelligence
<details><summary><code>client.intelligence.<a href="src/fern/intelligence/client.py">run_intelligence</a>(...) -> RunIntelligenceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Analyze audio, image, or video for comprehensive insights. Optionally reference an existing detect to associate.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.intelligence.run_intelligence()

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

**media_token:** `typing.Optional[str]` — Token for uploaded media file (from secure upload)
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — HTTPS URL to audio, image, or video file
    
</dd>
</dl>

<dl>
<dd>

**detect_id:** `typing.Optional[str]` — UUID of an existing detect to associate
    
</dd>
</dl>

<dl>
<dd>

**media_type:** `typing.Optional[RunIntelligenceRequestMediaType]` — Explicit media type (auto-detected if not provided)
    
</dd>
</dl>

<dl>
<dd>

**json:** `typing.Optional[bool]` — Return structured fields instead of prose. Default false for audio/video, true for images.
    
</dd>
</dl>

<dl>
<dd>

**callback_url:** `typing.Optional[str]` — URL that receives the final intelligence payload via HTTP POST. When present, the request runs asynchronously and returns 202 Accepted.
    
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

<details><summary><code>client.intelligence.<a href="src/fern/intelligence/client.py">list_intelligences</a>(...) -> ListIntelligencesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a paginated list of all intelligence reports for the authenticated user's team
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.intelligence.list_intelligences(
    page=1,
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

**page:** `int` — Page number (must be >= 1)
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of items per page (10-1000)
    
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

<details><summary><code>client.intelligence.<a href="src/fern/intelligence/client.py">get_intelligence</a>(...) -> GetIntelligenceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a single intelligence report by its UUID
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.intelligence.get_intelligence(
    uuid_="uuid",
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

**uuid:** `str` — The UUID of the intelligence report
    
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

## Detect Intelligence
<details><summary><code>client.detect_intelligence.<a href="src/fern/detect_intelligence/client.py">ask_detect_intelligence_question</a>(...) -> AskDetectIntelligenceQuestionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submit a natural-language question about a completed detection report. Returns 202 Accepted while the answer is generated in the background.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.detect_intelligence.ask_detect_intelligence_question(
    uuid_="uuid",
    query="query",
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

**uuid:** `str` — UUID of the completed detection report
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` — The natural-language question to ask about the detection
    
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

<details><summary><code>client.detect_intelligence.<a href="src/fern/detect_intelligence/client.py">get_detect_intelligence_question</a>(...) -> GetDetectIntelligenceQuestionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the status and answer for a previously submitted question. Poll until status is completed or failed.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.detect_intelligence.get_detect_intelligence_question(
    uuid_="uuid",
    question_uuid="question_uuid",
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

**uuid:** `str` — UUID of the detection report
    
</dd>
</dl>

<dl>
<dd>

**question_uuid:** `str` — UUID of the question
    
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

## Audio Source Tracing
<details><summary><code>client.audio_source_tracing.<a href="src/fern/audio_source_tracing/client.py">list_audio_source_tracings</a>(...) -> ListAudioSourceTracingsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a paginated list of all source tracing reports for the authenticated user's team
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.audio_source_tracing.list_audio_source_tracings(
    page=1,
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

**page:** `int` — Page number (must be >= 1)
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of items per page (10-1000)
    
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

<details><summary><code>client.audio_source_tracing.<a href="src/fern/audio_source_tracing/client.py">get_audio_source_tracing</a>(...) -> GetAudioSourceTracingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a single source tracing report by its UUID
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.audio_source_tracing.get_audio_source_tracing(
    uuid_="uuid",
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

**uuid:** `str` — The UUID of the source tracing report
    
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

## Identity
<details><summary><code>client.identity.<a href="src/fern/identity/client.py">list_identities</a>() -> ListIdentitiesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all speaker identities
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.identity.list_identities()

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

<details><summary><code>client.identity.<a href="src/fern/identity/client.py">create_identity</a>(...) -> CreateIdentityResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new speaker identity
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.identity.create_identity(
    audio_url="audio_url",
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

**audio_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
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

<details><summary><code>client.identity.<a href="src/fern/identity/client.py">search_identities</a>(...) -> SearchIdentitiesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for matching speaker identities
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.identity.search_identities(
    audio_url="audio_url",
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

**audio_url:** `str` 
    
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

## Watermark
<details><summary><code>client.watermark.<a href="src/fern/watermark/client.py">apply_watermark</a>(...) -> ApplyWatermarkResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Apply a watermark to an audio, image, or video file. The media type is automatically detected from the file content. Use the `Prefer: wait` header for synchronous processing.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.watermark.apply_watermark(
    url="url",
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

**url:** `str` — HTTPS URL to the media file (audio, image, or video).
    
</dd>
</dl>

<dl>
<dd>

**prefer:** `typing.Optional[ApplyWatermarkRequestPrefer]` — When set to "wait", the API processes synchronously and returns the completed result.
    
</dd>
</dl>

<dl>
<dd>

**strength:** `typing.Optional[float]` — Watermark strength for image/video. Ignored for audio.
    
</dd>
</dl>

<dl>
<dd>

**custom_message:** `typing.Optional[str]` — Custom message to embed for image/video. Ignored for audio.
    
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

<details><summary><code>client.watermark.<a href="src/fern/watermark/client.py">get_watermark_apply_result</a>(...) -> GetWatermarkApplyResultResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the result of a watermark apply job.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.watermark.get_watermark_apply_result(
    uuid_="uuid",
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

**uuid:** `str` 
    
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

<details><summary><code>client.watermark.<a href="src/fern/watermark/client.py">detect_watermark</a>(...) -> DetectWatermarkResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Detect a watermark in an audio, image, or video file. The media type is automatically detected from the file content. Use the `Prefer: wait` header for synchronous processing.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.watermark.detect_watermark(
    url="url",
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

**url:** `str` — HTTPS URL to the media file (audio, image, or video).
    
</dd>
</dl>

<dl>
<dd>

**prefer:** `typing.Optional[DetectWatermarkRequestPrefer]` — When set to "wait", the API processes synchronously and returns the completed result with metrics.
    
</dd>
</dl>

<dl>
<dd>

**custom_message:** `typing.Optional[str]` — Custom message used during encoding for image/video. Ignored for audio.
    
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

<details><summary><code>client.watermark.<a href="src/fern/watermark/client.py">get_watermark_detection_result</a>(...) -> GetWatermarkDetectionResultResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the result of a watermark detection.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.watermark.get_watermark_detection_result(
    uuid_="uuid",
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

**uuid:** `str` 
    
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

## Voices
<details><summary><code>client.voices.<a href="src/fern/voices/client.py">list_voices</a>(...) -> ListVoicesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve voice metadata
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.voices.list_voices(
    page=1,
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

**page:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**advanced:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.voices.<a href="src/fern/voices/client.py">create_voice</a>(...) -> CreateVoiceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new voice
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.voices.create_voice(
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

**voice_type:** `typing.Optional[CreateVoiceRequestVoiceType]` 
    
</dd>
</dl>

<dl>
<dd>

**dataset_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**callback_uri:** `typing.Optional[str]` 
    
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

<details><summary><code>client.voices.<a href="src/fern/voices/client.py">get_voice</a>(...) -> GetVoiceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get voice details
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.voices.get_voice(
    voice_uuid="voice_uuid",
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

**voice_uuid:** `str` 
    
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

<details><summary><code>client.voices.<a href="src/fern/voices/client.py">delete_voice</a>(...) -> DeleteVoiceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a voice
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.voices.delete_voice(
    voice_uuid="voice_uuid",
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

**voice_uuid:** `str` 
    
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

<details><summary><code>client.voices.<a href="src/fern/voices/client.py">build_voice</a>(...) -> BuildVoiceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start voice training
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.voices.build_voice(
    voice_uuid="voice_uuid",
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

**voice_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fill:** `typing.Optional[bool]` 
    
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

## Voice Design
<details><summary><code>client.voice_design.<a href="src/fern/voice_design/client.py">generate_voice_design</a>(...) -> GenerateVoiceDesignResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate three voice candidates from a text prompt
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.voice_design.generate_voice_design(
    user_prompt="user_prompt",
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

**user_prompt:** `str` — Description of desired voice
    
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

<details><summary><code>client.voice_design.<a href="src/fern/voice_design/client.py">create_voice_from_candidate</a>(...) -> CreateVoiceFromCandidateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a voice from a voice design candidate
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.voice_design.create_voice_from_candidate(
    uuid_="uuid",
    voice_sample_index=1,
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

**uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**voice_sample_index:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
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

## Recordings
<details><summary><code>client.recordings.<a href="src/fern/recordings/client.py">list_recordings</a>(...) -> ListRecordingsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all recordings for a voice
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.recordings.list_recordings(
    voice_uuid="voice_uuid",
    page=1,
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

**voice_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
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

<details><summary><code>client.recordings.<a href="src/fern/recordings/client.py">create_recording</a>(...) -> CreateRecordingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a new recording for voice training
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.recordings.create_recording(
    voice_uuid="voice_uuid",
    file="example_file",
    name="name",
    text="text",
    emotion="emotion",
    is_active=True,
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

**voice_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file:** `core.File` — Audio file (WAV recommended, 1-12 seconds)
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Display name
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — Transcript of the clip
    
</dd>
</dl>

<dl>
<dd>

**emotion:** `str` — Emotion label
    
</dd>
</dl>

<dl>
<dd>

**is_active:** `bool` — Include in training
    
</dd>
</dl>

<dl>
<dd>

**fill:** `typing.Optional[bool]` — Include for Resemble Fill
    
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

<details><summary><code>client.recordings.<a href="src/fern/recordings/client.py">get_recording</a>(...) -> GetRecordingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get recording details
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.recordings.get_recording(
    voice_uuid="voice_uuid",
    recording_id="recording_id",
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

**voice_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**recording_id:** `str` 
    
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

<details><summary><code>client.recordings.<a href="src/fern/recordings/client.py">delete_recording</a>(...) -> DeleteRecordingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a recording
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.recordings.delete_recording(
    voice_uuid="voice_uuid",
    recording_id="recording_id",
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

**voice_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**recording_id:** `str` 
    
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

<details><summary><code>client.recordings.<a href="src/fern/recordings/client.py">update_recording</a>(...) -> UpdateRecordingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a recording
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.recordings.update_recording(
    voice_uuid="voice_uuid",
    recording_id="recording_id",
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

**voice_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**recording_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**emotion:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**is_active:** `typing.Optional[bool]` 
    
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

## Term Substitutions
<details><summary><code>client.term_substitutions.<a href="src/fern/term_substitutions/client.py">list_term_substitutions</a>(...) -> ListTermSubstitutionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all term substitutions
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.term_substitutions.list_term_substitutions(
    page=1,
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

**page:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
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

<details><summary><code>client.term_substitutions.<a href="src/fern/term_substitutions/client.py">create_term_substitution</a>(...) -> CreateTermSubstitutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new pronunciation substitution
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.term_substitutions.create_term_substitution(
    original_text="original_text",
    replacement_text="replacement_text",
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

**original_text:** `str` — Original text to substitute
    
</dd>
</dl>

<dl>
<dd>

**replacement_text:** `str` — Replacement pronunciation
    
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

<details><summary><code>client.term_substitutions.<a href="src/fern/term_substitutions/client.py">get_term_substitution</a>(...) -> GetTermSubstitutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get term substitution details
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.term_substitutions.get_term_substitution(
    id=1,
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

**id:** `int` 
    
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

<details><summary><code>client.term_substitutions.<a href="src/fern/term_substitutions/client.py">delete_term_substitution</a>(...) -> DeleteTermSubstitutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a term substitution
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.term_substitutions.delete_term_substitution(
    id=1,
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

**id:** `int` 
    
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

## Custom Pronunciations
<details><summary><code>client.custom_pronunciations.<a href="src/fern/custom_pronunciations/client.py">list_pronunciations</a>(...) -> ListPronunciationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all custom pronunciations for your team, with optional filters.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.custom_pronunciations.list_pronunciations()

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

**language:** `typing.Optional[str]` — Filter by language (e.g., en-us)
    
</dd>
</dl>

<dl>
<dd>

**domain:** `typing.Optional[str]` — Filter by domain (e.g., medical)
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListPronunciationsRequestStatus]` — Filter by processing status
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` — Filter by active state
    
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

<details><summary><code>client.custom_pronunciations.<a href="src/fern/custom_pronunciations/client.py">create_pronunciation</a>(...) -> CreatePronunciationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a single pronunciation with a reference audio file.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.custom_pronunciations.create_pronunciation(
    audio="example_audio",
    word="word",
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

**word:** `str` — The word or phrase (2-100 characters). Letters, accented characters, apostrophes, hyphens, and spaces only.
    
</dd>
</dl>

<dl>
<dd>

**audio:** `core.File` — Reference audio file (wav, flac, mp3, m4a, ogg, webm, aac). Duration 200ms-10s. Max 10MB.
    
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

<details><summary><code>client.custom_pronunciations.<a href="src/fern/custom_pronunciations/client.py">bulk_create_pronunciations</a>(...) -> BulkCreatePronunciationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload multiple pronunciations at once. Each audio file in the ZIP becomes a pronunciation — the filename (without extension) is used as the word.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.custom_pronunciations.bulk_create_pronunciations(
    zip="example_zip",
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

**zip:** `core.File` — ZIP file containing audio files. Max 50 files, max 100MB total.
    
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

<details><summary><code>client.custom_pronunciations.<a href="src/fern/custom_pronunciations/client.py">get_pronunciation</a>(...) -> GetPronunciationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a single custom pronunciation by UUID
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.custom_pronunciations.get_pronunciation(
    uuid_="uuid",
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

**uuid:** `str` 
    
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

<details><summary><code>client.custom_pronunciations.<a href="src/fern/custom_pronunciations/client.py">delete_pronunciation</a>(...) -> DeletePronunciationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently remove a custom pronunciation. Takes effect immediately.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.custom_pronunciations.delete_pronunciation(
    uuid_="uuid",
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

**uuid:** `str` 
    
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

<details><summary><code>client.custom_pronunciations.<a href="src/fern/custom_pronunciations/client.py">update_pronunciation</a>(...) -> UpdatePronunciationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enable or disable a pronunciation without deleting it. Inactive pronunciations are not used during synthesis.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.custom_pronunciations.update_pronunciation(
    uuid_="uuid",
    active=True,
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

**uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**active:** `bool` — Set to false to disable, true to re-enable
    
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

## Voice Settings Presets
<details><summary><code>client.voice_settings_presets.<a href="src/fern/voice_settings_presets/client.py">list_voice_settings_presets</a>() -> ListVoiceSettingsPresetsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all voice settings presets
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.voice_settings_presets.list_voice_settings_presets()

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

<details><summary><code>client.voice_settings_presets.<a href="src/fern/voice_settings_presets/client.py">create_voice_settings_preset</a>(...) -> CreateVoiceSettingsPresetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new voice settings preset (max 5 per user)
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.voice_settings_presets.create_voice_settings_preset(
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

**name:** `str` — Preset name (unique, max 30 characters)
    
</dd>
</dl>

<dl>
<dd>

**pace:** `typing.Optional[float]` — Speech pace/speed
    
</dd>
</dl>

<dl>
<dd>

**temperature:** `typing.Optional[float]` — Voice variation
    
</dd>
</dl>

<dl>
<dd>

**pitch:** `typing.Optional[float]` — Voice pitch adjustment
    
</dd>
</dl>

<dl>
<dd>

**use_hd:** `typing.Optional[bool]` — Use HD quality
    
</dd>
</dl>

<dl>
<dd>

**exaggeration:** `typing.Optional[float]` — Emotional exaggeration
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Voice style prompt
    
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

<details><summary><code>client.voice_settings_presets.<a href="src/fern/voice_settings_presets/client.py">get_voice_settings_preset</a>(...) -> GetVoiceSettingsPresetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get preset details
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.voice_settings_presets.get_voice_settings_preset(
    uuid_="uuid",
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

**uuid:** `str` 
    
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

<details><summary><code>client.voice_settings_presets.<a href="src/fern/voice_settings_presets/client.py">delete_voice_settings_preset</a>(...) -> DeleteVoiceSettingsPresetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a preset
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.voice_settings_presets.delete_voice_settings_preset(
    uuid_="uuid",
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

**uuid:** `str` 
    
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

<details><summary><code>client.voice_settings_presets.<a href="src/fern/voice_settings_presets/client.py">update_voice_settings_preset</a>(...) -> UpdateVoiceSettingsPresetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a preset
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.voice_settings_presets.update_voice_settings_preset(
    uuid_="uuid",
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

**uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**pace:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**pitch:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**use_hd:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**exaggeration:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
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

## Projects
<details><summary><code>client.projects.<a href="src/fern/projects/client.py">list_projects</a>(...) -> ListProjectsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all projects
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.projects.list_projects(
    page=1,
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

**page:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">create_project</a>(...) -> CreateProjectResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new project
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.projects.create_project(
    name="name",
    description="description",
    is_collaborative=True,
    is_archived=True,
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

**description:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**is_collaborative:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**is_archived:** `bool` 
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">get_project</a>(...) -> GetProjectResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get project details
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.projects.get_project(
    project_uuid="project_uuid",
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

**project_uuid:** `str` 
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">update_project</a>(...) -> UpdateProjectResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a project
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.projects.update_project(
    project_uuid="project_uuid",
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

**project_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**is_collaborative:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**is_archived:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">delete_project</a>(...) -> DeleteProjectResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a project
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.projects.delete_project(
    project_uuid="project_uuid",
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

**project_uuid:** `str` 
    
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

## Clips
<details><summary><code>client.clips.<a href="src/fern/clips/client.py">list_clips</a>(...) -> ListClipsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List clips in a project
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.clips.list_clips(
    project_uuid="project_uuid",
    page=1,
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

**project_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
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

<details><summary><code>client.clips.<a href="src/fern/clips/client.py">get_clip</a>(...) -> GetClipResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get clip details
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.clips.get_clip(
    project_uuid="project_uuid",
    clip_uuid="clip_uuid",
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

**project_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**clip_uuid:** `str` 
    
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

<details><summary><code>client.clips.<a href="src/fern/clips/client.py">delete_clip</a>(...) -> DeleteClipResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a clip
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.clips.delete_clip(
    project_uuid="project_uuid",
    clip_uuid="clip_uuid",
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

**project_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**clip_uuid:** `str` 
    
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

<details><summary><code>client.clips.<a href="src/fern/clips/client.py">update_clip</a>(...) -> UpdateClipResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a clip
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.clips.update_clip(
    project_uuid="project_uuid",
    clip_uuid="clip_uuid",
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

**project_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**clip_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**is_archived:** `typing.Optional[bool]` 
    
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

## Account
<details><summary><code>client.account.<a href="src/fern/account/client.py">get_account</a>() -> GetAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get account information
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.account.get_account()

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

<details><summary><code>client.account.<a href="src/fern/account/client.py">get_teams</a>() -> GetTeamsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get team information
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.account.get_teams()

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

<details><summary><code>client.account.<a href="src/fern/account/client.py">get_team</a>(...) -> GetTeamResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get specific team information
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.account.get_team(
    team_uuid="team_uuid",
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

**team_uuid:** `str` 
    
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

<details><summary><code>client.account.<a href="src/fern/account/client.py">get_billing_usage</a>() -> GetBillingUsageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get billing and usage information
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.account.get_billing_usage()

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

## Duets
<details><summary><code>client.duets.<a href="src/fern/duets/client.py">list_duet_voices</a>() -> ListDuetVoicesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns default and custom duet voices
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.duets.list_duet_voices()

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

<details><summary><code>client.duets.<a href="src/fern/duets/client.py">create_duet_voice</a>(...) -> CreateDuetVoiceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a custom voice for duet generation
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.duets.create_duet_voice(
    audio="example_audio",
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

**name:** `str` — Voice name
    
</dd>
</dl>

<dl>
<dd>

**audio:** `core.File` — Audio file (MP3/WAV/M4A/OGG/AAC/FLAC max 10 MB)
    
</dd>
</dl>

<dl>
<dd>

**style_prompt:** `typing.Optional[str]` — Optional style prompt
    
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

<details><summary><code>client.duets.<a href="src/fern/duets/client.py">update_duet_voice</a>(...) -> UpdateDuetVoiceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a custom duet voice (default voices cannot be modified)
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.duets.update_duet_voice(
    id=1,
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

**id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**style_prompt:** `typing.Optional[str]` 
    
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

<details><summary><code>client.duets.<a href="src/fern/duets/client.py">delete_duet_voice</a>(...) -> DeleteDuetVoiceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a custom duet voice (default voices cannot be deleted)
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.duets.delete_duet_voice(
    id=1,
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

**id:** `int` 
    
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

<details><summary><code>client.duets.<a href="src/fern/duets/client.py">list_duet_voice_pairs</a>() -> ListDuetVoicePairsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all voice pairs for duet generation
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.duets.list_duet_voice_pairs()

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

<details><summary><code>client.duets.<a href="src/fern/duets/client.py">create_duet_voice_pair</a>(...) -> CreateDuetVoicePairResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a voice pair for duet generation
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.duets.create_duet_voice_pair(
    voice1id=1,
    voice2id=1,
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

**voice1id:** `int` — ID of first voice
    
</dd>
</dl>

<dl>
<dd>

**voice2id:** `int` — ID of second voice
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Optional pair name
    
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

<details><summary><code>client.duets.<a href="src/fern/duets/client.py">generate_duet</a>(...) -> GenerateDuetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate conversational audio with two speakers
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
from fern.duets import GenerateDuetRequestScriptItem

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.duets.generate_duet(
    voice_pair_id=1,
    script=[
        GenerateDuetRequestScriptItem(
            speaker=1,
            text="text",
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

**voice_pair_id:** `int` — Voice pair ID to use
    
</dd>
</dl>

<dl>
<dd>

**script:** `typing.List[GenerateDuetRequestScriptItem]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Optional title for the duet
    
</dd>
</dl>

<dl>
<dd>

**callback_uri:** `typing.Optional[str]` — Webhook URL for completion notification
    
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

