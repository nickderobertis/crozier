

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawGeneralClient, RawGeneralClient
from .types.get_system_info_response import GetSystemInfoResponse


class GeneralClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGeneralClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGeneralClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGeneralClient
        """
        return self._raw_client

    def get_system_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetSystemInfoResponse:
        """
        Returns device identity, firmware, network state, meter status and more.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSystemInfoResponse
            System information

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.general.get_system_info()
        """
        _response = self._raw_client.get_system_info(request_options=request_options)
        return _response.data


class AsyncGeneralClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGeneralClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGeneralClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGeneralClient
        """
        return self._raw_client

    async def get_system_info(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSystemInfoResponse:
        """
        Returns device identity, firmware, network state, meter status and more.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSystemInfoResponse
            System information

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.general.get_system_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_system_info(request_options=request_options)
        return _response.data
