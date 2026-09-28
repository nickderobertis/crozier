

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawEventsClient, RawEventsClient


class EventsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEventsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEventsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEventsClient
        """
        return self._raw_client

    def otoroshi_controllers_adminapi_events_controller_audit_events(
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
        client.events.otoroshi_controllers_adminapi_events_controller_audit_events()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_events_controller_audit_events(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_events_controller_alert_events(
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
        client.events.otoroshi_controllers_adminapi_events_controller_alert_events()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_events_controller_alert_events(
            request_options=request_options
        )
        return _response.data


class AsyncEventsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEventsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEventsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEventsClient
        """
        return self._raw_client

    async def otoroshi_controllers_adminapi_events_controller_audit_events(
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
            await client.events.otoroshi_controllers_adminapi_events_controller_audit_events()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_events_controller_audit_events(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_events_controller_alert_events(
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
            await client.events.otoroshi_controllers_adminapi_events_controller_alert_events()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_events_controller_alert_events(
            request_options=request_options
        )
        return _response.data
