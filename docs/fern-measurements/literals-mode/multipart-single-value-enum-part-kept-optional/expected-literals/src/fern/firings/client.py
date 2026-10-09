

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawFiringsClient, RawFiringsClient
from .types.book_firing_request_atmosphere import BookFiringRequestAtmosphere


OMIT = typing.cast(typing.Any, ...)


class FiringsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFiringsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFiringsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFiringsClient
        """
        return self._raw_client

    def book_firing(
        self,
        *,
        glaze_sheet: core.File,
        atmosphere: typing.Optional[BookFiringRequestAtmosphere] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        glaze_sheet : core.File
            See core.File for more documentation

        atmosphere : typing.Optional[BookFiringRequestAtmosphere]

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
        client.firings.book_firing()
        """
        _response = self._raw_client.book_firing(
            glaze_sheet=glaze_sheet, atmosphere=atmosphere, request_options=request_options
        )
        return _response.data


class AsyncFiringsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFiringsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFiringsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFiringsClient
        """
        return self._raw_client

    async def book_firing(
        self,
        *,
        glaze_sheet: core.File,
        atmosphere: typing.Optional[BookFiringRequestAtmosphere] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        glaze_sheet : core.File
            See core.File for more documentation

        atmosphere : typing.Optional[BookFiringRequestAtmosphere]

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
            await client.firings.book_firing()


        asyncio.run(main())
        """
        _response = await self._raw_client.book_firing(
            glaze_sheet=glaze_sheet, atmosphere=atmosphere, request_options=request_options
        )
        return _response.data
