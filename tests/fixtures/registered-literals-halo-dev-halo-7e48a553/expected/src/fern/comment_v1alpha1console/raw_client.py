

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.comment import Comment
from ..types.comment_email_owner import CommentEmailOwner
from ..types.listed_comment_list import ListedCommentList
from ..types.ref import Ref
from ..types.reply import Reply
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCommentV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_comments(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        keyword: typing.Optional[str] = None,
        approved: typing.Optional[str] = None,
        owner_kind: typing.Optional[str] = None,
        owner_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListedCommentList]:
        """
        List comments with pagination, sorting, keyword, and commenter filters.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number. Default is 0.

        size : typing.Optional[int]
            Size number. Default is 0.

        label_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Label selector. e.g.: hidden!=true

        field_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Field selector. e.g.: metadata.name==halo

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        keyword : typing.Optional[str]
            Keyword used to match the raw comment text.

        approved : typing.Optional[str]
            Approval state filter. When false, comments with pending replies are also included.

        owner_kind : typing.Optional[str]
            Kind of the commenter identity. Defaults to User when ownerName is provided.

        owner_name : typing.Optional[str]
            Name of the commenter identity to filter by.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListedCommentList]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/comments",
            method="GET",
            params={
                "page": page,
                "size": size,
                "labelSelector": label_selector,
                "fieldSelector": field_selector,
                "sort": sort,
                "keyword": keyword,
                "approved": approved,
                "ownerKind": owner_kind,
                "ownerName": owner_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListedCommentList,
                    parse_obj_as(
                        type_=ListedCommentList,
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

    def create_comment(
        self,
        *,
        content: str,
        raw: str,
        subject_ref: Ref,
        allow_notification: typing.Optional[bool] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        owner: typing.Optional[CommentEmailOwner] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Comment]:
        """
        Create a comment for a subject. Console-created comments are created through the comment service with request IP and user agent captured.

        Parameters
        ----------
        content : str
            Rendered HTML content for the comment. Unsafe HTML is rejected.

        raw : str
            Original comment text submitted by the editor.

        subject_ref : Ref

        allow_notification : typing.Optional[bool]
            Whether to notify the owner of future replies. Only an explicit false disables notifications.

        hidden : typing.Optional[bool]
            Whether the comment should be hidden from normal display.

        owner : typing.Optional[CommentEmailOwner]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Comment]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/comments",
            method="POST",
            json={
                "allowNotification": allow_notification,
                "content": content,
                "hidden": hidden,
                "owner": convert_and_respect_annotation_metadata(
                    object_=owner, annotation=CommentEmailOwner, direction="write"
                ),
                "raw": raw,
                "subjectRef": convert_and_respect_annotation_metadata(
                    object_=subject_ref, annotation=Ref, direction="write"
                ),
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
                    Comment,
                    parse_obj_as(
                        type_=Comment,
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

    def update_comment_content(
        self,
        name: str,
        *,
        content: str,
        raw: str,
        version: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Comment]:
        """
        Update only the body of an existing comment. Requires its current version.

        Parameters
        ----------
        name : str

        content : str

        raw : str

        version : int
            Resource version when the editor was opened.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Comment]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/comments/{encode_path_param(name)}/content",
            method="PUT",
            json={
                "content": content,
                "raw": raw,
                "version": version,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Comment,
                    parse_obj_as(
                        type_=Comment,
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

    def create_reply(
        self,
        name: str,
        *,
        content: str,
        raw: str,
        allow_notification: typing.Optional[bool] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        owner: typing.Optional[CommentEmailOwner] = OMIT,
        quote_reply: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Reply]:
        """
        Create an approved reply under an existing comment.

        Parameters
        ----------
        name : str
            metadata.name of the comment to reply to.

        content : str
            Rendered HTML content for the reply. Unsafe HTML is rejected.

        raw : str
            Original reply text submitted by the editor.

        allow_notification : typing.Optional[bool]
            Whether to notify the owner of future replies. Only an explicit false disables notifications.

        hidden : typing.Optional[bool]
            Whether the reply should be hidden from normal display.

        owner : typing.Optional[CommentEmailOwner]

        quote_reply : typing.Optional[str]
            Metadata name of the reply being quoted, if this reply quotes another reply.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Reply]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/comments/{encode_path_param(name)}/reply",
            method="POST",
            json={
                "allowNotification": allow_notification,
                "content": content,
                "hidden": hidden,
                "owner": convert_and_respect_annotation_metadata(
                    object_=owner, annotation=CommentEmailOwner, direction="write"
                ),
                "quoteReply": quote_reply,
                "raw": raw,
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
                    Reply,
                    parse_obj_as(
                        type_=Reply,
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


class AsyncRawCommentV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_comments(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        keyword: typing.Optional[str] = None,
        approved: typing.Optional[str] = None,
        owner_kind: typing.Optional[str] = None,
        owner_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListedCommentList]:
        """
        List comments with pagination, sorting, keyword, and commenter filters.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number. Default is 0.

        size : typing.Optional[int]
            Size number. Default is 0.

        label_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Label selector. e.g.: hidden!=true

        field_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Field selector. e.g.: metadata.name==halo

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        keyword : typing.Optional[str]
            Keyword used to match the raw comment text.

        approved : typing.Optional[str]
            Approval state filter. When false, comments with pending replies are also included.

        owner_kind : typing.Optional[str]
            Kind of the commenter identity. Defaults to User when ownerName is provided.

        owner_name : typing.Optional[str]
            Name of the commenter identity to filter by.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListedCommentList]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/comments",
            method="GET",
            params={
                "page": page,
                "size": size,
                "labelSelector": label_selector,
                "fieldSelector": field_selector,
                "sort": sort,
                "keyword": keyword,
                "approved": approved,
                "ownerKind": owner_kind,
                "ownerName": owner_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListedCommentList,
                    parse_obj_as(
                        type_=ListedCommentList,
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

    async def create_comment(
        self,
        *,
        content: str,
        raw: str,
        subject_ref: Ref,
        allow_notification: typing.Optional[bool] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        owner: typing.Optional[CommentEmailOwner] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Comment]:
        """
        Create a comment for a subject. Console-created comments are created through the comment service with request IP and user agent captured.

        Parameters
        ----------
        content : str
            Rendered HTML content for the comment. Unsafe HTML is rejected.

        raw : str
            Original comment text submitted by the editor.

        subject_ref : Ref

        allow_notification : typing.Optional[bool]
            Whether to notify the owner of future replies. Only an explicit false disables notifications.

        hidden : typing.Optional[bool]
            Whether the comment should be hidden from normal display.

        owner : typing.Optional[CommentEmailOwner]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Comment]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/comments",
            method="POST",
            json={
                "allowNotification": allow_notification,
                "content": content,
                "hidden": hidden,
                "owner": convert_and_respect_annotation_metadata(
                    object_=owner, annotation=CommentEmailOwner, direction="write"
                ),
                "raw": raw,
                "subjectRef": convert_and_respect_annotation_metadata(
                    object_=subject_ref, annotation=Ref, direction="write"
                ),
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
                    Comment,
                    parse_obj_as(
                        type_=Comment,
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

    async def update_comment_content(
        self,
        name: str,
        *,
        content: str,
        raw: str,
        version: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Comment]:
        """
        Update only the body of an existing comment. Requires its current version.

        Parameters
        ----------
        name : str

        content : str

        raw : str

        version : int
            Resource version when the editor was opened.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Comment]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/comments/{encode_path_param(name)}/content",
            method="PUT",
            json={
                "content": content,
                "raw": raw,
                "version": version,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Comment,
                    parse_obj_as(
                        type_=Comment,
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

    async def create_reply(
        self,
        name: str,
        *,
        content: str,
        raw: str,
        allow_notification: typing.Optional[bool] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        owner: typing.Optional[CommentEmailOwner] = OMIT,
        quote_reply: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Reply]:
        """
        Create an approved reply under an existing comment.

        Parameters
        ----------
        name : str
            metadata.name of the comment to reply to.

        content : str
            Rendered HTML content for the reply. Unsafe HTML is rejected.

        raw : str
            Original reply text submitted by the editor.

        allow_notification : typing.Optional[bool]
            Whether to notify the owner of future replies. Only an explicit false disables notifications.

        hidden : typing.Optional[bool]
            Whether the reply should be hidden from normal display.

        owner : typing.Optional[CommentEmailOwner]

        quote_reply : typing.Optional[str]
            Metadata name of the reply being quoted, if this reply quotes another reply.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Reply]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/comments/{encode_path_param(name)}/reply",
            method="POST",
            json={
                "allowNotification": allow_notification,
                "content": content,
                "hidden": hidden,
                "owner": convert_and_respect_annotation_metadata(
                    object_=owner, annotation=CommentEmailOwner, direction="write"
                ),
                "quoteReply": quote_reply,
                "raw": raw,
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
                    Reply,
                    parse_obj_as(
                        type_=Reply,
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
