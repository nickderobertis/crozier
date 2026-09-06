# Reference
## images
<details><summary><code>client.images.<a href="src/fern/images/client.py">search_images</a>(...) -> PaginatedImageResults</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for openly-licensed images with extensive filtering options.
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

client.images.search_images()

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

**q:** `typing.Optional[str]` — Full-text search query (max 200 characters)
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for pagination
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results per page
    
</dd>
</dl>

<dl>
<dd>

**license:** `typing.Optional[str]` — Filter by license type (comma-separated)
    
</dd>
</dl>

<dl>
<dd>

**license_type:** `typing.Optional[str]` — Filter by license category (commercial, modification)
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[str]` — Filter by content source
    
</dd>
</dl>

<dl>
<dd>

**excluded_source:** `typing.Optional[str]` — Exclude content from specific sources
    
</dd>
</dl>

<dl>
<dd>

**creator:** `typing.Optional[str]` — Filter by creator name
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[str]` — Filter by tags
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Filter by title
    
</dd>
</dl>

<dl>
<dd>

**mature:** `typing.Optional[bool]` — Include mature/sensitive content
    
</dd>
</dl>

<dl>
<dd>

**filter_dead:** `typing.Optional[bool]` — Filter out dead/broken links
    
</dd>
</dl>

<dl>
<dd>

**aspect_ratio:** `typing.Optional[SearchImagesRequestAspectRatio]` — Filter by aspect ratio
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[SearchImagesRequestSize]` — Filter by image size
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[SearchImagesRequestCategory]` — Filter by image category
    
</dd>
</dl>

<dl>
<dd>

**extension:** `typing.Optional[str]` — Filter by file extension
    
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

<details><summary><code>client.images.<a href="src/fern/images/client.py">get_image</a>(...) -> Image</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve detailed information about a specific image by its UUID.
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

