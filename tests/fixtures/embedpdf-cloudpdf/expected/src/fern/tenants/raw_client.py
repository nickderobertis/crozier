

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
from ..errors.not_found_error import NotFoundError
from ..types.tenants_create200response import TenantsCreate200Response
from ..types.tenants_get200response import TenantsGet200Response
from ..types.tenants_list200response import TenantsList200Response
from ..types.tenants_usage200response import TenantsUsage200Response
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTenantsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TenantsList200Response]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TenantsList200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/tenants",
            method="GET",
            params={
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TenantsList200Response,
                    parse_obj_as(
                        type_=TenantsList200Response,
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
        self, *, id: str, name: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TenantsCreate200Response]:
        """
        Parameters
        ----------
        id : str

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TenantsCreate200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/tenants",
            method="POST",
            json={
                "id": id,
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
                    TenantsCreate200Response,
                    parse_obj_as(
                        type_=TenantsCreate200Response,
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

    def get(
        self, tenant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TenantsGet200Response]:
        """
        Parameters
        ----------
        tenant_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TenantsGet200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TenantsGet200Response,
                    parse_obj_as(
                        type_=TenantsGet200Response,
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

    def delete(self, tenant_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Destroys the tenant and everything in its namespace — documents, layers, stored bytes, audit history. Irreversible.

        Parameters
        ----------
        tenant_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}",
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

    def resume(self, tenant_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Parameters
        ----------
        tenant_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/resume",
            method="POST",
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

    def suspend(
        self,
        tenant_id: str,
        *,
        reason: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Instantly reversible with resume. The API token is exempt, so a suspended tenant can still be inspected, exported, resumed, or deleted.

        Parameters
        ----------
        tenant_id : str

        reason : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/suspend",
            method="POST",
            json={
                "reason": reason,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    def usage(
        self,
        tenant_id: str,
        *,
        period: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TenantsUsage200Response]:
        """
        Facts only — no limits or billing state. Views count share exchanges plus authorized /v1/access grants, deduplicated across the two.

        Parameters
        ----------
        tenant_id : str

        period : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TenantsUsage200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/usage",
            method="GET",
            params={
                "period": period,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TenantsUsage200Response,
                    parse_obj_as(
                        type_=TenantsUsage200Response,
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


class AsyncRawTenantsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TenantsList200Response]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TenantsList200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/tenants",
            method="GET",
            params={
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TenantsList200Response,
                    parse_obj_as(
                        type_=TenantsList200Response,
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
        self, *, id: str, name: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TenantsCreate200Response]:
        """
        Parameters
        ----------
        id : str

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TenantsCreate200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/tenants",
            method="POST",
            json={
                "id": id,
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
                    TenantsCreate200Response,
                    parse_obj_as(
                        type_=TenantsCreate200Response,
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

    async def get(
        self, tenant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TenantsGet200Response]:
        """
        Parameters
        ----------
        tenant_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TenantsGet200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TenantsGet200Response,
                    parse_obj_as(
                        type_=TenantsGet200Response,
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
        self, tenant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Destroys the tenant and everything in its namespace — documents, layers, stored bytes, audit history. Irreversible.

        Parameters
        ----------
        tenant_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}",
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

    async def resume(
        self, tenant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        tenant_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/resume",
            method="POST",
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

    async def suspend(
        self,
        tenant_id: str,
        *,
        reason: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Instantly reversible with resume. The API token is exempt, so a suspended tenant can still be inspected, exported, resumed, or deleted.

        Parameters
        ----------
        tenant_id : str

        reason : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/suspend",
            method="POST",
            json={
                "reason": reason,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    async def usage(
        self,
        tenant_id: str,
        *,
        period: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TenantsUsage200Response]:
        """
        Facts only — no limits or billing state. Views count share exchanges plus authorized /v1/access grants, deduplicated across the two.

        Parameters
        ----------
        tenant_id : str

        period : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TenantsUsage200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/usage",
            method="GET",
            params={
                "period": period,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TenantsUsage200Response,
                    parse_obj_as(
                        type_=TenantsUsage200Response,
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
