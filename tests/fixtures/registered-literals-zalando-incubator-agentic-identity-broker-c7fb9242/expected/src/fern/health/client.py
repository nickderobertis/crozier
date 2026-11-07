

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.health_response import HealthResponse
from .raw_client import AsyncRawHealthClient, RawHealthClient


class HealthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawHealthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawHealthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawHealthClient
        """
        return self._raw_client

    def get_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> HealthResponse:
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
        HealthResponse
            Server is healthy and accepting requests

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )
        client.health.get_health()
        """
        _response = self._raw_client.get_health(request_options=request_options)
        return _response.data


class AsyncHealthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawHealthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawHealthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawHealthClient
        """
        return self._raw_client

    async def get_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> HealthResponse:
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
        HealthResponse
            Server is healthy and accepting requests

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.health.get_health()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_health(request_options=request_options)
        return _response.data
