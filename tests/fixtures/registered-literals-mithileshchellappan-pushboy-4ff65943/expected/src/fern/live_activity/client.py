

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_live_activity_job_request import CreateLiveActivityJobRequest
from ..types.live_activity_job_response import LiveActivityJobResponse
from ..types.live_activity_token_type import LiveActivityTokenType
from ..types.live_activity_user_topic_subscription import LiveActivityUserTopicSubscription
from ..types.platform import Platform
from .raw_client import AsyncRawLiveActivityClient, RawLiveActivityClient
from .types.post_v1live_activity_tokens_response import PostV1LiveActivityTokensResponse


OMIT = typing.cast(typing.Any, ...)


class LiveActivityClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLiveActivityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLiveActivityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLiveActivityClient
        """
        return self._raw_client

    def register_a_live_activity_token(
        self,
        *,
        user_id: str,
        platform: Platform,
        token_type: LiveActivityTokenType,
        token: str,
        topic_id: typing.Optional[str] = OMIT,
        activity_id: typing.Optional[str] = OMIT,
        expires_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1LiveActivityTokensResponse:
        """
        FCM tokens are stored as update tokens. APNS update tokens are capped to the default Live Activity lifetime if no sooner expiry is provided.

        Parameters
        ----------
        user_id : str

        platform : Platform

        token_type : LiveActivityTokenType

        token : str

        topic_id : typing.Optional[str]

        activity_id : typing.Optional[str]
            Associates this token with a specific Live Activity for scoped update/end fanout.

        expires_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1LiveActivityTokensResponse
            Token registered.

        Examples
        --------
        from fern import FernApi, LiveActivityTokenType, Platform

        client = FernApi()
        client.live_activity.register_a_live_activity_token(
            user_id="user-123",
            platform=Platform.APNS,
            token_type=LiveActivityTokenType.START,
            token="live-activity-token",
        )
        """
        _response = self._raw_client.register_a_live_activity_token(
            user_id=user_id,
            platform=platform,
            token_type=token_type,
            token=token,
            topic_id=topic_id,
            activity_id=activity_id,
            expires_at=expires_at,
            request_options=request_options,
        )
        return _response.data

    def invalidate_a_live_activity_token(
        self, *, user_id: str, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        user_id : str

        token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.live_activity.invalidate_a_live_activity_token(
            user_id="userId",
            token="token",
        )
        """
        _response = self._raw_client.invalidate_a_live_activity_token(
            user_id=user_id, token=token, request_options=request_options
        )
        return _response.data

    def subscribe_a_user_to_a_live_activity_topic(
        self, topic_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LiveActivityUserTopicSubscription:
        """
        Parameters
        ----------
        topic_id : str

        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LiveActivityUserTopicSubscription
            Live Activity topic subscription created.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.live_activity.subscribe_a_user_to_a_live_activity_topic(
            topic_id="broadcast",
            user_id="user-123",
        )
        """
        _response = self._raw_client.subscribe_a_user_to_a_live_activity_topic(
            topic_id, user_id, request_options=request_options
        )
        return _response.data

    def start_update_or_end_a_live_activity(
        self, *, request: CreateLiveActivityJobRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> LiveActivityJobResponse:
        """
        Parameters
        ----------
        request : CreateLiveActivityJobRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LiveActivityJobResponse
            Existing Live Activity was already started or closed.

        Examples
        --------
        from fern import (
            FernApi,
            LiveActivityOptions,
            LiveActivityOptionsAlert,
            LiveActivityOptionsPriorityZero,
            LiveActivityStartJobRequest,
            LiveActivityStartJobRequestAction,
        )

        client = FernApi()
        client.live_activity.start_update_or_end_a_live_activity(
            request=LiveActivityStartJobRequest(
                action=LiveActivityStartJobRequestAction.START,
                activity_id="order-123",
                activity_type="OrderDeliveryActivity",
                user_id="user-123",
                payload={"status": "driver_assigned", "etaMinutes": 18},
                options=LiveActivityOptions(
                    alert=LiveActivityOptionsAlert(
                        title="Order update",
                        body="Your driver is on the way.",
                    ),
                    attributes_type="OrderDeliveryAttributes",
                    attributes={"orderId": "order-123"},
                    priority=LiveActivityOptionsPriorityZero.HIGH,
                ),
            ),
        )
        """
        _response = self._raw_client.start_update_or_end_a_live_activity(
            request=request, request_options=request_options
        )
        return _response.data


class AsyncLiveActivityClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLiveActivityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLiveActivityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLiveActivityClient
        """
        return self._raw_client

    async def register_a_live_activity_token(
        self,
        *,
        user_id: str,
        platform: Platform,
        token_type: LiveActivityTokenType,
        token: str,
        topic_id: typing.Optional[str] = OMIT,
        activity_id: typing.Optional[str] = OMIT,
        expires_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1LiveActivityTokensResponse:
        """
        FCM tokens are stored as update tokens. APNS update tokens are capped to the default Live Activity lifetime if no sooner expiry is provided.

        Parameters
        ----------
        user_id : str

        platform : Platform

        token_type : LiveActivityTokenType

        token : str

        topic_id : typing.Optional[str]

        activity_id : typing.Optional[str]
            Associates this token with a specific Live Activity for scoped update/end fanout.

        expires_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1LiveActivityTokensResponse
            Token registered.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, LiveActivityTokenType, Platform

        client = AsyncFernApi()


        async def main() -> None:
            await client.live_activity.register_a_live_activity_token(
                user_id="user-123",
                platform=Platform.APNS,
                token_type=LiveActivityTokenType.START,
                token="live-activity-token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_a_live_activity_token(
            user_id=user_id,
            platform=platform,
            token_type=token_type,
            token=token,
            topic_id=topic_id,
            activity_id=activity_id,
            expires_at=expires_at,
            request_options=request_options,
        )
        return _response.data

    async def invalidate_a_live_activity_token(
        self, *, user_id: str, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        user_id : str

        token : str

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
            await client.live_activity.invalidate_a_live_activity_token(
                user_id="userId",
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.invalidate_a_live_activity_token(
            user_id=user_id, token=token, request_options=request_options
        )
        return _response.data

    async def subscribe_a_user_to_a_live_activity_topic(
        self, topic_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LiveActivityUserTopicSubscription:
        """
        Parameters
        ----------
        topic_id : str

        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LiveActivityUserTopicSubscription
            Live Activity topic subscription created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.live_activity.subscribe_a_user_to_a_live_activity_topic(
                topic_id="broadcast",
                user_id="user-123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.subscribe_a_user_to_a_live_activity_topic(
            topic_id, user_id, request_options=request_options
        )
        return _response.data

    async def start_update_or_end_a_live_activity(
        self, *, request: CreateLiveActivityJobRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> LiveActivityJobResponse:
        """
        Parameters
        ----------
        request : CreateLiveActivityJobRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LiveActivityJobResponse
            Existing Live Activity was already started or closed.

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            LiveActivityOptions,
            LiveActivityOptionsAlert,
            LiveActivityOptionsPriorityZero,
            LiveActivityStartJobRequest,
            LiveActivityStartJobRequestAction,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.live_activity.start_update_or_end_a_live_activity(
                request=LiveActivityStartJobRequest(
                    action=LiveActivityStartJobRequestAction.START,
                    activity_id="order-123",
                    activity_type="OrderDeliveryActivity",
                    user_id="user-123",
                    payload={"status": "driver_assigned", "etaMinutes": 18},
                    options=LiveActivityOptions(
                        alert=LiveActivityOptionsAlert(
                            title="Order update",
                            body="Your driver is on the way.",
                        ),
                        attributes_type="OrderDeliveryAttributes",
                        attributes={"orderId": "order-123"},
                        priority=LiveActivityOptionsPriorityZero.HIGH,
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_update_or_end_a_live_activity(
            request=request, request_options=request_options
        )
        return _response.data
