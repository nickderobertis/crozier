

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.fireteam_get_active_private_clan_fireteam_count_response import (
    FireteamGetActivePrivateClanFireteamCountResponse,
)
from .types.fireteam_get_available_clan_fireteams_response import FireteamGetAvailableClanFireteamsResponse
from .types.fireteam_get_clan_fireteam_response import FireteamGetClanFireteamResponse
from .types.fireteam_get_my_clan_fireteams_response import FireteamGetMyClanFireteamsResponse
from .types.fireteam_search_public_available_clan_fireteams_response import (
    FireteamSearchPublicAvailableClanFireteamsResponse,
)
from pydantic import ValidationError


class RawFireteamClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getactiveprivateclanfireteamcount(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FireteamGetActivePrivateClanFireteamCountResponse]:
        """
        Gets a count of all active non-public fireteams for the specified clan. Maximum value returned is 25.

        Parameters
        ----------
        group_id : int
            The group id of the clan.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FireteamGetActivePrivateClanFireteamCountResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Fireteam/Clan/{encode_path_param(group_id)}/ActiveCount/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FireteamGetActivePrivateClanFireteamCountResponse,
                    parse_obj_as(
                        type_=FireteamGetActivePrivateClanFireteamCountResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getavailableclanfireteams(
        self,
        group_id: int,
        platform: int,
        activity_type: int,
        date_range: int,
        slot_filter: int,
        public_only: int,
        page: int,
        *,
        exclude_immediate: typing.Optional[bool] = None,
        lang_filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FireteamGetAvailableClanFireteamsResponse]:
        """
        Gets a listing of all of this clan's fireteams that are have available slots. Caller is not checked for join criteria so caching is maximized.

        Parameters
        ----------
        group_id : int
            The group id of the clan.

        platform : int
            The platform filter.

        activity_type : int
            The activity type to filter by.

        date_range : int
            The date range to grab available fireteams.

        slot_filter : int
            Filters based on available slots

        public_only : int
            Determines public/private filtering.

        page : int
            Zero based page

        exclude_immediate : typing.Optional[bool]
            If you wish the result to exclude immediate fireteams, set this to true. Immediate-only can be forced using the dateRange enum.

        lang_filter : typing.Optional[str]
            An optional language filter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FireteamGetAvailableClanFireteamsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Fireteam/Clan/{encode_path_param(group_id)}/Available/{encode_path_param(platform)}/{encode_path_param(activity_type)}/{encode_path_param(date_range)}/{encode_path_param(slot_filter)}/{encode_path_param(public_only)}/{encode_path_param(page)}/",
            method="GET",
            params={
                "excludeImmediate": exclude_immediate,
                "langFilter": lang_filter,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FireteamGetAvailableClanFireteamsResponse,
                    parse_obj_as(
                        type_=FireteamGetAvailableClanFireteamsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getmyclanfireteams(
        self,
        group_id: int,
        platform: int,
        include_closed: bool,
        page: int,
        *,
        group_filter: typing.Optional[bool] = None,
        lang_filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FireteamGetMyClanFireteamsResponse]:
        """
        Gets a listing of all fireteams that caller is an applicant, a member, or an alternate of.

        Parameters
        ----------
        group_id : int
            The group id of the clan. (This parameter is ignored unless the optional query parameter groupFilter is true).

        platform : int
            The platform filter.

        include_closed : bool
            If true, return fireteams that have been closed.

        page : int
            Deprecated parameter, ignored.

        group_filter : typing.Optional[bool]
            If true, filter by clan. Otherwise, ignore the clan and show all of the user's fireteams.

        lang_filter : typing.Optional[str]
            An optional language filter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FireteamGetMyClanFireteamsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Fireteam/Clan/{encode_path_param(group_id)}/My/{encode_path_param(platform)}/{encode_path_param(include_closed)}/{encode_path_param(page)}/",
            method="GET",
            params={
                "groupFilter": group_filter,
                "langFilter": lang_filter,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FireteamGetMyClanFireteamsResponse,
                    parse_obj_as(
                        type_=FireteamGetMyClanFireteamsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getclanfireteam(
        self, group_id: int, fireteam_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FireteamGetClanFireteamResponse]:
        """
        Gets a specific fireteam.

        Parameters
        ----------
        group_id : int
            The group id of the clan.

        fireteam_id : int
            The unique id of the fireteam.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FireteamGetClanFireteamResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Fireteam/Clan/{encode_path_param(group_id)}/Summary/{encode_path_param(fireteam_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FireteamGetClanFireteamResponse,
                    parse_obj_as(
                        type_=FireteamGetClanFireteamResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def searchpublicavailableclanfireteams(
        self,
        platform: int,
        activity_type: int,
        date_range: int,
        slot_filter: int,
        page: int,
        *,
        exclude_immediate: typing.Optional[bool] = None,
        lang_filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FireteamSearchPublicAvailableClanFireteamsResponse]:
        """
        Gets a listing of all public fireteams starting now with open slots. Caller is not checked for join criteria so caching is maximized.

        Parameters
        ----------
        platform : int
            The platform filter.

        activity_type : int
            The activity type to filter by.

        date_range : int
            The date range to grab available fireteams.

        slot_filter : int
            Filters based on available slots

        page : int
            Zero based page

        exclude_immediate : typing.Optional[bool]
            If you wish the result to exclude immediate fireteams, set this to true. Immediate-only can be forced using the dateRange enum.

        lang_filter : typing.Optional[str]
            An optional language filter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FireteamSearchPublicAvailableClanFireteamsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Fireteam/Search/Available/{encode_path_param(platform)}/{encode_path_param(activity_type)}/{encode_path_param(date_range)}/{encode_path_param(slot_filter)}/{encode_path_param(page)}/",
            method="GET",
            params={
                "excludeImmediate": exclude_immediate,
                "langFilter": lang_filter,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FireteamSearchPublicAvailableClanFireteamsResponse,
                    parse_obj_as(
                        type_=FireteamSearchPublicAvailableClanFireteamsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawFireteamClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getactiveprivateclanfireteamcount(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FireteamGetActivePrivateClanFireteamCountResponse]:
        """
        Gets a count of all active non-public fireteams for the specified clan. Maximum value returned is 25.

        Parameters
        ----------
        group_id : int
            The group id of the clan.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FireteamGetActivePrivateClanFireteamCountResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Fireteam/Clan/{encode_path_param(group_id)}/ActiveCount/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FireteamGetActivePrivateClanFireteamCountResponse,
                    parse_obj_as(
                        type_=FireteamGetActivePrivateClanFireteamCountResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getavailableclanfireteams(
        self,
        group_id: int,
        platform: int,
        activity_type: int,
        date_range: int,
        slot_filter: int,
        public_only: int,
        page: int,
        *,
        exclude_immediate: typing.Optional[bool] = None,
        lang_filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FireteamGetAvailableClanFireteamsResponse]:
        """
        Gets a listing of all of this clan's fireteams that are have available slots. Caller is not checked for join criteria so caching is maximized.

        Parameters
        ----------
        group_id : int
            The group id of the clan.

        platform : int
            The platform filter.

        activity_type : int
            The activity type to filter by.

        date_range : int
            The date range to grab available fireteams.

        slot_filter : int
            Filters based on available slots

        public_only : int
            Determines public/private filtering.

        page : int
            Zero based page

        exclude_immediate : typing.Optional[bool]
            If you wish the result to exclude immediate fireteams, set this to true. Immediate-only can be forced using the dateRange enum.

        lang_filter : typing.Optional[str]
            An optional language filter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FireteamGetAvailableClanFireteamsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Fireteam/Clan/{encode_path_param(group_id)}/Available/{encode_path_param(platform)}/{encode_path_param(activity_type)}/{encode_path_param(date_range)}/{encode_path_param(slot_filter)}/{encode_path_param(public_only)}/{encode_path_param(page)}/",
            method="GET",
            params={
                "excludeImmediate": exclude_immediate,
                "langFilter": lang_filter,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FireteamGetAvailableClanFireteamsResponse,
                    parse_obj_as(
                        type_=FireteamGetAvailableClanFireteamsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getmyclanfireteams(
        self,
        group_id: int,
        platform: int,
        include_closed: bool,
        page: int,
        *,
        group_filter: typing.Optional[bool] = None,
        lang_filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FireteamGetMyClanFireteamsResponse]:
        """
        Gets a listing of all fireteams that caller is an applicant, a member, or an alternate of.

        Parameters
        ----------
        group_id : int
            The group id of the clan. (This parameter is ignored unless the optional query parameter groupFilter is true).

        platform : int
            The platform filter.

        include_closed : bool
            If true, return fireteams that have been closed.

        page : int
            Deprecated parameter, ignored.

        group_filter : typing.Optional[bool]
            If true, filter by clan. Otherwise, ignore the clan and show all of the user's fireteams.

        lang_filter : typing.Optional[str]
            An optional language filter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FireteamGetMyClanFireteamsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Fireteam/Clan/{encode_path_param(group_id)}/My/{encode_path_param(platform)}/{encode_path_param(include_closed)}/{encode_path_param(page)}/",
            method="GET",
            params={
                "groupFilter": group_filter,
                "langFilter": lang_filter,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FireteamGetMyClanFireteamsResponse,
                    parse_obj_as(
                        type_=FireteamGetMyClanFireteamsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getclanfireteam(
        self, group_id: int, fireteam_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FireteamGetClanFireteamResponse]:
        """
        Gets a specific fireteam.

        Parameters
        ----------
        group_id : int
            The group id of the clan.

        fireteam_id : int
            The unique id of the fireteam.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FireteamGetClanFireteamResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Fireteam/Clan/{encode_path_param(group_id)}/Summary/{encode_path_param(fireteam_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FireteamGetClanFireteamResponse,
                    parse_obj_as(
                        type_=FireteamGetClanFireteamResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def searchpublicavailableclanfireteams(
        self,
        platform: int,
        activity_type: int,
        date_range: int,
        slot_filter: int,
        page: int,
        *,
        exclude_immediate: typing.Optional[bool] = None,
        lang_filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FireteamSearchPublicAvailableClanFireteamsResponse]:
        """
        Gets a listing of all public fireteams starting now with open slots. Caller is not checked for join criteria so caching is maximized.

        Parameters
        ----------
        platform : int
            The platform filter.

        activity_type : int
            The activity type to filter by.

        date_range : int
            The date range to grab available fireteams.

        slot_filter : int
            Filters based on available slots

        page : int
            Zero based page

        exclude_immediate : typing.Optional[bool]
            If you wish the result to exclude immediate fireteams, set this to true. Immediate-only can be forced using the dateRange enum.

        lang_filter : typing.Optional[str]
            An optional language filter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FireteamSearchPublicAvailableClanFireteamsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Fireteam/Search/Available/{encode_path_param(platform)}/{encode_path_param(activity_type)}/{encode_path_param(date_range)}/{encode_path_param(slot_filter)}/{encode_path_param(page)}/",
            method="GET",
            params={
                "excludeImmediate": exclude_immediate,
                "langFilter": lang_filter,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FireteamSearchPublicAvailableClanFireteamsResponse,
                    parse_obj_as(
                        type_=FireteamSearchPublicAvailableClanFireteamsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
