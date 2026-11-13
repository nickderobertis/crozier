# Reference
## Files
<details><summary><code>client.files.<a href="src/fern/files/client.py#L29-L63">upload</a>(...) -> UploadedFile</code></summary>
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.upload()

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
<details><summary><code>client.transcripts.<a href="src/fern/transcripts/client.py#L54-L127">list</a>(...) -> TranscriptList</code></summary>
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

<details><summary><code>client.transcripts.<a href="src/fern/transcripts/client.py#L129-L483">submit</a>(...) -> Transcript</code></summary>
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

Enable [Auto Chapters](https://www.assemblyai.com/docs/speech-understanding/auto-chapters), can be true or false. Requires `punctuate` to be `true`, and cannot be enabled together with `summarization`. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/quickstart) instead for more flexible chapter summaries. See the [updated Auto Chapters page](https://www.assemblyai.com/docs/speech-understanding/auto-chapters) for details.

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

**content_safety_confidence:** `typing.Optional[int]` — The confidence threshold for the [Content Moderation](https://www.assemblyai.com/docs/content-moderation) model. Values must be between 25 and 100. Requires `content_safety` to be enabled; otherwise it's ignored.
    
</dd>
</dl>

<dl>
<dd>

**custom_spelling:** `typing.Optional[typing.List[TranscriptCustomSpelling]]` — Customize how words are spelled and formatted using to and from values. Each `to` value must be a single word, and each `from` phrase can contain at most 5 words. See [Custom Spelling](https://www.assemblyai.com/docs/pre-recorded-audio/correct-spelling-of-terms) for more details.
    
</dd>
</dl>

<dl>
<dd>

**disfluencies:** `typing.Optional[bool]` — Transcribe [Filler Words](https://www.assemblyai.com/docs/pre-recorded-audio/include-filler-words), like "umm", in your media file; can be true or false. Supported on Universal-3.5 Pro and Universal-2.
    
</dd>
</dl>

<dl>
<dd>

**domain:** `typing.Optional[TranscriptOptionalParamsDomain]` 

Enable domain-specific transcription models to improve accuracy for specialized terminology. Set to `"medical-v1"` to enable [Medical Mode](https://www.assemblyai.com/docs/pre-recorded-audio/medical-mode) for improved accuracy of medical terms such as medications, procedures, conditions, and dosages.

Supported languages: English (`en`), Spanish (`es`), German (`de`), French (`fr`). If `medical-v1` is used with an unsupported language, the parameter is ignored and a warning is returned.
    
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

**keyterms_prompt:** `typing.Optional[typing.List[str]]` — Improve accuracy with up to 200 (for Universal-2) or 1000 (for Universal-3.5 Pro) domain-specific words or phrases (maximum 6 words per phrase). See [Keyterms Prompting](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro/prompting#keyterms-prompting) for more details.
    
</dd>
</dl>

<dl>
<dd>

**language_code:** `typing.Optional[TranscriptOptionalParamsLanguageCode]` 

The language of your audio file. Possible values are found in [Supported Languages](https://www.assemblyai.com/docs/pre-recorded-audio/supported-languages).
If you don't specify a language, it's detected automatically. Cannot be used together with `language_detection`.
    
</dd>
</dl>

<dl>
<dd>

**language_codes:** `typing.Optional[typing.List[TranscriptLanguageCode]]` 

The language codes of your audio file. Used for [Code switching](/speech-to-text/pre-recorded-audio/code-switching)
One of the values specified must be `en`.
    
</dd>
</dl>

<dl>
<dd>

**language_confidence_threshold:** `typing.Optional[float]` 

The confidence threshold for the automatically detected language.
An error will be returned if the language confidence is below this threshold.
Defaults to 0. Can only be set when `language_detection` is enabled. See [Automatic Language Detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection) for more details.
    
</dd>
</dl>

<dl>
<dd>

**language_detection:** `typing.Optional[bool]` — [Automatic language detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection) identifies the spoken language and routes the request to the best model. It's applied automatically when you don't specify a `language_code`. Set to `false` only together with a `language_code`; disabling it without specifying a language returns an error.
    
</dd>
</dl>

<dl>
<dd>

**language_detection_options:** `typing.Optional[TranscriptOptionalParamsLanguageDetectionOptions]` — Specify options for [Automatic Language Detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection).
    
</dd>
</dl>

<dl>
<dd>

**multichannel:** `typing.Optional[bool]` — Enable [Multichannel](https://www.assemblyai.com/docs/pre-recorded-audio/transcribe-multiple-audio-channels) transcription, can be true or false.
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `typing.Optional[str]` 

Provide natural language prompting of up to 1,500 words of contextual information to the model. See the [Prompting Guide](https://www.assemblyai.com/docs/pre-recorded-audio/prompting) for best practices.

Note: This parameter is only supported for the Universal-3.5 Pro model.
    
</dd>
</dl>

<dl>
<dd>

**punctuate:** `typing.Optional[bool]` — Enable [Automatic Punctuation](https://www.assemblyai.com/docs/pre-recorded-audio), can be true or false
    
</dd>
</dl>

<dl>
<dd>

**redact_pii:** `typing.Optional[bool]` — Redact PII from the transcribed text using the Redact PII model, can be true or false. Requires `format_text` to be `true`. See [PII Redaction](https://www.assemblyai.com/docs/pii-redaction) for more details.
    
</dd>
</dl>

<dl>
<dd>

**redact_pii_audio:** `typing.Optional[bool]` — Generate a copy of the original media file with spoken PII "beeped" out, can be true or false. Requires `redact_pii` to be `true`. See [PII redaction](https://www.assemblyai.com/docs/pii-redaction#request-for-redacted-audio) for more details.
    
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

**redact_pii_sub:** `typing.Optional[SubstitutionPolicy]` — The replacement logic for detected PII, can be `entity_name` or `hash`. See [PII redaction](https://www.assemblyai.com/docs/pii-redaction) for more details.
    
</dd>
</dl>

<dl>
<dd>

**redact_pii_return_unredacted:** `typing.Optional[bool]` 

When set to `true`, returns the original unredacted transcript alongside the redacted one in the same response. Requires `redact_pii` to be `true`, otherwise a 400 error is returned.

When enabled, the response includes the additional fields `unredacted_text`, `unredacted_words`, and `unredacted_utterances`. The existing `text`, `words`, and `utterances` fields remain fully redacted. When disabled (default), the response is unchanged and contains only the redacted transcript. See [PII redaction](https://www.assemblyai.com/docs/pii-redaction) for more details.
    
</dd>
</dl>

<dl>
<dd>

**redact_static_entities:** `typing.Optional[typing.Dict[str, typing.List[str]]]` 

A map of user-defined terms to redact, where each key is a redaction label and each value is a list of exact terms to match (e.g. `{ "INTERNAL_TOOL": ["Bearclaw", "Cubclaw"] }`). Each matching term in the transcript is redacted using the `redact_pii_sub` substitution, on top of standard PII Redaction. Useful for redacting specific, predefined terms (proprietary names, internal codenames) that aren't general PII categories.

This is a literal find-and-replace (tolerant of casing, surrounding punctuation, and minor spacing/hyphenation), not a model — it does not generalize beyond the terms you provide. Requires `redact_pii` to be `true`, otherwise a 400 error is returned. When `redact_pii_audio` is enabled, matched terms are also redacted in the audio output. You can provide up to 100 labels, each with up to 200 terms of at most 200 characters; a label may contain only letters, numbers, spaces, underscores, and hyphens (max 80 characters). See [Static Entity Redaction](https://www.assemblyai.com/docs/guardrails/redact-pii-from-transcripts#static-entity-redaction) for more details.
    
</dd>
</dl>

<dl>
<dd>

**sentiment_analysis:** `typing.Optional[bool]` — Enable [Sentiment Analysis](https://www.assemblyai.com/docs/speech-understanding/sentiment-analysis), can be true or false. Requires `punctuate` to be `true`.
    
</dd>
</dl>

<dl>
<dd>

**speaker_labels:** `typing.Optional[bool]` — Enable [Speaker diarization](https://www.assemblyai.com/docs/pre-recorded-audio/label-speakers), can be true or false. Requires `punctuate` to be `true`.
    
</dd>
</dl>

<dl>
<dd>

**speaker_options:** `typing.Optional[TranscriptOptionalParamsSpeakerOptions]` — Specify options for [Speaker diarization](https://www.assemblyai.com/docs/pre-recorded-audio/label-speakers#set-a-range-of-possible-speakers). Use this to set a range of possible speakers. Requires `speaker_labels` to be `true`, and cannot be used together with `speakers_expected`. When both bounds are set, `min_speakers_expected` must be less than or equal to `max_speakers_expected`.
    
</dd>
</dl>

<dl>
<dd>

**speakers_expected:** `typing.Optional[int]` — Tells the speaker label model how many speakers it should attempt to identify. Requires `speaker_labels` to be `true` and must be a positive integer; cannot be used together with `speaker_options`. See [Set number of speakers expected](https://www.assemblyai.com/docs/pre-recorded-audio/label-speakers#set-number-of-speakers-expected) for more details.
    
</dd>
</dl>

<dl>
<dd>

**speech_models:** `typing.Optional[typing.List[SpeechModel]]` — Optional. Supported values: `universal-3-5-pro`, `universal-2`. If omitted, defaults to `["universal-3-5-pro", "universal-2"]`. See [Model Selection](https://www.assemblyai.com/docs/pre-recorded-audio/select-the-speech-model) for available models and routing behavior.
    
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

Enable [Summarization](https://www.assemblyai.com/docs/speech-understanding/summarization), can be true or false. Requires both `punctuate` and `format_text` to be `true`, and cannot be enabled together with `auto_chapters`. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/quickstart) instead for more flexible summaries. See the [updated Summarization page](https://www.assemblyai.com/docs/speech-understanding/summarization) for details.

Note: This parameter is only supported for the Universal-2 model.
    
</dd>
</dl>

<dl>
<dd>

**summary_model:** `typing.Optional[SummaryModel]` — The model to summarize the transcript. Must be set together with `summary_type`. Compatibility - `catchy` supports `gist` and `headline`; `informative` and `conversational` support `headline`, `paragraph`, `bullets`, and `bullets_verbose`. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/quickstart) instead for more flexible summaries. See the [updated Summarization page](https://www.assemblyai.com/docs/speech-understanding/summarization) for details.
    
</dd>
</dl>

<dl>
<dd>

**summary_type:** `typing.Optional[SummaryType]` — The type of summary. Must be set together with `summary_model`; see `summary_model` for the supported model and type combinations. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/quickstart) instead for more flexible summaries. See the [updated Summarization page](https://www.assemblyai.com/docs/speech-understanding/summarization) for details.
    
</dd>
</dl>

<dl>
<dd>

**remove_audio_tags:** `typing.Optional[TranscriptOptionalParamsRemoveAudioTags]` 

Universal-3.5 Pro generates rich transcripts that can include inline annotations such as audio event markers and speaker cues. Set to `"all"` to remove all inline annotations, or `"speaker"` to remove only speaker cues while keeping other annotations. By default, all inline annotations are removed.

Note: This parameter is only supported for the Universal-3.5 Pro model.
    
</dd>
</dl>

<dl>
<dd>

**temperature:** `typing.Optional[float]` 

Control the amount of randomness injected into the model's response. See the [Prompting Guide](https://www.assemblyai.com/docs/pre-recorded-audio/prompting) for more details.

Note: This parameter only takes effect on the Universal-3.5 Pro model.
    
</dd>
</dl>

<dl>
<dd>

**webhook_auth_header_name:** `typing.Optional[str]` — The header name to be sent with the transcript completed or failed [webhook](https://www.assemblyai.com/docs/deployment/webhooks-for-pre-recorded-audio) requests. Must be 1-1000 characters and contain only ASCII letters, numbers, hyphens, and underscores. Requires `webhook_auth_header_value` and `webhook_url` to also be set.
    
</dd>
</dl>

<dl>
<dd>

**webhook_auth_header_value:** `typing.Optional[str]` — The header value to send back with the transcript completed or failed [webhook](https://www.assemblyai.com/docs/deployment/webhooks-for-pre-recorded-audio) requests for added security. Must be 1-1000 characters and must not contain carriage returns or newlines. Requires `webhook_auth_header_name` and `webhook_url` to also be set.
    
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

<details><summary><code>client.transcripts.<a href="src/fern/transcripts/client.py#L485-L515">get</a>(...) -> Transcript</code></summary>
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

<details><summary><code>client.transcripts.<a href="src/fern/transcripts/client.py#L517-L548">delete</a>(...) -> Transcript</code></summary>
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

<details><summary><code>client.transcripts.<a href="src/fern/transcripts/client.py#L550-L598">get_subtitles</a>(...) -> str</code></summary>
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

<details><summary><code>client.transcripts.<a href="src/fern/transcripts/client.py#L600-L632">get_sentences</a>(...) -> SentencesResponse</code></summary>
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

<details><summary><code>client.transcripts.<a href="src/fern/transcripts/client.py#L634-L666">get_paragraphs</a>(...) -> ParagraphsResponse</code></summary>
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

<details><summary><code>client.transcripts.<a href="src/fern/transcripts/client.py#L668-L708">word_search</a>(...) -> WordSearchResponse</code></summary>
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

<details><summary><code>client.transcripts.<a href="src/fern/transcripts/client.py#L710-L743">get_redacted_audio</a>(...) -> RedactedAudioResponse</code></summary>
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

