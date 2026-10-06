

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .errors.unprocessable_entity_error import UnprocessableEntityError
from .types.check_asset_for_work_orders_get_response import CheckAssetForWorkOrdersGetResponse
from .types.check_multiple_assets_for_work_orders_get_response import CheckMultipleAssetsForWorkOrdersGetResponse
from .types.create_work_order_get_response import CreateWorkOrderGetResponse
from .types.get_unhealthy_assets_get_response import GetUnhealthyAssetsGetResponse
from .types.login_token_post_response import LoginTokenPostResponse
from .types.unprocessable_entity_error_body import UnprocessableEntityErrorBody
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def login_token_post(
        self,
        *,
        username: str,
        password: str,
        grant_type: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LoginTokenPostResponse]:
        """
        Parameters
        ----------
        username : str
            The username of the user

        password : str
            The password of the user

        grant_type : typing.Optional[str]
            Grant type

        scope : typing.Optional[str]
            The scope of the user

        client_id : typing.Optional[str]
            The client id of the user

        client_secret : typing.Optional[str]
            The client id of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LoginTokenPostResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "token",
            method="POST",
            json={
                "grant_type": grant_type,
                "username": username,
                "password": password,
                "scope": scope,
                "client_id": client_id,
                "client_secret": client_secret,
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
                    LoginTokenPostResponse,
                    parse_obj_as(
                        type_=LoginTokenPostResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableEntityErrorBody,
                        parse_obj_as(
                            type_=UnprocessableEntityErrorBody,
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

    def read_users_me_users_me_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "users/me",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    def hello_world_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    def read_items_items_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "items/",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    def get_unhealthy_assets_get(
        self, *, x_access_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetUnhealthyAssetsGetResponse]:
        """
        Parameters
        ----------
        x_access_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetUnhealthyAssetsGetResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "get_unhealthy_assets",
            method="GET",
            params={
                "x_access_token": x_access_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetUnhealthyAssetsGetResponse,
                    parse_obj_as(
                        type_=GetUnhealthyAssetsGetResponse,
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

    def create_work_order_get(
        self,
        *,
        x_access_token: str,
        asset_number: str,
        site_id: str,
        description: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateWorkOrderGetResponse]:
        """
        Parameters
        ----------
        x_access_token : str

        asset_number : str

        site_id : str

        description : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateWorkOrderGetResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "create_work_order",
            method="GET",
            params={
                "x_access_token": x_access_token,
                "asset_number": asset_number,
                "site_id": site_id,
                "description": description,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateWorkOrderGetResponse,
                    parse_obj_as(
                        type_=CreateWorkOrderGetResponse,
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

    def check_asset_for_work_orders_get(
        self, *, x_access_token: str, asset_number: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CheckAssetForWorkOrdersGetResponse]:
        """
        Parameters
        ----------
        x_access_token : str

        asset_number : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CheckAssetForWorkOrdersGetResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "check_asset_for_work_orders",
            method="GET",
            params={
                "x_access_token": x_access_token,
                "asset_number": asset_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckAssetForWorkOrdersGetResponse,
                    parse_obj_as(
                        type_=CheckAssetForWorkOrdersGetResponse,
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

    def check_multiple_assets_for_work_orders_get(
        self,
        *,
        x_access_token: str,
        comma_separated_asset_list: str,
        comma_separated_asset_uid_list: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CheckMultipleAssetsForWorkOrdersGetResponse]:
        """
        Parameters
        ----------
        x_access_token : str

        comma_separated_asset_list : str

        comma_separated_asset_uid_list : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CheckMultipleAssetsForWorkOrdersGetResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "check_multiple_assets_for_work_orders",
            method="GET",
            params={
                "x_access_token": x_access_token,
                "comma_separated_asset_list": comma_separated_asset_list,
                "comma_separated_asset_uid_list": comma_separated_asset_uid_list,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckMultipleAssetsForWorkOrdersGetResponse,
                    parse_obj_as(
                        type_=CheckMultipleAssetsForWorkOrdersGetResponse,
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def login_token_post(
        self,
        *,
        username: str,
        password: str,
        grant_type: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LoginTokenPostResponse]:
        """
        Parameters
        ----------
        username : str
            The username of the user

        password : str
            The password of the user

        grant_type : typing.Optional[str]
            Grant type

        scope : typing.Optional[str]
            The scope of the user

        client_id : typing.Optional[str]
            The client id of the user

        client_secret : typing.Optional[str]
            The client id of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LoginTokenPostResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "token",
            method="POST",
            json={
                "grant_type": grant_type,
                "username": username,
                "password": password,
                "scope": scope,
                "client_id": client_id,
                "client_secret": client_secret,
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
                    LoginTokenPostResponse,
                    parse_obj_as(
                        type_=LoginTokenPostResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableEntityErrorBody,
                        parse_obj_as(
                            type_=UnprocessableEntityErrorBody,
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

    async def read_users_me_users_me_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/me",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    async def hello_world_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    async def read_items_items_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "items/",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    async def get_unhealthy_assets_get(
        self, *, x_access_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetUnhealthyAssetsGetResponse]:
        """
        Parameters
        ----------
        x_access_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetUnhealthyAssetsGetResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "get_unhealthy_assets",
            method="GET",
            params={
                "x_access_token": x_access_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetUnhealthyAssetsGetResponse,
                    parse_obj_as(
                        type_=GetUnhealthyAssetsGetResponse,
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

    async def create_work_order_get(
        self,
        *,
        x_access_token: str,
        asset_number: str,
        site_id: str,
        description: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateWorkOrderGetResponse]:
        """
        Parameters
        ----------
        x_access_token : str

        asset_number : str

        site_id : str

        description : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateWorkOrderGetResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "create_work_order",
            method="GET",
            params={
                "x_access_token": x_access_token,
                "asset_number": asset_number,
                "site_id": site_id,
                "description": description,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateWorkOrderGetResponse,
                    parse_obj_as(
                        type_=CreateWorkOrderGetResponse,
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

    async def check_asset_for_work_orders_get(
        self, *, x_access_token: str, asset_number: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CheckAssetForWorkOrdersGetResponse]:
        """
        Parameters
        ----------
        x_access_token : str

        asset_number : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CheckAssetForWorkOrdersGetResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "check_asset_for_work_orders",
            method="GET",
            params={
                "x_access_token": x_access_token,
                "asset_number": asset_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckAssetForWorkOrdersGetResponse,
                    parse_obj_as(
                        type_=CheckAssetForWorkOrdersGetResponse,
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

    async def check_multiple_assets_for_work_orders_get(
        self,
        *,
        x_access_token: str,
        comma_separated_asset_list: str,
        comma_separated_asset_uid_list: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CheckMultipleAssetsForWorkOrdersGetResponse]:
        """
        Parameters
        ----------
        x_access_token : str

        comma_separated_asset_list : str

        comma_separated_asset_uid_list : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CheckMultipleAssetsForWorkOrdersGetResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "check_multiple_assets_for_work_orders",
            method="GET",
            params={
                "x_access_token": x_access_token,
                "comma_separated_asset_list": comma_separated_asset_list,
                "comma_separated_asset_uid_list": comma_separated_asset_uid_list,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckMultipleAssetsForWorkOrdersGetResponse,
                    parse_obj_as(
                        type_=CheckMultipleAssetsForWorkOrdersGetResponse,
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
