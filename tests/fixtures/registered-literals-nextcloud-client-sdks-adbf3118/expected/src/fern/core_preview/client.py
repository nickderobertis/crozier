

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCorePreviewClient, RawCorePreviewClient


class CorePreviewClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCorePreviewClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCorePreviewClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCorePreviewClient
        """
        return self._raw_client

    def get_preview_by_file_id(
        self,
        *,
        file_id: typing.Optional[int] = None,
        x: typing.Optional[int] = None,
        y: typing.Optional[int] = None,
        a: typing.Optional[int] = None,
        force_icon: typing.Optional[int] = None,
        mode: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        file_id : typing.Optional[int]
            ID of the file

        x : typing.Optional[int]
            Width of the preview

        y : typing.Optional[int]
            Height of the preview

        a : typing.Optional[int]
            Not crop the preview

        force_icon : typing.Optional[int]
            Force returning an icon

        mode : typing.Optional[str]
            How to crop the image

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Preview returned
        """
        with self._raw_client.get_preview_by_file_id(
            file_id=file_id, x=x, y=y, a=a, force_icon=force_icon, mode=mode, request_options=request_options
        ) as r:
            yield from r.data

    def get_preview(
        self,
        *,
        file: typing.Optional[str] = None,
        x: typing.Optional[int] = None,
        y: typing.Optional[int] = None,
        a: typing.Optional[int] = None,
        force_icon: typing.Optional[int] = None,
        mode: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        file : typing.Optional[str]
            Path of the file

        x : typing.Optional[int]
            Width of the preview

        y : typing.Optional[int]
            Height of the preview

        a : typing.Optional[int]
            Not crop the preview

        force_icon : typing.Optional[int]
            Force returning an icon

        mode : typing.Optional[str]
            How to crop the image

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Preview returned
        """
        with self._raw_client.get_preview(
            file=file, x=x, y=y, a=a, force_icon=force_icon, mode=mode, request_options=request_options
        ) as r:
            yield from r.data


class AsyncCorePreviewClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCorePreviewClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCorePreviewClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCorePreviewClient
        """
        return self._raw_client

    async def get_preview_by_file_id(
        self,
        *,
        file_id: typing.Optional[int] = None,
        x: typing.Optional[int] = None,
        y: typing.Optional[int] = None,
        a: typing.Optional[int] = None,
        force_icon: typing.Optional[int] = None,
        mode: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        file_id : typing.Optional[int]
            ID of the file

        x : typing.Optional[int]
            Width of the preview

        y : typing.Optional[int]
            Height of the preview

        a : typing.Optional[int]
            Not crop the preview

        force_icon : typing.Optional[int]
            Force returning an icon

        mode : typing.Optional[str]
            How to crop the image

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Preview returned
        """
        async with self._raw_client.get_preview_by_file_id(
            file_id=file_id, x=x, y=y, a=a, force_icon=force_icon, mode=mode, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_preview(
        self,
        *,
        file: typing.Optional[str] = None,
        x: typing.Optional[int] = None,
        y: typing.Optional[int] = None,
        a: typing.Optional[int] = None,
        force_icon: typing.Optional[int] = None,
        mode: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        file : typing.Optional[str]
            Path of the file

        x : typing.Optional[int]
            Width of the preview

        y : typing.Optional[int]
            Height of the preview

        a : typing.Optional[int]
            Not crop the preview

        force_icon : typing.Optional[int]
            Force returning an icon

        mode : typing.Optional[str]
            How to crop the image

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Preview returned
        """
        async with self._raw_client.get_preview(
            file=file, x=x, y=y, a=a, force_icon=force_icon, mode=mode, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk
