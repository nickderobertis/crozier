

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.gone_error import GoneError
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.shares_create200response import SharesCreate200Response
from ..types.shares_exchange200response import SharesExchange200Response
from ..types.shares_exchange410response import SharesExchange410Response
from ..types.shares_exchange422response import SharesExchange422Response
from ..types.shares_get200response import SharesGet200Response
from ..types.shares_list200response import SharesList200Response
from ..types.shares_update200response import SharesUpdate200Response
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSharesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def exchange(
        self,
        *,
        share_token: str,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SharesExchange200Response]:
        """
        Unauthenticated, but requires a browser Origin header, checked against the grant allowlist. Unknown, revoked, and disabled tokens are indistinguishable (404). Passphrase-protected grants return 422 SharePasswordRequired until `password` is supplied. Mounted only when the deployment can sign (HS256 mode).

        Parameters
        ----------
        share_token : str

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SharesExchange200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/share-sessions",
            method="POST",
            json={
                "shareToken": share_token,
                "password": password,
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
                    SharesExchange200Response,
                    parse_obj_as(
                        type_=SharesExchange200Response,
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
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        SharesExchange410Response,
                        parse_obj_as(
                            type_=SharesExchange410Response,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        SharesExchange422Response,
                        parse_obj_as(
                            type_=SharesExchange422Response,
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

    def list(
        self,
        tenant_id: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        doc_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SharesList200Response]:
        """
        Parameters
        ----------
        tenant_id : str

        limit : typing.Optional[int]

        cursor : typing.Optional[str]

        doc_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SharesList200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/shares",
            method="GET",
            params={
                "limit": limit,
                "cursor": cursor,
                "docId": doc_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SharesList200Response,
                    parse_obj_as(
                        type_=SharesList200Response,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create(
        self,
        tenant_id: str,
        *,
        doc_id: str,
        scope: typing.Sequence[str],
        layer_name: typing.Optional[str] = OMIT,
        origins: typing.Optional[typing.Sequence[str]] = OMIT,
        password: typing.Optional[str] = OMIT,
        session_ttl_seconds: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SharesCreate200Response]:
        """
        The returned share id IS the public share token. Mounted only when the deployment can sign (HS256 mode) — exchange mints session JWTs, so grants exist only where minting does.

        Parameters
        ----------
        tenant_id : str

        doc_id : str

        scope : typing.Sequence[str]

        layer_name : typing.Optional[str]

        origins : typing.Optional[typing.Sequence[str]]

        password : typing.Optional[str]

        session_ttl_seconds : typing.Optional[int]

        expires_at : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SharesCreate200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/shares",
            method="POST",
            json={
                "docId": doc_id,
                "layerName": layer_name,
                "scope": scope,
                "origins": origins,
                "password": password,
                "sessionTtlSeconds": session_ttl_seconds,
                "expiresAt": expires_at,
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
                    SharesCreate200Response,
                    parse_obj_as(
                        type_=SharesCreate200Response,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get(
        self, tenant_id: str, share_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SharesGet200Response]:
        """
        Parameters
        ----------
        tenant_id : str

        share_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SharesGet200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/shares/{encode_path_param(share_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SharesGet200Response,
                    parse_obj_as(
                        type_=SharesGet200Response,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete(
        self, tenant_id: str, share_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        tenant_id : str

        share_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/shares/{encode_path_param(share_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update(
        self,
        tenant_id: str,
        share_id: str,
        *,
        scope: typing.Optional[typing.Sequence[str]] = OMIT,
        origins: typing.Optional[typing.Sequence[str]] = OMIT,
        password: typing.Optional[str] = OMIT,
        session_ttl_seconds: typing.Optional[int] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        expires_at: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SharesUpdate200Response]:
        """
        Parameters
        ----------
        tenant_id : str

        share_id : str

        scope : typing.Optional[typing.Sequence[str]]

        origins : typing.Optional[typing.Sequence[str]]

        password : typing.Optional[str]

        session_ttl_seconds : typing.Optional[int]

        disabled : typing.Optional[bool]

        expires_at : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SharesUpdate200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/shares/{encode_path_param(share_id)}",
            method="PATCH",
            json={
                "scope": scope,
                "origins": origins,
                "password": password,
                "sessionTtlSeconds": session_ttl_seconds,
                "disabled": disabled,
                "expiresAt": expires_at,
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
                    SharesUpdate200Response,
                    parse_obj_as(
                        type_=SharesUpdate200Response,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawSharesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def exchange(
        self,
        *,
        share_token: str,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SharesExchange200Response]:
        """
        Unauthenticated, but requires a browser Origin header, checked against the grant allowlist. Unknown, revoked, and disabled tokens are indistinguishable (404). Passphrase-protected grants return 422 SharePasswordRequired until `password` is supplied. Mounted only when the deployment can sign (HS256 mode).

        Parameters
        ----------
        share_token : str

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SharesExchange200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/share-sessions",
            method="POST",
            json={
                "shareToken": share_token,
                "password": password,
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
                    SharesExchange200Response,
                    parse_obj_as(
                        type_=SharesExchange200Response,
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
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        SharesExchange410Response,
                        parse_obj_as(
                            type_=SharesExchange410Response,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        SharesExchange422Response,
                        parse_obj_as(
                            type_=SharesExchange422Response,
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

    async def list(
        self,
        tenant_id: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        doc_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SharesList200Response]:
        """
        Parameters
        ----------
        tenant_id : str

        limit : typing.Optional[int]

        cursor : typing.Optional[str]

        doc_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SharesList200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/shares",
            method="GET",
            params={
                "limit": limit,
                "cursor": cursor,
                "docId": doc_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SharesList200Response,
                    parse_obj_as(
                        type_=SharesList200Response,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create(
        self,
        tenant_id: str,
        *,
        doc_id: str,
        scope: typing.Sequence[str],
        layer_name: typing.Optional[str] = OMIT,
        origins: typing.Optional[typing.Sequence[str]] = OMIT,
        password: typing.Optional[str] = OMIT,
        session_ttl_seconds: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SharesCreate200Response]:
        """
        The returned share id IS the public share token. Mounted only when the deployment can sign (HS256 mode) — exchange mints session JWTs, so grants exist only where minting does.

        Parameters
        ----------
        tenant_id : str

        doc_id : str

        scope : typing.Sequence[str]

        layer_name : typing.Optional[str]

        origins : typing.Optional[typing.Sequence[str]]

        password : typing.Optional[str]

        session_ttl_seconds : typing.Optional[int]

        expires_at : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SharesCreate200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/shares",
            method="POST",
            json={
                "docId": doc_id,
                "layerName": layer_name,
                "scope": scope,
                "origins": origins,
                "password": password,
                "sessionTtlSeconds": session_ttl_seconds,
                "expiresAt": expires_at,
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
                    SharesCreate200Response,
                    parse_obj_as(
                        type_=SharesCreate200Response,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get(
        self, tenant_id: str, share_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SharesGet200Response]:
        """
        Parameters
        ----------
        tenant_id : str

        share_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SharesGet200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/shares/{encode_path_param(share_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SharesGet200Response,
                    parse_obj_as(
                        type_=SharesGet200Response,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete(
        self, tenant_id: str, share_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        tenant_id : str

        share_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/shares/{encode_path_param(share_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update(
        self,
        tenant_id: str,
        share_id: str,
        *,
        scope: typing.Optional[typing.Sequence[str]] = OMIT,
        origins: typing.Optional[typing.Sequence[str]] = OMIT,
        password: typing.Optional[str] = OMIT,
        session_ttl_seconds: typing.Optional[int] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        expires_at: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SharesUpdate200Response]:
        """
        Parameters
        ----------
        tenant_id : str

        share_id : str

        scope : typing.Optional[typing.Sequence[str]]

        origins : typing.Optional[typing.Sequence[str]]

        password : typing.Optional[str]

        session_ttl_seconds : typing.Optional[int]

        disabled : typing.Optional[bool]

        expires_at : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SharesUpdate200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/shares/{encode_path_param(share_id)}",
            method="PATCH",
            json={
                "scope": scope,
                "origins": origins,
                "password": password,
                "sessionTtlSeconds": session_ttl_seconds,
                "disabled": disabled,
                "expiresAt": expires_at,
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
                    SharesUpdate200Response,
                    parse_obj_as(
                        type_=SharesUpdate200Response,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
