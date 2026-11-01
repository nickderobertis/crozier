

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawMirrorsClient, RawMirrorsClient
from .types.add_mirror_response import AddMirrorResponse


OMIT = typing.cast(typing.Any, ...)


class MirrorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMirrorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMirrorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMirrorsClient
        """
        return self._raw_client

    def add_mirror(
        self, *, source: str, region: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AddMirrorResponse:
        """
        A format uri and a pattern-only string.

        Parameters
        ----------
        source : str

        region : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddMirrorResponse
            Added

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.mirrors.add_mirror(
            source="source",
            region="region",
        )
        """
        _response = self._raw_client.add_mirror(source=source, region=region, request_options=request_options)
        return _response.data


class AsyncMirrorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMirrorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMirrorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMirrorsClient
        """
        return self._raw_client

    async def add_mirror(
        self, *, source: str, region: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AddMirrorResponse:
        """
        A format uri and a pattern-only string.

        Parameters
        ----------
        source : str

        region : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddMirrorResponse
            Added

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.mirrors.add_mirror(
                source="source",
                region="region",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_mirror(source=source, region=region, request_options=request_options)
        return _response.data