client.images.get_image(
    identifier="identifier",
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

**identifier:** `str` — Unique media identifier (UUID)
    
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

<details><summary><code>client.images.<a href="src/fern/images/client.py">get_related_images</a>(...) -> PaginatedImageResults</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Find images related to a specified image.
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

client.images.get_related_images(
    identifier="identifier",
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

**identifier:** `str` — Unique media identifier (UUID)
    
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

<details><summary><code>client.images.<a href="src/fern/images/client.py">report_image</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Report an image for issues such as DMCA violations, mature content, or other concerns.
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
from fern import FernApi, ReportRequestReason
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.images.report_image(
    identifier="identifier",
    reason=ReportRequestReason.MATURE,
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

**identifier:** `str` — Unique media identifier (UUID)
    
</dd>
</dl>

<dl>
<dd>

**request:** `ReportRequest` 
    
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

<details><summary><code>client.images.<a href="src/fern/images/client.py">get_image_thumbnail</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a thumbnail proxy for the specified image.
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

client.images.get_image_thumbnail(
    identifier="identifier",
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

**identifier:** `str` — Unique media identifier (UUID)
    
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

<details><summary><code>client.images.<a href="src/fern/images/client.py">get_image_oembed</a>(...) -> GetImageOembedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve oEmbed structured data for embedding an image.
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

client.images.get_image_oembed(
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

**url:** `str` — The URL of the image to retrieve oEmbed data for
    
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

<details><summary><code>client.images.<a href="src/fern/images/client.py">get_image_stats</a>() -> typing.List[SourceStats]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all content sources for images and their media counts.
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

client.images.get_image_stats()

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

## audio
<details><summary><code>client.audio.<a href="src/fern/audio/client.py">search_audio</a>(...) -> PaginatedAudioResults</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for openly-licensed audio files with filtering and pagination.
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

client.audio.search_audio()

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

**q:** `typing.Optional[str]` — Full-text search query (max 200 characters)
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for pagination
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results per page
    
</dd>
</dl>

<dl>
<dd>

**license:** `typing.Optional[str]` — Filter by license type (comma-separated)
    
</dd>
</dl>

<dl>
<dd>

**license_type:** `typing.Optional[str]` — Filter by license category (commercial, modification)
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[str]` — Filter by content source
    
</dd>
</dl>

<dl>
<dd>

**excluded_source:** `typing.Optional[str]` — Exclude content from specific sources
    
</dd>
</dl>

<dl>
<dd>

**creator:** `typing.Optional[str]` — Filter by creator name
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[str]` — Filter by tags
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Filter by title
    
</dd>
</dl>

<dl>
<dd>

**mature:** `typing.Optional[bool]` — Include mature/sensitive content
    
</dd>
</dl>

<dl>
<dd>

**filter_dead:** `typing.Optional[bool]` — Filter out dead/broken links
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[SearchAudioRequestCategory]` — Filter by audio category
    
</dd>
</dl>

<dl>
<dd>

**length:** `typing.Optional[SearchAudioRequestLength]` — Filter by audio duration
    
</dd>
</dl>

<dl>
<dd>

**extension:** `typing.Optional[str]` — Filter by file extension (e.g., mp3, ogg, flac)
    
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

<details><summary><code>client.audio.<a href="src/fern/audio/client.py">get_audio</a>(...) -> Audio</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve detailed information about a specific audio file by its UUID.
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

client.audio.get_audio(
    identifier="identifier",
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

**identifier:** `str` — Unique media identifier (UUID)
    
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

<details><summary><code>client.audio.<a href="src/fern/audio/client.py">get_related_audio</a>(...) -> PaginatedAudioResults</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Find audio files related to a specified audio.
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

client.audio.get_related_audio(
    identifier="identifier",
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

**identifier:** `str` — Unique media identifier (UUID)
    
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

<details><summary><code>client.audio.<a href="src/fern/audio/client.py">report_audio</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Report an audio file for issues such as DMCA violations or mature content.
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
from fern import FernApi, ReportRequestReason
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.audio.report_audio(
    identifier="identifier",
    reason=ReportRequestReason.MATURE,
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

**identifier:** `str` — Unique media identifier (UUID)
    
</dd>
</dl>

<dl>
<dd>

**request:** `ReportRequest` 
    
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

<details><summary><code>client.audio.<a href="src/fern/audio/client.py">get_audio_thumbnail</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a thumbnail for the specified audio file.
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

client.audio.get_audio_thumbnail(
    identifier="identifier",
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

**identifier:** `str` — Unique media identifier (UUID)
    
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

<details><summary><code>client.audio.<a href="src/fern/audio/client.py">get_audio_waveform</a>(...) -> GetAudioWaveformResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve waveform peak data for the specified audio file.
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

client.audio.get_audio_waveform(
    identifier="identifier",
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

**identifier:** `str` — Unique media identifier (UUID)
    
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

<details><summary><code>client.audio.<a href="src/fern/audio/client.py">get_audio_stats</a>() -> typing.List[SourceStats]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all content sources for audio and their media counts.
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

client.audio.get_audio_stats()

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

## auth
<details><summary><code>client.auth.<a href="src/fern/auth/client.py">register_application</a>(...) -> RegisterApplicationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Register a new application to obtain client credentials for API access.
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

client.auth.register_application(
    name="name",
    description="description",
    email="email",
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

**name:** `str` — Application name
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — Application description
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — Contact email
    
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

<details><summary><code>client.auth.<a href="src/fern/auth/client.py">get_access_token</a>(...) -> GetAccessTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Exchange client credentials for an API access token.
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
from fern.auth import GetAccessTokenRequestGrantType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.auth.get_access_token(
    client_id="client_id",
    client_secret="client_secret",
    grant_type=GetAccessTokenRequestGrantType.CLIENT_CREDENTIALS,
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

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**grant_type:** `GetAccessTokenRequestGrantType` 
    
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

<details><summary><code>client.auth.<a href="src/fern/auth/client.py">get_rate_limit</a>() -> GetRateLimitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check the current rate limit status for your API key.
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

client.auth.get_rate_limit()

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

