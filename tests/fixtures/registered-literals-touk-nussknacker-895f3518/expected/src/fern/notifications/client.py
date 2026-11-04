

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.notification import Notification
from .raw_client import AsyncRawNotificationsClient, RawNotificationsClient


class NotificationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNotificationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNotificationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNotificationsClient
        """
        return self._raw_client

    def get_api_notifications(
        self, *, scenario_name: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Notification]:
        """
        Parameters
        ----------
        scenario_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Notification]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.notifications.get_api_notifications()
        """
        _response = self._raw_client.get_api_notifications(scenario_name=scenario_name, request_options=request_options)
        return _response.data


class AsyncNotificationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNotificationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNotificationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNotificationsClient
        """
        return self._raw_client

    async def get_api_notifications(
        self, *, scenario_name: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Notification]:
        """
        Parameters
        ----------
        scenario_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Notification]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.notifications.get_api_notifications()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_notifications(
            scenario_name=scenario_name, request_options=request_options
        )
        return _response.data
