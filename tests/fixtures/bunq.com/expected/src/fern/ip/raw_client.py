

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.permitted_ip_create import PermittedIpCreate
from ..types.permitted_ip_listing import PermittedIpListing
from ..types.permitted_ip_read import PermittedIpRead
from ..types.permitted_ip_update import PermittedIpUpdate


OMIT = typing.cast(typing.Any, ...)


class RawIpClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_ip_for_user_credential_password_ip(
        self, user_id: int, credential_password_ip_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[PermittedIpListing]]:
        """
        Manage the IPs which may be used for a credential of a user for server authentication.

        Parameters
        ----------
        user_id : int


        credential_password_ip_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[PermittedIpListing]]
            Manage the IPs which may be used for a credential of a user for server authentication.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/credential-password-ip/{jsonable_encoder(credential_password_ip_id)}/ip",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PermittedIpListing],
                    parse_obj_as(
                        type_=typing.List[PermittedIpListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_ip_for_user_credential_password_ip(
        self,
        user_id: int,
        credential_password_ip_id: int,
        *,
        ip: str,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PermittedIpCreate]:
        """
        Manage the IPs which may be used for a credential of a user for server authentication.

        Parameters
        ----------
        user_id : int


        credential_password_ip_id : int


        ip : str
            The IP address.

        status : typing.Optional[str]
            The status of the IP. May be "ACTIVE" or "INACTIVE". It is only possible to make requests from "ACTIVE" IP addresses. Only "ACTIVE" IPs will be billed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PermittedIpCreate]
            Manage the IPs which may be used for a credential of a user for server authentication.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/credential-password-ip/{jsonable_encoder(credential_password_ip_id)}/ip",
            method="POST",
            json={
                "ip": ip,
                "status": status,
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
                    PermittedIpCreate,
                    parse_obj_as(
                        type_=PermittedIpCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_ip_for_user_credential_password_ip(
        self,
        user_id: int,
        credential_password_ip_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PermittedIpRead]:
        """
        Manage the IPs which may be used for a credential of a user for server authentication.

        Parameters
        ----------
        user_id : int


        credential_password_ip_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PermittedIpRead]
            Manage the IPs which may be used for a credential of a user for server authentication.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/credential-password-ip/{jsonable_encoder(credential_password_ip_id)}/ip/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PermittedIpRead,
                    parse_obj_as(
                        type_=PermittedIpRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_ip_for_user_credential_password_ip(
        self,
        user_id: int,
        credential_password_ip_id: int,
        item_id: int,
        *,
        ip: str,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PermittedIpUpdate]:
        """
        Manage the IPs which may be used for a credential of a user for server authentication.

        Parameters
        ----------
        user_id : int


        credential_password_ip_id : int


        item_id : int


        ip : str
            The IP address.

        status : typing.Optional[str]
            The status of the IP. May be "ACTIVE" or "INACTIVE". It is only possible to make requests from "ACTIVE" IP addresses. Only "ACTIVE" IPs will be billed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PermittedIpUpdate]
            Manage the IPs which may be used for a credential of a user for server authentication.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/credential-password-ip/{jsonable_encoder(credential_password_ip_id)}/ip/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "ip": ip,
                "status": status,
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
                    PermittedIpUpdate,
                    parse_obj_as(
                        type_=PermittedIpUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawIpClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_ip_for_user_credential_password_ip(
        self, user_id: int, credential_password_ip_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[PermittedIpListing]]:
        """
        Manage the IPs which may be used for a credential of a user for server authentication.

        Parameters
        ----------
        user_id : int


        credential_password_ip_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[PermittedIpListing]]
            Manage the IPs which may be used for a credential of a user for server authentication.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/credential-password-ip/{jsonable_encoder(credential_password_ip_id)}/ip",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PermittedIpListing],
                    parse_obj_as(
                        type_=typing.List[PermittedIpListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_ip_for_user_credential_password_ip(
        self,
        user_id: int,
        credential_password_ip_id: int,
        *,
        ip: str,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PermittedIpCreate]:
        """
        Manage the IPs which may be used for a credential of a user for server authentication.

        Parameters
        ----------
        user_id : int


        credential_password_ip_id : int


        ip : str
            The IP address.

        status : typing.Optional[str]
            The status of the IP. May be "ACTIVE" or "INACTIVE". It is only possible to make requests from "ACTIVE" IP addresses. Only "ACTIVE" IPs will be billed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PermittedIpCreate]
            Manage the IPs which may be used for a credential of a user for server authentication.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/credential-password-ip/{jsonable_encoder(credential_password_ip_id)}/ip",
            method="POST",
            json={
                "ip": ip,
                "status": status,
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
                    PermittedIpCreate,
                    parse_obj_as(
                        type_=PermittedIpCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_ip_for_user_credential_password_ip(
        self,
        user_id: int,
        credential_password_ip_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PermittedIpRead]:
        """
        Manage the IPs which may be used for a credential of a user for server authentication.

        Parameters
        ----------
        user_id : int


        credential_password_ip_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PermittedIpRead]
            Manage the IPs which may be used for a credential of a user for server authentication.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/credential-password-ip/{jsonable_encoder(credential_password_ip_id)}/ip/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PermittedIpRead,
                    parse_obj_as(
                        type_=PermittedIpRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_ip_for_user_credential_password_ip(
        self,
        user_id: int,
        credential_password_ip_id: int,
        item_id: int,
        *,
        ip: str,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PermittedIpUpdate]:
        """
        Manage the IPs which may be used for a credential of a user for server authentication.

        Parameters
        ----------
        user_id : int


        credential_password_ip_id : int


        item_id : int


        ip : str
            The IP address.

        status : typing.Optional[str]
            The status of the IP. May be "ACTIVE" or "INACTIVE". It is only possible to make requests from "ACTIVE" IP addresses. Only "ACTIVE" IPs will be billed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PermittedIpUpdate]
            Manage the IPs which may be used for a credential of a user for server authentication.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/credential-password-ip/{jsonable_encoder(credential_password_ip_id)}/ip/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "ip": ip,
                "status": status,
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
                    PermittedIpUpdate,
                    parse_obj_as(
                        type_=PermittedIpUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
