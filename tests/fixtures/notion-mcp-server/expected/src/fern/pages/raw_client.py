

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
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..types.conflict_error_body import ConflictErrorBody
from ..types.forbidden_error_body import ForbiddenErrorBody
from ..types.move_page_parent_request import MovePageParentRequest
from ..types.not_found_error_body import NotFoundErrorBody
from ..types.too_many_requests_error_body import TooManyRequestsErrorBody
from .types.retrieve_page_markdown_response import RetrievePageMarkdownResponse
from .types.update_page_markdown_request_insert_content import UpdatePageMarkdownRequestInsertContent
from .types.update_page_markdown_request_replace_content import UpdatePageMarkdownRequestReplaceContent
from .types.update_page_markdown_request_replace_content_range import UpdatePageMarkdownRequestReplaceContentRange
from .types.update_page_markdown_request_type import UpdatePageMarkdownRequestType
from .types.update_page_markdown_request_update_content import UpdatePageMarkdownRequestUpdateContent
from .types.update_page_markdown_response import UpdatePageMarkdownResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def move_page(
        self, page_id: str, *, parent: MovePageParentRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Move a page to a different parent location

        Parameters
        ----------
        page_id : str
            Identifier for a Notion page

        parent : MovePageParentRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/pages/{encode_path_param(page_id)}/move",
            method="POST",
            json={
                "parent": convert_and_respect_annotation_metadata(
                    object_=parent, annotation=MovePageParentRequest, direction="write"
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_page_markdown(
        self,
        page_id: str,
        *,
        include_transcript: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RetrievePageMarkdownResponse]:
        """
        Retrieve the full content of a Notion page rendered as enhanced Markdown. Designed for agentic and developer tools that work natively with Markdown instead of the block JSON returned by Retrieve block children.

        Parameters
        ----------
        page_id : str
            Identifier for a Notion page (or block) to read or update as markdown.

        include_transcript : typing.Optional[bool]
            Whether to include meeting note transcripts. When false (default), a placeholder with the meeting note URL is shown instead of the full transcript.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrievePageMarkdownResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/pages/{encode_path_param(page_id)}/markdown",
            method="GET",
            params={
                "include_transcript": include_transcript,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrievePageMarkdownResponse,
                    parse_obj_as(
                        type_=RetrievePageMarkdownResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
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

    def update_page_markdown(
        self,
        page_id: str,
        *,
        type: UpdatePageMarkdownRequestType,
        replace_content: typing.Optional[UpdatePageMarkdownRequestReplaceContent] = OMIT,
        update_content: typing.Optional[UpdatePageMarkdownRequestUpdateContent] = OMIT,
        insert_content: typing.Optional[UpdatePageMarkdownRequestInsertContent] = OMIT,
        replace_content_range: typing.Optional[UpdatePageMarkdownRequestReplaceContentRange] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdatePageMarkdownResponse]:
        """
        Update the content of a Notion page using enhanced Markdown. Prefer `replace_content` to overwrite the whole page or `update_content` for targeted find-and-replace edits.

        Parameters
        ----------
        page_id : str
            Identifier for a Notion page (or block) to read or update as markdown.

        type : UpdatePageMarkdownRequestType
            The kind of edit to apply. Prefer `replace_content` (overwrite the whole page) or `update_content` (targeted find-and-replace). `insert_content` and `replace_content_range` are deprecated.

        replace_content : typing.Optional[UpdatePageMarkdownRequestReplaceContent]
            Provide when type is `replace_content`. Replaces the entire page content.

        update_content : typing.Optional[UpdatePageMarkdownRequestUpdateContent]
            Provide when type is `update_content`. Applies targeted find-and-replace edits.

        insert_content : typing.Optional[UpdatePageMarkdownRequestInsertContent]
            Deprecated. Provide when type is `insert_content`. Inserts Markdown at a position.

        replace_content_range : typing.Optional[UpdatePageMarkdownRequestReplaceContentRange]
            Deprecated. Provide when type is `replace_content_range`. Replaces a selected range of Markdown.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdatePageMarkdownResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/pages/{encode_path_param(page_id)}/markdown",
            method="PATCH",
            json={
                "type": type,
                "replace_content": convert_and_respect_annotation_metadata(
                    object_=replace_content, annotation=UpdatePageMarkdownRequestReplaceContent, direction="write"
                ),
                "update_content": convert_and_respect_annotation_metadata(
                    object_=update_content, annotation=UpdatePageMarkdownRequestUpdateContent, direction="write"
                ),
                "insert_content": convert_and_respect_annotation_metadata(
                    object_=insert_content, annotation=UpdatePageMarkdownRequestInsertContent, direction="write"
                ),
                "replace_content_range": convert_and_respect_annotation_metadata(
                    object_=replace_content_range,
                    annotation=UpdatePageMarkdownRequestReplaceContentRange,
                    direction="write",
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
                    UpdatePageMarkdownResponse,
                    parse_obj_as(
                        type_=UpdatePageMarkdownResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ConflictErrorBody,
                        parse_obj_as(
                            type_=ConflictErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
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


class AsyncRawPagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def move_page(
        self, page_id: str, *, parent: MovePageParentRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Move a page to a different parent location

        Parameters
        ----------
        page_id : str
            Identifier for a Notion page

        parent : MovePageParentRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/pages/{encode_path_param(page_id)}/move",
            method="POST",
            json={
                "parent": convert_and_respect_annotation_metadata(
                    object_=parent, annotation=MovePageParentRequest, direction="write"
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_page_markdown(
        self,
        page_id: str,
        *,
        include_transcript: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RetrievePageMarkdownResponse]:
        """
        Retrieve the full content of a Notion page rendered as enhanced Markdown. Designed for agentic and developer tools that work natively with Markdown instead of the block JSON returned by Retrieve block children.

        Parameters
        ----------
        page_id : str
            Identifier for a Notion page (or block) to read or update as markdown.

        include_transcript : typing.Optional[bool]
            Whether to include meeting note transcripts. When false (default), a placeholder with the meeting note URL is shown instead of the full transcript.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrievePageMarkdownResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/pages/{encode_path_param(page_id)}/markdown",
            method="GET",
            params={
                "include_transcript": include_transcript,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrievePageMarkdownResponse,
                    parse_obj_as(
                        type_=RetrievePageMarkdownResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
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

    async def update_page_markdown(
        self,
        page_id: str,
        *,
        type: UpdatePageMarkdownRequestType,
        replace_content: typing.Optional[UpdatePageMarkdownRequestReplaceContent] = OMIT,
        update_content: typing.Optional[UpdatePageMarkdownRequestUpdateContent] = OMIT,
        insert_content: typing.Optional[UpdatePageMarkdownRequestInsertContent] = OMIT,
        replace_content_range: typing.Optional[UpdatePageMarkdownRequestReplaceContentRange] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdatePageMarkdownResponse]:
        """
        Update the content of a Notion page using enhanced Markdown. Prefer `replace_content` to overwrite the whole page or `update_content` for targeted find-and-replace edits.

        Parameters
        ----------
        page_id : str
            Identifier for a Notion page (or block) to read or update as markdown.

        type : UpdatePageMarkdownRequestType
            The kind of edit to apply. Prefer `replace_content` (overwrite the whole page) or `update_content` (targeted find-and-replace). `insert_content` and `replace_content_range` are deprecated.

        replace_content : typing.Optional[UpdatePageMarkdownRequestReplaceContent]
            Provide when type is `replace_content`. Replaces the entire page content.

        update_content : typing.Optional[UpdatePageMarkdownRequestUpdateContent]
            Provide when type is `update_content`. Applies targeted find-and-replace edits.

        insert_content : typing.Optional[UpdatePageMarkdownRequestInsertContent]
            Deprecated. Provide when type is `insert_content`. Inserts Markdown at a position.

        replace_content_range : typing.Optional[UpdatePageMarkdownRequestReplaceContentRange]
            Deprecated. Provide when type is `replace_content_range`. Replaces a selected range of Markdown.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdatePageMarkdownResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/pages/{encode_path_param(page_id)}/markdown",
            method="PATCH",
            json={
                "type": type,
                "replace_content": convert_and_respect_annotation_metadata(
                    object_=replace_content, annotation=UpdatePageMarkdownRequestReplaceContent, direction="write"
                ),
                "update_content": convert_and_respect_annotation_metadata(
                    object_=update_content, annotation=UpdatePageMarkdownRequestUpdateContent, direction="write"
                ),
                "insert_content": convert_and_respect_annotation_metadata(
                    object_=insert_content, annotation=UpdatePageMarkdownRequestInsertContent, direction="write"
                ),
                "replace_content_range": convert_and_respect_annotation_metadata(
                    object_=replace_content_range,
                    annotation=UpdatePageMarkdownRequestReplaceContentRange,
                    direction="write",
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
                    UpdatePageMarkdownResponse,
                    parse_obj_as(
                        type_=UpdatePageMarkdownResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ConflictErrorBody,
                        parse_obj_as(
                            type_=ConflictErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
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
