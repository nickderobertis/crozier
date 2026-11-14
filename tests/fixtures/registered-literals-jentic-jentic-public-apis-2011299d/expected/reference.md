# Reference
## Files
<details><summary><code>client.files.<a href="src/fern/files/client.py#L29-L54">upload</a>(...) -> UploadedFile</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a media file to AssemblyAI's servers.

<Note>To upload a media file to our EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
<Warning>Requests to transcribe uploaded files must use an API key from the same project as the key that was used to upload the file. If you use an API key from a different project you will get a `403` error and "Cannot access uploaded file" message.</Warning>
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
client.files.upload(...)
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

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` 
    
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

## Transcripts
<details><summary><code>client.transcripts.<a href="src/fern/transcripts/client.py#L53-L126">list</a>(...) -> TranscriptList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>To retrieve your transcriptions on our EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
Retrieve a list of transcripts you created.
Transcripts are sorted from newest to oldest and can be retrieved for the last 90 days of usage. The previous URL always points to a page with older transcripts.

If you need to retrieve transcripts from more than 90 days ago please reach out to our Support team at support@assemblyai.com.

**Pagination**

This endpoint returns paginated results. The response includes a `page_details` object with the following properties:
- `page_details.limit` - Maximum number of transcripts per page.
- `page_details.result_count` - Total number of transcripts returned on the current page.
- `page_details.current_url` - URL to the current page.
- `page_details.prev_url` - URL to the previous page of older transcripts.
- `page_details.next_url` - URL to the next page of newer transcripts.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.transcripts.list()

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

**limit:** `typing.Optional[int]` — Maximum amount of transcripts to retrieve
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[TranscriptStatus]` — Filter by transcript status
    
</dd>
</dl>

<dl>
<dd>

**created_on:** `typing.Optional[datetime.date]` — Only get transcripts created on this date
    
</dd>
</dl>

<dl>
<dd>

**before_id:** `typing.Optional[str]` — Get transcripts that were created before this transcript ID
    
</dd>
</dl>

<dl>
<dd>

**after_id:** `typing.Optional[str]` — Get transcripts that were created after this transcript ID
    
</dd>
</dl>

<dl>
<dd>

**throttled_only:** `typing.Optional[bool]` — Only get throttled transcripts, overrides the status filter
    
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

