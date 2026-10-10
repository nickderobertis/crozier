# Reference
## Movies
<details><summary><code>client.movies.<a href="src/fern/movies/client.py">list_movies</a>(...) -> MovieListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns movies visible to the authenticated account. Exact pagination,
sorting, and filter names must be verified by live drift tests.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.movies.list_movies(
    subtitles="en",
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

**page:** `typing.Optional[int]` — Page number for catalog pagination. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise paginate locally over fetched data.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Results per page for catalog pagination. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise paginate locally over fetched data.
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Free-text search query for catalog filtering. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise search locally over fetched data.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListMoviesRequestSort]` — Sort order for catalog results. Sort values and production use must be verified against the Kodi plugin request surface by live drift tests; otherwise sort locally over fetched data.
    
</dd>
</dl>

<dl>
<dd>

**genre:** `typing.Optional[str]` — Filter catalog by genre slug. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — Filter catalog by country code. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.
    
</dd>
</dl>

<dl>
<dd>

**subtitles:** `typing.Optional[LanguageCode]` — Filter catalog by subtitle language code. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.
    
</dd>
</dl>

<dl>
<dd>

**year_from:** `typing.Optional[int]` — Filter catalog by minimum release year (inclusive). Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.
    
</dd>
</dl>

<dl>
<dd>

**year_to:** `typing.Optional[int]` — Filter catalog by maximum release year (inclusive). Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.
    
</dd>
</dl>

<dl>
<dd>

**rating_from:** `typing.Optional[float]` — Filter catalog by minimum rating (inclusive). Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.
    
</dd>
</dl>

<dl>
<dd>

**rating_to:** `typing.Optional[float]` — Filter catalog by maximum rating (inclusive). Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.
    
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

<details><summary><code>client.movies.<a href="src/fern/movies/client.py">get_movie</a>(...) -> MovieDetailResponse</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.movies.get_movie(
    movie_id=1,
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

**movie_id:** `int` — Movie numeric id, as observed in live Kodi API responses.
    
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

## Shows
<details><summary><code>client.shows.<a href="src/fern/shows/client.py">list_shows</a>(...) -> ShowListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns shows visible to the authenticated account. Exact pagination,
sorting, and filter names must be verified by live drift tests.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.shows.list_shows(
    subtitles="en",
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

**page:** `typing.Optional[int]` — Page number for catalog pagination. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise paginate locally over fetched data.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Results per page for catalog pagination. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise paginate locally over fetched data.
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Free-text search query for catalog filtering. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise search locally over fetched data.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListShowsRequestSort]` — Sort order for catalog results. Sort values and production use must be verified against the Kodi plugin request surface by live drift tests; otherwise sort locally over fetched data.
    
</dd>
</dl>

<dl>
<dd>

**genre:** `typing.Optional[str]` — Filter catalog by genre slug. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — Filter catalog by country code. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.
    
</dd>
</dl>

<dl>
<dd>

**subtitles:** `typing.Optional[LanguageCode]` — Filter catalog by subtitle language code. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.
    
</dd>
</dl>

<dl>
<dd>

**year_from:** `typing.Optional[int]` — Filter catalog by minimum release year (inclusive). Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.
    
</dd>
</dl>

<dl>
<dd>

**year_to:** `typing.Optional[int]` — Filter catalog by maximum release year (inclusive). Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.
    
</dd>
</dl>

<dl>
<dd>

**rating_from:** `typing.Optional[float]` — Filter catalog by minimum rating (inclusive). Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.
    
</dd>
</dl>

<dl>
<dd>

**rating_to:** `typing.Optional[float]` — Filter catalog by maximum rating (inclusive). Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.
    
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

<details><summary><code>client.shows.<a href="src/fern/shows/client.py">get_show</a>(...) -> ShowDetailResponse</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.shows.get_show(
    show_id=1,
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

**show_id:** `int` — Show numeric id, as observed in live Kodi API responses.
    
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

## Episodes
<details><summary><code>client.episodes.<a href="src/fern/episodes/client.py">get_episode</a>(...) -> EpisodeDetailResponse</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.episodes.get_episode(
    episode_id=1,
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

**episode_id:** `int` — Episode numeric id, as observed in live Kodi API responses.
    
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

