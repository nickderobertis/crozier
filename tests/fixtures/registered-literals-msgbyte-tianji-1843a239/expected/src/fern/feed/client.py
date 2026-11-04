

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawFeedClient, RawFeedClient
from .types.feed_channel_info_response import FeedChannelInfoResponse
from .types.feed_channels_response_item import FeedChannelsResponseItem
from .types.feed_create_channel_request_notify_frequency import FeedCreateChannelRequestNotifyFrequency
from .types.feed_create_channel_response import FeedCreateChannelResponse
from .types.feed_delete_channel_response import FeedDeleteChannelResponse
from .types.feed_disable_public_share_id_response import FeedDisablePublicShareIdResponse
from .types.feed_fetch_events_by_cursor_response import FeedFetchEventsByCursorResponse
from .types.feed_fetch_public_events_by_cursor_response import FeedFetchPublicEventsByCursorResponse
from .types.feed_get_channel_by_share_id_response import FeedGetChannelByShareIdResponse
from .types.feed_refresh_public_share_id_response import FeedRefreshPublicShareIdResponse
from .types.feed_send_event_response import FeedSendEventResponse
from .types.feed_state_all_response_item import FeedStateAllResponseItem
from .types.feed_state_resolve_response import FeedStateResolveResponse
from .types.feed_state_upsert_response import FeedStateUpsertResponse
from .types.feed_update_channel_info_request_notify_frequency import FeedUpdateChannelInfoRequestNotifyFrequency
from .types.feed_update_channel_info_response import FeedUpdateChannelInfoResponse


OMIT = typing.cast(typing.Any, ...)


class FeedClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFeedClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFeedClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFeedClient
        """
        return self._raw_client

    def channels(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FeedChannelsResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FeedChannelsResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feed.channels(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.channels(workspace_id, request_options=request_options)
        return _response.data

    def channelinfo(
        self, workspace_id: str, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[FeedChannelInfoResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        channel_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[FeedChannelInfoResponse]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feed.channelinfo(
            workspace_id="workspaceId",
            channel_id="channelId",
        )
        """
        _response = self._raw_client.channelinfo(workspace_id, channel_id, request_options=request_options)
        return _response.data

    def updatechannelinfo(
        self,
        workspace_id: str,
        channel_id: str,
        *,
        name: str,
        webhook_signature: str,
        notify_frequency: FeedUpdateChannelInfoRequestNotifyFrequency,
        notification_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[FeedUpdateChannelInfoResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        channel_id : str

        name : str

        webhook_signature : str

        notify_frequency : FeedUpdateChannelInfoRequestNotifyFrequency

        notification_ids : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[FeedUpdateChannelInfoResponse]
            Successful response

        Examples
        --------
        from fern.feed import FeedUpdateChannelInfoRequestNotifyFrequency

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feed.updatechannelinfo(
            workspace_id="workspaceId",
            channel_id="channelId",
            name="name",
            webhook_signature="webhookSignature",
            notify_frequency=FeedUpdateChannelInfoRequestNotifyFrequency.NONE,
        )
        """
        _response = self._raw_client.updatechannelinfo(
            workspace_id,
            channel_id,
            name=name,
            webhook_signature=webhook_signature,
            notify_frequency=notify_frequency,
            notification_ids=notification_ids,
            request_options=request_options,
        )
        return _response.data

    def fetcheventsbycursor(
        self,
        workspace_id: str,
        channel_id: str,
        *,
        limit: typing.Optional[float] = None,
        cursor: typing.Optional[str] = None,
        archived: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedFetchEventsByCursorResponse:
        """
        Fetch workspace feed channel events

        Parameters
        ----------
        workspace_id : str

        channel_id : str

        limit : typing.Optional[float]

        cursor : typing.Optional[str]

        archived : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedFetchEventsByCursorResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feed.fetcheventsbycursor(
            workspace_id="workspaceId",
            channel_id="channelId",
        )
        """
        _response = self._raw_client.fetcheventsbycursor(
            workspace_id, channel_id, limit=limit, cursor=cursor, archived=archived, request_options=request_options
        )
        return _response.data

    def fetchpubliceventsbycursor(
        self,
        share_id: str,
        *,
        limit: typing.Optional[float] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedFetchPublicEventsByCursorResponse:
        """
        Fetch public feed channel events by shareId

        Parameters
        ----------
        share_id : str

        limit : typing.Optional[float]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedFetchPublicEventsByCursorResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feed.fetchpubliceventsbycursor(
            share_id="shareId",
        )
        """
        _response = self._raw_client.fetchpubliceventsbycursor(
            share_id, limit=limit, cursor=cursor, request_options=request_options
        )
        return _response.data

    def getchannelbyshareid(
        self, share_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FeedGetChannelByShareIdResponse:
        """
        Fetch public feed channel info by shareId

        Parameters
        ----------
        share_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedGetChannelByShareIdResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feed.getchannelbyshareid(
            share_id="shareId",
        )
        """
        _response = self._raw_client.getchannelbyshareid(share_id, request_options=request_options)
        return _response.data

    def createchannel(
        self,
        workspace_id: str,
        *,
        name: str,
        notify_frequency: FeedCreateChannelRequestNotifyFrequency,
        notification_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedCreateChannelResponse:
        """
        Parameters
        ----------
        workspace_id : str

        name : str

        notify_frequency : FeedCreateChannelRequestNotifyFrequency

        notification_ids : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedCreateChannelResponse
            Successful response

        Examples
        --------
        from fern.feed import FeedCreateChannelRequestNotifyFrequency

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feed.createchannel(
            workspace_id="workspaceId",
            name="name",
            notify_frequency=FeedCreateChannelRequestNotifyFrequency.NONE,
        )
        """
        _response = self._raw_client.createchannel(
            workspace_id,
            name=name,
            notify_frequency=notify_frequency,
            notification_ids=notification_ids,
            request_options=request_options,
        )
        return _response.data

    def refreshpublicshareid(
        self, workspace_id: str, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FeedRefreshPublicShareIdResponse:
        """
        Regenerate public share id for feed channel

        Parameters
        ----------
        workspace_id : str

        channel_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedRefreshPublicShareIdResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feed.refreshpublicshareid(
            workspace_id="workspaceId",
            channel_id="channelId",
        )
        """
        _response = self._raw_client.refreshpublicshareid(workspace_id, channel_id, request_options=request_options)
        return _response.data

    def disablepublicshareid(
        self, workspace_id: str, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FeedDisablePublicShareIdResponse:
        """
        Disable public share for feed channel

        Parameters
        ----------
        workspace_id : str

        channel_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedDisablePublicShareIdResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feed.disablepublicshareid(
            workspace_id="workspaceId",
            channel_id="channelId",
        )
        """
        _response = self._raw_client.disablepublicshareid(workspace_id, channel_id, request_options=request_options)
        return _response.data

    def deletechannel(
        self, workspace_id: str, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FeedDeleteChannelResponse:
        """
        Parameters
        ----------
        workspace_id : str

        channel_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedDeleteChannelResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feed.deletechannel(
            workspace_id="workspaceId",
            channel_id="channelId",
        )
        """
        _response = self._raw_client.deletechannel(workspace_id, channel_id, request_options=request_options)
        return _response.data

    def sendevent(
        self,
        channel_id: str,
        *,
        event_name: str,
        event_content: str,
        source: str,
        important: bool,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        sender_id: typing.Optional[str] = OMIT,
        sender_name: typing.Optional[str] = OMIT,
        payload: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedSendEventResponse:
        """
        Parameters
        ----------
        channel_id : str

        event_name : str

        event_content : str

        source : str

        important : bool

        tags : typing.Optional[typing.Sequence[str]]

        sender_id : typing.Optional[str]

        sender_name : typing.Optional[str]

        payload : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedSendEventResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feed.sendevent(
            channel_id="channelId",
            event_name="eventName",
            event_content="eventContent",
            source="source",
            important=True,
        )
        """
        _response = self._raw_client.sendevent(
            channel_id,
            event_name=event_name,
            event_content=event_content,
            source=source,
            important=important,
            tags=tags,
            sender_id=sender_id,
            sender_name=sender_name,
            payload=payload,
            request_options=request_options,
        )
        return _response.data

    def archiveevent(
        self,
        channel_id: str,
        event_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        channel_id : str

        event_id : str

        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feed.archiveevent(
            channel_id="channelId",
            event_id="eventId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.archiveevent(
            channel_id, event_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def unarchiveevent(
        self,
        channel_id: str,
        event_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        channel_id : str

        event_id : str

        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feed.unarchiveevent(
            channel_id="channelId",
            event_id="eventId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.unarchiveevent(
            channel_id, event_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def clearallarchivedevents(
        self, channel_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> float:
        """
        Parameters
        ----------
        channel_id : str

        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feed.clearallarchivedevents(
            channel_id="channelId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.clearallarchivedevents(
            channel_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def integration_playground(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feed.integration_playground(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.integration_playground(workspace_id, request_options=request_options)
        return _response.data

    def integration_github(self, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        channel_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feed.integration_github(
            channel_id="channelId",
        )
        """
        _response = self._raw_client.integration_github(channel_id, request_options=request_options)
        return _response.data

    def integration_stripe(self, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        channel_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feed.integration_stripe(
            channel_id="channelId",
        )
        """
        _response = self._raw_client.integration_stripe(channel_id, request_options=request_options)
        return _response.data

    def integration_tencentcloudalarm(
        self, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        channel_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feed.integration_tencentcloudalarm(
            channel_id="channelId",
        )
        """
        _response = self._raw_client.integration_tencentcloudalarm(channel_id, request_options=request_options)
        return _response.data

    def integration_sentry(self, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        channel_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feed.integration_sentry(
            channel_id="channelId",
        )
        """
        _response = self._raw_client.integration_sentry(channel_id, request_options=request_options)
        return _response.data

    def state_all(
        self,
        workspace_id: str,
        *,
        channel_id: str,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[FeedStateAllResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        channel_id : str

        limit : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FeedStateAllResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feed.state_all(
            workspace_id="workspaceId",
            channel_id="channelId",
        )
        """
        _response = self._raw_client.state_all(
            workspace_id, channel_id=channel_id, limit=limit, request_options=request_options
        )
        return _response.data

    def state_upsert(
        self,
        channel_id: str,
        *,
        event_id: str,
        event_name: str,
        event_content: str,
        tags: typing.Sequence[str],
        source: str,
        important: bool,
        sender_id: typing.Optional[str] = OMIT,
        sender_name: typing.Optional[str] = OMIT,
        payload: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedStateUpsertResponse:
        """
        Parameters
        ----------
        channel_id : str

        event_id : str

        event_name : str

        event_content : str

        tags : typing.Sequence[str]

        source : str

        important : bool

        sender_id : typing.Optional[str]

        sender_name : typing.Optional[str]

        payload : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedStateUpsertResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feed.state_upsert(
            channel_id="channelId",
            event_id="eventId",
            event_name="eventName",
            event_content="eventContent",
            tags=["tags"],
            source="source",
            important=True,
        )
        """
        _response = self._raw_client.state_upsert(
            channel_id,
            event_id=event_id,
            event_name=event_name,
            event_content=event_content,
            tags=tags,
            source=source,
            important=important,
            sender_id=sender_id,
            sender_name=sender_name,
            payload=payload,
            request_options=request_options,
        )
        return _response.data

    def state_resolve(
        self,
        workspace_id: str,
        channel_id: str,
        *,
        state_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedStateResolveResponse:
        """
        Parameters
        ----------
        workspace_id : str

        channel_id : str

        state_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedStateResolveResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feed.state_resolve(
            workspace_id="workspaceId",
            channel_id="channelId",
            state_id="stateId",
        )
        """
        _response = self._raw_client.state_resolve(
            workspace_id, channel_id, state_id=state_id, request_options=request_options
        )
        return _response.data


class AsyncFeedClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFeedClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFeedClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFeedClient
        """
        return self._raw_client

    async def channels(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FeedChannelsResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FeedChannelsResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feed.channels(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.channels(workspace_id, request_options=request_options)
        return _response.data

    async def channelinfo(
        self, workspace_id: str, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[FeedChannelInfoResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        channel_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[FeedChannelInfoResponse]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feed.channelinfo(
                workspace_id="workspaceId",
                channel_id="channelId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.channelinfo(workspace_id, channel_id, request_options=request_options)
        return _response.data

    async def updatechannelinfo(
        self,
        workspace_id: str,
        channel_id: str,
        *,
        name: str,
        webhook_signature: str,
        notify_frequency: FeedUpdateChannelInfoRequestNotifyFrequency,
        notification_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[FeedUpdateChannelInfoResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        channel_id : str

        name : str

        webhook_signature : str

        notify_frequency : FeedUpdateChannelInfoRequestNotifyFrequency

        notification_ids : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[FeedUpdateChannelInfoResponse]
            Successful response

        Examples
        --------
        import asyncio

        from fern.feed import FeedUpdateChannelInfoRequestNotifyFrequency

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feed.updatechannelinfo(
                workspace_id="workspaceId",
                channel_id="channelId",
                name="name",
                webhook_signature="webhookSignature",
                notify_frequency=FeedUpdateChannelInfoRequestNotifyFrequency.NONE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatechannelinfo(
            workspace_id,
            channel_id,
            name=name,
            webhook_signature=webhook_signature,
            notify_frequency=notify_frequency,
            notification_ids=notification_ids,
            request_options=request_options,
        )
        return _response.data

    async def fetcheventsbycursor(
        self,
        workspace_id: str,
        channel_id: str,
        *,
        limit: typing.Optional[float] = None,
        cursor: typing.Optional[str] = None,
        archived: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedFetchEventsByCursorResponse:
        """
        Fetch workspace feed channel events

        Parameters
        ----------
        workspace_id : str

        channel_id : str

        limit : typing.Optional[float]

        cursor : typing.Optional[str]

        archived : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedFetchEventsByCursorResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feed.fetcheventsbycursor(
                workspace_id="workspaceId",
                channel_id="channelId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetcheventsbycursor(
            workspace_id, channel_id, limit=limit, cursor=cursor, archived=archived, request_options=request_options
        )
        return _response.data

    async def fetchpubliceventsbycursor(
        self,
        share_id: str,
        *,
        limit: typing.Optional[float] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedFetchPublicEventsByCursorResponse:
        """
        Fetch public feed channel events by shareId

        Parameters
        ----------
        share_id : str

        limit : typing.Optional[float]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedFetchPublicEventsByCursorResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feed.fetchpubliceventsbycursor(
                share_id="shareId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetchpubliceventsbycursor(
            share_id, limit=limit, cursor=cursor, request_options=request_options
        )
        return _response.data

    async def getchannelbyshareid(
        self, share_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FeedGetChannelByShareIdResponse:
        """
        Fetch public feed channel info by shareId

        Parameters
        ----------
        share_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedGetChannelByShareIdResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feed.getchannelbyshareid(
                share_id="shareId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getchannelbyshareid(share_id, request_options=request_options)
        return _response.data

    async def createchannel(
        self,
        workspace_id: str,
        *,
        name: str,
        notify_frequency: FeedCreateChannelRequestNotifyFrequency,
        notification_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedCreateChannelResponse:
        """
        Parameters
        ----------
        workspace_id : str

        name : str

        notify_frequency : FeedCreateChannelRequestNotifyFrequency

        notification_ids : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedCreateChannelResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern.feed import FeedCreateChannelRequestNotifyFrequency

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feed.createchannel(
                workspace_id="workspaceId",
                name="name",
                notify_frequency=FeedCreateChannelRequestNotifyFrequency.NONE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createchannel(
            workspace_id,
            name=name,
            notify_frequency=notify_frequency,
            notification_ids=notification_ids,
            request_options=request_options,
        )
        return _response.data

    async def refreshpublicshareid(
        self, workspace_id: str, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FeedRefreshPublicShareIdResponse:
        """
        Regenerate public share id for feed channel

        Parameters
        ----------
        workspace_id : str

        channel_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedRefreshPublicShareIdResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feed.refreshpublicshareid(
                workspace_id="workspaceId",
                channel_id="channelId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.refreshpublicshareid(
            workspace_id, channel_id, request_options=request_options
        )
        return _response.data

    async def disablepublicshareid(
        self, workspace_id: str, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FeedDisablePublicShareIdResponse:
        """
        Disable public share for feed channel

        Parameters
        ----------
        workspace_id : str

        channel_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedDisablePublicShareIdResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feed.disablepublicshareid(
                workspace_id="workspaceId",
                channel_id="channelId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.disablepublicshareid(
            workspace_id, channel_id, request_options=request_options
        )
        return _response.data

    async def deletechannel(
        self, workspace_id: str, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FeedDeleteChannelResponse:
        """
        Parameters
        ----------
        workspace_id : str

        channel_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedDeleteChannelResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feed.deletechannel(
                workspace_id="workspaceId",
                channel_id="channelId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletechannel(workspace_id, channel_id, request_options=request_options)
        return _response.data

    async def sendevent(
        self,
        channel_id: str,
        *,
        event_name: str,
        event_content: str,
        source: str,
        important: bool,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        sender_id: typing.Optional[str] = OMIT,
        sender_name: typing.Optional[str] = OMIT,
        payload: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedSendEventResponse:
        """
        Parameters
        ----------
        channel_id : str

        event_name : str

        event_content : str

        source : str

        important : bool

        tags : typing.Optional[typing.Sequence[str]]

        sender_id : typing.Optional[str]

        sender_name : typing.Optional[str]

        payload : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedSendEventResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feed.sendevent(
                channel_id="channelId",
                event_name="eventName",
                event_content="eventContent",
                source="source",
                important=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sendevent(
            channel_id,
            event_name=event_name,
            event_content=event_content,
            source=source,
            important=important,
            tags=tags,
            sender_id=sender_id,
            sender_name=sender_name,
            payload=payload,
            request_options=request_options,
        )
        return _response.data

    async def archiveevent(
        self,
        channel_id: str,
        event_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        channel_id : str

        event_id : str

        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feed.archiveevent(
                channel_id="channelId",
                event_id="eventId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.archiveevent(
            channel_id, event_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def unarchiveevent(
        self,
        channel_id: str,
        event_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        channel_id : str

        event_id : str

        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feed.unarchiveevent(
                channel_id="channelId",
                event_id="eventId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unarchiveevent(
            channel_id, event_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def clearallarchivedevents(
        self, channel_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> float:
        """
        Parameters
        ----------
        channel_id : str

        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feed.clearallarchivedevents(
                channel_id="channelId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.clearallarchivedevents(
            channel_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def integration_playground(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feed.integration_playground(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.integration_playground(workspace_id, request_options=request_options)
        return _response.data

    async def integration_github(
        self, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        channel_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feed.integration_github(
                channel_id="channelId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.integration_github(channel_id, request_options=request_options)
        return _response.data

    async def integration_stripe(
        self, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        channel_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feed.integration_stripe(
                channel_id="channelId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.integration_stripe(channel_id, request_options=request_options)
        return _response.data

    async def integration_tencentcloudalarm(
        self, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        channel_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feed.integration_tencentcloudalarm(
                channel_id="channelId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.integration_tencentcloudalarm(channel_id, request_options=request_options)
        return _response.data

    async def integration_sentry(
        self, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        channel_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feed.integration_sentry(
                channel_id="channelId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.integration_sentry(channel_id, request_options=request_options)
        return _response.data

    async def state_all(
        self,
        workspace_id: str,
        *,
        channel_id: str,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[FeedStateAllResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        channel_id : str

        limit : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FeedStateAllResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feed.state_all(
                workspace_id="workspaceId",
                channel_id="channelId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.state_all(
            workspace_id, channel_id=channel_id, limit=limit, request_options=request_options
        )
        return _response.data

    async def state_upsert(
        self,
        channel_id: str,
        *,
        event_id: str,
        event_name: str,
        event_content: str,
        tags: typing.Sequence[str],
        source: str,
        important: bool,
        sender_id: typing.Optional[str] = OMIT,
        sender_name: typing.Optional[str] = OMIT,
        payload: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedStateUpsertResponse:
        """
        Parameters
        ----------
        channel_id : str

        event_id : str

        event_name : str

        event_content : str

        tags : typing.Sequence[str]

        source : str

        important : bool

        sender_id : typing.Optional[str]

        sender_name : typing.Optional[str]

        payload : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedStateUpsertResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feed.state_upsert(
                channel_id="channelId",
                event_id="eventId",
                event_name="eventName",
                event_content="eventContent",
                tags=["tags"],
                source="source",
                important=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.state_upsert(
            channel_id,
            event_id=event_id,
            event_name=event_name,
            event_content=event_content,
            tags=tags,
            source=source,
            important=important,
            sender_id=sender_id,
            sender_name=sender_name,
            payload=payload,
            request_options=request_options,
        )
        return _response.data

    async def state_resolve(
        self,
        workspace_id: str,
        channel_id: str,
        *,
        state_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedStateResolveResponse:
        """
        Parameters
        ----------
        workspace_id : str

        channel_id : str

        state_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedStateResolveResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feed.state_resolve(
                workspace_id="workspaceId",
                channel_id="channelId",
                state_id="stateId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.state_resolve(
            workspace_id, channel_id, state_id=state_id, request_options=request_options
        )
        return _response.data
