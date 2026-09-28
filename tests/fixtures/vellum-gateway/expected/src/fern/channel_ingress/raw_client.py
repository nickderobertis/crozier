

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.channel_ingress_approve_response import ChannelIngressApproveResponse
from .types.channel_ingress_list_response import ChannelIngressListResponse
from .types.channel_ingress_revoke_response import ChannelIngressRevokeResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawChannelIngressClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ChannelIngressListResponse]:
        """
        Every declaration the gateway can see, each with the digest a guardian would approve, the public paths it would open, and the credential its signatures are verified against. This is the only way to learn that a declaration is waiting: on the public surface a route held back by approval 404s exactly like one nobody declared.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChannelIngressListResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/channel-ingress",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChannelIngressListResponse,
                    parse_obj_as(
                        type_=ChannelIngressListResponse,
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

    def approve(
        self, source: str, *, digest: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ChannelIngressApproveResponse]:
        """
        Records the guardian's approval of the declaration identified by the body's digest, after which the gateway serves its routes. Returns 409 when the digest is not what the source currently declares, and 404 when it declares nothing servable.

        Parameters
        ----------
        source : str
            The declaring ingress source (today, a plugin name)

        digest : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChannelIngressApproveResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/channel-ingress/{encode_path_param(source)}/approve",
            method="POST",
            json={
                "digest": digest,
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
                    ChannelIngressApproveResponse,
                    parse_obj_as(
                        type_=ChannelIngressApproveResponse,
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

    def revoke(
        self, source: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ChannelIngressRevokeResponse]:
        """
        Withdraws the source's grant, after which its routes stop being served. Reports whether there was a grant to withdraw. Succeeds even when the declaration itself has become unreadable.

        Parameters
        ----------
        source : str
            The declaring ingress source (today, a plugin name)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChannelIngressRevokeResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/channel-ingress/{encode_path_param(source)}/revoke",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChannelIngressRevokeResponse,
                    parse_obj_as(
                        type_=ChannelIngressRevokeResponse,
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


class AsyncRawChannelIngressClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ChannelIngressListResponse]:
        """
        Every declaration the gateway can see, each with the digest a guardian would approve, the public paths it would open, and the credential its signatures are verified against. This is the only way to learn that a declaration is waiting: on the public surface a route held back by approval 404s exactly like one nobody declared.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChannelIngressListResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/channel-ingress",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChannelIngressListResponse,
                    parse_obj_as(
                        type_=ChannelIngressListResponse,
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

    async def approve(
        self, source: str, *, digest: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ChannelIngressApproveResponse]:
        """
        Records the guardian's approval of the declaration identified by the body's digest, after which the gateway serves its routes. Returns 409 when the digest is not what the source currently declares, and 404 when it declares nothing servable.

        Parameters
        ----------
        source : str
            The declaring ingress source (today, a plugin name)

        digest : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChannelIngressApproveResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/channel-ingress/{encode_path_param(source)}/approve",
            method="POST",
            json={
                "digest": digest,
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
                    ChannelIngressApproveResponse,
                    parse_obj_as(
                        type_=ChannelIngressApproveResponse,
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

    async def revoke(
        self, source: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ChannelIngressRevokeResponse]:
        """
        Withdraws the source's grant, after which its routes stop being served. Reports whether there was a grant to withdraw. Succeeds even when the declaration itself has become unreadable.

        Parameters
        ----------
        source : str
            The declaring ingress source (today, a plugin name)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChannelIngressRevokeResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/channel-ingress/{encode_path_param(source)}/revoke",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChannelIngressRevokeResponse,
                    parse_obj_as(
                        type_=ChannelIngressRevokeResponse,
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
