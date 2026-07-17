

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
from ..types.address import Address
from ..types.bad_request_response import BadRequestResponse
from ..types.contact_gender import ContactGender
from ..types.contact_type import ContactType
from ..types.contacts_filter import ContactsFilter
from ..types.contacts_sort import ContactsSort
from ..types.create_contact_response import CreateContactResponse
from ..types.custom_field import CustomField
from ..types.delete_contact_response import DeleteContactResponse
from ..types.email import Email
from ..types.get_contact_response import GetContactResponse
from ..types.get_contacts_response import GetContactsResponse
from ..types.not_found_response import NotFoundResponse
from ..types.payment_required_response import PaymentRequiredResponse
from ..types.phone_number import PhoneNumber
from ..types.social_link import SocialLink
from ..types.tags import Tags
from ..types.unauthorized_response import UnauthorizedResponse
from ..types.unprocessable_response import UnprocessableResponse
from ..types.update_contact_response import UpdateContactResponse
from ..types.website import Website
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawContactsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[ContactsFilter] = None,
        sort: typing.Optional[ContactsSort] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetContactsResponse]:
        """
        List contacts

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[ContactsFilter]
            Apply filters

        sort : typing.Optional[ContactsSort]
            Apply sorting

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetContactsResponse]
            Contacts
        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/contacts",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=ContactsFilter, direction="write"
                ),
                "sort": convert_and_respect_annotation_metadata(
                    object_=sort, annotation=ContactsSort, direction="write"
                ),
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetContactsResponse,
                    parse_obj_as(
                        type_=GetContactsResponse,
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
        name: str,
        raw: typing.Optional[bool] = None,
        active: typing.Optional[bool] = OMIT,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        birthday: typing.Optional[str] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        current_balance: typing.Optional[float] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        department: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        email_domain: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        fax: typing.Optional[str] = OMIT,
        first_call_at: typing.Optional[dt.datetime] = OMIT,
        first_email_at: typing.Optional[dt.datetime] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        gender: typing.Optional[ContactGender] = OMIT,
        id: typing.Optional[str] = OMIT,
        image: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        last_activity_at: typing.Optional[dt.datetime] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        lead_id: typing.Optional[str] = OMIT,
        lead_source: typing.Optional[str] = OMIT,
        middle_name: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        photo_url: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[SocialLink]] = OMIT,
        status: typing.Optional[str] = OMIT,
        suffix: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        title: typing.Optional[str] = OMIT,
        type: typing.Optional[ContactType] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateContactResponse]:
        """
        Create contact

        Parameters
        ----------
        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[bool]

        addresses : typing.Optional[typing.Sequence[Address]]

        birthday : typing.Optional[str]

        company_id : typing.Optional[str]

        company_name : typing.Optional[str]

        created_at : typing.Optional[dt.datetime]

        current_balance : typing.Optional[float]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        department : typing.Optional[str]

        description : typing.Optional[str]

        email_domain : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        fax : typing.Optional[str]

        first_call_at : typing.Optional[dt.datetime]

        first_email_at : typing.Optional[dt.datetime]

        first_name : typing.Optional[str]

        gender : typing.Optional[ContactGender]

        id : typing.Optional[str]

        image : typing.Optional[str]

        language : typing.Optional[str]
            language code according to ISO 639-1. For the United States - EN

        last_activity_at : typing.Optional[dt.datetime]

        last_name : typing.Optional[str]

        lead_id : typing.Optional[str]

        lead_source : typing.Optional[str]

        middle_name : typing.Optional[str]

        owner_id : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        photo_url : typing.Optional[str]
            The URL of the photo of a person.

        prefix : typing.Optional[str]

        social_links : typing.Optional[typing.Sequence[SocialLink]]

        status : typing.Optional[str]

        suffix : typing.Optional[str]

        tags : typing.Optional[Tags]

        title : typing.Optional[str]

        type : typing.Optional[ContactType]

        updated_at : typing.Optional[dt.datetime]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateContactResponse]
            Contact created
        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/contacts",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "active": active,
                "addresses": convert_and_respect_annotation_metadata(
                    object_=addresses, annotation=typing.Sequence[Address], direction="write"
                ),
                "birthday": birthday,
                "company_id": company_id,
                "company_name": company_name,
                "created_at": created_at,
                "current_balance": current_balance,
                "custom_fields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=typing.Sequence[CustomField], direction="write"
                ),
                "department": department,
                "description": description,
                "email_domain": email_domain,
                "emails": convert_and_respect_annotation_metadata(
                    object_=emails, annotation=typing.Sequence[Email], direction="write"
                ),
                "fax": fax,
                "first_call_at": first_call_at,
                "first_email_at": first_email_at,
                "first_name": first_name,
                "gender": gender,
                "id": id,
                "image": image,
                "language": language,
                "last_activity_at": last_activity_at,
                "last_name": last_name,
                "lead_id": lead_id,
                "lead_source": lead_source,
                "middle_name": middle_name,
                "name": name,
                "owner_id": owner_id,
                "phone_numbers": convert_and_respect_annotation_metadata(
                    object_=phone_numbers, annotation=typing.Sequence[PhoneNumber], direction="write"
                ),
                "photo_url": photo_url,
                "prefix": prefix,
                "social_links": convert_and_respect_annotation_metadata(
                    object_=social_links, annotation=typing.Sequence[SocialLink], direction="write"
                ),
                "status": status,
                "suffix": suffix,
                "tags": tags,
                "title": title,
                "type": type,
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
                    CreateContactResponse,
                    parse_obj_as(
                        type_=CreateContactResponse,
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
    ) -> HttpResponse[GetContactResponse]:
        """
        Get contact

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
        HttpResponse[GetContactResponse]
            Contact
        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/contacts/{encode_path_param(id)}",
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
                    GetContactResponse,
                    parse_obj_as(
                        type_=GetContactResponse,
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
    ) -> HttpResponse[DeleteContactResponse]:
        """
        Delete contact

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
        HttpResponse[DeleteContactResponse]
            Contact deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/contacts/{encode_path_param(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteContactResponse,
                    parse_obj_as(
                        type_=DeleteContactResponse,
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
        name: str,
        raw: typing.Optional[bool] = None,
        active: typing.Optional[bool] = OMIT,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        birthday: typing.Optional[str] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        current_balance: typing.Optional[float] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        department: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        email_domain: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        fax: typing.Optional[str] = OMIT,
        first_call_at: typing.Optional[dt.datetime] = OMIT,
        first_email_at: typing.Optional[dt.datetime] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        gender: typing.Optional[ContactGender] = OMIT,
        id: typing.Optional[str] = OMIT,
        image: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        last_activity_at: typing.Optional[dt.datetime] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        lead_id: typing.Optional[str] = OMIT,
        lead_source: typing.Optional[str] = OMIT,
        middle_name: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        photo_url: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[SocialLink]] = OMIT,
        status: typing.Optional[str] = OMIT,
        suffix: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        title: typing.Optional[str] = OMIT,
        type: typing.Optional[ContactType] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateContactResponse]:
        """
        Update contact

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[bool]

        addresses : typing.Optional[typing.Sequence[Address]]

        birthday : typing.Optional[str]

        company_id : typing.Optional[str]

        company_name : typing.Optional[str]

        created_at : typing.Optional[dt.datetime]

        current_balance : typing.Optional[float]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        department : typing.Optional[str]

        description : typing.Optional[str]

        email_domain : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        fax : typing.Optional[str]

        first_call_at : typing.Optional[dt.datetime]

        first_email_at : typing.Optional[dt.datetime]

        first_name : typing.Optional[str]

        gender : typing.Optional[ContactGender]

        id : typing.Optional[str]

        image : typing.Optional[str]

        language : typing.Optional[str]
            language code according to ISO 639-1. For the United States - EN

        last_activity_at : typing.Optional[dt.datetime]

        last_name : typing.Optional[str]

        lead_id : typing.Optional[str]

        lead_source : typing.Optional[str]

        middle_name : typing.Optional[str]

        owner_id : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        photo_url : typing.Optional[str]
            The URL of the photo of a person.

        prefix : typing.Optional[str]

        social_links : typing.Optional[typing.Sequence[SocialLink]]

        status : typing.Optional[str]

        suffix : typing.Optional[str]

        tags : typing.Optional[Tags]

        title : typing.Optional[str]

        type : typing.Optional[ContactType]

        updated_at : typing.Optional[dt.datetime]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateContactResponse]
            Contact updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/contacts/{encode_path_param(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "active": active,
                "addresses": convert_and_respect_annotation_metadata(
                    object_=addresses, annotation=typing.Sequence[Address], direction="write"
                ),
                "birthday": birthday,
                "company_id": company_id,
                "company_name": company_name,
                "created_at": created_at,
                "current_balance": current_balance,
                "custom_fields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=typing.Sequence[CustomField], direction="write"
                ),
                "department": department,
                "description": description,
                "email_domain": email_domain,
                "emails": convert_and_respect_annotation_metadata(
                    object_=emails, annotation=typing.Sequence[Email], direction="write"
                ),
                "fax": fax,
                "first_call_at": first_call_at,
                "first_email_at": first_email_at,
                "first_name": first_name,
                "gender": gender,
                "id": id,
                "image": image,
                "language": language,
                "last_activity_at": last_activity_at,
                "last_name": last_name,
                "lead_id": lead_id,
                "lead_source": lead_source,
                "middle_name": middle_name,
                "name": name,
                "owner_id": owner_id,
                "phone_numbers": convert_and_respect_annotation_metadata(
                    object_=phone_numbers, annotation=typing.Sequence[PhoneNumber], direction="write"
                ),
                "photo_url": photo_url,
                "prefix": prefix,
                "social_links": convert_and_respect_annotation_metadata(
                    object_=social_links, annotation=typing.Sequence[SocialLink], direction="write"
                ),
                "status": status,
                "suffix": suffix,
                "tags": tags,
                "title": title,
                "type": type,
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
                    UpdateContactResponse,
                    parse_obj_as(
                        type_=UpdateContactResponse,
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


class AsyncRawContactsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[ContactsFilter] = None,
        sort: typing.Optional[ContactsSort] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetContactsResponse]:
        """
        List contacts

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[ContactsFilter]
            Apply filters

        sort : typing.Optional[ContactsSort]
            Apply sorting

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetContactsResponse]
            Contacts
        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/contacts",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=ContactsFilter, direction="write"
                ),
                "sort": convert_and_respect_annotation_metadata(
                    object_=sort, annotation=ContactsSort, direction="write"
                ),
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetContactsResponse,
                    parse_obj_as(
                        type_=GetContactsResponse,
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
        name: str,
        raw: typing.Optional[bool] = None,
        active: typing.Optional[bool] = OMIT,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        birthday: typing.Optional[str] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        current_balance: typing.Optional[float] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        department: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        email_domain: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        fax: typing.Optional[str] = OMIT,
        first_call_at: typing.Optional[dt.datetime] = OMIT,
        first_email_at: typing.Optional[dt.datetime] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        gender: typing.Optional[ContactGender] = OMIT,
        id: typing.Optional[str] = OMIT,
        image: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        last_activity_at: typing.Optional[dt.datetime] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        lead_id: typing.Optional[str] = OMIT,
        lead_source: typing.Optional[str] = OMIT,
        middle_name: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        photo_url: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[SocialLink]] = OMIT,
        status: typing.Optional[str] = OMIT,
        suffix: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        title: typing.Optional[str] = OMIT,
        type: typing.Optional[ContactType] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateContactResponse]:
        """
        Create contact

        Parameters
        ----------
        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[bool]

        addresses : typing.Optional[typing.Sequence[Address]]

        birthday : typing.Optional[str]

        company_id : typing.Optional[str]

        company_name : typing.Optional[str]

        created_at : typing.Optional[dt.datetime]

        current_balance : typing.Optional[float]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        department : typing.Optional[str]

        description : typing.Optional[str]

        email_domain : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        fax : typing.Optional[str]

        first_call_at : typing.Optional[dt.datetime]

        first_email_at : typing.Optional[dt.datetime]

        first_name : typing.Optional[str]

        gender : typing.Optional[ContactGender]

        id : typing.Optional[str]

        image : typing.Optional[str]

        language : typing.Optional[str]
            language code according to ISO 639-1. For the United States - EN

        last_activity_at : typing.Optional[dt.datetime]

        last_name : typing.Optional[str]

        lead_id : typing.Optional[str]

        lead_source : typing.Optional[str]

        middle_name : typing.Optional[str]

        owner_id : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        photo_url : typing.Optional[str]
            The URL of the photo of a person.

        prefix : typing.Optional[str]

        social_links : typing.Optional[typing.Sequence[SocialLink]]

        status : typing.Optional[str]

        suffix : typing.Optional[str]

        tags : typing.Optional[Tags]

        title : typing.Optional[str]

        type : typing.Optional[ContactType]

        updated_at : typing.Optional[dt.datetime]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateContactResponse]
            Contact created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/contacts",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "active": active,
                "addresses": convert_and_respect_annotation_metadata(
                    object_=addresses, annotation=typing.Sequence[Address], direction="write"
                ),
                "birthday": birthday,
                "company_id": company_id,
                "company_name": company_name,
                "created_at": created_at,
                "current_balance": current_balance,
                "custom_fields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=typing.Sequence[CustomField], direction="write"
                ),
                "department": department,
                "description": description,
                "email_domain": email_domain,
                "emails": convert_and_respect_annotation_metadata(
                    object_=emails, annotation=typing.Sequence[Email], direction="write"
                ),
                "fax": fax,
                "first_call_at": first_call_at,
                "first_email_at": first_email_at,
                "first_name": first_name,
                "gender": gender,
                "id": id,
                "image": image,
                "language": language,
                "last_activity_at": last_activity_at,
                "last_name": last_name,
                "lead_id": lead_id,
                "lead_source": lead_source,
                "middle_name": middle_name,
                "name": name,
                "owner_id": owner_id,
                "phone_numbers": convert_and_respect_annotation_metadata(
                    object_=phone_numbers, annotation=typing.Sequence[PhoneNumber], direction="write"
                ),
                "photo_url": photo_url,
                "prefix": prefix,
                "social_links": convert_and_respect_annotation_metadata(
                    object_=social_links, annotation=typing.Sequence[SocialLink], direction="write"
                ),
                "status": status,
                "suffix": suffix,
                "tags": tags,
                "title": title,
                "type": type,
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
                    CreateContactResponse,
                    parse_obj_as(
                        type_=CreateContactResponse,
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
    ) -> AsyncHttpResponse[GetContactResponse]:
        """
        Get contact

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
        AsyncHttpResponse[GetContactResponse]
            Contact
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/contacts/{encode_path_param(id)}",
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
                    GetContactResponse,
                    parse_obj_as(
                        type_=GetContactResponse,
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
    ) -> AsyncHttpResponse[DeleteContactResponse]:
        """
        Delete contact

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
        AsyncHttpResponse[DeleteContactResponse]
            Contact deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/contacts/{encode_path_param(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteContactResponse,
                    parse_obj_as(
                        type_=DeleteContactResponse,
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
        name: str,
        raw: typing.Optional[bool] = None,
        active: typing.Optional[bool] = OMIT,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        birthday: typing.Optional[str] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        current_balance: typing.Optional[float] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        department: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        email_domain: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        fax: typing.Optional[str] = OMIT,
        first_call_at: typing.Optional[dt.datetime] = OMIT,
        first_email_at: typing.Optional[dt.datetime] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        gender: typing.Optional[ContactGender] = OMIT,
        id: typing.Optional[str] = OMIT,
        image: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        last_activity_at: typing.Optional[dt.datetime] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        lead_id: typing.Optional[str] = OMIT,
        lead_source: typing.Optional[str] = OMIT,
        middle_name: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        photo_url: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[SocialLink]] = OMIT,
        status: typing.Optional[str] = OMIT,
        suffix: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        title: typing.Optional[str] = OMIT,
        type: typing.Optional[ContactType] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateContactResponse]:
        """
        Update contact

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[bool]

        addresses : typing.Optional[typing.Sequence[Address]]

        birthday : typing.Optional[str]

        company_id : typing.Optional[str]

        company_name : typing.Optional[str]

        created_at : typing.Optional[dt.datetime]

        current_balance : typing.Optional[float]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        department : typing.Optional[str]

        description : typing.Optional[str]

        email_domain : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        fax : typing.Optional[str]

        first_call_at : typing.Optional[dt.datetime]

        first_email_at : typing.Optional[dt.datetime]

        first_name : typing.Optional[str]

        gender : typing.Optional[ContactGender]

        id : typing.Optional[str]

        image : typing.Optional[str]

        language : typing.Optional[str]
            language code according to ISO 639-1. For the United States - EN

        last_activity_at : typing.Optional[dt.datetime]

        last_name : typing.Optional[str]

        lead_id : typing.Optional[str]

        lead_source : typing.Optional[str]

        middle_name : typing.Optional[str]

        owner_id : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        photo_url : typing.Optional[str]
            The URL of the photo of a person.

        prefix : typing.Optional[str]

        social_links : typing.Optional[typing.Sequence[SocialLink]]

        status : typing.Optional[str]

        suffix : typing.Optional[str]

        tags : typing.Optional[Tags]

        title : typing.Optional[str]

        type : typing.Optional[ContactType]

        updated_at : typing.Optional[dt.datetime]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateContactResponse]
            Contact updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/contacts/{encode_path_param(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "active": active,
                "addresses": convert_and_respect_annotation_metadata(
                    object_=addresses, annotation=typing.Sequence[Address], direction="write"
                ),
                "birthday": birthday,
                "company_id": company_id,
                "company_name": company_name,
                "created_at": created_at,
                "current_balance": current_balance,
                "custom_fields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=typing.Sequence[CustomField], direction="write"
                ),
                "department": department,
                "description": description,
                "email_domain": email_domain,
                "emails": convert_and_respect_annotation_metadata(
                    object_=emails, annotation=typing.Sequence[Email], direction="write"
                ),
                "fax": fax,
                "first_call_at": first_call_at,
                "first_email_at": first_email_at,
                "first_name": first_name,
                "gender": gender,
                "id": id,
                "image": image,
                "language": language,
                "last_activity_at": last_activity_at,
                "last_name": last_name,
                "lead_id": lead_id,
                "lead_source": lead_source,
                "middle_name": middle_name,
                "name": name,
                "owner_id": owner_id,
                "phone_numbers": convert_and_respect_annotation_metadata(
                    object_=phone_numbers, annotation=typing.Sequence[PhoneNumber], direction="write"
                ),
                "photo_url": photo_url,
                "prefix": prefix,
                "social_links": convert_and_respect_annotation_metadata(
                    object_=social_links, annotation=typing.Sequence[SocialLink], direction="write"
                ),
                "status": status,
                "suffix": suffix,
                "tags": tags,
                "title": title,
                "type": type,
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
                    UpdateContactResponse,
                    parse_obj_as(
                        type_=UpdateContactResponse,
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
