

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.abyss_season_response_dto_output import AbyssSeasonResponseDtoOutput
from ..types.battle_analytics_response_dto_output import BattleAnalyticsResponseDtoOutput
from ..types.battle_characters_response_dto_output import BattleCharactersResponseDtoOutput
from ..types.battle_created_response_dto_output import BattleCreatedResponseDtoOutput
from ..types.battle_deleted_response_dto_output import BattleDeletedResponseDtoOutput
from ..types.battle_duration_stats_response_dto_output import BattleDurationStatsResponseDtoOutput
from ..types.battle_raw_response_dto_output import BattleRawResponseDtoOutput
from ..types.battle_response_dto_output import BattleResponseDtoOutput
from ..types.battle_timeline_response_dto_output import BattleTimelineResponseDtoOutput
from ..types.battle_user_worlds_response_dto_output import BattleUserWorldsResponseDtoOutput
from ..types.battle_warriors_search_response_dto_output import BattleWarriorsSearchResponseDtoOutput
from ..types.battles_list_response_dto_output import BattlesListResponseDtoOutput
from ..types.combat_profile_response_dto_output import CombatProfileResponseDtoOutput
from ..types.head_to_head_paginated_response_dto_output import HeadToHeadPaginatedResponseDtoOutput
from ..types.ph_growth_data_point_response_dto_output import PhGrowthDataPointResponseDtoOutput
from ..types.player_vs_player_paginated_response_dto_output import PlayerVsPlayerPaginatedResponseDtoOutput
from ..types.profession_win_rate_response_dto_output import ProfessionWinRateResponseDtoOutput
from ..types.rating_delta_by_opponent_response_dto_output import RatingDeltaByOpponentResponseDtoOutput
from ..types.rating_growth_data_point_response_dto_output import RatingGrowthDataPointResponseDtoOutput
from ..types.streak_response_dto_output import StreakResponseDtoOutput
from .raw_client import AsyncRawBattlesClient, RawBattlesClient
from .types.battles_controller_get_battle_analytics_request_period import (
    BattlesControllerGetBattleAnalyticsRequestPeriod,
)
from .types.battles_controller_get_battle_duration_request_period import BattlesControllerGetBattleDurationRequestPeriod
from .types.battles_controller_get_battle_duration_request_sort_by import (
    BattlesControllerGetBattleDurationRequestSortBy,
)
from .types.battles_controller_get_battle_duration_request_sort_order import (
    BattlesControllerGetBattleDurationRequestSortOrder,
)
from .types.battles_controller_get_combat_profile_request_period import BattlesControllerGetCombatProfileRequestPeriod
from .types.battles_controller_get_combat_profile_request_sort_by import BattlesControllerGetCombatProfileRequestSortBy
from .types.battles_controller_get_combat_profile_request_sort_order import (
    BattlesControllerGetCombatProfileRequestSortOrder,
)
from .types.battles_controller_get_current_streak_request_period import BattlesControllerGetCurrentStreakRequestPeriod
from .types.battles_controller_get_current_streak_request_sort_by import BattlesControllerGetCurrentStreakRequestSortBy
from .types.battles_controller_get_current_streak_request_sort_order import (
    BattlesControllerGetCurrentStreakRequestSortOrder,
)
from .types.battles_controller_get_dashboard_battles_request_result_item import (
    BattlesControllerGetDashboardBattlesRequestResultItem,
)
from .types.battles_controller_get_dashboard_battles_request_sort_order import (
    BattlesControllerGetDashboardBattlesRequestSortOrder,
)
from .types.battles_controller_get_dashboard_battles_request_type_item import (
    BattlesControllerGetDashboardBattlesRequestTypeItem,
)
from .types.battles_controller_get_head_to_head_request_period import BattlesControllerGetHeadToHeadRequestPeriod
from .types.battles_controller_get_head_to_head_request_sort_by import BattlesControllerGetHeadToHeadRequestSortBy
from .types.battles_controller_get_head_to_head_request_sort_order import BattlesControllerGetHeadToHeadRequestSortOrder
from .types.battles_controller_get_ph_growth_request_period import BattlesControllerGetPhGrowthRequestPeriod
from .types.battles_controller_get_ph_growth_request_sort_by import BattlesControllerGetPhGrowthRequestSortBy
from .types.battles_controller_get_ph_growth_request_sort_order import BattlesControllerGetPhGrowthRequestSortOrder
from .types.battles_controller_get_player_vs_player_battles_request_period import (
    BattlesControllerGetPlayerVsPlayerBattlesRequestPeriod,
)
from .types.battles_controller_get_player_vs_player_battles_request_sort_by import (
    BattlesControllerGetPlayerVsPlayerBattlesRequestSortBy,
)
from .types.battles_controller_get_player_vs_player_battles_request_sort_order import (
    BattlesControllerGetPlayerVsPlayerBattlesRequestSortOrder,
)
from .types.battles_controller_get_profession_win_rate_request_period import (
    BattlesControllerGetProfessionWinRateRequestPeriod,
)
from .types.battles_controller_get_profession_win_rate_request_sort_by import (
    BattlesControllerGetProfessionWinRateRequestSortBy,
)
from .types.battles_controller_get_profession_win_rate_request_sort_order import (
    BattlesControllerGetProfessionWinRateRequestSortOrder,
)
from .types.battles_controller_get_rating_delta_by_opponent_request_period import (
    BattlesControllerGetRatingDeltaByOpponentRequestPeriod,
)
from .types.battles_controller_get_rating_delta_by_opponent_request_sort_by import (
    BattlesControllerGetRatingDeltaByOpponentRequestSortBy,
)
from .types.battles_controller_get_rating_delta_by_opponent_request_sort_order import (
    BattlesControllerGetRatingDeltaByOpponentRequestSortOrder,
)
from .types.battles_controller_get_rating_growth_request_period import BattlesControllerGetRatingGrowthRequestPeriod
from .types.battles_controller_get_rating_growth_request_sort_by import BattlesControllerGetRatingGrowthRequestSortBy
from .types.battles_controller_get_rating_growth_request_sort_order import (
    BattlesControllerGetRatingGrowthRequestSortOrder,
)
from .types.create_battle_dto_events_item import CreateBattleDtoEventsItem


OMIT = typing.cast(typing.Any, ...)


class BattlesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBattlesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBattlesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBattlesClient
        """
        return self._raw_client

    def battles_controller_create_battle(
        self,
        *,
        account_id: str,
        character_id: str,
        world: str,
        events: typing.Sequence[CreateBattleDtoEventsItem],
        submission_id: typing.Optional[str] = OMIT,
        matchmaking: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BattleCreatedResponseDtoOutput:
        """
        Parameters
        ----------
        account_id : str

        character_id : str

        world : str

        events : typing.Sequence[CreateBattleDtoEventsItem]

        submission_id : typing.Optional[str]

        matchmaking : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleCreatedResponseDtoOutput


        Examples
        --------
        from fern.battles import CreateBattleDtoEventsItem, CreateBattleDtoEventsItemF

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
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
        """
        _response = self._raw_client.battles_controller_create_battle(
            account_id=account_id,
            character_id=character_id,
            world=world,
            events=events,
            submission_id=submission_id,
            matchmaking=matchmaking,
            request_options=request_options,
        )
        return _response.data

    def battles_controller_get_dashboard_battles(
        self,
        *,
        cursor: typing.Optional[str] = None,
        size: typing.Optional[float] = None,
        sort_order: typing.Optional[BattlesControllerGetDashboardBattlesRequestSortOrder] = None,
        include_total: typing.Optional[bool] = None,
        world: typing.Optional[str] = None,
        type: typing.Optional[
            typing.Union[
                BattlesControllerGetDashboardBattlesRequestTypeItem,
                typing.Sequence[BattlesControllerGetDashboardBattlesRequestTypeItem],
            ]
        ] = None,
        user_id: typing.Optional[str] = None,
        public: typing.Optional[bool] = None,
        character_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        search: typing.Optional[str] = None,
        result: typing.Optional[
            typing.Union[
                BattlesControllerGetDashboardBattlesRequestResultItem,
                typing.Sequence[BattlesControllerGetDashboardBattlesRequestResultItem],
            ]
        ] = None,
        ph: typing.Optional[bool] = None,
        matchmaking: typing.Optional[bool] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        min_level: typing.Optional[float] = None,
        max_level: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BattlesListResponseDtoOutput:
        """
        Parameters
        ----------
        cursor : typing.Optional[str]

        size : typing.Optional[float]

        sort_order : typing.Optional[BattlesControllerGetDashboardBattlesRequestSortOrder]

        include_total : typing.Optional[bool]

        world : typing.Optional[str]

        type : typing.Optional[typing.Union[BattlesControllerGetDashboardBattlesRequestTypeItem, typing.Sequence[BattlesControllerGetDashboardBattlesRequestTypeItem]]]

        user_id : typing.Optional[str]

        public : typing.Optional[bool]

        character_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        search : typing.Optional[str]

        result : typing.Optional[typing.Union[BattlesControllerGetDashboardBattlesRequestResultItem, typing.Sequence[BattlesControllerGetDashboardBattlesRequestResultItem]]]

        ph : typing.Optional[bool]

        matchmaking : typing.Optional[bool]

        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        min_level : typing.Optional[float]

        max_level : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattlesListResponseDtoOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.battles.battles_controller_get_dashboard_battles()
        """
        _response = self._raw_client.battles_controller_get_dashboard_battles(
            cursor=cursor,
            size=size,
            sort_order=sort_order,
            include_total=include_total,
            world=world,
            type=type,
            user_id=user_id,
            public=public,
            character_id=character_id,
            search=search,
            result=result,
            ph=ph,
            matchmaking=matchmaking,
            start_date=start_date,
            end_date=end_date,
            min_level=min_level,
            max_level=max_level,
            request_options=request_options,
        )
        return _response.data

    def battles_controller_get_user_characters(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BattleCharactersResponseDtoOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleCharactersResponseDtoOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.battles.battles_controller_get_user_characters()
        """
        _response = self._raw_client.battles_controller_get_user_characters(request_options=request_options)
        return _response.data

    def battles_controller_get_battle_analytics(
        self,
        *,
        character_id: typing.Optional[str] = None,
        world: typing.Optional[str] = None,
        period: typing.Optional[BattlesControllerGetBattleAnalyticsRequestPeriod] = None,
        min_level: typing.Optional[int] = None,
        max_level: typing.Optional[int] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        ph: typing.Optional[bool] = None,
        matchmaking: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BattleAnalyticsResponseDtoOutput:
        """
        Parameters
        ----------
        character_id : typing.Optional[str]

        world : typing.Optional[str]

        period : typing.Optional[BattlesControllerGetBattleAnalyticsRequestPeriod]

        min_level : typing.Optional[int]

        max_level : typing.Optional[int]

        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        ph : typing.Optional[bool]

        matchmaking : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleAnalyticsResponseDtoOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.battles.battles_controller_get_battle_analytics()
        """
        _response = self._raw_client.battles_controller_get_battle_analytics(
            character_id=character_id,
            world=world,
            period=period,
            min_level=min_level,
            max_level=max_level,
            start_date=start_date,
            end_date=end_date,
            ph=ph,
            matchmaking=matchmaking,
            request_options=request_options,
        )
        return _response.data

    def battles_controller_get_abyss_seasons(
        self,
        *,
        character_id: str,
        world: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AbyssSeasonResponseDtoOutput]:
        """
        Parameters
        ----------
        character_id : str

        world : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AbyssSeasonResponseDtoOutput]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.battles.battles_controller_get_abyss_seasons(
            character_id="characterId",
        )
        """
        _response = self._raw_client.battles_controller_get_abyss_seasons(
            character_id=character_id, world=world, request_options=request_options
        )
        return _response.data

    def battles_controller_get_combat_profile(
        self,
        *,
        character_id: typing.Optional[str] = None,
        world: typing.Optional[str] = None,
        period: typing.Optional[BattlesControllerGetCombatProfileRequestPeriod] = None,
        min_level: typing.Optional[int] = None,
        max_level: typing.Optional[int] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        size: typing.Optional[int] = None,
        sort_by: typing.Optional[BattlesControllerGetCombatProfileRequestSortBy] = None,
        sort_order: typing.Optional[BattlesControllerGetCombatProfileRequestSortOrder] = None,
        include_total: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        min_battles: typing.Optional[int] = None,
        ph: typing.Optional[bool] = None,
        matchmaking: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CombatProfileResponseDtoOutput:
        """
        Parameters
        ----------
        character_id : typing.Optional[str]

        world : typing.Optional[str]

        period : typing.Optional[BattlesControllerGetCombatProfileRequestPeriod]

        min_level : typing.Optional[int]

        max_level : typing.Optional[int]

        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        cursor : typing.Optional[str]

        size : typing.Optional[int]

        sort_by : typing.Optional[BattlesControllerGetCombatProfileRequestSortBy]

        sort_order : typing.Optional[BattlesControllerGetCombatProfileRequestSortOrder]

        include_total : typing.Optional[bool]

        search : typing.Optional[str]

        min_battles : typing.Optional[int]

        ph : typing.Optional[bool]

        matchmaking : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CombatProfileResponseDtoOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.battles.battles_controller_get_combat_profile()
        """
        _response = self._raw_client.battles_controller_get_combat_profile(
            character_id=character_id,
            world=world,
            period=period,
            min_level=min_level,
            max_level=max_level,
            start_date=start_date,
            end_date=end_date,
            cursor=cursor,
            size=size,
            sort_by=sort_by,
            sort_order=sort_order,
            include_total=include_total,
            search=search,
            min_battles=min_battles,
            ph=ph,
            matchmaking=matchmaking,
            request_options=request_options,
        )
        return _response.data

    def battles_controller_get_profession_win_rate(
        self,
        *,
        character_id: typing.Optional[str] = None,
        world: typing.Optional[str] = None,
        period: typing.Optional[BattlesControllerGetProfessionWinRateRequestPeriod] = None,
        min_level: typing.Optional[int] = None,
        max_level: typing.Optional[int] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        size: typing.Optional[int] = None,
        sort_by: typing.Optional[BattlesControllerGetProfessionWinRateRequestSortBy] = None,
        sort_order: typing.Optional[BattlesControllerGetProfessionWinRateRequestSortOrder] = None,
        include_total: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        min_battles: typing.Optional[int] = None,
        ph: typing.Optional[bool] = None,
        matchmaking: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ProfessionWinRateResponseDtoOutput]:
        """
        Parameters
        ----------
        character_id : typing.Optional[str]

        world : typing.Optional[str]

        period : typing.Optional[BattlesControllerGetProfessionWinRateRequestPeriod]

        min_level : typing.Optional[int]

        max_level : typing.Optional[int]

        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        cursor : typing.Optional[str]

        size : typing.Optional[int]

        sort_by : typing.Optional[BattlesControllerGetProfessionWinRateRequestSortBy]

        sort_order : typing.Optional[BattlesControllerGetProfessionWinRateRequestSortOrder]

        include_total : typing.Optional[bool]

        search : typing.Optional[str]

        min_battles : typing.Optional[int]

        ph : typing.Optional[bool]

        matchmaking : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ProfessionWinRateResponseDtoOutput]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.battles.battles_controller_get_profession_win_rate()
        """
        _response = self._raw_client.battles_controller_get_profession_win_rate(
            character_id=character_id,
            world=world,
            period=period,
            min_level=min_level,
            max_level=max_level,
            start_date=start_date,
            end_date=end_date,
            cursor=cursor,
            size=size,
            sort_by=sort_by,
            sort_order=sort_order,
            include_total=include_total,
            search=search,
            min_battles=min_battles,
            ph=ph,
            matchmaking=matchmaking,
            request_options=request_options,
        )
        return _response.data

    def battles_controller_get_head_to_head(
        self,
        *,
        character_id: typing.Optional[str] = None,
        world: typing.Optional[str] = None,
        period: typing.Optional[BattlesControllerGetHeadToHeadRequestPeriod] = None,
        min_level: typing.Optional[int] = None,
        max_level: typing.Optional[int] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        size: typing.Optional[int] = None,
        sort_by: typing.Optional[BattlesControllerGetHeadToHeadRequestSortBy] = None,
        sort_order: typing.Optional[BattlesControllerGetHeadToHeadRequestSortOrder] = None,
        include_total: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        min_battles: typing.Optional[int] = None,
        ph: typing.Optional[bool] = None,
        matchmaking: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HeadToHeadPaginatedResponseDtoOutput:
        """
        Parameters
        ----------
        character_id : typing.Optional[str]

        world : typing.Optional[str]

        period : typing.Optional[BattlesControllerGetHeadToHeadRequestPeriod]

        min_level : typing.Optional[int]

        max_level : typing.Optional[int]

        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        cursor : typing.Optional[str]

        size : typing.Optional[int]

        sort_by : typing.Optional[BattlesControllerGetHeadToHeadRequestSortBy]

        sort_order : typing.Optional[BattlesControllerGetHeadToHeadRequestSortOrder]

        include_total : typing.Optional[bool]

        search : typing.Optional[str]

        min_battles : typing.Optional[int]

        ph : typing.Optional[bool]

        matchmaking : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HeadToHeadPaginatedResponseDtoOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.battles.battles_controller_get_head_to_head()
        """
        _response = self._raw_client.battles_controller_get_head_to_head(
            character_id=character_id,
            world=world,
            period=period,
            min_level=min_level,
            max_level=max_level,
            start_date=start_date,
            end_date=end_date,
            cursor=cursor,
            size=size,
            sort_by=sort_by,
            sort_order=sort_order,
            include_total=include_total,
            search=search,
            min_battles=min_battles,
            ph=ph,
            matchmaking=matchmaking,
            request_options=request_options,
        )
        return _response.data

    def battles_controller_get_current_streak(
        self,
        *,
        character_id: typing.Optional[str] = None,
        world: typing.Optional[str] = None,
        period: typing.Optional[BattlesControllerGetCurrentStreakRequestPeriod] = None,
        min_level: typing.Optional[int] = None,
        max_level: typing.Optional[int] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        size: typing.Optional[int] = None,
        sort_by: typing.Optional[BattlesControllerGetCurrentStreakRequestSortBy] = None,
        sort_order: typing.Optional[BattlesControllerGetCurrentStreakRequestSortOrder] = None,
        include_total: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        min_battles: typing.Optional[int] = None,
        ph: typing.Optional[bool] = None,
        matchmaking: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StreakResponseDtoOutput:
        """
        Parameters
        ----------
        character_id : typing.Optional[str]

        world : typing.Optional[str]

        period : typing.Optional[BattlesControllerGetCurrentStreakRequestPeriod]

        min_level : typing.Optional[int]

        max_level : typing.Optional[int]

        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        cursor : typing.Optional[str]

        size : typing.Optional[int]

        sort_by : typing.Optional[BattlesControllerGetCurrentStreakRequestSortBy]

        sort_order : typing.Optional[BattlesControllerGetCurrentStreakRequestSortOrder]

        include_total : typing.Optional[bool]

        search : typing.Optional[str]

        min_battles : typing.Optional[int]

        ph : typing.Optional[bool]

        matchmaking : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StreakResponseDtoOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.battles.battles_controller_get_current_streak()
        """
        _response = self._raw_client.battles_controller_get_current_streak(
            character_id=character_id,
            world=world,
            period=period,
            min_level=min_level,
            max_level=max_level,
            start_date=start_date,
            end_date=end_date,
            cursor=cursor,
            size=size,
            sort_by=sort_by,
            sort_order=sort_order,
            include_total=include_total,
            search=search,
            min_battles=min_battles,
            ph=ph,
            matchmaking=matchmaking,
            request_options=request_options,
        )
        return _response.data

    def battles_controller_get_battle_duration(
        self,
        *,
        character_id: typing.Optional[str] = None,
        world: typing.Optional[str] = None,
        period: typing.Optional[BattlesControllerGetBattleDurationRequestPeriod] = None,
        min_level: typing.Optional[int] = None,
        max_level: typing.Optional[int] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        size: typing.Optional[int] = None,
        sort_by: typing.Optional[BattlesControllerGetBattleDurationRequestSortBy] = None,
        sort_order: typing.Optional[BattlesControllerGetBattleDurationRequestSortOrder] = None,
        include_total: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        min_battles: typing.Optional[int] = None,
        ph: typing.Optional[bool] = None,
        matchmaking: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BattleDurationStatsResponseDtoOutput:
        """
        Parameters
        ----------
        character_id : typing.Optional[str]

        world : typing.Optional[str]

        period : typing.Optional[BattlesControllerGetBattleDurationRequestPeriod]

        min_level : typing.Optional[int]

        max_level : typing.Optional[int]

        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        cursor : typing.Optional[str]

        size : typing.Optional[int]

        sort_by : typing.Optional[BattlesControllerGetBattleDurationRequestSortBy]

        sort_order : typing.Optional[BattlesControllerGetBattleDurationRequestSortOrder]

        include_total : typing.Optional[bool]

        search : typing.Optional[str]

        min_battles : typing.Optional[int]

        ph : typing.Optional[bool]

        matchmaking : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleDurationStatsResponseDtoOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.battles.battles_controller_get_battle_duration()
        """
        _response = self._raw_client.battles_controller_get_battle_duration(
            character_id=character_id,
            world=world,
            period=period,
            min_level=min_level,
            max_level=max_level,
            start_date=start_date,
            end_date=end_date,
            cursor=cursor,
            size=size,
            sort_by=sort_by,
            sort_order=sort_order,
            include_total=include_total,
            search=search,
            min_battles=min_battles,
            ph=ph,
            matchmaking=matchmaking,
            request_options=request_options,
        )
        return _response.data

    def battles_controller_get_ph_growth(
        self,
        *,
        character_id: typing.Optional[str] = None,
        world: typing.Optional[str] = None,
        period: typing.Optional[BattlesControllerGetPhGrowthRequestPeriod] = None,
        min_level: typing.Optional[int] = None,
        max_level: typing.Optional[int] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        size: typing.Optional[int] = None,
        sort_by: typing.Optional[BattlesControllerGetPhGrowthRequestSortBy] = None,
        sort_order: typing.Optional[BattlesControllerGetPhGrowthRequestSortOrder] = None,
        include_total: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        min_battles: typing.Optional[int] = None,
        ph: typing.Optional[bool] = None,
        matchmaking: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[PhGrowthDataPointResponseDtoOutput]:
        """
        Parameters
        ----------
        character_id : typing.Optional[str]

        world : typing.Optional[str]

        period : typing.Optional[BattlesControllerGetPhGrowthRequestPeriod]

        min_level : typing.Optional[int]

        max_level : typing.Optional[int]

        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        cursor : typing.Optional[str]

        size : typing.Optional[int]

        sort_by : typing.Optional[BattlesControllerGetPhGrowthRequestSortBy]

        sort_order : typing.Optional[BattlesControllerGetPhGrowthRequestSortOrder]

        include_total : typing.Optional[bool]

        search : typing.Optional[str]

        min_battles : typing.Optional[int]

        ph : typing.Optional[bool]

        matchmaking : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PhGrowthDataPointResponseDtoOutput]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.battles.battles_controller_get_ph_growth()
        """
        _response = self._raw_client.battles_controller_get_ph_growth(
            character_id=character_id,
            world=world,
            period=period,
            min_level=min_level,
            max_level=max_level,
            start_date=start_date,
            end_date=end_date,
            cursor=cursor,
            size=size,
            sort_by=sort_by,
            sort_order=sort_order,
            include_total=include_total,
            search=search,
            min_battles=min_battles,
            ph=ph,
            matchmaking=matchmaking,
            request_options=request_options,
        )
        return _response.data

    def battles_controller_get_rating_growth(
        self,
        *,
        character_id: typing.Optional[str] = None,
        world: typing.Optional[str] = None,
        period: typing.Optional[BattlesControllerGetRatingGrowthRequestPeriod] = None,
        min_level: typing.Optional[int] = None,
        max_level: typing.Optional[int] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        size: typing.Optional[int] = None,
        sort_by: typing.Optional[BattlesControllerGetRatingGrowthRequestSortBy] = None,
        sort_order: typing.Optional[BattlesControllerGetRatingGrowthRequestSortOrder] = None,
        include_total: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        min_battles: typing.Optional[int] = None,
        ph: typing.Optional[bool] = None,
        matchmaking: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[RatingGrowthDataPointResponseDtoOutput]:
        """
        Parameters
        ----------
        character_id : typing.Optional[str]

        world : typing.Optional[str]

        period : typing.Optional[BattlesControllerGetRatingGrowthRequestPeriod]

        min_level : typing.Optional[int]

        max_level : typing.Optional[int]

        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        cursor : typing.Optional[str]

        size : typing.Optional[int]

        sort_by : typing.Optional[BattlesControllerGetRatingGrowthRequestSortBy]

        sort_order : typing.Optional[BattlesControllerGetRatingGrowthRequestSortOrder]

        include_total : typing.Optional[bool]

        search : typing.Optional[str]

        min_battles : typing.Optional[int]

        ph : typing.Optional[bool]

        matchmaking : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RatingGrowthDataPointResponseDtoOutput]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.battles.battles_controller_get_rating_growth()
        """
        _response = self._raw_client.battles_controller_get_rating_growth(
            character_id=character_id,
            world=world,
            period=period,
            min_level=min_level,
            max_level=max_level,
            start_date=start_date,
            end_date=end_date,
            cursor=cursor,
            size=size,
            sort_by=sort_by,
            sort_order=sort_order,
            include_total=include_total,
            search=search,
            min_battles=min_battles,
            ph=ph,
            matchmaking=matchmaking,
            request_options=request_options,
        )
        return _response.data

    def battles_controller_get_rating_delta_by_opponent(
        self,
        *,
        character_id: typing.Optional[str] = None,
        world: typing.Optional[str] = None,
        period: typing.Optional[BattlesControllerGetRatingDeltaByOpponentRequestPeriod] = None,
        min_level: typing.Optional[int] = None,
        max_level: typing.Optional[int] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        size: typing.Optional[int] = None,
        sort_by: typing.Optional[BattlesControllerGetRatingDeltaByOpponentRequestSortBy] = None,
        sort_order: typing.Optional[BattlesControllerGetRatingDeltaByOpponentRequestSortOrder] = None,
        include_total: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        min_battles: typing.Optional[int] = None,
        ph: typing.Optional[bool] = None,
        matchmaking: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[RatingDeltaByOpponentResponseDtoOutput]:
        """
        Parameters
        ----------
        character_id : typing.Optional[str]

        world : typing.Optional[str]

        period : typing.Optional[BattlesControllerGetRatingDeltaByOpponentRequestPeriod]

        min_level : typing.Optional[int]

        max_level : typing.Optional[int]

        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        cursor : typing.Optional[str]

        size : typing.Optional[int]

        sort_by : typing.Optional[BattlesControllerGetRatingDeltaByOpponentRequestSortBy]

        sort_order : typing.Optional[BattlesControllerGetRatingDeltaByOpponentRequestSortOrder]

        include_total : typing.Optional[bool]

        search : typing.Optional[str]

        min_battles : typing.Optional[int]

        ph : typing.Optional[bool]

        matchmaking : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RatingDeltaByOpponentResponseDtoOutput]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.battles.battles_controller_get_rating_delta_by_opponent()
        """
        _response = self._raw_client.battles_controller_get_rating_delta_by_opponent(
            character_id=character_id,
            world=world,
            period=period,
            min_level=min_level,
            max_level=max_level,
            start_date=start_date,
            end_date=end_date,
            cursor=cursor,
            size=size,
            sort_by=sort_by,
            sort_order=sort_order,
            include_total=include_total,
            search=search,
            min_battles=min_battles,
            ph=ph,
            matchmaking=matchmaking,
            request_options=request_options,
        )
        return _response.data

    def battles_controller_get_player_vs_player_battles(
        self,
        *,
        opponent_id: str,
        character_id: typing.Optional[str] = None,
        world: typing.Optional[str] = None,
        period: typing.Optional[BattlesControllerGetPlayerVsPlayerBattlesRequestPeriod] = None,
        min_level: typing.Optional[int] = None,
        max_level: typing.Optional[int] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        size: typing.Optional[int] = None,
        sort_by: typing.Optional[BattlesControllerGetPlayerVsPlayerBattlesRequestSortBy] = None,
        sort_order: typing.Optional[BattlesControllerGetPlayerVsPlayerBattlesRequestSortOrder] = None,
        include_total: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        min_battles: typing.Optional[int] = None,
        ph: typing.Optional[bool] = None,
        matchmaking: typing.Optional[bool] = None,
        exclude_battle_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PlayerVsPlayerPaginatedResponseDtoOutput:
        """
        Parameters
        ----------
        opponent_id : str

        character_id : typing.Optional[str]

        world : typing.Optional[str]

        period : typing.Optional[BattlesControllerGetPlayerVsPlayerBattlesRequestPeriod]

        min_level : typing.Optional[int]

        max_level : typing.Optional[int]

        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        cursor : typing.Optional[str]

        size : typing.Optional[int]

        sort_by : typing.Optional[BattlesControllerGetPlayerVsPlayerBattlesRequestSortBy]

        sort_order : typing.Optional[BattlesControllerGetPlayerVsPlayerBattlesRequestSortOrder]

        include_total : typing.Optional[bool]

        search : typing.Optional[str]

        min_battles : typing.Optional[int]

        ph : typing.Optional[bool]

        matchmaking : typing.Optional[bool]

        exclude_battle_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PlayerVsPlayerPaginatedResponseDtoOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.battles.battles_controller_get_player_vs_player_battles(
            opponent_id="opponentId",
        )
        """
        _response = self._raw_client.battles_controller_get_player_vs_player_battles(
            opponent_id=opponent_id,
            character_id=character_id,
            world=world,
            period=period,
            min_level=min_level,
            max_level=max_level,
            start_date=start_date,
            end_date=end_date,
            cursor=cursor,
            size=size,
            sort_by=sort_by,
            sort_order=sort_order,
            include_total=include_total,
            search=search,
            min_battles=min_battles,
            ph=ph,
            matchmaking=matchmaking,
            exclude_battle_id=exclude_battle_id,
            request_options=request_options,
        )
        return _response.data

    def battles_controller_search_warriors(
        self, *, q: str, request_options: typing.Optional[RequestOptions] = None
    ) -> BattleWarriorsSearchResponseDtoOutput:
        """
        Parameters
        ----------
        q : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleWarriorsSearchResponseDtoOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.battles.battles_controller_search_warriors(
            q="q",
        )
        """
        _response = self._raw_client.battles_controller_search_warriors(q=q, request_options=request_options)
        return _response.data

    def battles_controller_get_user_worlds(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BattleUserWorldsResponseDtoOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleUserWorldsResponseDtoOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.battles.battles_controller_get_user_worlds()
        """
        _response = self._raw_client.battles_controller_get_user_worlds(request_options=request_options)
        return _response.data

    def battles_controller_get_battle_timeline(
        self, battle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BattleTimelineResponseDtoOutput:
        """
        Parameters
        ----------
        battle_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleTimelineResponseDtoOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.battles.battles_controller_get_battle_timeline(
            battle_id="battleId",
        )
        """
        _response = self._raw_client.battles_controller_get_battle_timeline(battle_id, request_options=request_options)
        return _response.data

    def battles_controller_get_battle(
        self, battle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BattleResponseDtoOutput:
        """
        Parameters
        ----------
        battle_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleResponseDtoOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.battles.battles_controller_get_battle(
            battle_id="battleId",
        )
        """
        _response = self._raw_client.battles_controller_get_battle(battle_id, request_options=request_options)
        return _response.data

    def battles_controller_delete_battle(
        self, battle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BattleDeletedResponseDtoOutput:
        """
        Parameters
        ----------
        battle_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleDeletedResponseDtoOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.battles.battles_controller_delete_battle(
            battle_id="battleId",
        )
        """
        _response = self._raw_client.battles_controller_delete_battle(battle_id, request_options=request_options)
        return _response.data

    def battles_controller_update_battle(
        self, battle_id: str, *, public: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> BattleResponseDtoOutput:
        """
        Parameters
        ----------
        battle_id : str

        public : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleResponseDtoOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.battles.battles_controller_update_battle(
            battle_id="battleId",
            public=True,
        )
        """
        _response = self._raw_client.battles_controller_update_battle(
            battle_id, public=public, request_options=request_options
        )
        return _response.data

    def battles_controller_get_battle_raw_data(
        self, battle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BattleRawResponseDtoOutput:
        """
        Parameters
        ----------
        battle_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleRawResponseDtoOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.battles.battles_controller_get_battle_raw_data(
            battle_id="battleId",
        )
        """
        _response = self._raw_client.battles_controller_get_battle_raw_data(battle_id, request_options=request_options)
        return _response.data


class AsyncBattlesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBattlesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBattlesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBattlesClient
        """
        return self._raw_client

    async def battles_controller_create_battle(
        self,
        *,
        account_id: str,
        character_id: str,
        world: str,
        events: typing.Sequence[CreateBattleDtoEventsItem],
        submission_id: typing.Optional[str] = OMIT,
        matchmaking: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BattleCreatedResponseDtoOutput:
        """
        Parameters
        ----------
        account_id : str

        character_id : str

        world : str

        events : typing.Sequence[CreateBattleDtoEventsItem]

        submission_id : typing.Optional[str]

        matchmaking : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleCreatedResponseDtoOutput


        Examples
        --------
        import asyncio

        from fern.battles import CreateBattleDtoEventsItem, CreateBattleDtoEventsItemF

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.battles.battles_controller_create_battle(
                account_id="accountId",
                character_id="characterId",
                world="world",
                events=[
                    CreateBattleDtoEventsItem(
                        f=CreateBattleDtoEventsItemF(),
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.battles_controller_create_battle(
            account_id=account_id,
            character_id=character_id,
            world=world,
            events=events,
            submission_id=submission_id,
            matchmaking=matchmaking,
            request_options=request_options,
        )
        return _response.data

    async def battles_controller_get_dashboard_battles(
        self,
        *,
        cursor: typing.Optional[str] = None,
        size: typing.Optional[float] = None,
        sort_order: typing.Optional[BattlesControllerGetDashboardBattlesRequestSortOrder] = None,
        include_total: typing.Optional[bool] = None,
        world: typing.Optional[str] = None,
        type: typing.Optional[
            typing.Union[
                BattlesControllerGetDashboardBattlesRequestTypeItem,
                typing.Sequence[BattlesControllerGetDashboardBattlesRequestTypeItem],
            ]
        ] = None,
        user_id: typing.Optional[str] = None,
        public: typing.Optional[bool] = None,
        character_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        search: typing.Optional[str] = None,
        result: typing.Optional[
            typing.Union[
                BattlesControllerGetDashboardBattlesRequestResultItem,
                typing.Sequence[BattlesControllerGetDashboardBattlesRequestResultItem],
            ]
        ] = None,
        ph: typing.Optional[bool] = None,
        matchmaking: typing.Optional[bool] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        min_level: typing.Optional[float] = None,
        max_level: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BattlesListResponseDtoOutput:
        """
        Parameters
        ----------
        cursor : typing.Optional[str]

        size : typing.Optional[float]

        sort_order : typing.Optional[BattlesControllerGetDashboardBattlesRequestSortOrder]

        include_total : typing.Optional[bool]

        world : typing.Optional[str]

        type : typing.Optional[typing.Union[BattlesControllerGetDashboardBattlesRequestTypeItem, typing.Sequence[BattlesControllerGetDashboardBattlesRequestTypeItem]]]

        user_id : typing.Optional[str]

        public : typing.Optional[bool]

        character_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        search : typing.Optional[str]

        result : typing.Optional[typing.Union[BattlesControllerGetDashboardBattlesRequestResultItem, typing.Sequence[BattlesControllerGetDashboardBattlesRequestResultItem]]]

        ph : typing.Optional[bool]

        matchmaking : typing.Optional[bool]

        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        min_level : typing.Optional[float]

        max_level : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattlesListResponseDtoOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.battles.battles_controller_get_dashboard_battles()


        asyncio.run(main())
        """
        _response = await self._raw_client.battles_controller_get_dashboard_battles(
            cursor=cursor,
            size=size,
            sort_order=sort_order,
            include_total=include_total,
            world=world,
            type=type,
            user_id=user_id,
            public=public,
            character_id=character_id,
            search=search,
            result=result,
            ph=ph,
            matchmaking=matchmaking,
            start_date=start_date,
            end_date=end_date,
            min_level=min_level,
            max_level=max_level,
            request_options=request_options,
        )
        return _response.data

    async def battles_controller_get_user_characters(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BattleCharactersResponseDtoOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleCharactersResponseDtoOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.battles.battles_controller_get_user_characters()


        asyncio.run(main())
        """
        _response = await self._raw_client.battles_controller_get_user_characters(request_options=request_options)
        return _response.data

    async def battles_controller_get_battle_analytics(
        self,
        *,
        character_id: typing.Optional[str] = None,
        world: typing.Optional[str] = None,
        period: typing.Optional[BattlesControllerGetBattleAnalyticsRequestPeriod] = None,
        min_level: typing.Optional[int] = None,
        max_level: typing.Optional[int] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        ph: typing.Optional[bool] = None,
        matchmaking: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BattleAnalyticsResponseDtoOutput:
        """
        Parameters
        ----------
        character_id : typing.Optional[str]

        world : typing.Optional[str]

        period : typing.Optional[BattlesControllerGetBattleAnalyticsRequestPeriod]

        min_level : typing.Optional[int]

        max_level : typing.Optional[int]

        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        ph : typing.Optional[bool]

        matchmaking : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleAnalyticsResponseDtoOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.battles.battles_controller_get_battle_analytics()


        asyncio.run(main())
        """
        _response = await self._raw_client.battles_controller_get_battle_analytics(
            character_id=character_id,
            world=world,
            period=period,
            min_level=min_level,
            max_level=max_level,
            start_date=start_date,
            end_date=end_date,
            ph=ph,
            matchmaking=matchmaking,
            request_options=request_options,
        )
        return _response.data

    async def battles_controller_get_abyss_seasons(
        self,
        *,
        character_id: str,
        world: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AbyssSeasonResponseDtoOutput]:
        """
        Parameters
        ----------
        character_id : str

        world : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AbyssSeasonResponseDtoOutput]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.battles.battles_controller_get_abyss_seasons(
                character_id="characterId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.battles_controller_get_abyss_seasons(
            character_id=character_id, world=world, request_options=request_options
        )
        return _response.data

    async def battles_controller_get_combat_profile(
        self,
        *,
        character_id: typing.Optional[str] = None,
        world: typing.Optional[str] = None,
        period: typing.Optional[BattlesControllerGetCombatProfileRequestPeriod] = None,
        min_level: typing.Optional[int] = None,
        max_level: typing.Optional[int] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        size: typing.Optional[int] = None,
        sort_by: typing.Optional[BattlesControllerGetCombatProfileRequestSortBy] = None,
        sort_order: typing.Optional[BattlesControllerGetCombatProfileRequestSortOrder] = None,
        include_total: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        min_battles: typing.Optional[int] = None,
        ph: typing.Optional[bool] = None,
        matchmaking: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CombatProfileResponseDtoOutput:
        """
        Parameters
        ----------
        character_id : typing.Optional[str]

        world : typing.Optional[str]

        period : typing.Optional[BattlesControllerGetCombatProfileRequestPeriod]

        min_level : typing.Optional[int]

        max_level : typing.Optional[int]

        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        cursor : typing.Optional[str]

        size : typing.Optional[int]

        sort_by : typing.Optional[BattlesControllerGetCombatProfileRequestSortBy]

        sort_order : typing.Optional[BattlesControllerGetCombatProfileRequestSortOrder]

        include_total : typing.Optional[bool]

        search : typing.Optional[str]

        min_battles : typing.Optional[int]

        ph : typing.Optional[bool]

        matchmaking : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CombatProfileResponseDtoOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.battles.battles_controller_get_combat_profile()


        asyncio.run(main())
        """
        _response = await self._raw_client.battles_controller_get_combat_profile(
            character_id=character_id,
            world=world,
            period=period,
            min_level=min_level,
            max_level=max_level,
            start_date=start_date,
            end_date=end_date,
            cursor=cursor,
            size=size,
            sort_by=sort_by,
            sort_order=sort_order,
            include_total=include_total,
            search=search,
            min_battles=min_battles,
            ph=ph,
            matchmaking=matchmaking,
            request_options=request_options,
        )
        return _response.data

    async def battles_controller_get_profession_win_rate(
        self,
        *,
        character_id: typing.Optional[str] = None,
        world: typing.Optional[str] = None,
        period: typing.Optional[BattlesControllerGetProfessionWinRateRequestPeriod] = None,
        min_level: typing.Optional[int] = None,
        max_level: typing.Optional[int] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        size: typing.Optional[int] = None,
        sort_by: typing.Optional[BattlesControllerGetProfessionWinRateRequestSortBy] = None,
        sort_order: typing.Optional[BattlesControllerGetProfessionWinRateRequestSortOrder] = None,
        include_total: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        min_battles: typing.Optional[int] = None,
        ph: typing.Optional[bool] = None,
        matchmaking: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ProfessionWinRateResponseDtoOutput]:
        """
        Parameters
        ----------
        character_id : typing.Optional[str]

        world : typing.Optional[str]

        period : typing.Optional[BattlesControllerGetProfessionWinRateRequestPeriod]

        min_level : typing.Optional[int]

        max_level : typing.Optional[int]

        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        cursor : typing.Optional[str]

        size : typing.Optional[int]

        sort_by : typing.Optional[BattlesControllerGetProfessionWinRateRequestSortBy]

        sort_order : typing.Optional[BattlesControllerGetProfessionWinRateRequestSortOrder]

        include_total : typing.Optional[bool]

        search : typing.Optional[str]

        min_battles : typing.Optional[int]

        ph : typing.Optional[bool]

        matchmaking : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ProfessionWinRateResponseDtoOutput]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.battles.battles_controller_get_profession_win_rate()


        asyncio.run(main())
        """
        _response = await self._raw_client.battles_controller_get_profession_win_rate(
            character_id=character_id,
            world=world,
            period=period,
            min_level=min_level,
            max_level=max_level,
            start_date=start_date,
            end_date=end_date,
            cursor=cursor,
            size=size,
            sort_by=sort_by,
            sort_order=sort_order,
            include_total=include_total,
            search=search,
            min_battles=min_battles,
            ph=ph,
            matchmaking=matchmaking,
            request_options=request_options,
        )
        return _response.data

    async def battles_controller_get_head_to_head(
        self,
        *,
        character_id: typing.Optional[str] = None,
        world: typing.Optional[str] = None,
        period: typing.Optional[BattlesControllerGetHeadToHeadRequestPeriod] = None,
        min_level: typing.Optional[int] = None,
        max_level: typing.Optional[int] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        size: typing.Optional[int] = None,
        sort_by: typing.Optional[BattlesControllerGetHeadToHeadRequestSortBy] = None,
        sort_order: typing.Optional[BattlesControllerGetHeadToHeadRequestSortOrder] = None,
        include_total: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        min_battles: typing.Optional[int] = None,
        ph: typing.Optional[bool] = None,
        matchmaking: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HeadToHeadPaginatedResponseDtoOutput:
        """
        Parameters
        ----------
        character_id : typing.Optional[str]

        world : typing.Optional[str]

        period : typing.Optional[BattlesControllerGetHeadToHeadRequestPeriod]

        min_level : typing.Optional[int]

        max_level : typing.Optional[int]

        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        cursor : typing.Optional[str]

        size : typing.Optional[int]

        sort_by : typing.Optional[BattlesControllerGetHeadToHeadRequestSortBy]

        sort_order : typing.Optional[BattlesControllerGetHeadToHeadRequestSortOrder]

        include_total : typing.Optional[bool]

        search : typing.Optional[str]

        min_battles : typing.Optional[int]

        ph : typing.Optional[bool]

        matchmaking : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HeadToHeadPaginatedResponseDtoOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.battles.battles_controller_get_head_to_head()


        asyncio.run(main())
        """
        _response = await self._raw_client.battles_controller_get_head_to_head(
            character_id=character_id,
            world=world,
            period=period,
            min_level=min_level,
            max_level=max_level,
            start_date=start_date,
            end_date=end_date,
            cursor=cursor,
            size=size,
            sort_by=sort_by,
            sort_order=sort_order,
            include_total=include_total,
            search=search,
            min_battles=min_battles,
            ph=ph,
            matchmaking=matchmaking,
            request_options=request_options,
        )
        return _response.data

    async def battles_controller_get_current_streak(
        self,
        *,
        character_id: typing.Optional[str] = None,
        world: typing.Optional[str] = None,
        period: typing.Optional[BattlesControllerGetCurrentStreakRequestPeriod] = None,
        min_level: typing.Optional[int] = None,
        max_level: typing.Optional[int] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        size: typing.Optional[int] = None,
        sort_by: typing.Optional[BattlesControllerGetCurrentStreakRequestSortBy] = None,
        sort_order: typing.Optional[BattlesControllerGetCurrentStreakRequestSortOrder] = None,
        include_total: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        min_battles: typing.Optional[int] = None,
        ph: typing.Optional[bool] = None,
        matchmaking: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StreakResponseDtoOutput:
        """
        Parameters
        ----------
        character_id : typing.Optional[str]

        world : typing.Optional[str]

        period : typing.Optional[BattlesControllerGetCurrentStreakRequestPeriod]

        min_level : typing.Optional[int]

        max_level : typing.Optional[int]

        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        cursor : typing.Optional[str]

        size : typing.Optional[int]

        sort_by : typing.Optional[BattlesControllerGetCurrentStreakRequestSortBy]

        sort_order : typing.Optional[BattlesControllerGetCurrentStreakRequestSortOrder]

        include_total : typing.Optional[bool]

        search : typing.Optional[str]

        min_battles : typing.Optional[int]

        ph : typing.Optional[bool]

        matchmaking : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StreakResponseDtoOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.battles.battles_controller_get_current_streak()


        asyncio.run(main())
        """
        _response = await self._raw_client.battles_controller_get_current_streak(
            character_id=character_id,
            world=world,
            period=period,
            min_level=min_level,
            max_level=max_level,
            start_date=start_date,
            end_date=end_date,
            cursor=cursor,
            size=size,
            sort_by=sort_by,
            sort_order=sort_order,
            include_total=include_total,
            search=search,
            min_battles=min_battles,
            ph=ph,
            matchmaking=matchmaking,
            request_options=request_options,
        )
        return _response.data

    async def battles_controller_get_battle_duration(
        self,
        *,
        character_id: typing.Optional[str] = None,
        world: typing.Optional[str] = None,
        period: typing.Optional[BattlesControllerGetBattleDurationRequestPeriod] = None,
        min_level: typing.Optional[int] = None,
        max_level: typing.Optional[int] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        size: typing.Optional[int] = None,
        sort_by: typing.Optional[BattlesControllerGetBattleDurationRequestSortBy] = None,
        sort_order: typing.Optional[BattlesControllerGetBattleDurationRequestSortOrder] = None,
        include_total: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        min_battles: typing.Optional[int] = None,
        ph: typing.Optional[bool] = None,
        matchmaking: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BattleDurationStatsResponseDtoOutput:
        """
        Parameters
        ----------
        character_id : typing.Optional[str]

        world : typing.Optional[str]

        period : typing.Optional[BattlesControllerGetBattleDurationRequestPeriod]

        min_level : typing.Optional[int]

        max_level : typing.Optional[int]

        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        cursor : typing.Optional[str]

        size : typing.Optional[int]

        sort_by : typing.Optional[BattlesControllerGetBattleDurationRequestSortBy]

        sort_order : typing.Optional[BattlesControllerGetBattleDurationRequestSortOrder]

        include_total : typing.Optional[bool]

        search : typing.Optional[str]

        min_battles : typing.Optional[int]

        ph : typing.Optional[bool]

        matchmaking : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleDurationStatsResponseDtoOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.battles.battles_controller_get_battle_duration()


        asyncio.run(main())
        """
        _response = await self._raw_client.battles_controller_get_battle_duration(
            character_id=character_id,
            world=world,
            period=period,
            min_level=min_level,
            max_level=max_level,
            start_date=start_date,
            end_date=end_date,
            cursor=cursor,
            size=size,
            sort_by=sort_by,
            sort_order=sort_order,
            include_total=include_total,
            search=search,
            min_battles=min_battles,
            ph=ph,
            matchmaking=matchmaking,
            request_options=request_options,
        )
        return _response.data

    async def battles_controller_get_ph_growth(
        self,
        *,
        character_id: typing.Optional[str] = None,
        world: typing.Optional[str] = None,
        period: typing.Optional[BattlesControllerGetPhGrowthRequestPeriod] = None,
        min_level: typing.Optional[int] = None,
        max_level: typing.Optional[int] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        size: typing.Optional[int] = None,
        sort_by: typing.Optional[BattlesControllerGetPhGrowthRequestSortBy] = None,
        sort_order: typing.Optional[BattlesControllerGetPhGrowthRequestSortOrder] = None,
        include_total: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        min_battles: typing.Optional[int] = None,
        ph: typing.Optional[bool] = None,
        matchmaking: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[PhGrowthDataPointResponseDtoOutput]:
        """
        Parameters
        ----------
        character_id : typing.Optional[str]

        world : typing.Optional[str]

        period : typing.Optional[BattlesControllerGetPhGrowthRequestPeriod]

        min_level : typing.Optional[int]

        max_level : typing.Optional[int]

        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        cursor : typing.Optional[str]

        size : typing.Optional[int]

        sort_by : typing.Optional[BattlesControllerGetPhGrowthRequestSortBy]

        sort_order : typing.Optional[BattlesControllerGetPhGrowthRequestSortOrder]

        include_total : typing.Optional[bool]

        search : typing.Optional[str]

        min_battles : typing.Optional[int]

        ph : typing.Optional[bool]

        matchmaking : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PhGrowthDataPointResponseDtoOutput]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.battles.battles_controller_get_ph_growth()


        asyncio.run(main())
        """
        _response = await self._raw_client.battles_controller_get_ph_growth(
            character_id=character_id,
            world=world,
            period=period,
            min_level=min_level,
            max_level=max_level,
            start_date=start_date,
            end_date=end_date,
            cursor=cursor,
            size=size,
            sort_by=sort_by,
            sort_order=sort_order,
            include_total=include_total,
            search=search,
            min_battles=min_battles,
            ph=ph,
            matchmaking=matchmaking,
            request_options=request_options,
        )
        return _response.data

    async def battles_controller_get_rating_growth(
        self,
        *,
        character_id: typing.Optional[str] = None,
        world: typing.Optional[str] = None,
        period: typing.Optional[BattlesControllerGetRatingGrowthRequestPeriod] = None,
        min_level: typing.Optional[int] = None,
        max_level: typing.Optional[int] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        size: typing.Optional[int] = None,
        sort_by: typing.Optional[BattlesControllerGetRatingGrowthRequestSortBy] = None,
        sort_order: typing.Optional[BattlesControllerGetRatingGrowthRequestSortOrder] = None,
        include_total: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        min_battles: typing.Optional[int] = None,
        ph: typing.Optional[bool] = None,
        matchmaking: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[RatingGrowthDataPointResponseDtoOutput]:
        """
        Parameters
        ----------
        character_id : typing.Optional[str]

        world : typing.Optional[str]

        period : typing.Optional[BattlesControllerGetRatingGrowthRequestPeriod]

        min_level : typing.Optional[int]

        max_level : typing.Optional[int]

        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        cursor : typing.Optional[str]

        size : typing.Optional[int]

        sort_by : typing.Optional[BattlesControllerGetRatingGrowthRequestSortBy]

        sort_order : typing.Optional[BattlesControllerGetRatingGrowthRequestSortOrder]

        include_total : typing.Optional[bool]

        search : typing.Optional[str]

        min_battles : typing.Optional[int]

        ph : typing.Optional[bool]

        matchmaking : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RatingGrowthDataPointResponseDtoOutput]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.battles.battles_controller_get_rating_growth()


        asyncio.run(main())
        """
        _response = await self._raw_client.battles_controller_get_rating_growth(
            character_id=character_id,
            world=world,
            period=period,
            min_level=min_level,
            max_level=max_level,
            start_date=start_date,
            end_date=end_date,
            cursor=cursor,
            size=size,
            sort_by=sort_by,
            sort_order=sort_order,
            include_total=include_total,
            search=search,
            min_battles=min_battles,
            ph=ph,
            matchmaking=matchmaking,
            request_options=request_options,
        )
        return _response.data

    async def battles_controller_get_rating_delta_by_opponent(
        self,
        *,
        character_id: typing.Optional[str] = None,
        world: typing.Optional[str] = None,
        period: typing.Optional[BattlesControllerGetRatingDeltaByOpponentRequestPeriod] = None,
        min_level: typing.Optional[int] = None,
        max_level: typing.Optional[int] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        size: typing.Optional[int] = None,
        sort_by: typing.Optional[BattlesControllerGetRatingDeltaByOpponentRequestSortBy] = None,
        sort_order: typing.Optional[BattlesControllerGetRatingDeltaByOpponentRequestSortOrder] = None,
        include_total: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        min_battles: typing.Optional[int] = None,
        ph: typing.Optional[bool] = None,
        matchmaking: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[RatingDeltaByOpponentResponseDtoOutput]:
        """
        Parameters
        ----------
        character_id : typing.Optional[str]

        world : typing.Optional[str]

        period : typing.Optional[BattlesControllerGetRatingDeltaByOpponentRequestPeriod]

        min_level : typing.Optional[int]

        max_level : typing.Optional[int]

        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        cursor : typing.Optional[str]

        size : typing.Optional[int]

        sort_by : typing.Optional[BattlesControllerGetRatingDeltaByOpponentRequestSortBy]

        sort_order : typing.Optional[BattlesControllerGetRatingDeltaByOpponentRequestSortOrder]

        include_total : typing.Optional[bool]

        search : typing.Optional[str]

        min_battles : typing.Optional[int]

        ph : typing.Optional[bool]

        matchmaking : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RatingDeltaByOpponentResponseDtoOutput]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.battles.battles_controller_get_rating_delta_by_opponent()


        asyncio.run(main())
        """
        _response = await self._raw_client.battles_controller_get_rating_delta_by_opponent(
            character_id=character_id,
            world=world,
            period=period,
            min_level=min_level,
            max_level=max_level,
            start_date=start_date,
            end_date=end_date,
            cursor=cursor,
            size=size,
            sort_by=sort_by,
            sort_order=sort_order,
            include_total=include_total,
            search=search,
            min_battles=min_battles,
            ph=ph,
            matchmaking=matchmaking,
            request_options=request_options,
        )
        return _response.data

    async def battles_controller_get_player_vs_player_battles(
        self,
        *,
        opponent_id: str,
        character_id: typing.Optional[str] = None,
        world: typing.Optional[str] = None,
        period: typing.Optional[BattlesControllerGetPlayerVsPlayerBattlesRequestPeriod] = None,
        min_level: typing.Optional[int] = None,
        max_level: typing.Optional[int] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        size: typing.Optional[int] = None,
        sort_by: typing.Optional[BattlesControllerGetPlayerVsPlayerBattlesRequestSortBy] = None,
        sort_order: typing.Optional[BattlesControllerGetPlayerVsPlayerBattlesRequestSortOrder] = None,
        include_total: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        min_battles: typing.Optional[int] = None,
        ph: typing.Optional[bool] = None,
        matchmaking: typing.Optional[bool] = None,
        exclude_battle_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PlayerVsPlayerPaginatedResponseDtoOutput:
        """
        Parameters
        ----------
        opponent_id : str

        character_id : typing.Optional[str]

        world : typing.Optional[str]

        period : typing.Optional[BattlesControllerGetPlayerVsPlayerBattlesRequestPeriod]

        min_level : typing.Optional[int]

        max_level : typing.Optional[int]

        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        cursor : typing.Optional[str]

        size : typing.Optional[int]

        sort_by : typing.Optional[BattlesControllerGetPlayerVsPlayerBattlesRequestSortBy]

        sort_order : typing.Optional[BattlesControllerGetPlayerVsPlayerBattlesRequestSortOrder]

        include_total : typing.Optional[bool]

        search : typing.Optional[str]

        min_battles : typing.Optional[int]

        ph : typing.Optional[bool]

        matchmaking : typing.Optional[bool]

        exclude_battle_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PlayerVsPlayerPaginatedResponseDtoOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.battles.battles_controller_get_player_vs_player_battles(
                opponent_id="opponentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.battles_controller_get_player_vs_player_battles(
            opponent_id=opponent_id,
            character_id=character_id,
            world=world,
            period=period,
            min_level=min_level,
            max_level=max_level,
            start_date=start_date,
            end_date=end_date,
            cursor=cursor,
            size=size,
            sort_by=sort_by,
            sort_order=sort_order,
            include_total=include_total,
            search=search,
            min_battles=min_battles,
            ph=ph,
            matchmaking=matchmaking,
            exclude_battle_id=exclude_battle_id,
            request_options=request_options,
        )
        return _response.data

    async def battles_controller_search_warriors(
        self, *, q: str, request_options: typing.Optional[RequestOptions] = None
    ) -> BattleWarriorsSearchResponseDtoOutput:
        """
        Parameters
        ----------
        q : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleWarriorsSearchResponseDtoOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.battles.battles_controller_search_warriors(
                q="q",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.battles_controller_search_warriors(q=q, request_options=request_options)
        return _response.data

    async def battles_controller_get_user_worlds(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BattleUserWorldsResponseDtoOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleUserWorldsResponseDtoOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.battles.battles_controller_get_user_worlds()


        asyncio.run(main())
        """
        _response = await self._raw_client.battles_controller_get_user_worlds(request_options=request_options)
        return _response.data

    async def battles_controller_get_battle_timeline(
        self, battle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BattleTimelineResponseDtoOutput:
        """
        Parameters
        ----------
        battle_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleTimelineResponseDtoOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.battles.battles_controller_get_battle_timeline(
                battle_id="battleId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.battles_controller_get_battle_timeline(
            battle_id, request_options=request_options
        )
        return _response.data

    async def battles_controller_get_battle(
        self, battle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BattleResponseDtoOutput:
        """
        Parameters
        ----------
        battle_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleResponseDtoOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.battles.battles_controller_get_battle(
                battle_id="battleId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.battles_controller_get_battle(battle_id, request_options=request_options)
        return _response.data

    async def battles_controller_delete_battle(
        self, battle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BattleDeletedResponseDtoOutput:
        """
        Parameters
        ----------
        battle_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleDeletedResponseDtoOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.battles.battles_controller_delete_battle(
                battle_id="battleId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.battles_controller_delete_battle(battle_id, request_options=request_options)
        return _response.data

    async def battles_controller_update_battle(
        self, battle_id: str, *, public: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> BattleResponseDtoOutput:
        """
        Parameters
        ----------
        battle_id : str

        public : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleResponseDtoOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.battles.battles_controller_update_battle(
                battle_id="battleId",
                public=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.battles_controller_update_battle(
            battle_id, public=public, request_options=request_options
        )
        return _response.data

    async def battles_controller_get_battle_raw_data(
        self, battle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BattleRawResponseDtoOutput:
        """
        Parameters
        ----------
        battle_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleRawResponseDtoOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.battles.battles_controller_get_battle_raw_data(
                battle_id="battleId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.battles_controller_get_battle_raw_data(
            battle_id, request_options=request_options
        )
        return _response.data
