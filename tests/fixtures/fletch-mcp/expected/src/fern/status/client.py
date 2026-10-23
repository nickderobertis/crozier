

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawStatusClient, RawStatusClient
from .types.get_chains_chain_id_status_response import GetChainsChainIdStatusResponse
from .types.get_status_response import GetStatusResponse


class StatusClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStatusClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStatusClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStatusClient
        """
        return self._raw_client

    def whether_the_registry_is_live_the_daemons_heartbeat_every_job_against_its_cadence_the_scanners_still_reading_history_and_the_age_of_every_published_figure(
        self, chain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetChainsChainIdStatusResponse:
        """
        Public. Always 200; the verdict is in the body ('live', 'degraded', 'stale', 'never'), so a stale registry is a fact to read rather than an error to retry. Each job carries its cadence, last successful run, age and verdict ('fresh', 'late', 'failing', 'filling', 'stalled', 'never'); metadataBacklog reports the measured due, visible, never-read and failed token counts after the last successful metadata batch; filling does not mean complete coverage; each figure names the job that writes it and the newest timestamp behind it. Also served at /api/v1/status.

        Parameters
        ----------
        chain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChainsChainIdStatusResponse
            Freshness

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.status.whether_the_registry_is_live_the_daemons_heartbeat_every_job_against_its_cadence_the_scanners_still_reading_history_and_the_age_of_every_published_figure(
            chain_id=1,
        )
        """
        _response = self._raw_client.whether_the_registry_is_live_the_daemons_heartbeat_every_job_against_its_cadence_the_scanners_still_reading_history_and_the_age_of_every_published_figure(
            chain_id, request_options=request_options
        )
        return _response.data

    def alias_of_chains4663status_whether_the_registry_is_live(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetStatusResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStatusResponse
            Freshness

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.status.alias_of_chains4663status_whether_the_registry_is_live()
        """
        _response = self._raw_client.alias_of_chains4663status_whether_the_registry_is_live(
            request_options=request_options
        )
        return _response.data


class AsyncStatusClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStatusClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStatusClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStatusClient
        """
        return self._raw_client

    async def whether_the_registry_is_live_the_daemons_heartbeat_every_job_against_its_cadence_the_scanners_still_reading_history_and_the_age_of_every_published_figure(
        self, chain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetChainsChainIdStatusResponse:
        """
        Public. Always 200; the verdict is in the body ('live', 'degraded', 'stale', 'never'), so a stale registry is a fact to read rather than an error to retry. Each job carries its cadence, last successful run, age and verdict ('fresh', 'late', 'failing', 'filling', 'stalled', 'never'); metadataBacklog reports the measured due, visible, never-read and failed token counts after the last successful metadata batch; filling does not mean complete coverage; each figure names the job that writes it and the newest timestamp behind it. Also served at /api/v1/status.

        Parameters
        ----------
        chain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChainsChainIdStatusResponse
            Freshness

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.status.whether_the_registry_is_live_the_daemons_heartbeat_every_job_against_its_cadence_the_scanners_still_reading_history_and_the_age_of_every_published_figure(
                chain_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.whether_the_registry_is_live_the_daemons_heartbeat_every_job_against_its_cadence_the_scanners_still_reading_history_and_the_age_of_every_published_figure(
            chain_id, request_options=request_options
        )
        return _response.data

    async def alias_of_chains4663status_whether_the_registry_is_live(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetStatusResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStatusResponse
            Freshness

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.status.alias_of_chains4663status_whether_the_registry_is_live()


        asyncio.run(main())
        """
        _response = await self._raw_client.alias_of_chains4663status_whether_the_registry_is_live(
            request_options=request_options
        )
        return _response.data
