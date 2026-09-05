# Reference
## Directory API
<details><summary><code>client.directory_api.<a href="src/fern/directory_api/client.py">get_best_podcasts</a>(...) -> BestPodcastsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of curated best podcasts by genre,
which are curated by Listen Notes staffs based on various signals from the Internet, e.g.,
top charts on other podcast platforms, recommendations from mainstream media,
user activities on listennotes.com...
You can get the genre ids from `GET /genres` endpoint.
This endpoint returns same data as https://www.listennotes.com/best-podcasts/
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
    listen_api_key="<X-ListenAPI-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.directory_api.get_best_podcasts(
    page=2,
    region="us",
    safe_mode=0,
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

**genre_id:** `typing.Optional[str]` — You can get the id from `GET /genres`. If not specified, it'll be the overall best podcasts, which can be considered as a special genre.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number of those podcasts in this genre.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` 

Filter best podcasts by country/region.
Please note that podcasts that are "best" in a country/region may not be produced in that country/region.
For example, a podcast from the US may be very popular in Canada.
You can get the supported country codes (e.g., us, jp, gb...) from `GET /regions`.
If not specified, you'll get "best podcasts" in United States.
    
</dd>
</dl>

<dl>
<dd>

**publisher_region:** `typing.Optional[str]` 

Filter best podcasts by the publisher's country/region.
This is to narrow down the results to include "best podcasts" produced in a specific country/region.
You can get the supported country codes (e.g., us, jp, gb...) from `GET /regions`.
If not specified, you'll get "best podcasts" produced in any country/region.
If you want to get a country/region's "best podcasts" that are also produced in that country/region,
then you need to specify both **region** and **publisher_region**,
e.g., `region=jp` and `publisher_region=jp`.
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` 

Filter best podcasts by language.
You can get a list of supported languages (e.g., English, Chinese, Japanese...) from `GET /languages`.
If not specified, you'll get "best podcasts" in any language.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetBestPodcastsRequestSort]` 

How do you want to sort these podcasts?
If you'd like to sort by popularity, please use **listen_score**.
    
</dd>
</dl>

<dl>
<dd>

**safe_mode:** `typing.Optional[int]` — Whether or not to exclude podcasts with explicit language. 1 is yes, and 0 is no.
    
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

<details><summary><code>client.directory_api.<a href="src/fern/directory_api/client.py">get_curated_podcasts</a>(...) -> GetCuratedPodcastsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A bunch of curated lists from online media. For each list, you'll get basic info of up to 5 podcasts. To get detailed meta data of all podcasts in a specific list, you need to use `GET /curated_podcasts/{id}`. We add new curated lists to the database on a daily basis.
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
    listen_api_key="<X-ListenAPI-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.directory_api.get_curated_podcasts()

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

**page:** `typing.Optional[int]` — Page number of curated lists.
    
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

<details><summary><code>client.directory_api.<a href="src/fern/directory_api/client.py">get_curated_podcast_by_id</a>(...) -> CuratedListFull</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get detailed meta data of all podcasts in a specific curated list.
This endpoint returns same data as https://www.listennotes.com/curated-podcasts/
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
    listen_api_key="<X-ListenAPI-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.directory_api.get_curated_podcast_by_id(
    id="SDFKduyJ47r",
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

**id:** `str` — id for a specific curated list of podcasts. You can get the id from the response of `GET /search?type=curated` or `GET /curated_podcasts`.
    
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

<details><summary><code>client.directory_api.<a href="src/fern/directory_api/client.py">get_episodes_in_batch</a>(...) -> GetEpisodesInBatchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Batch fetch basic meta data for up to 10 episodes. This endpoint could be used to implement custom playlists for individual episodes. For detailed meta data of an individual episode, you need to use `GET /episodes/{id}`. This endpoint is available only in the PRO/ENTERPRISE plan.
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
    listen_api_key="<X-ListenAPI-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.directory_api.get_episodes_in_batch(
    ids="c577d55b2b2b483c969fae3ceb58e362,0f34a9099579490993eec9e8c8cebb82",
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

**request:** `GetEpisodesInBatchForm` 
    
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

<details><summary><code>client.directory_api.<a href="src/fern/directory_api/client.py">get_episode_by_id</a>(...) -> EpisodeFull</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch detailed meta data for a specific episode.
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
    listen_api_key="<X-ListenAPI-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.directory_api.get_episode_by_id(
    id="6b6d65930c5a4f71b254465871fed370",
    show_transcript=1,
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

**id:** `str` — id for a specific episode. You can get episode id from using other endpoints, e.g., `GET /search`...
    
</dd>
</dl>

