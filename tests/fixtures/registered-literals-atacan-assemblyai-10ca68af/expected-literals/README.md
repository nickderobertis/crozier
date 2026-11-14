# Fern Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=Fern%2FPython)
[![pypi](https://img.shields.io/pypi/v/fern)](https://pypi.python.org/pypi/fern)

The Fern Python library provides convenient access to the Fern APIs from Python.

## Table of Contents

- [Installation](#installation)
- [Reference](#reference)
- [Usage](#usage)
- [Environments](#environments)
- [Async Client](#async-client)
- [Exception Handling](#exception-handling)
- [Advanced](#advanced)
  - [Access Raw Response Data](#access-raw-response-data)
  - [Retries](#retries)
  - [Timeouts](#timeouts)
  - [Custom Client](#custom-client)
- [Contributing](#contributing)

## Installation

```sh
pip install fern
```

## Reference

A full reference for this library is available [here](./reference.md).

## Usage

Instantiate and use the client with the following:

```python
from fern import FernApi, TranslationRequestBody, TranslationRequestBodyTranslation
from fern.transcripts import TranscriptCustomSpelling, TranscriptOptionalParamsSpeechUnderstanding

client = FernApi(
    api_key="<value>",
)

client.transcripts.submit(
    audio_end_at=280,
    audio_start_from=10,
    auto_chapters=True,
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
    redact_pii_audio_quality="mp3",
    redact_pii_policies=[
        "us_social_security_number",
        "credit_card_number"
    ],
    redact_pii_sub="hash",
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
    summarization=True,
    summary_model="informative",
    summary_type="bullets",
    webhook_auth_header_name="webhook-secret",
    webhook_auth_header_value="webhook-secret-value",
    webhook_url="https://your-webhook-url/path",
    audio_url="https://assembly.ai/wildfires.mp3",
)
```

## Environments

This SDK allows you to configure different environments for API requests.

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API. Note that if you are constructing an Async httpx client class to pass into this client, use `httpx.AsyncClient()` instead of `httpx.Client()` (e.g. for the `httpx_client` parameter of this client).

```python
import asyncio
from fern.transcripts import TranscriptCustomSpelling, TranscriptOptionalParamsSpeechUnderstanding

from fern import AsyncFernApi, TranslationRequestBody, TranslationRequestBodyTranslation

client = AsyncFernApi(
    api_key="<value>",
)


async def main() -> None:
    await client.transcripts.submit(
        audio_end_at=280,
        audio_start_from=10,
        auto_chapters=True,
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
        redact_pii_audio_quality="mp3",
        redact_pii_policies=[
            "us_social_security_number",
            "credit_card_number"
        ],
        redact_pii_sub="hash",
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
        summarization=True,
        summary_model="informative",
        summary_type="bullets",
        webhook_auth_header_name="webhook-secret",
        webhook_auth_header_value="webhook-secret-value",
        webhook_url="https://your-webhook-url/path",
        audio_url="https://assembly.ai/wildfires.mp3",
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from fern.core.api_error import ApiError

try:
    client.transcripts.submit(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from fern import FernApi

client = FernApi(...)
response = client.transcripts.with_raw_response.submit(...)
print(response.headers)  # access the response headers
print(response.status_code)  # access the response status code
print(response.data)  # access the underlying object
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

Which status codes are retried depends on the `retryStatusCodes` generator configuration:

**`legacy`** (current default): retries on
- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [409](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409) (Conflict)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#server_error_responses) (All server errors, including 500)

**`recommended`**: retries on
- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [409](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409) (Conflict)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [502](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/502) (Bad Gateway)
- [503](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503) (Service Unavailable)
- [504](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/504) (Gateway Timeout)

Use the `max_retries` request option to configure this behavior.

```python
client.transcripts.submit(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python
from fern import FernApi

client = FernApi(..., timeout=20.0)

# Override timeout for a specific method
client.transcripts.submit(..., request_options={
    "timeout": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from fern import FernApi

client = FernApi(
    ...,
    httpx_client=httpx.Client(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
