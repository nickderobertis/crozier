

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawExperimentalClient, RawExperimentalClient


class ExperimentalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawExperimentalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawExperimentalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawExperimentalClient
        """
        return self._raw_client

    def otoroshi_next_controllers_adminapi_ng_routes_controller_domains_and_certificates(
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
        client.experimental.otoroshi_next_controllers_adminapi_ng_routes_controller_domains_and_certificates()
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_routes_controller_domains_and_certificates(
            request_options=request_options
        )
        return _response.data


class AsyncExperimentalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawExperimentalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawExperimentalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawExperimentalClient
        """
        return self._raw_client

    async def otoroshi_next_controllers_adminapi_ng_routes_controller_domains_and_certificates(
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
            await client.experimental.otoroshi_next_controllers_adminapi_ng_routes_controller_domains_and_certificates()


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_next_controllers_adminapi_ng_routes_controller_domains_and_certificates(
                request_options=request_options
            )
        )
        return _response.data
