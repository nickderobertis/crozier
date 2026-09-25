

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.accept_quote_response import AcceptQuoteResponse
from ..types.get_quote_by_id_quote_response import GetQuoteByIdQuoteResponse
from ..types.get_standalone_quotes_response import GetStandaloneQuotesResponse
from ..types.quote_totals_response import QuoteTotalsResponse
from .types.get_jobs_quotes_request_filter_status import GetJobsQuotesRequestFilterStatus
from .types.get_jobs_quotes_request_sort_field import GetJobsQuotesRequestSortField
from .types.get_jobs_quotes_request_sort_order import GetJobsQuotesRequestSortOrder
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawJobsQuotesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_jobs_quotes(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetJobsQuotesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        filter_status: typing.Optional[GetJobsQuotesRequestFilterStatus] = None,
        sort_field: typing.Optional[GetJobsQuotesRequestSortField] = None,
        created_after: typing.Optional[dt.datetime] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetStandaloneQuotesResponse]:
        """
        Returns a list of all quotes from across all jobs, sorted by created date and last modified date.

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetJobsQuotesRequestSortOrder]

        page_cursor : typing.Optional[str]

        filter_status : typing.Optional[GetJobsQuotesRequestFilterStatus]

        sort_field : typing.Optional[GetJobsQuotesRequestSortField]

        created_after : typing.Optional[dt.datetime]
            Get quote created after certain time. Overrides sortField and sortOrder

        modified_after : typing.Optional[dt.datetime]
            Get quote modified after certain time. Overrides sortField and sortOrder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetStandaloneQuotesResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "jobs/quotes",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "filterStatus": filter_status,
                "sortField": sort_field,
                "createdAfter": serialize_datetime(created_after) if created_after is not None else None,
                "modifiedAfter": serialize_datetime(modified_after) if modified_after is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetStandaloneQuotesResponse,
                    parse_obj_as(
                        type_=GetStandaloneQuotesResponse,
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

    def get_jobs_quotes_quote_id(
        self, quote_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetQuoteByIdQuoteResponse]:
        """
        Returns a specific quote by ID from across all jobs.

        Parameters
        ----------
        quote_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetQuoteByIdQuoteResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/quotes/{encode_path_param(quote_id)}",
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

    def get_jobs_quotes_guid_guid(
        self,
        guid: str,
        *,
        include_combined_item_parents: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetQuoteByIdQuoteResponse]:
        """
        Returns a specific quote by GUID with full details.

        Parameters
        ----------
        guid : str

        include_combined_item_parents : typing.Optional[bool]
            Include the parents of combined line item in the `lineItems` list (default: false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetQuoteByIdQuoteResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/quotes/guid/{encode_path_param(guid)}",
            method="GET",
            params={
                "includeCombinedItemParents": include_combined_item_parents,
            },
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

    def post_jobs_quotes_quote_id_publish(
        self,
        quote_id: str,
        *,
        published_at: typing.Optional[dt.datetime] = OMIT,
        published_by: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Publishes a quote.

        Parameters
        ----------
        quote_id : str

        published_at : typing.Optional[dt.datetime]

        published_by : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/quotes/{encode_path_param(quote_id)}/publish",
            method="POST",
            json={
                "publishedAt": published_at,
                "publishedBy": published_by,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    def post_jobs_quotes_quote_id_mark_as_sent(
        self,
        quote_id: str,
        *,
        is_sent: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Marks a quote as sent.

        Parameters
        ----------
        quote_id : str

        is_sent : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/quotes/{encode_path_param(quote_id)}/markAsSent",
            method="POST",
            json={
                "isSent": is_sent,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    def post_jobs_quotes_quote_id_accept(
        self,
        quote_id: str,
        *,
        accepted_by: str,
        accepted_at: typing.Optional[dt.datetime] = OMIT,
        selected_section_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[AcceptQuoteResponse]]:
        """
        Accepts a quote.

        Parameters
        ----------
        quote_id : str

        accepted_by : str
            The name or employee GUID of the person accepting the quote

        accepted_at : typing.Optional[dt.datetime]

        selected_section_ids : typing.Optional[typing.Sequence[int]]
            The IDs of the sections that the customer has accepted. Required if the quote has optional or multi-select sections.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[AcceptQuoteResponse]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/quotes/{encode_path_param(quote_id)}/accept",
            method="POST",
            json={
                "acceptedBy": accepted_by,
                "acceptedAt": accepted_at,
                "selectedSectionIds": selected_section_ids,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[AcceptQuoteResponse],
                    parse_obj_as(
                        type_=typing.Optional[AcceptQuoteResponse],
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

    def post_jobs_quotes_quote_id_decline(
        self,
        quote_id: str,
        *,
        declined_at: typing.Optional[dt.datetime] = OMIT,
        reason_notes: typing.Optional[str] = OMIT,
        rejected_by: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Declines a quote.

        Parameters
        ----------
        quote_id : str

        declined_at : typing.Optional[dt.datetime]

        reason_notes : typing.Optional[str]

        rejected_by : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/quotes/{encode_path_param(quote_id)}/decline",
            method="POST",
            json={
                "declinedAt": declined_at,
                "reasonNotes": reason_notes,
                "rejectedBy": rejected_by,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    def post_jobs_quotes_quote_id_void(
        self,
        quote_id: str,
        *,
        voided_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Voids a quote.

        Parameters
        ----------
        quote_id : str

        voided_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/quotes/{encode_path_param(quote_id)}/void",
            method="POST",
            json={
                "voidedAt": voided_at,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    def post_jobs_quotes_quote_id_totals(
        self,
        quote_id: float,
        *,
        selected_section_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[QuoteTotalsResponse]:
        """
        Get totals for a quote. Fixed sections are always included. Optionally provide optional/multiselect section IDs to include in the totals.

        Parameters
        ----------
        quote_id : float

        selected_section_ids : typing.Optional[typing.Sequence[int]]
            [] — returns totals for fixed sections only. [1, 2, 3] — returns totals for fixed sections + the provided optional/multiselect section IDs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[QuoteTotalsResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/quotes/{encode_path_param(quote_id)}/totals",
            method="POST",
            json={
                "selectedSectionIds": selected_section_ids,
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
                    QuoteTotalsResponse,
                    parse_obj_as(
                        type_=QuoteTotalsResponse,
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


class AsyncRawJobsQuotesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_jobs_quotes(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetJobsQuotesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        filter_status: typing.Optional[GetJobsQuotesRequestFilterStatus] = None,
        sort_field: typing.Optional[GetJobsQuotesRequestSortField] = None,
        created_after: typing.Optional[dt.datetime] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetStandaloneQuotesResponse]:
        """
        Returns a list of all quotes from across all jobs, sorted by created date and last modified date.

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetJobsQuotesRequestSortOrder]

        page_cursor : typing.Optional[str]

        filter_status : typing.Optional[GetJobsQuotesRequestFilterStatus]

        sort_field : typing.Optional[GetJobsQuotesRequestSortField]

        created_after : typing.Optional[dt.datetime]
            Get quote created after certain time. Overrides sortField and sortOrder

        modified_after : typing.Optional[dt.datetime]
            Get quote modified after certain time. Overrides sortField and sortOrder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetStandaloneQuotesResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "jobs/quotes",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "filterStatus": filter_status,
                "sortField": sort_field,
                "createdAfter": serialize_datetime(created_after) if created_after is not None else None,
                "modifiedAfter": serialize_datetime(modified_after) if modified_after is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetStandaloneQuotesResponse,
                    parse_obj_as(
                        type_=GetStandaloneQuotesResponse,
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

    async def get_jobs_quotes_quote_id(
        self, quote_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetQuoteByIdQuoteResponse]:
        """
        Returns a specific quote by ID from across all jobs.

        Parameters
        ----------
        quote_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetQuoteByIdQuoteResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/quotes/{encode_path_param(quote_id)}",
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

    async def get_jobs_quotes_guid_guid(
        self,
        guid: str,
        *,
        include_combined_item_parents: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetQuoteByIdQuoteResponse]:
        """
        Returns a specific quote by GUID with full details.

        Parameters
        ----------
        guid : str

        include_combined_item_parents : typing.Optional[bool]
            Include the parents of combined line item in the `lineItems` list (default: false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetQuoteByIdQuoteResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/quotes/guid/{encode_path_param(guid)}",
            method="GET",
            params={
                "includeCombinedItemParents": include_combined_item_parents,
            },
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

    async def post_jobs_quotes_quote_id_publish(
        self,
        quote_id: str,
        *,
        published_at: typing.Optional[dt.datetime] = OMIT,
        published_by: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Publishes a quote.

        Parameters
        ----------
        quote_id : str

        published_at : typing.Optional[dt.datetime]

        published_by : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/quotes/{encode_path_param(quote_id)}/publish",
            method="POST",
            json={
                "publishedAt": published_at,
                "publishedBy": published_by,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    async def post_jobs_quotes_quote_id_mark_as_sent(
        self,
        quote_id: str,
        *,
        is_sent: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Marks a quote as sent.

        Parameters
        ----------
        quote_id : str

        is_sent : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/quotes/{encode_path_param(quote_id)}/markAsSent",
            method="POST",
            json={
                "isSent": is_sent,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    async def post_jobs_quotes_quote_id_accept(
        self,
        quote_id: str,
        *,
        accepted_by: str,
        accepted_at: typing.Optional[dt.datetime] = OMIT,
        selected_section_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[AcceptQuoteResponse]]:
        """
        Accepts a quote.

        Parameters
        ----------
        quote_id : str

        accepted_by : str
            The name or employee GUID of the person accepting the quote

        accepted_at : typing.Optional[dt.datetime]

        selected_section_ids : typing.Optional[typing.Sequence[int]]
            The IDs of the sections that the customer has accepted. Required if the quote has optional or multi-select sections.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[AcceptQuoteResponse]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/quotes/{encode_path_param(quote_id)}/accept",
            method="POST",
            json={
                "acceptedBy": accepted_by,
                "acceptedAt": accepted_at,
                "selectedSectionIds": selected_section_ids,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[AcceptQuoteResponse],
                    parse_obj_as(
                        type_=typing.Optional[AcceptQuoteResponse],
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

    async def post_jobs_quotes_quote_id_decline(
        self,
        quote_id: str,
        *,
        declined_at: typing.Optional[dt.datetime] = OMIT,
        reason_notes: typing.Optional[str] = OMIT,
        rejected_by: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Declines a quote.

        Parameters
        ----------
        quote_id : str

        declined_at : typing.Optional[dt.datetime]

        reason_notes : typing.Optional[str]

        rejected_by : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/quotes/{encode_path_param(quote_id)}/decline",
            method="POST",
            json={
                "declinedAt": declined_at,
                "reasonNotes": reason_notes,
                "rejectedBy": rejected_by,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    async def post_jobs_quotes_quote_id_void(
        self,
        quote_id: str,
        *,
        voided_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Voids a quote.

        Parameters
        ----------
        quote_id : str

        voided_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/quotes/{encode_path_param(quote_id)}/void",
            method="POST",
            json={
                "voidedAt": voided_at,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    async def post_jobs_quotes_quote_id_totals(
        self,
        quote_id: float,
        *,
        selected_section_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[QuoteTotalsResponse]:
        """
        Get totals for a quote. Fixed sections are always included. Optionally provide optional/multiselect section IDs to include in the totals.

        Parameters
        ----------
        quote_id : float

        selected_section_ids : typing.Optional[typing.Sequence[int]]
            [] — returns totals for fixed sections only. [1, 2, 3] — returns totals for fixed sections + the provided optional/multiselect section IDs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[QuoteTotalsResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/quotes/{encode_path_param(quote_id)}/totals",
            method="POST",
            json={
                "selectedSectionIds": selected_section_ids,
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
                    QuoteTotalsResponse,
                    parse_obj_as(
                        type_=QuoteTotalsResponse,
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
