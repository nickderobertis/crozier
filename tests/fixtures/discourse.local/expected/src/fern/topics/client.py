

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTopicsClient, RawTopicsClient
from .types.create_topic_timer_response import CreateTopicTimerResponse
from .types.get_specific_posts_from_topic_response import GetSpecificPostsFromTopicResponse
from .types.get_topic_response import GetTopicResponse
from .types.invite_to_topic_response import InviteToTopicResponse
from .types.list_latest_topics_response import ListLatestTopicsResponse
from .types.list_top_topics_response import ListTopTopicsResponse
from .types.set_notification_level_request_notification_level import SetNotificationLevelRequestNotificationLevel
from .types.set_notification_level_response import SetNotificationLevelResponse
from .types.update_topic_request_topic import UpdateTopicRequestTopic
from .types.update_topic_response import UpdateTopicResponse
from .types.update_topic_status_request_enabled import UpdateTopicStatusRequestEnabled
from .types.update_topic_status_request_status import UpdateTopicStatusRequestStatus
from .types.update_topic_status_response import UpdateTopicStatusResponse
from .types.update_topic_timestamp_response import UpdateTopicTimestampResponse


OMIT = typing.cast(typing.Any, ...)


class TopicsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTopicsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTopicsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTopicsClient
        """
        return self._raw_client

    def list_latest_topics(
        self,
        *,
        api_key: str,
        api_username: str,
        order: typing.Optional[str] = None,
        ascending: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListLatestTopicsResponse:
        """
        Parameters
        ----------
        api_key : str

        api_username : str

        order : typing.Optional[str]
            Enum: `default`, `created`, `activity`, `views`, `posts`, `category`,
            `likes`, `op_likes`, `posters`

        ascending : typing.Optional[str]
            Defaults to `desc`, add `ascending=true` to sort asc

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListLatestTopicsResponse
            topic updated

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.topics.list_latest_topics(
            api_key="Api-Key",
            api_username="Api-Username",
        )
        """
        _response = self._raw_client.list_latest_topics(
            api_key=api_key,
            api_username=api_username,
            order=order,
            ascending=ascending,
            request_options=request_options,
        )
        return _response.data

    def update_topic(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        topic: typing.Optional[UpdateTopicRequestTopic] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateTopicResponse:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        topic : typing.Optional[UpdateTopicRequestTopic]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateTopicResponse
            topic updated

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.topics.update_topic(
            id="id",
            api_key="Api-Key",
            api_username="Api-Username",
        )
        """
        _response = self._raw_client.update_topic(
            id, api_key=api_key, api_username=api_username, topic=topic, request_options=request_options
        )
        return _response.data

    def get_topic_by_external_id(
        self, external_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        external_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.topics.get_topic_by_external_id(
            external_id="external_id",
        )
        """
        _response = self._raw_client.get_topic_by_external_id(external_id, request_options=request_options)
        return _response.data

    def get_topic(
        self, id: str, *, api_key: str, api_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTopicResponse:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTopicResponse
            specific posts

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.topics.get_topic(
            id="id",
            api_key="Api-Key",
            api_username="Api-Username",
        )
        """
        _response = self._raw_client.get_topic(
            id, api_key=api_key, api_username=api_username, request_options=request_options
        )
        return _response.data

    def remove_topic(
        self, id: str, *, api_key: str, api_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.topics.remove_topic(
            id="id",
            api_key="Api-Key",
            api_username="Api-Username",
        )
        """
        _response = self._raw_client.remove_topic(
            id, api_key=api_key, api_username=api_username, request_options=request_options
        )
        return _response.data

    def bookmark_topic(
        self, id: str, *, api_key: str, api_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.topics.bookmark_topic(
            id="id",
            api_key="Api-Key",
            api_username="Api-Username",
        )
        """
        _response = self._raw_client.bookmark_topic(
            id, api_key=api_key, api_username=api_username, request_options=request_options
        )
        return _response.data

    def update_topic_timestamp(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        timestamp: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateTopicTimestampResponse:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        timestamp : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateTopicTimestampResponse
            topic updated

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.topics.update_topic_timestamp(
            id="id",
            api_key="Api-Key",
            api_username="Api-Username",
            timestamp="1594291380",
        )
        """
        _response = self._raw_client.update_topic_timestamp(
            id, api_key=api_key, api_username=api_username, timestamp=timestamp, request_options=request_options
        )
        return _response.data

    def invite_to_topic(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        email: typing.Optional[str] = OMIT,
        user: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InviteToTopicResponse:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        email : typing.Optional[str]

        user : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InviteToTopicResponse
            topic updated

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.topics.invite_to_topic(
            id="id",
            api_key="Api-Key",
            api_username="Api-Username",
        )
        """
        _response = self._raw_client.invite_to_topic(
            id, api_key=api_key, api_username=api_username, email=email, user=user, request_options=request_options
        )
        return _response.data

    def set_notification_level(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        notification_level: SetNotificationLevelRequestNotificationLevel,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SetNotificationLevelResponse:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        notification_level : SetNotificationLevelRequestNotificationLevel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SetNotificationLevelResponse
            topic updated

        Examples
        --------
        from fern.topics import SetNotificationLevelRequestNotificationLevel

        from fern import FernApi

        client = FernApi()
        client.topics.set_notification_level(
            id="id",
            api_key="Api-Key",
            api_username="Api-Username",
            notification_level=SetNotificationLevelRequestNotificationLevel.ZERO,
        )
        """
        _response = self._raw_client.set_notification_level(
            id,
            api_key=api_key,
            api_username=api_username,
            notification_level=notification_level,
            request_options=request_options,
        )
        return _response.data

    def get_specific_posts_from_topic(
        self, id: str, *, api_key: str, api_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSpecificPostsFromTopicResponse:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSpecificPostsFromTopicResponse
            specific posts

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.topics.get_specific_posts_from_topic(
            id="id",
            api_key="Api-Key",
            api_username="Api-Username",
        )
        """
        _response = self._raw_client.get_specific_posts_from_topic(
            id, api_key=api_key, api_username=api_username, request_options=request_options
        )
        return _response.data

    def update_topic_status(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        enabled: UpdateTopicStatusRequestEnabled,
        status: UpdateTopicStatusRequestStatus,
        until: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateTopicStatusResponse:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        enabled : UpdateTopicStatusRequestEnabled

        status : UpdateTopicStatusRequestStatus

        until : typing.Optional[str]
            Only required for `pinned` and `pinned_globally`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateTopicStatusResponse
            topic updated

        Examples
        --------
        from fern.topics import (
            UpdateTopicStatusRequestEnabled,
            UpdateTopicStatusRequestStatus,
        )

        from fern import FernApi

        client = FernApi()
        client.topics.update_topic_status(
            id="id",
            api_key="Api-Key",
            api_username="Api-Username",
            enabled=UpdateTopicStatusRequestEnabled.TRUE,
            status=UpdateTopicStatusRequestStatus.CLOSED,
        )
        """
        _response = self._raw_client.update_topic_status(
            id,
            api_key=api_key,
            api_username=api_username,
            enabled=enabled,
            status=status,
            until=until,
            request_options=request_options,
        )
        return _response.data

    def create_topic_timer(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        based_on_last_post: typing.Optional[bool] = OMIT,
        category_id: typing.Optional[int] = OMIT,
        status_type: typing.Optional[str] = OMIT,
        time: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTopicTimerResponse:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        based_on_last_post : typing.Optional[bool]

        category_id : typing.Optional[int]

        status_type : typing.Optional[str]

        time : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTopicTimerResponse
            topic updated

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.topics.create_topic_timer(
            id="id",
            api_key="Api-Key",
            api_username="Api-Username",
        )
        """
        _response = self._raw_client.create_topic_timer(
            id,
            api_key=api_key,
            api_username=api_username,
            based_on_last_post=based_on_last_post,
            category_id=category_id,
            status_type=status_type,
            time=time,
            request_options=request_options,
        )
        return _response.data

    def list_top_topics(
        self,
        *,
        api_key: str,
        api_username: str,
        period: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListTopTopicsResponse:
        """
        Parameters
        ----------
        api_key : str

        api_username : str

        period : typing.Optional[str]
            Enum: `all`, `yearly`, `quarterly`, `monthly`, `weekly`, `daily`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListTopTopicsResponse
            response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.topics.list_top_topics(
            api_key="Api-Key",
            api_username="Api-Username",
        )
        """
        _response = self._raw_client.list_top_topics(
            api_key=api_key, api_username=api_username, period=period, request_options=request_options
        )
        return _response.data


class AsyncTopicsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTopicsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTopicsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTopicsClient
        """
        return self._raw_client

    async def list_latest_topics(
        self,
        *,
        api_key: str,
        api_username: str,
        order: typing.Optional[str] = None,
        ascending: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListLatestTopicsResponse:
        """
        Parameters
        ----------
        api_key : str

        api_username : str

        order : typing.Optional[str]
            Enum: `default`, `created`, `activity`, `views`, `posts`, `category`,
            `likes`, `op_likes`, `posters`

        ascending : typing.Optional[str]
            Defaults to `desc`, add `ascending=true` to sort asc

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListLatestTopicsResponse
            topic updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.topics.list_latest_topics(
                api_key="Api-Key",
                api_username="Api-Username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_latest_topics(
            api_key=api_key,
            api_username=api_username,
            order=order,
            ascending=ascending,
            request_options=request_options,
        )
        return _response.data

    async def update_topic(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        topic: typing.Optional[UpdateTopicRequestTopic] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateTopicResponse:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        topic : typing.Optional[UpdateTopicRequestTopic]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateTopicResponse
            topic updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.topics.update_topic(
                id="id",
                api_key="Api-Key",
                api_username="Api-Username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_topic(
            id, api_key=api_key, api_username=api_username, topic=topic, request_options=request_options
        )
        return _response.data

    async def get_topic_by_external_id(
        self, external_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        external_id : str

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
            await client.topics.get_topic_by_external_id(
                external_id="external_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_topic_by_external_id(external_id, request_options=request_options)
        return _response.data

    async def get_topic(
        self, id: str, *, api_key: str, api_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTopicResponse:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTopicResponse
            specific posts

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.topics.get_topic(
                id="id",
                api_key="Api-Key",
                api_username="Api-Username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_topic(
            id, api_key=api_key, api_username=api_username, request_options=request_options
        )
        return _response.data

    async def remove_topic(
        self, id: str, *, api_key: str, api_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

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
            await client.topics.remove_topic(
                id="id",
                api_key="Api-Key",
                api_username="Api-Username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_topic(
            id, api_key=api_key, api_username=api_username, request_options=request_options
        )
        return _response.data

    async def bookmark_topic(
        self, id: str, *, api_key: str, api_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

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
            await client.topics.bookmark_topic(
                id="id",
                api_key="Api-Key",
                api_username="Api-Username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bookmark_topic(
            id, api_key=api_key, api_username=api_username, request_options=request_options
        )
        return _response.data

    async def update_topic_timestamp(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        timestamp: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateTopicTimestampResponse:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        timestamp : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateTopicTimestampResponse
            topic updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.topics.update_topic_timestamp(
                id="id",
                api_key="Api-Key",
                api_username="Api-Username",
                timestamp="1594291380",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_topic_timestamp(
            id, api_key=api_key, api_username=api_username, timestamp=timestamp, request_options=request_options
        )
        return _response.data

    async def invite_to_topic(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        email: typing.Optional[str] = OMIT,
        user: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InviteToTopicResponse:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        email : typing.Optional[str]

        user : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InviteToTopicResponse
            topic updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.topics.invite_to_topic(
                id="id",
                api_key="Api-Key",
                api_username="Api-Username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.invite_to_topic(
            id, api_key=api_key, api_username=api_username, email=email, user=user, request_options=request_options
        )
        return _response.data

    async def set_notification_level(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        notification_level: SetNotificationLevelRequestNotificationLevel,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SetNotificationLevelResponse:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        notification_level : SetNotificationLevelRequestNotificationLevel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SetNotificationLevelResponse
            topic updated

        Examples
        --------
        import asyncio

        from fern.topics import SetNotificationLevelRequestNotificationLevel

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.topics.set_notification_level(
                id="id",
                api_key="Api-Key",
                api_username="Api-Username",
                notification_level=SetNotificationLevelRequestNotificationLevel.ZERO,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_notification_level(
            id,
            api_key=api_key,
            api_username=api_username,
            notification_level=notification_level,
            request_options=request_options,
        )
        return _response.data

    async def get_specific_posts_from_topic(
        self, id: str, *, api_key: str, api_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSpecificPostsFromTopicResponse:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSpecificPostsFromTopicResponse
            specific posts

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.topics.get_specific_posts_from_topic(
                id="id",
                api_key="Api-Key",
                api_username="Api-Username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_specific_posts_from_topic(
            id, api_key=api_key, api_username=api_username, request_options=request_options
        )
        return _response.data

    async def update_topic_status(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        enabled: UpdateTopicStatusRequestEnabled,
        status: UpdateTopicStatusRequestStatus,
        until: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateTopicStatusResponse:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        enabled : UpdateTopicStatusRequestEnabled

        status : UpdateTopicStatusRequestStatus

        until : typing.Optional[str]
            Only required for `pinned` and `pinned_globally`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateTopicStatusResponse
            topic updated

        Examples
        --------
        import asyncio

        from fern.topics import (
            UpdateTopicStatusRequestEnabled,
            UpdateTopicStatusRequestStatus,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.topics.update_topic_status(
                id="id",
                api_key="Api-Key",
                api_username="Api-Username",
                enabled=UpdateTopicStatusRequestEnabled.TRUE,
                status=UpdateTopicStatusRequestStatus.CLOSED,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_topic_status(
            id,
            api_key=api_key,
            api_username=api_username,
            enabled=enabled,
            status=status,
            until=until,
            request_options=request_options,
        )
        return _response.data

    async def create_topic_timer(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        based_on_last_post: typing.Optional[bool] = OMIT,
        category_id: typing.Optional[int] = OMIT,
        status_type: typing.Optional[str] = OMIT,
        time: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTopicTimerResponse:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        based_on_last_post : typing.Optional[bool]

        category_id : typing.Optional[int]

        status_type : typing.Optional[str]

        time : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTopicTimerResponse
            topic updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.topics.create_topic_timer(
                id="id",
                api_key="Api-Key",
                api_username="Api-Username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_topic_timer(
            id,
            api_key=api_key,
            api_username=api_username,
            based_on_last_post=based_on_last_post,
            category_id=category_id,
            status_type=status_type,
            time=time,
            request_options=request_options,
        )
        return _response.data

    async def list_top_topics(
        self,
        *,
        api_key: str,
        api_username: str,
        period: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListTopTopicsResponse:
        """
        Parameters
        ----------
        api_key : str

        api_username : str

        period : typing.Optional[str]
            Enum: `all`, `yearly`, `quarterly`, `monthly`, `weekly`, `daily`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListTopTopicsResponse
            response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.topics.list_top_topics(
                api_key="Api-Key",
                api_username="Api-Username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_top_topics(
            api_key=api_key, api_username=api_username, period=period, request_options=request_options
        )
        return _response.data
