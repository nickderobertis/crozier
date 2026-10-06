

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.deleted_post_response import DeletedPostResponse
from ..types.full_text_posts_search_posts_full_text_search_get_request_limit import (
    FullTextPostsSearchPostsFullTextSearchGetRequestLimit,
)
from ..types.full_text_posts_search_posts_full_text_search_get_request_offset import (
    FullTextPostsSearchPostsFullTextSearchGetRequestOffset,
)
from ..types.get_posts_order import GetPostsOrder
from ..types.get_user_posts_posts_user_posts_get_request_limit import GetUserPostsPostsUserPostsGetRequestLimit
from ..types.get_user_posts_posts_user_posts_get_request_offset import GetUserPostsPostsUserPostsGetRequestOffset
from ..types.post_response import PostResponse
from ..types.posts_response import PostsResponse
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

    def get_user_posts(
        self,
        *,
        creator_id: int,
        offset: typing.Optional[GetUserPostsPostsUserPostsGetRequestOffset] = None,
        limit: typing.Optional[GetUserPostsPostsUserPostsGetRequestLimit] = None,
        order: typing.Optional[GetPostsOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostsResponse:
        """
        Получение всех постов пользователя

        Parameters
        ----------
        creator_id : int

        offset : typing.Optional[GetUserPostsPostsUserPostsGetRequestOffset]

        limit : typing.Optional[GetUserPostsPostsUserPostsGetRequestLimit]

        order : typing.Optional[GetPostsOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostsResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.posts.get_user_posts(
            creator_id=1,
        )
        """
        _response = self._raw_client.get_user_posts(
            creator_id=creator_id, offset=offset, limit=limit, order=order, request_options=request_options
        )
        return _response.data

    def full_text_posts_search(
        self,
        *,
        query_string: str,
        offset: typing.Optional[FullTextPostsSearchPostsFullTextSearchGetRequestOffset] = None,
        limit: typing.Optional[FullTextPostsSearchPostsFullTextSearchGetRequestLimit] = None,
        order: typing.Optional[GetPostsOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostsResponse:
        """
        Получение всех постов пользователя

        Parameters
        ----------
        query_string : str

        offset : typing.Optional[FullTextPostsSearchPostsFullTextSearchGetRequestOffset]

        limit : typing.Optional[FullTextPostsSearchPostsFullTextSearchGetRequestLimit]

        order : typing.Optional[GetPostsOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostsResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.posts.full_text_posts_search(
            query_string="query_string",
        )
        """
        _response = self._raw_client.full_text_posts_search(
            query_string=query_string, offset=offset, limit=limit, order=order, request_options=request_options
        )
        return _response.data

    def create_post(
        self, *, authorization: str, text_content: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostResponse:
        """
        Создание поста

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        text_content : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.posts.create_post(
            authorization="Authorization",
            text_content="text_content",
        )
        """
        _response = self._raw_client.create_post(
            authorization=authorization, text_content=text_content, request_options=request_options
        )
        return _response.data

    def delete_post(
        self, *, authorization: str, post_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DeletedPostResponse:
        """
        Удание поста пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        post_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletedPostResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.posts.delete_post(
            authorization="Authorization",
            post_id="post_id",
        )
        """
        _response = self._raw_client.delete_post(
            authorization=authorization, post_id=post_id, request_options=request_options
        )
        return _response.data

    def update_post(
        self,
        *,
        authorization: str,
        post_id: str,
        text_content: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostResponse:
        """
        Обнволение поста пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        post_id : str

        text_content : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.posts.update_post(
            authorization="Authorization",
            post_id="post_id",
            text_content="text_content",
        )
        """
        _response = self._raw_client.update_post(
            authorization=authorization, post_id=post_id, text_content=text_content, request_options=request_options
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

    async def get_user_posts(
        self,
        *,
        creator_id: int,
        offset: typing.Optional[GetUserPostsPostsUserPostsGetRequestOffset] = None,
        limit: typing.Optional[GetUserPostsPostsUserPostsGetRequestLimit] = None,
        order: typing.Optional[GetPostsOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostsResponse:
        """
        Получение всех постов пользователя

        Parameters
        ----------
        creator_id : int

        offset : typing.Optional[GetUserPostsPostsUserPostsGetRequestOffset]

        limit : typing.Optional[GetUserPostsPostsUserPostsGetRequestLimit]

        order : typing.Optional[GetPostsOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.posts.get_user_posts(
                creator_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_posts(
            creator_id=creator_id, offset=offset, limit=limit, order=order, request_options=request_options
        )
        return _response.data

    async def full_text_posts_search(
        self,
        *,
        query_string: str,
        offset: typing.Optional[FullTextPostsSearchPostsFullTextSearchGetRequestOffset] = None,
        limit: typing.Optional[FullTextPostsSearchPostsFullTextSearchGetRequestLimit] = None,
        order: typing.Optional[GetPostsOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostsResponse:
        """
        Получение всех постов пользователя

        Parameters
        ----------
        query_string : str

        offset : typing.Optional[FullTextPostsSearchPostsFullTextSearchGetRequestOffset]

        limit : typing.Optional[FullTextPostsSearchPostsFullTextSearchGetRequestLimit]

        order : typing.Optional[GetPostsOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.posts.full_text_posts_search(
                query_string="query_string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.full_text_posts_search(
            query_string=query_string, offset=offset, limit=limit, order=order, request_options=request_options
        )
        return _response.data

    async def create_post(
        self, *, authorization: str, text_content: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostResponse:
        """
        Создание поста

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        text_content : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.posts.create_post(
                authorization="Authorization",
                text_content="text_content",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_post(
            authorization=authorization, text_content=text_content, request_options=request_options
        )
        return _response.data

    async def delete_post(
        self, *, authorization: str, post_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DeletedPostResponse:
        """
        Удание поста пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        post_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletedPostResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.posts.delete_post(
                authorization="Authorization",
                post_id="post_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_post(
            authorization=authorization, post_id=post_id, request_options=request_options
        )
        return _response.data

    async def update_post(
        self,
        *,
        authorization: str,
        post_id: str,
        text_content: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostResponse:
        """
        Обнволение поста пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        post_id : str

        text_content : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.posts.update_post(
                authorization="Authorization",
                post_id="post_id",
                text_content="text_content",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_post(
            authorization=authorization, post_id=post_id, text_content=text_content, request_options=request_options
        )
        return _response.data
