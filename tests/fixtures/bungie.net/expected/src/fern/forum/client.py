

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawForumClient, RawForumClient
from .types.forum_get_core_topics_paged_response import ForumGetCoreTopicsPagedResponse
from .types.forum_get_forum_tag_suggestions_response import ForumGetForumTagSuggestionsResponse
from .types.forum_get_poll_response import ForumGetPollResponse
from .types.forum_get_post_and_parent_awaiting_approval_response import ForumGetPostAndParentAwaitingApprovalResponse
from .types.forum_get_post_and_parent_response import ForumGetPostAndParentResponse
from .types.forum_get_posts_threaded_paged_from_child_response import ForumGetPostsThreadedPagedFromChildResponse
from .types.forum_get_posts_threaded_paged_response import ForumGetPostsThreadedPagedResponse
from .types.forum_get_recruitment_thread_summaries_response import ForumGetRecruitmentThreadSummariesResponse
from .types.forum_get_topic_for_content_response import ForumGetTopicForContentResponse
from .types.forum_get_topics_paged_response import ForumGetTopicsPagedResponse


class ForumClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawForumClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawForumClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawForumClient
        """
        return self._raw_client

    def getcoretopicspaged(
        self,
        page: int,
        sort: int,
        quick_date: int,
        category_filter: int,
        *,
        locales: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ForumGetCoreTopicsPagedResponse:
        """
        Gets a listing of all topics marked as part of the core group.

        Parameters
        ----------
        page : int
            Zero base page

        sort : int
            The sort mode.

        quick_date : int
            The date filter.

        category_filter : int
            The category filter.

        locales : typing.Optional[str]
            Comma seperated list of locales posts must match to return in the result list. Default 'en'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ForumGetCoreTopicsPagedResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.forum.getcoretopicspaged(
            page=1,
            sort=1,
            quick_date=1,
            category_filter=1,
        )
        """
        _response = self._raw_client.getcoretopicspaged(
            page, sort, quick_date, category_filter, locales=locales, request_options=request_options
        )
        return _response.data

    def getforumtagsuggestions(
        self, *, partialtag: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ForumGetForumTagSuggestionsResponse:
        """
        Gets tag suggestions based on partial text entry, matching them with other tags previously used in the forums.

        Parameters
        ----------
        partialtag : typing.Optional[str]
            The partial tag input to generate suggestions from.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ForumGetForumTagSuggestionsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.forum.getforumtagsuggestions()
        """
        _response = self._raw_client.getforumtagsuggestions(partialtag=partialtag, request_options=request_options)
        return _response.data

    def getpostandparent(
        self,
        child_post_id: int,
        *,
        showbanned: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ForumGetPostAndParentResponse:
        """
        Returns the post specified and its immediate parent.

        Parameters
        ----------
        child_post_id : int


        showbanned : typing.Optional[str]
            If this value is not null or empty, banned posts are requested to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ForumGetPostAndParentResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.forum.getpostandparent(
            child_post_id=1000000,
        )
        """
        _response = self._raw_client.getpostandparent(
            child_post_id, showbanned=showbanned, request_options=request_options
        )
        return _response.data

    def getpostandparentawaitingapproval(
        self,
        child_post_id: int,
        *,
        showbanned: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ForumGetPostAndParentAwaitingApprovalResponse:
        """
        Returns the post specified and its immediate parent of posts that are awaiting approval.

        Parameters
        ----------
        child_post_id : int


        showbanned : typing.Optional[str]
            If this value is not null or empty, banned posts are requested to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ForumGetPostAndParentAwaitingApprovalResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.forum.getpostandparentawaitingapproval(
            child_post_id=1000000,
        )
        """
        _response = self._raw_client.getpostandparentawaitingapproval(
            child_post_id, showbanned=showbanned, request_options=request_options
        )
        return _response.data

    def getpoststhreadedpaged(
        self,
        parent_post_id: int,
        page: int,
        page_size: int,
        reply_size: int,
        get_parent_post: bool,
        root_thread_mode: bool,
        sort_mode: int,
        *,
        showbanned: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ForumGetPostsThreadedPagedResponse:
        """
        Returns a thread of posts at the given parent, optionally returning replies to those posts as well as the original parent.

        Parameters
        ----------
        parent_post_id : int


        page : int


        page_size : int


        reply_size : int


        get_parent_post : bool


        root_thread_mode : bool


        sort_mode : int


        showbanned : typing.Optional[str]
            If this value is not null or empty, banned posts are requested to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ForumGetPostsThreadedPagedResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.forum.getpoststhreadedpaged(
            parent_post_id=1000000,
            page=1,
            page_size=1,
            reply_size=1,
            get_parent_post=True,
            root_thread_mode=True,
            sort_mode=1,
        )
        """
        _response = self._raw_client.getpoststhreadedpaged(
            parent_post_id,
            page,
            page_size,
            reply_size,
            get_parent_post,
            root_thread_mode,
            sort_mode,
            showbanned=showbanned,
            request_options=request_options,
        )
        return _response.data

    def getpoststhreadedpagedfromchild(
        self,
        child_post_id: int,
        page: int,
        page_size: int,
        reply_size: int,
        root_thread_mode: bool,
        sort_mode: int,
        *,
        showbanned: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ForumGetPostsThreadedPagedFromChildResponse:
        """
        Returns a thread of posts starting at the topicId of the input childPostId, optionally returning replies to those posts as well as the original parent.

        Parameters
        ----------
        child_post_id : int


        page : int


        page_size : int


        reply_size : int


        root_thread_mode : bool


        sort_mode : int


        showbanned : typing.Optional[str]
            If this value is not null or empty, banned posts are requested to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ForumGetPostsThreadedPagedFromChildResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.forum.getpoststhreadedpagedfromchild(
            child_post_id=1000000,
            page=1,
            page_size=1,
            reply_size=1,
            root_thread_mode=True,
            sort_mode=1,
        )
        """
        _response = self._raw_client.getpoststhreadedpagedfromchild(
            child_post_id,
            page,
            page_size,
            reply_size,
            root_thread_mode,
            sort_mode,
            showbanned=showbanned,
            request_options=request_options,
        )
        return _response.data

    def gettopicforcontent(
        self, content_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ForumGetTopicForContentResponse:
        """
        Gets the post Id for the given content item's comments, if it exists.

        Parameters
        ----------
        content_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ForumGetTopicForContentResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.forum.gettopicforcontent(
            content_id=1000000,
        )
        """
        _response = self._raw_client.gettopicforcontent(content_id, request_options=request_options)
        return _response.data

    def gettopicspaged(
        self,
        page: int,
        page_size: int,
        group: int,
        sort: int,
        quick_date: int,
        category_filter: int,
        *,
        locales: typing.Optional[str] = None,
        tagstring: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ForumGetTopicsPagedResponse:
        """
        Get topics from any forum.

        Parameters
        ----------
        page : int
            Zero paged page number

        page_size : int
            Unused

        group : int
            The group, if any.

        sort : int
            The sort mode.

        quick_date : int
            A date filter.

        category_filter : int
            A category filter

        locales : typing.Optional[str]
            Comma seperated list of locales posts must match to return in the result list. Default 'en'

        tagstring : typing.Optional[str]
            The tags to search, if any.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ForumGetTopicsPagedResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.forum.gettopicspaged(
            page=1,
            page_size=1,
            group=1000000,
            sort=1,
            quick_date=1,
            category_filter=1,
        )
        """
        _response = self._raw_client.gettopicspaged(
            page,
            page_size,
            group,
            sort,
            quick_date,
            category_filter,
            locales=locales,
            tagstring=tagstring,
            request_options=request_options,
        )
        return _response.data

    def getpoll(
        self, topic_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ForumGetPollResponse:
        """
        Gets the specified forum poll.

        Parameters
        ----------
        topic_id : int
            The post id of the topic that has the poll.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ForumGetPollResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.forum.getpoll(
            topic_id=1000000,
        )
        """
        _response = self._raw_client.getpoll(topic_id, request_options=request_options)
        return _response.data

    def getrecruitmentthreadsummaries(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ForumGetRecruitmentThreadSummariesResponse:
        """
        Allows the caller to get a list of to 25 recruitment thread summary information objects.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ForumGetRecruitmentThreadSummariesResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.forum.getrecruitmentthreadsummaries()
        """
        _response = self._raw_client.getrecruitmentthreadsummaries(request_options=request_options)
        return _response.data


class AsyncForumClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawForumClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawForumClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawForumClient
        """
        return self._raw_client

    async def getcoretopicspaged(
        self,
        page: int,
        sort: int,
        quick_date: int,
        category_filter: int,
        *,
        locales: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ForumGetCoreTopicsPagedResponse:
        """
        Gets a listing of all topics marked as part of the core group.

        Parameters
        ----------
        page : int
            Zero base page

        sort : int
            The sort mode.

        quick_date : int
            The date filter.

        category_filter : int
            The category filter.

        locales : typing.Optional[str]
            Comma seperated list of locales posts must match to return in the result list. Default 'en'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ForumGetCoreTopicsPagedResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.forum.getcoretopicspaged(
                page=1,
                sort=1,
                quick_date=1,
                category_filter=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getcoretopicspaged(
            page, sort, quick_date, category_filter, locales=locales, request_options=request_options
        )
        return _response.data

    async def getforumtagsuggestions(
        self, *, partialtag: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ForumGetForumTagSuggestionsResponse:
        """
        Gets tag suggestions based on partial text entry, matching them with other tags previously used in the forums.

        Parameters
        ----------
        partialtag : typing.Optional[str]
            The partial tag input to generate suggestions from.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ForumGetForumTagSuggestionsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.forum.getforumtagsuggestions()


        asyncio.run(main())
        """
        _response = await self._raw_client.getforumtagsuggestions(
            partialtag=partialtag, request_options=request_options
        )
        return _response.data

    async def getpostandparent(
        self,
        child_post_id: int,
        *,
        showbanned: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ForumGetPostAndParentResponse:
        """
        Returns the post specified and its immediate parent.

        Parameters
        ----------
        child_post_id : int


        showbanned : typing.Optional[str]
            If this value is not null or empty, banned posts are requested to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ForumGetPostAndParentResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.forum.getpostandparent(
                child_post_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getpostandparent(
            child_post_id, showbanned=showbanned, request_options=request_options
        )
        return _response.data

    async def getpostandparentawaitingapproval(
        self,
        child_post_id: int,
        *,
        showbanned: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ForumGetPostAndParentAwaitingApprovalResponse:
        """
        Returns the post specified and its immediate parent of posts that are awaiting approval.

        Parameters
        ----------
        child_post_id : int


        showbanned : typing.Optional[str]
            If this value is not null or empty, banned posts are requested to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ForumGetPostAndParentAwaitingApprovalResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.forum.getpostandparentawaitingapproval(
                child_post_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getpostandparentawaitingapproval(
            child_post_id, showbanned=showbanned, request_options=request_options
        )
        return _response.data

    async def getpoststhreadedpaged(
        self,
        parent_post_id: int,
        page: int,
        page_size: int,
        reply_size: int,
        get_parent_post: bool,
        root_thread_mode: bool,
        sort_mode: int,
        *,
        showbanned: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ForumGetPostsThreadedPagedResponse:
        """
        Returns a thread of posts at the given parent, optionally returning replies to those posts as well as the original parent.

        Parameters
        ----------
        parent_post_id : int


        page : int


        page_size : int


        reply_size : int


        get_parent_post : bool


        root_thread_mode : bool


        sort_mode : int


        showbanned : typing.Optional[str]
            If this value is not null or empty, banned posts are requested to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ForumGetPostsThreadedPagedResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.forum.getpoststhreadedpaged(
                parent_post_id=1000000,
                page=1,
                page_size=1,
                reply_size=1,
                get_parent_post=True,
                root_thread_mode=True,
                sort_mode=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getpoststhreadedpaged(
            parent_post_id,
            page,
            page_size,
            reply_size,
            get_parent_post,
            root_thread_mode,
            sort_mode,
            showbanned=showbanned,
            request_options=request_options,
        )
        return _response.data

    async def getpoststhreadedpagedfromchild(
        self,
        child_post_id: int,
        page: int,
        page_size: int,
        reply_size: int,
        root_thread_mode: bool,
        sort_mode: int,
        *,
        showbanned: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ForumGetPostsThreadedPagedFromChildResponse:
        """
        Returns a thread of posts starting at the topicId of the input childPostId, optionally returning replies to those posts as well as the original parent.

        Parameters
        ----------
        child_post_id : int


        page : int


        page_size : int


        reply_size : int


        root_thread_mode : bool


        sort_mode : int


        showbanned : typing.Optional[str]
            If this value is not null or empty, banned posts are requested to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ForumGetPostsThreadedPagedFromChildResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.forum.getpoststhreadedpagedfromchild(
                child_post_id=1000000,
                page=1,
                page_size=1,
                reply_size=1,
                root_thread_mode=True,
                sort_mode=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getpoststhreadedpagedfromchild(
            child_post_id,
            page,
            page_size,
            reply_size,
            root_thread_mode,
            sort_mode,
            showbanned=showbanned,
            request_options=request_options,
        )
        return _response.data

    async def gettopicforcontent(
        self, content_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ForumGetTopicForContentResponse:
        """
        Gets the post Id for the given content item's comments, if it exists.

        Parameters
        ----------
        content_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ForumGetTopicForContentResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.forum.gettopicforcontent(
                content_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.gettopicforcontent(content_id, request_options=request_options)
        return _response.data

    async def gettopicspaged(
        self,
        page: int,
        page_size: int,
        group: int,
        sort: int,
        quick_date: int,
        category_filter: int,
        *,
        locales: typing.Optional[str] = None,
        tagstring: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ForumGetTopicsPagedResponse:
        """
        Get topics from any forum.

        Parameters
        ----------
        page : int
            Zero paged page number

        page_size : int
            Unused

        group : int
            The group, if any.

        sort : int
            The sort mode.

        quick_date : int
            A date filter.

        category_filter : int
            A category filter

        locales : typing.Optional[str]
            Comma seperated list of locales posts must match to return in the result list. Default 'en'

        tagstring : typing.Optional[str]
            The tags to search, if any.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ForumGetTopicsPagedResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.forum.gettopicspaged(
                page=1,
                page_size=1,
                group=1000000,
                sort=1,
                quick_date=1,
                category_filter=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.gettopicspaged(
            page,
            page_size,
            group,
            sort,
            quick_date,
            category_filter,
            locales=locales,
            tagstring=tagstring,
            request_options=request_options,
        )
        return _response.data

    async def getpoll(
        self, topic_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ForumGetPollResponse:
        """
        Gets the specified forum poll.

        Parameters
        ----------
        topic_id : int
            The post id of the topic that has the poll.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ForumGetPollResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.forum.getpoll(
                topic_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getpoll(topic_id, request_options=request_options)
        return _response.data

    async def getrecruitmentthreadsummaries(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ForumGetRecruitmentThreadSummariesResponse:
        """
        Allows the caller to get a list of to 25 recruitment thread summary information objects.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ForumGetRecruitmentThreadSummariesResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.forum.getrecruitmentthreadsummaries()


        asyncio.run(main())
        """
        _response = await self._raw_client.getrecruitmentthreadsummaries(request_options=request_options)
        return _response.data
