

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.internal_server_error import InternalServerError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.app_filter import AppFilter
from ..types.apps_include import AppsInclude
from ..types.config_filter import ConfigFilter
from ..types.config_include import ConfigInclude
from ..types.config_rank import ConfigRank
from ..types.error_model import ErrorModel
from ..types.search_response_body import SearchResponseBody
from .types.post_v1search_configs_response import PostV1SearchConfigsResponse
from .types.post_v1search_games_response import PostV1SearchGamesResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSearchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search_steam_games_and_configurations_all_at_once(
        self,
        *,
        search_term: str,
        limit: typing.Optional[int] = OMIT,
        limit_configs: typing.Optional[int] = OMIT,
        limit_games: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SearchResponseBody]:
        """
        Search for games that are available on Steam
        **and** Search for SteamInput configurations for Steam and non-Steam games
        **all at once**

        This endpoint supports no pagination and has pretty strict limits, it's intended for the "main-page" of the Frontend only

        Parameters
        ----------
        search_term : str

        limit : typing.Optional[int]

        limit_configs : typing.Optional[int]

        limit_games : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SearchResponseBody]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/search/",
            method="POST",
            json={
                "limit": limit,
                "limit_configs": limit_configs,
                "limit_games": limit_games,
                "search_term": search_term,
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
                    SearchResponseBody,
                    parse_obj_as(
                        type_=SearchResponseBody,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    def search_steam_input_configurations(
        self,
        *,
        query_text: str,
        filter: typing.Optional[ConfigFilter] = OMIT,
        include: typing.Optional[ConfigInclude] = OMIT,
        limit: typing.Optional[int] = OMIT,
        page: typing.Optional[int] = OMIT,
        rank: typing.Optional[ConfigRank] = OMIT,
        raw: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV1SearchConfigsResponse]:
        """
        Search for SteamInput configurations for Steam and non-Steam games

        Parameters
        ----------
        query_text : str
            The search query string

        filter : typing.Optional[ConfigFilter]

        include : typing.Optional[ConfigInclude]

        limit : typing.Optional[int]
            Maximum number of results to return

        page : typing.Optional[int]
            Page number for paginated results

        rank : typing.Optional[ConfigRank]

        raw : typing.Optional[bool]
            Return raw Steam API response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV1SearchConfigsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/search/configs",
            method="POST",
            json={
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=ConfigFilter, direction="write"
                ),
                "include": convert_and_respect_annotation_metadata(
                    object_=include, annotation=ConfigInclude, direction="write"
                ),
                "limit": limit,
                "page": page,
                "query_text": query_text,
                "rank": convert_and_respect_annotation_metadata(object_=rank, annotation=ConfigRank, direction="write"),
                "raw": raw,
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
                    PostV1SearchConfigsResponse,
                    parse_obj_as(
                        type_=PostV1SearchConfigsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    def search_steam_games(
        self,
        *,
        query_text: str,
        filter: typing.Optional[AppFilter] = OMIT,
        include: typing.Optional[AppsInclude] = OMIT,
        limit: typing.Optional[int] = OMIT,
        raw: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV1SearchGamesResponse]:
        """
        Search for games that are available on Steam

        Parameters
        ----------
        query_text : str
            The search query string

        filter : typing.Optional[AppFilter]

        include : typing.Optional[AppsInclude]

        limit : typing.Optional[int]
            Maximum number of results to return

        raw : typing.Optional[bool]
            Return raw Steam API response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV1SearchGamesResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/search/games",
            method="POST",
            json={
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=AppFilter, direction="write"
                ),
                "include": convert_and_respect_annotation_metadata(
                    object_=include, annotation=AppsInclude, direction="write"
                ),
                "limit": limit,
                "query_text": query_text,
                "raw": raw,
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
                    PostV1SearchGamesResponse,
                    parse_obj_as(
                        type_=PostV1SearchGamesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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


class AsyncRawSearchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search_steam_games_and_configurations_all_at_once(
        self,
        *,
        search_term: str,
        limit: typing.Optional[int] = OMIT,
        limit_configs: typing.Optional[int] = OMIT,
        limit_games: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SearchResponseBody]:
        """
        Search for games that are available on Steam
        **and** Search for SteamInput configurations for Steam and non-Steam games
        **all at once**

        This endpoint supports no pagination and has pretty strict limits, it's intended for the "main-page" of the Frontend only

        Parameters
        ----------
        search_term : str

        limit : typing.Optional[int]

        limit_configs : typing.Optional[int]

        limit_games : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SearchResponseBody]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/search/",
            method="POST",
            json={
                "limit": limit,
                "limit_configs": limit_configs,
                "limit_games": limit_games,
                "search_term": search_term,
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
                    SearchResponseBody,
                    parse_obj_as(
                        type_=SearchResponseBody,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    async def search_steam_input_configurations(
        self,
        *,
        query_text: str,
        filter: typing.Optional[ConfigFilter] = OMIT,
        include: typing.Optional[ConfigInclude] = OMIT,
        limit: typing.Optional[int] = OMIT,
        page: typing.Optional[int] = OMIT,
        rank: typing.Optional[ConfigRank] = OMIT,
        raw: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV1SearchConfigsResponse]:
        """
        Search for SteamInput configurations for Steam and non-Steam games

        Parameters
        ----------
        query_text : str
            The search query string

        filter : typing.Optional[ConfigFilter]

        include : typing.Optional[ConfigInclude]

        limit : typing.Optional[int]
            Maximum number of results to return

        page : typing.Optional[int]
            Page number for paginated results

        rank : typing.Optional[ConfigRank]

        raw : typing.Optional[bool]
            Return raw Steam API response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV1SearchConfigsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/search/configs",
            method="POST",
            json={
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=ConfigFilter, direction="write"
                ),
                "include": convert_and_respect_annotation_metadata(
                    object_=include, annotation=ConfigInclude, direction="write"
                ),
                "limit": limit,
                "page": page,
                "query_text": query_text,
                "rank": convert_and_respect_annotation_metadata(object_=rank, annotation=ConfigRank, direction="write"),
                "raw": raw,
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
                    PostV1SearchConfigsResponse,
                    parse_obj_as(
                        type_=PostV1SearchConfigsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    async def search_steam_games(
        self,
        *,
        query_text: str,
        filter: typing.Optional[AppFilter] = OMIT,
        include: typing.Optional[AppsInclude] = OMIT,
        limit: typing.Optional[int] = OMIT,
        raw: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV1SearchGamesResponse]:
        """
        Search for games that are available on Steam

        Parameters
        ----------
        query_text : str
            The search query string

        filter : typing.Optional[AppFilter]

        include : typing.Optional[AppsInclude]

        limit : typing.Optional[int]
            Maximum number of results to return

        raw : typing.Optional[bool]
            Return raw Steam API response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV1SearchGamesResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/search/games",
            method="POST",
            json={
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=AppFilter, direction="write"
                ),
                "include": convert_and_respect_annotation_metadata(
                    object_=include, annotation=AppsInclude, direction="write"
                ),
                "limit": limit,
                "query_text": query_text,
                "raw": raw,
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
                    PostV1SearchGamesResponse,
                    parse_obj_as(
                        type_=PostV1SearchGamesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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
