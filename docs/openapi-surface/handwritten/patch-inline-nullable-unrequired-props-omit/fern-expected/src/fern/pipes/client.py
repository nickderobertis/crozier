

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPipesClient, RawPipesClient


OMIT = typing.cast(typing.Any, ...)


class PipesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPipesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPipesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPipesClient
        """
        return self._raw_client

    def tune_pipe(
        self,
        pipe_id: str,
        *,
        pitch: typing.Optional[str] = OMIT,
        cents: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        pipe_id : str

        pitch : typing.Optional[str]

        cents : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pipes.tune_pipe(
            pipe_id="pipeId",
        )
        """
        _response = self._raw_client.tune_pipe(pipe_id, pitch=pitch, cents=cents, request_options=request_options)
        return _response.data


class AsyncPipesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPipesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPipesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPipesClient
        """
        return self._raw_client

    async def tune_pipe(
        self,
        pipe_id: str,
        *,
        pitch: typing.Optional[str] = OMIT,
        cents: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        pipe_id : str

        pitch : typing.Optional[str]

        cents : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pipes.tune_pipe(
                pipe_id="pipeId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tune_pipe(pipe_id, pitch=pitch, cents=cents, request_options=request_options)
        return _response.data
