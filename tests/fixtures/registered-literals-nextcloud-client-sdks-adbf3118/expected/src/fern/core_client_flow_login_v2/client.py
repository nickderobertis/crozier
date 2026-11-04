

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.core_login_flow_v2 import CoreLoginFlowV2
from ..types.core_login_flow_v2credentials import CoreLoginFlowV2Credentials
from .raw_client import AsyncRawCoreClientFlowLoginV2Client, RawCoreClientFlowLoginV2Client


class CoreClientFlowLoginV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCoreClientFlowLoginV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCoreClientFlowLoginV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCoreClientFlowLoginV2Client
        """
        return self._raw_client

    def poll(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreLoginFlowV2Credentials:
        """
        Parameters
        ----------
        token : str
            Token of the flow

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreLoginFlowV2Credentials
            Login flow credentials returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_client_flow_login_v2.poll(
            token="token",
        )
        """
        _response = self._raw_client.poll(token=token, request_options=request_options)
        return _response.data

    def init(self, *, request_options: typing.Optional[RequestOptions] = None) -> CoreLoginFlowV2:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreLoginFlowV2


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_client_flow_login_v2.init()
        """
        _response = self._raw_client.init(request_options=request_options)
        return _response.data


class AsyncCoreClientFlowLoginV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCoreClientFlowLoginV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCoreClientFlowLoginV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCoreClientFlowLoginV2Client
        """
        return self._raw_client

    async def poll(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreLoginFlowV2Credentials:
        """
        Parameters
        ----------
        token : str
            Token of the flow

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreLoginFlowV2Credentials
            Login flow credentials returned

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
            await client.core_client_flow_login_v2.poll(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.poll(token=token, request_options=request_options)
        return _response.data

    async def init(self, *, request_options: typing.Optional[RequestOptions] = None) -> CoreLoginFlowV2:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreLoginFlowV2


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
            await client.core_client_flow_login_v2.init()


        asyncio.run(main())
        """
        _response = await self._raw_client.init(request_options=request_options)
        return _response.data
