

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.conflict_error import ConflictError
from ..errors.gone_error import GoneError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error import Error
from .types.key_bind_response import KeyBindResponse
from .types.key_register_response import KeyRegisterResponse
from .types.key_retrieve_response import KeyRetrieveResponse
from .types.key_revoke_nosecret_response import KeyRevokeNosecretResponse
from .types.key_revoke_response import KeyRevokeResponse
from .types.key_update_response import KeyUpdateResponse


class RawKeyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def register(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[KeyRegisterResponse]:
        """
        Register a new ID `JWT(sub, devtoken)`

        v5: `JWT(sub, pk, devtoken, ...)`

        See: https://github.com/skion/authentiq/wiki/JWT-Examples

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[KeyRegisterResponse]
            Successfully registered
        """
        _response = self._client_wrapper.httpx_client.request(
            "key",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KeyRegisterResponse,
                    parse_obj_as(
                        type_=KeyRegisterResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def revoke_nosecret(
        self,
        *,
        email: str,
        phone: str,
        code: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[KeyRevokeNosecretResponse]:
        """
        Revoke an Authentiq ID using email & phone.

        If called with `email` and `phone` only, a verification code
        will be sent by email. Do a second call adding `code` to
        complete the revocation.

        Parameters
        ----------
        email : str
            primary email associated to Key (ID)

        phone : str
            primary phone number, international representation

        code : typing.Optional[str]
            verification code sent by email

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[KeyRevokeNosecretResponse]
            Successfully deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            "key",
            method="DELETE",
            params={
                "email": email,
                "phone": phone,
                "code": code,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KeyRevokeNosecretResponse,
                    parse_obj_as(
                        type_=KeyRevokeNosecretResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve(
        self, pk: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[KeyRetrieveResponse]:
        """
        Get public details of an Authentiq ID.

        Parameters
        ----------
        pk : str
            Public Signing Key - Authentiq ID (43 chars)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[KeyRetrieveResponse]
            Successfully retrieved
        """
        _response = self._client_wrapper.httpx_client.request(
            f"key/{jsonable_encoder(pk)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KeyRetrieveResponse,
                    parse_obj_as(
                        type_=KeyRetrieveResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update(
        self, pk: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[KeyUpdateResponse]:
        """
        update properties of an Authentiq ID.
        (not operational in v4; use PUT for now)

        v5: POST issuer-signed email & phone scopes in
        a self-signed JWT

        See: https://github.com/skion/authentiq/wiki/JWT-Examples

        Parameters
        ----------
        pk : str
            Public Signing Key - Authentiq ID (43 chars)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[KeyUpdateResponse]
            Successfully updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"key/{jsonable_encoder(pk)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KeyUpdateResponse,
                    parse_obj_as(
                        type_=KeyUpdateResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def bind(
        self, pk: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[KeyBindResponse]:
        """
        Update Authentiq ID by replacing the object.

        v4: `JWT(sub,email,phone)` to bind email/phone hash;

        v5: POST issuer-signed email & phone scopes
        and PUT to update registration `JWT(sub, pk, devtoken, ...)`

        See: https://github.com/skion/authentiq/wiki/JWT-Examples

        Parameters
        ----------
        pk : str
            Public Signing Key - Authentiq ID (43 chars)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[KeyBindResponse]
            Successfully updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"key/{jsonable_encoder(pk)}",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KeyBindResponse,
                    parse_obj_as(
                        type_=KeyBindResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def revoke(
        self, pk: str, *, secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[KeyRevokeResponse]:
        """
        Revoke an Identity (Key) with a revocation secret

        Parameters
        ----------
        pk : str
            Public Signing Key - Authentiq ID (43 chars)

        secret : str
            revokation secret

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[KeyRevokeResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"key/{jsonable_encoder(pk)}",
            method="DELETE",
            params={
                "secret": secret,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KeyRevokeResponse,
                    parse_obj_as(
                        type_=KeyRevokeResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def head_key_pk(self, pk: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        HEAD info on Authentiq ID

        Parameters
        ----------
        pk : str
            Public Signing Key - Authentiq ID (43 chars)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"key/{jsonable_encoder(pk)}",
            method="HEAD",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawKeyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def register(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[KeyRegisterResponse]:
        """
        Register a new ID `JWT(sub, devtoken)`

        v5: `JWT(sub, pk, devtoken, ...)`

        See: https://github.com/skion/authentiq/wiki/JWT-Examples

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[KeyRegisterResponse]
            Successfully registered
        """
        _response = await self._client_wrapper.httpx_client.request(
            "key",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KeyRegisterResponse,
                    parse_obj_as(
                        type_=KeyRegisterResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def revoke_nosecret(
        self,
        *,
        email: str,
        phone: str,
        code: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[KeyRevokeNosecretResponse]:
        """
        Revoke an Authentiq ID using email & phone.

        If called with `email` and `phone` only, a verification code
        will be sent by email. Do a second call adding `code` to
        complete the revocation.

        Parameters
        ----------
        email : str
            primary email associated to Key (ID)

        phone : str
            primary phone number, international representation

        code : typing.Optional[str]
            verification code sent by email

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[KeyRevokeNosecretResponse]
            Successfully deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            "key",
            method="DELETE",
            params={
                "email": email,
                "phone": phone,
                "code": code,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KeyRevokeNosecretResponse,
                    parse_obj_as(
                        type_=KeyRevokeNosecretResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve(
        self, pk: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[KeyRetrieveResponse]:
        """
        Get public details of an Authentiq ID.

        Parameters
        ----------
        pk : str
            Public Signing Key - Authentiq ID (43 chars)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[KeyRetrieveResponse]
            Successfully retrieved
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"key/{jsonable_encoder(pk)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KeyRetrieveResponse,
                    parse_obj_as(
                        type_=KeyRetrieveResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update(
        self, pk: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[KeyUpdateResponse]:
        """
        update properties of an Authentiq ID.
        (not operational in v4; use PUT for now)

        v5: POST issuer-signed email & phone scopes in
        a self-signed JWT

        See: https://github.com/skion/authentiq/wiki/JWT-Examples

        Parameters
        ----------
        pk : str
            Public Signing Key - Authentiq ID (43 chars)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[KeyUpdateResponse]
            Successfully updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"key/{jsonable_encoder(pk)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KeyUpdateResponse,
                    parse_obj_as(
                        type_=KeyUpdateResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def bind(
        self, pk: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[KeyBindResponse]:
        """
        Update Authentiq ID by replacing the object.

        v4: `JWT(sub,email,phone)` to bind email/phone hash;

        v5: POST issuer-signed email & phone scopes
        and PUT to update registration `JWT(sub, pk, devtoken, ...)`

        See: https://github.com/skion/authentiq/wiki/JWT-Examples

        Parameters
        ----------
        pk : str
            Public Signing Key - Authentiq ID (43 chars)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[KeyBindResponse]
            Successfully updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"key/{jsonable_encoder(pk)}",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KeyBindResponse,
                    parse_obj_as(
                        type_=KeyBindResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def revoke(
        self, pk: str, *, secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[KeyRevokeResponse]:
        """
        Revoke an Identity (Key) with a revocation secret

        Parameters
        ----------
        pk : str
            Public Signing Key - Authentiq ID (43 chars)

        secret : str
            revokation secret

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[KeyRevokeResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"key/{jsonable_encoder(pk)}",
            method="DELETE",
            params={
                "secret": secret,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KeyRevokeResponse,
                    parse_obj_as(
                        type_=KeyRevokeResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def head_key_pk(
        self, pk: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        HEAD info on Authentiq ID

        Parameters
        ----------
        pk : str
            Public Signing Key - Authentiq ID (43 chars)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"key/{jsonable_encoder(pk)}",
            method="HEAD",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
