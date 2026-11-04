

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.files_sharing_share_info import FilesSharingShareInfo
from .raw_client import AsyncRawFilesSharingShareInfoClient, RawFilesSharingShareInfoClient


class FilesSharingShareInfoClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFilesSharingShareInfoClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFilesSharingShareInfoClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFilesSharingShareInfoClient
        """
        return self._raw_client

    def info(
        self,
        *,
        t: str,
        password: typing.Optional[str] = None,
        dir: typing.Optional[str] = None,
        depth: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FilesSharingShareInfo:
        """
        Parameters
        ----------
        t : str
            Token of the share

        password : typing.Optional[str]
            Password of the share

        dir : typing.Optional[str]
            Subdirectory to get info about

        depth : typing.Optional[int]
            Maximum depth to get info about

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesSharingShareInfo
            Share info returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.files_sharing_share_info.info(
            t="t",
        )
        """
        _response = self._raw_client.info(t=t, password=password, dir=dir, depth=depth, request_options=request_options)
        return _response.data


class AsyncFilesSharingShareInfoClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFilesSharingShareInfoClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFilesSharingShareInfoClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFilesSharingShareInfoClient
        """
        return self._raw_client

    async def info(
        self,
        *,
        t: str,
        password: typing.Optional[str] = None,
        dir: typing.Optional[str] = None,
        depth: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FilesSharingShareInfo:
        """
        Parameters
        ----------
        t : str
            Token of the share

        password : typing.Optional[str]
            Password of the share

        dir : typing.Optional[str]
            Subdirectory to get info about

        depth : typing.Optional[int]
            Maximum depth to get info about

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesSharingShareInfo
            Share info returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.files_sharing_share_info.info(
                t="t",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.info(
            t=t, password=password, dir=dir, depth=depth, request_options=request_options
        )
        return _response.data
