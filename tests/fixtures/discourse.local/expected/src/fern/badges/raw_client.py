

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.admin_list_badges_response import AdminListBadgesResponse
from .types.create_badge_response import CreateBadgeResponse
from .types.list_user_badges_response import ListUserBadgesResponse
from .types.update_badge_response import UpdateBadgeResponse


OMIT = typing.cast(typing.Any, ...)


class RawBadgesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def admin_list_badges(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AdminListBadgesResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AdminListBadgesResponse]
            success response
        """
        _response = self._client_wrapper.httpx_client.request(
            "admin/badges.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AdminListBadgesResponse,
                    parse_obj_as(
                        type_=AdminListBadgesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_badge(
        self, *, badge_type_id: int, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CreateBadgeResponse]:
        """
        Parameters
        ----------
        badge_type_id : int
            The ID for the badge type. 1 for Gold, 2 for Silver,
            3 for Bronze.

        name : str
            The name for the new badge.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateBadgeResponse]
            success response
        """
        _response = self._client_wrapper.httpx_client.request(
            "admin/badges.json",
            method="POST",
            json={
                "badge_type_id": badge_type_id,
                "name": name,
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
                    CreateBadgeResponse,
                    parse_obj_as(
                        type_=CreateBadgeResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_badge(
        self, id: int, *, badge_type_id: int, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UpdateBadgeResponse]:
        """
        Parameters
        ----------
        id : int

        badge_type_id : int
            The ID for the badge type. 1 for Gold, 2 for Silver,
            3 for Bronze.

        name : str
            The name for the new badge.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateBadgeResponse]
            success response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"admin/badges/{jsonable_encoder(id)}.json",
            method="PUT",
            json={
                "badge_type_id": badge_type_id,
                "name": name,
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
                    UpdateBadgeResponse,
                    parse_obj_as(
                        type_=UpdateBadgeResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_badge(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"admin/badges/{jsonable_encoder(id)}.json",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_user_badges(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListUserBadgesResponse]:
        """
        Parameters
        ----------
        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListUserBadgesResponse]
            success response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user-badges/{jsonable_encoder(username)}.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListUserBadgesResponse,
                    parse_obj_as(
                        type_=ListUserBadgesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawBadgesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def admin_list_badges(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AdminListBadgesResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AdminListBadgesResponse]
            success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "admin/badges.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AdminListBadgesResponse,
                    parse_obj_as(
                        type_=AdminListBadgesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_badge(
        self, *, badge_type_id: int, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CreateBadgeResponse]:
        """
        Parameters
        ----------
        badge_type_id : int
            The ID for the badge type. 1 for Gold, 2 for Silver,
            3 for Bronze.

        name : str
            The name for the new badge.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateBadgeResponse]
            success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "admin/badges.json",
            method="POST",
            json={
                "badge_type_id": badge_type_id,
                "name": name,
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
                    CreateBadgeResponse,
                    parse_obj_as(
                        type_=CreateBadgeResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_badge(
        self, id: int, *, badge_type_id: int, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UpdateBadgeResponse]:
        """
        Parameters
        ----------
        id : int

        badge_type_id : int
            The ID for the badge type. 1 for Gold, 2 for Silver,
            3 for Bronze.

        name : str
            The name for the new badge.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateBadgeResponse]
            success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"admin/badges/{jsonable_encoder(id)}.json",
            method="PUT",
            json={
                "badge_type_id": badge_type_id,
                "name": name,
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
                    UpdateBadgeResponse,
                    parse_obj_as(
                        type_=UpdateBadgeResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_badge(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"admin/badges/{jsonable_encoder(id)}.json",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_user_badges(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListUserBadgesResponse]:
        """
        Parameters
        ----------
        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListUserBadgesResponse]
            success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user-badges/{jsonable_encoder(username)}.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListUserBadgesResponse,
                    parse_obj_as(
                        type_=ListUserBadgesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
