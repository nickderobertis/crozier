# Reference
## Meta
<details><summary><code>client.meta.<a href="src/fern/meta/client.py">ping</a>() -> Ping</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Health check and basic information
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

client.meta.ping()

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

## Search
<details><summary><code>client.search.<a href="src/fern/search/client.py">search_steam_games_and_configurations_all_at_once</a>(...) -> SearchResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for games that are available on Steam
**and** Search for SteamInput configurations for Steam and non-Steam games
**all at once**

This endpoint supports no pagination and has pretty strict limits, it's intended for the "main-page" of the Frontend only
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

client.search.search_steam_games_and_configurations_all_at_once(
    search_term="search_term",
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

**search_term:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit_configs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit_games:** `typing.Optional[int]` 
    
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

<details><summary><code>client.search.<a href="src/fern/search/client.py">search_steam_input_configurations</a>(...) -> PostV1SearchConfigsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for SteamInput configurations for Steam and non-Steam games
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

client.search.search_steam_input_configurations(
    query_text="query_text",
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

**query_text:** `str` — The search query string
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[ConfigFilter]` 
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[ConfigInclude]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results to return
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for paginated results
    
</dd>
</dl>

<dl>
<dd>

**rank:** `typing.Optional[ConfigRank]` 
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Return raw Steam API response
    
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

<details><summary><code>client.search.<a href="src/fern/search/client.py">search_steam_games</a>(...) -> PostV1SearchGamesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for games that are available on Steam
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

client.search.search_steam_games(
    query_text="query_text",
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

**query_text:** `str` — The search query string
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[AppFilter]` 
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[AppsInclude]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results to return
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Return raw Steam API response
    
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

## Steam
<details><summary><code>client.steam.<a href="src/fern/steam/client.py">get_steam_app_info</a>(...) -> AppInfoItem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve app information from Steam Store for a given app ID
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

client.steam.get_steam_app_info(
    app_id=1,
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

**app_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**controller_support:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**official_configs:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**force_refresh:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.steam.<a href="src/fern/steam/client.py">get_controller_config_details</a>(...) -> GetV1SteamFiledetailsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


Retrieve details for a given controller config file ID.  
If a non-controller config file ID is provided, this will respond with a 404
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

client.steam.get_controller_config_details(
    file_id=1,
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

**file_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**playtime_stats:** `typing.Optional[int]` — Number of days for playtime statistics
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.steam.<a href="src/fern/steam/client.py">log_in_with_steam</a>(...) -> LoginResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Authenticate user via Steam OpenID and return JWT token  
			Wrapper endpoint for SSR frontend
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
from fern.steam import OpenIdBodyMode

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.steam.log_in_with_steam(
    assoc_handle="assoc_handle",
    claimed_id="claimed_id",
    identity="identity",
    mode=OpenIdBodyMode.ID_RES,
    ns="ns",
    op_endpoint="op_endpoint",
    response_nonce="response_nonce",
    return_to="return_to",
    sig="sig",
    signed="signed",
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

**assoc_handle:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**claimed_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**identity:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**mode:** `OpenIdBodyMode` 
    
</dd>
</dl>

<dl>
<dd>

**ns:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**op_endpoint:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**response_nonce:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**return_to:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**sig:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**signed:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**openid_ns:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**openid_mode:** `typing.Optional[PostV1SteamLoginRequestOpenidMode]` 
    
</dd>
</dl>

<dl>
<dd>

**openid_op_endpoint:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**openid_claimed_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**openid_identity:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**openid_return_to:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**openid_response_nonce:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**openid_assoc_handle:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**openid_signed:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**openid_sig:** `typing.Optional[str]` 
    
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

<details><summary><code>client.steam.<a href="src/fern/steam/client.py">get_steam_user_info</a>(...) -> UserInfoResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve user information from Steam for the provided userId,  
or for attempt authenticated user if no userId is provided  
Returns 401 if no id provided and token is invalid and 400 if everything is missing
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

client.steam.get_steam_user_info()

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

**user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**include_avatar_frame:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**include_profile_background:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**include_mini_profile_background:** `typing.Optional[bool]` 
    
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

