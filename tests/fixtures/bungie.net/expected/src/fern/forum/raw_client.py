

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
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
from pydantic import ValidationError


class RawForumClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getcoretopicspaged(
        self,
        page: int,
        sort: int,
        quick_date: int,
        category_filter: int,
        *,
        locales: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ForumGetCoreTopicsPagedResponse]:
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
        HttpResponse[ForumGetCoreTopicsPagedResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Forum/GetCoreTopicsPaged/{encode_path_param(page)}/{encode_path_param(sort)}/{encode_path_param(quick_date)}/{encode_path_param(category_filter)}/",
            method="GET",
            params={
                "locales": locales,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ForumGetCoreTopicsPagedResponse,
                    parse_obj_as(
                        type_=ForumGetCoreTopicsPagedResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getforumtagsuggestions(
        self, *, partialtag: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ForumGetForumTagSuggestionsResponse]:
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
        HttpResponse[ForumGetForumTagSuggestionsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "Forum/GetForumTagSuggestions/",
            method="GET",
            params={
                "partialtag": partialtag,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ForumGetForumTagSuggestionsResponse,
                    parse_obj_as(
                        type_=ForumGetForumTagSuggestionsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getpostandparent(
        self,
        child_post_id: int,
        *,
        showbanned: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ForumGetPostAndParentResponse]:
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
        HttpResponse[ForumGetPostAndParentResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Forum/GetPostAndParent/{encode_path_param(child_post_id)}/",
            method="GET",
            params={
                "showbanned": showbanned,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ForumGetPostAndParentResponse,
                    parse_obj_as(
                        type_=ForumGetPostAndParentResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getpostandparentawaitingapproval(
        self,
        child_post_id: int,
        *,
        showbanned: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ForumGetPostAndParentAwaitingApprovalResponse]:
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
        HttpResponse[ForumGetPostAndParentAwaitingApprovalResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Forum/GetPostAndParentAwaitingApproval/{encode_path_param(child_post_id)}/",
            method="GET",
            params={
                "showbanned": showbanned,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ForumGetPostAndParentAwaitingApprovalResponse,
                    parse_obj_as(
                        type_=ForumGetPostAndParentAwaitingApprovalResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ForumGetPostsThreadedPagedResponse]:
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
        HttpResponse[ForumGetPostsThreadedPagedResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Forum/GetPostsThreadedPaged/{encode_path_param(parent_post_id)}/{encode_path_param(page)}/{encode_path_param(page_size)}/{encode_path_param(reply_size)}/{encode_path_param(get_parent_post)}/{encode_path_param(root_thread_mode)}/{encode_path_param(sort_mode)}/",
            method="GET",
            params={
                "showbanned": showbanned,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ForumGetPostsThreadedPagedResponse,
                    parse_obj_as(
                        type_=ForumGetPostsThreadedPagedResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ForumGetPostsThreadedPagedFromChildResponse]:
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
        HttpResponse[ForumGetPostsThreadedPagedFromChildResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Forum/GetPostsThreadedPagedFromChild/{encode_path_param(child_post_id)}/{encode_path_param(page)}/{encode_path_param(page_size)}/{encode_path_param(reply_size)}/{encode_path_param(root_thread_mode)}/{encode_path_param(sort_mode)}/",
            method="GET",
            params={
                "showbanned": showbanned,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ForumGetPostsThreadedPagedFromChildResponse,
                    parse_obj_as(
                        type_=ForumGetPostsThreadedPagedFromChildResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def gettopicforcontent(
        self, content_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ForumGetTopicForContentResponse]:
        """
        Gets the post Id for the given content item's comments, if it exists.

        Parameters
        ----------
        content_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ForumGetTopicForContentResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Forum/GetTopicForContent/{encode_path_param(content_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ForumGetTopicForContentResponse,
                    parse_obj_as(
                        type_=ForumGetTopicForContentResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ForumGetTopicsPagedResponse]:
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
        HttpResponse[ForumGetTopicsPagedResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Forum/GetTopicsPaged/{encode_path_param(page)}/{encode_path_param(page_size)}/{encode_path_param(group)}/{encode_path_param(sort)}/{encode_path_param(quick_date)}/{encode_path_param(category_filter)}/",
            method="GET",
            params={
                "locales": locales,
                "tagstring": tagstring,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ForumGetTopicsPagedResponse,
                    parse_obj_as(
                        type_=ForumGetTopicsPagedResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getpoll(
        self, topic_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ForumGetPollResponse]:
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
        HttpResponse[ForumGetPollResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Forum/Poll/{encode_path_param(topic_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ForumGetPollResponse,
                    parse_obj_as(
                        type_=ForumGetPollResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getrecruitmentthreadsummaries(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ForumGetRecruitmentThreadSummariesResponse]:
        """
        Allows the caller to get a list of to 25 recruitment thread summary information objects.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ForumGetRecruitmentThreadSummariesResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "Forum/Recruit/Summaries/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ForumGetRecruitmentThreadSummariesResponse,
                    parse_obj_as(
                        type_=ForumGetRecruitmentThreadSummariesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawForumClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getcoretopicspaged(
        self,
        page: int,
        sort: int,
        quick_date: int,
        category_filter: int,
        *,
        locales: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ForumGetCoreTopicsPagedResponse]:
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
        AsyncHttpResponse[ForumGetCoreTopicsPagedResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Forum/GetCoreTopicsPaged/{encode_path_param(page)}/{encode_path_param(sort)}/{encode_path_param(quick_date)}/{encode_path_param(category_filter)}/",
            method="GET",
            params={
                "locales": locales,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ForumGetCoreTopicsPagedResponse,
                    parse_obj_as(
                        type_=ForumGetCoreTopicsPagedResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getforumtagsuggestions(
        self, *, partialtag: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ForumGetForumTagSuggestionsResponse]:
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
        AsyncHttpResponse[ForumGetForumTagSuggestionsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Forum/GetForumTagSuggestions/",
            method="GET",
            params={
                "partialtag": partialtag,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ForumGetForumTagSuggestionsResponse,
                    parse_obj_as(
                        type_=ForumGetForumTagSuggestionsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getpostandparent(
        self,
        child_post_id: int,
        *,
        showbanned: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ForumGetPostAndParentResponse]:
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
        AsyncHttpResponse[ForumGetPostAndParentResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Forum/GetPostAndParent/{encode_path_param(child_post_id)}/",
            method="GET",
            params={
                "showbanned": showbanned,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ForumGetPostAndParentResponse,
                    parse_obj_as(
                        type_=ForumGetPostAndParentResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getpostandparentawaitingapproval(
        self,
        child_post_id: int,
        *,
        showbanned: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ForumGetPostAndParentAwaitingApprovalResponse]:
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
        AsyncHttpResponse[ForumGetPostAndParentAwaitingApprovalResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Forum/GetPostAndParentAwaitingApproval/{encode_path_param(child_post_id)}/",
            method="GET",
            params={
                "showbanned": showbanned,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ForumGetPostAndParentAwaitingApprovalResponse,
                    parse_obj_as(
                        type_=ForumGetPostAndParentAwaitingApprovalResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ForumGetPostsThreadedPagedResponse]:
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
        AsyncHttpResponse[ForumGetPostsThreadedPagedResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Forum/GetPostsThreadedPaged/{encode_path_param(parent_post_id)}/{encode_path_param(page)}/{encode_path_param(page_size)}/{encode_path_param(reply_size)}/{encode_path_param(get_parent_post)}/{encode_path_param(root_thread_mode)}/{encode_path_param(sort_mode)}/",
            method="GET",
            params={
                "showbanned": showbanned,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ForumGetPostsThreadedPagedResponse,
                    parse_obj_as(
                        type_=ForumGetPostsThreadedPagedResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ForumGetPostsThreadedPagedFromChildResponse]:
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
        AsyncHttpResponse[ForumGetPostsThreadedPagedFromChildResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Forum/GetPostsThreadedPagedFromChild/{encode_path_param(child_post_id)}/{encode_path_param(page)}/{encode_path_param(page_size)}/{encode_path_param(reply_size)}/{encode_path_param(root_thread_mode)}/{encode_path_param(sort_mode)}/",
            method="GET",
            params={
                "showbanned": showbanned,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ForumGetPostsThreadedPagedFromChildResponse,
                    parse_obj_as(
                        type_=ForumGetPostsThreadedPagedFromChildResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def gettopicforcontent(
        self, content_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ForumGetTopicForContentResponse]:
        """
        Gets the post Id for the given content item's comments, if it exists.

        Parameters
        ----------
        content_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ForumGetTopicForContentResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Forum/GetTopicForContent/{encode_path_param(content_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ForumGetTopicForContentResponse,
                    parse_obj_as(
                        type_=ForumGetTopicForContentResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ForumGetTopicsPagedResponse]:
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
        AsyncHttpResponse[ForumGetTopicsPagedResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Forum/GetTopicsPaged/{encode_path_param(page)}/{encode_path_param(page_size)}/{encode_path_param(group)}/{encode_path_param(sort)}/{encode_path_param(quick_date)}/{encode_path_param(category_filter)}/",
            method="GET",
            params={
                "locales": locales,
                "tagstring": tagstring,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ForumGetTopicsPagedResponse,
                    parse_obj_as(
                        type_=ForumGetTopicsPagedResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getpoll(
        self, topic_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ForumGetPollResponse]:
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
        AsyncHttpResponse[ForumGetPollResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Forum/Poll/{encode_path_param(topic_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ForumGetPollResponse,
                    parse_obj_as(
                        type_=ForumGetPollResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getrecruitmentthreadsummaries(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ForumGetRecruitmentThreadSummariesResponse]:
        """
        Allows the caller to get a list of to 25 recruitment thread summary information objects.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ForumGetRecruitmentThreadSummariesResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Forum/Recruit/Summaries/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ForumGetRecruitmentThreadSummariesResponse,
                    parse_obj_as(
                        type_=ForumGetRecruitmentThreadSummariesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
