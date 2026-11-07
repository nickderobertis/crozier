

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.trigger_sync_response import TriggerSyncResponse
from .raw_client import AsyncRawSyncClient, RawSyncClient


class SyncClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSyncClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSyncClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSyncClient
        """
        return self._raw_client

    def triggersync(
        self,
        *,
        revert_api_token: str,
        revert_t_id: str,
        connection_api_key: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TriggerSyncResponse:
        """
        Trigger sync for a specific tenant

        Parameters
        ----------
        revert_api_token : str
            Your official API key for accessing revert apis.

        revert_t_id : str
            The unique customer id used when the customer linked their account.

        connection_api_key : typing.Optional[str]
            API key for third party provider

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TriggerSyncResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.sync.triggersync(
            revert_api_token="x-revert-api-token",
            revert_t_id="x-revert-t-id",
        )
        """
        _response = self._raw_client.triggersync(
            revert_api_token=revert_api_token,
            revert_t_id=revert_t_id,
            connection_api_key=connection_api_key,
            request_options=request_options,
        )
        return _response.data


class AsyncSyncClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSyncClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSyncClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSyncClient
        """
        return self._raw_client

    async def triggersync(
        self,
        *,
        revert_api_token: str,
        revert_t_id: str,
        connection_api_key: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TriggerSyncResponse:
        """
        Trigger sync for a specific tenant

        Parameters
        ----------
        revert_api_token : str
            Your official API key for accessing revert apis.

        revert_t_id : str
            The unique customer id used when the customer linked their account.

        connection_api_key : typing.Optional[str]
            API key for third party provider

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TriggerSyncResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.sync.triggersync(
                revert_api_token="x-revert-api-token",
                revert_t_id="x-revert-t-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.triggersync(
            revert_api_token=revert_api_token,
            revert_t_id=revert_t_id,
            connection_api_key=connection_api_key,
            request_options=request_options,
        )
        return _response.data
