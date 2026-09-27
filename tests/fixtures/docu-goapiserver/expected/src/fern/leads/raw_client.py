

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
from ..errors.method_not_allowed_error import MethodNotAllowedError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unsupported_media_type_error import UnsupportedMediaTypeError
from ..types.bulk_lead_stages_item import BulkLeadStagesItem
from ..types.error import Error
from ..types.intended_start_date_update import IntendedStartDateUpdate
from ..types.lead_stage import LeadStage
from ..types.lead_stages import LeadStages
from ..types.update_intended_start_dates_response import UpdateIntendedStartDatesResponse
from ..types.update_lead_stages_request import UpdateLeadStagesRequest
from .types.get_leads_id_v3request_fields_item import GetLeadsIdV3RequestFieldsItem
from .types.get_leads_id_v3response import GetLeadsIdV3Response
from .types.get_leads_v3request_fields_item import GetLeadsV3RequestFieldsItem
from .types.get_leads_v3request_status import GetLeadsV3RequestStatus
from .types.get_leads_v3request_view import GetLeadsV3RequestView
from .types.get_leads_v3response import GetLeadsV3Response
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawLeadsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_leads_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        view: typing.Optional[GetLeadsV3RequestView] = None,
        fields: typing.Optional[
            typing.Union[GetLeadsV3RequestFieldsItem, typing.Sequence[GetLeadsV3RequestFieldsItem]]
        ] = None,
        ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        query: typing.Optional[str] = None,
        max_results: typing.Optional[int] = None,
        status: typing.Optional[GetLeadsV3RequestStatus] = None,
        date_from: typing.Optional[dt.date] = None,
        date_to: typing.Optional[dt.date] = None,
        age_min: typing.Optional[float] = None,
        age_max: typing.Optional[float] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetLeadsV3Response]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns paginated lead rows, or paginated LeadStages objects when view=stages.

        Normal lookup precedence is ids, then query, then the filtered school collection. ids is limited to 200 UUIDs and missing IDs are omitted. query performs a name search with optional max_results. status, date_from/date_to and age_min/age_max are validated before these branches but only filter the normal school collection; ids and query bypass those filters. Negative ages are accepted for expected children. The age interval defaults to -12 through 180 months. date_to cannot precede date_from, and age_max cannot be smaller than age_min.

        view=stages requires the school in the session assignments and accepts only company_id, school_id, view, page and per_page. Any other parameter in this view returns 400.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        view : typing.Optional[GetLeadsV3RequestView]
            Omit for lead rows; stages includes per-stage timestamps.

        fields : typing.Optional[typing.Union[GetLeadsV3RequestFieldsItem, typing.Sequence[GetLeadsV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400. Normal lead representation only; names are case-sensitive. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Read at most 200 lead UUIDs; takes precedence over query. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        query : typing.Optional[str]
            Name search; used only when ids is omitted.

        max_results : typing.Optional[int]
            Maximum name-search results; 0 keeps the backend default.

        status : typing.Optional[GetLeadsV3RequestStatus]
            Procare lead status; exact case required. Applies only to normal school collection.

        date_from : typing.Optional[dt.date]
            Inclusive start date in YYYY-MM-DD. Optional created-date window for the normal school collection.

        date_to : typing.Optional[dt.date]
            Inclusive end date in YYYY-MM-DD. Optional created-date window for the normal school collection.

        age_min : typing.Optional[float]
            Minimum child age in months; normal school collection only.

        age_max : typing.Optional[float]
            Maximum child age in months; normal school collection only.

        page : typing.Optional[int]
            One-based page number.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetLeadsV3Response]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "leads",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "view": view,
                "fields": fields,
                "ids": ids,
                "query": query,
                "max_results": max_results,
                "status": status,
                "date_from": str(date_from) if date_from is not None else None,
                "date_to": str(date_to) if date_to is not None else None,
                "age_min": age_min,
                "age_max": age_max,
                "page": page,
                "per_page": per_page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLeadsV3Response,
                    parse_obj_as(
                        type_=GetLeadsV3Response,
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

    def patch_leads_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        request: typing.Sequence[BulkLeadStagesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[LeadStages]]:
        """
        Requires school_id assigned to the session. The body is an array of 1 to 200 items, each with lead_id and at least one non-null stage. All items are validated before writes. Missing leads are omitted from the response. Repeated lead IDs are allowed; each appears once in the response in first-occurrence order with its final stages. The batch is not atomic: a database failure returns 500 and stops processing after any earlier writes.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        request : typing.Sequence[BulkLeadStagesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[LeadStages]]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "leads",
            method="PATCH",
            params={
                "company_id": company_id,
                "school_id": school_id,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[BulkLeadStagesItem], direction="write"
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
                    typing.List[LeadStages],
                    parse_obj_as(
                        type_=typing.List[LeadStages],
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
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
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

    def get_leads_id_v3(
        self,
        id: str,
        *,
        company_id: str,
        school_id: str,
        fields: typing.Optional[
            typing.Union[GetLeadsIdV3RequestFieldsItem, typing.Sequence[GetLeadsIdV3RequestFieldsItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetLeadsIdV3Response]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Requires school_id. fields selects properties from the lead projection; unknown fields return 400. Returns 404 when the scoped lead does not exist.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        fields : typing.Optional[typing.Union[GetLeadsIdV3RequestFieldsItem, typing.Sequence[GetLeadsIdV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400.  Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetLeadsIdV3Response]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"leads/{encode_path_param(id)}",
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
                    GetLeadsIdV3Response,
                    parse_obj_as(
                        type_=GetLeadsIdV3Response,
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

    def get_leads_id_stages_v3(
        self, id: str, *, company_id: str, school_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[LeadStage]]:
        """
        Requires school_id assigned to the session. Each stage includes its own state and timestamp. The company lead-stages setting selects the underlying stage source for both reading and writing; it is not a read-only permission.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[LeadStage]]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"leads/{encode_path_param(id)}/stages",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[LeadStage],
                    parse_obj_as(
                        type_=typing.List[LeadStage],
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

    def patch_leads_id_stages_v3(
        self,
        id: str,
        *,
        company_id: str,
        school_id: str,
        request: UpdateLeadStagesRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[LeadStage]]:
        """
        Requires school_id assigned to the session and at least one non-null boolean stage. Unknown properties return 400. Stages are written in the documented schema order. Each stage is a separate write: a later failure returns 404/500 and earlier stages may remain applied; an error response does not include a partial stage list. On success the current stages are read back.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        request : UpdateLeadStagesRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[LeadStage]]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"leads/{encode_path_param(id)}/stages",
            method="PATCH",
            params={
                "company_id": company_id,
                "school_id": school_id,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=UpdateLeadStagesRequest, direction="write"
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
                    typing.List[LeadStage],
                    parse_obj_as(
                        type_=typing.List[LeadStage],
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
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
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

    def patch_leads_intended_start_date_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        updates: typing.Sequence[IntendedStartDateUpdate],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateIntendedStartDatesResponse]:
        """
        Requires school_id assigned to the session. At most 200 lead IDs are accepted across all update groups, and duplicates anywhere in the request return 400. Dates must be future YYYY-MM-DD values or TBD. Leads with a CRM/Procare expected start date are not overwritten and are reported in lead_ids_not_updated. Missing lead IDs and leads without raw records are omitted. Per-lead write failures are reported with HTTP 200 in lead_ids_not_updated; a group lookup failure returns 500 after any earlier groups may have been applied.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        updates : typing.Sequence[IntendedStartDateUpdate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateIntendedStartDatesResponse]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "leads/intended_start_date",
            method="PATCH",
            params={
                "company_id": company_id,
                "school_id": school_id,
            },
            json={
                "updates": convert_and_respect_annotation_metadata(
                    object_=updates, annotation=typing.Sequence[IntendedStartDateUpdate], direction="write"
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
                    UpdateIntendedStartDatesResponse,
                    parse_obj_as(
                        type_=UpdateIntendedStartDatesResponse,
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
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
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


class AsyncRawLeadsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_leads_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        view: typing.Optional[GetLeadsV3RequestView] = None,
        fields: typing.Optional[
            typing.Union[GetLeadsV3RequestFieldsItem, typing.Sequence[GetLeadsV3RequestFieldsItem]]
        ] = None,
        ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        query: typing.Optional[str] = None,
        max_results: typing.Optional[int] = None,
        status: typing.Optional[GetLeadsV3RequestStatus] = None,
        date_from: typing.Optional[dt.date] = None,
        date_to: typing.Optional[dt.date] = None,
        age_min: typing.Optional[float] = None,
        age_max: typing.Optional[float] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetLeadsV3Response]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns paginated lead rows, or paginated LeadStages objects when view=stages.

        Normal lookup precedence is ids, then query, then the filtered school collection. ids is limited to 200 UUIDs and missing IDs are omitted. query performs a name search with optional max_results. status, date_from/date_to and age_min/age_max are validated before these branches but only filter the normal school collection; ids and query bypass those filters. Negative ages are accepted for expected children. The age interval defaults to -12 through 180 months. date_to cannot precede date_from, and age_max cannot be smaller than age_min.

        view=stages requires the school in the session assignments and accepts only company_id, school_id, view, page and per_page. Any other parameter in this view returns 400.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        view : typing.Optional[GetLeadsV3RequestView]
            Omit for lead rows; stages includes per-stage timestamps.

        fields : typing.Optional[typing.Union[GetLeadsV3RequestFieldsItem, typing.Sequence[GetLeadsV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400. Normal lead representation only; names are case-sensitive. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Read at most 200 lead UUIDs; takes precedence over query. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        query : typing.Optional[str]
            Name search; used only when ids is omitted.

        max_results : typing.Optional[int]
            Maximum name-search results; 0 keeps the backend default.

        status : typing.Optional[GetLeadsV3RequestStatus]
            Procare lead status; exact case required. Applies only to normal school collection.

        date_from : typing.Optional[dt.date]
            Inclusive start date in YYYY-MM-DD. Optional created-date window for the normal school collection.

        date_to : typing.Optional[dt.date]
            Inclusive end date in YYYY-MM-DD. Optional created-date window for the normal school collection.

        age_min : typing.Optional[float]
            Minimum child age in months; normal school collection only.

        age_max : typing.Optional[float]
            Maximum child age in months; normal school collection only.

        page : typing.Optional[int]
            One-based page number.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetLeadsV3Response]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "leads",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "view": view,
                "fields": fields,
                "ids": ids,
                "query": query,
                "max_results": max_results,
                "status": status,
                "date_from": str(date_from) if date_from is not None else None,
                "date_to": str(date_to) if date_to is not None else None,
                "age_min": age_min,
                "age_max": age_max,
                "page": page,
                "per_page": per_page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLeadsV3Response,
                    parse_obj_as(
                        type_=GetLeadsV3Response,
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

    async def patch_leads_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        request: typing.Sequence[BulkLeadStagesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[LeadStages]]:
        """
        Requires school_id assigned to the session. The body is an array of 1 to 200 items, each with lead_id and at least one non-null stage. All items are validated before writes. Missing leads are omitted from the response. Repeated lead IDs are allowed; each appears once in the response in first-occurrence order with its final stages. The batch is not atomic: a database failure returns 500 and stops processing after any earlier writes.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        request : typing.Sequence[BulkLeadStagesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[LeadStages]]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "leads",
            method="PATCH",
            params={
                "company_id": company_id,
                "school_id": school_id,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[BulkLeadStagesItem], direction="write"
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
                    typing.List[LeadStages],
                    parse_obj_as(
                        type_=typing.List[LeadStages],
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
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
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

    async def get_leads_id_v3(
        self,
        id: str,
        *,
        company_id: str,
        school_id: str,
        fields: typing.Optional[
            typing.Union[GetLeadsIdV3RequestFieldsItem, typing.Sequence[GetLeadsIdV3RequestFieldsItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetLeadsIdV3Response]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Requires school_id. fields selects properties from the lead projection; unknown fields return 400. Returns 404 when the scoped lead does not exist.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        fields : typing.Optional[typing.Union[GetLeadsIdV3RequestFieldsItem, typing.Sequence[GetLeadsIdV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400.  Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetLeadsIdV3Response]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"leads/{encode_path_param(id)}",
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
                    GetLeadsIdV3Response,
                    parse_obj_as(
                        type_=GetLeadsIdV3Response,
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

    async def get_leads_id_stages_v3(
        self, id: str, *, company_id: str, school_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[LeadStage]]:
        """
        Requires school_id assigned to the session. Each stage includes its own state and timestamp. The company lead-stages setting selects the underlying stage source for both reading and writing; it is not a read-only permission.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[LeadStage]]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"leads/{encode_path_param(id)}/stages",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[LeadStage],
                    parse_obj_as(
                        type_=typing.List[LeadStage],
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

    async def patch_leads_id_stages_v3(
        self,
        id: str,
        *,
        company_id: str,
        school_id: str,
        request: UpdateLeadStagesRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[LeadStage]]:
        """
        Requires school_id assigned to the session and at least one non-null boolean stage. Unknown properties return 400. Stages are written in the documented schema order. Each stage is a separate write: a later failure returns 404/500 and earlier stages may remain applied; an error response does not include a partial stage list. On success the current stages are read back.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        request : UpdateLeadStagesRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[LeadStage]]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"leads/{encode_path_param(id)}/stages",
            method="PATCH",
            params={
                "company_id": company_id,
                "school_id": school_id,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=UpdateLeadStagesRequest, direction="write"
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
                    typing.List[LeadStage],
                    parse_obj_as(
                        type_=typing.List[LeadStage],
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
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
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

    async def patch_leads_intended_start_date_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        updates: typing.Sequence[IntendedStartDateUpdate],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateIntendedStartDatesResponse]:
        """
        Requires school_id assigned to the session. At most 200 lead IDs are accepted across all update groups, and duplicates anywhere in the request return 400. Dates must be future YYYY-MM-DD values or TBD. Leads with a CRM/Procare expected start date are not overwritten and are reported in lead_ids_not_updated. Missing lead IDs and leads without raw records are omitted. Per-lead write failures are reported with HTTP 200 in lead_ids_not_updated; a group lookup failure returns 500 after any earlier groups may have been applied.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        updates : typing.Sequence[IntendedStartDateUpdate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateIntendedStartDatesResponse]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "leads/intended_start_date",
            method="PATCH",
            params={
                "company_id": company_id,
                "school_id": school_id,
            },
            json={
                "updates": convert_and_respect_annotation_metadata(
                    object_=updates, annotation=typing.Sequence[IntendedStartDateUpdate], direction="write"
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
                    UpdateIntendedStartDatesResponse,
                    parse_obj_as(
                        type_=UpdateIntendedStartDatesResponse,
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
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
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
