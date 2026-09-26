

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawVersionClient, RawVersionClient


class VersionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVersionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVersionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVersionClient
        """
        return self._raw_client

    def otoroshi_controllers_adminapi_infos_api_controller_version(
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
        client.version.otoroshi_controllers_adminapi_infos_api_controller_version()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_infos_api_controller_version(
            request_options=request_options
        )
        return _response.data


class AsyncVersionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVersionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVersionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVersionClient
        """
        return self._raw_client

    async def otoroshi_controllers_adminapi_infos_api_controller_version(
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
            await client.version.otoroshi_controllers_adminapi_infos_api_controller_version()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_infos_api_controller_version(
            request_options=request_options
        )
        return _response.data
