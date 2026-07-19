

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.feeds_list_feeds_request_offset import FeedsListFeedsRequestOffset
from ..types.feeds_list_subscriptions_request_offset import FeedsListSubscriptionsRequestOffset
from .raw_client import AsyncRawFeedsClient, RawFeedsClient
from .types.feeds_backfill_subscription_response import FeedsBackfillSubscriptionResponse
from .types.feeds_create_feed_response import FeedsCreateFeedResponse
from .types.feeds_delete_feed_request_body import FeedsDeleteFeedRequestBody
from .types.feeds_delete_feed_response import FeedsDeleteFeedResponse
from .types.feeds_delete_subscription_request_body import FeedsDeleteSubscriptionRequestBody
from .types.feeds_delete_subscription_response import FeedsDeleteSubscriptionResponse
from .types.feeds_get_feed_response import FeedsGetFeedResponse
from .types.feeds_get_message_response import FeedsGetMessageResponse
from .types.feeds_list_feeds_response import FeedsListFeedsResponse
from .types.feeds_list_messages_response import FeedsListMessagesResponse
from .types.feeds_list_subscription_history_response import FeedsListSubscriptionHistoryResponse
from .types.feeds_list_subscriptions_response import FeedsListSubscriptionsResponse
from .types.feeds_publish_messages_request_messages_item import FeedsPublishMessagesRequestMessagesItem
from .types.feeds_publish_messages_response import FeedsPublishMessagesResponse
from .types.feeds_subscribe_agent_response import FeedsSubscribeAgentResponse
from .types.feeds_trigger_subscription_response import FeedsTriggerSubscriptionResponse
from .types.feeds_unsubscribe_agent_response import FeedsUnsubscribeAgentResponse
from .types.feeds_update_all_subscriptions_cron_response import FeedsUpdateAllSubscriptionsCronResponse
from .types.feeds_update_subscription_response import FeedsUpdateSubscriptionResponse


OMIT = typing.cast(typing.Any, ...)


class FeedsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFeedsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFeedsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFeedsClient
        """
        return self._raw_client

    def listfeeds(
        self,
        *,
        project_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        limit: typing.Optional[str] = None,
        offset: typing.Optional[FeedsListFeedsRequestOffset] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedsListFeedsResponse:
        """
        List all feeds with optional filters and pagination

        Parameters
        ----------
        project_id : typing.Optional[str]

        name : typing.Optional[str]

        limit : typing.Optional[str]

        offset : typing.Optional[FeedsListFeedsRequestOffset]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsListFeedsResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feeds.listfeeds()
        """
        _response = self._raw_client.listfeeds(
            project_id=project_id, name=name, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def createfeed(
        self,
        *,
        project_id: str,
        name: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedsCreateFeedResponse:
        """
        Create a new feed in a project

        Parameters
        ----------
        project_id : str

        name : str

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsCreateFeedResponse
            201

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feeds.createfeed(
            project_id="project_id",
            name="name",
        )
        """
        _response = self._raw_client.createfeed(
            project_id=project_id, name=name, description=description, request_options=request_options
        )
        return _response.data

    def getfeed(self, feed_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> FeedsGetFeedResponse:
        """
        Retrieve feed details by ID

        Parameters
        ----------
        feed_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsGetFeedResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feeds.getfeed(
            feed_id="feed_id",
        )
        """
        _response = self._raw_client.getfeed(feed_id, request_options=request_options)
        return _response.data

    def deletefeed(
        self,
        feed_id: str,
        *,
        request: typing.Optional[FeedsDeleteFeedRequestBody] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedsDeleteFeedResponse:
        """
        Soft delete a feed and clean up its sequence

        Parameters
        ----------
        feed_id : str

        request : typing.Optional[FeedsDeleteFeedRequestBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsDeleteFeedResponse
            200

        Examples
        --------
        from fern.feeds import FeedsDeleteFeedRequestBody

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feeds.deletefeed(
            feed_id="feed_id",
            request=FeedsDeleteFeedRequestBody(),
        )
        """
        _response = self._raw_client.deletefeed(feed_id, request=request, request_options=request_options)
        return _response.data

    def listmessages(
        self,
        feed_id: str,
        *,
        after_sequence: typing.Optional[str] = None,
        limit: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedsListMessagesResponse:
        """
        List messages from a feed (for debugging/inspection)

        Parameters
        ----------
        feed_id : str

        after_sequence : typing.Optional[str]

        limit : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsListMessagesResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feeds.listmessages(
            feed_id="feed_id",
        )
        """
        _response = self._raw_client.listmessages(
            feed_id, after_sequence=after_sequence, limit=limit, request_options=request_options
        )
        return _response.data

    def publishmessages(
        self,
        feed_id: str,
        *,
        messages: typing.Sequence[FeedsPublishMessagesRequestMessagesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedsPublishMessagesResponse:
        """
        Batch insert messages into a feed (up to 10,000 per request)

        Parameters
        ----------
        feed_id : str

        messages : typing.Sequence[FeedsPublishMessagesRequestMessagesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsPublishMessagesResponse
            201

        Examples
        --------
        from fern.feeds import FeedsPublishMessagesRequestMessagesItem

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feeds.publishmessages(
            feed_id="feed_id",
            messages=[
                FeedsPublishMessagesRequestMessagesItem(
                    content="content",
                )
            ],
        )
        """
        _response = self._raw_client.publishmessages(feed_id, messages=messages, request_options=request_options)
        return _response.data

    def getmessage(
        self, feed_id: str, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FeedsGetMessageResponse:
        """
        Get full content of a feed message

        Parameters
        ----------
        feed_id : str

        message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsGetMessageResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feeds.getmessage(
            feed_id="feed_id",
            message_id="message_id",
        )
        """
        _response = self._raw_client.getmessage(feed_id, message_id, request_options=request_options)
        return _response.data

    def subscribeagent(
        self,
        feed_id: str,
        *,
        agent_id: str,
        cron_schedule: str,
        prompt_template: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedsSubscribeAgentResponse:
        """
        Subscribe an agent to a feed with polling configuration

        Parameters
        ----------
        feed_id : str

        agent_id : str

        cron_schedule : str

        prompt_template : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsSubscribeAgentResponse
            201

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feeds.subscribeagent(
            feed_id="feed_id",
            agent_id="agent_id",
            cron_schedule="cron_schedule",
        )
        """
        _response = self._raw_client.subscribeagent(
            feed_id,
            agent_id=agent_id,
            cron_schedule=cron_schedule,
            prompt_template=prompt_template,
            request_options=request_options,
        )
        return _response.data

    def deletesubscription(
        self,
        feed_id: str,
        subscription_id: str,
        *,
        request: typing.Optional[FeedsDeleteSubscriptionRequestBody] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedsDeleteSubscriptionResponse:
        """
        Remove agent subscription from a feed (by subscription_id)

        Parameters
        ----------
        feed_id : str

        subscription_id : str

        request : typing.Optional[FeedsDeleteSubscriptionRequestBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsDeleteSubscriptionResponse
            200

        Examples
        --------
        from fern.feeds import FeedsDeleteSubscriptionRequestBody

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feeds.deletesubscription(
            feed_id="feed_id",
            subscription_id="subscription_id",
            request=FeedsDeleteSubscriptionRequestBody(),
        )
        """
        _response = self._raw_client.deletesubscription(
            feed_id, subscription_id, request=request, request_options=request_options
        )
        return _response.data

    def updatesubscription(
        self,
        feed_id: str,
        subscription_id: str,
        *,
        cron_schedule: typing.Optional[str] = OMIT,
        prompt_template: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedsUpdateSubscriptionResponse:
        """
        Update subscription configuration (cron schedule, enable/disable)

        Parameters
        ----------
        feed_id : str

        subscription_id : str

        cron_schedule : typing.Optional[str]

        prompt_template : typing.Optional[str]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsUpdateSubscriptionResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feeds.updatesubscription(
            feed_id="feed_id",
            subscription_id="subscription_id",
        )
        """
        _response = self._raw_client.updatesubscription(
            feed_id,
            subscription_id,
            cron_schedule=cron_schedule,
            prompt_template=prompt_template,
            disabled=disabled,
            request_options=request_options,
        )
        return _response.data

    def unsubscribeagent(
        self, feed_id: str, *, agent_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FeedsUnsubscribeAgentResponse:
        """
        Remove agent subscription from a feed (by agent_id)

        Parameters
        ----------
        feed_id : str

        agent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsUnsubscribeAgentResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feeds.unsubscribeagent(
            feed_id="feed_id",
            agent_id="agent_id",
        )
        """
        _response = self._raw_client.unsubscribeagent(feed_id, agent_id=agent_id, request_options=request_options)
        return _response.data

    def triggersubscription(
        self, feed_id: str, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FeedsTriggerSubscriptionResponse:
        """
        Immediately trigger a subscription to process pending messages

        Parameters
        ----------
        feed_id : str

        subscription_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsTriggerSubscriptionResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feeds.triggersubscription(
            feed_id="feed_id",
            subscription_id="subscription_id",
        )
        """
        _response = self._raw_client.triggersubscription(feed_id, subscription_id, request_options=request_options)
        return _response.data

    def backfillsubscription(
        self,
        feed_id: str,
        subscription_id: str,
        *,
        from_sequence: typing.Optional[float] = OMIT,
        to_sequence: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedsBackfillSubscriptionResponse:
        """
        Start a background job to send historical messages to an agent subscription. Returns immediately with workflow ID. Does not update last_consumed_sequence.

        Parameters
        ----------
        feed_id : str

        subscription_id : str

        from_sequence : typing.Optional[float]

        to_sequence : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsBackfillSubscriptionResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feeds.backfillsubscription(
            feed_id="feed_id",
            subscription_id="subscription_id",
        )
        """
        _response = self._raw_client.backfillsubscription(
            feed_id,
            subscription_id,
            from_sequence=from_sequence,
            to_sequence=to_sequence,
            request_options=request_options,
        )
        return _response.data

    def listsubscriptionhistory(
        self,
        feed_id: str,
        subscription_id: str,
        *,
        page_size: typing.Optional[str] = None,
        next_page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedsListSubscriptionHistoryResponse:
        """
        List the run history for a subscription including scheduled runs, manual triggers, and backfills.

        Parameters
        ----------
        feed_id : str

        subscription_id : str

        page_size : typing.Optional[str]

        next_page_token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsListSubscriptionHistoryResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feeds.listsubscriptionhistory(
            feed_id="feed_id",
            subscription_id="subscription_id",
        )
        """
        _response = self._raw_client.listsubscriptionhistory(
            feed_id,
            subscription_id,
            page_size=page_size,
            next_page_token=next_page_token,
            request_options=request_options,
        )
        return _response.data

    def updateallsubscriptionscron(
        self, feed_id: str, *, cron_schedule: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FeedsUpdateAllSubscriptionsCronResponse:
        """
        Update the cron schedule for all subscriptions of a feed

        Parameters
        ----------
        feed_id : str

        cron_schedule : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsUpdateAllSubscriptionsCronResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feeds.updateallsubscriptionscron(
            feed_id="feed_id",
            cron_schedule="cron_schedule",
        )
        """
        _response = self._raw_client.updateallsubscriptionscron(
            feed_id, cron_schedule=cron_schedule, request_options=request_options
        )
        return _response.data

    def listsubscriptions(
        self,
        feed_id: str,
        *,
        limit: typing.Optional[str] = None,
        offset: typing.Optional[FeedsListSubscriptionsRequestOffset] = None,
        agent_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedsListSubscriptionsResponse:
        """
        List all agent subscriptions for a feed

        Parameters
        ----------
        feed_id : str

        limit : typing.Optional[str]

        offset : typing.Optional[FeedsListSubscriptionsRequestOffset]

        agent_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsListSubscriptionsResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feeds.listsubscriptions(
            feed_id="feed_id",
        )
        """
        _response = self._raw_client.listsubscriptions(
            feed_id, limit=limit, offset=offset, agent_id=agent_id, request_options=request_options
        )
        return _response.data


class AsyncFeedsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFeedsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFeedsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFeedsClient
        """
        return self._raw_client

    async def listfeeds(
        self,
        *,
        project_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        limit: typing.Optional[str] = None,
        offset: typing.Optional[FeedsListFeedsRequestOffset] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedsListFeedsResponse:
        """
        List all feeds with optional filters and pagination

        Parameters
        ----------
        project_id : typing.Optional[str]

        name : typing.Optional[str]

        limit : typing.Optional[str]

        offset : typing.Optional[FeedsListFeedsRequestOffset]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsListFeedsResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feeds.listfeeds()


        asyncio.run(main())
        """
        _response = await self._raw_client.listfeeds(
            project_id=project_id, name=name, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def createfeed(
        self,
        *,
        project_id: str,
        name: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedsCreateFeedResponse:
        """
        Create a new feed in a project

        Parameters
        ----------
        project_id : str

        name : str

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsCreateFeedResponse
            201

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feeds.createfeed(
                project_id="project_id",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createfeed(
            project_id=project_id, name=name, description=description, request_options=request_options
        )
        return _response.data

    async def getfeed(
        self, feed_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FeedsGetFeedResponse:
        """
        Retrieve feed details by ID

        Parameters
        ----------
        feed_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsGetFeedResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feeds.getfeed(
                feed_id="feed_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getfeed(feed_id, request_options=request_options)
        return _response.data

    async def deletefeed(
        self,
        feed_id: str,
        *,
        request: typing.Optional[FeedsDeleteFeedRequestBody] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedsDeleteFeedResponse:
        """
        Soft delete a feed and clean up its sequence

        Parameters
        ----------
        feed_id : str

        request : typing.Optional[FeedsDeleteFeedRequestBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsDeleteFeedResponse
            200

        Examples
        --------
        import asyncio

        from fern.feeds import FeedsDeleteFeedRequestBody

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feeds.deletefeed(
                feed_id="feed_id",
                request=FeedsDeleteFeedRequestBody(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletefeed(feed_id, request=request, request_options=request_options)
        return _response.data

    async def listmessages(
        self,
        feed_id: str,
        *,
        after_sequence: typing.Optional[str] = None,
        limit: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedsListMessagesResponse:
        """
        List messages from a feed (for debugging/inspection)

        Parameters
        ----------
        feed_id : str

        after_sequence : typing.Optional[str]

        limit : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsListMessagesResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feeds.listmessages(
                feed_id="feed_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listmessages(
            feed_id, after_sequence=after_sequence, limit=limit, request_options=request_options
        )
        return _response.data

    async def publishmessages(
        self,
        feed_id: str,
        *,
        messages: typing.Sequence[FeedsPublishMessagesRequestMessagesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedsPublishMessagesResponse:
        """
        Batch insert messages into a feed (up to 10,000 per request)

        Parameters
        ----------
        feed_id : str

        messages : typing.Sequence[FeedsPublishMessagesRequestMessagesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsPublishMessagesResponse
            201

        Examples
        --------
        import asyncio

        from fern.feeds import FeedsPublishMessagesRequestMessagesItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feeds.publishmessages(
                feed_id="feed_id",
                messages=[
                    FeedsPublishMessagesRequestMessagesItem(
                        content="content",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.publishmessages(feed_id, messages=messages, request_options=request_options)
        return _response.data

    async def getmessage(
        self, feed_id: str, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FeedsGetMessageResponse:
        """
        Get full content of a feed message

        Parameters
        ----------
        feed_id : str

        message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsGetMessageResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feeds.getmessage(
                feed_id="feed_id",
                message_id="message_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getmessage(feed_id, message_id, request_options=request_options)
        return _response.data

    async def subscribeagent(
        self,
        feed_id: str,
        *,
        agent_id: str,
        cron_schedule: str,
        prompt_template: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedsSubscribeAgentResponse:
        """
        Subscribe an agent to a feed with polling configuration

        Parameters
        ----------
        feed_id : str

        agent_id : str

        cron_schedule : str

        prompt_template : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsSubscribeAgentResponse
            201

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feeds.subscribeagent(
                feed_id="feed_id",
                agent_id="agent_id",
                cron_schedule="cron_schedule",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.subscribeagent(
            feed_id,
            agent_id=agent_id,
            cron_schedule=cron_schedule,
            prompt_template=prompt_template,
            request_options=request_options,
        )
        return _response.data

    async def deletesubscription(
        self,
        feed_id: str,
        subscription_id: str,
        *,
        request: typing.Optional[FeedsDeleteSubscriptionRequestBody] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedsDeleteSubscriptionResponse:
        """
        Remove agent subscription from a feed (by subscription_id)

        Parameters
        ----------
        feed_id : str

        subscription_id : str

        request : typing.Optional[FeedsDeleteSubscriptionRequestBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsDeleteSubscriptionResponse
            200

        Examples
        --------
        import asyncio

        from fern.feeds import FeedsDeleteSubscriptionRequestBody

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feeds.deletesubscription(
                feed_id="feed_id",
                subscription_id="subscription_id",
                request=FeedsDeleteSubscriptionRequestBody(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletesubscription(
            feed_id, subscription_id, request=request, request_options=request_options
        )
        return _response.data

    async def updatesubscription(
        self,
        feed_id: str,
        subscription_id: str,
        *,
        cron_schedule: typing.Optional[str] = OMIT,
        prompt_template: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedsUpdateSubscriptionResponse:
        """
        Update subscription configuration (cron schedule, enable/disable)

        Parameters
        ----------
        feed_id : str

        subscription_id : str

        cron_schedule : typing.Optional[str]

        prompt_template : typing.Optional[str]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsUpdateSubscriptionResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feeds.updatesubscription(
                feed_id="feed_id",
                subscription_id="subscription_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatesubscription(
            feed_id,
            subscription_id,
            cron_schedule=cron_schedule,
            prompt_template=prompt_template,
            disabled=disabled,
            request_options=request_options,
        )
        return _response.data

    async def unsubscribeagent(
        self, feed_id: str, *, agent_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FeedsUnsubscribeAgentResponse:
        """
        Remove agent subscription from a feed (by agent_id)

        Parameters
        ----------
        feed_id : str

        agent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsUnsubscribeAgentResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feeds.unsubscribeagent(
                feed_id="feed_id",
                agent_id="agent_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unsubscribeagent(feed_id, agent_id=agent_id, request_options=request_options)
        return _response.data

    async def triggersubscription(
        self, feed_id: str, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FeedsTriggerSubscriptionResponse:
        """
        Immediately trigger a subscription to process pending messages

        Parameters
        ----------
        feed_id : str

        subscription_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsTriggerSubscriptionResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feeds.triggersubscription(
                feed_id="feed_id",
                subscription_id="subscription_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.triggersubscription(
            feed_id, subscription_id, request_options=request_options
        )
        return _response.data

    async def backfillsubscription(
        self,
        feed_id: str,
        subscription_id: str,
        *,
        from_sequence: typing.Optional[float] = OMIT,
        to_sequence: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedsBackfillSubscriptionResponse:
        """
        Start a background job to send historical messages to an agent subscription. Returns immediately with workflow ID. Does not update last_consumed_sequence.

        Parameters
        ----------
        feed_id : str

        subscription_id : str

        from_sequence : typing.Optional[float]

        to_sequence : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsBackfillSubscriptionResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feeds.backfillsubscription(
                feed_id="feed_id",
                subscription_id="subscription_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.backfillsubscription(
            feed_id,
            subscription_id,
            from_sequence=from_sequence,
            to_sequence=to_sequence,
            request_options=request_options,
        )
        return _response.data

    async def listsubscriptionhistory(
        self,
        feed_id: str,
        subscription_id: str,
        *,
        page_size: typing.Optional[str] = None,
        next_page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedsListSubscriptionHistoryResponse:
        """
        List the run history for a subscription including scheduled runs, manual triggers, and backfills.

        Parameters
        ----------
        feed_id : str

        subscription_id : str

        page_size : typing.Optional[str]

        next_page_token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsListSubscriptionHistoryResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feeds.listsubscriptionhistory(
                feed_id="feed_id",
                subscription_id="subscription_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listsubscriptionhistory(
            feed_id,
            subscription_id,
            page_size=page_size,
            next_page_token=next_page_token,
            request_options=request_options,
        )
        return _response.data

    async def updateallsubscriptionscron(
        self, feed_id: str, *, cron_schedule: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FeedsUpdateAllSubscriptionsCronResponse:
        """
        Update the cron schedule for all subscriptions of a feed

        Parameters
        ----------
        feed_id : str

        cron_schedule : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsUpdateAllSubscriptionsCronResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feeds.updateallsubscriptionscron(
                feed_id="feed_id",
                cron_schedule="cron_schedule",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updateallsubscriptionscron(
            feed_id, cron_schedule=cron_schedule, request_options=request_options
        )
        return _response.data

    async def listsubscriptions(
        self,
        feed_id: str,
        *,
        limit: typing.Optional[str] = None,
        offset: typing.Optional[FeedsListSubscriptionsRequestOffset] = None,
        agent_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedsListSubscriptionsResponse:
        """
        List all agent subscriptions for a feed

        Parameters
        ----------
        feed_id : str

        limit : typing.Optional[str]

        offset : typing.Optional[FeedsListSubscriptionsRequestOffset]

        agent_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedsListSubscriptionsResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feeds.listsubscriptions(
                feed_id="feed_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listsubscriptions(
            feed_id, limit=limit, offset=offset, agent_id=agent_id, request_options=request_options
        )
        return _response.data