<details><summary><code>client.transcripts.<a href="src/fern/transcripts/client.py#L128-L470">submit</a>(...) -> Transcript</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>To use our EU server for transcription, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
Create a transcript from a media file that is accessible via a URL.
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
from fern import FernApi, TranslationRequestBody, TranslationRequestBodyTranslation
from fern.environment import FernApiEnvironment
from fern.transcripts import TranscriptCustomSpelling, RedactPiiAudioQuality, PiiPolicy, SubstitutionPolicy, TranscriptOptionalParamsSpeechUnderstanding

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.transcripts.submit(
    audio_end_at=280,
    audio_start_from=10,
    auto_highlights=True,
    content_safety=True,
    custom_spelling=[
        TranscriptCustomSpelling(
            from_=[
                "dicarlo"
            ],
            to="Decarlo",
        )
    ],
    disfluencies=False,
    entity_detection=True,
    filter_profanity=True,
    format_text=True,
    iab_categories=True,
    language_code="en_us",
    language_confidence_threshold=0.7,
    language_detection=True,
    multichannel=True,
    punctuate=True,
    redact_pii=True,
    redact_pii_audio=True,
    redact_pii_audio_quality=RedactPiiAudioQuality.MP3,
    redact_pii_policies=[
        PiiPolicy.US_SOCIAL_SECURITY_NUMBER,
        PiiPolicy.CREDIT_CARD_NUMBER
    ],
    redact_pii_sub=SubstitutionPolicy.HASH,
    sentiment_analysis=True,
    speaker_labels=True,
    speakers_expected=2,
    speech_models=[
        "speech_models"
    ],
    speech_threshold=0.5,
    speech_understanding=TranscriptOptionalParamsSpeechUnderstanding(
        request=TranslationRequestBody(
            translation=TranslationRequestBodyTranslation(
                target_languages=[
                    "es",
                    "de"
                ],
                formal=True,
                match_original_utterance=True,
            ),
        ),
    ),
    webhook_auth_header_name="webhook-secret",
    webhook_auth_header_value="webhook-secret-value",
    webhook_url="https://your-webhook-url/path",
    audio_url="https://assembly.ai/wildfires.mp3",
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

**speech_models:** `typing.List[SpeechModel]` — List multiple speech models in priority order, allowing our system to automatically route your audio to the best available option. See [Model Selection](https://www.assemblyai.com/docs/pre-recorded-audio/select-the-speech-model) for available models and routing behavior.
    
</dd>
</dl>

<dl>
<dd>

**audio_url:** `str` — The URL of the audio or video file to transcribe.
    
</dd>
</dl>

<dl>
<dd>

**audio_end_at:** `typing.Optional[int]` — The point in time, in milliseconds, to stop transcribing in your media file. See [Set the start and end of the transcript](https://www.assemblyai.com/docs/pre-recorded-audio/set-the-start-and-end-of-the-transcript) for more details.
    
</dd>
</dl>

<dl>
<dd>

**audio_start_from:** `typing.Optional[int]` — The point in time, in milliseconds, to begin transcribing in your media file. See [Set the start and end of the transcript](https://www.assemblyai.com/docs/pre-recorded-audio/set-the-start-and-end-of-the-transcript) for more details.
    
</dd>
</dl>

<dl>
<dd>

**auto_chapters:** `typing.Optional[bool]` 

Enable [Auto Chapters](https://www.assemblyai.com/docs/speech-understanding/auto-chapters), can be true or false. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/overview) instead for more flexible chapter summaries. See the [updated Auto Chapters page](https://www.assemblyai.com/docs/speech-understanding/auto-chapters) for details.

Note: This parameter is only supported for the Universal-2 model.
    
</dd>
</dl>

<dl>
<dd>

**auto_highlights:** `typing.Optional[bool]` — Enable [Key Phrases](https://www.assemblyai.com/docs/speech-understanding/key-phrases), either true or false
    
</dd>
</dl>

<dl>
<dd>

**content_safety:** `typing.Optional[bool]` — Enable [Content Moderation](https://www.assemblyai.com/docs/content-moderation), can be true or false
    
</dd>
</dl>

<dl>
<dd>

**content_safety_confidence:** `typing.Optional[int]` — The confidence threshold for the [Content Moderation](https://www.assemblyai.com/docs/content-moderation) model. Values must be between 25 and 100.
    
</dd>
</dl>

<dl>
<dd>

**custom_spelling:** `typing.Optional[typing.List[TranscriptCustomSpelling]]` — Customize how words are spelled and formatted using to and from values. See [Custom Spelling](https://www.assemblyai.com/docs/pre-recorded-audio/custom-spelling) for more details.
    
</dd>
</dl>

<dl>
<dd>

**disfluencies:** `typing.Optional[bool]` — Transcribe [Filler Words](https://www.assemblyai.com/docs/pre-recorded-audio/filler-words), like "umm", in your media file; can be true or false
    
</dd>
</dl>

<dl>
<dd>

**domain:** `typing.Optional[str]` 

Enable domain-specific transcription models to improve accuracy for specialized terminology. Set to `"medical-v1"` to enable [Medical Mode](https://www.assemblyai.com/docs/pre-recorded-audio/medical-mode) for improved accuracy of medical terms such as medications, procedures, conditions, and dosages.

Supported languages: English (`en`), Spanish (`es`), German (`de`), French (`fr`). If used with an unsupported language, the parameter is ignored and a warning is returned.
    
</dd>
</dl>

<dl>
<dd>

**entity_detection:** `typing.Optional[bool]` — Enable [Entity Detection](https://www.assemblyai.com/docs/speech-understanding/entity-detection), can be true or false
    
</dd>
</dl>

<dl>
<dd>

**filter_profanity:** `typing.Optional[bool]` — Filter profanity from the transcribed text, can be true or false. See [Profanity Filtering](https://www.assemblyai.com/docs/profanity-filtering) for more details.
    
</dd>
</dl>

<dl>
<dd>

**format_text:** `typing.Optional[bool]` — Enable [Text Formatting](https://www.assemblyai.com/docs/pre-recorded-audio), can be true or false
    
</dd>
</dl>

<dl>
<dd>

**iab_categories:** `typing.Optional[bool]` — Enable [Topic Detection](https://www.assemblyai.com/docs/speech-understanding/topic-detection), can be true or false
    
</dd>
</dl>

<dl>
<dd>

**keyterms_prompt:** `typing.Optional[typing.List[str]]` — Improve accuracy with up to 200 (for Universal-2) or 1000 (for Universal-3 Pro) domain-specific words or phrases (maximum 6 words per phrase). See [Keyterms Prompting](https://www.assemblyai.com/docs/pre-recorded-audio/keyterms-prompting) for more details.
    
</dd>
</dl>

<dl>
<dd>

**language_code:** `typing.Optional[TranscriptOptionalParamsLanguageCode]` 

The language of your audio file. Possible values are found in [Supported Languages](https://www.assemblyai.com/docs/pre-recorded-audio/supported-languages).
The default value is 'en_us'.
    
</dd>
</dl>

<dl>
<dd>

**language_codes:** `typing.Optional[typing.List[TranscriptLanguageCode]]` 

The language codes of your audio file. Used for [Code switching](/docs/speech-to-text/pre-recorded-audio/code-switching)
One of the values specified must be `en`.
    
</dd>
</dl>

<dl>
<dd>

**language_confidence_threshold:** `typing.Optional[float]` 

The confidence threshold for the automatically detected language.
An error will be returned if the language confidence is below this threshold.
Defaults to 0. See [Automatic Language Detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection) for more details.
    
</dd>
</dl>

<dl>
<dd>

**language_detection:** `typing.Optional[bool]` — Enable [Automatic language detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection), either true or false.
    
</dd>
</dl>

<dl>
<dd>

**language_detection_options:** `typing.Optional[TranscriptOptionalParamsLanguageDetectionOptions]` — Specify options for [Automatic Language Detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection).
    
</dd>
</dl>

<dl>
<dd>

**multichannel:** `typing.Optional[bool]` — Enable [Multichannel](https://www.assemblyai.com/docs/pre-recorded-audio/multichannel) transcription, can be true or false.
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `typing.Optional[str]` 

Provide natural language prompting of up to 1,500 words of contextual information to the model. See the [Prompting Guide](https://www.assemblyai.com/docs/pre-recorded-audio/prompting) for best practices.

Note: This parameter is only supported for the Universal-3 Pro model.
    
</dd>
</dl>

<dl>
<dd>

**punctuate:** `typing.Optional[bool]` — Enable [Automatic Punctuation](https://www.assemblyai.com/docs/pre-recorded-audio), can be true or false
    
</dd>
</dl>

<dl>
<dd>

**redact_pii:** `typing.Optional[bool]` — Redact PII from the transcribed text using the Redact PII model, can be true or false. See [PII Redaction](https://www.assemblyai.com/docs/pii-redaction) for more details.
    
</dd>
</dl>

<dl>
<dd>

**redact_pii_audio:** `typing.Optional[bool]` — Generate a copy of the original media file with spoken PII "beeped" out, can be true or false. See [PII redaction](https://www.assemblyai.com/docs/pii-redaction#request-for-redacted-audio) for more details.
    
</dd>
</dl>

<dl>
<dd>

**redact_pii_audio_options:** `typing.Optional[TranscriptOptionalParamsRedactPiiAudioOptions]` — Specify options for [PII redacted audio](https://www.assemblyai.com/docs/pii-redaction#request-for-redacted-audio) files.
    
</dd>
</dl>

<dl>
<dd>

**redact_pii_audio_quality:** `typing.Optional[RedactPiiAudioQuality]` — Controls the filetype of the audio created by redact_pii_audio. Currently supports mp3 (default) and wav. See [PII redaction](https://www.assemblyai.com/docs/pii-redaction#request-for-redacted-audio) for more details.
    
</dd>
</dl>

<dl>
<dd>

**redact_pii_policies:** `typing.Optional[typing.List[PiiPolicy]]` — The list of PII Redaction policies to enable. See [PII redaction](https://www.assemblyai.com/docs/pii-redaction) for more details.
    
</dd>
</dl>

<dl>
<dd>

**redact_pii_sub:** `typing.Optional[SubstitutionPolicy]` — The replacement logic for detected PII, can be `entity_type` or `hash`. See [PII redaction](https://www.assemblyai.com/docs/pii-redaction) for more details.
    
</dd>
</dl>

<dl>
<dd>

**sentiment_analysis:** `typing.Optional[bool]` — Enable [Sentiment Analysis](https://www.assemblyai.com/docs/speech-understanding/sentiment-analysis), can be true or false
    
</dd>
</dl>

<dl>
<dd>

**speaker_labels:** `typing.Optional[bool]` — Enable [Speaker diarization](https://www.assemblyai.com/docs/pre-recorded-audio/speaker-diarization), can be true or false
    
</dd>
</dl>

<dl>
<dd>

**speaker_options:** `typing.Optional[TranscriptOptionalParamsSpeakerOptions]` — Specify options for [Speaker diarization](https://www.assemblyai.com/docs/pre-recorded-audio/speaker-diarization#set-a-range-of-possible-speakers). Use this to set a range of possible speakers.
    
</dd>
</dl>

<dl>
<dd>

**speakers_expected:** `typing.Optional[int]` — Tells the speaker label model how many speakers it should attempt to identify. See [Set number of speakers expected](https://www.assemblyai.com/docs/pre-recorded-audio/speaker-diarization#set-number-of-speakers-expected) for more details.
    
</dd>
</dl>

<dl>
<dd>

**speech_threshold:** `typing.Optional[float]` 

Reject audio files that contain less than this fraction of speech.
Valid values are in the range [0, 1] inclusive. See [Speech Threshold](https://www.assemblyai.com/docs/speech-threshold) for more details.
    
</dd>
</dl>

<dl>
<dd>

**speech_understanding:** `typing.Optional[TranscriptOptionalParamsSpeechUnderstanding]` — Enable speech understanding tasks like [Translation](https://www.assemblyai.com/docs/speech-understanding/translation), [Speaker Identification](https://www.assemblyai.com/docs/speech-understanding/speaker-identification), and [Custom Formatting](https://www.assemblyai.com/docs/speech-understanding/custom-formatting). See the task-specific docs for available options and configuration.
    
</dd>
</dl>

<dl>
<dd>

**summarization:** `typing.Optional[bool]` 

Enable [Summarization](https://www.assemblyai.com/docs/speech-understanding/summarization), can be true or false. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/overview) instead for more flexible summaries. See the [updated Summarization page](https://www.assemblyai.com/docs/speech-understanding/summarization) for details.

Note: This parameter is only supported for the Universal-2 model.
    
</dd>
</dl>

<dl>
<dd>

**summary_model:** `typing.Optional[SummaryModel]` — The model to summarize the transcript. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/overview) instead for more flexible summaries. See the [updated Summarization page](https://www.assemblyai.com/docs/speech-understanding/summarization) for details.
    
</dd>
</dl>

<dl>
<dd>

**summary_type:** `typing.Optional[SummaryType]` — The type of summary. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/overview) instead for more flexible summaries. See the [updated Summarization page](https://www.assemblyai.com/docs/speech-understanding/summarization) for details.
    
</dd>
</dl>

<dl>
<dd>

**remove_audio_tags:** `typing.Optional[TranscriptOptionalParamsRemoveAudioTags]` 

Remove [audio event tags](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-pro#audio-event-tags) from the transcript text. Set to `"all"` to remove all audio tags.

Note: This parameter is only supported for the Universal-3 Pro model.
    
</dd>
</dl>

<dl>
<dd>

**temperature:** `typing.Optional[float]` 

Control the amount of randomness injected into the model's response. See the [Prompting Guide](https://www.assemblyai.com/docs/pre-recorded-audio/prompting) for more details.

Note: This parameter can only be used with the Universal-3 Pro model.
    
</dd>
</dl>

<dl>
<dd>

**webhook_auth_header_name:** `typing.Optional[str]` — The header name to be sent with the transcript completed or failed [webhook](https://www.assemblyai.com/docs/deployment/webhooks-for-pre-recorded-audio) requests
    
</dd>
</dl>

<dl>
<dd>

**webhook_auth_header_value:** `typing.Optional[str]` — The header value to send back with the transcript completed or failed [webhook](https://www.assemblyai.com/docs/deployment/webhooks-for-pre-recorded-audio) requests for added security
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — The URL to which we send [webhook](https://www.assemblyai.com/docs/deployment/webhooks-for-pre-recorded-audio) requests.
    
</dd>
</dl>

<dl>
<dd>

**custom_topics:** `typing.Optional[bool]` — This parameter does not currently have any functionality attached to it.
    
</dd>
</dl>

<dl>
<dd>

**speech_model:** `typing.Optional[SpeechModel]` — This parameter has been replaced with the `speech_models` parameter, learn more about the `speech_models` parameter [here](https://www.assemblyai.com/docs/pre-recorded-audio/select-the-speech-model).
    
</dd>
</dl>

<dl>
<dd>

**topics:** `typing.Optional[typing.List[str]]` — This parameter does not currently have any functionality attached to it.
    
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

<details><summary><code>client.transcripts.<a href="src/fern/transcripts/client.py#L472-L502">get</a>(...) -> Transcript</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>To retrieve your transcriptions on our EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
Get the transcript resource. The transcript is ready when the "status" is "completed".
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.transcripts.get(
    transcript_id="transcript_id",
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

**transcript_id:** `str` — ID of the transcript
    
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

<details><summary><code>client.transcripts.<a href="src/fern/transcripts/client.py#L504-L535">delete</a>(...) -> Transcript</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>To delete your transcriptions on our EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
Remove the data from the transcript and mark it as deleted.
<Warning>Files uploaded via the `/upload` endpoint are immediately deleted alongside the transcript when you make a DELETE request, ensuring your data is removed from our systems right away.</Warning>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.transcripts.delete(
    transcript_id="transcript_id",
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

**transcript_id:** `str` — ID of the transcript
    
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

<details><summary><code>client.transcripts.<a href="src/fern/transcripts/client.py#L537-L585">get_subtitles</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>To retrieve your transcriptions on our EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
Export your transcript in SRT or VTT format to use with a video player for subtitles and closed captions.
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
from fern.transcripts import SubtitleFormat

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.transcripts.get_subtitles(
    transcript_id="transcript_id",
    subtitle_format=SubtitleFormat.SRT,
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

**transcript_id:** `str` — ID of the transcript
    
</dd>
</dl>

<dl>
<dd>

**subtitle_format:** `SubtitleFormat` — The format of the captions
    
</dd>
</dl>

<dl>
<dd>

**chars_per_caption:** `typing.Optional[int]` — The maximum number of characters per caption
    
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

<details><summary><code>client.transcripts.<a href="src/fern/transcripts/client.py#L587-L619">get_sentences</a>(...) -> SentencesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>To retrieve your transcriptions on our EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
Get the transcript split by sentences. The API will attempt to semantically segment the transcript into sentences to create more reader-friendly transcripts.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.transcripts.get_sentences(
    transcript_id="transcript_id",
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

**transcript_id:** `str` — ID of the transcript
    
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

<details><summary><code>client.transcripts.<a href="src/fern/transcripts/client.py#L621-L653">get_paragraphs</a>(...) -> ParagraphsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>To retrieve your transcriptions on our EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
Get the transcript split by paragraphs. The API will attempt to semantically segment your transcript into paragraphs to create more reader-friendly transcripts.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.transcripts.get_paragraphs(
    transcript_id="transcript_id",
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

**transcript_id:** `str` — ID of the transcript
    
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

<details><summary><code>client.transcripts.<a href="src/fern/transcripts/client.py#L655-L695">word_search</a>(...) -> WordSearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>To search through a transcription created on our EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
Search through the transcript for keywords. You can search for individual words, numbers, or phrases containing up to five words or numbers.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.transcripts.word_search(
    transcript_id="transcript_id",
    words=[
        "words"
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

**transcript_id:** `str` — ID of the transcript
    
</dd>
</dl>

<dl>
<dd>

**words:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Keywords to search for
    
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

<details><summary><code>client.transcripts.<a href="src/fern/transcripts/client.py#L697-L730">get_redacted_audio</a>(...) -> RedactedAudioResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>To retrieve the redacted audio on the EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com` in the `GET` request above.</Note>
<Note>Redacted audio files are only available for 24 hours. Make sure to download the file within this time frame.</Note>
Retrieve the redacted audio object containing the status and URL to the redacted audio.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.transcripts.get_redacted_audio(
    transcript_id="transcript_id",
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

**transcript_id:** `str` — ID of the transcript
    
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

