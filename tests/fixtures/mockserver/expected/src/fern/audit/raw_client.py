

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from .types.get_mockserver_audit_response_item import GetMockserverAuditResponseItem
from pydantic import ValidationError


class RawAuditClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def retrieve_the_control_plane_audit_log(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[GetMockserverAuditResponseItem]]:
        """
        Returns the most-recent control-plane audit entries (one per authorised control-plane mutation, newest first). Off by default — enable with controlPlaneAuditEnabled. Each entry records redacted, structural metadata only (method, control-plane path with query string dropped, logical operation, source address, best-effort principal, outcome); it never contains request headers or bodies.

        Parameters
        ----------
        limit : typing.Optional[int]
            maximum number of recent audit entries to return (default 200, capped at 1000)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetMockserverAuditResponseItem]]
            audit entries returned (newest first)
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/audit",
            method="GET",
            params={
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetMockserverAuditResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetMockserverAuditResponseItem],
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


class AsyncRawAuditClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def retrieve_the_control_plane_audit_log(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[GetMockserverAuditResponseItem]]:
        """
        Returns the most-recent control-plane audit entries (one per authorised control-plane mutation, newest first). Off by default — enable with controlPlaneAuditEnabled. Each entry records redacted, structural metadata only (method, control-plane path with query string dropped, logical operation, source address, best-effort principal, outcome); it never contains request headers or bodies.

        Parameters
        ----------
        limit : typing.Optional[int]
            maximum number of recent audit entries to return (default 200, capped at 1000)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetMockserverAuditResponseItem]]
            audit entries returned (newest first)
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/audit",
            method="GET",
            params={
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetMockserverAuditResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetMockserverAuditResponseItem],
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
