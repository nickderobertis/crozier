

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user_status_user_status_get_status200response import UserStatusUserStatusGetStatus200Response
from .raw_client import AsyncRawUserStatusHeartbeatClient, RawUserStatusHeartbeatClient


class UserStatusHeartbeatClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserStatusHeartbeatClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserStatusHeartbeatClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserStatusHeartbeatClient
        """
        return self._raw_client

    def heartbeat(
        self, *, status: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UserStatusUserStatusGetStatus200Response:
        """
        Parameters
        ----------
        status : str
            Only online, away

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserStatusUserStatusGetStatus200Response
            Status successfully updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_status_heartbeat.heartbeat(
            status="status",
        )
        """
        _response = self._raw_client.heartbeat(status=status, request_options=request_options)
        return _response.data


class AsyncUserStatusHeartbeatClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserStatusHeartbeatClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserStatusHeartbeatClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserStatusHeartbeatClient
        """
        return self._raw_client

    async def heartbeat(
        self, *, status: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UserStatusUserStatusGetStatus200Response:
        """
        Parameters
        ----------
        status : str
            Only online, away

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserStatusUserStatusGetStatus200Response
            Status successfully updated

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
            await client.user_status_heartbeat.heartbeat(
                status="status",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.heartbeat(status=status, request_options=request_options)
        return _response.data
