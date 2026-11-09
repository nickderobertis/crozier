

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.gone_error import GoneError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.range_not_satisfiable_error import RangeNotSatisfiableError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.forbidden_error_body import ForbiddenErrorBody
from ..types.id import Id
from ..types.internal_server_error_body import InternalServerErrorBody
from ..types.not_found_error_body import NotFoundErrorBody
from ..types.order import Order
from ..types.range_not_satisfiable_error_body import RangeNotSatisfiableErrorBody
from ..types.rate_limit_error import RateLimitError
from ..types.tombstone import Tombstone
from ..types.unauthorized_error_body import UnauthorizedErrorBody
from .types.get_file_request_disposition import GetFileRequestDisposition
from .types.head_file_request_disposition import HeadFileRequestDisposition
from .types.list_files_request_sort import ListFilesRequestSort
from .types.list_files_response import ListFilesResponse
from pydantic import ValidationError


class RawFilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_files(
        self,
        *,
        member_of: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[ListFilesRequestSort] = None,
        order: typing.Optional[Order] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListFilesResponse]:
        """
        Retrieve and list file in the repository. This endpoint returns key metadata describing each file. The response can be filtered by memberOf to show files attached to a specific entity, and supports pagination and sorting.

        Parameters
        ----------
        member_of : typing.Optional[str]
            Filter to only files that are directly attached to a specific entity (e.g., files within a collection or object).

        limit : typing.Optional[int]
            Maximum number of entities to return.

        offset : typing.Optional[int]
            Number of items to skip before returning the results, useful for pagination.

        sort : typing.Optional[ListFilesRequestSort]
            Field to sort by, such as `filename` or `createdAt`.

        order : typing.Optional[Order]
            Sort order:
            * `asc` - Ascending, from A to Z
            * `desc` - Descending, from Z to A

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListFilesResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "files",
            method="GET",
            params={
                "memberOf": member_of,
                "limit": limit,
                "offset": offset,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListFilesResponse,
                    parse_obj_as(
                        type_=ListFilesResponse,
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
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RateLimitError,
                        parse_obj_as(
                            type_=RateLimitError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    def get_file(
        self,
        id: Id,
        *,
        disposition: typing.Optional[GetFileRequestDisposition] = None,
        filename: typing.Optional[str] = None,
        no_redirect: typing.Optional[bool] = None,
        range: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Retrieve a file. The file can be returned inline (e.g., displayed in the browser) or as an attachment for download (e.g., prompting a save dialog), based on the disposition parameter.
        The API can serve the file directly or redirect to the location of the file.

        Parameters
        ----------
        id : Id
            The ID of the file.

        disposition : typing.Optional[GetFileRequestDisposition]
            The HTTP Content-Disposition for how the file should be handled by the client.

        filename : typing.Optional[str]
            When the file is served as an attachment, the name to use when saving.

        no_redirect : typing.Optional[bool]
            Return the location as JSON instead of a 302 redirect.

        range : typing.Optional[str]
            Request specific byte range(s) of the file. Supports standard HTTP Range header syntax.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"file/{encode_path_param(id)}",
            method="GET",
            params={
                "disposition": disposition,
                "filename": filename,
                "noRedirect": no_redirect,
            },
            headers={
                "Range": str(range) if range is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
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
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Tombstone,
                        parse_obj_as(
                            type_=Tombstone,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 416:
                raise RangeNotSatisfiableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RangeNotSatisfiableErrorBody,
                        parse_obj_as(
                            type_=RangeNotSatisfiableErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RateLimitError,
                        parse_obj_as(
                            type_=RateLimitError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    def head_file(
        self,
        id: Id,
        *,
        disposition: typing.Optional[HeadFileRequestDisposition] = None,
        filename: typing.Optional[str] = None,
        no_redirect: typing.Optional[bool] = None,
        range: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Retrieve file metadata headers without downloading the file content. Returns the same headers as GET but with no response body, useful for checking file availability, size, type, and caching information.

        Parameters
        ----------
        id : Id
            The ID of the file.

        disposition : typing.Optional[HeadFileRequestDisposition]
            The HTTP Content-Disposition for how the file should be handled by the client.

        filename : typing.Optional[str]
            When the file is served as an attachment, the name to use when saving.

        no_redirect : typing.Optional[bool]
            Return the location as JSON instead of a 302 redirect.

        range : typing.Optional[str]
            Request specific byte range(s) of the file. Supports standard HTTP Range header syntax.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"file/{encode_path_param(id)}",
            method="HEAD",
            params={
                "disposition": disposition,
                "filename": filename,
                "noRedirect": no_redirect,
            },
            headers={
                "Range": str(range) if range is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
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
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Tombstone,
                        parse_obj_as(
                            type_=Tombstone,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RateLimitError,
                        parse_obj_as(
                            type_=RateLimitError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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


class AsyncRawFilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_files(
        self,
        *,
        member_of: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[ListFilesRequestSort] = None,
        order: typing.Optional[Order] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListFilesResponse]:
        """
        Retrieve and list file in the repository. This endpoint returns key metadata describing each file. The response can be filtered by memberOf to show files attached to a specific entity, and supports pagination and sorting.

        Parameters
        ----------
        member_of : typing.Optional[str]
            Filter to only files that are directly attached to a specific entity (e.g., files within a collection or object).

        limit : typing.Optional[int]
            Maximum number of entities to return.

        offset : typing.Optional[int]
            Number of items to skip before returning the results, useful for pagination.

        sort : typing.Optional[ListFilesRequestSort]
            Field to sort by, such as `filename` or `createdAt`.

        order : typing.Optional[Order]
            Sort order:
            * `asc` - Ascending, from A to Z
            * `desc` - Descending, from Z to A

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListFilesResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "files",
            method="GET",
            params={
                "memberOf": member_of,
                "limit": limit,
                "offset": offset,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListFilesResponse,
                    parse_obj_as(
                        type_=ListFilesResponse,
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
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RateLimitError,
                        parse_obj_as(
                            type_=RateLimitError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    async def get_file(
        self,
        id: Id,
        *,
        disposition: typing.Optional[GetFileRequestDisposition] = None,
        filename: typing.Optional[str] = None,
        no_redirect: typing.Optional[bool] = None,
        range: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Retrieve a file. The file can be returned inline (e.g., displayed in the browser) or as an attachment for download (e.g., prompting a save dialog), based on the disposition parameter.
        The API can serve the file directly or redirect to the location of the file.

        Parameters
        ----------
        id : Id
            The ID of the file.

        disposition : typing.Optional[GetFileRequestDisposition]
            The HTTP Content-Disposition for how the file should be handled by the client.

        filename : typing.Optional[str]
            When the file is served as an attachment, the name to use when saving.

        no_redirect : typing.Optional[bool]
            Return the location as JSON instead of a 302 redirect.

        range : typing.Optional[str]
            Request specific byte range(s) of the file. Supports standard HTTP Range header syntax.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"file/{encode_path_param(id)}",
            method="GET",
            params={
                "disposition": disposition,
                "filename": filename,
                "noRedirect": no_redirect,
            },
            headers={
                "Range": str(range) if range is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
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
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Tombstone,
                        parse_obj_as(
                            type_=Tombstone,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 416:
                raise RangeNotSatisfiableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RangeNotSatisfiableErrorBody,
                        parse_obj_as(
                            type_=RangeNotSatisfiableErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RateLimitError,
                        parse_obj_as(
                            type_=RateLimitError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    async def head_file(
        self,
        id: Id,
        *,
        disposition: typing.Optional[HeadFileRequestDisposition] = None,
        filename: typing.Optional[str] = None,
        no_redirect: typing.Optional[bool] = None,
        range: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Retrieve file metadata headers without downloading the file content. Returns the same headers as GET but with no response body, useful for checking file availability, size, type, and caching information.

        Parameters
        ----------
        id : Id
            The ID of the file.

        disposition : typing.Optional[HeadFileRequestDisposition]
            The HTTP Content-Disposition for how the file should be handled by the client.

        filename : typing.Optional[str]
            When the file is served as an attachment, the name to use when saving.

        no_redirect : typing.Optional[bool]
            Return the location as JSON instead of a 302 redirect.

        range : typing.Optional[str]
            Request specific byte range(s) of the file. Supports standard HTTP Range header syntax.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"file/{encode_path_param(id)}",
            method="HEAD",
            params={
                "disposition": disposition,
                "filename": filename,
                "noRedirect": no_redirect,
            },
            headers={
                "Range": str(range) if range is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
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
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Tombstone,
                        parse_obj_as(
                            type_=Tombstone,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RateLimitError,
                        parse_obj_as(
                            type_=RateLimitError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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
