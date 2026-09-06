

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawManagementClient, RawManagementClient


class ManagementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawManagementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawManagementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawManagementClient
        """
        return self._raw_client

    def get_actuator_info(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.management.get_actuator_info()
        """
        _response = self._raw_client.get_actuator_info(request_options=request_options)
        return _response.data


class AsyncManagementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawManagementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawManagementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawManagementClient
        """
        return self._raw_client

    async def get_actuator_info(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.management.get_actuator_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_actuator_info(request_options=request_options)
        return _response.data