<dl>
<dd>

**show_transcript:** `typing.Optional[int]` — To include the transcript of this episode or not? If it is 1, then include the transcript in the **transcript** field. The default value is 0 - we don't include transcript by default, because 1) it would make the response data very big, thus slow response time; 2) less than 1% of episodes have transcripts. The transcript field is available only in the PRO/ENTERPRISE plan.
    
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

<details><summary><code>client.directory_api.<a href="src/fern/directory_api/client.py">get_episode_recommendations</a>(...) -> GetEpisodeRecommendationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch up to 8 episode recommendations based on the given episode id.
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
    listen_api_key="<X-ListenAPI-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.directory_api.get_episode_recommendations(
    id="254444fa6cf64a43a95292a70eb6869b",
    safe_mode=0,
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

**id:** `str` — Episode id.
    
</dd>
</dl>

<dl>
<dd>

**safe_mode:** `typing.Optional[int]` — Whether or not to exclude podcasts with explicit language. 1 is yes, and 0 is no.
    
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

<details><summary><code>client.directory_api.<a href="src/fern/directory_api/client.py">get_genres</a>(...) -> GetGenresResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of podcast genres that are supported in Listen Notes.
The genre id can be passed to other endpoints as a parameter to get podcasts in a specific genre,
e.g., `GET /best_podcasts`, `GET /search`...
You may want to cache the list of genres on the client side.
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
    listen_api_key="<X-ListenAPI-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.directory_api.get_genres(
    top_level_only=1,
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

**top_level_only:** `typing.Optional[int]` — Just show top level genres? If 1, yes, just show top level genres. If 0, no, show all genres.
    
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

<details><summary><code>client.directory_api.<a href="src/fern/directory_api/client.py">just_listen</a>() -> EpisodeSimple</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Recently published episodes are more likely to be fetched. Good luck!
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
    listen_api_key="<X-ListenAPI-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.directory_api.just_listen()

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

<details><summary><code>client.directory_api.<a href="src/fern/directory_api/client.py">get_languages</a>() -> GetLanguagesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of languages that are supported in Listen Notes database. You can use the language string as query parameter in `GET /search`.
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
    listen_api_key="<X-ListenAPI-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.directory_api.get_languages()

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

<details><summary><code>client.directory_api.<a href="src/fern/directory_api/client.py">get_podcasts_in_batch</a>(...) -> GetPodcastsInBatchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Batch fetch basic meta data for up to 10 podcasts.
This endpoint could be used to build something like OPML import,
allowing users to import a bunch of podcasts via rss urls.
For detailed meta data (including episodes) of an individual podcast, you need to use `GET /podcasts/{id}`. This endpoint is available only in the PRO/ENTERPRISE plan.
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
    listen_api_key="<X-ListenAPI-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.directory_api.get_podcasts_in_batch()

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

**request:** `GetPodcastsInBatchForm` 
    
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

<details><summary><code>client.directory_api.<a href="src/fern/directory_api/client.py">get_podcast_by_id</a>(...) -> PodcastFull</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch detailed meta data and episodes for a specific podcast (up to 10 episodes each time).
You can use the **next_episode_pub_date** parameter to do pagination and fetch more episodes.
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
    listen_api_key="<X-ListenAPI-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.directory_api.get_podcast_by_id(
    id="4d3fe717742d4963a85562e9f84d8c79",
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

**id:** `str` — Podcast id. You can get podcast id from using other endpoints, e.g., `GET /search`, `GET /best_podcasts`...
    
</dd>
</dl>

<dl>
<dd>

**next_episode_pub_date:** `typing.Optional[int]` — For episodes pagination. It's the value of **next_episode_pub_date** from the response of last request. If not specified, just return latest 10 episodes or oldest 10 episodes, depending on the value of the **sort** parameter.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetPodcastByIdRequestSort]` — How do you want to sort the episodes of this podcast?
    
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

<details><summary><code>client.directory_api.<a href="src/fern/directory_api/client.py">get_podcast_recommendations</a>(...) -> GetPodcastRecommendationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch up to 8 podcast recommendations based on the given podcast id.
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
    listen_api_key="<X-ListenAPI-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.directory_api.get_podcast_recommendations(
    id="25212ac3c53240a880dd5032e547047b",
    safe_mode=0,
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

**id:** `str` — Podcast id.
    
</dd>
</dl>

<dl>
<dd>

**safe_mode:** `typing.Optional[int]` — Whether or not to exclude podcasts with explicit language. 1 is yes, and 0 is no.
    
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

<details><summary><code>client.directory_api.<a href="src/fern/directory_api/client.py">get_regions</a>() -> GetRegionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

