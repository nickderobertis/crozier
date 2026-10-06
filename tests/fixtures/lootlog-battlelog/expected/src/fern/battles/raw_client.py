

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawBattlesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[BattleCreatedResponseDtoOutput]:
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
        HttpResponse[BattleCreatedResponseDtoOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            "battles",
            method="POST",
            json={
                "accountId": account_id,
                "characterId": character_id,
                "submissionId": submission_id,
                "world": world,
                "matchmaking": matchmaking,
                "events": convert_and_respect_annotation_metadata(
                    object_=events, annotation=typing.Sequence[CreateBattleDtoEventsItem], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BattleCreatedResponseDtoOutput,
                    parse_obj_as(
                        type_=BattleCreatedResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[BattlesListResponseDtoOutput]:
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
        HttpResponse[BattlesListResponseDtoOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            "battles/@me",
            method="GET",
            params={
                "cursor": cursor,
                "size": size,
                "sortOrder": sort_order,
                "includeTotal": include_total,
                "world": world,
                "type": type,
                "userId": user_id,
                "public": public,
                "characterId": character_id,
                "search": search,
                "result": result,
                "ph": ph,
                "matchmaking": matchmaking,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "minLevel": min_level,
                "maxLevel": max_level,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BattlesListResponseDtoOutput,
                    parse_obj_as(
                        type_=BattlesListResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def battles_controller_get_user_characters(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BattleCharactersResponseDtoOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BattleCharactersResponseDtoOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            "battles/@me/characters",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BattleCharactersResponseDtoOutput,
                    parse_obj_as(
                        type_=BattleCharactersResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[BattleAnalyticsResponseDtoOutput]:
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
        HttpResponse[BattleAnalyticsResponseDtoOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            "battles/@me/analytics",
            method="GET",
            params={
                "characterId": character_id,
                "world": world,
                "period": period,
                "minLevel": min_level,
                "maxLevel": max_level,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "ph": ph,
                "matchmaking": matchmaking,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BattleAnalyticsResponseDtoOutput,
                    parse_obj_as(
                        type_=BattleAnalyticsResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def battles_controller_get_abyss_seasons(
        self,
        *,
        character_id: str,
        world: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[AbyssSeasonResponseDtoOutput]]:
        """
        Parameters
        ----------
        character_id : str

        world : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[AbyssSeasonResponseDtoOutput]]

        """
        _response = self._client_wrapper.httpx_client.request(
            "battles/@me/abyss/seasons",
            method="GET",
            params={
                "characterId": character_id,
                "world": world,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AbyssSeasonResponseDtoOutput],
                    parse_obj_as(
                        type_=typing.List[AbyssSeasonResponseDtoOutput],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[CombatProfileResponseDtoOutput]:
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
        HttpResponse[CombatProfileResponseDtoOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            "battles/@me/statistics/combat-profile",
            method="GET",
            params={
                "characterId": character_id,
                "world": world,
                "period": period,
                "minLevel": min_level,
                "maxLevel": max_level,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "cursor": cursor,
                "size": size,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "includeTotal": include_total,
                "search": search,
                "minBattles": min_battles,
                "ph": ph,
                "matchmaking": matchmaking,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CombatProfileResponseDtoOutput,
                    parse_obj_as(
                        type_=CombatProfileResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[typing.List[ProfessionWinRateResponseDtoOutput]]:
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
        HttpResponse[typing.List[ProfessionWinRateResponseDtoOutput]]

        """
        _response = self._client_wrapper.httpx_client.request(
            "battles/@me/statistics/profession-win-rate",
            method="GET",
            params={
                "characterId": character_id,
                "world": world,
                "period": period,
                "minLevel": min_level,
                "maxLevel": max_level,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "cursor": cursor,
                "size": size,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "includeTotal": include_total,
                "search": search,
                "minBattles": min_battles,
                "ph": ph,
                "matchmaking": matchmaking,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ProfessionWinRateResponseDtoOutput],
                    parse_obj_as(
                        type_=typing.List[ProfessionWinRateResponseDtoOutput],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[HeadToHeadPaginatedResponseDtoOutput]:
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
        HttpResponse[HeadToHeadPaginatedResponseDtoOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            "battles/@me/statistics/head-to-head",
            method="GET",
            params={
                "characterId": character_id,
                "world": world,
                "period": period,
                "minLevel": min_level,
                "maxLevel": max_level,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "cursor": cursor,
                "size": size,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "includeTotal": include_total,
                "search": search,
                "minBattles": min_battles,
                "ph": ph,
                "matchmaking": matchmaking,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    HeadToHeadPaginatedResponseDtoOutput,
                    parse_obj_as(
                        type_=HeadToHeadPaginatedResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[StreakResponseDtoOutput]:
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
        HttpResponse[StreakResponseDtoOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            "battles/@me/statistics/streak",
            method="GET",
            params={
                "characterId": character_id,
                "world": world,
                "period": period,
                "minLevel": min_level,
                "maxLevel": max_level,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "cursor": cursor,
                "size": size,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "includeTotal": include_total,
                "search": search,
                "minBattles": min_battles,
                "ph": ph,
                "matchmaking": matchmaking,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StreakResponseDtoOutput,
                    parse_obj_as(
                        type_=StreakResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[BattleDurationStatsResponseDtoOutput]:
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
        HttpResponse[BattleDurationStatsResponseDtoOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            "battles/@me/statistics/duration",
            method="GET",
            params={
                "characterId": character_id,
                "world": world,
                "period": period,
                "minLevel": min_level,
                "maxLevel": max_level,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "cursor": cursor,
                "size": size,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "includeTotal": include_total,
                "search": search,
                "minBattles": min_battles,
                "ph": ph,
                "matchmaking": matchmaking,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BattleDurationStatsResponseDtoOutput,
                    parse_obj_as(
                        type_=BattleDurationStatsResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[typing.List[PhGrowthDataPointResponseDtoOutput]]:
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
        HttpResponse[typing.List[PhGrowthDataPointResponseDtoOutput]]

        """
        _response = self._client_wrapper.httpx_client.request(
            "battles/@me/statistics/ph-growth",
            method="GET",
            params={
                "characterId": character_id,
                "world": world,
                "period": period,
                "minLevel": min_level,
                "maxLevel": max_level,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "cursor": cursor,
                "size": size,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "includeTotal": include_total,
                "search": search,
                "minBattles": min_battles,
                "ph": ph,
                "matchmaking": matchmaking,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PhGrowthDataPointResponseDtoOutput],
                    parse_obj_as(
                        type_=typing.List[PhGrowthDataPointResponseDtoOutput],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[typing.List[RatingGrowthDataPointResponseDtoOutput]]:
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
        HttpResponse[typing.List[RatingGrowthDataPointResponseDtoOutput]]

        """
        _response = self._client_wrapper.httpx_client.request(
            "battles/@me/statistics/rating-growth",
            method="GET",
            params={
                "characterId": character_id,
                "world": world,
                "period": period,
                "minLevel": min_level,
                "maxLevel": max_level,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "cursor": cursor,
                "size": size,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "includeTotal": include_total,
                "search": search,
                "minBattles": min_battles,
                "ph": ph,
                "matchmaking": matchmaking,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RatingGrowthDataPointResponseDtoOutput],
                    parse_obj_as(
                        type_=typing.List[RatingGrowthDataPointResponseDtoOutput],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[typing.List[RatingDeltaByOpponentResponseDtoOutput]]:
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
        HttpResponse[typing.List[RatingDeltaByOpponentResponseDtoOutput]]

        """
        _response = self._client_wrapper.httpx_client.request(
            "battles/@me/statistics/rating-delta-by-opponent",
            method="GET",
            params={
                "characterId": character_id,
                "world": world,
                "period": period,
                "minLevel": min_level,
                "maxLevel": max_level,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "cursor": cursor,
                "size": size,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "includeTotal": include_total,
                "search": search,
                "minBattles": min_battles,
                "ph": ph,
                "matchmaking": matchmaking,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RatingDeltaByOpponentResponseDtoOutput],
                    parse_obj_as(
                        type_=typing.List[RatingDeltaByOpponentResponseDtoOutput],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[PlayerVsPlayerPaginatedResponseDtoOutput]:
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
        HttpResponse[PlayerVsPlayerPaginatedResponseDtoOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            "battles/@me/statistics/player-vs-player",
            method="GET",
            params={
                "characterId": character_id,
                "world": world,
                "period": period,
                "minLevel": min_level,
                "maxLevel": max_level,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "cursor": cursor,
                "size": size,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "includeTotal": include_total,
                "search": search,
                "minBattles": min_battles,
                "ph": ph,
                "matchmaking": matchmaking,
                "opponentId": opponent_id,
                "excludeBattleId": exclude_battle_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PlayerVsPlayerPaginatedResponseDtoOutput,
                    parse_obj_as(
                        type_=PlayerVsPlayerPaginatedResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def battles_controller_search_warriors(
        self, *, q: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BattleWarriorsSearchResponseDtoOutput]:
        """
        Parameters
        ----------
        q : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BattleWarriorsSearchResponseDtoOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            "battles/@me/warriors/search",
            method="GET",
            params={
                "q": q,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BattleWarriorsSearchResponseDtoOutput,
                    parse_obj_as(
                        type_=BattleWarriorsSearchResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def battles_controller_get_user_worlds(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BattleUserWorldsResponseDtoOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BattleUserWorldsResponseDtoOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            "battles/@me/worlds",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BattleUserWorldsResponseDtoOutput,
                    parse_obj_as(
                        type_=BattleUserWorldsResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def battles_controller_get_battle_timeline(
        self, battle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BattleTimelineResponseDtoOutput]:
        """
        Parameters
        ----------
        battle_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BattleTimelineResponseDtoOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"battles/{encode_path_param(battle_id)}/timeline",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BattleTimelineResponseDtoOutput,
                    parse_obj_as(
                        type_=BattleTimelineResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def battles_controller_get_battle(
        self, battle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BattleResponseDtoOutput]:
        """
        Parameters
        ----------
        battle_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BattleResponseDtoOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"battles/{encode_path_param(battle_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BattleResponseDtoOutput,
                    parse_obj_as(
                        type_=BattleResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def battles_controller_delete_battle(
        self, battle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BattleDeletedResponseDtoOutput]:
        """
        Parameters
        ----------
        battle_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BattleDeletedResponseDtoOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"battles/{encode_path_param(battle_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BattleDeletedResponseDtoOutput,
                    parse_obj_as(
                        type_=BattleDeletedResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def battles_controller_update_battle(
        self, battle_id: str, *, public: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BattleResponseDtoOutput]:
        """
        Parameters
        ----------
        battle_id : str

        public : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BattleResponseDtoOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"battles/{encode_path_param(battle_id)}",
            method="PATCH",
            json={
                "public": public,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BattleResponseDtoOutput,
                    parse_obj_as(
                        type_=BattleResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def battles_controller_get_battle_raw_data(
        self, battle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BattleRawResponseDtoOutput]:
        """
        Parameters
        ----------
        battle_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BattleRawResponseDtoOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"battles/{encode_path_param(battle_id)}/raw",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BattleRawResponseDtoOutput,
                    parse_obj_as(
                        type_=BattleRawResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawBattlesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[BattleCreatedResponseDtoOutput]:
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
        AsyncHttpResponse[BattleCreatedResponseDtoOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "battles",
            method="POST",
            json={
                "accountId": account_id,
                "characterId": character_id,
                "submissionId": submission_id,
                "world": world,
                "matchmaking": matchmaking,
                "events": convert_and_respect_annotation_metadata(
                    object_=events, annotation=typing.Sequence[CreateBattleDtoEventsItem], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BattleCreatedResponseDtoOutput,
                    parse_obj_as(
                        type_=BattleCreatedResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[BattlesListResponseDtoOutput]:
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
        AsyncHttpResponse[BattlesListResponseDtoOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "battles/@me",
            method="GET",
            params={
                "cursor": cursor,
                "size": size,
                "sortOrder": sort_order,
                "includeTotal": include_total,
                "world": world,
                "type": type,
                "userId": user_id,
                "public": public,
                "characterId": character_id,
                "search": search,
                "result": result,
                "ph": ph,
                "matchmaking": matchmaking,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "minLevel": min_level,
                "maxLevel": max_level,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BattlesListResponseDtoOutput,
                    parse_obj_as(
                        type_=BattlesListResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def battles_controller_get_user_characters(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BattleCharactersResponseDtoOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BattleCharactersResponseDtoOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "battles/@me/characters",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BattleCharactersResponseDtoOutput,
                    parse_obj_as(
                        type_=BattleCharactersResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[BattleAnalyticsResponseDtoOutput]:
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
        AsyncHttpResponse[BattleAnalyticsResponseDtoOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "battles/@me/analytics",
            method="GET",
            params={
                "characterId": character_id,
                "world": world,
                "period": period,
                "minLevel": min_level,
                "maxLevel": max_level,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "ph": ph,
                "matchmaking": matchmaking,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BattleAnalyticsResponseDtoOutput,
                    parse_obj_as(
                        type_=BattleAnalyticsResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def battles_controller_get_abyss_seasons(
        self,
        *,
        character_id: str,
        world: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[AbyssSeasonResponseDtoOutput]]:
        """
        Parameters
        ----------
        character_id : str

        world : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[AbyssSeasonResponseDtoOutput]]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "battles/@me/abyss/seasons",
            method="GET",
            params={
                "characterId": character_id,
                "world": world,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AbyssSeasonResponseDtoOutput],
                    parse_obj_as(
                        type_=typing.List[AbyssSeasonResponseDtoOutput],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[CombatProfileResponseDtoOutput]:
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
        AsyncHttpResponse[CombatProfileResponseDtoOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "battles/@me/statistics/combat-profile",
            method="GET",
            params={
                "characterId": character_id,
                "world": world,
                "period": period,
                "minLevel": min_level,
                "maxLevel": max_level,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "cursor": cursor,
                "size": size,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "includeTotal": include_total,
                "search": search,
                "minBattles": min_battles,
                "ph": ph,
                "matchmaking": matchmaking,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CombatProfileResponseDtoOutput,
                    parse_obj_as(
                        type_=CombatProfileResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[typing.List[ProfessionWinRateResponseDtoOutput]]:
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
        AsyncHttpResponse[typing.List[ProfessionWinRateResponseDtoOutput]]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "battles/@me/statistics/profession-win-rate",
            method="GET",
            params={
                "characterId": character_id,
                "world": world,
                "period": period,
                "minLevel": min_level,
                "maxLevel": max_level,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "cursor": cursor,
                "size": size,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "includeTotal": include_total,
                "search": search,
                "minBattles": min_battles,
                "ph": ph,
                "matchmaking": matchmaking,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ProfessionWinRateResponseDtoOutput],
                    parse_obj_as(
                        type_=typing.List[ProfessionWinRateResponseDtoOutput],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[HeadToHeadPaginatedResponseDtoOutput]:
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
        AsyncHttpResponse[HeadToHeadPaginatedResponseDtoOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "battles/@me/statistics/head-to-head",
            method="GET",
            params={
                "characterId": character_id,
                "world": world,
                "period": period,
                "minLevel": min_level,
                "maxLevel": max_level,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "cursor": cursor,
                "size": size,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "includeTotal": include_total,
                "search": search,
                "minBattles": min_battles,
                "ph": ph,
                "matchmaking": matchmaking,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    HeadToHeadPaginatedResponseDtoOutput,
                    parse_obj_as(
                        type_=HeadToHeadPaginatedResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[StreakResponseDtoOutput]:
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
        AsyncHttpResponse[StreakResponseDtoOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "battles/@me/statistics/streak",
            method="GET",
            params={
                "characterId": character_id,
                "world": world,
                "period": period,
                "minLevel": min_level,
                "maxLevel": max_level,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "cursor": cursor,
                "size": size,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "includeTotal": include_total,
                "search": search,
                "minBattles": min_battles,
                "ph": ph,
                "matchmaking": matchmaking,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StreakResponseDtoOutput,
                    parse_obj_as(
                        type_=StreakResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[BattleDurationStatsResponseDtoOutput]:
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
        AsyncHttpResponse[BattleDurationStatsResponseDtoOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "battles/@me/statistics/duration",
            method="GET",
            params={
                "characterId": character_id,
                "world": world,
                "period": period,
                "minLevel": min_level,
                "maxLevel": max_level,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "cursor": cursor,
                "size": size,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "includeTotal": include_total,
                "search": search,
                "minBattles": min_battles,
                "ph": ph,
                "matchmaking": matchmaking,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BattleDurationStatsResponseDtoOutput,
                    parse_obj_as(
                        type_=BattleDurationStatsResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[typing.List[PhGrowthDataPointResponseDtoOutput]]:
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
        AsyncHttpResponse[typing.List[PhGrowthDataPointResponseDtoOutput]]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "battles/@me/statistics/ph-growth",
            method="GET",
            params={
                "characterId": character_id,
                "world": world,
                "period": period,
                "minLevel": min_level,
                "maxLevel": max_level,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "cursor": cursor,
                "size": size,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "includeTotal": include_total,
                "search": search,
                "minBattles": min_battles,
                "ph": ph,
                "matchmaking": matchmaking,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PhGrowthDataPointResponseDtoOutput],
                    parse_obj_as(
                        type_=typing.List[PhGrowthDataPointResponseDtoOutput],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[typing.List[RatingGrowthDataPointResponseDtoOutput]]:
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
        AsyncHttpResponse[typing.List[RatingGrowthDataPointResponseDtoOutput]]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "battles/@me/statistics/rating-growth",
            method="GET",
            params={
                "characterId": character_id,
                "world": world,
                "period": period,
                "minLevel": min_level,
                "maxLevel": max_level,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "cursor": cursor,
                "size": size,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "includeTotal": include_total,
                "search": search,
                "minBattles": min_battles,
                "ph": ph,
                "matchmaking": matchmaking,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RatingGrowthDataPointResponseDtoOutput],
                    parse_obj_as(
                        type_=typing.List[RatingGrowthDataPointResponseDtoOutput],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[typing.List[RatingDeltaByOpponentResponseDtoOutput]]:
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
        AsyncHttpResponse[typing.List[RatingDeltaByOpponentResponseDtoOutput]]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "battles/@me/statistics/rating-delta-by-opponent",
            method="GET",
            params={
                "characterId": character_id,
                "world": world,
                "period": period,
                "minLevel": min_level,
                "maxLevel": max_level,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "cursor": cursor,
                "size": size,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "includeTotal": include_total,
                "search": search,
                "minBattles": min_battles,
                "ph": ph,
                "matchmaking": matchmaking,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RatingDeltaByOpponentResponseDtoOutput],
                    parse_obj_as(
                        type_=typing.List[RatingDeltaByOpponentResponseDtoOutput],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[PlayerVsPlayerPaginatedResponseDtoOutput]:
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
        AsyncHttpResponse[PlayerVsPlayerPaginatedResponseDtoOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "battles/@me/statistics/player-vs-player",
            method="GET",
            params={
                "characterId": character_id,
                "world": world,
                "period": period,
                "minLevel": min_level,
                "maxLevel": max_level,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "cursor": cursor,
                "size": size,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "includeTotal": include_total,
                "search": search,
                "minBattles": min_battles,
                "ph": ph,
                "matchmaking": matchmaking,
                "opponentId": opponent_id,
                "excludeBattleId": exclude_battle_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PlayerVsPlayerPaginatedResponseDtoOutput,
                    parse_obj_as(
                        type_=PlayerVsPlayerPaginatedResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def battles_controller_search_warriors(
        self, *, q: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BattleWarriorsSearchResponseDtoOutput]:
        """
        Parameters
        ----------
        q : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BattleWarriorsSearchResponseDtoOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "battles/@me/warriors/search",
            method="GET",
            params={
                "q": q,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BattleWarriorsSearchResponseDtoOutput,
                    parse_obj_as(
                        type_=BattleWarriorsSearchResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def battles_controller_get_user_worlds(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BattleUserWorldsResponseDtoOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BattleUserWorldsResponseDtoOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "battles/@me/worlds",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BattleUserWorldsResponseDtoOutput,
                    parse_obj_as(
                        type_=BattleUserWorldsResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def battles_controller_get_battle_timeline(
        self, battle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BattleTimelineResponseDtoOutput]:
        """
        Parameters
        ----------
        battle_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BattleTimelineResponseDtoOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"battles/{encode_path_param(battle_id)}/timeline",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BattleTimelineResponseDtoOutput,
                    parse_obj_as(
                        type_=BattleTimelineResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def battles_controller_get_battle(
        self, battle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BattleResponseDtoOutput]:
        """
        Parameters
        ----------
        battle_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BattleResponseDtoOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"battles/{encode_path_param(battle_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BattleResponseDtoOutput,
                    parse_obj_as(
                        type_=BattleResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def battles_controller_delete_battle(
        self, battle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BattleDeletedResponseDtoOutput]:
        """
        Parameters
        ----------
        battle_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BattleDeletedResponseDtoOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"battles/{encode_path_param(battle_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BattleDeletedResponseDtoOutput,
                    parse_obj_as(
                        type_=BattleDeletedResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def battles_controller_update_battle(
        self, battle_id: str, *, public: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BattleResponseDtoOutput]:
        """
        Parameters
        ----------
        battle_id : str

        public : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BattleResponseDtoOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"battles/{encode_path_param(battle_id)}",
            method="PATCH",
            json={
                "public": public,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BattleResponseDtoOutput,
                    parse_obj_as(
                        type_=BattleResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def battles_controller_get_battle_raw_data(
        self, battle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BattleRawResponseDtoOutput]:
        """
        Parameters
        ----------
        battle_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BattleRawResponseDtoOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"battles/{encode_path_param(battle_id)}/raw",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BattleRawResponseDtoOutput,
                    parse_obj_as(
                        type_=BattleRawResponseDtoOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
