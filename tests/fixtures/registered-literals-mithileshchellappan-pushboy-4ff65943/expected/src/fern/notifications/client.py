

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.notification_payload_priority import NotificationPayloadPriority
from ..types.paginated_publish_jobs import PaginatedPublishJobs
from ..types.publish_job import PublishJob
from ..types.queued_job_response import QueuedJobResponse
from .raw_client import AsyncRawNotificationsClient, RawNotificationsClient
from .types.get_v1topics_topic_id_notifications_request_status import GetV1TopicsTopicIdNotificationsRequestStatus
from .types.get_v1users_user_id_notifications_request_status import GetV1UsersUserIdNotificationsRequestStatus


OMIT = typing.cast(typing.Any, ...)


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

    def list_notifications_eligible_for_a_user(
        self,
        user_id: str,
        *,
        status: typing.Optional[GetV1UsersUserIdNotificationsRequestStatus] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedPublishJobs:
        """
        Returns direct user sends and topic sends where the user is currently subscribed and the job effective time is on or after the subscription time. This is eligibility, not delivery history.

        Parameters
        ----------
        user_id : str

        status : typing.Optional[GetV1UsersUserIdNotificationsRequestStatus]
            Exact uppercase notification job status. Omit for no status filter.

        cursor : typing.Optional[str]
            Opaque URL-safe cursor returned by the previous page.

        limit : typing.Optional[int]
            Page size. Defaults to 50 and must be between 1 and 200.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedPublishJobs
            Eligible notification jobs ordered by effective time descending.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.notifications.list_notifications_eligible_for_a_user(
            user_id="user-123",
        )
        """
        _response = self._raw_client.list_notifications_eligible_for_a_user(
            user_id, status=status, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data

    def send_or_schedule_a_notification_to_one_user(
        self,
        user_id: str,
        *,
        scheduled_at: typing.Optional[dt.datetime] = OMIT,
        title: typing.Optional[str] = OMIT,
        body: typing.Optional[str] = OMIT,
        silent: typing.Optional[str] = OMIT,
        image_url: typing.Optional[str] = OMIT,
        sound: typing.Optional[str] = OMIT,
        badge: typing.Optional[int] = OMIT,
        data: typing.Optional[typing.Dict[str, str]] = OMIT,
        collapse_id: typing.Optional[str] = OMIT,
        priority: typing.Optional[NotificationPayloadPriority] = OMIT,
        ttl: typing.Optional[int] = OMIT,
        thread_id: typing.Optional[str] = OMIT,
        category: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QueuedJobResponse:
        """
        Parameters
        ----------
        user_id : str

        scheduled_at : typing.Optional[dt.datetime]
            Optional future RFC3339 timestamp.

        title : typing.Optional[str]

        body : typing.Optional[str]

        silent : typing.Optional[str]

        image_url : typing.Optional[str]

        sound : typing.Optional[str]

        badge : typing.Optional[int]

        data : typing.Optional[typing.Dict[str, str]]

        collapse_id : typing.Optional[str]

        priority : typing.Optional[NotificationPayloadPriority]

        ttl : typing.Optional[int]
            Seconds until expiration.

        thread_id : typing.Optional[str]

        category : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueuedJobResponse
            Job queued.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.notifications.send_or_schedule_a_notification_to_one_user(
            user_id="user-123",
        )
        """
        _response = self._raw_client.send_or_schedule_a_notification_to_one_user(
            user_id,
            scheduled_at=scheduled_at,
            title=title,
            body=body,
            silent=silent,
            image_url=image_url,
            sound=sound,
            badge=badge,
            data=data,
            collapse_id=collapse_id,
            priority=priority,
            ttl=ttl,
            thread_id=thread_id,
            category=category,
            request_options=request_options,
        )
        return _response.data

    def list_notifications_for_a_topic(
        self,
        topic_id: str,
        *,
        status: typing.Optional[GetV1TopicsTopicIdNotificationsRequestStatus] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedPublishJobs:
        """
        Parameters
        ----------
        topic_id : str

        status : typing.Optional[GetV1TopicsTopicIdNotificationsRequestStatus]
            Exact uppercase notification job status. Omit for no status filter.

        cursor : typing.Optional[str]
            Opaque URL-safe cursor returned by the previous page.

        limit : typing.Optional[int]
            Page size. Defaults to 50 and must be between 1 and 200.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedPublishJobs
            Topic notification jobs ordered by effective time descending.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.notifications.list_notifications_for_a_topic(
            topic_id="broadcast",
        )
        """
        _response = self._raw_client.list_notifications_for_a_topic(
            topic_id, status=status, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data

    def send_or_schedule_a_notification_to_a_topic(
        self,
        topic_id: str,
        *,
        scheduled_at: typing.Optional[dt.datetime] = OMIT,
        title: typing.Optional[str] = OMIT,
        body: typing.Optional[str] = OMIT,
        silent: typing.Optional[str] = OMIT,
        image_url: typing.Optional[str] = OMIT,
        sound: typing.Optional[str] = OMIT,
        badge: typing.Optional[int] = OMIT,
        data: typing.Optional[typing.Dict[str, str]] = OMIT,
        collapse_id: typing.Optional[str] = OMIT,
        priority: typing.Optional[NotificationPayloadPriority] = OMIT,
        ttl: typing.Optional[int] = OMIT,
        thread_id: typing.Optional[str] = OMIT,
        category: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QueuedJobResponse:
        """
        Parameters
        ----------
        topic_id : str

        scheduled_at : typing.Optional[dt.datetime]
            Optional future RFC3339 timestamp.

        title : typing.Optional[str]

        body : typing.Optional[str]

        silent : typing.Optional[str]

        image_url : typing.Optional[str]

        sound : typing.Optional[str]

        badge : typing.Optional[int]

        data : typing.Optional[typing.Dict[str, str]]

        collapse_id : typing.Optional[str]

        priority : typing.Optional[NotificationPayloadPriority]

        ttl : typing.Optional[int]
            Seconds until expiration.

        thread_id : typing.Optional[str]

        category : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueuedJobResponse
            Job queued.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.notifications.send_or_schedule_a_notification_to_a_topic(
            topic_id="broadcast",
        )
        """
        _response = self._raw_client.send_or_schedule_a_notification_to_a_topic(
            topic_id,
            scheduled_at=scheduled_at,
            title=title,
            body=body,
            silent=silent,
            image_url=image_url,
            sound=sound,
            badge=badge,
            data=data,
            collapse_id=collapse_id,
            priority=priority,
            ttl=ttl,
            thread_id=thread_id,
            category=category,
            request_options=request_options,
        )
        return _response.data

    def get_notification_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PublishJob:
        """
        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublishJob
            Notification job.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.notifications.get_notification_job(
            job_id="018f7b7a-a9b7-7a22-9d6f-6fb3c9b6b9c0",
        )
        """
        _response = self._raw_client.get_notification_job(job_id, request_options=request_options)
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

    async def list_notifications_eligible_for_a_user(
        self,
        user_id: str,
        *,
        status: typing.Optional[GetV1UsersUserIdNotificationsRequestStatus] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedPublishJobs:
        """
        Returns direct user sends and topic sends where the user is currently subscribed and the job effective time is on or after the subscription time. This is eligibility, not delivery history.

        Parameters
        ----------
        user_id : str

        status : typing.Optional[GetV1UsersUserIdNotificationsRequestStatus]
            Exact uppercase notification job status. Omit for no status filter.

        cursor : typing.Optional[str]
            Opaque URL-safe cursor returned by the previous page.

        limit : typing.Optional[int]
            Page size. Defaults to 50 and must be between 1 and 200.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedPublishJobs
            Eligible notification jobs ordered by effective time descending.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.notifications.list_notifications_eligible_for_a_user(
                user_id="user-123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_notifications_eligible_for_a_user(
            user_id, status=status, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data

    async def send_or_schedule_a_notification_to_one_user(
        self,
        user_id: str,
        *,
        scheduled_at: typing.Optional[dt.datetime] = OMIT,
        title: typing.Optional[str] = OMIT,
        body: typing.Optional[str] = OMIT,
        silent: typing.Optional[str] = OMIT,
        image_url: typing.Optional[str] = OMIT,
        sound: typing.Optional[str] = OMIT,
        badge: typing.Optional[int] = OMIT,
        data: typing.Optional[typing.Dict[str, str]] = OMIT,
        collapse_id: typing.Optional[str] = OMIT,
        priority: typing.Optional[NotificationPayloadPriority] = OMIT,
        ttl: typing.Optional[int] = OMIT,
        thread_id: typing.Optional[str] = OMIT,
        category: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QueuedJobResponse:
        """
        Parameters
        ----------
        user_id : str

        scheduled_at : typing.Optional[dt.datetime]
            Optional future RFC3339 timestamp.

        title : typing.Optional[str]

        body : typing.Optional[str]

        silent : typing.Optional[str]

        image_url : typing.Optional[str]

        sound : typing.Optional[str]

        badge : typing.Optional[int]

        data : typing.Optional[typing.Dict[str, str]]

        collapse_id : typing.Optional[str]

        priority : typing.Optional[NotificationPayloadPriority]

        ttl : typing.Optional[int]
            Seconds until expiration.

        thread_id : typing.Optional[str]

        category : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueuedJobResponse
            Job queued.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.notifications.send_or_schedule_a_notification_to_one_user(
                user_id="user-123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_or_schedule_a_notification_to_one_user(
            user_id,
            scheduled_at=scheduled_at,
            title=title,
            body=body,
            silent=silent,
            image_url=image_url,
            sound=sound,
            badge=badge,
            data=data,
            collapse_id=collapse_id,
            priority=priority,
            ttl=ttl,
            thread_id=thread_id,
            category=category,
            request_options=request_options,
        )
        return _response.data

    async def list_notifications_for_a_topic(
        self,
        topic_id: str,
        *,
        status: typing.Optional[GetV1TopicsTopicIdNotificationsRequestStatus] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedPublishJobs:
        """
        Parameters
        ----------
        topic_id : str

        status : typing.Optional[GetV1TopicsTopicIdNotificationsRequestStatus]
            Exact uppercase notification job status. Omit for no status filter.

        cursor : typing.Optional[str]
            Opaque URL-safe cursor returned by the previous page.

        limit : typing.Optional[int]
            Page size. Defaults to 50 and must be between 1 and 200.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedPublishJobs
            Topic notification jobs ordered by effective time descending.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.notifications.list_notifications_for_a_topic(
                topic_id="broadcast",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_notifications_for_a_topic(
            topic_id, status=status, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data

    async def send_or_schedule_a_notification_to_a_topic(
        self,
        topic_id: str,
        *,
        scheduled_at: typing.Optional[dt.datetime] = OMIT,
        title: typing.Optional[str] = OMIT,
        body: typing.Optional[str] = OMIT,
        silent: typing.Optional[str] = OMIT,
        image_url: typing.Optional[str] = OMIT,
        sound: typing.Optional[str] = OMIT,
        badge: typing.Optional[int] = OMIT,
        data: typing.Optional[typing.Dict[str, str]] = OMIT,
        collapse_id: typing.Optional[str] = OMIT,
        priority: typing.Optional[NotificationPayloadPriority] = OMIT,
        ttl: typing.Optional[int] = OMIT,
        thread_id: typing.Optional[str] = OMIT,
        category: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QueuedJobResponse:
        """
        Parameters
        ----------
        topic_id : str

        scheduled_at : typing.Optional[dt.datetime]
            Optional future RFC3339 timestamp.

        title : typing.Optional[str]

        body : typing.Optional[str]

        silent : typing.Optional[str]

        image_url : typing.Optional[str]

        sound : typing.Optional[str]

        badge : typing.Optional[int]

        data : typing.Optional[typing.Dict[str, str]]

        collapse_id : typing.Optional[str]

        priority : typing.Optional[NotificationPayloadPriority]

        ttl : typing.Optional[int]
            Seconds until expiration.

        thread_id : typing.Optional[str]

        category : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueuedJobResponse
            Job queued.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.notifications.send_or_schedule_a_notification_to_a_topic(
                topic_id="broadcast",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_or_schedule_a_notification_to_a_topic(
            topic_id,
            scheduled_at=scheduled_at,
            title=title,
            body=body,
            silent=silent,
            image_url=image_url,
            sound=sound,
            badge=badge,
            data=data,
            collapse_id=collapse_id,
            priority=priority,
            ttl=ttl,
            thread_id=thread_id,
            category=category,
            request_options=request_options,
        )
        return _response.data

    async def get_notification_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PublishJob:
        """
        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublishJob
            Notification job.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.notifications.get_notification_job(
                job_id="018f7b7a-a9b7-7a22-9d6f-6fb3c9b6b9c0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_notification_job(job_id, request_options=request_options)
        return _response.data
