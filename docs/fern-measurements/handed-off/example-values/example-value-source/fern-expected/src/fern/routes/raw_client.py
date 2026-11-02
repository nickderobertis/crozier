

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.plan_routes_response import PlanRoutesResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRoutesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def plan_routes(
        self, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PlanRoutesResponse]:
        """
        An array body's schema-level example.

        Parameters
        ----------
        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PlanRoutesResponse]
            Planned
        """
        _response = self._client_wrapper.httpx_client.request(
            "routes",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PlanRoutesResponse,
                    parse_obj_as(
                        type_=PlanRoutesResponse,
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


class AsyncRawRoutesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def plan_routes(
        self, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PlanRoutesResponse]:
        """
        An array body's schema-level example.

        Parameters
        ----------
        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PlanRoutesResponse]
            Planned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "routes",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PlanRoutesResponse,
                    parse_obj_as(
                        type_=PlanRoutesResponse,
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