It returns a dictionary of country codes (e.g., us, gb...) & country names (United States, United Kingdom...). The country code is used in the query parameter **region** of `GET /best_podcasts`.
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
    listen_api_key="<X-ListenAPI-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.directory_api.get_regions()

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

## Playlist API
<details><summary><code>client.playlist_api.<a href="src/fern/playlist_api/client.py">get_playlists</a>(...) -> PlaylistsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint returns same data as listennotes.com/listen under your account.
You can use the **page** parameter to do pagination and fetch more playlists.
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
    listen_api_key="<X-ListenAPI-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.playlist_api.get_playlists(
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

**sort:** `typing.Optional[GetPlaylistsRequestSort]` — How do you want to sort playlists?
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number of playlists.
    
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

<details><summary><code>client.playlist_api.<a href="src/fern/playlist_api/client.py">get_playlist_by_id</a>(...) -> PlaylistResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A playlist can be an episode list (i.e., all items are episodes) or a podcast list (i.e., all items are podcasts),
which is essentially the same as those created via listennotes.com/listen/.
This endpoint fetches a list of items (i.e., episodes or podcasts) in the playlist.
You can use the **last_pub_date_ms** parameter to do pagination and fetch more items.
A playlist can be **public** (discoverable on ListenNotes.com),
**unlisted** (accessible to anyone who knows the playlist id),
or **private** (accessible to its owner).
You can fetch all playlists created by you, and **public** / **unlisted** playlists created by others.
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
    listen_api_key="<X-ListenAPI-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.playlist_api.get_playlist_by_id(
    id="m1pe7z60bsw",
    last_timestamp_ms=0,
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

Playlist id (always 11 characters, e.g., m1pe7z60bsw).
You can get the podcast id from the url of a playlist, e.g.,
m1pe7z60bsw is the playlist id of listennotes.com/listen/podcasts-about-podcasting-m1pe7z60bsw
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[GetPlaylistByIdRequestType]` — The type of this playlist, which should be either **episode_list** or **podcast_list**.
    
</dd>
</dl>

<dl>
<dd>

**last_timestamp_ms:** `typing.Optional[int]` 

For playlist items pagination.
It's the value of **last_timestamp_ms** from the response of last request.
If it's 0 or not specified, just return the latest or the oldest 20 items,
depending on the value of the **sort** parameter.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetPlaylistByIdRequestSort]` — How do you want to sort playlist items?
    
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

## Insights API
<details><summary><code>client.insights_api.<a href="src/fern/insights_api/client.py">get_podcasts_by_domain_name</a>(...) -> PodcastDomainResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch podcasts by a publisher's domain name, e.g., nytimes.com, wondery.com, npr.org...
Each request will return up to 10 podcasts. You can use the `page` parameter to paginate.
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
    listen_api_key="<X-ListenAPI-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.insights_api.get_podcasts_by_domain_name(
    domain_name="nytimes.com",
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

**domain_name:** `str` — A publisher's domain name, e.g., nytimes.com, wondery.com, npr.org...
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number of the podcasts from this domain name
    
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

<details><summary><code>client.insights_api.<a href="src/fern/insights_api/client.py">get_podcast_audience</a>(...) -> PodcastAudienceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch audience demographics for a podcast - 1) directly measured on the Listen Notes platform; 2) only supports audience breakdown by regions for now; 3) not every podcast has data.
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
    listen_api_key="<X-ListenAPI-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.insights_api.get_podcast_audience(
    id="25212ac3c53240a880dd5032e547047b",
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

**id:** `str` — Podcast id.
    
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

## Podcaster API
<details><summary><code>client.podcaster_api.<a href="src/fern/podcaster_api/client.py">submit_podcast</a>(...) -> SubmitPodcastResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Podcast hosting services can use this endpoint to help your users directly submit a new podcast to Listen Notes database. If the podcast doesn't exist in the database, "status" in the response will be "in review", and we'll review it within 12 hours. If the podcast exists, "status" in the response will be "found". If this submission is rejected, "status" in the response will be "rejected". You can use `POST /podcasts` to check if multiple podcasts exist in the database. If you want to get a notification once the podcast is accepted, you can either specify the "email" parameter or configure a webhook url in the dashboard: listennotes.com/api/dashboard/#webhooks
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
    listen_api_key="<X-ListenAPI-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.podcaster_api.submit_podcast(
    rss="https://feeds.megaphone.fm/committed",
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

**request:** `SubmitPodcastForm` 
    
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

