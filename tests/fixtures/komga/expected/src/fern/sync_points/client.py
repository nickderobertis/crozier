

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSyncPointsClient, RawSyncPointsClient


class SyncPointsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSyncPointsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSyncPointsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSyncPointsClient
        """
        return self._raw_client

    def delete_sync_points_for_current_user(
        self,
        *,
        key_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        If an API Key ID is passed, deletes only the sync points associated with that API Key. Deleting sync points will allow a Kobo to sync from scratch upon the next sync.

        Parameters
        ----------
        key_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.sync_points.delete_sync_points_for_current_user()
        """
        _response = self._raw_client.delete_sync_points_for_current_user(key_id=key_id, request_options=request_options)
        return _response.data


class AsyncSyncPointsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSyncPointsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSyncPointsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSyncPointsClient
        """
        return self._raw_client

    async def delete_sync_points_for_current_user(
        self,
        *,
        key_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        If an API Key ID is passed, deletes only the sync points associated with that API Key. Deleting sync points will allow a Kobo to sync from scratch upon the next sync.

        Parameters
        ----------
        key_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.sync_points.delete_sync_points_for_current_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_sync_points_for_current_user(
            key_id=key_id, request_options=request_options
        )
        return _response.data
