

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.address import Address
from ..types.bad_request_response import BadRequestResponse
from ..types.create_lead_response import CreateLeadResponse
from ..types.currency import Currency
from ..types.custom_field import CustomField
from ..types.delete_lead_response import DeleteLeadResponse
from ..types.email import Email
from ..types.get_lead_response import GetLeadResponse
from ..types.get_leads_response import GetLeadsResponse
from ..types.leads_filter import LeadsFilter
from ..types.leads_sort import LeadsSort
from ..types.not_found_response import NotFoundResponse
from ..types.payment_required_response import PaymentRequiredResponse
from ..types.phone_number import PhoneNumber
from ..types.social_link import SocialLink
from ..types.tags import Tags
from ..types.unauthorized_response import UnauthorizedResponse
from ..types.unprocessable_response import UnprocessableResponse
from ..types.update_lead_response import UpdateLeadResponse
from ..types.website import Website


OMIT = typing.cast(typing.Any, ...)


class RawLeadsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[LeadsFilter] = None,
        sort: typing.Optional[LeadsSort] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetLeadsResponse]:
        """
        List leads

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[LeadsFilter]
            Apply filters

        sort : typing.Optional[LeadsSort]
            Apply sorting

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetLeadsResponse]
            Leads
        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/leads",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=LeadsFilter, direction="write"
                ),
                "sort": convert_and_respect_annotation_metadata(object_=sort, annotation=LeadsSort, direction="write"),
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLeadsResponse,
                    parse_obj_as(
                        type_=GetLeadsResponse,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def add(
        self,
        *,
        name: str,
        raw: typing.Optional[bool] = None,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        description: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        fax: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        lead_source: typing.Optional[str] = OMIT,
        monetary_amount: typing.Optional[float] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[SocialLink]] = OMIT,
        status: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateLeadResponse]:
        """
        Create lead

        Parameters
        ----------
        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        addresses : typing.Optional[typing.Sequence[Address]]

        company_id : typing.Optional[str]

        company_name : typing.Optional[str]

        contact_id : typing.Optional[str]

        created_at : typing.Optional[str]

        currency : typing.Optional[Currency]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        description : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        fax : typing.Optional[str]

        first_name : typing.Optional[str]

        id : typing.Optional[str]

        language : typing.Optional[str]
            language code according to ISO 639-1. For the United States - EN

        last_name : typing.Optional[str]

        lead_source : typing.Optional[str]

        monetary_amount : typing.Optional[float]

        owner_id : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        prefix : typing.Optional[str]

        social_links : typing.Optional[typing.Sequence[SocialLink]]

        status : typing.Optional[str]

        tags : typing.Optional[Tags]

        title : typing.Optional[str]

        updated_at : typing.Optional[str]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateLeadResponse]
            Lead created
        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/leads",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "addresses": convert_and_respect_annotation_metadata(
                    object_=addresses, annotation=typing.Sequence[Address], direction="write"
                ),
                "company_id": company_id,
                "company_name": company_name,
                "contact_id": contact_id,
                "created_at": created_at,
                "currency": currency,
                "custom_fields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=typing.Sequence[CustomField], direction="write"
                ),
                "description": description,
                "emails": convert_and_respect_annotation_metadata(
                    object_=emails, annotation=typing.Sequence[Email], direction="write"
                ),
                "fax": fax,
                "first_name": first_name,
                "id": id,
                "language": language,
                "last_name": last_name,
                "lead_source": lead_source,
                "monetary_amount": monetary_amount,
                "name": name,
                "owner_id": owner_id,
                "phone_numbers": convert_and_respect_annotation_metadata(
                    object_=phone_numbers, annotation=typing.Sequence[PhoneNumber], direction="write"
                ),
                "prefix": prefix,
                "social_links": convert_and_respect_annotation_metadata(
                    object_=social_links, annotation=typing.Sequence[SocialLink], direction="write"
                ),
                "status": status,
                "tags": tags,
                "title": title,
                "updated_at": updated_at,
                "websites": convert_and_respect_annotation_metadata(
                    object_=websites, annotation=typing.Sequence[Website], direction="write"
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
                    CreateLeadResponse,
                    parse_obj_as(
                        type_=CreateLeadResponse,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetLeadResponse]:
        """
        Get lead

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
        HttpResponse[GetLeadResponse]
            Lead
        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/leads/{jsonable_encoder(id)}",
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
                    GetLeadResponse,
                    parse_obj_as(
                        type_=GetLeadResponse,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteLeadResponse]:
        """
        Delete lead

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
        HttpResponse[DeleteLeadResponse]
            Lead deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/leads/{jsonable_encoder(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteLeadResponse,
                    parse_obj_as(
                        type_=DeleteLeadResponse,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update(
        self,
        id_: str,
        *,
        name: str,
        raw: typing.Optional[bool] = None,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        description: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        fax: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        lead_source: typing.Optional[str] = OMIT,
        monetary_amount: typing.Optional[float] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[SocialLink]] = OMIT,
        status: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateLeadResponse]:
        """
        Update lead

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        addresses : typing.Optional[typing.Sequence[Address]]

        company_id : typing.Optional[str]

        company_name : typing.Optional[str]

        contact_id : typing.Optional[str]

        created_at : typing.Optional[str]

        currency : typing.Optional[Currency]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        description : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        fax : typing.Optional[str]

        first_name : typing.Optional[str]

        id : typing.Optional[str]

        language : typing.Optional[str]
            language code according to ISO 639-1. For the United States - EN

        last_name : typing.Optional[str]

        lead_source : typing.Optional[str]

        monetary_amount : typing.Optional[float]

        owner_id : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        prefix : typing.Optional[str]

        social_links : typing.Optional[typing.Sequence[SocialLink]]

        status : typing.Optional[str]

        tags : typing.Optional[Tags]

        title : typing.Optional[str]

        updated_at : typing.Optional[str]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateLeadResponse]
            Lead updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/leads/{jsonable_encoder(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "addresses": convert_and_respect_annotation_metadata(
                    object_=addresses, annotation=typing.Sequence[Address], direction="write"
                ),
                "company_id": company_id,
                "company_name": company_name,
                "contact_id": contact_id,
                "created_at": created_at,
                "currency": currency,
                "custom_fields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=typing.Sequence[CustomField], direction="write"
                ),
                "description": description,
                "emails": convert_and_respect_annotation_metadata(
                    object_=emails, annotation=typing.Sequence[Email], direction="write"
                ),
                "fax": fax,
                "first_name": first_name,
                "id": id,
                "language": language,
                "last_name": last_name,
                "lead_source": lead_source,
                "monetary_amount": monetary_amount,
                "name": name,
                "owner_id": owner_id,
                "phone_numbers": convert_and_respect_annotation_metadata(
                    object_=phone_numbers, annotation=typing.Sequence[PhoneNumber], direction="write"
                ),
                "prefix": prefix,
                "social_links": convert_and_respect_annotation_metadata(
                    object_=social_links, annotation=typing.Sequence[SocialLink], direction="write"
                ),
                "status": status,
                "tags": tags,
                "title": title,
                "updated_at": updated_at,
                "websites": convert_and_respect_annotation_metadata(
                    object_=websites, annotation=typing.Sequence[Website], direction="write"
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
                    UpdateLeadResponse,
                    parse_obj_as(
                        type_=UpdateLeadResponse,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawLeadsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[LeadsFilter] = None,
        sort: typing.Optional[LeadsSort] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetLeadsResponse]:
        """
        List leads

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[LeadsFilter]
            Apply filters

        sort : typing.Optional[LeadsSort]
            Apply sorting

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetLeadsResponse]
            Leads
        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/leads",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=LeadsFilter, direction="write"
                ),
                "sort": convert_and_respect_annotation_metadata(object_=sort, annotation=LeadsSort, direction="write"),
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLeadsResponse,
                    parse_obj_as(
                        type_=GetLeadsResponse,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def add(
        self,
        *,
        name: str,
        raw: typing.Optional[bool] = None,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        description: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        fax: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        lead_source: typing.Optional[str] = OMIT,
        monetary_amount: typing.Optional[float] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[SocialLink]] = OMIT,
        status: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateLeadResponse]:
        """
        Create lead

        Parameters
        ----------
        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        addresses : typing.Optional[typing.Sequence[Address]]

        company_id : typing.Optional[str]

        company_name : typing.Optional[str]

        contact_id : typing.Optional[str]

        created_at : typing.Optional[str]

        currency : typing.Optional[Currency]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        description : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        fax : typing.Optional[str]

        first_name : typing.Optional[str]

        id : typing.Optional[str]

        language : typing.Optional[str]
            language code according to ISO 639-1. For the United States - EN

        last_name : typing.Optional[str]

        lead_source : typing.Optional[str]

        monetary_amount : typing.Optional[float]

        owner_id : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        prefix : typing.Optional[str]

        social_links : typing.Optional[typing.Sequence[SocialLink]]

        status : typing.Optional[str]

        tags : typing.Optional[Tags]

        title : typing.Optional[str]

        updated_at : typing.Optional[str]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateLeadResponse]
            Lead created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/leads",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "addresses": convert_and_respect_annotation_metadata(
                    object_=addresses, annotation=typing.Sequence[Address], direction="write"
                ),
                "company_id": company_id,
                "company_name": company_name,
                "contact_id": contact_id,
                "created_at": created_at,
                "currency": currency,
                "custom_fields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=typing.Sequence[CustomField], direction="write"
                ),
                "description": description,
                "emails": convert_and_respect_annotation_metadata(
                    object_=emails, annotation=typing.Sequence[Email], direction="write"
                ),
                "fax": fax,
                "first_name": first_name,
                "id": id,
                "language": language,
                "last_name": last_name,
                "lead_source": lead_source,
                "monetary_amount": monetary_amount,
                "name": name,
                "owner_id": owner_id,
                "phone_numbers": convert_and_respect_annotation_metadata(
                    object_=phone_numbers, annotation=typing.Sequence[PhoneNumber], direction="write"
                ),
                "prefix": prefix,
                "social_links": convert_and_respect_annotation_metadata(
                    object_=social_links, annotation=typing.Sequence[SocialLink], direction="write"
                ),
                "status": status,
                "tags": tags,
                "title": title,
                "updated_at": updated_at,
                "websites": convert_and_respect_annotation_metadata(
                    object_=websites, annotation=typing.Sequence[Website], direction="write"
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
                    CreateLeadResponse,
                    parse_obj_as(
                        type_=CreateLeadResponse,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetLeadResponse]:
        """
        Get lead

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
        AsyncHttpResponse[GetLeadResponse]
            Lead
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/leads/{jsonable_encoder(id)}",
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
                    GetLeadResponse,
                    parse_obj_as(
                        type_=GetLeadResponse,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteLeadResponse]:
        """
        Delete lead

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
        AsyncHttpResponse[DeleteLeadResponse]
            Lead deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/leads/{jsonable_encoder(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteLeadResponse,
                    parse_obj_as(
                        type_=DeleteLeadResponse,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update(
        self,
        id_: str,
        *,
        name: str,
        raw: typing.Optional[bool] = None,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        description: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        fax: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        lead_source: typing.Optional[str] = OMIT,
        monetary_amount: typing.Optional[float] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[SocialLink]] = OMIT,
        status: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateLeadResponse]:
        """
        Update lead

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        addresses : typing.Optional[typing.Sequence[Address]]

        company_id : typing.Optional[str]

        company_name : typing.Optional[str]

        contact_id : typing.Optional[str]

        created_at : typing.Optional[str]

        currency : typing.Optional[Currency]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        description : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        fax : typing.Optional[str]

        first_name : typing.Optional[str]

        id : typing.Optional[str]

        language : typing.Optional[str]
            language code according to ISO 639-1. For the United States - EN

        last_name : typing.Optional[str]

        lead_source : typing.Optional[str]

        monetary_amount : typing.Optional[float]

        owner_id : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        prefix : typing.Optional[str]

        social_links : typing.Optional[typing.Sequence[SocialLink]]

        status : typing.Optional[str]

        tags : typing.Optional[Tags]

        title : typing.Optional[str]

        updated_at : typing.Optional[str]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateLeadResponse]
            Lead updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/leads/{jsonable_encoder(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "addresses": convert_and_respect_annotation_metadata(
                    object_=addresses, annotation=typing.Sequence[Address], direction="write"
                ),
                "company_id": company_id,
                "company_name": company_name,
                "contact_id": contact_id,
                "created_at": created_at,
                "currency": currency,
                "custom_fields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=typing.Sequence[CustomField], direction="write"
                ),
                "description": description,
                "emails": convert_and_respect_annotation_metadata(
                    object_=emails, annotation=typing.Sequence[Email], direction="write"
                ),
                "fax": fax,
                "first_name": first_name,
                "id": id,
                "language": language,
                "last_name": last_name,
                "lead_source": lead_source,
                "monetary_amount": monetary_amount,
                "name": name,
                "owner_id": owner_id,
                "phone_numbers": convert_and_respect_annotation_metadata(
                    object_=phone_numbers, annotation=typing.Sequence[PhoneNumber], direction="write"
                ),
                "prefix": prefix,
                "social_links": convert_and_respect_annotation_metadata(
                    object_=social_links, annotation=typing.Sequence[SocialLink], direction="write"
                ),
                "status": status,
                "tags": tags,
                "title": title,
                "updated_at": updated_at,
                "websites": convert_and_respect_annotation_metadata(
                    object_=websites, annotation=typing.Sequence[Website], direction="write"
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
                    UpdateLeadResponse,
                    parse_obj_as(
                        type_=UpdateLeadResponse,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
