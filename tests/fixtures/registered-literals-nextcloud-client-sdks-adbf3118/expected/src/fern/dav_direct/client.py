

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.dav_direct_get_url200response import DavDirectGetUrl200Response
from .raw_client import AsyncRawDavDirectClient, RawDavDirectClient


class DavDirectClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDavDirectClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDavDirectClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDavDirectClient
        """
        return self._raw_client

    def get_url(
        self,
        *,
        file_id: int,
        expiration_time: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DavDirectGetUrl200Response:
        """
        Parameters
        ----------
        file_id : int
            ID of the file

        expiration_time : typing.Optional[int]
            Duration until the link expires

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DavDirectGetUrl200Response
            Direct link returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dav_direct.get_url(
            file_id=1000000,
        )
        """
        _response = self._raw_client.get_url(
            file_id=file_id, expiration_time=expiration_time, request_options=request_options
        )
        return _response.data


class AsyncDavDirectClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDavDirectClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDavDirectClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDavDirectClient
        """
        return self._raw_client

    async def get_url(
        self,
        *,
        file_id: int,
        expiration_time: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DavDirectGetUrl200Response:
        """
        Parameters
        ----------
        file_id : int
            ID of the file

        expiration_time : typing.Optional[int]
            Duration until the link expires

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DavDirectGetUrl200Response
            Direct link returned

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
            await client.dav_direct.get_url(
                file_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_url(
            file_id=file_id, expiration_time=expiration_time, request_options=request_options
        )
        return _response.data
