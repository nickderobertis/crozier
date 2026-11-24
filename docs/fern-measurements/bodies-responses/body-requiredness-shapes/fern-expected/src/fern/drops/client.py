

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawDropsClient, RawDropsClient
from .types.create_drop_request import CreateDropRequest
from .types.preview_drop_request import PreviewDropRequest


OMIT = typing.cast(typing.Any, ...)


class DropsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDropsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDropsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDropsClient
        """
        return self._raw_client

    def create_drop(
        self, *, request: CreateDropRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : CreateDropRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, KilnDrop

        client = FernApi()
        client.drops.create_drop(
            request=KilnDrop(
                kiln="kiln",
            ),
        )
        """
        _response = self._raw_client.create_drop(request=request, request_options=request_options)
        return _response.data

    def preview_drop(
        self, *, request: PreviewDropRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : PreviewDropRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, KilnDrop

        client = FernApi()
        client.drops.preview_drop(
            request=KilnDrop(
                kiln="kiln",
            ),
        )
        """
        _response = self._raw_client.preview_drop(request=request, request_options=request_options)
        return _response.data


class AsyncDropsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDropsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDropsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDropsClient
        """
        return self._raw_client

    async def create_drop(
        self, *, request: CreateDropRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : CreateDropRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, KilnDrop

        client = AsyncFernApi()


        async def main() -> None:
            await client.drops.create_drop(
                request=KilnDrop(
                    kiln="kiln",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_drop(request=request, request_options=request_options)
        return _response.data

    async def preview_drop(
        self, *, request: PreviewDropRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : PreviewDropRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, KilnDrop

        client = AsyncFernApi()


        async def main() -> None:
            await client.drops.preview_drop(
                request=KilnDrop(
                    kiln="kiln",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.preview_drop(request=request, request_options=request_options)
        return _response.data
