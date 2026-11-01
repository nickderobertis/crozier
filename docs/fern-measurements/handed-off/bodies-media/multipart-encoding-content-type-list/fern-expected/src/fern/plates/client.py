

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPlatesClient, RawPlatesClient


OMIT = typing.cast(typing.Any, ...)


class PlatesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPlatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPlatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPlatesClient
        """
        return self._raw_client

    def upload_artwork(
        self, plate_id: str, *, artwork: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        plate_id : str

        artwork : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.plates.upload_artwork(
            plate_id="plateId",
        )
        """
        _response = self._raw_client.upload_artwork(plate_id, artwork=artwork, request_options=request_options)
        return _response.data


class AsyncPlatesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPlatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPlatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPlatesClient
        """
        return self._raw_client

    async def upload_artwork(
        self, plate_id: str, *, artwork: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        plate_id : str

        artwork : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.plates.upload_artwork(
                plate_id="plateId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_artwork(plate_id, artwork=artwork, request_options=request_options)
        return _response.data
