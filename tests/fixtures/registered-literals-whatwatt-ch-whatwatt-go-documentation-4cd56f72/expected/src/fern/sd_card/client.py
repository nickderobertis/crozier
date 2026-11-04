

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSdCardClient, RawSdCardClient
from .types.list_sd_root_response import ListSdRootResponse


class SdCardClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSdCardClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSdCardClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSdCardClient
        """
        return self._raw_client

    def list_sd_root(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListSdRootResponse:
        """
        Lists files and directories on the SD card root.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSdRootResponse
            Directory listing

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.sd_card.list_sd_root()
        """
        _response = self._raw_client.list_sd_root(request_options=request_options)
        return _response.data

    def get_sd_path(
        self, path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Download a file (raw) or list a subdirectory (JSON) when the path ends with '/'.

        Parameters
        ----------
        path : str
            File or directory path relative to /sdcard. If ends with '/', a JSON directory listing is returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            File download or directory listing

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.sd_card.get_sd_path(
            path="path",
        )
        """
        with self._raw_client.get_sd_path(path, request_options=request_options) as r:
            yield from r.data

    def delete_sd_path(self, path: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes a file or recursively deletes a directory.

        Parameters
        ----------
        path : str
            File or directory path relative to /sdcard. If ends with '/', a JSON directory listing is returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.sd_card.delete_sd_path(
            path="path",
        )
        """
        _response = self._raw_client.delete_sd_path(path, request_options=request_options)
        return _response.data


class AsyncSdCardClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSdCardClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSdCardClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSdCardClient
        """
        return self._raw_client

    async def list_sd_root(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListSdRootResponse:
        """
        Lists files and directories on the SD card root.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSdRootResponse
            Directory listing

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.sd_card.list_sd_root()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_sd_root(request_options=request_options)
        return _response.data

    async def get_sd_path(
        self, path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Download a file (raw) or list a subdirectory (JSON) when the path ends with '/'.

        Parameters
        ----------
        path : str
            File or directory path relative to /sdcard. If ends with '/', a JSON directory listing is returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            File download or directory listing

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.sd_card.get_sd_path(
                path="path",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_sd_path(path, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def delete_sd_path(self, path: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes a file or recursively deletes a directory.

        Parameters
        ----------
        path : str
            File or directory path relative to /sdcard. If ends with '/', a JSON directory listing is returned.

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.sd_card.delete_sd_path(
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_sd_path(path, request_options=request_options)
        return _response.data
