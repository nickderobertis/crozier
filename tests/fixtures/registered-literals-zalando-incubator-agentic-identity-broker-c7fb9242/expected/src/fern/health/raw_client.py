

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..types.health_response import HealthResponse
from pydantic import ValidationError


class RawHealthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[HealthResponse]:
        """
        Returns the current health status of the end-user HTTP server.

        This endpoint does not require authentication and is intended for:

        - Load balancer health checks
        - Kubernetes liveness/readiness probes
        - Monitoring systems
        - Service discovery health validation

        **Status Codes**:

        - `200 OK`: Server is healthy and accepting requests
        - `503 Service Unavailable`: Server is starting, shutting down, or unhealthy

        **Health States**:

        - `healthy`: Server is operational and processing requests normally
        - `starting`: Server is initializing (binding to port, setting up routes)
        - `shutting_down`: Graceful shutdown in progress, completing in-flight requests
        - `unhealthy`: Server encountered an error and requires restart

        In proxy and hybrid OAuth2 modes, the response may also include component-level health in `components`. The `upstream_jwks` component reports `healthy` or `degraded` without changing the top-level server lifecycle status.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[HealthResponse]
            Server is healthy and accepting requests
        """
        _response = self._client_wrapper.httpx_client.request(
            "health",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    HealthResponse,
                    parse_obj_as(
                        type_=HealthResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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


class AsyncRawHealthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[HealthResponse]:
        """
        Returns the current health status of the end-user HTTP server.

        This endpoint does not require authentication and is intended for:

        - Load balancer health checks
        - Kubernetes liveness/readiness probes
        - Monitoring systems
        - Service discovery health validation

        **Status Codes**:

        - `200 OK`: Server is healthy and accepting requests
        - `503 Service Unavailable`: Server is starting, shutting down, or unhealthy

        **Health States**:

        - `healthy`: Server is operational and processing requests normally
        - `starting`: Server is initializing (binding to port, setting up routes)
        - `shutting_down`: Graceful shutdown in progress, completing in-flight requests
        - `unhealthy`: Server encountered an error and requires restart

        In proxy and hybrid OAuth2 modes, the response may also include component-level health in `components`. The `upstream_jwks` component reports `healthy` or `degraded` without changing the top-level server lifecycle status.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[HealthResponse]
            Server is healthy and accepting requests
        """
        _response = await self._client_wrapper.httpx_client.request(
            "health",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    HealthResponse,
                    parse_obj_as(
                        type_=HealthResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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
