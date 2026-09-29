

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.volume_tree_response import VolumeTreeResponse
from .raw_client import AsyncRawVolumeClient, RawVolumeClient


class VolumeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVolumeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVolumeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVolumeClient
        """
        return self._raw_client

    def list_volume_tree_api(
        self,
        *,
        root: typing.Optional[str] = None,
        max_depth: typing.Optional[int] = None,
        max_files: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VolumeTreeResponse:
        """
        Parameters
        ----------
        root : typing.Optional[str]

        max_depth : typing.Optional[int]

        max_files : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VolumeTreeResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.volume.list_volume_tree_api()
        """
        _response = self._raw_client.list_volume_tree_api(
            root=root, max_depth=max_depth, max_files=max_files, request_options=request_options
        )
        return _response.data


class AsyncVolumeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVolumeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVolumeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVolumeClient
        """
        return self._raw_client

    async def list_volume_tree_api(
        self,
        *,
        root: typing.Optional[str] = None,
        max_depth: typing.Optional[int] = None,
        max_files: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VolumeTreeResponse:
        """
        Parameters
        ----------
        root : typing.Optional[str]

        max_depth : typing.Optional[int]

        max_files : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VolumeTreeResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.volume.list_volume_tree_api()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_volume_tree_api(
            root=root, max_depth=max_depth, max_files=max_files, request_options=request_options
        )
        return _response.data
