

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.run_summary import RunSummary
from .raw_client import AsyncRawRunsClient, RawRunsClient


class RunsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRunsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRunsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRunsClient
        """
        return self._raw_client

    def get_run(self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> RunSummary:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RunSummary
            The run.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.runs.get_run(
            run_id="run_id",
        )
        """
        _response = self._raw_client.get_run(run_id, request_options=request_options)
        return _response.data


class AsyncRunsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRunsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRunsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRunsClient
        """
        return self._raw_client

    async def get_run(self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> RunSummary:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RunSummary
            The run.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.runs.get_run(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_run(run_id, request_options=request_options)
        return _response.data