<details><summary><code>client.podcaster_api.<a href="src/fern/podcaster_api/client.py">delete_podcast_by_id</a>(...) -> DeletePodcastResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Podcast hosting services can use this endpoint to streamline the process of podcast deletion on behave of their users (podcasters). We will review the deletion request within 12 hours. If the podcast is already deleted, the "status" field in the response will be "deleted". Otherwise, the status field will be "in review". If you want to get a notification once the podcast is deleted, you can configure a webhook url in the dashboard: listennotes.com/api/dashboard/#webhooks
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
    listen_api_key="<X-ListenAPI-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.podcaster_api.delete_podcast_by_id(
    id="4d3fe717742d4963a85562e9f84d8c79",
    reason="the podcaster wants to delete it",
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

**id:** `str` — Podcast id. You can get podcast id from using other endpoints, e.g., `GET /search`, `GET /best_podcasts`...
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` — The reason why this podcast should be deleted, e.g., copyright violation, the podcaster wants to delete it... You can put "testing" here to indicate that you are testing this endpoint, so we will not actually delete the podcast.
    
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

## Search API
<details><summary><code>client.search_api.<a href="src/fern/search_api/client.py">get_related_searches</a>(...) -> RelatedSearchesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Suggest related search terms. The results are more comprehensive than from `GET /typeahead`. This endpoint is available only in the PRO/ENTERPRISE plan.
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
    listen_api_key="<X-ListenAPI-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.search_api.get_related_searches(
    q="evergrande",
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

**q:** `str` — Search term, e.g., person, place, topic...
    
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

<details><summary><code>client.search_api.<a href="src/fern/search_api/client.py">search</a>(...) -> SearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Full-text search on episodes, podcasts, or curated lists of podcasts.
Use the `offset` parameter to paginate through search results.
The FREE plan allows to see up to 30 search results (or `offset` < 30) per query.
The PRO plan allows to see up to 300 search results (or `offset` < 300) per query.
The ENTERPRISE plan allows to see up to 10,000 search results (or `offset` < 10000) per query.
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
    listen_api_key="<X-ListenAPI-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.search_api.search(
    q="star wars",
    sort_by_date=0,
    offset=0,
    len_min=10,
    len_max=30,
    genre_ids="68,82",
    published_before=1580172454000,
    published_after=0,
    only_in="title,description",
    language="English",
    region="",
    safe_mode=0,
    unique_podcasts=0,
    page_size=10,
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

**q:** `str` — Search term, e.g., person, place, topic... You can use double quotes to do verbatim match, e.g., "game of thrones". Otherwise, it's fuzzy search.
    
</dd>
</dl>

<dl>
<dd>

**sort_by_date:** `typing.Optional[int]` — Sort by date or not? If 0, then sort by relevance. If 1, then sort by date.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[SearchRequestType]` — What type of contents do you want to search for? 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Offset for search results, for pagination. You'll use **next_offset** from response for this parameter.
    
</dd>
</dl>

<dl>
<dd>

**len_min:** `typing.Optional[int]` 

Minimum audio length in minutes. Applicable only when **type** parameter is **episode** or **podcast**.
If **type** parameter is **episode**, it's for audio length of an episode.
If **type** parameter is **podcast**, it's for average audio length of all episodes in a podcast.
    
</dd>
</dl>

<dl>
<dd>

**len_max:** `typing.Optional[int]` 

Maximum audio length in minutes. Applicable only when **type** parameter is **episode** or **podcast**.
If **type** parameter is **episode**, it's for audio length of an episode.
If **type** parameter is **podcast**, it's for average audio length of all episodes in a podcast.
    
</dd>
</dl>

<dl>
<dd>

**episode_count_min:** `typing.Optional[int]` — Minimum number of episodes. Applicable only when type parameter is **podcast**.
    
</dd>
</dl>

<dl>
<dd>

**episode_count_max:** `typing.Optional[int]` — Maximum number of episodes. Applicable only when type parameter is **podcast**.
    
</dd>
</dl>

<dl>
<dd>

**update_freq_min:** `typing.Optional[int]` — Minimum update frequency in hours (how frequently does a podcast release a new episode). For example, if you want to find "weekly" podcasts, then you can set **update_freq_min**=144 hours (or 6 days) and **update_freq_max**=192 hours (or 8 days). Applicable only when type parameter is **podcast**.
    
</dd>
</dl>

<dl>
<dd>

**update_freq_max:** `typing.Optional[int]` — Maximum update frequency in hours (how frequently does a podcast release a new episode). For example, if you want to find "weekly" podcasts, then you can set **update_freq_min**=144 hours (or 6 days) and **update_freq_max**=192 hours (or 8 days). Applicable only when type parameter is **podcast**.
    
</dd>
</dl>

