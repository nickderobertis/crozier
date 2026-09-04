# Reference
## AdvancedAuthentication
<details><summary><code>client.advanced_authentication.<a href="src/fern/advanced_authentication/client.py">post_auth_api_key</a>(...) -> AccessToken</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a bearer token that can be used to authenticate other endpoint.

You can find the tutorial on using the disposable bearer token [here](https://docs.api.video/reference/disposable-bearer-token-authentication).
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

client.advanced_authentication.post_auth_api_key(
    api_key="9VxMaPgsaFg7EBqmuspSzF7",
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

**api_key:** `str` — Your account API key. You can use your sandbox API key, or you can use your production API key.
    
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

<details><summary><code>client.advanced_authentication.<a href="src/fern/advanced_authentication/client.py">post_auth_refresh</a>(...) -> AccessToken</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Accepts the old bearer token and returns a new bearer token that can be used to authenticate other endpoint.

You can find the tutorial on using the disposable bearer token [here](https://docs.api.video/reference/disposable-bearer-token-authentication).
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

client.advanced_authentication.post_auth_refresh(
    refresh_token="def502005346d9cc2bd79a7793ab5bdabfefcaabfbb8c253f14733f1262077e1a3f38c4751d6d20f590c3784e531a82adc11f05fc1949aa46d5575aaa99cb84b9334ba66ac773576b5d7a418937ae337de62811d086dd42ad1164b12f87d67be6ffea18f2d50be9b95697b21c4d3c4372849bdb2287259cb80541570e913691a08b2fa33c85885930de15cebea627fc09f0255562ab3d39d87d4ff8fc02b00e252afcd480421dec7de9d1411176bcf669c527762e22294b453bc9ea06e9fa8ba5b873feb2ee14ce0a6a6ddd4b78c580631e210e9b9387265dc2bec9478a66a09dcdce1c40d2f856689e9d81742c9628a0b87b359e0b218ea1f07427eef89f999e47af89792f598e05847bd008fddc32ee63f4a601ffb4cd2ad08977f1c854ec358238322c918f05aa5a41f8a171dee497218408abc8283473f6112aeed7310815416a0fa36c63667e0ed014fa40b8992891bf58bae400d901c01450101c88f4978938ad138adc19cfe5698d60fd82cb27c586f6a8f70f4393c7c9e579df8739d46d249fb76d7",
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

**refresh_token:** `str` — The refresh token is either the first refresh token you received when you authenticated with the auth/api-key endpoint, or it's the refresh token from the last time you used the auth/refresh endpoint. Place this in the body of your request to obtain a new access token (which is valid for an hour) and a new refresh token.
    
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

## Videos
<details><summary><code>client.videos.<a href="src/fern/videos/client.py">post_videos_video_id_source</a>(...) -> Video</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ingest a video from a source or file.
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

client.videos.post_videos_video_id_source(
    video_id="vi4k0jvEUuaTdRAEjQ4Jfrgz",
    content_range="bytes 209715200-419430399/524288000 OR part 2/3",
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

**video_id:** `str` — Enter the videoId you want to use to upload your video.
    
</dd>
</dl>

<dl>
<dd>

**file:** `core.File` — The path to the video you would like to upload. The path must be local. If you want to use a video from an online source, you must use the "/videos" endpoint and add the "source" parameter when you create a new video.
    
</dd>
</dl>

<dl>
<dd>

**content_range:** `typing.Optional[str]` — `part <part>/<total_parts>` ; `bytes <from_byte>-<to_byte>/<total_bytes>`
    
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

<details><summary><code>client.videos.<a href="src/fern/videos/client.py">post_upload</a>(...) -> Video</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Uploading a video with the delegated upload token.
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

client.videos.post_upload(
    token="to1tcmSFHeYY5KzyhOqVKMKb",
    content_range="Content-Range: bytes 200-100/5000",
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

**token:** `str` — The unique identifier for the token you want to use to upload a video.
    
</dd>
</dl>

<dl>
<dd>

**file:** `core.File` — The path to the video you want to upload.
    
</dd>
</dl>

<dl>
<dd>

**content_range:** `typing.Optional[str]` — Content-Range represents the range of bytes that will be returned as a result of the request. Byte ranges are inclusive, meaning that bytes 0-999 represents the first 1000 bytes in a file or object.
    
</dd>
</dl>

<dl>
<dd>

**video_id:** `typing.Optional[str]` — The video id returned by the first call to this endpoint in a large video upload scenario.
    
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

