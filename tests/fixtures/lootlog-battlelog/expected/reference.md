# Reference
## Health
<details><summary><code>client.health.<a href="src/fern/health/client.py">healthz_controller_health_check</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check the health status of the API
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.health.healthz_controller_health_check()

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

## Battles
<details><summary><code>client.battles.<a href="src/fern/battles/client.py">battles_controller_create_battle</a>(...) -> BattleCreatedResponseDtoOutput</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.battles import CreateBattleDtoEventsItem, CreateBattleDtoEventsItemF

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.battles.battles_controller_create_battle(
    account_id="accountId",
    character_id="characterId",
    world="world",
    events=[
        CreateBattleDtoEventsItem(
            f=CreateBattleDtoEventsItemF(),
        )
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

**account_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**character_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**world:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**events:** `typing.List[CreateBattleDtoEventsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**submission_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**matchmaking:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.battles.<a href="src/fern/battles/client.py">battles_controller_get_dashboard_battles</a>(...) -> BattlesListResponseDtoOutput</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.battles.battles_controller_get_dashboard_battles()

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

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[BattlesControllerGetDashboardBattlesRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**include_total:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**world:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Union[BattlesControllerGetDashboardBattlesRequestTypeItem, typing.Sequence[BattlesControllerGetDashboardBattlesRequestTypeItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**public:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**character_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**result:** `typing.Optional[typing.Union[BattlesControllerGetDashboardBattlesRequestResultItem, typing.Sequence[BattlesControllerGetDashboardBattlesRequestResultItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**ph:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**matchmaking:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**min_level:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_level:** `typing.Optional[float]` 
    
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

<details><summary><code>client.battles.<a href="src/fern/battles/client.py">battles_controller_get_user_characters</a>() -> BattleCharactersResponseDtoOutput</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.battles.battles_controller_get_user_characters()

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

<details><summary><code>client.battles.<a href="src/fern/battles/client.py">battles_controller_get_battle_analytics</a>(...) -> BattleAnalyticsResponseDtoOutput</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.battles.battles_controller_get_battle_analytics()

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

**character_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**world:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[BattlesControllerGetBattleAnalyticsRequestPeriod]` 
    
</dd>
</dl>

<dl>
<dd>

**min_level:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_level:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**ph:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**matchmaking:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.battles.<a href="src/fern/battles/client.py">battles_controller_get_abyss_seasons</a>(...) -> typing.List[AbyssSeasonResponseDtoOutput]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.battles.battles_controller_get_abyss_seasons(
    character_id="characterId",
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

**character_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**world:** `typing.Optional[str]` 
    
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

<details><summary><code>client.battles.<a href="src/fern/battles/client.py">battles_controller_get_combat_profile</a>(...) -> CombatProfileResponseDtoOutput</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.battles.battles_controller_get_combat_profile()

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

**character_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**world:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[BattlesControllerGetCombatProfileRequestPeriod]` 
    
</dd>
</dl>

<dl>
<dd>

**min_level:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_level:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[BattlesControllerGetCombatProfileRequestSortBy]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[BattlesControllerGetCombatProfileRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**include_total:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**min_battles:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**ph:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**matchmaking:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.battles.<a href="src/fern/battles/client.py">battles_controller_get_profession_win_rate</a>(...) -> typing.List[ProfessionWinRateResponseDtoOutput]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.battles.battles_controller_get_profession_win_rate()

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

**character_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**world:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[BattlesControllerGetProfessionWinRateRequestPeriod]` 
    
</dd>
</dl>

<dl>
<dd>

**min_level:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_level:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[BattlesControllerGetProfessionWinRateRequestSortBy]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[BattlesControllerGetProfessionWinRateRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**include_total:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**min_battles:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**ph:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**matchmaking:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.battles.<a href="src/fern/battles/client.py">battles_controller_get_head_to_head</a>(...) -> HeadToHeadPaginatedResponseDtoOutput</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.battles.battles_controller_get_head_to_head()

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

**character_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**world:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[BattlesControllerGetHeadToHeadRequestPeriod]` 
    
</dd>
</dl>

<dl>
<dd>

**min_level:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_level:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[BattlesControllerGetHeadToHeadRequestSortBy]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[BattlesControllerGetHeadToHeadRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**include_total:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**min_battles:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**ph:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**matchmaking:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.battles.<a href="src/fern/battles/client.py">battles_controller_get_current_streak</a>(...) -> StreakResponseDtoOutput</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.battles.battles_controller_get_current_streak()

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

**character_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**world:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[BattlesControllerGetCurrentStreakRequestPeriod]` 
    
</dd>
</dl>

<dl>
<dd>

**min_level:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_level:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[BattlesControllerGetCurrentStreakRequestSortBy]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[BattlesControllerGetCurrentStreakRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**include_total:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**min_battles:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**ph:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**matchmaking:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.battles.<a href="src/fern/battles/client.py">battles_controller_get_battle_duration</a>(...) -> BattleDurationStatsResponseDtoOutput</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.battles.battles_controller_get_battle_duration()

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

**character_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**world:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[BattlesControllerGetBattleDurationRequestPeriod]` 
    
</dd>
</dl>

<dl>
<dd>

**min_level:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_level:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[BattlesControllerGetBattleDurationRequestSortBy]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[BattlesControllerGetBattleDurationRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**include_total:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**min_battles:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**ph:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**matchmaking:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.battles.<a href="src/fern/battles/client.py">battles_controller_get_ph_growth</a>(...) -> typing.List[PhGrowthDataPointResponseDtoOutput]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.battles.battles_controller_get_ph_growth()

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

**character_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**world:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[BattlesControllerGetPhGrowthRequestPeriod]` 
    
</dd>
</dl>

<dl>
<dd>

**min_level:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_level:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[BattlesControllerGetPhGrowthRequestSortBy]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[BattlesControllerGetPhGrowthRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**include_total:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**min_battles:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**ph:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**matchmaking:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.battles.<a href="src/fern/battles/client.py">battles_controller_get_rating_growth</a>(...) -> typing.List[RatingGrowthDataPointResponseDtoOutput]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.battles.battles_controller_get_rating_growth()

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

**character_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**world:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[BattlesControllerGetRatingGrowthRequestPeriod]` 
    
</dd>
</dl>

<dl>
<dd>

**min_level:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_level:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[BattlesControllerGetRatingGrowthRequestSortBy]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[BattlesControllerGetRatingGrowthRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**include_total:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**min_battles:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**ph:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**matchmaking:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.battles.<a href="src/fern/battles/client.py">battles_controller_get_rating_delta_by_opponent</a>(...) -> typing.List[RatingDeltaByOpponentResponseDtoOutput]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.battles.battles_controller_get_rating_delta_by_opponent()

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

**character_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**world:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[BattlesControllerGetRatingDeltaByOpponentRequestPeriod]` 
    
</dd>
</dl>

<dl>
<dd>

**min_level:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_level:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[BattlesControllerGetRatingDeltaByOpponentRequestSortBy]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[BattlesControllerGetRatingDeltaByOpponentRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**include_total:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**min_battles:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**ph:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**matchmaking:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.battles.<a href="src/fern/battles/client.py">battles_controller_get_player_vs_player_battles</a>(...) -> PlayerVsPlayerPaginatedResponseDtoOutput</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.battles.battles_controller_get_player_vs_player_battles(
    opponent_id="opponentId",
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

**opponent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**character_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**world:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[BattlesControllerGetPlayerVsPlayerBattlesRequestPeriod]` 
    
</dd>
</dl>

<dl>
<dd>

**min_level:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_level:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[BattlesControllerGetPlayerVsPlayerBattlesRequestSortBy]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[BattlesControllerGetPlayerVsPlayerBattlesRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**include_total:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**min_battles:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**ph:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**matchmaking:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**exclude_battle_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.battles.<a href="src/fern/battles/client.py">battles_controller_search_warriors</a>(...) -> BattleWarriorsSearchResponseDtoOutput</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.battles.battles_controller_search_warriors(
    q="q",
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

**q:** `str` 
    
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

<details><summary><code>client.battles.<a href="src/fern/battles/client.py">battles_controller_get_user_worlds</a>() -> BattleUserWorldsResponseDtoOutput</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.battles.battles_controller_get_user_worlds()

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

<details><summary><code>client.battles.<a href="src/fern/battles/client.py">battles_controller_get_battle_timeline</a>(...) -> BattleTimelineResponseDtoOutput</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.battles.battles_controller_get_battle_timeline(
    battle_id="battleId",
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

**battle_id:** `str` 
    
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

<details><summary><code>client.battles.<a href="src/fern/battles/client.py">battles_controller_get_battle</a>(...) -> BattleResponseDtoOutput</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.battles.battles_controller_get_battle(
    battle_id="battleId",
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

**battle_id:** `str` 
    
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

<details><summary><code>client.battles.<a href="src/fern/battles/client.py">battles_controller_delete_battle</a>(...) -> BattleDeletedResponseDtoOutput</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.battles.battles_controller_delete_battle(
    battle_id="battleId",
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

**battle_id:** `str` 
    
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

<details><summary><code>client.battles.<a href="src/fern/battles/client.py">battles_controller_update_battle</a>(...) -> BattleResponseDtoOutput</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.battles.battles_controller_update_battle(
    battle_id="battleId",
    public=True,
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

**battle_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**public:** `bool` 
    
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

<details><summary><code>client.battles.<a href="src/fern/battles/client.py">battles_controller_get_battle_raw_data</a>(...) -> BattleRawResponseDtoOutput</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.battles.battles_controller_get_battle_raw_data(
    battle_id="battleId",
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

**battle_id:** `str` 
    
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

## PublicBattles
<details><summary><code>client.public_battles.<a href="src/fern/public_battles/client.py">public_battles_controller_get_public_battle</a>(...) -> BattleResponseDtoOutput</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.public_battles.public_battles_controller_get_public_battle(
    battle_id="battleId",
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

**battle_id:** `str` 
    
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

<details><summary><code>client.public_battles.<a href="src/fern/public_battles/client.py">public_battles_controller_get_public_battle_raw</a>(...) -> BattleRawResponseDtoOutput</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.public_battles.public_battles_controller_get_public_battle_raw(
    battle_id="battleId",
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

**battle_id:** `str` 
    
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

<details><summary><code>client.public_battles.<a href="src/fern/public_battles/client.py">public_battles_controller_get_public_battle_timeline</a>(...) -> BattleTimelineResponseDtoOutput</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.public_battles.public_battles_controller_get_public_battle_timeline(
    battle_id="battleId",
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

**battle_id:** `str` 
    
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

## Internal
<details><summary><code>client.internal.<a href="src/fern/internal/client.py">internal_controller_delete_user_data</a>(...) -> BattleAcceptedResponseDtoOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Internal API caller only. Requires the BATTLELOG_CLEANUP_SECRET bearer credential; user sessions and forwarded identity headers do not authorize this operation.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.internal.internal_controller_delete_user_data(
    user_id="userId",
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

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
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

