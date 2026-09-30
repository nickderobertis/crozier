

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.cancellation_response import CancellationResponse
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

    def request_run_cancellation(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CancellationResponse:
        """
        Request cancellation for a run.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CancellationResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.runs.request_run_cancellation(
            run_id="run_id",
        )
        """
        _response = self._raw_client.request_run_cancellation(run_id, request_options=request_options)
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

    async def request_run_cancellation(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CancellationResponse:
        """
        Request cancellation for a run.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CancellationResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.runs.request_run_cancellation(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.request_run_cancellation(run_id, request_options=request_options)
        return _response.data
