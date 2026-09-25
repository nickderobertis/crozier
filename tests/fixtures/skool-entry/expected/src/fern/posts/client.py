

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.post import Post
from .raw_client import AsyncRawPostsClient, RawPostsClient


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

    def list_posts(
        self,
        group_slug: str,
        *,
        session_id: str,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        category: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Post]:
        """
        Retrieve posts from a Skool group community feed.

        Parameters
        ----------
        group_slug : str

        session_id : str

        page : typing.Optional[int]

        limit : typing.Optional[int]

        category : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Post]
            List of posts

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.posts.list_posts(
            group_slug="group_slug",
            session_id="session_id",
        )
        """
        _response = self._raw_client.list_posts(
            group_slug,
            session_id=session_id,
            page=page,
            limit=limit,
            category=category,
            request_options=request_options,
        )
        return _response.data

    def create_post(
        self,
        group_slug: str,
        *,
        session_id: str,
        title: str,
        content: str,
        category: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Post:
        """
        Create a new post in a Skool group community.

        Parameters
        ----------
        group_slug : str

        session_id : str

        title : str

        content : str

        category : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Post
            Post created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.posts.create_post(
            group_slug="group_slug",
            session_id="session_id",
            title="title",
            content="content",
        )
        """
        _response = self._raw_client.create_post(
            group_slug,
            session_id=session_id,
            title=title,
            content=content,
            category=category,
            request_options=request_options,
        )
        return _response.data

    def get_post(
        self, group_slug: str, post_id: str, *, session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Post:
        """
        Retrieve a specific post with its content and comments.

        Parameters
        ----------
        group_slug : str

        post_id : str

        session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Post
            Post details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.posts.get_post(
            group_slug="group_slug",
            post_id="post_id",
            session_id="session_id",
        )
        """
        _response = self._raw_client.get_post(
            group_slug, post_id, session_id=session_id, request_options=request_options
        )
        return _response.data

    def list_comments(
        self, group_slug: str, post_id: str, *, session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Retrieve comments on a specific post.

        Parameters
        ----------
        group_slug : str

        post_id : str

        session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            List of comments

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.posts.list_comments(
            group_slug="group_slug",
            post_id="post_id",
            session_id="session_id",
        )
        """
        _response = self._raw_client.list_comments(
            group_slug, post_id, session_id=session_id, request_options=request_options
        )
        return _response.data

    def create_comment(
        self,
        group_slug: str,
        post_id: str,
        *,
        session_id: str,
        content: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Add a comment to a post.

        Parameters
        ----------
        group_slug : str

        post_id : str

        session_id : str

        content : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.posts.create_comment(
            group_slug="group_slug",
            post_id="post_id",
            session_id="session_id",
            content="content",
        )
        """
        _response = self._raw_client.create_comment(
            group_slug, post_id, session_id=session_id, content=content, request_options=request_options
        )
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

    async def list_posts(
        self,
        group_slug: str,
        *,
        session_id: str,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        category: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Post]:
        """
        Retrieve posts from a Skool group community feed.

        Parameters
        ----------
        group_slug : str

        session_id : str

        page : typing.Optional[int]

        limit : typing.Optional[int]

        category : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Post]
            List of posts

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.posts.list_posts(
                group_slug="group_slug",
                session_id="session_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_posts(
            group_slug,
            session_id=session_id,
            page=page,
            limit=limit,
            category=category,
            request_options=request_options,
        )
        return _response.data

    async def create_post(
        self,
        group_slug: str,
        *,
        session_id: str,
        title: str,
        content: str,
        category: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Post:
        """
        Create a new post in a Skool group community.

        Parameters
        ----------
        group_slug : str

        session_id : str

        title : str

        content : str

        category : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Post
            Post created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.posts.create_post(
                group_slug="group_slug",
                session_id="session_id",
                title="title",
                content="content",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_post(
            group_slug,
            session_id=session_id,
            title=title,
            content=content,
            category=category,
            request_options=request_options,
        )
        return _response.data

    async def get_post(
        self, group_slug: str, post_id: str, *, session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Post:
        """
        Retrieve a specific post with its content and comments.

        Parameters
        ----------
        group_slug : str

        post_id : str

        session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Post
            Post details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.posts.get_post(
                group_slug="group_slug",
                post_id="post_id",
                session_id="session_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_post(
            group_slug, post_id, session_id=session_id, request_options=request_options
        )
        return _response.data

    async def list_comments(
        self, group_slug: str, post_id: str, *, session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Retrieve comments on a specific post.

        Parameters
        ----------
        group_slug : str

        post_id : str

        session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            List of comments

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.posts.list_comments(
                group_slug="group_slug",
                post_id="post_id",
                session_id="session_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_comments(
            group_slug, post_id, session_id=session_id, request_options=request_options
        )
        return _response.data

    async def create_comment(
        self,
        group_slug: str,
        post_id: str,
        *,
        session_id: str,
        content: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Add a comment to a post.

        Parameters
        ----------
        group_slug : str

        post_id : str

        session_id : str

        content : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.posts.create_comment(
                group_slug="group_slug",
                post_id="post_id",
                session_id="session_id",
                content="content",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_comment(
            group_slug, post_id, session_id=session_id, content=content, request_options=request_options
        )
        return _response.data
