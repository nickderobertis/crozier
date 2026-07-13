# Reference
## App
<details><summary><code>client.app.<a href="src/fern/app/client.py">getapplicationapiusage</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get API usage by application for time frame specified. You can go as far back as 30 days ago, and can ask for up to a 48 hour window of time in a single request. You must be authenticated with at least the ReadUserData permission to access this endpoint.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.app.getapplicationapiusage(
    application_id=1,
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

**application_id:** `int` — ID of the application to get usage statistics.
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[dt.datetime]` — End time for query. Goes to now if not specified.
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[dt.datetime]` — Start time for query. Goes to 24 hours ago if not specified.
    
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

<details><summary><code>client.app.<a href="src/fern/app/client.py">getbungieapplications</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get list of applications created by Bungie.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.app.getbungieapplications()

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

## CommunityContent
<details><summary><code>client.communitycontent.<a href="src/fern/communitycontent/client.py">getcommunitycontent</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns community content.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.communitycontent.getcommunitycontent(
    sort=1,
    media_filter=1,
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

**sort:** `int` — The sort mode.
    
</dd>
</dl>

<dl>
<dd>

**media_filter:** `int` — The type of media to get
    
</dd>
</dl>

<dl>
<dd>

**page:** `int` — Zero based page
    
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

## Content
<details><summary><code>client.content.<a href="src/fern/content/client.py">getcontentbyid</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a content item referenced by id
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.content.getcontentbyid(
    id=1000000,
    locale="locale",
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

**id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**locale:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**head:** `typing.Optional[bool]` — false
    
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

<details><summary><code>client.content.<a href="src/fern/content/client.py">getcontentbytagandtype</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the newest item that matches a given tag and Content Type.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.content.getcontentbytagandtype(
    tag="tag",
    type="type",
    locale="locale",
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

**tag:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**locale:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**head:** `typing.Optional[bool]` — Not used.
    
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

<details><summary><code>client.content.<a href="src/fern/content/client.py">getcontenttype</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets an object describing a particular variant of content.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.content.getcontenttype(
    type="type",
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

**type:** `str` — 
    
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

<details><summary><code>client.content.<a href="src/fern/content/client.py">rssnewsarticles</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a JSON string response that is the RSS feed for news articles.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.content.rssnewsarticles(
    page_token="pageToken",
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

**page_token:** `str` — Zero-based pagination token for paging through result sets.
    
</dd>
</dl>

<dl>
<dd>

**categoryfilter:** `typing.Optional[str]` — Optionally filter response to only include news items in a certain category.
    
</dd>
</dl>

<dl>
<dd>

**includebody:** `typing.Optional[bool]` — Optionally include full content body for each news item.
    
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

<details><summary><code>client.content.<a href="src/fern/content/client.py">searchcontentwithtext</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets content based on querystring information passed in. Provides basic search and text search capabilities.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.content.searchcontentwithtext(
    locale="locale",
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

**locale:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**ctype:** `typing.Optional[str]` — Content type tag: Help, News, etc. Supply multiple ctypes separated by space.
    
</dd>
</dl>

<dl>
<dd>

**currentpage:** `typing.Optional[int]` — Page number for the search results, starting with page 1.
    
</dd>
</dl>

<dl>
<dd>

**head:** `typing.Optional[bool]` — Not used.
    
</dd>
</dl>

<dl>
<dd>

**searchtext:** `typing.Optional[str]` — Word or phrase for the search.
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[str]` — For analytics, hint at the part of the app that triggered the search. Optional.
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[str]` — Tag used on the content to be searched.
    
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

<details><summary><code>client.content.<a href="src/fern/content/client.py">searchcontentbytagandtype</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for Content Items that match the given Tag and Content Type.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.content.searchcontentbytagandtype(
    tag="tag",
    type="type",
    locale="locale",
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

**tag:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**locale:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**currentpage:** `typing.Optional[int]` — Page number for the search results starting with page 1.
    
</dd>
</dl>

<dl>
<dd>

**head:** `typing.Optional[bool]` — Not used.
    
</dd>
</dl>

<dl>
<dd>

**itemsperpage:** `typing.Optional[int]` — Not used.
    
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

<details><summary><code>client.content.<a href="src/fern/content/client.py">searchhelparticles</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for Help Articles.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.content.searchhelparticles(
    searchtext="searchtext",
    size="size",
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

**searchtext:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**size:** `str` — 
    
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

## Destiny2
<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">equipitem</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Equip an item. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.equipitem()

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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">equipitems</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Equip a list of items by itemInstanceIds. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Any items not found on your character will be ignored.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.equipitems()

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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">insertsocketplug</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Insert a plug into a socketed item. I know how it sounds, but I assure you it's much more G-rated than you might be guessing. We haven't decided yet whether this will be able to insert plugs that have side effects, but if we do it will require special scope permission for an application attempting to do so. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Request must include proof of permission for 'InsertPlugs' from the account owner.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.insertsocketplug()

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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">insertsocketplugfree</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Insert a 'free' plug into an item's socket. This does not require 'Advanced Write Action' authorization and is available to 3rd-party apps, but will only work on 'free and reversible' socket actions (Perks, Armor Mods, Shaders, Ornaments, etc.). You must have a valid Destiny Account, and the character must either be in a social space, in orbit, or offline.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.insertsocketplugfree()

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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">pullfrompostmaster</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Extract an item from the Postmaster, with whatever implications that may entail. You must have a valid Destiny account. You must also pass BOTH a reference AND an instance ID if it's an instanced item.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.pullfrompostmaster()

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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">setitemlockstate</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set the Lock State for an instanced item. You must have a valid Destiny Account.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.setitemlockstate()

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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">setquesttrackedstate</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set the Tracking State for an instanced item, if that item is a Quest or Bounty. You must have a valid Destiny Account. Yeah, it's an item.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.setquesttrackedstate()

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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">transferitem</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Transfer an item to/from your vault. You must have a valid Destiny account. You must also pass BOTH a reference AND an instance ID if it's an instanced item. itshappening.gif
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.transferitem()

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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">clearloadout</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Clear the identifiers and items of a loadout.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.clearloadout()

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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">equiploadout</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Equip a loadout. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.equiploadout()

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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">snapshotloadout</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Snapshot a loadout with the currently equipped items.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.snapshotloadout()

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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">updateloadoutidentifiers</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the color, icon, and name of a loadout.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.updateloadoutidentifiers()

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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">searchdestinyentities</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a page list of Destiny items.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.searchdestinyentities(
    type="type",
    search_term="searchTerm",
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

**type:** `str` — The type of entity for whom you would like results. These correspond to the entity's definition contract name. For instance, if you are looking for items, this property should be 'DestinyInventoryItemDefinition'.
    
</dd>
</dl>

<dl>
<dd>

**search_term:** `str` — The string to use when searching for Destiny entities.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number to return, starting with 0.
    
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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">awaprovideauthorizationresult</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provide the result of the user interaction. Called by the Bungie Destiny App to approve or reject a request.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.awaprovideauthorizationresult()

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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">awagetactiontoken</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the action token if user approves the request.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.awagetactiontoken(
    correlation_id="correlationId",
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

**correlation_id:** `str` — The identifier for the advanced write action request.
    
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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">awainitializerequest</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initialize a request to perform an advanced write action.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.awainitializerequest()

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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">getclanbannersource</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the dictionary of values for the Clan Banner
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.getclanbannersource()

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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">getclanweeklyrewardstate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information on the weekly clan rewards and if the clan has earned them or not. Note that this will always report rewards as not redeemed.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.getclanweeklyrewardstate(
    group_id=1000000,
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

**group_id:** `int` — A valid group id of clan.
    
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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">getdestinymanifest</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current version of the manifest as a json object.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.getdestinymanifest()

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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">getdestinyentitydefinition</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the static definition of an entity of the given Type and hash identifier. Examine the API Documentation for the Type Names of entities that have their own definitions. Note that the return type will always *inherit from* DestinyDefinition, but the specific type returned will be the requested entity type if it can be found. Please don't use this as a chatty alternative to the Manifest database if you require large sets of data, but for simple and one-off accesses this should be handy.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.getdestinyentitydefinition(
    entity_type="entityType",
    hash_identifier=1,
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

**entity_type:** `str` — The type of entity for whom you would like results. These correspond to the entity's definition contract name. For instance, if you are looking for items, this property should be 'DestinyInventoryItemDefinition'. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is tentatively in final form, but there may be bugs that prevent desirable operation.
    
</dd>
</dl>

<dl>
<dd>

**hash_identifier:** `int` — The hash identifier for the specific Entity you want returned.
    
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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">getpublicmilestones</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets public information about currently available Milestones.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.getpublicmilestones()

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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">getpublicmilestonecontent</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets custom localized content for the milestone of the given hash, if it exists.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.getpublicmilestonecontent(
    milestone_hash=1,
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

**milestone_hash:** `int` — The identifier for the milestone to be returned.
    
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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">searchdestinyplayerbybungiename</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of Destiny memberships given a global Bungie Display Name. This method will hide overridden memberships due to cross save.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.searchdestinyplayerbybungiename(
    membership_type=1,
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

**membership_type:** `int` — A valid non-BungieNet membership type, or All. Indicates which memberships to return. You probably want this set to All.
    
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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">getclanaggregatestats</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets aggregated stats for a clan using the same categories as the clan leaderboards. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.getclanaggregatestats(
    group_id=1000000,
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

**group_id:** `int` — Group ID of the clan whose leaderboards you wish to fetch.
    
</dd>
</dl>

<dl>
<dd>

**modes:** `typing.Optional[str]` — List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
    
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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">gethistoricalstatsdefinition</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets historical stats definitions.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.gethistoricalstatsdefinition()

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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">getclanleaderboards</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.getclanleaderboards(
    group_id=1000000,
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

**group_id:** `int` — Group ID of the clan whose leaderboards you wish to fetch.
    
</dd>
</dl>

<dl>
<dd>

**maxtop:** `typing.Optional[int]` — Maximum number of top players to return. Use a large number to get entire leaderboard.
    
</dd>
</dl>

<dl>
<dd>

**modes:** `typing.Optional[str]` — List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
    
</dd>
</dl>

<dl>
<dd>

**statid:** `typing.Optional[str]` — ID of stat to return rather than returning all Leaderboard stats.
    
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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">getleaderboardsforcharacter</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.getleaderboardsforcharacter(
    membership_type=1,
    destiny_membership_id=1000000,
    character_id=1000000,
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

**membership_type:** `int` — A valid non-BungieNet membership type.
    
</dd>
</dl>

<dl>
<dd>

**destiny_membership_id:** `int` — The Destiny membershipId of the user to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**character_id:** `int` — The specific character to build the leaderboard around for the provided Destiny Membership.
    
</dd>
</dl>

<dl>
<dd>

**maxtop:** `typing.Optional[int]` — Maximum number of top players to return. Use a large number to get entire leaderboard.
    
</dd>
</dl>

<dl>
<dd>

**modes:** `typing.Optional[str]` — List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
    
</dd>
</dl>

<dl>
<dd>

**statid:** `typing.Optional[str]` — ID of stat to return rather than returning all Leaderboard stats.
    
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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">getpostgamecarnagereport</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the available post game carnage report for the activity ID.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.getpostgamecarnagereport(
    activity_id=1000000,
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

**activity_id:** `int` — The ID of the activity whose PGCR is requested.
    
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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">reportoffensivepostgamecarnagereportplayer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Report a player that you met in an activity that was engaging in ToS-violating activities. Both you and the offending player must have played in the activityId passed in. Please use this judiciously and only when you have strong suspicions of violation, pretty please.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.reportoffensivepostgamecarnagereportplayer(
    activity_id=1000000,
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

**activity_id:** `int` — The ID of the activity where you ran into the brigand that you're reporting.
    
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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">getpublicvendors</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get items available from vendors where the vendors have items for sale that are common for everyone. If any portion of the Vendor's available inventory is character or account specific, we will be unable to return their data from this endpoint due to the way that available inventory is computed. As I am often guilty of saying: 'It's a long story...'
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.getpublicvendors()

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

**components:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` — A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
    
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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">gethistoricalstats</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets historical stats for indicated character.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.gethistoricalstats(
    membership_type=1,
    destiny_membership_id=1000000,
    character_id=1000000,
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

**membership_type:** `int` — A valid non-BungieNet membership type.
    
</dd>
</dl>

<dl>
<dd>

**destiny_membership_id:** `int` — The Destiny membershipId of the user to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**character_id:** `int` — The id of the character to retrieve. You can omit this character ID or set it to 0 to get aggregate stats across all characters.
    
</dd>
</dl>

<dl>
<dd>

**dayend:** `typing.Optional[dt.datetime]` — Last day to return when daily stats are requested. Use the format YYYY-MM-DD. Currently, we cannot allow more than 31 days of daily data to be requested in a single request.
    
</dd>
</dl>

<dl>
<dd>

**daystart:** `typing.Optional[dt.datetime]` — First day to return when daily stats are requested. Use the format YYYY-MM-DD. Currently, we cannot allow more than 31 days of daily data to be requested in a single request.
    
</dd>
</dl>

<dl>
<dd>

**groups:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` — Group of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals
    
</dd>
</dl>

<dl>
<dd>

**modes:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` — Game modes to return. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
    
</dd>
</dl>

<dl>
<dd>

**period_type:** `typing.Optional[int]` — Indicates a specific period type to return. Optional. May be: Daily, AllTime, or Activity
    
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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">getactivityhistory</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets activity history stats for indicated character.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.getactivityhistory(
    membership_type=1,
    destiny_membership_id=1000000,
    character_id=1000000,
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

**membership_type:** `int` — A valid non-BungieNet membership type.
    
</dd>
</dl>

<dl>
<dd>

**destiny_membership_id:** `int` — The Destiny membershipId of the user to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**character_id:** `int` — The id of the character to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — Number of rows to return
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[int]` — A filter for the activity mode to be returned. None returns all activities. See the documentation for DestinyActivityModeType for valid values, and pass in string representation.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number to return, starting with 0.
    
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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">getdestinyaggregateactivitystats</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets all activities the character has participated in together with aggregate statistics for those activities.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.getdestinyaggregateactivitystats(
    membership_type=1,
    destiny_membership_id=1000000,
    character_id=1000000,
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

**membership_type:** `int` — A valid non-BungieNet membership type.
    
</dd>
</dl>

<dl>
<dd>

**destiny_membership_id:** `int` — The Destiny membershipId of the user to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**character_id:** `int` — The specific character whose activities should be returned.
    
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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">getuniqueweaponhistory</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets details about unique weapon usage, including all exotic weapons.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.getuniqueweaponhistory(
    membership_type=1,
    destiny_membership_id=1000000,
    character_id=1000000,
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

**membership_type:** `int` — A valid non-BungieNet membership type.
    
</dd>
</dl>

<dl>
<dd>

**destiny_membership_id:** `int` — The Destiny membershipId of the user to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**character_id:** `int` — The id of the character to retrieve.
    
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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">gethistoricalstatsforaccount</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets aggregate historical stats organized around each character for a given account.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.gethistoricalstatsforaccount(
    membership_type=1,
    destiny_membership_id=1000000,
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

**membership_type:** `int` — A valid non-BungieNet membership type.
    
</dd>
</dl>

<dl>
<dd>

**destiny_membership_id:** `int` — The Destiny membershipId of the user to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**groups:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` — Groups of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals.
    
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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">getleaderboards</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint has not yet been implemented. It is being returned for a preview of future functionality, and for public comment/suggestion/preparation.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.getleaderboards(
    membership_type=1,
    destiny_membership_id=1000000,
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

**membership_type:** `int` — A valid non-BungieNet membership type.
    
</dd>
</dl>

<dl>
<dd>

**destiny_membership_id:** `int` — The Destiny membershipId of the user to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**maxtop:** `typing.Optional[int]` — Maximum number of top players to return. Use a large number to get entire leaderboard.
    
</dd>
</dl>

<dl>
<dd>

**modes:** `typing.Optional[str]` — List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
    
</dd>
</dl>

<dl>
<dd>

**statid:** `typing.Optional[str]` — ID of stat to return rather than returning all Leaderboard stats.
    
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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">getprofile</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns Destiny Profile information for the supplied membership.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.getprofile(
    membership_type=1,
    destiny_membership_id=1000000,
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

**membership_type:** `int` — A valid non-BungieNet membership type.
    
</dd>
</dl>

<dl>
<dd>

**destiny_membership_id:** `int` — Destiny membership ID.
    
</dd>
</dl>

<dl>
<dd>

**components:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` — A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
    
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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">getcharacter</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns character information for the supplied character.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.getcharacter(
    membership_type=1,
    destiny_membership_id=1000000,
    character_id=1000000,
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

**membership_type:** `int` — A valid non-BungieNet membership type.
    
</dd>
</dl>

<dl>
<dd>

**destiny_membership_id:** `int` — Destiny membership ID.
    
</dd>
</dl>

<dl>
<dd>

**character_id:** `int` — ID of the character.
    
</dd>
</dl>

<dl>
<dd>

**components:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` — A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
    
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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">getcollectiblenodedetails</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Given a Presentation Node that has Collectibles as direct descendants, this will return item details about those descendants in the context of the requesting character.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.getcollectiblenodedetails(
    membership_type=1,
    destiny_membership_id=1000000,
    character_id=1000000,
    collectible_presentation_node_hash=1,
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

**membership_type:** `int` — A valid non-BungieNet membership type.
    
</dd>
</dl>

<dl>
<dd>

**destiny_membership_id:** `int` — Destiny membership ID of another user. You may be denied.
    
</dd>
</dl>

<dl>
<dd>

**character_id:** `int` — The Destiny Character ID of the character for whom we're getting collectible detail info.
    
</dd>
</dl>

<dl>
<dd>

**collectible_presentation_node_hash:** `int` — The hash identifier of the Presentation Node for whom we should return collectible details. Details will only be returned for collectibles that are direct descendants of this node.
    
</dd>
</dl>

<dl>
<dd>

**components:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` — A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
    
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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">getvendors</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get currently available vendors from the list of vendors that can possibly have rotating inventory. Note that this does not include things like preview vendors and vendors-as-kiosks, neither of whom have rotating/dynamic inventories. Use their definitions as-is for those.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.getvendors(
    membership_type=1,
    destiny_membership_id=1000000,
    character_id=1000000,
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

**membership_type:** `int` — A valid non-BungieNet membership type.
    
</dd>
</dl>

<dl>
<dd>

**destiny_membership_id:** `int` — Destiny membership ID of another user. You may be denied.
    
</dd>
</dl>

<dl>
<dd>

**character_id:** `int` — The Destiny Character ID of the character for whom we're getting vendor info.
    
</dd>
</dl>

<dl>
<dd>

**components:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` — A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[int]` — The filter of what vendors and items to return, if any.
    
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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">getvendor</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the details of a specific Vendor.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.getvendor(
    membership_type=1,
    destiny_membership_id=1000000,
    character_id=1000000,
    vendor_hash=1,
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

**membership_type:** `int` — A valid non-BungieNet membership type.
    
</dd>
</dl>

<dl>
<dd>

**destiny_membership_id:** `int` — Destiny membership ID of another user. You may be denied.
    
</dd>
</dl>

<dl>
<dd>

**character_id:** `int` — The Destiny Character ID of the character for whom we're getting vendor info.
    
</dd>
</dl>

<dl>
<dd>

**vendor_hash:** `int` — The Hash identifier of the Vendor to be returned.
    
</dd>
</dl>

<dl>
<dd>

**components:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` — A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
    
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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">getitem</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the details of an instanced Destiny Item. An instanced Destiny item is one with an ItemInstanceId. Non-instanced items, such as materials, have no useful instance-specific details and thus are not queryable here.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.getitem(
    membership_type=1,
    destiny_membership_id=1000000,
    item_instance_id=1000000,
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

**membership_type:** `int` — A valid non-BungieNet membership type.
    
</dd>
</dl>

<dl>
<dd>

**destiny_membership_id:** `int` — The membership ID of the destiny profile.
    
</dd>
</dl>

<dl>
<dd>

**item_instance_id:** `int` — The Instance ID of the destiny item.
    
</dd>
</dl>

<dl>
<dd>

**components:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` — A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
    
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

<details><summary><code>client.destiny2.<a href="src/fern/destiny2/client.py">getlinkedprofiles</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a summary information about all profiles linked to the requesting membership type/membership ID that have valid Destiny information. The passed-in Membership Type/Membership ID may be a Bungie.Net membership or a Destiny membership. It only returns the minimal amount of data to begin making more substantive requests, but will hopefully serve as a useful alternative to UserServices for people who just care about Destiny data. Note that it will only return linked accounts whose linkages you are allowed to view.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.destiny2.getlinkedprofiles(
    membership_type=1,
    membership_id=1000000,
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

**membership_type:** `int` — The type for the membership whose linked Destiny accounts you want returned.
    
</dd>
</dl>

<dl>
<dd>

**membership_id:** `int` — The ID of the membership whose linked Destiny accounts you want returned. Make sure your membership ID matches its Membership Type: don't pass us a PSN membership ID and the XBox membership type, it's not going to work!
    
</dd>
</dl>

<dl>
<dd>

**get_all_memberships:** `typing.Optional[bool]` — (optional) if set to 'true', all memberships regardless of whether they're obscured by overrides will be returned. Normal privacy restrictions on account linking will still apply no matter what.
    
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

## Fireteam
<details><summary><code>client.fireteam.<a href="src/fern/fireteam/client.py">getactiveprivateclanfireteamcount</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a count of all active non-public fireteams for the specified clan. Maximum value returned is 25.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.fireteam.getactiveprivateclanfireteamcount(
    group_id=1000000,
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

**group_id:** `int` — The group id of the clan.
    
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

<details><summary><code>client.fireteam.<a href="src/fern/fireteam/client.py">getavailableclanfireteams</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a listing of all of this clan's fireteams that are have available slots. Caller is not checked for join criteria so caching is maximized.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.fireteam.getavailableclanfireteams(
    group_id=1000000,
    platform=1,
    activity_type=1,
    date_range=1,
    slot_filter=1,
    public_only=1,
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

**group_id:** `int` — The group id of the clan.
    
</dd>
</dl>

<dl>
<dd>

**platform:** `int` — The platform filter.
    
</dd>
</dl>

<dl>
<dd>

**activity_type:** `int` — The activity type to filter by.
    
</dd>
</dl>

<dl>
<dd>

**date_range:** `int` — The date range to grab available fireteams.
    
</dd>
</dl>

<dl>
<dd>

**slot_filter:** `int` — Filters based on available slots
    
</dd>
</dl>

<dl>
<dd>

**public_only:** `int` — Determines public/private filtering.
    
</dd>
</dl>

<dl>
<dd>

**page:** `int` — Zero based page
    
</dd>
</dl>

<dl>
<dd>

**exclude_immediate:** `typing.Optional[bool]` — If you wish the result to exclude immediate fireteams, set this to true. Immediate-only can be forced using the dateRange enum.
    
</dd>
</dl>

<dl>
<dd>

**lang_filter:** `typing.Optional[str]` — An optional language filter.
    
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

<details><summary><code>client.fireteam.<a href="src/fern/fireteam/client.py">getmyclanfireteams</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a listing of all fireteams that caller is an applicant, a member, or an alternate of.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.fireteam.getmyclanfireteams(
    group_id=1000000,
    platform=1,
    include_closed=True,
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

**group_id:** `int` — The group id of the clan. (This parameter is ignored unless the optional query parameter groupFilter is true).
    
</dd>
</dl>

<dl>
<dd>

**platform:** `int` — The platform filter.
    
</dd>
</dl>

<dl>
<dd>

**include_closed:** `bool` — If true, return fireteams that have been closed.
    
</dd>
</dl>

<dl>
<dd>

**page:** `int` — Deprecated parameter, ignored.
    
</dd>
</dl>

<dl>
<dd>

**group_filter:** `typing.Optional[bool]` — If true, filter by clan. Otherwise, ignore the clan and show all of the user's fireteams.
    
</dd>
</dl>

<dl>
<dd>

**lang_filter:** `typing.Optional[str]` — An optional language filter.
    
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

<details><summary><code>client.fireteam.<a href="src/fern/fireteam/client.py">getclanfireteam</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a specific fireteam.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.fireteam.getclanfireteam(
    group_id=1000000,
    fireteam_id=1000000,
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

**group_id:** `int` — The group id of the clan.
    
</dd>
</dl>

<dl>
<dd>

**fireteam_id:** `int` — The unique id of the fireteam.
    
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

<details><summary><code>client.fireteam.<a href="src/fern/fireteam/client.py">searchpublicavailableclanfireteams</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a listing of all public fireteams starting now with open slots. Caller is not checked for join criteria so caching is maximized.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.fireteam.searchpublicavailableclanfireteams(
    platform=1,
    activity_type=1,
    date_range=1,
    slot_filter=1,
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

**platform:** `int` — The platform filter.
    
</dd>
</dl>

<dl>
<dd>

**activity_type:** `int` — The activity type to filter by.
    
</dd>
</dl>

<dl>
<dd>

**date_range:** `int` — The date range to grab available fireteams.
    
</dd>
</dl>

<dl>
<dd>

**slot_filter:** `int` — Filters based on available slots
    
</dd>
</dl>

<dl>
<dd>

**page:** `int` — Zero based page
    
</dd>
</dl>

<dl>
<dd>

**exclude_immediate:** `typing.Optional[bool]` — If you wish the result to exclude immediate fireteams, set this to true. Immediate-only can be forced using the dateRange enum.
    
</dd>
</dl>

<dl>
<dd>

**lang_filter:** `typing.Optional[str]` — An optional language filter.
    
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

## Forum
<details><summary><code>client.forum.<a href="src/fern/forum/client.py">getcoretopicspaged</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a listing of all topics marked as part of the core group.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.forum.getcoretopicspaged(
    page=1,
    sort=1,
    quick_date=1,
    category_filter=1,
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

**page:** `int` — Zero base page
    
</dd>
</dl>

<dl>
<dd>

**sort:** `int` — The sort mode.
    
</dd>
</dl>

<dl>
<dd>

**quick_date:** `int` — The date filter.
    
</dd>
</dl>

<dl>
<dd>

**category_filter:** `int` — The category filter.
    
</dd>
</dl>

<dl>
<dd>

**locales:** `typing.Optional[str]` — Comma seperated list of locales posts must match to return in the result list. Default 'en'
    
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

<details><summary><code>client.forum.<a href="src/fern/forum/client.py">getforumtagsuggestions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets tag suggestions based on partial text entry, matching them with other tags previously used in the forums.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.forum.getforumtagsuggestions()

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

**partialtag:** `typing.Optional[str]` — The partial tag input to generate suggestions from.
    
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

<details><summary><code>client.forum.<a href="src/fern/forum/client.py">getpostandparent</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the post specified and its immediate parent.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.forum.getpostandparent(
    child_post_id=1000000,
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

**child_post_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**showbanned:** `typing.Optional[str]` — If this value is not null or empty, banned posts are requested to be returned
    
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

<details><summary><code>client.forum.<a href="src/fern/forum/client.py">getpostandparentawaitingapproval</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the post specified and its immediate parent of posts that are awaiting approval.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.forum.getpostandparentawaitingapproval(
    child_post_id=1000000,
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

**child_post_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**showbanned:** `typing.Optional[str]` — If this value is not null or empty, banned posts are requested to be returned
    
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

<details><summary><code>client.forum.<a href="src/fern/forum/client.py">getpoststhreadedpaged</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a thread of posts at the given parent, optionally returning replies to those posts as well as the original parent.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.forum.getpoststhreadedpaged(
    parent_post_id=1000000,
    page=1,
    page_size=1,
    reply_size=1,
    get_parent_post=True,
    root_thread_mode=True,
    sort_mode=1,
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

**parent_post_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**page:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**reply_size:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**get_parent_post:** `bool` — 
    
</dd>
</dl>

<dl>
<dd>

**root_thread_mode:** `bool` — 
    
</dd>
</dl>

<dl>
<dd>

**sort_mode:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**showbanned:** `typing.Optional[str]` — If this value is not null or empty, banned posts are requested to be returned
    
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

<details><summary><code>client.forum.<a href="src/fern/forum/client.py">getpoststhreadedpagedfromchild</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a thread of posts starting at the topicId of the input childPostId, optionally returning replies to those posts as well as the original parent.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.forum.getpoststhreadedpagedfromchild(
    child_post_id=1000000,
    page=1,
    page_size=1,
    reply_size=1,
    root_thread_mode=True,
    sort_mode=1,
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

**child_post_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**page:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**reply_size:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**root_thread_mode:** `bool` — 
    
</dd>
</dl>

<dl>
<dd>

**sort_mode:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**showbanned:** `typing.Optional[str]` — If this value is not null or empty, banned posts are requested to be returned
    
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

<details><summary><code>client.forum.<a href="src/fern/forum/client.py">gettopicforcontent</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the post Id for the given content item's comments, if it exists.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.forum.gettopicforcontent(
    content_id=1000000,
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

**content_id:** `int` — 
    
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

<details><summary><code>client.forum.<a href="src/fern/forum/client.py">gettopicspaged</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get topics from any forum.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.forum.gettopicspaged(
    page=1,
    page_size=1,
    group=1000000,
    sort=1,
    quick_date=1,
    category_filter=1,
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

**page:** `int` — Zero paged page number
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `int` — Unused
    
</dd>
</dl>

<dl>
<dd>

**group:** `int` — The group, if any.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `int` — The sort mode.
    
</dd>
</dl>

<dl>
<dd>

**quick_date:** `int` — A date filter.
    
</dd>
</dl>

<dl>
<dd>

**category_filter:** `int` — A category filter
    
</dd>
</dl>

<dl>
<dd>

**locales:** `typing.Optional[str]` — Comma seperated list of locales posts must match to return in the result list. Default 'en'
    
</dd>
</dl>

<dl>
<dd>

**tagstring:** `typing.Optional[str]` — The tags to search, if any.
    
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

<details><summary><code>client.forum.<a href="src/fern/forum/client.py">getpoll</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the specified forum poll.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.forum.getpoll(
    topic_id=1000000,
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

**topic_id:** `int` — The post id of the topic that has the poll.
    
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

<details><summary><code>client.forum.<a href="src/fern/forum/client.py">getrecruitmentthreadsummaries</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Allows the caller to get a list of to 25 recruitment thread summary information objects.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.forum.getrecruitmentthreadsummaries()

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

## 
<details><summary><code>client._.<a href="src/fern/_/client.py">getavailablelocales</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of available localization cultures
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client._.getavailablelocales()

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

<details><summary><code>client._.<a href="src/fern/_/client.py">getglobalalerts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets any active global alert for display in the forum banners, help pages, etc. Usually used for DOC alerts.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client._.getglobalalerts()

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

**includestreaming:** `typing.Optional[bool]` — Determines whether Streaming Alerts are included in results
    
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

<details><summary><code>client._.<a href="src/fern/_/client.py">getcommonsettings</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the common settings used by the Bungie.Net environment.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client._.getcommonsettings()

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

<details><summary><code>client._.<a href="src/fern/_/client.py">getusersystemoverrides</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the user-specific system overrides that should be respected alongside common systems.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client._.getusersystemoverrides()

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

## GroupV2
<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">getavailableavatars</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all available group avatars for the signed-in user.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.getavailableavatars()

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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">getavailablethemes</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all available group themes.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.getavailablethemes()

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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">getuserclaninvitesetting</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the state of the user's clan invite preferences for a particular membership type - true if they wish to be invited to clans, false otherwise.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.getuserclaninvitesetting(
    m_type=1,
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

**m_type:** `int` — The Destiny membership type of the account we wish to access settings.
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">getgroupbyname</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific group with the given name and type.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.getgroupbyname(
    group_name="groupName",
    group_type=1,
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

**group_name:** `str` — Exact name of the group to find.
    
</dd>
</dl>

<dl>
<dd>

**group_type:** `int` — Type of group to find.
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">getgroupbynamev2</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific group with the given name and type. The POST version.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.getgroupbynamev2()

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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">getrecommendedgroups</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets groups recommended for you based on the groups to whom those you follow belong.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.getrecommendedgroups(
    group_type=1,
    create_date_range=1,
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

**group_type:** `int` — Type of groups requested
    
</dd>
</dl>

<dl>
<dd>

**create_date_range:** `int` — Requested range in which to pull recommended groups
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">recovergroupforfounder</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Allows a founder to manually recover a group they can see in game but not on bungie.net
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.recovergroupforfounder(
    membership_type=1,
    membership_id=1000000,
    group_type=1,
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

**membership_type:** `int` — Membership type of the supplied membership ID.
    
</dd>
</dl>

<dl>
<dd>

**membership_id:** `int` — Membership ID to for which to find founded groups.
    
</dd>
</dl>

<dl>
<dd>

**group_type:** `int` — Type of group the supplied member founded.
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">groupsearch</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for Groups.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.groupsearch()

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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">getpotentialgroupsformember</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about the groups that a given member has applied to or been invited to.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.getpotentialgroupsformember(
    membership_type=1,
    membership_id=1000000,
    filter=1,
    group_type=1,
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

**membership_type:** `int` — Membership type of the supplied membership ID.
    
</dd>
</dl>

<dl>
<dd>

**membership_id:** `int` — Membership ID to for which to find applied groups.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `int` — Filter apply to list of potential joined groups.
    
</dd>
</dl>

<dl>
<dd>

**group_type:** `int` — Type of group the supplied member applied.
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">getgroupsformember</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about the groups that a given member has joined.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.getgroupsformember(
    membership_type=1,
    membership_id=1000000,
    filter=1,
    group_type=1,
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

**membership_type:** `int` — Membership type of the supplied membership ID.
    
</dd>
</dl>

<dl>
<dd>

**membership_id:** `int` — Membership ID to for which to find founded groups.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `int` — Filter apply to list of joined groups.
    
</dd>
</dl>

<dl>
<dd>

**group_type:** `int` — Type of group the supplied member founded.
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">getgroup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific group of the given ID.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.getgroup(
    group_id=1000000,
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

**group_id:** `int` — Requested group's id.
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">abdicatefoundership</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

An administrative method to allow the founder of a group or clan to give up their position to another admin permanently.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.abdicatefoundership(
    group_id=1000000,
    membership_type=1,
    founder_id_new=1000000,
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

**group_id:** `int` — The target group id.
    
</dd>
</dl>

<dl>
<dd>

**membership_type:** `int` — Membership type of the provided founderIdNew.
    
</dd>
</dl>

<dl>
<dd>

**founder_id_new:** `int` — The new founder for this group. Must already be a group admin.
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">getadminsandfounderofgroup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the list of members in a given group who are of admin level or higher.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.getadminsandfounderofgroup(
    group_id=1000000,
    currentpage=1,
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

**group_id:** `int` — The ID of the group.
    
</dd>
</dl>

<dl>
<dd>

**currentpage:** `int` — Page number (starting with 1). Each page has a fixed size of 50 items per page.
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">getbannedmembersofgroup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the list of banned members in a given group. Only accessible to group Admins and above. Not applicable to all groups. Check group features.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.getbannedmembersofgroup(
    group_id=1000000,
    currentpage=1,
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

**group_id:** `int` — Group ID whose banned members you are fetching
    
</dd>
</dl>

<dl>
<dd>

**currentpage:** `int` — Page number (starting with 1). Each page has a fixed size of 50 entries.
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">editgroup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Edit an existing group. You must have suitable permissions in the group to perform this operation. This latest revision will only edit the fields you pass in - pass null for properties you want to leave unaltered.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.editgroup(
    group_id=1000000,
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

**group_id:** `int` — Group ID of the group to edit.
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">editclanbanner</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Edit an existing group's clan banner. You must have suitable permissions in the group to perform this operation. All fields are required.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.editclanbanner(
    group_id=1000000,
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

**group_id:** `int` — Group ID of the group to edit.
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">editfounderoptions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Edit group options only available to a founder. You must have suitable permissions in the group to perform this operation.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.editfounderoptions(
    group_id=1000000,
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

**group_id:** `int` — Group ID of the group to edit.
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">getmembersofgroup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the list of members in a given group.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.getmembersofgroup(
    group_id=1000000,
    currentpage=1,
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

**group_id:** `int` — The ID of the group.
    
</dd>
</dl>

<dl>
<dd>

**currentpage:** `int` — Page number (starting with 1). Each page has a fixed size of 50 items per page.
    
</dd>
</dl>

<dl>
<dd>

**member_type:** `typing.Optional[int]` — Filter out other member types. Use None for all members.
    
</dd>
</dl>

<dl>
<dd>

**name_search:** `typing.Optional[str]` — The name fragment upon which a search should be executed for members with matching display or unique names.
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">approvepending</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Approve the given membershipId to join the group/clan as long as they have applied.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.approvepending(
    group_id=1000000,
    membership_type=1,
    membership_id=1000000,
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

**group_id:** `int` — ID of the group.
    
</dd>
</dl>

<dl>
<dd>

**membership_type:** `int` — Membership type of the supplied membership ID.
    
</dd>
</dl>

<dl>
<dd>

**membership_id:** `int` — The membership id being approved.
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">approveallpending</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Approve all of the pending users for the given group.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.approveallpending(
    group_id=1000000,
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

**group_id:** `int` — ID of the group.
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">approvependingforlist</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Approve all of the pending users for the given group.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.approvependingforlist(
    group_id=1000000,
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

**group_id:** `int` — ID of the group.
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">denyallpending</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deny all of the pending users for the given group.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.denyallpending(
    group_id=1000000,
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

**group_id:** `int` — ID of the group.
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">denypendingforlist</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deny all of the pending users for the given group that match the passed-in .
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.denypendingforlist(
    group_id=1000000,
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

**group_id:** `int` — ID of the group.
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">individualgroupinvite</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Invite a user to join this group.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.individualgroupinvite(
    group_id=1000000,
    membership_type=1,
    membership_id=1000000,
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

**group_id:** `int` — ID of the group you would like to join.
    
</dd>
</dl>

<dl>
<dd>

**membership_type:** `int` — MembershipType of the account being invited.
    
</dd>
</dl>

<dl>
<dd>

**membership_id:** `int` — Membership id of the account being invited.
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">individualgroupinvitecancel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels a pending invitation to join a group.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.individualgroupinvitecancel(
    group_id=1000000,
    membership_type=1,
    membership_id=1000000,
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

**group_id:** `int` — ID of the group you would like to join.
    
</dd>
</dl>

<dl>
<dd>

**membership_type:** `int` — MembershipType of the account being cancelled.
    
</dd>
</dl>

<dl>
<dd>

**membership_id:** `int` — Membership id of the account being cancelled.
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">getinvitedindividuals</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the list of users who have been invited into the group.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.getinvitedindividuals(
    group_id=1000000,
    currentpage=1,
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

**group_id:** `int` — ID of the group.
    
</dd>
</dl>

<dl>
<dd>

**currentpage:** `int` — Page number (starting with 1). Each page has a fixed size of 50 items per page.
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">getpendingmemberships</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the list of users who are awaiting a decision on their application to join a given group. Modified to include application info.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.getpendingmemberships(
    group_id=1000000,
    currentpage=1,
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

**group_id:** `int` — ID of the group.
    
</dd>
</dl>

<dl>
<dd>

**currentpage:** `int` — Page number (starting with 1). Each page has a fixed size of 50 items per page.
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">banmember</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bans the requested member from the requested group for the specified period of time.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.banmember(
    group_id=1000000,
    membership_type=1,
    membership_id=1000000,
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

**group_id:** `int` — Group ID that has the member to ban.
    
</dd>
</dl>

<dl>
<dd>

**membership_type:** `int` — Membership type of the provided membership ID.
    
</dd>
</dl>

<dl>
<dd>

**membership_id:** `int` — Membership ID of the member to ban from the group.
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">kickmember</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Kick a member from the given group, forcing them to reapply if they wish to re-join the group. You must have suitable permissions in the group to perform this operation.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.kickmember(
    group_id=1000000,
    membership_type=1,
    membership_id=1000000,
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

**group_id:** `int` — Group ID to kick the user from.
    
</dd>
</dl>

<dl>
<dd>

**membership_type:** `int` — Membership type of the provided membership ID.
    
</dd>
</dl>

<dl>
<dd>

**membership_id:** `int` — Membership ID to kick.
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">editgroupmembership</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Edit the membership type of a given member. You must have suitable permissions in the group to perform this operation.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.editgroupmembership(
    group_id=1000000,
    membership_type=1,
    membership_id=1000000,
    member_type=1,
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

**group_id:** `int` — ID of the group to which the member belongs.
    
</dd>
</dl>

<dl>
<dd>

**membership_type:** `int` — Membership type of the provide membership ID.
    
</dd>
</dl>

<dl>
<dd>

**membership_id:** `int` — Membership ID to modify.
    
</dd>
</dl>

<dl>
<dd>

**member_type:** `int` — New membertype for the specified member.
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">unbanmember</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unbans the requested member, allowing them to re-apply for membership.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.unbanmember(
    group_id=1000000,
    membership_type=1,
    membership_id=1000000,
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

**group_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**membership_type:** `int` — Membership type of the provided membership ID.
    
</dd>
</dl>

<dl>
<dd>

**membership_id:** `int` — Membership ID of the member to unban from the group
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">getgroupoptionalconversations</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of available optional conversation channels and their settings.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.getgroupoptionalconversations(
    group_id=1000000,
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

**group_id:** `int` — Requested group's id.
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">addoptionalconversation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new optional conversation/chat channel. Requires admin permissions to the group.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.addoptionalconversation(
    group_id=1000000,
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

**group_id:** `int` — Group ID of the group to edit.
    
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

<details><summary><code>client.groupv2.<a href="src/fern/groupv2/client.py">editoptionalconversation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Edit the settings of an optional conversation/chat channel. Requires admin permissions to the group.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.groupv2.editoptionalconversation(
    group_id=1000000,
    conversation_id=1000000,
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

**group_id:** `int` — Group ID of the group to edit.
    
</dd>
</dl>

<dl>
<dd>

**conversation_id:** `int` — Conversation Id of the channel being edited.
    
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

## Social
<details><summary><code>client.social.<a href="src/fern/social/client.py">getfriendlist</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns your Bungie Friend list
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.social.getfriendlist()

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

<details><summary><code>client.social.<a href="src/fern/social/client.py">issuefriendrequest</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requests a friend relationship with the target user. Any of the target user's linked membership ids are valid inputs.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.social.issuefriendrequest(
    membership_id="membershipId",
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

**membership_id:** `str` — The membership id of the user you wish to add.
    
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

<details><summary><code>client.social.<a href="src/fern/social/client.py">removefriend</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a friend relationship with the target user. The user must be on your friend list, though no error will occur if they are not.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.social.removefriend(
    membership_id="membershipId",
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

**membership_id:** `str` — The membership id of the user you wish to remove.
    
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

<details><summary><code>client.social.<a href="src/fern/social/client.py">getfriendrequestlist</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns your friend request queue.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.social.getfriendrequestlist()

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

<details><summary><code>client.social.<a href="src/fern/social/client.py">acceptfriendrequest</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Accepts a friend relationship with the target user. The user must be on your incoming friend request list, though no error will occur if they are not.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.social.acceptfriendrequest(
    membership_id="membershipId",
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

**membership_id:** `str` — The membership id of the user you wish to accept.
    
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

<details><summary><code>client.social.<a href="src/fern/social/client.py">declinefriendrequest</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Declines a friend relationship with the target user. The user must be on your incoming friend request list, though no error will occur if they are not.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.social.declinefriendrequest(
    membership_id="membershipId",
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

**membership_id:** `str` — The membership id of the user you wish to decline.
    
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

<details><summary><code>client.social.<a href="src/fern/social/client.py">removefriendrequest</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a friend relationship with the target user. The user must be on your outgoing request friend list, though no error will occur if they are not.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.social.removefriendrequest(
    membership_id="membershipId",
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

**membership_id:** `str` — The membership id of the user you wish to remove.
    
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

<details><summary><code>client.social.<a href="src/fern/social/client.py">getplatformfriendlist</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the platform friend of the requested type, with additional information if they have Bungie accounts. Must have a recent login session with said platform.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.social.getplatformfriendlist(
    friend_platform=1,
    page="page",
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

**friend_platform:** `int` — The platform friend type.
    
</dd>
</dl>

<dl>
<dd>

**page:** `str` — The zero based page to return. Page size is 100.
    
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

## Tokens
<details><summary><code>client.tokens.<a href="src/fern/tokens/client.py">applymissingpartnerofferswithoutclaim</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Apply a partner offer to the targeted user. This endpoint does not claim a new offer, but any already claimed offers will be applied to the game if not already.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.tokens.applymissingpartnerofferswithoutclaim(
    partner_application_id=1,
    target_bnet_membership_id=1000000,
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

**partner_application_id:** `int` — The partner application identifier.
    
</dd>
</dl>

<dl>
<dd>

**target_bnet_membership_id:** `int` — The bungie.net user to apply missing offers to. If not self, elevated permissions are required.
    
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

<details><summary><code>client.tokens.<a href="src/fern/tokens/client.py">claimpartneroffer</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Claim a partner offer as the authenticated user.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.tokens.claimpartneroffer()

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

<details><summary><code>client.tokens.<a href="src/fern/tokens/client.py">forcedropsrepair</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Twitch Drops self-repair function - scans twitch for drops not marked as fulfilled and resyncs them.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.tokens.forcedropsrepair()

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

<details><summary><code>client.tokens.<a href="src/fern/tokens/client.py">getpartnerofferskuhistory</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the partner sku and offer history of the targeted user. Elevated permissions are required to see users that are not yourself.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.tokens.getpartnerofferskuhistory(
    partner_application_id=1,
    target_bnet_membership_id=1000000,
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

**partner_application_id:** `int` — The partner application identifier.
    
</dd>
</dl>

<dl>
<dd>

**target_bnet_membership_id:** `int` — The bungie.net user to apply missing offers to. If not self, elevated permissions are required.
    
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

<details><summary><code>client.tokens.<a href="src/fern/tokens/client.py">getpartnerrewardhistory</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the partner rewards history of the targeted user, both partner offers and Twitch drops.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.tokens.getpartnerrewardhistory(
    target_bnet_membership_id=1000000,
    partner_application_id=1,
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

**target_bnet_membership_id:** `int` — The bungie.net user to return reward history for.
    
</dd>
</dl>

<dl>
<dd>

**partner_application_id:** `int` — The partner application identifier.
    
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

<details><summary><code>client.tokens.<a href="src/fern/tokens/client.py">getbungierewardslist</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of the current bungie rewards
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.tokens.getbungierewardslist()

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

<details><summary><code>client.tokens.<a href="src/fern/tokens/client.py">getbungierewardsforplatformuser</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the bungie rewards for the targeted user when a platform membership Id and Type are used.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.tokens.getbungierewardsforplatformuser(
    membership_id=1000000,
    membership_type=1,
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

**membership_id:** `int` — users platform membershipId for requested user rewards. If not self, elevated permissions are required.
    
</dd>
</dl>

<dl>
<dd>

**membership_type:** `int` — The target Destiny 2 membership type.
    
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

<details><summary><code>client.tokens.<a href="src/fern/tokens/client.py">getbungierewardsforuser</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the bungie rewards for the targeted user.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.tokens.getbungierewardsforuser(
    membership_id=1000000,
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

**membership_id:** `int` — bungie.net user membershipId for requested user rewards. If not self, elevated permissions are required.
    
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

## Trending
<details><summary><code>client.trending.<a href="src/fern/trending/client.py">gettrendingcategories</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns trending items for Bungie.net, collapsed into the first page of items per category. For pagination within a category, call GetTrendingCategory.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.trending.gettrendingcategories()

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

<details><summary><code>client.trending.<a href="src/fern/trending/client.py">gettrendingcategory</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns paginated lists of trending items for a category.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.trending.gettrendingcategory(
    category_id="categoryId",
    page_number=1,
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

**category_id:** `str` — The ID of the category for whom you want additional results.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `int` — The page # of results to return.
    
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

<details><summary><code>client.trending.<a href="src/fern/trending/client.py">gettrendingentrydetail</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the detailed results for a specific trending entry. Note that trending entries are uniquely identified by a combination of *both* the TrendingEntryType *and* the identifier: the identifier alone is not guaranteed to be globally unique.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.trending.gettrendingentrydetail(
    trending_entry_type=1,
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

**trending_entry_type:** `int` — The type of entity to be returned.
    
</dd>
</dl>

<dl>
<dd>

**identifier:** `str` — The identifier for the entity to be returned.
    
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

## User
<details><summary><code>client.user.<a href="src/fern/user/client.py">getavailablethemes</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all available user themes.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.user.getavailablethemes()

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

<details><summary><code>client.user.<a href="src/fern/user/client.py">getbungienetuserbyid</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Loads a bungienet user by membership id.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.user.getbungienetuserbyid(
    id=1000000,
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

**id:** `int` — The requested Bungie.net membership id.
    
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

<details><summary><code>client.user.<a href="src/fern/user/client.py">getcredentialtypesfortargetaccount</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of credential types attached to the requested account
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.user.getcredentialtypesfortargetaccount(
    membership_id=1000000,
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

**membership_id:** `int` — The user's membership id
    
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

<details><summary><code>client.user.<a href="src/fern/user/client.py">getmembershipfromhardlinkedcredential</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets any hard linked membership given a credential. Only works for credentials that are public (just SteamID64 right now). Cross Save aware.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.user.getmembershipfromhardlinkedcredential(
    cr_type=1,
    credential="credential",
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

**cr_type:** `int` — The credential type. 'SteamId' is the only valid value at present.
    
</dd>
</dl>

<dl>
<dd>

**credential:** `str` — The credential to look up. Must be a valid SteamID64.
    
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

<details><summary><code>client.user.<a href="src/fern/user/client.py">getmembershipdatabyid</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of accounts associated with the supplied membership ID and membership type. This will include all linked accounts (even when hidden) if supplied credentials permit it.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.user.getmembershipdatabyid(
    membership_id=1000000,
    membership_type=1,
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

**membership_id:** `int` — The membership ID of the target user.
    
</dd>
</dl>

<dl>
<dd>

**membership_type:** `int` — Type of the supplied membership ID.
    
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

<details><summary><code>client.user.<a href="src/fern/user/client.py">getmembershipdataforcurrentuser</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of accounts associated with signed in user. This is useful for OAuth implementations that do not give you access to the token response.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.user.getmembershipdataforcurrentuser()

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

<details><summary><code>client.user.<a href="src/fern/user/client.py">getsanitizedplatformdisplaynames</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of all display names linked to this membership id but sanitized (profanity filtered). Obeys all visibility rules of calling user and is heavily cached.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.user.getsanitizedplatformdisplaynames(
    membership_id=1000000,
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

**membership_id:** `int` — The requested membership id to load.
    
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

<details><summary><code>client.user.<a href="src/fern/user/client.py">searchbyglobalnamepost</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Given the prefix of a global display name, returns all users who share that name.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.user.searchbyglobalnamepost(
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

**page:** `int` — The zero-based page of results you desire.
    
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

<details><summary><code>client.user.<a href="src/fern/user/client.py">searchbyglobalnameprefix</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[OBSOLETE] Do not use this to search users, use SearchByGlobalNamePost instead.
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

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.user.searchbyglobalnameprefix(
    display_name_prefix="displayNamePrefix",
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

**display_name_prefix:** `str` — The display name prefix you're looking for.
    
</dd>
</dl>

<dl>
<dd>

**page:** `int` — The zero-based page of results you desire.
    
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

