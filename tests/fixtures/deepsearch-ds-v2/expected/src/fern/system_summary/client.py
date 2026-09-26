

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.cps_summary import CpsSummary
from ..types.storage_summary_task import StorageSummaryTask
from .raw_client import AsyncRawSystemSummaryClient, RawSystemSummaryClient


class SystemSummaryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSystemSummaryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSystemSummaryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSystemSummaryClient
        """
        return self._raw_client

    def system_get_kg_storage_summary_async(
        self, kg_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StorageSummaryTask:
        """
        Get knowledge graph storage summary.

        Parameters
        ----------
        kg_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StorageSummaryTask
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.system_summary.system_get_kg_storage_summary_async(
            kg_key="kg_key",
        )
        """
        _response = self._raw_client.system_get_kg_storage_summary_async(kg_key, request_options=request_options)
        return _response.data

    def system_get_dc_storage_summary_async(
        self, dc_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StorageSummaryTask:
        """
        Get data catalog storage summary.

        Parameters
        ----------
        dc_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StorageSummaryTask
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.system_summary.system_get_dc_storage_summary_async(
            dc_key="dc_key",
        )
        """
        _response = self._raw_client.system_get_dc_storage_summary_async(dc_key, request_options=request_options)
        return _response.data

    def system_get_cps_summary(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CpsSummary]:
        """
        Get cps summary data.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CpsSummary]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.system_summary.system_get_cps_summary()
        """
        _response = self._raw_client.system_get_cps_summary(request_options=request_options)
        return _response.data


class AsyncSystemSummaryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSystemSummaryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSystemSummaryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSystemSummaryClient
        """
        return self._raw_client

    async def system_get_kg_storage_summary_async(
        self, kg_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StorageSummaryTask:
        """
        Get knowledge graph storage summary.

        Parameters
        ----------
        kg_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StorageSummaryTask
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.system_summary.system_get_kg_storage_summary_async(
                kg_key="kg_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.system_get_kg_storage_summary_async(kg_key, request_options=request_options)
        return _response.data

    async def system_get_dc_storage_summary_async(
        self, dc_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StorageSummaryTask:
        """
        Get data catalog storage summary.

        Parameters
        ----------
        dc_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StorageSummaryTask
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.system_summary.system_get_dc_storage_summary_async(
                dc_key="dc_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.system_get_dc_storage_summary_async(dc_key, request_options=request_options)
        return _response.data

    async def system_get_cps_summary(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CpsSummary]:
        """
        Get cps summary data.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CpsSummary]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.system_summary.system_get_cps_summary()


        asyncio.run(main())
        """
        _response = await self._raw_client.system_get_cps_summary(request_options=request_options)
        return _response.data
