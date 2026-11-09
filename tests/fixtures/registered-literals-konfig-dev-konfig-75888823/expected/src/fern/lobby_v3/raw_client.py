

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError as core_api_error_ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.api_error import ApiError as types_api_error_ApiError
from ..types.app_id import AppId
from ..types.lobby_v3 import LobbyV3
from ..types.lobby_visibility import LobbyVisibility
from ..types.region import Region
from ..types.room_config import RoomConfig
from ..types.room_id import RoomId
from ..types.short_code import ShortCode
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawLobbyV3Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_lobby(
        self,
        app_id: AppId,
        *,
        visibility: LobbyVisibility,
        region: Region,
        short_code: typing.Optional[ShortCode] = None,
        room_id: typing.Optional[RoomId] = None,
        room_config: typing.Optional[RoomConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LobbyV3]:
        """
        Create a new lobby for an [application](https://hathora.dev/docs/concepts/hathora-entities#application). A lobby object is a wrapper around a [room](https://hathora.dev/docs/concepts/hathora-entities#room) object. With a lobby, you get additional functionality like configuring the visibility of the room, managing the state of a match, and retrieving a list of public lobbies to display to players.

        Parameters
        ----------
        app_id : AppId

        visibility : LobbyVisibility

        region : Region

        short_code : typing.Optional[ShortCode]

        room_id : typing.Optional[RoomId]

        room_config : typing.Optional[RoomConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LobbyV3]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"lobby/v3/{encode_path_param(app_id)}/create",
            method="POST",
            params={
                "shortCode": short_code,
                "roomId": room_id,
            },
            json={
                "visibility": visibility,
                "roomConfig": room_config,
                "region": region,
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
                    LobbyV3,
                    parse_obj_as(
                        type_=LobbyV3,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )

    def list_active_public_lobbies(
        self,
        app_id: AppId,
        *,
        region: typing.Optional[Region] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[LobbyV3]]:
        """
        Get all active lobbies for a given [application](https://hathora.dev/docs/concepts/hathora-entities#application). Filter the array by optionally passing in a `region`. Use this endpoint to display all public lobbies that a player can join in the game client.

        Parameters
        ----------
        app_id : AppId

        region : typing.Optional[Region]
            If omitted, active public lobbies in all regions will be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[LobbyV3]]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            f"lobby/v3/{encode_path_param(app_id)}/list/public",
            method="GET",
            params={
                "region": region,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[LobbyV3],
                    parse_obj_as(
                        type_=typing.List[LobbyV3],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )

    def get_lobby_info_by_room_id(
        self, app_id: AppId, room_id: RoomId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[LobbyV3]:
        """
        Get details for a lobby.

        Parameters
        ----------
        app_id : AppId

        room_id : RoomId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LobbyV3]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            f"lobby/v3/{encode_path_param(app_id)}/info/roomid/{encode_path_param(room_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LobbyV3,
                    parse_obj_as(
                        type_=LobbyV3,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )

    def get_lobby_info_by_short_code(
        self, app_id: AppId, short_code: ShortCode, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[LobbyV3]:
        """
        Get details for a lobby. If 2 or more lobbies have the same `shortCode`, then the most recently created lobby will be returned.

        Parameters
        ----------
        app_id : AppId

        short_code : ShortCode

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LobbyV3]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            f"lobby/v3/{encode_path_param(app_id)}/info/shortcode/{encode_path_param(short_code)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LobbyV3,
                    parse_obj_as(
                        type_=LobbyV3,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )


class AsyncRawLobbyV3Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_lobby(
        self,
        app_id: AppId,
        *,
        visibility: LobbyVisibility,
        region: Region,
        short_code: typing.Optional[ShortCode] = None,
        room_id: typing.Optional[RoomId] = None,
        room_config: typing.Optional[RoomConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LobbyV3]:
        """
        Create a new lobby for an [application](https://hathora.dev/docs/concepts/hathora-entities#application). A lobby object is a wrapper around a [room](https://hathora.dev/docs/concepts/hathora-entities#room) object. With a lobby, you get additional functionality like configuring the visibility of the room, managing the state of a match, and retrieving a list of public lobbies to display to players.

        Parameters
        ----------
        app_id : AppId

        visibility : LobbyVisibility

        region : Region

        short_code : typing.Optional[ShortCode]

        room_id : typing.Optional[RoomId]

        room_config : typing.Optional[RoomConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LobbyV3]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"lobby/v3/{encode_path_param(app_id)}/create",
            method="POST",
            params={
                "shortCode": short_code,
                "roomId": room_id,
            },
            json={
                "visibility": visibility,
                "roomConfig": room_config,
                "region": region,
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
                    LobbyV3,
                    parse_obj_as(
                        type_=LobbyV3,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )

    async def list_active_public_lobbies(
        self,
        app_id: AppId,
        *,
        region: typing.Optional[Region] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[LobbyV3]]:
        """
        Get all active lobbies for a given [application](https://hathora.dev/docs/concepts/hathora-entities#application). Filter the array by optionally passing in a `region`. Use this endpoint to display all public lobbies that a player can join in the game client.

        Parameters
        ----------
        app_id : AppId

        region : typing.Optional[Region]
            If omitted, active public lobbies in all regions will be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[LobbyV3]]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"lobby/v3/{encode_path_param(app_id)}/list/public",
            method="GET",
            params={
                "region": region,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[LobbyV3],
                    parse_obj_as(
                        type_=typing.List[LobbyV3],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )

    async def get_lobby_info_by_room_id(
        self, app_id: AppId, room_id: RoomId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[LobbyV3]:
        """
        Get details for a lobby.

        Parameters
        ----------
        app_id : AppId

        room_id : RoomId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LobbyV3]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"lobby/v3/{encode_path_param(app_id)}/info/roomid/{encode_path_param(room_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LobbyV3,
                    parse_obj_as(
                        type_=LobbyV3,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )

    async def get_lobby_info_by_short_code(
        self, app_id: AppId, short_code: ShortCode, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[LobbyV3]:
        """
        Get details for a lobby. If 2 or more lobbies have the same `shortCode`, then the most recently created lobby will be returned.

        Parameters
        ----------
        app_id : AppId

        short_code : ShortCode

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LobbyV3]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"lobby/v3/{encode_path_param(app_id)}/info/shortcode/{encode_path_param(short_code)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LobbyV3,
                    parse_obj_as(
                        type_=LobbyV3,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )
