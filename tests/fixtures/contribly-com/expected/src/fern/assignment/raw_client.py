

import datetime as dt
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
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.assignment import Assignment
from ..types.error_response import ErrorResponse
from ..types.media_usage import MediaUsage
from ..types.tag import Tag
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAssignmentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_assignments(
        self,
        *,
        owned_by: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        open: typing.Optional[bool] = None,
        always_open: typing.Optional[bool] = None,
        tag: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Assignment]]:
        """
        Parameters
        ----------
        owned_by : typing.Optional[str]
            Restrict results to assignments owned by this user.

        page : typing.Optional[int]
            Pagination page

        page_size : typing.Optional[int]
            Pagination page size

        q : typing.Optional[str]
            Restrict results to assignments whose name or description matches this keyword.

        url_words : typing.Optional[str]
            Select an assignment by urlWords.

        open : typing.Optional[bool]
            Select open or closed assignments

        always_open : typing.Optional[bool]
            Select assignments with no closing date.

        tag : typing.Optional[str]
            Restrict results to assignments which are tagged with this tag.

        name : typing.Optional[str]
            Restrict results to the assignment (or potentially assignments) with this exact name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Assignment]]
            A list of assignments
        """
        _response = self._client_wrapper.httpx_client.request(
            "assignments",
            method="GET",
            params={
                "ownedBy": owned_by,
                "page": page,
                "pageSize": page_size,
                "q": q,
                "urlWords": url_words,
                "open": open,
                "alwaysOpen": always_open,
                "tag": tag,
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Assignment],
                    parse_obj_as(
                        type_=typing.List[Assignment],
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

    def create_a_new_assignment(
        self,
        *,
        name: str,
        allows_anonymous_contributions: typing.Optional[bool] = OMIT,
        cover: typing.Optional[MediaUsage] = OMIT,
        description: typing.Optional[str] = OMIT,
        embargo: typing.Optional[dt.datetime] = OMIT,
        ends: typing.Optional[dt.datetime] = OMIT,
        featured: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        media_required: typing.Optional[bool] = OMIT,
        moderator: typing.Optional[str] = OMIT,
        receipt_message: typing.Optional[str] = OMIT,
        starts: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[Tag]] = OMIT,
        url_words: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Assignment]:
        """
        Parameters
        ----------
        name : str

        allows_anonymous_contributions : typing.Optional[bool]

        cover : typing.Optional[MediaUsage]

        description : typing.Optional[str]

        embargo : typing.Optional[dt.datetime]

        ends : typing.Optional[dt.datetime]

        featured : typing.Optional[bool]

        id : typing.Optional[str]

        media_required : typing.Optional[bool]

        moderator : typing.Optional[str]
            Optional credential id of the login which will moderator this assignment.

        receipt_message : typing.Optional[str]
            An optional assignment specific message to be displayed on successful contribution submission. For example, this might be used to inform contributors of assignment specific moderation time frames.

        starts : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[Tag]]

        url_words : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Assignment]
            Assignment created
        """
        _response = self._client_wrapper.httpx_client.request(
            "assignments",
            method="POST",
            json={
                "allowsAnonymousContributions": allows_anonymous_contributions,
                "cover": convert_and_respect_annotation_metadata(
                    object_=cover, annotation=MediaUsage, direction="write"
                ),
                "description": description,
                "embargo": embargo,
                "ends": ends,
                "featured": featured,
                "id": id,
                "mediaRequired": media_required,
                "moderator": moderator,
                "name": name,
                "receiptMessage": receipt_message,
                "starts": starts,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[Tag], direction="write"
                ),
                "urlWords": url_words,
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
                    Assignment,
                    parse_obj_as(
                        type_=Assignment,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def get_a_single_assigment_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Assignment]:
        """
        Parameters
        ----------
        id : str
            Id of the assignment to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Assignment]
            Assignment found
        """
        _response = self._client_wrapper.httpx_client.request(
            f"assignments/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Assignment,
                    parse_obj_as(
                        type_=Assignment,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_this_assignment_and_all_of_its_contributions(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : str
            Id of the assignment to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"assignments/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 403:
                raise ForbiddenError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawAssignmentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_assignments(
        self,
        *,
        owned_by: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        open: typing.Optional[bool] = None,
        always_open: typing.Optional[bool] = None,
        tag: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Assignment]]:
        """
        Parameters
        ----------
        owned_by : typing.Optional[str]
            Restrict results to assignments owned by this user.

        page : typing.Optional[int]
            Pagination page

        page_size : typing.Optional[int]
            Pagination page size

        q : typing.Optional[str]
            Restrict results to assignments whose name or description matches this keyword.

        url_words : typing.Optional[str]
            Select an assignment by urlWords.

        open : typing.Optional[bool]
            Select open or closed assignments

        always_open : typing.Optional[bool]
            Select assignments with no closing date.

        tag : typing.Optional[str]
            Restrict results to assignments which are tagged with this tag.

        name : typing.Optional[str]
            Restrict results to the assignment (or potentially assignments) with this exact name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Assignment]]
            A list of assignments
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assignments",
            method="GET",
            params={
                "ownedBy": owned_by,
                "page": page,
                "pageSize": page_size,
                "q": q,
                "urlWords": url_words,
                "open": open,
                "alwaysOpen": always_open,
                "tag": tag,
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Assignment],
                    parse_obj_as(
                        type_=typing.List[Assignment],
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

    async def create_a_new_assignment(
        self,
        *,
        name: str,
        allows_anonymous_contributions: typing.Optional[bool] = OMIT,
        cover: typing.Optional[MediaUsage] = OMIT,
        description: typing.Optional[str] = OMIT,
        embargo: typing.Optional[dt.datetime] = OMIT,
        ends: typing.Optional[dt.datetime] = OMIT,
        featured: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        media_required: typing.Optional[bool] = OMIT,
        moderator: typing.Optional[str] = OMIT,
        receipt_message: typing.Optional[str] = OMIT,
        starts: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[Tag]] = OMIT,
        url_words: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Assignment]:
        """
        Parameters
        ----------
        name : str

        allows_anonymous_contributions : typing.Optional[bool]

        cover : typing.Optional[MediaUsage]

        description : typing.Optional[str]

        embargo : typing.Optional[dt.datetime]

        ends : typing.Optional[dt.datetime]

        featured : typing.Optional[bool]

        id : typing.Optional[str]

        media_required : typing.Optional[bool]

        moderator : typing.Optional[str]
            Optional credential id of the login which will moderator this assignment.

        receipt_message : typing.Optional[str]
            An optional assignment specific message to be displayed on successful contribution submission. For example, this might be used to inform contributors of assignment specific moderation time frames.

        starts : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[Tag]]

        url_words : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Assignment]
            Assignment created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assignments",
            method="POST",
            json={
                "allowsAnonymousContributions": allows_anonymous_contributions,
                "cover": convert_and_respect_annotation_metadata(
                    object_=cover, annotation=MediaUsage, direction="write"
                ),
                "description": description,
                "embargo": embargo,
                "ends": ends,
                "featured": featured,
                "id": id,
                "mediaRequired": media_required,
                "moderator": moderator,
                "name": name,
                "receiptMessage": receipt_message,
                "starts": starts,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[Tag], direction="write"
                ),
                "urlWords": url_words,
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
                    Assignment,
                    parse_obj_as(
                        type_=Assignment,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def get_a_single_assigment_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Assignment]:
        """
        Parameters
        ----------
        id : str
            Id of the assignment to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Assignment]
            Assignment found
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"assignments/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Assignment,
                    parse_obj_as(
                        type_=Assignment,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_this_assignment_and_all_of_its_contributions(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : str
            Id of the assignment to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"assignments/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 403:
                raise ForbiddenError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
