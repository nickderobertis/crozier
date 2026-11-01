# Reference
## Info
<details><summary><code>client.info.<a href="src/fern/info/client.py">artifact_formats</a>() -> ArtifactFormats</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the available artifact formats
</dd>
</dl>
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

client.info.artifact_formats()

```
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

<details><summary><code>client.info.<a href="src/fern/info/client.py">recent_changes</a>() -> typing.List[ChangeLogItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Contribly change log.
</dd>
</dl>
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

client.info.recent_changes()

```
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

<details><summary><code>client.info.<a href="src/fern/info/client.py">event_types</a>() -> typing.List[EventType]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List available notification event types
</dd>
</dl>
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

client.info.event_types()

```
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

## Assignment
<details><summary><code>client.assignment.<a href="src/fern/assignment/client.py">list_assignments</a>(...) -> typing.List[Assignment]</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assignment.list_assignments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**owned_by:** `typing.Optional[str]` — Restrict results to assignments owned by this user.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Pagination page
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Pagination page size
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Restrict results to assignments whose name or description matches this keyword.
    
</dd>
</dl>

<dl>
<dd>

**url_words:** `typing.Optional[str]` — Select an assignment by urlWords.
    
</dd>
</dl>

<dl>
<dd>

**open:** `typing.Optional[bool]` — Select open or closed assignments
    
</dd>
</dl>

<dl>
<dd>

**always_open:** `typing.Optional[bool]` — Select assignments with no closing date.
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[str]` — Restrict results to assignments which are tagged with this tag.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Restrict results to the assignment (or potentially assignments) with this exact name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assignment.<a href="src/fern/assignment/client.py">create_a_new_assignment</a>(...) -> Assignment</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assignment.create_a_new_assignment(
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

**allows_anonymous_contributions:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**cover:** `typing.Optional[MediaUsage]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**embargo:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**ends:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**featured:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**media_required:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**moderator:** `typing.Optional[str]` — Optional credential id of the login which will moderator this assignment.
    
</dd>
</dl>

<dl>
<dd>

**receipt_message:** `typing.Optional[str]` — An optional assignment specific message to be displayed on successful contribution submission. For example, this might be used to inform contributors of assignment specific moderation time frames.
    
</dd>
</dl>

<dl>
<dd>

**starts:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[Tag]]` 
    
</dd>
</dl>

<dl>
<dd>

**url_words:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assignment.<a href="src/fern/assignment/client.py">get_a_single_assigment_by_id</a>(...) -> Assignment</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assignment.get_a_single_assigment_by_id(
    id="id",
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

**id:** `str` — Id of the assignment to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assignment.<a href="src/fern/assignment/client.py">delete_this_assignment_and_all_of_its_contributions</a>(...)</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assignment.delete_this_assignment_and_all_of_its_contributions(
    id="id",
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

**id:** `str` — Id of the assignment to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Contribution
<details><summary><code>client.contribution.<a href="src/fern/contribution/client.py">list_valid_contribution_refinement_types</a>() -> typing.List[str]</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.contribution.list_valid_contribution_refinement_types()

```
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

<details><summary><code>client.contribution.<a href="src/fern/contribution/client.py">list_contribution_refinement_options</a>(...) -> typing.Dict[str, typing.List[str]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Given a contribution list query determine the available filter options. Can be used to generate the UI to refinement a filter.
</dd>
</dl>
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

client.contribution.list_contribution_refinement_options()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assignment:** `typing.Optional[str]` — Restrict results to contributions submitted to this assignment.
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — Limit results to contributions created before this date time.
    
</dd>
</dl>

<dl>
<dd>

**created_after:** `typing.Optional[datetime.datetime]` — Limit results to contributions created after this date time.
    
</dd>
</dl>

<dl>
<dd>

**geohash:** `typing.Optional[str]` — Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)
    
</dd>
</dl>

<dl>
<dd>

**has_location:** `typing.Optional[bool]` — Restrict results to contributions which have a publicly visible location.
    
</dd>
</dl>

<dl>
<dd>

**lat_long:** `typing.Optional[str]` — Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius
    
</dd>
</dl>

<dl>
<dd>

**radius:** `typing.Optional[float]` — When limiting result by location with the latLong parameter, specify the radius in kilometers.
    
</dd>
</dl>

<dl>
<dd>

**media_type:** `typing.Optional[str]` — Restrict results to contributions which include a media file of the given type (ie. image / video)
    
</dd>
</dl>

<dl>
<dd>

**owned_by:** `typing.Optional[str]` — Restrict results to contributions which are fall under the jurisdiction by this user.
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Restrict results to contributions whose headline text matches this keyword.
    
</dd>
</dl>

<dl>
<dd>

**url_words:** `typing.Optional[str]` — Locate a specific contribution by URL words
    
</dd>
</dl>

<dl>
<dd>

**user:** `typing.Optional[str]` — Restrict results to contributions by this user identified by id.
    
</dd>
</dl>

<dl>
<dd>

**refinements:** `typing.Optional[str]` — Comma seperated list of refinement names.
    
</dd>
</dl>

<dl>
<dd>

**refinement_size:** `typing.Optional[float]` — Number of refinement options to return.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contribution.<a href="src/fern/contribution/client.py">list_contributions</a>(...) -> typing.List[Contribution]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve contributions.
</dd>
</dl>
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

client.contribution.list_contributions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assignment:** `typing.Optional[str]` — Restrict results to contributions submitted to this assignment.
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — Limit results to contributions created before this date time.
    
</dd>
</dl>

<dl>
<dd>

**created_after:** `typing.Optional[datetime.datetime]` — Limit results to contributions created after this date time.
    
</dd>
</dl>

<dl>
<dd>

**created_day:** `typing.Optional[datetime.date]` — Limit results to contributions created on this day.
    
</dd>
</dl>

<dl>
<dd>

**created_month:** `typing.Optional[str]` — Limit results to contributions created during this month.
    
</dd>
</dl>

<dl>
<dd>

**geohash:** `typing.Optional[str]` — Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)
    
</dd>
</dl>

<dl>
<dd>

**has_location:** `typing.Optional[bool]` — Restrict results to contributions which have a publicly visible location.
    
</dd>
</dl>

<dl>
<dd>

**lat_long:** `typing.Optional[str]` — Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius
    
</dd>
</dl>

<dl>
<dd>

**radius:** `typing.Optional[float]` — When limiting result by location with the latLong parameter, specify the radius in kilometers.
    
</dd>
</dl>

<dl>
<dd>

**media_type:** `typing.Optional[str]` — Restrict results to contributions which include a media file of the given type (ie. image / video)
    
</dd>
</dl>

<dl>
<dd>

**owned_by:** `typing.Optional[str]` — Restrict results to contributions which are fall under the jurisdiction by this user.
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Restrict results to contributions whose headline text matches this keyword.
    
</dd>
</dl>

<dl>
<dd>

**url_words:** `typing.Optional[str]` — Locate a specific contribution by URL words
    
</dd>
</dl>

<dl>
<dd>

**user:** `typing.Optional[str]` — Restrict results to contributions by this user identified by id.
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[str]` — Restrict results to a list of specific contributions identified by a comma seperated list of ids.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` — Select output format. 'json' or 'rss'. Defaults to JSON.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contribution.<a href="src/fern/contribution/client.py">create_a_new_contribution</a>(...) -> Contribution</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.contribution.create_a_new_contribution()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `Contribution` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contribution.<a href="src/fern/contribution/client.py">get_a_single_contribution_by_id</a>(...) -> Contribution</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.contribution.get_a_single_contribution_by_id(
    id="id",
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

**id:** `str` — Id of the contribution to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contribution.<a href="src/fern/contribution/client.py">delete_this_contribution</a>(...) -> Contribution</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.contribution.delete_this_contribution(
    id="id",
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

**id:** `str` — Id of the contribution to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contribution.<a href="src/fern/contribution/client.py">raise_a_flag_against_this_contribution</a>(...) -> Flag</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Allows end users to bring potential issues with publicly visible content to the attention of moderators.
</dd>
</dl>
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

client.contribution.raise_a_flag_against_this_contribution(
    id_="id",
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

**id:** `str` — Id of the contribution to flag
    
</dd>
</dl>

<dl>
<dd>

**request:** `Flag` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contribution.<a href="src/fern/contribution/client.py">allows_a_user_to_mark_a_contribution_as_liked</a>(...) -> float</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.contribution.allows_a_user_to_mark_a_contribution_as_liked(
    id="id",
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

**id:** `str` — Id of the contribution
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contribution.<a href="src/fern/contribution/client.py">list_users_who_have_liked_this_contributions</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of user ids of users who have liked this conribution
</dd>
</dl>
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

client.contribution.list_users_who_have_liked_this_contributions(
    id="id",
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

**id:** `str` — Id of the contribution
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contribution.<a href="src/fern/contribution/client.py">perform_a_moderation_action_on_this_contribution</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Allows the contribution to approved of rejected.
</dd>
</dl>
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

client.contribution.perform_a_moderation_action_on_this_contribution(
    id="id",
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

**id:** `str` — Id of the contribution to moderate
    
</dd>
</dl>

<dl>
<dd>

**action:** `typing.Optional[ModerationAction]` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contribution.<a href="src/fern/contribution/client.py">export_contributions</a>(...) -> Export</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Begin an export job. Returns a export job which can be polled to follow the progress of an export.
</dd>
</dl>
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

client.contribution.export_contributions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assignment:** `typing.Optional[str]` — Restrict results to contributions submitted to this assignment.
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — Limit results to contributions created before this date time.
    
</dd>
</dl>

<dl>
<dd>

**created_after:** `typing.Optional[datetime.datetime]` — Limit results to contributions created after this date time.
    
</dd>
</dl>

<dl>
<dd>

**geohash:** `typing.Optional[str]` — Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)
    
</dd>
</dl>

<dl>
<dd>

**has_location:** `typing.Optional[bool]` — Restrict results to contributions which have a publicly visible location.
    
</dd>
</dl>

<dl>
<dd>

**lat_long:** `typing.Optional[str]` — Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius
    
</dd>
</dl>

<dl>
<dd>

**radius:** `typing.Optional[float]` — When limiting result by location with the latLong parameter, specify the radius in kilometers.
    
</dd>
</dl>

<dl>
<dd>

**media_type:** `typing.Optional[str]` — Restrict results to contributions which include a media file of the given type (ie. image / video)
    
</dd>
</dl>

<dl>
<dd>

**owned_by:** `typing.Optional[str]` — Restrict results to contributions which are fall under the jurisdiction by this user.
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Restrict results to contributions whose headline text matches this keyword.
    
</dd>
</dl>

<dl>
<dd>

**url_words:** `typing.Optional[str]` — Locate a specific contribution by URL words
    
</dd>
</dl>

<dl>
<dd>

**user:** `typing.Optional[str]` — Restrict results to contributions by this user identified by id.
    
</dd>
</dl>

<dl>
<dd>

**tagged:** `typing.Optional[bool]` — Should exported media files be tagged with metadata. Deprecated; use format instead.
    
</dd>
</dl>

<dl>
<dd>

**combined:** `typing.Optional[bool]` — Included a combined file with all contribution text.
    
</dd>
</dl>

<dl>
<dd>

**individual:** `typing.Optional[bool]` — Include individual text files for each contribution.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` — Media format to export; none, fullsize, tagged or original.
    
</dd>
</dl>

<dl>
<dd>

**json:** `typing.Optional[bool]` — Include raw JSON for each contribution.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contribution.<a href="src/fern/contribution/client.py">export_contributions_preflight_summary</a>(...) -> ExportSummary</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provide a preflight summary of an export request.
</dd>
</dl>
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

client.contribution.export_contributions_preflight_summary()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assignment:** `typing.Optional[str]` — Restrict results to contributions submitted to this assignment.
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — Limit results to contributions created before this date time.
    
</dd>
</dl>

<dl>
<dd>

**created_after:** `typing.Optional[datetime.datetime]` — Limit results to contributions created after this date time.
    
</dd>
</dl>

<dl>
<dd>

**geohash:** `typing.Optional[str]` — Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)
    
</dd>
</dl>

<dl>
<dd>

**has_location:** `typing.Optional[bool]` — Restrict results to contributions which have a publicly visible location.
    
</dd>
</dl>

<dl>
<dd>

**lat_long:** `typing.Optional[str]` — Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius
    
</dd>
</dl>

<dl>
<dd>

**radius:** `typing.Optional[float]` — When limiting result by location with the latLong parameter, specify the radius in kilometers.
    
</dd>
</dl>

<dl>
<dd>

**media_type:** `typing.Optional[str]` — Restrict results to contributions which include a media file of the given type (ie. image / video)
    
</dd>
</dl>

<dl>
<dd>

**owned_by:** `typing.Optional[str]` — Restrict results to contributions which are fall under the jurisdiction by this user.
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Restrict results to contributions whose headline text matches this keyword.
    
</dd>
</dl>

<dl>
<dd>

**url_words:** `typing.Optional[str]` — Locate a specific contribution by URL words
    
</dd>
</dl>

<dl>
<dd>

**user:** `typing.Optional[str]` — Restrict results to contributions by this user identified by id.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contribution.<a href="src/fern/contribution/client.py">get_a_single_export_job_poll_to_follow_export_progress</a>(...) -> Export</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.contribution.get_a_single_export_job_poll_to_follow_export_progress(
    id="id",
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

**id:** `str` — Id of the export job to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Auth
<details><summary><code>client.auth.<a href="src/fern/auth/client.py">list_the_credentials_associated_with_the_authenticated_user</a>() -> typing.List[Credential]</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.auth.list_the_credentials_associated_with_the_authenticated_user()

```
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

<details><summary><code>client.auth.<a href="src/fern/auth/client.py">scopes</a>() -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List available token scopes
</dd>
</dl>
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

client.auth.scopes()

```
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

<details><summary><code>client.auth.<a href="src/fern/auth/client.py">verify_token_and_return_details_of_the_owning_user</a>() -> Authority</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.auth.verify_token_and_return_details_of_the_owning_user()

```
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

## Form
<details><summary><code>client.form.<a href="src/fern/form/client.py">list_form_responses</a>(...) -> typing.List[FormResponse]</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.form.list_form_responses()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user:** `typing.Optional[str]` — Restrict results to responses submitted by this user.
    
</dd>
</dl>

<dl>
<dd>

**form:** `typing.Optional[str]` — Restrict results to responses submitted to this form.
    
</dd>
</dl>

<dl>
<dd>

**contribution:** `typing.Optional[str]` — Restrict results to responses relating to this contribution.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.form.<a href="src/fern/form/client.py">submit_a_response_to_a_form</a>(...) -> FormResponse</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.form.submit_a_response_to_a_form()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contribution:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**form:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**responses:** `typing.Optional[typing.Dict[str, str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.form.<a href="src/fern/form/client.py">get_a_single_form_response_by_id</a>(...) -> FormResponse</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.form.get_a_single_form_response_by_id(
    id="id",
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

**id:** `str` — Id of the assignment to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.form.<a href="src/fern/form/client.py">list_forms</a>(...) -> typing.List[Form]</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.form.list_forms(
    owned_by="ownedBy",
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

**owned_by:** `str` — Restrict results to forms owned by this user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.form.<a href="src/fern/form/client.py">create_a_form</a>(...) -> Form</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.form.create_a_form()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**call_to_action:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**css_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.List[FormField]]` 
    
</dd>
</dl>

<dl>
<dd>

**heading:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**no_css:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[Tag]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.form.<a href="src/fern/form/client.py">get_a_single_form_by_id</a>(...) -> Form</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.form.get_a_single_form_by_id(
    id="id",
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

**id:** `str` — Id of the form to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.form.<a href="src/fern/form/client.py">delete_this_form_and_all_of_its_responses</a>(...)</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.form.delete_this_form_and_all_of_its_responses(
    id="id",
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

**id:** `str` — Id of the form to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Media
<details><summary><code>client.media.<a href="src/fern/media/client.py">submit_a_new_media_file</a>(...) -> Media</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.media.submit_a_new_media_file(
    request="string",
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

**request:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Notifications
<details><summary><code>client.notifications.<a href="src/fern/notifications/client.py">get_notifications_contributions_id_preview</a>(...) -> NotificationPreview</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.notifications.get_notifications_contributions_id_preview(
    id="id",
    message="message",
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

**id:** `str` — Id of the contribution to preview a notification for
    
</dd>
</dl>

<dl>
<dd>

**message:** `str` — Type of message to preview.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Subscriptions
<details><summary><code>client.subscriptions.<a href="src/fern/subscriptions/client.py">subscription_types</a>() -> typing.List[SubscriptionType]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List available subscription types
</dd>
</dl>
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

client.subscriptions.subscription_types()

```
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

<details><summary><code>client.subscriptions.<a href="src/fern/subscriptions/client.py">list_subscriptions_for_the_authorised_user</a>() -> typing.List[Subscription]</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.subscriptions.list_subscriptions_for_the_authorised_user()

```
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

<details><summary><code>client.subscriptions.<a href="src/fern/subscriptions/client.py">delete_a_subscription</a>(...)</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.subscriptions.delete_a_subscription(
    id="id",
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

**id:** `str` — Id of the subscription to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tag
<details><summary><code>client.tag.<a href="src/fern/tag/client.py">list_tags</a>(...) -> typing.List[Tag]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve tags.
</dd>
</dl>
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

client.tag.list_tags()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**owned_by:** `typing.Optional[str]` — Restrict results to those owned by this user.
    
</dd>
</dl>

<dl>
<dd>

**tag_set:** `typing.Optional[str]` — Restrict results to tags belonging to this tag set.
    
</dd>
</dl>

<dl>
<dd>

**url_words:** `typing.Optional[str]` — Restrict results by urlWords. Should be used with ownedBy when searching for one of your own tags.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tag.<a href="src/fern/tag/client.py">create_a_new_tag</a>(...) -> Tag</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tag.create_a_new_tag(
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

**colour:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**tag_set:** `typing.Optional[TagSet]` 
    
</dd>
</dl>

<dl>
<dd>

**url_words:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tag.<a href="src/fern/tag/client.py">retrieve_a_single_tag_by_id</a>(...) -> Tag</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tag.retrieve_a_single_tag_by_id(
    id="id",
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

**id:** `str` — Id of the tag to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tag.<a href="src/fern/tag/client.py">list_tag_sets</a>(...) -> typing.List[TagSet]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve tag sets.
</dd>
</dl>
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

client.tag.list_tag_sets()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**owned_by:** `typing.Optional[str]` — Restrict results to those owned by this user.
    
</dd>
</dl>

<dl>
<dd>

**url_words:** `typing.Optional[str]` — Restrict results by urlWords. Should be used with ownedBy when searching for one of your own tag sets.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tag.<a href="src/fern/tag/client.py">create_a_new_tag_set</a>(...) -> TagSet</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tag.create_a_new_tag_set(
    name="name",
    url_words="urlWords",
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

**url_words:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tag.<a href="src/fern/tag/client.py">retrieve_a_single_tag_set_by_id</a>(...) -> TagSet</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tag.retrieve_a_single_tag_set_by_id(
    id="id",
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

**id:** `str` — Id of the tag set to return
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.user.<a href="src/fern/user/client.py">list_users</a>(...) -> typing.List[User]</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user.list_users()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assignment:** `typing.Optional[str]` — Restrict results to the users who have contributed to this assignment.
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — Restrict results to the users who have submitted a contribution with a public location located within this country.
    
</dd>
</dl>

<dl>
<dd>

**minimum_contributions:** `typing.Optional[float]` — Restrict results to the users who have submitted at least this many contributions.
    
</dd>
</dl>

<dl>
<dd>

**linked_profile:** `typing.Optional[str]` — Restrict results to the users who a linked profile of this type.
    
</dd>
</dl>

<dl>
<dd>

**owned_by:** `typing.Optional[str]` — Restrict results to the users who are owned by of this owner.
    
</dd>
</dl>

<dl>
<dd>

**submitted_before:** `typing.Optional[datetime.datetime]` — Limit results to users who have submitted at least one contribution before this date time.
    
</dd>
</dl>

<dl>
<dd>

**submitted_after:** `typing.Optional[datetime.datetime]` — Limit results to users who have submitted at least one contribution after this date time.
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` — Restrict results to the user with this username.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/fern/user/client.py">retrieve_a_single_user_by_id</a>(...) -> User</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user.retrieve_a_single_user_by_id(
    id="id",
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

**id:** `str` — Id of the user to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/fern/user/client.py">retrieve_a_users_linked_profile_by_type</a>(...) -> LinkedProfile</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user.retrieve_a_users_linked_profile_by_type(
    id="id",
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

**id:** `str` — Id of the user to return
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — Type of the linked profile to fetch
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

