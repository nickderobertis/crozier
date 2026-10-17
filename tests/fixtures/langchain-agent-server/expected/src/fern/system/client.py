

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSystemClient, RawSystemClient
from .types.health_check_ok_get_response import HealthCheckOkGetResponse
from .types.server_info_info_get_response import ServerInfoInfoGetResponse
from .types.system_metrics_metrics_get_request_format import SystemMetricsMetricsGetRequestFormat


class SystemClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSystemClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSystemClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSystemClient
        """
        return self._raw_client

    def server_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> ServerInfoInfoGetResponse:
        """
        Get server version information, feature flags, and metadata.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServerInfoInfoGetResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.system.server_info()
        """
        _response = self._raw_client.server_info(request_options=request_options)
        return _response.data

    def system_metrics(
        self,
        *,
        format: typing.Optional[SystemMetricsMetricsGetRequestFormat] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Get system metrics in Prometheus or JSON format for monitoring and observability.

        Parameters
        ----------
        format : typing.Optional[SystemMetricsMetricsGetRequestFormat]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.system.system_metrics()
        """
        _response = self._raw_client.system_metrics(format=format, request_options=request_options)
        return _response.data

    def docs_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        A local reference to the Agent Server API documentation.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.system.docs_get()
        """
        _response = self._raw_client.docs_get(request_options=request_options)
        return _response.data

    def health_check(
        self, *, check_db: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HealthCheckOkGetResponse:
        """
        Check the health status of the server. Optionally check database connectivity.

        Parameters
        ----------
        check_db : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthCheckOkGetResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.system.health_check()
        """
        _response = self._raw_client.health_check(check_db=check_db, request_options=request_options)
        return _response.data


class AsyncSystemClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSystemClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSystemClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSystemClient
        """
        return self._raw_client

    async def server_info(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServerInfoInfoGetResponse:
        """
        Get server version information, feature flags, and metadata.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServerInfoInfoGetResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.system.server_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.server_info(request_options=request_options)
        return _response.data

    async def system_metrics(
        self,
        *,
        format: typing.Optional[SystemMetricsMetricsGetRequestFormat] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Get system metrics in Prometheus or JSON format for monitoring and observability.

        Parameters
        ----------
        format : typing.Optional[SystemMetricsMetricsGetRequestFormat]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.system.system_metrics()


        asyncio.run(main())
        """
        _response = await self._raw_client.system_metrics(format=format, request_options=request_options)
        return _response.data

    async def docs_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        A local reference to the Agent Server API documentation.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.system.docs_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.docs_get(request_options=request_options)
        return _response.data

    async def health_check(
        self, *, check_db: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HealthCheckOkGetResponse:
        """
        Check the health status of the server. Optionally check database connectivity.

        Parameters
        ----------
        check_db : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthCheckOkGetResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.system.health_check()


        asyncio.run(main())
        """
        _response = await self._raw_client.health_check(check_db=check_db, request_options=request_options)
        return _response.data
