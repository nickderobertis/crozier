

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAigatewayClient, RawAigatewayClient
from .types.ai_gateway_all_response_item import AiGatewayAllResponseItem


class AigatewayClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAigatewayClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAigatewayClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAigatewayClient
        """
        return self._raw_client

    def all_(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AiGatewayAllResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AiGatewayAllResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.aigateway.all_(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.all_(workspace_id, request_options=request_options)
        return _response.data


class AsyncAigatewayClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAigatewayClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAigatewayClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAigatewayClient
        """
        return self._raw_client

    async def all_(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AiGatewayAllResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AiGatewayAllResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.aigateway.all_(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(workspace_id, request_options=request_options)
        return _response.data
