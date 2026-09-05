

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..types.generic_error import GenericError
from ..types.remote_networks_ipsec_tunnel import RemoteNetworksIpsecTunnel
from ..types.remote_networks_read_result import RemoteNetworksReadResult
from ..types.remote_networks_response import RemoteNetworksResponse
from ..types.uuid_response import UuidResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRemoteNetworksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_v1remote_networks(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RemoteNetworksResponse]:
        """
        Get remote networks IPSec tunnel details for create, modify, or delete by ID.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RemoteNetworksResponse]
            Remote networks IPSEC tunnel details.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/remote-networks",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RemoteNetworksResponse,
                    parse_obj_as(
                        type_=RemoteNetworksResponse,
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

    def post_v1remote_networks(
        self,
        *,
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        remote_networks_ipsec_tunnels: typing.Optional[typing.Sequence[RemoteNetworksIpsecTunnel]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UuidResponse]:
        """
        Create  remote network IPSec tunnels.

        Parameters
        ----------
        name : str
            provide a name to use as a suffix for bulk operations

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        remote_networks_ipsec_tunnels : typing.Optional[typing.Sequence[RemoteNetworksIpsecTunnel]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UuidResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/remote-networks",
            method="POST",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "name": name,
                "remote_networks_ipsec_tunnels": convert_and_respect_annotation_metadata(
                    object_=remote_networks_ipsec_tunnels,
                    annotation=typing.Sequence[RemoteNetworksIpsecTunnel],
                    direction="write",
                ),
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
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    def put_v1remote_networks(
        self,
        *,
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        remote_networks_ipsec_tunnels: typing.Optional[typing.Sequence[RemoteNetworksIpsecTunnel]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UuidResponse]:
        """
        Modify remote network IPSec tunnels.

        Parameters
        ----------
        name : str
            provide a name to use as a suffix for bulk operations

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        remote_networks_ipsec_tunnels : typing.Optional[typing.Sequence[RemoteNetworksIpsecTunnel]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UuidResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/remote-networks",
            method="PUT",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "name": name,
                "remote_networks_ipsec_tunnels": convert_and_respect_annotation_metadata(
                    object_=remote_networks_ipsec_tunnels,
                    annotation=typing.Sequence[RemoteNetworksIpsecTunnel],
                    direction="write",
                ),
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
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    def delete_v1remote_networks(
        self,
        *,
        remote_networks_prefix: str,
        sub_tenant_name: typing.Optional[str] = None,
        name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UuidResponse]:
        """
        Allows you to delete the set of IPSec tunnels.

        Parameters
        ----------
        remote_networks_prefix : str
            remote networks prefix for bulk deletion

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of remote networks along with their names.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UuidResponse]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/remote-networks",
            method="DELETE",
            params={
                "SubTenantName": sub_tenant_name,
                "remote_networks_prefix": remote_networks_prefix,
                "Name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    def get_v1remote_networks_read(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RemoteNetworksReadResult]:
        """
        Read the remote networks IPSec tunnel status by UUID.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RemoteNetworksReadResult]
            Get the remote networks IPSEC tunnel status by UUID.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/remote-networks-read",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RemoteNetworksReadResult,
                    parse_obj_as(
                        type_=RemoteNetworksReadResult,
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

    def post_v1remote_networks_read(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        remote_networks_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UuidResponse]:
        """
        Create a request to read remote network IPSec tunnels.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        remote_networks_names : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UuidResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/remote-networks-read",
            method="POST",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "remote_networks_names": remote_networks_names,
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
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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


class AsyncRawRemoteNetworksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_v1remote_networks(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RemoteNetworksResponse]:
        """
        Get remote networks IPSec tunnel details for create, modify, or delete by ID.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RemoteNetworksResponse]
            Remote networks IPSEC tunnel details.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/remote-networks",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RemoteNetworksResponse,
                    parse_obj_as(
                        type_=RemoteNetworksResponse,
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

    async def post_v1remote_networks(
        self,
        *,
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        remote_networks_ipsec_tunnels: typing.Optional[typing.Sequence[RemoteNetworksIpsecTunnel]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UuidResponse]:
        """
        Create  remote network IPSec tunnels.

        Parameters
        ----------
        name : str
            provide a name to use as a suffix for bulk operations

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        remote_networks_ipsec_tunnels : typing.Optional[typing.Sequence[RemoteNetworksIpsecTunnel]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UuidResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/remote-networks",
            method="POST",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "name": name,
                "remote_networks_ipsec_tunnels": convert_and_respect_annotation_metadata(
                    object_=remote_networks_ipsec_tunnels,
                    annotation=typing.Sequence[RemoteNetworksIpsecTunnel],
                    direction="write",
                ),
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
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    async def put_v1remote_networks(
        self,
        *,
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        remote_networks_ipsec_tunnels: typing.Optional[typing.Sequence[RemoteNetworksIpsecTunnel]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UuidResponse]:
        """
        Modify remote network IPSec tunnels.

        Parameters
        ----------
        name : str
            provide a name to use as a suffix for bulk operations

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        remote_networks_ipsec_tunnels : typing.Optional[typing.Sequence[RemoteNetworksIpsecTunnel]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UuidResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/remote-networks",
            method="PUT",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "name": name,
                "remote_networks_ipsec_tunnels": convert_and_respect_annotation_metadata(
                    object_=remote_networks_ipsec_tunnels,
                    annotation=typing.Sequence[RemoteNetworksIpsecTunnel],
                    direction="write",
                ),
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
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    async def delete_v1remote_networks(
        self,
        *,
        remote_networks_prefix: str,
        sub_tenant_name: typing.Optional[str] = None,
        name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UuidResponse]:
        """
        Allows you to delete the set of IPSec tunnels.

        Parameters
        ----------
        remote_networks_prefix : str
            remote networks prefix for bulk deletion

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of remote networks along with their names.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UuidResponse]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/remote-networks",
            method="DELETE",
            params={
                "SubTenantName": sub_tenant_name,
                "remote_networks_prefix": remote_networks_prefix,
                "Name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    async def get_v1remote_networks_read(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RemoteNetworksReadResult]:
        """
        Read the remote networks IPSec tunnel status by UUID.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RemoteNetworksReadResult]
            Get the remote networks IPSEC tunnel status by UUID.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/remote-networks-read",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RemoteNetworksReadResult,
                    parse_obj_as(
                        type_=RemoteNetworksReadResult,
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

    async def post_v1remote_networks_read(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        remote_networks_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UuidResponse]:
        """
        Create a request to read remote network IPSec tunnels.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        remote_networks_names : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UuidResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/remote-networks-read",
            method="POST",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "remote_networks_names": remote_networks_names,
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
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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
