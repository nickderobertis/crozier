

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.anchore_error_code import AnchoreErrorCode
from ..types.feed_metadata import FeedMetadata
from ..types.feed_sync_results import FeedSyncResults
from ..types.gate_spec import GateSpec
from ..types.service_list import ServiceList
from ..types.status_response import StatusResponse
from ..types.system_status_response import SystemStatusResponse
from .raw_client import AsyncRawSystemClient, RawSystemClient
from .types.test_webhook_request_notification_type import TestWebhookRequestNotificationType


class SystemClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSystemClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSystemClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSystemClient
        """
        return self._raw_client

    def get_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> StatusResponse:
        """
        Get the API service status

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatusResponse
            Status listing

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.system.get_status()
        """
        _response = self._raw_client.get_status(request_options=request_options)
        return _response.data

    def get_service_detail(self, *, request_options: typing.Optional[RequestOptions] = None) -> SystemStatusResponse:
        """
        Get the system status including queue lengths

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemStatusResponse
            Status listing

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.system.get_service_detail()
        """
        _response = self._raw_client.get_service_detail(request_options=request_options)
        return _response.data

    def describe_error_codes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AnchoreErrorCode]:
        """
        Describe anchore engine error codes.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AnchoreErrorCode]
            Error Codes Description

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.system.describe_error_codes()
        """
        _response = self._raw_client.describe_error_codes(request_options=request_options)
        return _response.data

    def get_system_feeds(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[FeedMetadata]:
        """
        Return a list of feed and their groups along with update and record count information. This data reflects the state of the policy engine, not the upstream feed service itself.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FeedMetadata]
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.system.get_system_feeds()
        """
        _response = self._raw_client.get_system_feeds(request_options=request_options)
        return _response.data

    def post_system_feeds(
        self,
        *,
        flush: typing.Optional[bool] = None,
        sync: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedSyncResults:
        """
        Execute a synchronous feed sync operation. The response will block until complete, then return the result summary.

        Parameters
        ----------
        flush : typing.Optional[bool]
            instruct system to flush existing data feeds records from anchore-engine

        sync : typing.Optional[bool]
            instruct system to re-sync data feeds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedSyncResults
            Feeds operation success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.system.post_system_feeds()
        """
        _response = self._raw_client.post_system_feeds(flush=flush, sync=sync, request_options=request_options)
        return _response.data

    def toggle_feed_enabled(
        self, feed: str, *, enabled: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> FeedMetadata:
        """
        Disable the feed so that it does not sync on subsequent sync operations

        Parameters
        ----------
        feed : str

        enabled : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedMetadata
            FeedInfo

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.system.toggle_feed_enabled(
            feed="feed",
            enabled=True,
        )
        """
        _response = self._raw_client.toggle_feed_enabled(feed, enabled=enabled, request_options=request_options)
        return _response.data

    def delete_feed(self, feed: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete the groups and data for the feed and disable the feed itself

        Parameters
        ----------
        feed : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.system.delete_feed(
            feed="feed",
        )
        """
        _response = self._raw_client.delete_feed(feed, request_options=request_options)
        return _response.data

    def toggle_group_enabled(
        self, feed: str, group: str, *, enabled: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FeedMetadata]:
        """
        Disable a specific group within a feed to not sync

        Parameters
        ----------
        feed : str

        group : str

        enabled : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FeedMetadata]
            FeedInfo listing

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.system.toggle_group_enabled(
            feed="feed",
            group="group",
            enabled=True,
        )
        """
        _response = self._raw_client.toggle_group_enabled(feed, group, enabled=enabled, request_options=request_options)
        return _response.data

    def delete_feed_group(
        self, feed: str, group: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete the group data and disable the group itself

        Parameters
        ----------
        feed : str

        group : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.system.delete_feed_group(
            feed="feed",
            group="group",
        )
        """
        _response = self._raw_client.delete_feed_group(feed, group, request_options=request_options)
        return _response.data

    def describe_policy(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[GateSpec]:
        """
        Get the policy language spec for this service

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GateSpec]
            Policy Language Description

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.system.describe_policy()
        """
        _response = self._raw_client.describe_policy(request_options=request_options)
        return _response.data

    def list_services(self, *, request_options: typing.Optional[RequestOptions] = None) -> ServiceList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceList
            Service listing

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.system.list_services()
        """
        _response = self._raw_client.list_services(request_options=request_options)
        return _response.data

    def get_services_by_name(
        self, servicename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceList:
        """
        Parameters
        ----------
        servicename : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceList
            Service Info

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.system.get_services_by_name(
            servicename="servicename",
        )
        """
        _response = self._raw_client.get_services_by_name(servicename, request_options=request_options)
        return _response.data

    def get_services_by_name_and_host(
        self, servicename: str, hostid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceList:
        """
        Parameters
        ----------
        servicename : str

        hostid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceList
            Listing of registered services

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.system.get_services_by_name_and_host(
            servicename="servicename",
            hostid="hostid",
        )
        """
        _response = self._raw_client.get_services_by_name_and_host(servicename, hostid, request_options=request_options)
        return _response.data

    def delete_service(
        self, servicename: str, hostid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        servicename : str

        hostid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.system.delete_service(
            servicename="servicename",
            hostid="hostid",
        )
        """
        _response = self._raw_client.delete_service(servicename, hostid, request_options=request_options)
        return _response.data

    def test_webhook(
        self,
        webhook_type: str,
        *,
        notification_type: typing.Optional[TestWebhookRequestNotificationType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Loads the Webhook configuration for webhook_type, and sends the notification out as a test

        Parameters
        ----------
        webhook_type : str
            The Webhook Type that we should test

        notification_type : typing.Optional[TestWebhookRequestNotificationType]
            What kind of Notification to send

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.system.test_webhook(
            webhook_type="webhook_type",
        )
        """
        _response = self._raw_client.test_webhook(
            webhook_type, notification_type=notification_type, request_options=request_options
        )
        return _response.data


class AsyncSystemClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSystemClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSystemClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSystemClient
        """
        return self._raw_client

    async def get_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> StatusResponse:
        """
        Get the API service status

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatusResponse
            Status listing

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.system.get_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_status(request_options=request_options)
        return _response.data

    async def get_service_detail(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SystemStatusResponse:
        """
        Get the system status including queue lengths

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemStatusResponse
            Status listing

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.system.get_service_detail()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_service_detail(request_options=request_options)
        return _response.data

    async def describe_error_codes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AnchoreErrorCode]:
        """
        Describe anchore engine error codes.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AnchoreErrorCode]
            Error Codes Description

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.system.describe_error_codes()


        asyncio.run(main())
        """
        _response = await self._raw_client.describe_error_codes(request_options=request_options)
        return _response.data

    async def get_system_feeds(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FeedMetadata]:
        """
        Return a list of feed and their groups along with update and record count information. This data reflects the state of the policy engine, not the upstream feed service itself.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FeedMetadata]
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.system.get_system_feeds()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_system_feeds(request_options=request_options)
        return _response.data

    async def post_system_feeds(
        self,
        *,
        flush: typing.Optional[bool] = None,
        sync: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedSyncResults:
        """
        Execute a synchronous feed sync operation. The response will block until complete, then return the result summary.

        Parameters
        ----------
        flush : typing.Optional[bool]
            instruct system to flush existing data feeds records from anchore-engine

        sync : typing.Optional[bool]
            instruct system to re-sync data feeds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedSyncResults
            Feeds operation success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.system.post_system_feeds()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_system_feeds(flush=flush, sync=sync, request_options=request_options)
        return _response.data

    async def toggle_feed_enabled(
        self, feed: str, *, enabled: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> FeedMetadata:
        """
        Disable the feed so that it does not sync on subsequent sync operations

        Parameters
        ----------
        feed : str

        enabled : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedMetadata
            FeedInfo

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.system.toggle_feed_enabled(
                feed="feed",
                enabled=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.toggle_feed_enabled(feed, enabled=enabled, request_options=request_options)
        return _response.data

    async def delete_feed(self, feed: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete the groups and data for the feed and disable the feed itself

        Parameters
        ----------
        feed : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.system.delete_feed(
                feed="feed",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_feed(feed, request_options=request_options)
        return _response.data

    async def toggle_group_enabled(
        self, feed: str, group: str, *, enabled: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FeedMetadata]:
        """
        Disable a specific group within a feed to not sync

        Parameters
        ----------
        feed : str

        group : str

        enabled : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FeedMetadata]
            FeedInfo listing

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.system.toggle_group_enabled(
                feed="feed",
                group="group",
                enabled=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.toggle_group_enabled(
            feed, group, enabled=enabled, request_options=request_options
        )
        return _response.data

    async def delete_feed_group(
        self, feed: str, group: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete the group data and disable the group itself

        Parameters
        ----------
        feed : str

        group : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.system.delete_feed_group(
                feed="feed",
                group="group",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_feed_group(feed, group, request_options=request_options)
        return _response.data

    async def describe_policy(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GateSpec]:
        """
        Get the policy language spec for this service

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GateSpec]
            Policy Language Description

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.system.describe_policy()


        asyncio.run(main())
        """
        _response = await self._raw_client.describe_policy(request_options=request_options)
        return _response.data

    async def list_services(self, *, request_options: typing.Optional[RequestOptions] = None) -> ServiceList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceList
            Service listing

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.system.list_services()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_services(request_options=request_options)
        return _response.data

    async def get_services_by_name(
        self, servicename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceList:
        """
        Parameters
        ----------
        servicename : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceList
            Service Info

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.system.get_services_by_name(
                servicename="servicename",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_services_by_name(servicename, request_options=request_options)
        return _response.data

    async def get_services_by_name_and_host(
        self, servicename: str, hostid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceList:
        """
        Parameters
        ----------
        servicename : str

        hostid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceList
            Listing of registered services

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.system.get_services_by_name_and_host(
                servicename="servicename",
                hostid="hostid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_services_by_name_and_host(
            servicename, hostid, request_options=request_options
        )
        return _response.data

    async def delete_service(
        self, servicename: str, hostid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        servicename : str

        hostid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.system.delete_service(
                servicename="servicename",
                hostid="hostid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_service(servicename, hostid, request_options=request_options)
        return _response.data

    async def test_webhook(
        self,
        webhook_type: str,
        *,
        notification_type: typing.Optional[TestWebhookRequestNotificationType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Loads the Webhook configuration for webhook_type, and sends the notification out as a test

        Parameters
        ----------
        webhook_type : str
            The Webhook Type that we should test

        notification_type : typing.Optional[TestWebhookRequestNotificationType]
            What kind of Notification to send

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.system.test_webhook(
                webhook_type="webhook_type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.test_webhook(
            webhook_type, notification_type=notification_type, request_options=request_options
        )
        return _response.data
