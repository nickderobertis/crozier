

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.envelope_app_status_check import EnvelopeAppStatusCheck
from ..types.envelope_dict_str_any import EnvelopeDictStrAny
from ..types.envelope_health_info_dict import EnvelopeHealthInfoDict
from ..types.envelope_status_diagnostics_get import EnvelopeStatusDiagnosticsGet
from ..types.envelope_str import EnvelopeStr
from .raw_client import AsyncRawMaintenanceClient, RawMaintenanceClient


class MaintenanceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMaintenanceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMaintenanceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMaintenanceClient
        """
        return self._raw_client

    def healthcheck_readiness_probe(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeHealthInfoDict:
        """
        Readiness probe: check if the container is ready to receive traffic

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeHealthInfoDict
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.maintenance.healthcheck_readiness_probe()
        """
        _response = self._raw_client.healthcheck_readiness_probe(request_options=request_options)
        return _response.data

    def healthcheck_liveness_probe(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeDictStrAny:
        """
        Liveness probe: check if the container is alive

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeDictStrAny
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.maintenance.healthcheck_liveness_probe()
        """
        _response = self._raw_client.healthcheck_liveness_probe(request_options=request_options)
        return _response.data

    def get_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> EnvelopeDictStrAny:
        """
        Front end runtime configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeDictStrAny
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.maintenance.get_config()
        """
        _response = self._raw_client.get_config(request_options=request_options)
        return _response.data

    def get_scheduled_maintenance(self, *, request_options: typing.Optional[RequestOptions] = None) -> EnvelopeStr:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeStr
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.maintenance.get_scheduled_maintenance()
        """
        _response = self._raw_client.get_scheduled_maintenance(request_options=request_options)
        return _response.data

    def get_app_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> EnvelopeAppStatusCheck:
        """
        checks status of self and connected services

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeAppStatusCheck
            Returns app status check

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.maintenance.get_app_status()
        """
        _response = self._raw_client.get_app_status(request_options=request_options)
        return _response.data

    def get_app_diagnostics(
        self, *, top_tracemalloc: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeStatusDiagnosticsGet:
        """
        Parameters
        ----------
        top_tracemalloc : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeStatusDiagnosticsGet
            Returns app diagnostics report

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.maintenance.get_app_diagnostics()
        """
        _response = self._raw_client.get_app_diagnostics(
            top_tracemalloc=top_tracemalloc, request_options=request_options
        )
        return _response.data

    def get_service_status(
        self, service_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeAppStatusCheck:
        """
        Parameters
        ----------
        service_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeAppStatusCheck
            Returns app status check

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.maintenance.get_service_status(
            service_name="service_name",
        )
        """
        _response = self._raw_client.get_service_status(service_name, request_options=request_options)
        return _response.data


class AsyncMaintenanceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMaintenanceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMaintenanceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMaintenanceClient
        """
        return self._raw_client

    async def healthcheck_readiness_probe(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeHealthInfoDict:
        """
        Readiness probe: check if the container is ready to receive traffic

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeHealthInfoDict
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.maintenance.healthcheck_readiness_probe()


        asyncio.run(main())
        """
        _response = await self._raw_client.healthcheck_readiness_probe(request_options=request_options)
        return _response.data

    async def healthcheck_liveness_probe(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeDictStrAny:
        """
        Liveness probe: check if the container is alive

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeDictStrAny
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.maintenance.healthcheck_liveness_probe()


        asyncio.run(main())
        """
        _response = await self._raw_client.healthcheck_liveness_probe(request_options=request_options)
        return _response.data

    async def get_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> EnvelopeDictStrAny:
        """
        Front end runtime configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeDictStrAny
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.maintenance.get_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_config(request_options=request_options)
        return _response.data

    async def get_scheduled_maintenance(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeStr:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeStr
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.maintenance.get_scheduled_maintenance()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_scheduled_maintenance(request_options=request_options)
        return _response.data

    async def get_app_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeAppStatusCheck:
        """
        checks status of self and connected services

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeAppStatusCheck
            Returns app status check

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.maintenance.get_app_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_app_status(request_options=request_options)
        return _response.data

    async def get_app_diagnostics(
        self, *, top_tracemalloc: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeStatusDiagnosticsGet:
        """
        Parameters
        ----------
        top_tracemalloc : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeStatusDiagnosticsGet
            Returns app diagnostics report

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.maintenance.get_app_diagnostics()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_app_diagnostics(
            top_tracemalloc=top_tracemalloc, request_options=request_options
        )
        return _response.data

    async def get_service_status(
        self, service_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeAppStatusCheck:
        """
        Parameters
        ----------
        service_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeAppStatusCheck
            Returns app status check

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.maintenance.get_service_status(
                service_name="service_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_service_status(service_name, request_options=request_options)
        return _response.data
