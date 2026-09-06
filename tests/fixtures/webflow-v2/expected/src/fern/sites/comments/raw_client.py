

import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.http_response import AsyncHttpResponse, HttpResponse
from ...core.jsonable_encoder import encode_path_param
from ...core.parse_error import ParsingError
from ...core.pydantic_utilities import parse_obj_as
from ...core.request_options import RequestOptions
from ...errors.bad_request_error import BadRequestError
from ...errors.internal_server_error import InternalServerError
from ...errors.not_found_error import NotFoundError
from ...errors.too_many_requests_error import TooManyRequestsError
from ...errors.unauthorized_error import UnauthorizedError
from .types.create_comment_reply_comments_response import CreateCommentReplyCommentsResponse
from .types.get_comment_thread_comments_request_sort_by import GetCommentThreadCommentsRequestSortBy
from .types.get_comment_thread_comments_request_sort_order import GetCommentThreadCommentsRequestSortOrder
from .types.get_comment_thread_comments_response import GetCommentThreadCommentsResponse
from .types.list_comment_replies_comments_request_sort_by import ListCommentRepliesCommentsRequestSortBy
from .types.list_comment_replies_comments_request_sort_order import ListCommentRepliesCommentsRequestSortOrder
from .types.list_comment_replies_comments_response import ListCommentRepliesCommentsResponse
from .types.list_comment_threads_comments_request_sort_by import ListCommentThreadsCommentsRequestSortBy
from .types.list_comment_threads_comments_request_sort_order import ListCommentThreadsCommentsRequestSortOrder
from .types.list_comment_threads_comments_response import ListCommentThreadsCommentsResponse
from .types.resolve_comment_thread_comments_response import ResolveCommentThreadCommentsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCommentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_comment_threads(
        self,
        site_id: str,
        *,
        locale_id: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        sort_by: typing.Optional[ListCommentThreadsCommentsRequestSortBy] = None,
        sort_order: typing.Optional[ListCommentThreadsCommentsRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListCommentThreadsCommentsResponse]:
        """
        List all comment threads for a site.

        <Note title="Timing of comment threads">
          There may be a delay of up to 5 minutes before new comments appear in the system.
        </Note>

        Required scope | `comments:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        locale_id : typing.Optional[str]
            Unique identifier for a specific Locale.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        sort_by : typing.Optional[ListCommentThreadsCommentsRequestSortBy]
            Sort results by the provided value. Only allowed when sortOrder is provided.

        sort_order : typing.Optional[ListCommentThreadsCommentsRequestSortOrder]
            Sorts the results by asc or desc

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListCommentThreadsCommentsResponse]
            Request was successful
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/comments",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "localeId": locale_id,
                "offset": offset,
                "limit": limit,
                "sortBy": sort_by,
                "sortOrder": sort_order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListCommentThreadsCommentsResponse,
                    parse_obj_as(
                        type_=ListCommentThreadsCommentsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_comment_thread(
        self,
        site_id: str,
        comment_thread_id: str,
        *,
        locale_id: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        sort_by: typing.Optional[GetCommentThreadCommentsRequestSortBy] = None,
        sort_order: typing.Optional[GetCommentThreadCommentsRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetCommentThreadCommentsResponse]:
        """
        Get details of a specific comment thread.

          <Note title="Timing of comment threads">
            There may be a delay of up to 5 minutes before new comments appear in the system.
          </Note>

        Required scope | `comments:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        comment_thread_id : str
            Unique identifier for a Comment Thread

        locale_id : typing.Optional[str]
            Unique identifier for a specific Locale.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        sort_by : typing.Optional[GetCommentThreadCommentsRequestSortBy]
            Sort results by the provided value. Only allowed when sortOrder is provided.

        sort_order : typing.Optional[GetCommentThreadCommentsRequestSortOrder]
            Sorts the results by asc or desc

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetCommentThreadCommentsResponse]
            Request was successful
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/comments/{encode_path_param(comment_thread_id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "localeId": locale_id,
                "offset": offset,
                "limit": limit,
                "sortBy": sort_by,
                "sortOrder": sort_order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCommentThreadCommentsResponse,
                    parse_obj_as(
                        type_=GetCommentThreadCommentsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def resolve_comment_thread(
        self,
        site_id: str,
        comment_thread_id: str,
        *,
        resolved: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResolveCommentThreadCommentsResponse]:
        """
        Resolve or unresolve a comment thread.

        <Note>
          This endpoint is rate limited to 60 requests per minute per site.
        </Note>

        Required scope | `comments:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        comment_thread_id : str
            Unique identifier for a Comment Thread

        resolved : bool
            Set to `true` to resolve the thread, or `false` to unresolve it

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResolveCommentThreadCommentsResponse]
            Request was successful
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/comments/{encode_path_param(comment_thread_id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="PATCH",
            json={
                "resolved": resolved,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResolveCommentThreadCommentsResponse,
                    parse_obj_as(
                        type_=ResolveCommentThreadCommentsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_comment_replies(
        self,
        site_id: str,
        comment_thread_id: str,
        *,
        locale_id: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        sort_by: typing.Optional[ListCommentRepliesCommentsRequestSortBy] = None,
        sort_order: typing.Optional[ListCommentRepliesCommentsRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListCommentRepliesCommentsResponse]:
        """
        List all replies to a specific comment thread.

        <Note title="Timing of comment threads">
          There may be a delay of up to 5 minutes before new comments appear in the system.
        </Note>

        Required scope | `comments:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        comment_thread_id : str
            Unique identifier for a Comment Thread

        locale_id : typing.Optional[str]
            Unique identifier for a specific Locale.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        sort_by : typing.Optional[ListCommentRepliesCommentsRequestSortBy]
            Sort results by the provided value. Only allowed when sortOrder is provided.

        sort_order : typing.Optional[ListCommentRepliesCommentsRequestSortOrder]
            Sorts the results by asc or desc

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListCommentRepliesCommentsResponse]
            Request was successful
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/comments/{encode_path_param(comment_thread_id)}/replies",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "localeId": locale_id,
                "offset": offset,
                "limit": limit,
                "sortBy": sort_by,
                "sortOrder": sort_order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListCommentRepliesCommentsResponse,
                    parse_obj_as(
                        type_=ListCommentRepliesCommentsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_comment_reply(
        self,
        site_id: str,
        comment_thread_id: str,
        *,
        content: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateCommentReplyCommentsResponse]:
        """
        Create a reply to an existing comment thread.

        The reply author is always the user who authorized the OAuth token.
        To @mention a user in the reply, include their user ID in double square brackets in the `content` field, as in `[[userId]]`.

        <Note>
          The `comment_created` webhook fires automatically when a reply is created.
        </Note>

        Required scope | `comments:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        comment_thread_id : str
            Unique identifier for a Comment Thread

        content : str
            The text content of the reply. To @mention a user, include their user ID in double square brackets, as in `[[userId]]`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateCommentReplyCommentsResponse]
            Reply created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/comments/{encode_path_param(comment_thread_id)}/replies",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "content": content,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateCommentReplyCommentsResponse,
                    parse_obj_as(
                        type_=CreateCommentReplyCommentsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawCommentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_comment_threads(
        self,
        site_id: str,
        *,
        locale_id: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        sort_by: typing.Optional[ListCommentThreadsCommentsRequestSortBy] = None,
        sort_order: typing.Optional[ListCommentThreadsCommentsRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListCommentThreadsCommentsResponse]:
        """
        List all comment threads for a site.

        <Note title="Timing of comment threads">
          There may be a delay of up to 5 minutes before new comments appear in the system.
        </Note>

        Required scope | `comments:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        locale_id : typing.Optional[str]
            Unique identifier for a specific Locale.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        sort_by : typing.Optional[ListCommentThreadsCommentsRequestSortBy]
            Sort results by the provided value. Only allowed when sortOrder is provided.

        sort_order : typing.Optional[ListCommentThreadsCommentsRequestSortOrder]
            Sorts the results by asc or desc

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListCommentThreadsCommentsResponse]
            Request was successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/comments",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "localeId": locale_id,
                "offset": offset,
                "limit": limit,
                "sortBy": sort_by,
                "sortOrder": sort_order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListCommentThreadsCommentsResponse,
                    parse_obj_as(
                        type_=ListCommentThreadsCommentsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_comment_thread(
        self,
        site_id: str,
        comment_thread_id: str,
        *,
        locale_id: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        sort_by: typing.Optional[GetCommentThreadCommentsRequestSortBy] = None,
        sort_order: typing.Optional[GetCommentThreadCommentsRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetCommentThreadCommentsResponse]:
        """
        Get details of a specific comment thread.

          <Note title="Timing of comment threads">
            There may be a delay of up to 5 minutes before new comments appear in the system.
          </Note>

        Required scope | `comments:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        comment_thread_id : str
            Unique identifier for a Comment Thread

        locale_id : typing.Optional[str]
            Unique identifier for a specific Locale.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        sort_by : typing.Optional[GetCommentThreadCommentsRequestSortBy]
            Sort results by the provided value. Only allowed when sortOrder is provided.

        sort_order : typing.Optional[GetCommentThreadCommentsRequestSortOrder]
            Sorts the results by asc or desc

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetCommentThreadCommentsResponse]
            Request was successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/comments/{encode_path_param(comment_thread_id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "localeId": locale_id,
                "offset": offset,
                "limit": limit,
                "sortBy": sort_by,
                "sortOrder": sort_order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCommentThreadCommentsResponse,
                    parse_obj_as(
                        type_=GetCommentThreadCommentsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def resolve_comment_thread(
        self,
        site_id: str,
        comment_thread_id: str,
        *,
        resolved: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResolveCommentThreadCommentsResponse]:
        """
        Resolve or unresolve a comment thread.

        <Note>
          This endpoint is rate limited to 60 requests per minute per site.
        </Note>

        Required scope | `comments:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        comment_thread_id : str
            Unique identifier for a Comment Thread

        resolved : bool
            Set to `true` to resolve the thread, or `false` to unresolve it

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResolveCommentThreadCommentsResponse]
            Request was successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/comments/{encode_path_param(comment_thread_id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="PATCH",
            json={
                "resolved": resolved,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResolveCommentThreadCommentsResponse,
                    parse_obj_as(
                        type_=ResolveCommentThreadCommentsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_comment_replies(
        self,
        site_id: str,
        comment_thread_id: str,
        *,
        locale_id: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        sort_by: typing.Optional[ListCommentRepliesCommentsRequestSortBy] = None,
        sort_order: typing.Optional[ListCommentRepliesCommentsRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListCommentRepliesCommentsResponse]:
        """
        List all replies to a specific comment thread.

        <Note title="Timing of comment threads">
          There may be a delay of up to 5 minutes before new comments appear in the system.
        </Note>

        Required scope | `comments:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        comment_thread_id : str
            Unique identifier for a Comment Thread

        locale_id : typing.Optional[str]
            Unique identifier for a specific Locale.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        sort_by : typing.Optional[ListCommentRepliesCommentsRequestSortBy]
            Sort results by the provided value. Only allowed when sortOrder is provided.

        sort_order : typing.Optional[ListCommentRepliesCommentsRequestSortOrder]
            Sorts the results by asc or desc

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListCommentRepliesCommentsResponse]
            Request was successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/comments/{encode_path_param(comment_thread_id)}/replies",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "localeId": locale_id,
                "offset": offset,
                "limit": limit,
                "sortBy": sort_by,
                "sortOrder": sort_order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListCommentRepliesCommentsResponse,
                    parse_obj_as(
                        type_=ListCommentRepliesCommentsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_comment_reply(
        self,
        site_id: str,
        comment_thread_id: str,
        *,
        content: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateCommentReplyCommentsResponse]:
        """
        Create a reply to an existing comment thread.

        The reply author is always the user who authorized the OAuth token.
        To @mention a user in the reply, include their user ID in double square brackets in the `content` field, as in `[[userId]]`.

        <Note>
          The `comment_created` webhook fires automatically when a reply is created.
        </Note>

        Required scope | `comments:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        comment_thread_id : str
            Unique identifier for a Comment Thread

        content : str
            The text content of the reply. To @mention a user, include their user ID in double square brackets, as in `[[userId]]`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateCommentReplyCommentsResponse]
            Reply created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/comments/{encode_path_param(comment_thread_id)}/replies",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "content": content,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateCommentReplyCommentsResponse,
                    parse_obj_as(
                        type_=CreateCommentReplyCommentsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
