

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
from ..errors.not_found_error import NotFoundError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.bad_request_response import BadRequestResponse
from ..types.create_opportunity_response import CreateOpportunityResponse
from ..types.currency import Currency
from ..types.custom_field import CustomField
from ..types.delete_opportunity_response import DeleteOpportunityResponse
from ..types.get_opportunities_response import GetOpportunitiesResponse
from ..types.get_opportunity_response import GetOpportunityResponse
from ..types.not_found_response import NotFoundResponse
from ..types.opportunities_filter import OpportunitiesFilter
from ..types.opportunities_sort import OpportunitiesSort
from ..types.payment_required_response import PaymentRequiredResponse
from ..types.tags import Tags
from ..types.unauthorized_response import UnauthorizedResponse
from ..types.unprocessable_response import UnprocessableResponse
from ..types.update_opportunity_response import UpdateOpportunityResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawOpportunitiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[OpportunitiesFilter] = None,
        sort: typing.Optional[OpportunitiesSort] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetOpportunitiesResponse]:
        """
        List opportunities

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[OpportunitiesFilter]
            Apply filters

        sort : typing.Optional[OpportunitiesSort]
            Apply sorting

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetOpportunitiesResponse]
            Opportunities
        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/opportunities",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=OpportunitiesFilter, direction="write"
                ),
                "sort": convert_and_respect_annotation_metadata(
                    object_=sort, annotation=OpportunitiesSort, direction="write"
                ),
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetOpportunitiesResponse,
                    parse_obj_as(
                        type_=GetOpportunitiesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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

    def add(
        self,
        *,
        title: str,
        raw: typing.Optional[bool] = None,
        close_date: typing.Optional[dt.date] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        contact_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        date_last_contacted: typing.Optional[dt.datetime] = OMIT,
        date_lead_created: typing.Optional[dt.datetime] = OMIT,
        date_stage_changed: typing.Optional[dt.datetime] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        expected_revenue: typing.Optional[float] = OMIT,
        id: typing.Optional[str] = OMIT,
        interaction_count: typing.Optional[float] = OMIT,
        last_activity_at: typing.Optional[str] = OMIT,
        lead_id: typing.Optional[str] = OMIT,
        lead_source: typing.Optional[str] = OMIT,
        loss_reason: typing.Optional[str] = OMIT,
        loss_reason_id: typing.Optional[str] = OMIT,
        monetary_amount: typing.Optional[float] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        pipeline_id: typing.Optional[str] = OMIT,
        pipeline_stage_id: typing.Optional[str] = OMIT,
        primary_contact_id: typing.Optional[str] = OMIT,
        priority: typing.Optional[str] = OMIT,
        source_id: typing.Optional[str] = OMIT,
        stage_last_changed_at: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[str] = OMIT,
        status_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        win_probability: typing.Optional[float] = OMIT,
        won_reason: typing.Optional[str] = OMIT,
        won_reason_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateOpportunityResponse]:
        """
        Create opportunity

        Parameters
        ----------
        title : str
            The title or name of the opportunity.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        close_date : typing.Optional[dt.date]
            The actual closing date for the opportunity. If close_date is null, the opportunity is not closed yet.

        company_id : typing.Optional[str]
            The unique identifier of the company associated with the opportunity.

        company_name : typing.Optional[str]
            The name of the company associated with the opportunity.

        contact_id : typing.Optional[str]
            The unique identifier of the contact associated with the opportunity.

        contact_ids : typing.Optional[typing.Sequence[str]]
            An array of unique identifiers of all contacts associated with the opportunity.

        created_at : typing.Optional[dt.datetime]
            The date and time when the opportunity was created.

        created_by : typing.Optional[str]
            The unique identifier of the user who created the opportunity.

        currency : typing.Optional[Currency]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        date_last_contacted : typing.Optional[dt.datetime]
            The date and time when the opportunity was last contacted.

        date_lead_created : typing.Optional[dt.datetime]
            The date and time when the lead associated with the opportunity was created.

        date_stage_changed : typing.Optional[dt.datetime]
            The date and time when the stage of the opportunity was last changed.

        deleted : typing.Optional[bool]
            Indicates whether the opportunity has been deleted.

        description : typing.Optional[str]
            A description of the opportunity.

        expected_revenue : typing.Optional[float]
            The expected revenue from the opportunity

        id : typing.Optional[str]
            A unique identifier for the opportunity.

        interaction_count : typing.Optional[float]
            The number of interactions with the opportunity.

        last_activity_at : typing.Optional[str]
            The date and time of the last activity associated with the opportunity.

        lead_id : typing.Optional[str]
            The unique identifier of the lead associated with the opportunity.

        lead_source : typing.Optional[str]
            The source of the lead associated with the opportunity.

        loss_reason : typing.Optional[str]
            The reason why the opportunity was lost.

        loss_reason_id : typing.Optional[str]
            The unique identifier of the reason why the opportunity was lost.

        monetary_amount : typing.Optional[float]
            The monetary value associated with the opportunity

        owner_id : typing.Optional[str]
            The unique identifier of the user who owns the opportunity.

        pipeline_id : typing.Optional[str]
            The unique identifier of the pipeline associated with the opportunity

        pipeline_stage_id : typing.Optional[str]
            The unique identifier of the stage in the pipeline associated with the opportunity.

        primary_contact_id : typing.Optional[str]
            The unique identifier of the primary contact associated with the opportunity.

        priority : typing.Optional[str]
            The priority level of the opportunity.

        source_id : typing.Optional[str]
            The unique identifier of the source of the opportunity.

        stage_last_changed_at : typing.Optional[dt.datetime]
            The date and time when the stage of the opportunity was last changed.

        status : typing.Optional[str]
            The current status of the opportunity.

        status_id : typing.Optional[str]
            The unique identifier of the current status of the opportunity.

        tags : typing.Optional[Tags]

        type : typing.Optional[str]
            The type of the opportunity

        updated_at : typing.Optional[dt.datetime]
            The date and time when the opportunity was last updated.

        updated_by : typing.Optional[str]
            The unique identifier of the user who last updated the opportunity.

        win_probability : typing.Optional[float]
            The probability of winning the opportunity, expressed as a percentage.

        won_reason : typing.Optional[str]
            The reason why the opportunity was won.

        won_reason_id : typing.Optional[str]
            The unique identifier of the reason why the opportunity was won.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateOpportunityResponse]
            Opportunity created
        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/opportunities",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "close_date": close_date,
                "company_id": company_id,
                "company_name": company_name,
                "contact_id": contact_id,
                "contact_ids": contact_ids,
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "custom_fields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=typing.Sequence[CustomField], direction="write"
                ),
                "date_last_contacted": date_last_contacted,
                "date_lead_created": date_lead_created,
                "date_stage_changed": date_stage_changed,
                "deleted": deleted,
                "description": description,
                "expected_revenue": expected_revenue,
                "id": id,
                "interaction_count": interaction_count,
                "last_activity_at": last_activity_at,
                "lead_id": lead_id,
                "lead_source": lead_source,
                "loss_reason": loss_reason,
                "loss_reason_id": loss_reason_id,
                "monetary_amount": monetary_amount,
                "owner_id": owner_id,
                "pipeline_id": pipeline_id,
                "pipeline_stage_id": pipeline_stage_id,
                "primary_contact_id": primary_contact_id,
                "priority": priority,
                "source_id": source_id,
                "stage_last_changed_at": stage_last_changed_at,
                "status": status,
                "status_id": status_id,
                "tags": tags,
                "title": title,
                "type": type,
                "updated_at": updated_at,
                "updated_by": updated_by,
                "win_probability": win_probability,
                "won_reason": won_reason,
                "won_reason_id": won_reason_id,
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
                    CreateOpportunityResponse,
                    parse_obj_as(
                        type_=CreateOpportunityResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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

    def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetOpportunityResponse]:
        """
        Get opportunity

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetOpportunityResponse]
            Opportunity
        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/opportunities/{encode_path_param(id)}",
            method="GET",
            params={
                "raw": raw,
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetOpportunityResponse,
                    parse_obj_as(
                        type_=GetOpportunityResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteOpportunityResponse]:
        """
        Delete opportunity

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteOpportunityResponse]
            Opportunity deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/opportunities/{encode_path_param(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteOpportunityResponse,
                    parse_obj_as(
                        type_=DeleteOpportunityResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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

    def update(
        self,
        id_: str,
        *,
        title: str,
        raw: typing.Optional[bool] = None,
        close_date: typing.Optional[dt.date] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        contact_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        date_last_contacted: typing.Optional[dt.datetime] = OMIT,
        date_lead_created: typing.Optional[dt.datetime] = OMIT,
        date_stage_changed: typing.Optional[dt.datetime] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        expected_revenue: typing.Optional[float] = OMIT,
        id: typing.Optional[str] = OMIT,
        interaction_count: typing.Optional[float] = OMIT,
        last_activity_at: typing.Optional[str] = OMIT,
        lead_id: typing.Optional[str] = OMIT,
        lead_source: typing.Optional[str] = OMIT,
        loss_reason: typing.Optional[str] = OMIT,
        loss_reason_id: typing.Optional[str] = OMIT,
        monetary_amount: typing.Optional[float] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        pipeline_id: typing.Optional[str] = OMIT,
        pipeline_stage_id: typing.Optional[str] = OMIT,
        primary_contact_id: typing.Optional[str] = OMIT,
        priority: typing.Optional[str] = OMIT,
        source_id: typing.Optional[str] = OMIT,
        stage_last_changed_at: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[str] = OMIT,
        status_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        win_probability: typing.Optional[float] = OMIT,
        won_reason: typing.Optional[str] = OMIT,
        won_reason_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateOpportunityResponse]:
        """
        Update opportunity

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        title : str
            The title or name of the opportunity.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        close_date : typing.Optional[dt.date]
            The actual closing date for the opportunity. If close_date is null, the opportunity is not closed yet.

        company_id : typing.Optional[str]
            The unique identifier of the company associated with the opportunity.

        company_name : typing.Optional[str]
            The name of the company associated with the opportunity.

        contact_id : typing.Optional[str]
            The unique identifier of the contact associated with the opportunity.

        contact_ids : typing.Optional[typing.Sequence[str]]
            An array of unique identifiers of all contacts associated with the opportunity.

        created_at : typing.Optional[dt.datetime]
            The date and time when the opportunity was created.

        created_by : typing.Optional[str]
            The unique identifier of the user who created the opportunity.

        currency : typing.Optional[Currency]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        date_last_contacted : typing.Optional[dt.datetime]
            The date and time when the opportunity was last contacted.

        date_lead_created : typing.Optional[dt.datetime]
            The date and time when the lead associated with the opportunity was created.

        date_stage_changed : typing.Optional[dt.datetime]
            The date and time when the stage of the opportunity was last changed.

        deleted : typing.Optional[bool]
            Indicates whether the opportunity has been deleted.

        description : typing.Optional[str]
            A description of the opportunity.

        expected_revenue : typing.Optional[float]
            The expected revenue from the opportunity

        id : typing.Optional[str]
            A unique identifier for the opportunity.

        interaction_count : typing.Optional[float]
            The number of interactions with the opportunity.

        last_activity_at : typing.Optional[str]
            The date and time of the last activity associated with the opportunity.

        lead_id : typing.Optional[str]
            The unique identifier of the lead associated with the opportunity.

        lead_source : typing.Optional[str]
            The source of the lead associated with the opportunity.

        loss_reason : typing.Optional[str]
            The reason why the opportunity was lost.

        loss_reason_id : typing.Optional[str]
            The unique identifier of the reason why the opportunity was lost.

        monetary_amount : typing.Optional[float]
            The monetary value associated with the opportunity

        owner_id : typing.Optional[str]
            The unique identifier of the user who owns the opportunity.

        pipeline_id : typing.Optional[str]
            The unique identifier of the pipeline associated with the opportunity

        pipeline_stage_id : typing.Optional[str]
            The unique identifier of the stage in the pipeline associated with the opportunity.

        primary_contact_id : typing.Optional[str]
            The unique identifier of the primary contact associated with the opportunity.

        priority : typing.Optional[str]
            The priority level of the opportunity.

        source_id : typing.Optional[str]
            The unique identifier of the source of the opportunity.

        stage_last_changed_at : typing.Optional[dt.datetime]
            The date and time when the stage of the opportunity was last changed.

        status : typing.Optional[str]
            The current status of the opportunity.

        status_id : typing.Optional[str]
            The unique identifier of the current status of the opportunity.

        tags : typing.Optional[Tags]

        type : typing.Optional[str]
            The type of the opportunity

        updated_at : typing.Optional[dt.datetime]
            The date and time when the opportunity was last updated.

        updated_by : typing.Optional[str]
            The unique identifier of the user who last updated the opportunity.

        win_probability : typing.Optional[float]
            The probability of winning the opportunity, expressed as a percentage.

        won_reason : typing.Optional[str]
            The reason why the opportunity was won.

        won_reason_id : typing.Optional[str]
            The unique identifier of the reason why the opportunity was won.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateOpportunityResponse]
            Opportunity updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/opportunities/{encode_path_param(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "close_date": close_date,
                "company_id": company_id,
                "company_name": company_name,
                "contact_id": contact_id,
                "contact_ids": contact_ids,
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "custom_fields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=typing.Sequence[CustomField], direction="write"
                ),
                "date_last_contacted": date_last_contacted,
                "date_lead_created": date_lead_created,
                "date_stage_changed": date_stage_changed,
                "deleted": deleted,
                "description": description,
                "expected_revenue": expected_revenue,
                "id": id,
                "interaction_count": interaction_count,
                "last_activity_at": last_activity_at,
                "lead_id": lead_id,
                "lead_source": lead_source,
                "loss_reason": loss_reason,
                "loss_reason_id": loss_reason_id,
                "monetary_amount": monetary_amount,
                "owner_id": owner_id,
                "pipeline_id": pipeline_id,
                "pipeline_stage_id": pipeline_stage_id,
                "primary_contact_id": primary_contact_id,
                "priority": priority,
                "source_id": source_id,
                "stage_last_changed_at": stage_last_changed_at,
                "status": status,
                "status_id": status_id,
                "tags": tags,
                "title": title,
                "type": type,
                "updated_at": updated_at,
                "updated_by": updated_by,
                "win_probability": win_probability,
                "won_reason": won_reason,
                "won_reason_id": won_reason_id,
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
                    UpdateOpportunityResponse,
                    parse_obj_as(
                        type_=UpdateOpportunityResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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


class AsyncRawOpportunitiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[OpportunitiesFilter] = None,
        sort: typing.Optional[OpportunitiesSort] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetOpportunitiesResponse]:
        """
        List opportunities

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[OpportunitiesFilter]
            Apply filters

        sort : typing.Optional[OpportunitiesSort]
            Apply sorting

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetOpportunitiesResponse]
            Opportunities
        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/opportunities",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=OpportunitiesFilter, direction="write"
                ),
                "sort": convert_and_respect_annotation_metadata(
                    object_=sort, annotation=OpportunitiesSort, direction="write"
                ),
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetOpportunitiesResponse,
                    parse_obj_as(
                        type_=GetOpportunitiesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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

    async def add(
        self,
        *,
        title: str,
        raw: typing.Optional[bool] = None,
        close_date: typing.Optional[dt.date] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        contact_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        date_last_contacted: typing.Optional[dt.datetime] = OMIT,
        date_lead_created: typing.Optional[dt.datetime] = OMIT,
        date_stage_changed: typing.Optional[dt.datetime] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        expected_revenue: typing.Optional[float] = OMIT,
        id: typing.Optional[str] = OMIT,
        interaction_count: typing.Optional[float] = OMIT,
        last_activity_at: typing.Optional[str] = OMIT,
        lead_id: typing.Optional[str] = OMIT,
        lead_source: typing.Optional[str] = OMIT,
        loss_reason: typing.Optional[str] = OMIT,
        loss_reason_id: typing.Optional[str] = OMIT,
        monetary_amount: typing.Optional[float] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        pipeline_id: typing.Optional[str] = OMIT,
        pipeline_stage_id: typing.Optional[str] = OMIT,
        primary_contact_id: typing.Optional[str] = OMIT,
        priority: typing.Optional[str] = OMIT,
        source_id: typing.Optional[str] = OMIT,
        stage_last_changed_at: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[str] = OMIT,
        status_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        win_probability: typing.Optional[float] = OMIT,
        won_reason: typing.Optional[str] = OMIT,
        won_reason_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateOpportunityResponse]:
        """
        Create opportunity

        Parameters
        ----------
        title : str
            The title or name of the opportunity.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        close_date : typing.Optional[dt.date]
            The actual closing date for the opportunity. If close_date is null, the opportunity is not closed yet.

        company_id : typing.Optional[str]
            The unique identifier of the company associated with the opportunity.

        company_name : typing.Optional[str]
            The name of the company associated with the opportunity.

        contact_id : typing.Optional[str]
            The unique identifier of the contact associated with the opportunity.

        contact_ids : typing.Optional[typing.Sequence[str]]
            An array of unique identifiers of all contacts associated with the opportunity.

        created_at : typing.Optional[dt.datetime]
            The date and time when the opportunity was created.

        created_by : typing.Optional[str]
            The unique identifier of the user who created the opportunity.

        currency : typing.Optional[Currency]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        date_last_contacted : typing.Optional[dt.datetime]
            The date and time when the opportunity was last contacted.

        date_lead_created : typing.Optional[dt.datetime]
            The date and time when the lead associated with the opportunity was created.

        date_stage_changed : typing.Optional[dt.datetime]
            The date and time when the stage of the opportunity was last changed.

        deleted : typing.Optional[bool]
            Indicates whether the opportunity has been deleted.

        description : typing.Optional[str]
            A description of the opportunity.

        expected_revenue : typing.Optional[float]
            The expected revenue from the opportunity

        id : typing.Optional[str]
            A unique identifier for the opportunity.

        interaction_count : typing.Optional[float]
            The number of interactions with the opportunity.

        last_activity_at : typing.Optional[str]
            The date and time of the last activity associated with the opportunity.

        lead_id : typing.Optional[str]
            The unique identifier of the lead associated with the opportunity.

        lead_source : typing.Optional[str]
            The source of the lead associated with the opportunity.

        loss_reason : typing.Optional[str]
            The reason why the opportunity was lost.

        loss_reason_id : typing.Optional[str]
            The unique identifier of the reason why the opportunity was lost.

        monetary_amount : typing.Optional[float]
            The monetary value associated with the opportunity

        owner_id : typing.Optional[str]
            The unique identifier of the user who owns the opportunity.

        pipeline_id : typing.Optional[str]
            The unique identifier of the pipeline associated with the opportunity

        pipeline_stage_id : typing.Optional[str]
            The unique identifier of the stage in the pipeline associated with the opportunity.

        primary_contact_id : typing.Optional[str]
            The unique identifier of the primary contact associated with the opportunity.

        priority : typing.Optional[str]
            The priority level of the opportunity.

        source_id : typing.Optional[str]
            The unique identifier of the source of the opportunity.

        stage_last_changed_at : typing.Optional[dt.datetime]
            The date and time when the stage of the opportunity was last changed.

        status : typing.Optional[str]
            The current status of the opportunity.

        status_id : typing.Optional[str]
            The unique identifier of the current status of the opportunity.

        tags : typing.Optional[Tags]

        type : typing.Optional[str]
            The type of the opportunity

        updated_at : typing.Optional[dt.datetime]
            The date and time when the opportunity was last updated.

        updated_by : typing.Optional[str]
            The unique identifier of the user who last updated the opportunity.

        win_probability : typing.Optional[float]
            The probability of winning the opportunity, expressed as a percentage.

        won_reason : typing.Optional[str]
            The reason why the opportunity was won.

        won_reason_id : typing.Optional[str]
            The unique identifier of the reason why the opportunity was won.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateOpportunityResponse]
            Opportunity created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/opportunities",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "close_date": close_date,
                "company_id": company_id,
                "company_name": company_name,
                "contact_id": contact_id,
                "contact_ids": contact_ids,
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "custom_fields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=typing.Sequence[CustomField], direction="write"
                ),
                "date_last_contacted": date_last_contacted,
                "date_lead_created": date_lead_created,
                "date_stage_changed": date_stage_changed,
                "deleted": deleted,
                "description": description,
                "expected_revenue": expected_revenue,
                "id": id,
                "interaction_count": interaction_count,
                "last_activity_at": last_activity_at,
                "lead_id": lead_id,
                "lead_source": lead_source,
                "loss_reason": loss_reason,
                "loss_reason_id": loss_reason_id,
                "monetary_amount": monetary_amount,
                "owner_id": owner_id,
                "pipeline_id": pipeline_id,
                "pipeline_stage_id": pipeline_stage_id,
                "primary_contact_id": primary_contact_id,
                "priority": priority,
                "source_id": source_id,
                "stage_last_changed_at": stage_last_changed_at,
                "status": status,
                "status_id": status_id,
                "tags": tags,
                "title": title,
                "type": type,
                "updated_at": updated_at,
                "updated_by": updated_by,
                "win_probability": win_probability,
                "won_reason": won_reason,
                "won_reason_id": won_reason_id,
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
                    CreateOpportunityResponse,
                    parse_obj_as(
                        type_=CreateOpportunityResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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

    async def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetOpportunityResponse]:
        """
        Get opportunity

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetOpportunityResponse]
            Opportunity
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/opportunities/{encode_path_param(id)}",
            method="GET",
            params={
                "raw": raw,
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetOpportunityResponse,
                    parse_obj_as(
                        type_=GetOpportunityResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteOpportunityResponse]:
        """
        Delete opportunity

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteOpportunityResponse]
            Opportunity deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/opportunities/{encode_path_param(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteOpportunityResponse,
                    parse_obj_as(
                        type_=DeleteOpportunityResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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

    async def update(
        self,
        id_: str,
        *,
        title: str,
        raw: typing.Optional[bool] = None,
        close_date: typing.Optional[dt.date] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        contact_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        date_last_contacted: typing.Optional[dt.datetime] = OMIT,
        date_lead_created: typing.Optional[dt.datetime] = OMIT,
        date_stage_changed: typing.Optional[dt.datetime] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        expected_revenue: typing.Optional[float] = OMIT,
        id: typing.Optional[str] = OMIT,
        interaction_count: typing.Optional[float] = OMIT,
        last_activity_at: typing.Optional[str] = OMIT,
        lead_id: typing.Optional[str] = OMIT,
        lead_source: typing.Optional[str] = OMIT,
        loss_reason: typing.Optional[str] = OMIT,
        loss_reason_id: typing.Optional[str] = OMIT,
        monetary_amount: typing.Optional[float] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        pipeline_id: typing.Optional[str] = OMIT,
        pipeline_stage_id: typing.Optional[str] = OMIT,
        primary_contact_id: typing.Optional[str] = OMIT,
        priority: typing.Optional[str] = OMIT,
        source_id: typing.Optional[str] = OMIT,
        stage_last_changed_at: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[str] = OMIT,
        status_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        win_probability: typing.Optional[float] = OMIT,
        won_reason: typing.Optional[str] = OMIT,
        won_reason_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateOpportunityResponse]:
        """
        Update opportunity

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        title : str
            The title or name of the opportunity.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        close_date : typing.Optional[dt.date]
            The actual closing date for the opportunity. If close_date is null, the opportunity is not closed yet.

        company_id : typing.Optional[str]
            The unique identifier of the company associated with the opportunity.

        company_name : typing.Optional[str]
            The name of the company associated with the opportunity.

        contact_id : typing.Optional[str]
            The unique identifier of the contact associated with the opportunity.

        contact_ids : typing.Optional[typing.Sequence[str]]
            An array of unique identifiers of all contacts associated with the opportunity.

        created_at : typing.Optional[dt.datetime]
            The date and time when the opportunity was created.

        created_by : typing.Optional[str]
            The unique identifier of the user who created the opportunity.

        currency : typing.Optional[Currency]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        date_last_contacted : typing.Optional[dt.datetime]
            The date and time when the opportunity was last contacted.

        date_lead_created : typing.Optional[dt.datetime]
            The date and time when the lead associated with the opportunity was created.

        date_stage_changed : typing.Optional[dt.datetime]
            The date and time when the stage of the opportunity was last changed.

        deleted : typing.Optional[bool]
            Indicates whether the opportunity has been deleted.

        description : typing.Optional[str]
            A description of the opportunity.

        expected_revenue : typing.Optional[float]
            The expected revenue from the opportunity

        id : typing.Optional[str]
            A unique identifier for the opportunity.

        interaction_count : typing.Optional[float]
            The number of interactions with the opportunity.

        last_activity_at : typing.Optional[str]
            The date and time of the last activity associated with the opportunity.

        lead_id : typing.Optional[str]
            The unique identifier of the lead associated with the opportunity.

        lead_source : typing.Optional[str]
            The source of the lead associated with the opportunity.

        loss_reason : typing.Optional[str]
            The reason why the opportunity was lost.

        loss_reason_id : typing.Optional[str]
            The unique identifier of the reason why the opportunity was lost.

        monetary_amount : typing.Optional[float]
            The monetary value associated with the opportunity

        owner_id : typing.Optional[str]
            The unique identifier of the user who owns the opportunity.

        pipeline_id : typing.Optional[str]
            The unique identifier of the pipeline associated with the opportunity

        pipeline_stage_id : typing.Optional[str]
            The unique identifier of the stage in the pipeline associated with the opportunity.

        primary_contact_id : typing.Optional[str]
            The unique identifier of the primary contact associated with the opportunity.

        priority : typing.Optional[str]
            The priority level of the opportunity.

        source_id : typing.Optional[str]
            The unique identifier of the source of the opportunity.

        stage_last_changed_at : typing.Optional[dt.datetime]
            The date and time when the stage of the opportunity was last changed.

        status : typing.Optional[str]
            The current status of the opportunity.

        status_id : typing.Optional[str]
            The unique identifier of the current status of the opportunity.

        tags : typing.Optional[Tags]

        type : typing.Optional[str]
            The type of the opportunity

        updated_at : typing.Optional[dt.datetime]
            The date and time when the opportunity was last updated.

        updated_by : typing.Optional[str]
            The unique identifier of the user who last updated the opportunity.

        win_probability : typing.Optional[float]
            The probability of winning the opportunity, expressed as a percentage.

        won_reason : typing.Optional[str]
            The reason why the opportunity was won.

        won_reason_id : typing.Optional[str]
            The unique identifier of the reason why the opportunity was won.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateOpportunityResponse]
            Opportunity updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/opportunities/{encode_path_param(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "close_date": close_date,
                "company_id": company_id,
                "company_name": company_name,
                "contact_id": contact_id,
                "contact_ids": contact_ids,
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "custom_fields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=typing.Sequence[CustomField], direction="write"
                ),
                "date_last_contacted": date_last_contacted,
                "date_lead_created": date_lead_created,
                "date_stage_changed": date_stage_changed,
                "deleted": deleted,
                "description": description,
                "expected_revenue": expected_revenue,
                "id": id,
                "interaction_count": interaction_count,
                "last_activity_at": last_activity_at,
                "lead_id": lead_id,
                "lead_source": lead_source,
                "loss_reason": loss_reason,
                "loss_reason_id": loss_reason_id,
                "monetary_amount": monetary_amount,
                "owner_id": owner_id,
                "pipeline_id": pipeline_id,
                "pipeline_stage_id": pipeline_stage_id,
                "primary_contact_id": primary_contact_id,
                "priority": priority,
                "source_id": source_id,
                "stage_last_changed_at": stage_last_changed_at,
                "status": status,
                "status_id": status_id,
                "tags": tags,
                "title": title,
                "type": type,
                "updated_at": updated_at,
                "updated_by": updated_by,
                "win_probability": win_probability,
                "won_reason": won_reason,
                "won_reason_id": won_reason_id,
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
                    UpdateOpportunityResponse,
                    parse_obj_as(
                        type_=UpdateOpportunityResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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
