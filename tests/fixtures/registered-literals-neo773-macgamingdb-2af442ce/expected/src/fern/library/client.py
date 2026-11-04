

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawLibraryClient, RawLibraryClient
from .types.library_link_start_url_response import LibraryLinkStartUrlResponse
from .types.library_list_response_item import LibraryListResponseItem
from .types.library_status_response import LibraryStatusResponse
from .types.library_sync_response import LibrarySyncResponse
from .types.library_unlink_response import LibraryUnlinkResponse


class LibraryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLibraryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLibraryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLibraryClient
        """
        return self._raw_client

    def linkstarturl(self, *, request_options: typing.Optional[RequestOptions] = None) -> LibraryLinkStartUrlResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LibraryLinkStartUrlResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.library.linkstarturl()
        """
        _response = self._raw_client.linkstarturl(request_options=request_options)
        return _response.data

    def status(self, *, request_options: typing.Optional[RequestOptions] = None) -> LibraryStatusResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LibraryStatusResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.library.status()
        """
        _response = self._raw_client.status(request_options=request_options)
        return _response.data

    def sync(self, *, request_options: typing.Optional[RequestOptions] = None) -> LibrarySyncResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LibrarySyncResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.library.sync()
        """
        _response = self._raw_client.sync(request_options=request_options)
        return _response.data

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[LibraryListResponseItem]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LibraryListResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.library.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    def unlink(self, *, request_options: typing.Optional[RequestOptions] = None) -> LibraryUnlinkResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LibraryUnlinkResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.library.unlink()
        """
        _response = self._raw_client.unlink(request_options=request_options)
        return _response.data


class AsyncLibraryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLibraryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLibraryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLibraryClient
        """
        return self._raw_client

    async def linkstarturl(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LibraryLinkStartUrlResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LibraryLinkStartUrlResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.library.linkstarturl()


        asyncio.run(main())
        """
        _response = await self._raw_client.linkstarturl(request_options=request_options)
        return _response.data

    async def status(self, *, request_options: typing.Optional[RequestOptions] = None) -> LibraryStatusResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LibraryStatusResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.library.status()


        asyncio.run(main())
        """
        _response = await self._raw_client.status(request_options=request_options)
        return _response.data

    async def sync(self, *, request_options: typing.Optional[RequestOptions] = None) -> LibrarySyncResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LibrarySyncResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.library.sync()


        asyncio.run(main())
        """
        _response = await self._raw_client.sync(request_options=request_options)
        return _response.data

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[LibraryListResponseItem]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LibraryListResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.library.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    async def unlink(self, *, request_options: typing.Optional[RequestOptions] = None) -> LibraryUnlinkResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LibraryUnlinkResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.library.unlink()


        asyncio.run(main())
        """
        _response = await self._raw_client.unlink(request_options=request_options)
        return _response.data
