

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPostsClient, RawPostsClient
from .types.create_topic_post_pm_response import CreateTopicPostPmResponse
from .types.get_post_response import GetPostResponse
from .types.list_posts_response import ListPostsResponse
from .types.lock_post_response import LockPostResponse
from .types.perform_post_action_response import PerformPostActionResponse
from .types.post_replies_response_item import PostRepliesResponseItem
from .types.update_post_request_post import UpdatePostRequestPost
from .types.update_post_response import UpdatePostResponse


OMIT = typing.cast(typing.Any, ...)


class PostsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPostsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPostsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPostsClient
        """
        return self._raw_client

    def perform_post_action(
        self,
        *,
        api_key: str,
        api_username: str,
        id: int,
        post_action_type_id: int,
        flag_topic: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PerformPostActionResponse:
        """
        Parameters
        ----------
        api_key : str

        api_username : str

        id : int

        post_action_type_id : int

        flag_topic : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PerformPostActionResponse
            post updated

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.posts.perform_post_action(
            api_key="Api-Key",
            api_username="Api-Username",
            id=1,
            post_action_type_id=1,
        )
        """
        _response = self._raw_client.perform_post_action(
            api_key=api_key,
            api_username=api_username,
            id=id,
            post_action_type_id=post_action_type_id,
            flag_topic=flag_topic,
            request_options=request_options,
        )
        return _response.data

    def list_posts(
        self,
        *,
        api_key: str,
        api_username: str,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListPostsResponse:
        """
        Parameters
        ----------
        api_key : str

        api_username : str

        before : typing.Optional[str]
            Load posts with an id lower than this value. Useful for pagination.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPostsResponse
            latest posts

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.posts.list_posts(
            api_key="Api-Key",
            api_username="Api-Username",
        )
        """
        _response = self._raw_client.list_posts(
            api_key=api_key, api_username=api_username, before=before, request_options=request_options
        )
        return _response.data

    def create_topic_post_pm(
        self,
        *,
        raw: str,
        archetype: typing.Optional[str] = OMIT,
        category: typing.Optional[int] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        embed_url: typing.Optional[str] = OMIT,
        external_id: typing.Optional[str] = OMIT,
        target_recipients: typing.Optional[str] = OMIT,
        target_usernames: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        topic_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTopicPostPmResponse:
        """
        Parameters
        ----------
        raw : str

        archetype : typing.Optional[str]
            Required for new private message.

        category : typing.Optional[int]
            Optional if creating a new topic, and ignored if creating
            a new post.

        created_at : typing.Optional[str]

        embed_url : typing.Optional[str]
            Provide a URL from a remote system to associate a forum
            topic with that URL, typically for using Discourse as a comments
            system for an external blog.

        external_id : typing.Optional[str]
            Provide an external_id from a remote system to associate
            a forum topic with that id.

        target_recipients : typing.Optional[str]
            Required for private message, comma separated.

        target_usernames : typing.Optional[str]
            Deprecated. Use target_recipients instead.

        title : typing.Optional[str]
            Required if creating a new topic or new private message.

        topic_id : typing.Optional[int]
            Required if creating a new post.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTopicPostPmResponse
            post created

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.posts.create_topic_post_pm(
            raw="raw",
        )
        """
        _response = self._raw_client.create_topic_post_pm(
            raw=raw,
            archetype=archetype,
            category=category,
            created_at=created_at,
            embed_url=embed_url,
            external_id=external_id,
            target_recipients=target_recipients,
            target_usernames=target_usernames,
            title=title,
            topic_id=topic_id,
            request_options=request_options,
        )
        return _response.data

    def get_post(
        self, id: str, *, api_key: str, api_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPostResponse:
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
        GetPostResponse
            latest posts

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.posts.get_post(
            id="id",
            api_key="Api-Key",
            api_username="Api-Username",
        )
        """
        _response = self._raw_client.get_post(
            id, api_key=api_key, api_username=api_username, request_options=request_options
        )
        return _response.data

    def update_post(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        post: typing.Optional[UpdatePostRequestPost] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdatePostResponse:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        post : typing.Optional[UpdatePostRequestPost]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdatePostResponse
            post updated

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.posts.update_post(
            id="id",
            api_key="Api-Key",
            api_username="Api-Username",
        )
        """
        _response = self._raw_client.update_post(
            id, api_key=api_key, api_username=api_username, post=post, request_options=request_options
        )
        return _response.data

    def delete_post(
        self,
        id: int,
        *,
        force_destroy: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        force_destroy : typing.Optional[bool]
            The `SiteSetting.can_permanently_delete` needs to be
            enabled first before this param can be used. Also this endpoint
            needs to be called first without `force_destroy` and then followed
            up with a second call 5 minutes later with `force_destroy` to
            permanently delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.posts.delete_post(
            id=1,
        )
        """
        _response = self._raw_client.delete_post(id, force_destroy=force_destroy, request_options=request_options)
        return _response.data

    def lock_post(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        locked: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LockPostResponse:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        locked : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LockPostResponse
            post updated

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.posts.lock_post(
            id="id",
            api_key="Api-Key",
            api_username="Api-Username",
            locked="locked",
        )
        """
        _response = self._raw_client.lock_post(
            id, api_key=api_key, api_username=api_username, locked=locked, request_options=request_options
        )
        return _response.data

    def post_replies(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PostRepliesResponseItem]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PostRepliesResponseItem]
            post replies

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.posts.post_replies(
            id="id",
        )
        """
        _response = self._raw_client.post_replies(id, request_options=request_options)
        return _response.data


class AsyncPostsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPostsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPostsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPostsClient
        """
        return self._raw_client

    async def perform_post_action(
        self,
        *,
        api_key: str,
        api_username: str,
        id: int,
        post_action_type_id: int,
        flag_topic: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PerformPostActionResponse:
        """
        Parameters
        ----------
        api_key : str

        api_username : str

        id : int

        post_action_type_id : int

        flag_topic : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PerformPostActionResponse
            post updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.posts.perform_post_action(
                api_key="Api-Key",
                api_username="Api-Username",
                id=1,
                post_action_type_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.perform_post_action(
            api_key=api_key,
            api_username=api_username,
            id=id,
            post_action_type_id=post_action_type_id,
            flag_topic=flag_topic,
            request_options=request_options,
        )
        return _response.data

    async def list_posts(
        self,
        *,
        api_key: str,
        api_username: str,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListPostsResponse:
        """
        Parameters
        ----------
        api_key : str

        api_username : str

        before : typing.Optional[str]
            Load posts with an id lower than this value. Useful for pagination.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPostsResponse
            latest posts

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.posts.list_posts(
                api_key="Api-Key",
                api_username="Api-Username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_posts(
            api_key=api_key, api_username=api_username, before=before, request_options=request_options
        )
        return _response.data

    async def create_topic_post_pm(
        self,
        *,
        raw: str,
        archetype: typing.Optional[str] = OMIT,
        category: typing.Optional[int] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        embed_url: typing.Optional[str] = OMIT,
        external_id: typing.Optional[str] = OMIT,
        target_recipients: typing.Optional[str] = OMIT,
        target_usernames: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        topic_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTopicPostPmResponse:
        """
        Parameters
        ----------
        raw : str

        archetype : typing.Optional[str]
            Required for new private message.

        category : typing.Optional[int]
            Optional if creating a new topic, and ignored if creating
            a new post.

        created_at : typing.Optional[str]

        embed_url : typing.Optional[str]
            Provide a URL from a remote system to associate a forum
            topic with that URL, typically for using Discourse as a comments
            system for an external blog.

        external_id : typing.Optional[str]
            Provide an external_id from a remote system to associate
            a forum topic with that id.

        target_recipients : typing.Optional[str]
            Required for private message, comma separated.

        target_usernames : typing.Optional[str]
            Deprecated. Use target_recipients instead.

        title : typing.Optional[str]
            Required if creating a new topic or new private message.

        topic_id : typing.Optional[int]
            Required if creating a new post.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTopicPostPmResponse
            post created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.posts.create_topic_post_pm(
                raw="raw",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_topic_post_pm(
            raw=raw,
            archetype=archetype,
            category=category,
            created_at=created_at,
            embed_url=embed_url,
            external_id=external_id,
            target_recipients=target_recipients,
            target_usernames=target_usernames,
            title=title,
            topic_id=topic_id,
            request_options=request_options,
        )
        return _response.data

    async def get_post(
        self, id: str, *, api_key: str, api_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPostResponse:
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
        GetPostResponse
            latest posts

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.posts.get_post(
                id="id",
                api_key="Api-Key",
                api_username="Api-Username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_post(
            id, api_key=api_key, api_username=api_username, request_options=request_options
        )
        return _response.data

    async def update_post(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        post: typing.Optional[UpdatePostRequestPost] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdatePostResponse:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        post : typing.Optional[UpdatePostRequestPost]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdatePostResponse
            post updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.posts.update_post(
                id="id",
                api_key="Api-Key",
                api_username="Api-Username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_post(
            id, api_key=api_key, api_username=api_username, post=post, request_options=request_options
        )
        return _response.data

    async def delete_post(
        self,
        id: int,
        *,
        force_destroy: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        force_destroy : typing.Optional[bool]
            The `SiteSetting.can_permanently_delete` needs to be
            enabled first before this param can be used. Also this endpoint
            needs to be called first without `force_destroy` and then followed
            up with a second call 5 minutes later with `force_destroy` to
            permanently delete.

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
            await client.posts.delete_post(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_post(id, force_destroy=force_destroy, request_options=request_options)
        return _response.data

    async def lock_post(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        locked: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LockPostResponse:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        locked : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LockPostResponse
            post updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.posts.lock_post(
                id="id",
                api_key="Api-Key",
                api_username="Api-Username",
                locked="locked",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.lock_post(
            id, api_key=api_key, api_username=api_username, locked=locked, request_options=request_options
        )
        return _response.data

    async def post_replies(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PostRepliesResponseItem]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PostRepliesResponseItem]
            post replies

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.posts.post_replies(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_replies(id, request_options=request_options)
        return _response.data
