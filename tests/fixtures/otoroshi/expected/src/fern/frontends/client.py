

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawFrontendsClient, RawFrontendsClient


class FrontendsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFrontendsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFrontendsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFrontendsClient
        """
        return self._raw_client

    def otoroshi_next_controllers_adminapi_ng_frontends_controller_form(
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
        client.frontends.otoroshi_next_controllers_adminapi_ng_frontends_controller_form()
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_frontends_controller_form(
            request_options=request_options
        )
        return _response.data


class AsyncFrontendsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFrontendsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFrontendsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFrontendsClient
        """
        return self._raw_client

    async def otoroshi_next_controllers_adminapi_ng_frontends_controller_form(
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
            await client.frontends.otoroshi_next_controllers_adminapi_ng_frontends_controller_form()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_frontends_controller_form(
            request_options=request_options
        )
        return _response.data
