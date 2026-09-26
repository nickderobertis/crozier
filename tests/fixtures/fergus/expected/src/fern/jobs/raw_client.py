

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
from ..types.add_quote_response import AddQuoteResponse
from ..types.get_quote_by_id_quote_response import GetQuoteByIdQuoteResponse
from ..types.get_quotes_response import GetQuotesResponse
from ..types.job_financial_summary_response import JobFinancialSummaryResponse
from ..types.job_phase_response import JobPhaseResponse
from ..types.job_phases_response import JobPhasesResponse
from ..types.job_response import JobResponse
from ..types.jobs_response import JobsResponse
from ..types.update_quote_response import UpdateQuoteResponse
from .types.get_jobs_job_id_quotes_request_filter_status import GetJobsJobIdQuotesRequestFilterStatus
from .types.get_jobs_job_id_quotes_request_sort_field import GetJobsJobIdQuotesRequestSortField
from .types.get_jobs_job_id_quotes_request_sort_order import GetJobsJobIdQuotesRequestSortOrder
from .types.get_jobs_request_filter_job_status import GetJobsRequestFilterJobStatus
from .types.get_jobs_request_filter_job_type import GetJobsRequestFilterJobType
from .types.get_jobs_request_sort_field import GetJobsRequestSortField
from .types.get_jobs_request_sort_order import GetJobsRequestSortOrder
from .types.post_jobs_job_id_quotes_request_sections_item import PostJobsJobIdQuotesRequestSectionsItem
from .types.post_jobs_request_job_type import PostJobsRequestJobType
from .types.put_jobs_job_id_quotes_quote_id_request_sections_item import PutJobsJobIdQuotesQuoteIdRequestSectionsItem
from .types.put_jobs_job_id_quotes_version_version_number_request_sections_item import (
    PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItem,
)
from .types.put_jobs_job_id_request_body import PutJobsJobIdRequestBody
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawJobsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_jobs(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetJobsRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        filter_job_no: typing.Optional[str] = None,
        filter_job_status: typing.Optional[GetJobsRequestFilterJobStatus] = None,
        filter_job_type: typing.Optional[GetJobsRequestFilterJobType] = None,
        filter_customer_id: typing.Optional[float] = None,
        filter_site_id: typing.Optional[float] = None,
        sort_field: typing.Optional[GetJobsRequestSortField] = None,
        filter_show_on_hold: typing.Optional[bool] = None,
        filter_show_archived: typing.Optional[bool] = None,
        filter_search_text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JobsResponse]:
        """
        Returns a list of jobs. The list can be filtered by job type.

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetJobsRequestSortOrder]

        page_cursor : typing.Optional[str]

        filter_job_no : typing.Optional[str]

        filter_job_status : typing.Optional[GetJobsRequestFilterJobStatus]

        filter_job_type : typing.Optional[GetJobsRequestFilterJobType]

        filter_customer_id : typing.Optional[float]

        filter_site_id : typing.Optional[float]

        sort_field : typing.Optional[GetJobsRequestSortField]

        filter_show_on_hold : typing.Optional[bool]

        filter_show_archived : typing.Optional[bool]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `description`
            - `longDescription`
            - `jobNo`
            - `customer.customerFullName`
            - `siteAddress.name`
            - `siteAddress.firstName`
            - `siteAddress.lastName`
            - `mainContact.firstName`
            - `mainContact.lastName`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JobsResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "jobs",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "filterJobNo": filter_job_no,
                "filterJobStatus": filter_job_status,
                "filterJobType": filter_job_type,
                "filterCustomerId": filter_customer_id,
                "filterSiteId": filter_site_id,
                "sortField": sort_field,
                "filterShowOnHold": filter_show_on_hold,
                "filterShowArchived": filter_show_archived,
                "filterSearchText": filter_search_text,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobsResponse,
                    parse_obj_as(
                        type_=JobsResponse,
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

    def post_jobs(
        self,
        *,
        job_type: PostJobsRequestJobType,
        title: str,
        is_draft: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        customer_id: typing.Optional[float] = OMIT,
        customer_reference: typing.Optional[str] = OMIT,
        site_id: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JobResponse]:
        """
        Create a new job

        Parameters
        ----------
        job_type : PostJobsRequestJobType

        title : str

        is_draft : typing.Optional[bool]

        description : typing.Optional[str]

        customer_id : typing.Optional[float]

        customer_reference : typing.Optional[str]

        site_id : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JobResponse]
            Resource created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "jobs",
            method="POST",
            json={
                "isDraft": is_draft,
                "jobType": job_type,
                "title": title,
                "description": description,
                "customerId": customer_id,
                "customerReference": customer_reference,
                "siteId": site_id,
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
                    JobResponse,
                    parse_obj_as(
                        type_=JobResponse,
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

    def get_jobs_job_id(
        self, job_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JobResponse]:
        """
        Returns a job by id

        Parameters
        ----------
        job_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JobResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobResponse,
                    parse_obj_as(
                        type_=JobResponse,
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

    def put_jobs_job_id(
        self,
        job_id: float,
        *,
        request: PutJobsJobIdRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JobResponse]:
        """
        Updates a draft job

        Parameters
        ----------
        job_id : float

        request : PutJobsJobIdRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JobResponse]
            Resource created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PutJobsJobIdRequestBody, direction="write"
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
                    JobResponse,
                    parse_obj_as(
                        type_=JobResponse,
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

    def put_jobs_job_id_finalise(
        self, job_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JobResponse]:
        """
        Finalise a draft job.

        Parameters
        ----------
        job_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JobResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}/finalise",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobResponse,
                    parse_obj_as(
                        type_=JobResponse,
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

    def get_jobs_job_id_phases(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JobPhasesResponse]:
        """
        Returns a list of job phases

        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JobPhasesResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}/phases",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobPhasesResponse,
                    parse_obj_as(
                        type_=JobPhasesResponse,
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

    def post_jobs_job_id_phases(
        self, job_id: str, *, title: str, description: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JobPhaseResponse]:
        """
        Creates a job phase

        Parameters
        ----------
        job_id : str

        title : str

        description : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JobPhaseResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}/phases",
            method="POST",
            json={
                "title": title,
                "description": description,
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
                    JobPhaseResponse,
                    parse_obj_as(
                        type_=JobPhaseResponse,
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

    def get_jobs_job_id_phases_job_phase_id(
        self, job_id: str, job_phase_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JobPhaseResponse]:
        """
        Returns a job phase

        Parameters
        ----------
        job_id : str

        job_phase_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JobPhaseResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}/phases/{encode_path_param(job_phase_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobPhaseResponse,
                    parse_obj_as(
                        type_=JobPhaseResponse,
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

    def put_jobs_job_id_phases_job_phase_id(
        self,
        job_id: str,
        job_phase_id: str,
        *,
        title: str,
        description: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JobPhaseResponse]:
        """
        Creates a job phase

        Parameters
        ----------
        job_id : str

        job_phase_id : str

        title : str

        description : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JobPhaseResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}/phases/{encode_path_param(job_phase_id)}",
            method="PUT",
            json={
                "title": title,
                "description": description,
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
                    JobPhaseResponse,
                    parse_obj_as(
                        type_=JobPhaseResponse,
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

    def post_jobs_job_id_phases_job_phase_id_void(
        self, job_id: float, job_phase_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Void a job phase by JobId and Job PhaseId

        Parameters
        ----------
        job_id : float

        job_phase_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}/phases/{encode_path_param(job_phase_id)}/void",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_jobs_job_id_financial_summary(
        self, job_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JobFinancialSummaryResponse]:
        """
        Get a job financial summary

        Parameters
        ----------
        job_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JobFinancialSummaryResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}/financialSummary",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobFinancialSummaryResponse,
                    parse_obj_as(
                        type_=JobFinancialSummaryResponse,
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

    def get_jobs_job_id_phases_job_phase_id_financial_summary(
        self, job_id: float, job_phase_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JobFinancialSummaryResponse]:
        """
        Get a job phase financial summary

        Parameters
        ----------
        job_id : float

        job_phase_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JobFinancialSummaryResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}/phases/{encode_path_param(job_phase_id)}/financialSummary",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobFinancialSummaryResponse,
                    parse_obj_as(
                        type_=JobFinancialSummaryResponse,
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

    def get_jobs_job_id_quotes(
        self,
        job_id: str,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetJobsJobIdQuotesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        include_combined_item_parents: typing.Optional[bool] = None,
        filter_status: typing.Optional[GetJobsJobIdQuotesRequestFilterStatus] = None,
        sort_field: typing.Optional[GetJobsJobIdQuotesRequestSortField] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetQuotesResponse]:
        """
        Get all quotes for a job

        Parameters
        ----------
        job_id : str

        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetJobsJobIdQuotesRequestSortOrder]

        page_cursor : typing.Optional[str]

        include_combined_item_parents : typing.Optional[bool]

        filter_status : typing.Optional[GetJobsJobIdQuotesRequestFilterStatus]

        sort_field : typing.Optional[GetJobsJobIdQuotesRequestSortField]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetQuotesResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}/quotes",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "includeCombinedItemParents": include_combined_item_parents,
                "filterStatus": filter_status,
                "sortField": sort_field,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetQuotesResponse,
                    parse_obj_as(
                        type_=GetQuotesResponse,
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

    def post_jobs_job_id_quotes(
        self,
        job_id: str,
        *,
        title: str,
        due_days: float,
        sections: typing.Sequence[PostJobsJobIdQuotesRequestSectionsItem],
        description: typing.Optional[str] = OMIT,
        version_number: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AddQuoteResponse]:
        """
        Create a new quote

        Parameters
        ----------
        job_id : str

        title : str

        due_days : float

        sections : typing.Sequence[PostJobsJobIdQuotesRequestSectionsItem]

        description : typing.Optional[str]

        version_number : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AddQuoteResponse]
            Resource created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}/quotes",
            method="POST",
            json={
                "title": title,
                "description": description,
                "dueDays": due_days,
                "versionNumber": version_number,
                "sections": convert_and_respect_annotation_metadata(
                    object_=sections,
                    annotation=typing.Sequence[PostJobsJobIdQuotesRequestSectionsItem],
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
                    AddQuoteResponse,
                    parse_obj_as(
                        type_=AddQuoteResponse,
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

    def get_jobs_job_id_quotes_quote_id(
        self, job_id: float, quote_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetQuoteByIdQuoteResponse]:
        """
        Get a quote

        Parameters
        ----------
        job_id : float

        quote_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetQuoteByIdQuoteResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}/quotes/{encode_path_param(quote_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetQuoteByIdQuoteResponse,
                    parse_obj_as(
                        type_=GetQuoteByIdQuoteResponse,
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

    def put_jobs_job_id_quotes_quote_id(
        self,
        job_id: float,
        quote_id: float,
        *,
        sections: typing.Sequence[PutJobsJobIdQuotesQuoteIdRequestSectionsItem],
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateQuoteResponse]:
        """
        Update a quote by ID

        Parameters
        ----------
        job_id : float

        quote_id : float

        sections : typing.Sequence[PutJobsJobIdQuotesQuoteIdRequestSectionsItem]

        title : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateQuoteResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}/quotes/{encode_path_param(quote_id)}",
            method="PUT",
            json={
                "title": title,
                "description": description,
                "sections": convert_and_respect_annotation_metadata(
                    object_=sections,
                    annotation=typing.Sequence[PutJobsJobIdQuotesQuoteIdRequestSectionsItem],
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
                    UpdateQuoteResponse,
                    parse_obj_as(
                        type_=UpdateQuoteResponse,
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

    def put_jobs_job_id_quotes_version_version_number(
        self,
        job_id: float,
        version_number: float,
        *,
        sections: typing.Sequence[PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItem],
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateQuoteResponse]:
        """
        Update a quote by version number

        Parameters
        ----------
        job_id : float

        version_number : float

        sections : typing.Sequence[PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItem]

        title : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateQuoteResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}/quotes/version/{encode_path_param(version_number)}",
            method="PUT",
            json={
                "title": title,
                "description": description,
                "sections": convert_and_respect_annotation_metadata(
                    object_=sections,
                    annotation=typing.Sequence[PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItem],
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
                    UpdateQuoteResponse,
                    parse_obj_as(
                        type_=UpdateQuoteResponse,
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


class AsyncRawJobsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_jobs(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetJobsRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        filter_job_no: typing.Optional[str] = None,
        filter_job_status: typing.Optional[GetJobsRequestFilterJobStatus] = None,
        filter_job_type: typing.Optional[GetJobsRequestFilterJobType] = None,
        filter_customer_id: typing.Optional[float] = None,
        filter_site_id: typing.Optional[float] = None,
        sort_field: typing.Optional[GetJobsRequestSortField] = None,
        filter_show_on_hold: typing.Optional[bool] = None,
        filter_show_archived: typing.Optional[bool] = None,
        filter_search_text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JobsResponse]:
        """
        Returns a list of jobs. The list can be filtered by job type.

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetJobsRequestSortOrder]

        page_cursor : typing.Optional[str]

        filter_job_no : typing.Optional[str]

        filter_job_status : typing.Optional[GetJobsRequestFilterJobStatus]

        filter_job_type : typing.Optional[GetJobsRequestFilterJobType]

        filter_customer_id : typing.Optional[float]

        filter_site_id : typing.Optional[float]

        sort_field : typing.Optional[GetJobsRequestSortField]

        filter_show_on_hold : typing.Optional[bool]

        filter_show_archived : typing.Optional[bool]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `description`
            - `longDescription`
            - `jobNo`
            - `customer.customerFullName`
            - `siteAddress.name`
            - `siteAddress.firstName`
            - `siteAddress.lastName`
            - `mainContact.firstName`
            - `mainContact.lastName`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JobsResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "jobs",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "filterJobNo": filter_job_no,
                "filterJobStatus": filter_job_status,
                "filterJobType": filter_job_type,
                "filterCustomerId": filter_customer_id,
                "filterSiteId": filter_site_id,
                "sortField": sort_field,
                "filterShowOnHold": filter_show_on_hold,
                "filterShowArchived": filter_show_archived,
                "filterSearchText": filter_search_text,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobsResponse,
                    parse_obj_as(
                        type_=JobsResponse,
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

    async def post_jobs(
        self,
        *,
        job_type: PostJobsRequestJobType,
        title: str,
        is_draft: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        customer_id: typing.Optional[float] = OMIT,
        customer_reference: typing.Optional[str] = OMIT,
        site_id: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JobResponse]:
        """
        Create a new job

        Parameters
        ----------
        job_type : PostJobsRequestJobType

        title : str

        is_draft : typing.Optional[bool]

        description : typing.Optional[str]

        customer_id : typing.Optional[float]

        customer_reference : typing.Optional[str]

        site_id : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JobResponse]
            Resource created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "jobs",
            method="POST",
            json={
                "isDraft": is_draft,
                "jobType": job_type,
                "title": title,
                "description": description,
                "customerId": customer_id,
                "customerReference": customer_reference,
                "siteId": site_id,
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
                    JobResponse,
                    parse_obj_as(
                        type_=JobResponse,
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

    async def get_jobs_job_id(
        self, job_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JobResponse]:
        """
        Returns a job by id

        Parameters
        ----------
        job_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JobResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobResponse,
                    parse_obj_as(
                        type_=JobResponse,
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

    async def put_jobs_job_id(
        self,
        job_id: float,
        *,
        request: PutJobsJobIdRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JobResponse]:
        """
        Updates a draft job

        Parameters
        ----------
        job_id : float

        request : PutJobsJobIdRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JobResponse]
            Resource created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PutJobsJobIdRequestBody, direction="write"
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
                    JobResponse,
                    parse_obj_as(
                        type_=JobResponse,
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

    async def put_jobs_job_id_finalise(
        self, job_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JobResponse]:
        """
        Finalise a draft job.

        Parameters
        ----------
        job_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JobResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}/finalise",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobResponse,
                    parse_obj_as(
                        type_=JobResponse,
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

    async def get_jobs_job_id_phases(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JobPhasesResponse]:
        """
        Returns a list of job phases

        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JobPhasesResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}/phases",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobPhasesResponse,
                    parse_obj_as(
                        type_=JobPhasesResponse,
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

    async def post_jobs_job_id_phases(
        self, job_id: str, *, title: str, description: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JobPhaseResponse]:
        """
        Creates a job phase

        Parameters
        ----------
        job_id : str

        title : str

        description : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JobPhaseResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}/phases",
            method="POST",
            json={
                "title": title,
                "description": description,
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
                    JobPhaseResponse,
                    parse_obj_as(
                        type_=JobPhaseResponse,
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

    async def get_jobs_job_id_phases_job_phase_id(
        self, job_id: str, job_phase_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JobPhaseResponse]:
        """
        Returns a job phase

        Parameters
        ----------
        job_id : str

        job_phase_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JobPhaseResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}/phases/{encode_path_param(job_phase_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobPhaseResponse,
                    parse_obj_as(
                        type_=JobPhaseResponse,
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

    async def put_jobs_job_id_phases_job_phase_id(
        self,
        job_id: str,
        job_phase_id: str,
        *,
        title: str,
        description: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JobPhaseResponse]:
        """
        Creates a job phase

        Parameters
        ----------
        job_id : str

        job_phase_id : str

        title : str

        description : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JobPhaseResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}/phases/{encode_path_param(job_phase_id)}",
            method="PUT",
            json={
                "title": title,
                "description": description,
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
                    JobPhaseResponse,
                    parse_obj_as(
                        type_=JobPhaseResponse,
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

    async def post_jobs_job_id_phases_job_phase_id_void(
        self, job_id: float, job_phase_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Void a job phase by JobId and Job PhaseId

        Parameters
        ----------
        job_id : float

        job_phase_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}/phases/{encode_path_param(job_phase_id)}/void",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_jobs_job_id_financial_summary(
        self, job_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JobFinancialSummaryResponse]:
        """
        Get a job financial summary

        Parameters
        ----------
        job_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JobFinancialSummaryResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}/financialSummary",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobFinancialSummaryResponse,
                    parse_obj_as(
                        type_=JobFinancialSummaryResponse,
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

    async def get_jobs_job_id_phases_job_phase_id_financial_summary(
        self, job_id: float, job_phase_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JobFinancialSummaryResponse]:
        """
        Get a job phase financial summary

        Parameters
        ----------
        job_id : float

        job_phase_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JobFinancialSummaryResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}/phases/{encode_path_param(job_phase_id)}/financialSummary",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobFinancialSummaryResponse,
                    parse_obj_as(
                        type_=JobFinancialSummaryResponse,
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

    async def get_jobs_job_id_quotes(
        self,
        job_id: str,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetJobsJobIdQuotesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        include_combined_item_parents: typing.Optional[bool] = None,
        filter_status: typing.Optional[GetJobsJobIdQuotesRequestFilterStatus] = None,
        sort_field: typing.Optional[GetJobsJobIdQuotesRequestSortField] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetQuotesResponse]:
        """
        Get all quotes for a job

        Parameters
        ----------
        job_id : str

        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetJobsJobIdQuotesRequestSortOrder]

        page_cursor : typing.Optional[str]

        include_combined_item_parents : typing.Optional[bool]

        filter_status : typing.Optional[GetJobsJobIdQuotesRequestFilterStatus]

        sort_field : typing.Optional[GetJobsJobIdQuotesRequestSortField]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetQuotesResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}/quotes",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "includeCombinedItemParents": include_combined_item_parents,
                "filterStatus": filter_status,
                "sortField": sort_field,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetQuotesResponse,
                    parse_obj_as(
                        type_=GetQuotesResponse,
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

    async def post_jobs_job_id_quotes(
        self,
        job_id: str,
        *,
        title: str,
        due_days: float,
        sections: typing.Sequence[PostJobsJobIdQuotesRequestSectionsItem],
        description: typing.Optional[str] = OMIT,
        version_number: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AddQuoteResponse]:
        """
        Create a new quote

        Parameters
        ----------
        job_id : str

        title : str

        due_days : float

        sections : typing.Sequence[PostJobsJobIdQuotesRequestSectionsItem]

        description : typing.Optional[str]

        version_number : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AddQuoteResponse]
            Resource created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}/quotes",
            method="POST",
            json={
                "title": title,
                "description": description,
                "dueDays": due_days,
                "versionNumber": version_number,
                "sections": convert_and_respect_annotation_metadata(
                    object_=sections,
                    annotation=typing.Sequence[PostJobsJobIdQuotesRequestSectionsItem],
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
                    AddQuoteResponse,
                    parse_obj_as(
                        type_=AddQuoteResponse,
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

    async def get_jobs_job_id_quotes_quote_id(
        self, job_id: float, quote_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetQuoteByIdQuoteResponse]:
        """
        Get a quote

        Parameters
        ----------
        job_id : float

        quote_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetQuoteByIdQuoteResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}/quotes/{encode_path_param(quote_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetQuoteByIdQuoteResponse,
                    parse_obj_as(
                        type_=GetQuoteByIdQuoteResponse,
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

    async def put_jobs_job_id_quotes_quote_id(
        self,
        job_id: float,
        quote_id: float,
        *,
        sections: typing.Sequence[PutJobsJobIdQuotesQuoteIdRequestSectionsItem],
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateQuoteResponse]:
        """
        Update a quote by ID

        Parameters
        ----------
        job_id : float

        quote_id : float

        sections : typing.Sequence[PutJobsJobIdQuotesQuoteIdRequestSectionsItem]

        title : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateQuoteResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}/quotes/{encode_path_param(quote_id)}",
            method="PUT",
            json={
                "title": title,
                "description": description,
                "sections": convert_and_respect_annotation_metadata(
                    object_=sections,
                    annotation=typing.Sequence[PutJobsJobIdQuotesQuoteIdRequestSectionsItem],
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
                    UpdateQuoteResponse,
                    parse_obj_as(
                        type_=UpdateQuoteResponse,
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

    async def put_jobs_job_id_quotes_version_version_number(
        self,
        job_id: float,
        version_number: float,
        *,
        sections: typing.Sequence[PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItem],
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateQuoteResponse]:
        """
        Update a quote by version number

        Parameters
        ----------
        job_id : float

        version_number : float

        sections : typing.Sequence[PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItem]

        title : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateQuoteResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(job_id)}/quotes/version/{encode_path_param(version_number)}",
            method="PUT",
            json={
                "title": title,
                "description": description,
                "sections": convert_and_respect_annotation_metadata(
                    object_=sections,
                    annotation=typing.Sequence[PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItem],
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
                    UpdateQuoteResponse,
                    parse_obj_as(
                        type_=UpdateQuoteResponse,
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