<dl>
<dd>

**genre_ids:** `typing.Optional[str]` — A comma-delimited string of a list of genre ids. If not specified, then all genres are included. You can find the id and the name of all genres from `GET /genres`. It works only when **type** is *episode* or *podcast*.
    
</dd>
</dl>

<dl>
<dd>

**published_before:** `typing.Optional[int]` — Only show episodes/podcasts/curated lists published before this timestamp (in milliseconds). If **published_before** & **published_after** are used at the same time, **published_before** should be bigger than **published_after**.
    
</dd>
</dl>

<dl>
<dd>

**published_after:** `typing.Optional[int]` — Only show episodes/podcasts/curated lists published after this timestamp (in milliseconds). If **published_before** & **published_after** are used at the same time, **published_before** should be bigger than **published_after**.
    
</dd>
</dl>

<dl>
<dd>

**only_in:** `typing.Optional[str]` — A comma-delimited string to search only in specific fields. Allowed values are title, description, author, and audio. If not specified, then search every fields.
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — Limit search results to a specific language. If not specified, it'll be any language. You can get a list of supported languages from `GET /languages`. It works only when **type** is *episode* or *podcast*.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Limit search results to a specific region (e.g., us, gb, in...). If not specified, it'll be any region. You can get the supported country codes from `GET /regions`. It works only when **type** is *episode* or *podcast*.
    
</dd>
</dl>

<dl>
<dd>

**ocid:** `typing.Optional[str]` — A comma-delimited string of podcast ids (up to 5 podcasts) - you can get a podcast id from the **podcast_id** field in response. This parameter is to limit search results from only a few specific podcasts. It works only when **type** is *episode*.
    
</dd>
</dl>

<dl>
<dd>

**ncid:** `typing.Optional[str]` — A comma-delimited string of podcast ids (up to 5 podcasts) - you can get a podcast id from the **podcast_id** field in response. This parameter is to exclude search results of a few specific podcasts. It works only when **type** is *episode*.
    
</dd>
</dl>

<dl>
<dd>

**safe_mode:** `typing.Optional[int]` — Whether or not to exclude podcasts/episodes with explicit language. 1 is yes and 0 is no. It works only when **type** is *episode* or *podcast*.
    
</dd>
</dl>

<dl>
<dd>

**unique_podcasts:** `typing.Optional[int]` — Whether or not to keep only one episode per podcast in search results. 1 is yes and 0 is no. It works only when **type** is *episode*.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of search results per page. A valid value should be an integer between 1 and 10 (inclusive).
    
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

<details><summary><code>client.search_api.<a href="src/fern/search_api/client.py">spellcheck</a>(...) -> SpellCheckResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Suggest a list of words that correct the spelling errors of a search term. This endpoint is available only in the PRO/ENTERPRISE plan.
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
    listen_api_key="<X-ListenAPI-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.search_api.spellcheck(
    q="evergrand stok",
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

**q:** `str` — Search term, e.g., person, place, topic...
    
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

<details><summary><code>client.search_api.<a href="src/fern/search_api/client.py">get_trending_searches</a>() -> TrendingSearchesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch up to 10 most recent trending search terms on the Listen Notes platform.
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
    listen_api_key="<X-ListenAPI-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.search_api.get_trending_searches()

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

<details><summary><code>client.search_api.<a href="src/fern/search_api/client.py">typeahead</a>(...) -> TypeaheadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Suggest search terms, podcast genres, and podcasts.
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
    listen_api_key="<X-ListenAPI-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.search_api.typeahead(
    q="star wars",
    show_podcasts=1,
    show_genres=1,
    safe_mode=0,
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

**q:** `str` — Search term, e.g., person, place, topic... You can use double quotes to do verbatim match, e.g., "game of thrones". Otherwise, it's fuzzy search.
    
</dd>
</dl>

<dl>
<dd>

**show_podcasts:** `typing.Optional[int]` — Autosuggest podcasts. This only searches podcast title and publisher and returns very limited info of 5 podcasts. 1 is yes, 0 is no. It's a bit slow to autosuggest podcasts, so we turn it off by default. If show_podcasts=1, you can also pass iTunes id (e.g., 474722933) to the q parameter to fetch podcast meta data.
    
</dd>
</dl>

<dl>
<dd>

**show_genres:** `typing.Optional[int]` — Whether or not to autosuggest genres. 1 is yes, 0 is no.
    
</dd>
</dl>

<dl>
<dd>

**safe_mode:** `typing.Optional[int]` — Whether or not to exclude podcasts/episodes with explicit language. 1 is yes and 0 is no. It works only when **show_podcasts** is *1*.
    
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

