

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
from ..errors.method_not_allowed_error import MethodNotAllowedError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error import Error
from ..types.update_student_request import UpdateStudentRequest
from ..types.update_student_response import UpdateStudentResponse
from .types.get_students_id_v3request_fields_item import GetStudentsIdV3RequestFieldsItem
from .types.get_students_id_v3response import GetStudentsIdV3Response
from .types.get_students_v3request_fields_item import GetStudentsV3RequestFieldsItem
from .types.get_students_v3response import GetStudentsV3Response
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawStudentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_students_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        status: typing.Optional[str] = None,
        fields: typing.Optional[
            typing.Union[GetStudentsV3RequestFieldsItem, typing.Sequence[GetStudentsV3RequestFieldsItem]]
        ] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetStudentsV3Response]:
        """
        The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. Returns paginated students. The normal collection includes only Procare Desktop enrollment statuses configured as visible for the school. status defaults to active plus hold; all includes active, hold, inactive and graduate. Unknown status values also fall back to active plus hold.

        ids switches to a batch lookup of at most 200 UUIDs and requires school_id; this branch bypasses the normal status selection. Missing IDs are omitted. fields selects JSON properties, case-insensitively, and duplicate field names are removed.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.

        ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional batch of at most 200 student UUIDs; requires school_id. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        status : typing.Optional[str]
            Normal collection: active, hold, inactive, graduate or all. Omitted/unrecognized values select active plus hold.

        fields : typing.Optional[typing.Union[GetStudentsV3RequestFieldsItem, typing.Sequence[GetStudentsV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400. Names are normalized to lowercase. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        page : typing.Optional[int]
            One-based page number.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetStudentsV3Response]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "students",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "ids": ids,
                "status": status,
                "fields": fields,
                "page": page,
                "per_page": per_page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetStudentsV3Response,
                    parse_obj_as(
                        type_=GetStudentsV3Response,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def get_students_id_v3(
        self,
        id: str,
        *,
        company_id: str,
        school_id: str,
        fields: typing.Optional[
            typing.Union[GetStudentsIdV3RequestFieldsItem, typing.Sequence[GetStudentsIdV3RequestFieldsItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetStudentsIdV3Response]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Requires school_id. Returns the full student or the requested field projection. This item read does not apply the collection's session-school assignment check.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        fields : typing.Optional[typing.Union[GetStudentsIdV3RequestFieldsItem, typing.Sequence[GetStudentsIdV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400.  Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetStudentsIdV3Response]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"students/{encode_path_param(id)}",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetStudentsIdV3Response,
                    parse_obj_as(
                        type_=GetStudentsIdV3Response,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def patch_students_id_v3(
        self,
        id: str,
        *,
        company_id: str,
        school_id: str,
        request: UpdateStudentRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateStudentResponse]:
        """
        Requires school_id assigned to the session and an authenticated user belonging to company_id. Attribution comes from that user; updated_by_email is accepted but ignored. At least one update property is required. Unknown properties return 400. Dates and room UUIDs may be cleared with null or an empty string; omission leaves them unchanged.

        Validation uses the resulting student state, including existing values:
        - transition_date_2 requires transition_date.
        - transition_room_override_id requires transition_date.
        - transition_room_2_id requires transition_date_2.
        - Effective start date must precede transition_date; transition_date must precede transition_date_2 when present; both transitions must precede the effective withdrawal date.
        - Specified room IDs must be active rooms in the student's school.

        Returns an update summary containing student_data, not the full GET representation. Unlike the shared write decoder, this handler does not enforce Content-Type. A post-update retrieval failure can return 404 or 500 after the write has executed.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        request : UpdateStudentRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateStudentResponse]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"students/{encode_path_param(id)}",
            method="PATCH",
            params={
                "company_id": company_id,
                "school_id": school_id,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=UpdateStudentRequest, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateStudentResponse,
                    parse_obj_as(
                        type_=UpdateStudentResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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


class AsyncRawStudentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_students_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        status: typing.Optional[str] = None,
        fields: typing.Optional[
            typing.Union[GetStudentsV3RequestFieldsItem, typing.Sequence[GetStudentsV3RequestFieldsItem]]
        ] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetStudentsV3Response]:
        """
        The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. Returns paginated students. The normal collection includes only Procare Desktop enrollment statuses configured as visible for the school. status defaults to active plus hold; all includes active, hold, inactive and graduate. Unknown status values also fall back to active plus hold.

        ids switches to a batch lookup of at most 200 UUIDs and requires school_id; this branch bypasses the normal status selection. Missing IDs are omitted. fields selects JSON properties, case-insensitively, and duplicate field names are removed.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.

        ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional batch of at most 200 student UUIDs; requires school_id. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        status : typing.Optional[str]
            Normal collection: active, hold, inactive, graduate or all. Omitted/unrecognized values select active plus hold.

        fields : typing.Optional[typing.Union[GetStudentsV3RequestFieldsItem, typing.Sequence[GetStudentsV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400. Names are normalized to lowercase. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        page : typing.Optional[int]
            One-based page number.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetStudentsV3Response]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "students",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "ids": ids,
                "status": status,
                "fields": fields,
                "page": page,
                "per_page": per_page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetStudentsV3Response,
                    parse_obj_as(
                        type_=GetStudentsV3Response,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def get_students_id_v3(
        self,
        id: str,
        *,
        company_id: str,
        school_id: str,
        fields: typing.Optional[
            typing.Union[GetStudentsIdV3RequestFieldsItem, typing.Sequence[GetStudentsIdV3RequestFieldsItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetStudentsIdV3Response]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Requires school_id. Returns the full student or the requested field projection. This item read does not apply the collection's session-school assignment check.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        fields : typing.Optional[typing.Union[GetStudentsIdV3RequestFieldsItem, typing.Sequence[GetStudentsIdV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400.  Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetStudentsIdV3Response]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"students/{encode_path_param(id)}",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetStudentsIdV3Response,
                    parse_obj_as(
                        type_=GetStudentsIdV3Response,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def patch_students_id_v3(
        self,
        id: str,
        *,
        company_id: str,
        school_id: str,
        request: UpdateStudentRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateStudentResponse]:
        """
        Requires school_id assigned to the session and an authenticated user belonging to company_id. Attribution comes from that user; updated_by_email is accepted but ignored. At least one update property is required. Unknown properties return 400. Dates and room UUIDs may be cleared with null or an empty string; omission leaves them unchanged.

        Validation uses the resulting student state, including existing values:
        - transition_date_2 requires transition_date.
        - transition_room_override_id requires transition_date.
        - transition_room_2_id requires transition_date_2.
        - Effective start date must precede transition_date; transition_date must precede transition_date_2 when present; both transitions must precede the effective withdrawal date.
        - Specified room IDs must be active rooms in the student's school.

        Returns an update summary containing student_data, not the full GET representation. Unlike the shared write decoder, this handler does not enforce Content-Type. A post-update retrieval failure can return 404 or 500 after the write has executed.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        request : UpdateStudentRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateStudentResponse]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"students/{encode_path_param(id)}",
            method="PATCH",
            params={
                "company_id": company_id,
                "school_id": school_id,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=UpdateStudentRequest, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateStudentResponse,
                    parse_obj_as(
                        type_=UpdateStudentResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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
