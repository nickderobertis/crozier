

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawInfosClient, RawInfosClient


class InfosClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInfosClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInfosClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInfosClient
        """
        return self._raw_client

    def otoroshi_controllers_adminapi_infos_api_controller_infos(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.infos.otoroshi_controllers_adminapi_infos_api_controller_infos()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_infos_api_controller_infos(
            request_options=request_options
        )
        return _response.data


class AsyncInfosClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInfosClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInfosClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInfosClient
        """
        return self._raw_client

    async def otoroshi_controllers_adminapi_infos_api_controller_infos(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.infos.otoroshi_controllers_adminapi_infos_api_controller_infos()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_infos_api_controller_infos(
            request_options=request_options
        )
        return _response.data
