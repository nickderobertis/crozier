

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_gateway_error import BadGatewayError
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.app_info_item import AppInfoItem
from ..types.error_model import ErrorModel
from ..types.login_response import LoginResponse
from ..types.user_info_response import UserInfoResponse
from .types.get_v1steam_filedetails_response import GetV1SteamFiledetailsResponse
from .types.open_id_body_mode import OpenIdBodyMode
from .types.post_v1steam_login_request_openid_mode import PostV1SteamLoginRequestOpenidMode
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSteamClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_steam_app_info(
        self,
        *,
        app_id: int,
        raw: typing.Optional[bool] = None,
        controller_support: typing.Optional[bool] = None,
        official_configs: typing.Optional[bool] = None,
        force_refresh: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AppInfoItem]:
        """
        Retrieve app information from Steam Store for a given app ID

        Parameters
        ----------
        app_id : int

        raw : typing.Optional[bool]

        controller_support : typing.Optional[bool]

        official_configs : typing.Optional[bool]

        force_refresh : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AppInfoItem]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/steam/appinfo",
            method="GET",
            params={
                "app_id": app_id,
                "raw": raw,
                "controller_support": controller_support,
                "official_configs": official_configs,
                "force_refresh": force_refresh,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AppInfoItem,
                    parse_obj_as(
                        type_=AppInfoItem,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 502:
                raise BadGatewayError(
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

    def get_controller_config_details(
        self,
        *,
        file_id: int,
        playtime_stats: typing.Optional[int] = None,
        raw: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetV1SteamFiledetailsResponse]:
        """

        Retrieve details for a given controller config file ID.
        If a non-controller config file ID is provided, this will respond with a 404

        Parameters
        ----------
        file_id : int

        playtime_stats : typing.Optional[int]
            Number of days for playtime statistics

        raw : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetV1SteamFiledetailsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/steam/filedetails",
            method="GET",
            params={
                "file_id": file_id,
                "playtime_stats": playtime_stats,
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetV1SteamFiledetailsResponse,
                    parse_obj_as(
                        type_=GetV1SteamFiledetailsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 502:
                raise BadGatewayError(
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

    def log_in_with_steam(
        self,
        *,
        assoc_handle: str,
        claimed_id: str,
        identity: str,
        mode: OpenIdBodyMode,
        ns: str,
        op_endpoint: str,
        response_nonce: str,
        return_to: str,
        sig: str,
        signed: str,
        openid_ns: typing.Optional[str] = None,
        openid_mode: typing.Optional[PostV1SteamLoginRequestOpenidMode] = None,
        openid_op_endpoint: typing.Optional[str] = None,
        openid_claimed_id: typing.Optional[str] = None,
        openid_identity: typing.Optional[str] = None,
        openid_return_to: typing.Optional[str] = None,
        openid_response_nonce: typing.Optional[str] = None,
        openid_assoc_handle: typing.Optional[str] = None,
        openid_signed: typing.Optional[str] = None,
        openid_sig: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LoginResponse]:
        """
        Authenticate user via Steam OpenID and return JWT token
                    Wrapper endpoint for SSR frontend

        Parameters
        ----------
        assoc_handle : str

        claimed_id : str

        identity : str

        mode : OpenIdBodyMode

        ns : str

        op_endpoint : str

        response_nonce : str

        return_to : str

        sig : str

        signed : str

        openid_ns : typing.Optional[str]

        openid_mode : typing.Optional[PostV1SteamLoginRequestOpenidMode]

        openid_op_endpoint : typing.Optional[str]

        openid_claimed_id : typing.Optional[str]

        openid_identity : typing.Optional[str]

        openid_return_to : typing.Optional[str]

        openid_response_nonce : typing.Optional[str]

        openid_assoc_handle : typing.Optional[str]

        openid_signed : typing.Optional[str]

        openid_sig : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LoginResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/steam/login",
            method="POST",
            params={
                "openid.ns": openid_ns,
                "openid.mode": openid_mode,
                "openid.op_endpoint": openid_op_endpoint,
                "openid.claimed_id": openid_claimed_id,
                "openid.identity": openid_identity,
                "openid.return_to": openid_return_to,
                "openid.response_nonce": openid_response_nonce,
                "openid.assoc_handle": openid_assoc_handle,
                "openid.signed": openid_signed,
                "openid.sig": openid_sig,
            },
            json={
                "assoc_handle": assoc_handle,
                "claimed_id": claimed_id,
                "identity": identity,
                "mode": mode,
                "ns": ns,
                "op_endpoint": op_endpoint,
                "response_nonce": response_nonce,
                "return_to": return_to,
                "sig": sig,
                "signed": signed,
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
                    LoginResponse,
                    parse_obj_as(
                        type_=LoginResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 502:
                raise BadGatewayError(
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

    def get_steam_user_info(
        self,
        *,
        user_id: typing.Optional[str] = None,
        include_avatar_frame: typing.Optional[bool] = None,
        include_profile_background: typing.Optional[bool] = None,
        include_mini_profile_background: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UserInfoResponse]:
        """
        Retrieve user information from Steam for the provided userId,
        or for attempt authenticated user if no userId is provided
        Returns 401 if no id provided and token is invalid and 400 if everything is missing

        Parameters
        ----------
        user_id : typing.Optional[str]

        include_avatar_frame : typing.Optional[bool]

        include_profile_background : typing.Optional[bool]

        include_mini_profile_background : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserInfoResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/steam/userinfo",
            method="GET",
            params={
                "user_id": user_id,
                "include_avatar_frame": include_avatar_frame,
                "include_profile_background": include_profile_background,
                "include_mini_profile_background": include_mini_profile_background,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserInfoResponse,
                    parse_obj_as(
                        type_=UserInfoResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 502:
                raise BadGatewayError(
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


class AsyncRawSteamClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_steam_app_info(
        self,
        *,
        app_id: int,
        raw: typing.Optional[bool] = None,
        controller_support: typing.Optional[bool] = None,
        official_configs: typing.Optional[bool] = None,
        force_refresh: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AppInfoItem]:
        """
        Retrieve app information from Steam Store for a given app ID

        Parameters
        ----------
        app_id : int

        raw : typing.Optional[bool]

        controller_support : typing.Optional[bool]

        official_configs : typing.Optional[bool]

        force_refresh : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AppInfoItem]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/steam/appinfo",
            method="GET",
            params={
                "app_id": app_id,
                "raw": raw,
                "controller_support": controller_support,
                "official_configs": official_configs,
                "force_refresh": force_refresh,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AppInfoItem,
                    parse_obj_as(
                        type_=AppInfoItem,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 502:
                raise BadGatewayError(
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

    async def get_controller_config_details(
        self,
        *,
        file_id: int,
        playtime_stats: typing.Optional[int] = None,
        raw: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetV1SteamFiledetailsResponse]:
        """

        Retrieve details for a given controller config file ID.
        If a non-controller config file ID is provided, this will respond with a 404

        Parameters
        ----------
        file_id : int

        playtime_stats : typing.Optional[int]
            Number of days for playtime statistics

        raw : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetV1SteamFiledetailsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/steam/filedetails",
            method="GET",
            params={
                "file_id": file_id,
                "playtime_stats": playtime_stats,
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetV1SteamFiledetailsResponse,
                    parse_obj_as(
                        type_=GetV1SteamFiledetailsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 502:
                raise BadGatewayError(
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

    async def log_in_with_steam(
        self,
        *,
        assoc_handle: str,
        claimed_id: str,
        identity: str,
        mode: OpenIdBodyMode,
        ns: str,
        op_endpoint: str,
        response_nonce: str,
        return_to: str,
        sig: str,
        signed: str,
        openid_ns: typing.Optional[str] = None,
        openid_mode: typing.Optional[PostV1SteamLoginRequestOpenidMode] = None,
        openid_op_endpoint: typing.Optional[str] = None,
        openid_claimed_id: typing.Optional[str] = None,
        openid_identity: typing.Optional[str] = None,
        openid_return_to: typing.Optional[str] = None,
        openid_response_nonce: typing.Optional[str] = None,
        openid_assoc_handle: typing.Optional[str] = None,
        openid_signed: typing.Optional[str] = None,
        openid_sig: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LoginResponse]:
        """
        Authenticate user via Steam OpenID and return JWT token
                    Wrapper endpoint for SSR frontend

        Parameters
        ----------
        assoc_handle : str

        claimed_id : str

        identity : str

        mode : OpenIdBodyMode

        ns : str

        op_endpoint : str

        response_nonce : str

        return_to : str

        sig : str

        signed : str

        openid_ns : typing.Optional[str]

        openid_mode : typing.Optional[PostV1SteamLoginRequestOpenidMode]

        openid_op_endpoint : typing.Optional[str]

        openid_claimed_id : typing.Optional[str]

        openid_identity : typing.Optional[str]

        openid_return_to : typing.Optional[str]

        openid_response_nonce : typing.Optional[str]

        openid_assoc_handle : typing.Optional[str]

        openid_signed : typing.Optional[str]

        openid_sig : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LoginResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/steam/login",
            method="POST",
            params={
                "openid.ns": openid_ns,
                "openid.mode": openid_mode,
                "openid.op_endpoint": openid_op_endpoint,
                "openid.claimed_id": openid_claimed_id,
                "openid.identity": openid_identity,
                "openid.return_to": openid_return_to,
                "openid.response_nonce": openid_response_nonce,
                "openid.assoc_handle": openid_assoc_handle,
                "openid.signed": openid_signed,
                "openid.sig": openid_sig,
            },
            json={
                "assoc_handle": assoc_handle,
                "claimed_id": claimed_id,
                "identity": identity,
                "mode": mode,
                "ns": ns,
                "op_endpoint": op_endpoint,
                "response_nonce": response_nonce,
                "return_to": return_to,
                "sig": sig,
                "signed": signed,
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
                    LoginResponse,
                    parse_obj_as(
                        type_=LoginResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 502:
                raise BadGatewayError(
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

    async def get_steam_user_info(
        self,
        *,
        user_id: typing.Optional[str] = None,
        include_avatar_frame: typing.Optional[bool] = None,
        include_profile_background: typing.Optional[bool] = None,
        include_mini_profile_background: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UserInfoResponse]:
        """
        Retrieve user information from Steam for the provided userId,
        or for attempt authenticated user if no userId is provided
        Returns 401 if no id provided and token is invalid and 400 if everything is missing

        Parameters
        ----------
        user_id : typing.Optional[str]

        include_avatar_frame : typing.Optional[bool]

        include_profile_background : typing.Optional[bool]

        include_mini_profile_background : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserInfoResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/steam/userinfo",
            method="GET",
            params={
                "user_id": user_id,
                "include_avatar_frame": include_avatar_frame,
                "include_profile_background": include_profile_background,
                "include_mini_profile_background": include_mini_profile_background,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserInfoResponse,
                    parse_obj_as(
                        type_=UserInfoResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 502:
                raise BadGatewayError(
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
