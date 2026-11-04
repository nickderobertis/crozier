

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawRcloneClient, RawRcloneClient
from .types.rclone_stage_response import RcloneStageResponse


OMIT = typing.cast(typing.Any, ...)


class RcloneClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRcloneClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRcloneClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRcloneClient
        """
        return self._raw_client

    def action(
        self,
        *,
        method: str,
        params: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        method : str

        params : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.rclone.action(
            method="method",
        )
        """
        _response = self._raw_client.action(method=method, params=params, request_options=request_options)
        return _response.data

    def stage(
        self,
        filename: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RcloneStageResponse:
        """
        Parameters
        ----------
        filename : str

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RcloneStageResponse
            The request has succeeded and a new resource has been created as a result.
        """
        _response = self._raw_client.stage(filename, request=request, request_options=request_options)
        return _response.data

    def local_content(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.rclone.local_content(
            path="path",
        )
        """
        with self._raw_client.local_content(path=path, request_options=request_options) as r:
            yield from r.data


class AsyncRcloneClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRcloneClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRcloneClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRcloneClient
        """
        return self._raw_client

    async def action(
        self,
        *,
        method: str,
        params: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        method : str

        params : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rclone.action(
                method="method",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.action(method=method, params=params, request_options=request_options)
        return _response.data

    async def stage(
        self,
        filename: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RcloneStageResponse:
        """
        Parameters
        ----------
        filename : str

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RcloneStageResponse
            The request has succeeded and a new resource has been created as a result.
        """
        _response = await self._raw_client.stage(filename, request=request, request_options=request_options)
        return _response.data

    async def local_content(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rclone.local_content(
                path="path",
            )


        asyncio.run(main())
        """
        async with self._raw_client.local_content(path=path, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
