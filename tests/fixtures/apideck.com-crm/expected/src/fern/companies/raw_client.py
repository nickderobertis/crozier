

import datetime as dt
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
from ..types.bank_account import BankAccount
from ..types.companies_filter import CompaniesFilter
from ..types.companies_sort import CompaniesSort
from ..types.company_row_type import CompanyRowType
from ..types.create_company_response import CreateCompanyResponse
from ..types.currency import Currency
from ..types.custom_field import CustomField
from ..types.delete_company_response import DeleteCompanyResponse
from ..types.email import Email
from ..types.first_name import FirstName
from ..types.get_companies_response import GetCompaniesResponse
from ..types.get_company_response import GetCompanyResponse
from ..types.last_name import LastName
from ..types.not_found_response import NotFoundResponse
from ..types.payment_required_response import PaymentRequiredResponse
from ..types.phone_number import PhoneNumber
from ..types.social_link import SocialLink
from ..types.tags import Tags
from ..types.unauthorized_response import UnauthorizedResponse
from ..types.unprocessable_response import UnprocessableResponse
from ..types.update_company_response import UpdateCompanyResponse
from ..types.website import Website


OMIT = typing.cast(typing.Any, ...)


class RawCompaniesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[CompaniesFilter] = None,
        sort: typing.Optional[CompaniesSort] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetCompaniesResponse]:
        """
        List companies

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[CompaniesFilter]
            Apply filters

        sort : typing.Optional[CompaniesSort]
            Apply sorting

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetCompaniesResponse]
            Companies
        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/companies",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=CompaniesFilter, direction="write"
                ),
                "sort": convert_and_respect_annotation_metadata(
                    object_=sort, annotation=CompaniesSort, direction="write"
                ),
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCompaniesResponse,
                    parse_obj_as(
                        type_=GetCompaniesResponse,
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
        abn_branch: typing.Optional[str] = OMIT,
        abn_or_tfn: typing.Optional[str] = OMIT,
        acn: typing.Optional[str] = OMIT,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        annual_revenue: typing.Optional[str] = OMIT,
        bank_accounts: typing.Optional[typing.Sequence[BankAccount]] = OMIT,
        birthday: typing.Optional[dt.date] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        fax: typing.Optional[str] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        id: typing.Optional[str] = OMIT,
        image: typing.Optional[str] = OMIT,
        industry: typing.Optional[str] = OMIT,
        interaction_count: typing.Optional[int] = OMIT,
        last_activity_at: typing.Optional[dt.datetime] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        number_of_employees: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        ownership: typing.Optional[str] = OMIT,
        parent_id: typing.Optional[str] = OMIT,
        payee_number: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        row_type: typing.Optional[CompanyRowType] = OMIT,
        sales_tax_number: typing.Optional[str] = OMIT,
        salutation: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[SocialLink]] = OMIT,
        status: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        vat_number: typing.Optional[str] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateCompanyResponse]:
        """
        Create company

        Parameters
        ----------
        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        abn_branch : typing.Optional[str]
            An ABN Branch (also known as a GST Branch) is used if part of your business needs to account for GST separately from its parent entity.

        abn_or_tfn : typing.Optional[str]
            An ABN is necessary for operating a business, while a TFN (Tax File Number) is required for any person working in Australia.

        acn : typing.Optional[str]
            The Australian Company Number (ACN) is a nine digit number with the last digit being a check digit calculated using a modified modulus 10 calculation. ASIC has adopted a convention of always printing and displaying the ACN in the format XXX XXX XXX; three blocks of three characters, each block separated by a blank.

        addresses : typing.Optional[typing.Sequence[Address]]

        annual_revenue : typing.Optional[str]
            Annual revenue

        bank_accounts : typing.Optional[typing.Sequence[BankAccount]]

        birthday : typing.Optional[dt.date]
            The date of birth of the person.

        created_at : typing.Optional[dt.datetime]

        created_by : typing.Optional[str]

        currency : typing.Optional[Currency]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        deleted : typing.Optional[bool]

        description : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        fax : typing.Optional[str]

        first_name : typing.Optional[FirstName]

        id : typing.Optional[str]

        image : typing.Optional[str]

        industry : typing.Optional[str]
            Industry

        interaction_count : typing.Optional[int]

        last_activity_at : typing.Optional[dt.datetime]

        last_name : typing.Optional[LastName]

        number_of_employees : typing.Optional[str]
            Number of employees

        owner_id : typing.Optional[str]

        ownership : typing.Optional[str]
            Ownership

        parent_id : typing.Optional[str]
            Parent ID

        payee_number : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        read_only : typing.Optional[bool]

        row_type : typing.Optional[CompanyRowType]

        sales_tax_number : typing.Optional[str]

        salutation : typing.Optional[str]
            A formal salutation for the person. For example, 'Mr', 'Mrs'

        social_links : typing.Optional[typing.Sequence[SocialLink]]

        status : typing.Optional[str]

        tags : typing.Optional[Tags]

        updated_at : typing.Optional[dt.datetime]

        updated_by : typing.Optional[str]

        vat_number : typing.Optional[str]
            VAT number

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateCompanyResponse]
            Company created
        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/companies",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "abn_branch": abn_branch,
                "abn_or_tfn": abn_or_tfn,
                "acn": acn,
                "addresses": convert_and_respect_annotation_metadata(
                    object_=addresses, annotation=typing.Sequence[Address], direction="write"
                ),
                "annual_revenue": annual_revenue,
                "bank_accounts": convert_and_respect_annotation_metadata(
                    object_=bank_accounts, annotation=typing.Sequence[BankAccount], direction="write"
                ),
                "birthday": birthday,
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "custom_fields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=typing.Sequence[CustomField], direction="write"
                ),
                "deleted": deleted,
                "description": description,
                "emails": convert_and_respect_annotation_metadata(
                    object_=emails, annotation=typing.Sequence[Email], direction="write"
                ),
                "fax": fax,
                "first_name": first_name,
                "id": id,
                "image": image,
                "industry": industry,
                "interaction_count": interaction_count,
                "last_activity_at": last_activity_at,
                "last_name": last_name,
                "name": name,
                "number_of_employees": number_of_employees,
                "owner_id": owner_id,
                "ownership": ownership,
                "parent_id": parent_id,
                "payee_number": payee_number,
                "phone_numbers": convert_and_respect_annotation_metadata(
                    object_=phone_numbers, annotation=typing.Sequence[PhoneNumber], direction="write"
                ),
                "read_only": read_only,
                "row_type": convert_and_respect_annotation_metadata(
                    object_=row_type, annotation=CompanyRowType, direction="write"
                ),
                "sales_tax_number": sales_tax_number,
                "salutation": salutation,
                "social_links": convert_and_respect_annotation_metadata(
                    object_=social_links, annotation=typing.Sequence[SocialLink], direction="write"
                ),
                "status": status,
                "tags": tags,
                "updated_at": updated_at,
                "updated_by": updated_by,
                "vat_number": vat_number,
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
                    CreateCompanyResponse,
                    parse_obj_as(
                        type_=CreateCompanyResponse,
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
    ) -> HttpResponse[GetCompanyResponse]:
        """
        Get company

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
        HttpResponse[GetCompanyResponse]
            Company
        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/companies/{jsonable_encoder(id)}",
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
                    GetCompanyResponse,
                    parse_obj_as(
                        type_=GetCompanyResponse,
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
    ) -> HttpResponse[DeleteCompanyResponse]:
        """
        Delete company

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
        HttpResponse[DeleteCompanyResponse]
            Company deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/companies/{jsonable_encoder(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteCompanyResponse,
                    parse_obj_as(
                        type_=DeleteCompanyResponse,
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
        abn_branch: typing.Optional[str] = OMIT,
        abn_or_tfn: typing.Optional[str] = OMIT,
        acn: typing.Optional[str] = OMIT,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        annual_revenue: typing.Optional[str] = OMIT,
        bank_accounts: typing.Optional[typing.Sequence[BankAccount]] = OMIT,
        birthday: typing.Optional[dt.date] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        fax: typing.Optional[str] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        id: typing.Optional[str] = OMIT,
        image: typing.Optional[str] = OMIT,
        industry: typing.Optional[str] = OMIT,
        interaction_count: typing.Optional[int] = OMIT,
        last_activity_at: typing.Optional[dt.datetime] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        number_of_employees: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        ownership: typing.Optional[str] = OMIT,
        parent_id: typing.Optional[str] = OMIT,
        payee_number: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        row_type: typing.Optional[CompanyRowType] = OMIT,
        sales_tax_number: typing.Optional[str] = OMIT,
        salutation: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[SocialLink]] = OMIT,
        status: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        vat_number: typing.Optional[str] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateCompanyResponse]:
        """
        Update company

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        abn_branch : typing.Optional[str]
            An ABN Branch (also known as a GST Branch) is used if part of your business needs to account for GST separately from its parent entity.

        abn_or_tfn : typing.Optional[str]
            An ABN is necessary for operating a business, while a TFN (Tax File Number) is required for any person working in Australia.

        acn : typing.Optional[str]
            The Australian Company Number (ACN) is a nine digit number with the last digit being a check digit calculated using a modified modulus 10 calculation. ASIC has adopted a convention of always printing and displaying the ACN in the format XXX XXX XXX; three blocks of three characters, each block separated by a blank.

        addresses : typing.Optional[typing.Sequence[Address]]

        annual_revenue : typing.Optional[str]
            Annual revenue

        bank_accounts : typing.Optional[typing.Sequence[BankAccount]]

        birthday : typing.Optional[dt.date]
            The date of birth of the person.

        created_at : typing.Optional[dt.datetime]

        created_by : typing.Optional[str]

        currency : typing.Optional[Currency]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        deleted : typing.Optional[bool]

        description : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        fax : typing.Optional[str]

        first_name : typing.Optional[FirstName]

        id : typing.Optional[str]

        image : typing.Optional[str]

        industry : typing.Optional[str]
            Industry

        interaction_count : typing.Optional[int]

        last_activity_at : typing.Optional[dt.datetime]

        last_name : typing.Optional[LastName]

        number_of_employees : typing.Optional[str]
            Number of employees

        owner_id : typing.Optional[str]

        ownership : typing.Optional[str]
            Ownership

        parent_id : typing.Optional[str]
            Parent ID

        payee_number : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        read_only : typing.Optional[bool]

        row_type : typing.Optional[CompanyRowType]

        sales_tax_number : typing.Optional[str]

        salutation : typing.Optional[str]
            A formal salutation for the person. For example, 'Mr', 'Mrs'

        social_links : typing.Optional[typing.Sequence[SocialLink]]

        status : typing.Optional[str]

        tags : typing.Optional[Tags]

        updated_at : typing.Optional[dt.datetime]

        updated_by : typing.Optional[str]

        vat_number : typing.Optional[str]
            VAT number

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateCompanyResponse]
            Company updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/companies/{jsonable_encoder(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "abn_branch": abn_branch,
                "abn_or_tfn": abn_or_tfn,
                "acn": acn,
                "addresses": convert_and_respect_annotation_metadata(
                    object_=addresses, annotation=typing.Sequence[Address], direction="write"
                ),
                "annual_revenue": annual_revenue,
                "bank_accounts": convert_and_respect_annotation_metadata(
                    object_=bank_accounts, annotation=typing.Sequence[BankAccount], direction="write"
                ),
                "birthday": birthday,
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "custom_fields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=typing.Sequence[CustomField], direction="write"
                ),
                "deleted": deleted,
                "description": description,
                "emails": convert_and_respect_annotation_metadata(
                    object_=emails, annotation=typing.Sequence[Email], direction="write"
                ),
                "fax": fax,
                "first_name": first_name,
                "id": id,
                "image": image,
                "industry": industry,
                "interaction_count": interaction_count,
                "last_activity_at": last_activity_at,
                "last_name": last_name,
                "name": name,
                "number_of_employees": number_of_employees,
                "owner_id": owner_id,
                "ownership": ownership,
                "parent_id": parent_id,
                "payee_number": payee_number,
                "phone_numbers": convert_and_respect_annotation_metadata(
                    object_=phone_numbers, annotation=typing.Sequence[PhoneNumber], direction="write"
                ),
                "read_only": read_only,
                "row_type": convert_and_respect_annotation_metadata(
                    object_=row_type, annotation=CompanyRowType, direction="write"
                ),
                "sales_tax_number": sales_tax_number,
                "salutation": salutation,
                "social_links": convert_and_respect_annotation_metadata(
                    object_=social_links, annotation=typing.Sequence[SocialLink], direction="write"
                ),
                "status": status,
                "tags": tags,
                "updated_at": updated_at,
                "updated_by": updated_by,
                "vat_number": vat_number,
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
                    UpdateCompanyResponse,
                    parse_obj_as(
                        type_=UpdateCompanyResponse,
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


class AsyncRawCompaniesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[CompaniesFilter] = None,
        sort: typing.Optional[CompaniesSort] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetCompaniesResponse]:
        """
        List companies

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[CompaniesFilter]
            Apply filters

        sort : typing.Optional[CompaniesSort]
            Apply sorting

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetCompaniesResponse]
            Companies
        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/companies",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=CompaniesFilter, direction="write"
                ),
                "sort": convert_and_respect_annotation_metadata(
                    object_=sort, annotation=CompaniesSort, direction="write"
                ),
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCompaniesResponse,
                    parse_obj_as(
                        type_=GetCompaniesResponse,
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
        abn_branch: typing.Optional[str] = OMIT,
        abn_or_tfn: typing.Optional[str] = OMIT,
        acn: typing.Optional[str] = OMIT,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        annual_revenue: typing.Optional[str] = OMIT,
        bank_accounts: typing.Optional[typing.Sequence[BankAccount]] = OMIT,
        birthday: typing.Optional[dt.date] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        fax: typing.Optional[str] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        id: typing.Optional[str] = OMIT,
        image: typing.Optional[str] = OMIT,
        industry: typing.Optional[str] = OMIT,
        interaction_count: typing.Optional[int] = OMIT,
        last_activity_at: typing.Optional[dt.datetime] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        number_of_employees: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        ownership: typing.Optional[str] = OMIT,
        parent_id: typing.Optional[str] = OMIT,
        payee_number: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        row_type: typing.Optional[CompanyRowType] = OMIT,
        sales_tax_number: typing.Optional[str] = OMIT,
        salutation: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[SocialLink]] = OMIT,
        status: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        vat_number: typing.Optional[str] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateCompanyResponse]:
        """
        Create company

        Parameters
        ----------
        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        abn_branch : typing.Optional[str]
            An ABN Branch (also known as a GST Branch) is used if part of your business needs to account for GST separately from its parent entity.

        abn_or_tfn : typing.Optional[str]
            An ABN is necessary for operating a business, while a TFN (Tax File Number) is required for any person working in Australia.

        acn : typing.Optional[str]
            The Australian Company Number (ACN) is a nine digit number with the last digit being a check digit calculated using a modified modulus 10 calculation. ASIC has adopted a convention of always printing and displaying the ACN in the format XXX XXX XXX; three blocks of three characters, each block separated by a blank.

        addresses : typing.Optional[typing.Sequence[Address]]

        annual_revenue : typing.Optional[str]
            Annual revenue

        bank_accounts : typing.Optional[typing.Sequence[BankAccount]]

        birthday : typing.Optional[dt.date]
            The date of birth of the person.

        created_at : typing.Optional[dt.datetime]

        created_by : typing.Optional[str]

        currency : typing.Optional[Currency]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        deleted : typing.Optional[bool]

        description : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        fax : typing.Optional[str]

        first_name : typing.Optional[FirstName]

        id : typing.Optional[str]

        image : typing.Optional[str]

        industry : typing.Optional[str]
            Industry

        interaction_count : typing.Optional[int]

        last_activity_at : typing.Optional[dt.datetime]

        last_name : typing.Optional[LastName]

        number_of_employees : typing.Optional[str]
            Number of employees

        owner_id : typing.Optional[str]

        ownership : typing.Optional[str]
            Ownership

        parent_id : typing.Optional[str]
            Parent ID

        payee_number : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        read_only : typing.Optional[bool]

        row_type : typing.Optional[CompanyRowType]

        sales_tax_number : typing.Optional[str]

        salutation : typing.Optional[str]
            A formal salutation for the person. For example, 'Mr', 'Mrs'

        social_links : typing.Optional[typing.Sequence[SocialLink]]

        status : typing.Optional[str]

        tags : typing.Optional[Tags]

        updated_at : typing.Optional[dt.datetime]

        updated_by : typing.Optional[str]

        vat_number : typing.Optional[str]
            VAT number

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateCompanyResponse]
            Company created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/companies",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "abn_branch": abn_branch,
                "abn_or_tfn": abn_or_tfn,
                "acn": acn,
                "addresses": convert_and_respect_annotation_metadata(
                    object_=addresses, annotation=typing.Sequence[Address], direction="write"
                ),
                "annual_revenue": annual_revenue,
                "bank_accounts": convert_and_respect_annotation_metadata(
                    object_=bank_accounts, annotation=typing.Sequence[BankAccount], direction="write"
                ),
                "birthday": birthday,
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "custom_fields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=typing.Sequence[CustomField], direction="write"
                ),
                "deleted": deleted,
                "description": description,
                "emails": convert_and_respect_annotation_metadata(
                    object_=emails, annotation=typing.Sequence[Email], direction="write"
                ),
                "fax": fax,
                "first_name": first_name,
                "id": id,
                "image": image,
                "industry": industry,
                "interaction_count": interaction_count,
                "last_activity_at": last_activity_at,
                "last_name": last_name,
                "name": name,
                "number_of_employees": number_of_employees,
                "owner_id": owner_id,
                "ownership": ownership,
                "parent_id": parent_id,
                "payee_number": payee_number,
                "phone_numbers": convert_and_respect_annotation_metadata(
                    object_=phone_numbers, annotation=typing.Sequence[PhoneNumber], direction="write"
                ),
                "read_only": read_only,
                "row_type": convert_and_respect_annotation_metadata(
                    object_=row_type, annotation=CompanyRowType, direction="write"
                ),
                "sales_tax_number": sales_tax_number,
                "salutation": salutation,
                "social_links": convert_and_respect_annotation_metadata(
                    object_=social_links, annotation=typing.Sequence[SocialLink], direction="write"
                ),
                "status": status,
                "tags": tags,
                "updated_at": updated_at,
                "updated_by": updated_by,
                "vat_number": vat_number,
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
                    CreateCompanyResponse,
                    parse_obj_as(
                        type_=CreateCompanyResponse,
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
    ) -> AsyncHttpResponse[GetCompanyResponse]:
        """
        Get company

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
        AsyncHttpResponse[GetCompanyResponse]
            Company
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/companies/{jsonable_encoder(id)}",
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
                    GetCompanyResponse,
                    parse_obj_as(
                        type_=GetCompanyResponse,
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
    ) -> AsyncHttpResponse[DeleteCompanyResponse]:
        """
        Delete company

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
        AsyncHttpResponse[DeleteCompanyResponse]
            Company deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/companies/{jsonable_encoder(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteCompanyResponse,
                    parse_obj_as(
                        type_=DeleteCompanyResponse,
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
        abn_branch: typing.Optional[str] = OMIT,
        abn_or_tfn: typing.Optional[str] = OMIT,
        acn: typing.Optional[str] = OMIT,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        annual_revenue: typing.Optional[str] = OMIT,
        bank_accounts: typing.Optional[typing.Sequence[BankAccount]] = OMIT,
        birthday: typing.Optional[dt.date] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        fax: typing.Optional[str] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        id: typing.Optional[str] = OMIT,
        image: typing.Optional[str] = OMIT,
        industry: typing.Optional[str] = OMIT,
        interaction_count: typing.Optional[int] = OMIT,
        last_activity_at: typing.Optional[dt.datetime] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        number_of_employees: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        ownership: typing.Optional[str] = OMIT,
        parent_id: typing.Optional[str] = OMIT,
        payee_number: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        row_type: typing.Optional[CompanyRowType] = OMIT,
        sales_tax_number: typing.Optional[str] = OMIT,
        salutation: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[SocialLink]] = OMIT,
        status: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        vat_number: typing.Optional[str] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateCompanyResponse]:
        """
        Update company

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        abn_branch : typing.Optional[str]
            An ABN Branch (also known as a GST Branch) is used if part of your business needs to account for GST separately from its parent entity.

        abn_or_tfn : typing.Optional[str]
            An ABN is necessary for operating a business, while a TFN (Tax File Number) is required for any person working in Australia.

        acn : typing.Optional[str]
            The Australian Company Number (ACN) is a nine digit number with the last digit being a check digit calculated using a modified modulus 10 calculation. ASIC has adopted a convention of always printing and displaying the ACN in the format XXX XXX XXX; three blocks of three characters, each block separated by a blank.

        addresses : typing.Optional[typing.Sequence[Address]]

        annual_revenue : typing.Optional[str]
            Annual revenue

        bank_accounts : typing.Optional[typing.Sequence[BankAccount]]

        birthday : typing.Optional[dt.date]
            The date of birth of the person.

        created_at : typing.Optional[dt.datetime]

        created_by : typing.Optional[str]

        currency : typing.Optional[Currency]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        deleted : typing.Optional[bool]

        description : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        fax : typing.Optional[str]

        first_name : typing.Optional[FirstName]

        id : typing.Optional[str]

        image : typing.Optional[str]

        industry : typing.Optional[str]
            Industry

        interaction_count : typing.Optional[int]

        last_activity_at : typing.Optional[dt.datetime]

        last_name : typing.Optional[LastName]

        number_of_employees : typing.Optional[str]
            Number of employees

        owner_id : typing.Optional[str]

        ownership : typing.Optional[str]
            Ownership

        parent_id : typing.Optional[str]
            Parent ID

        payee_number : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        read_only : typing.Optional[bool]

        row_type : typing.Optional[CompanyRowType]

        sales_tax_number : typing.Optional[str]

        salutation : typing.Optional[str]
            A formal salutation for the person. For example, 'Mr', 'Mrs'

        social_links : typing.Optional[typing.Sequence[SocialLink]]

        status : typing.Optional[str]

        tags : typing.Optional[Tags]

        updated_at : typing.Optional[dt.datetime]

        updated_by : typing.Optional[str]

        vat_number : typing.Optional[str]
            VAT number

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateCompanyResponse]
            Company updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/companies/{jsonable_encoder(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "abn_branch": abn_branch,
                "abn_or_tfn": abn_or_tfn,
                "acn": acn,
                "addresses": convert_and_respect_annotation_metadata(
                    object_=addresses, annotation=typing.Sequence[Address], direction="write"
                ),
                "annual_revenue": annual_revenue,
                "bank_accounts": convert_and_respect_annotation_metadata(
                    object_=bank_accounts, annotation=typing.Sequence[BankAccount], direction="write"
                ),
                "birthday": birthday,
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "custom_fields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=typing.Sequence[CustomField], direction="write"
                ),
                "deleted": deleted,
                "description": description,
                "emails": convert_and_respect_annotation_metadata(
                    object_=emails, annotation=typing.Sequence[Email], direction="write"
                ),
                "fax": fax,
                "first_name": first_name,
                "id": id,
                "image": image,
                "industry": industry,
                "interaction_count": interaction_count,
                "last_activity_at": last_activity_at,
                "last_name": last_name,
                "name": name,
                "number_of_employees": number_of_employees,
                "owner_id": owner_id,
                "ownership": ownership,
                "parent_id": parent_id,
                "payee_number": payee_number,
                "phone_numbers": convert_and_respect_annotation_metadata(
                    object_=phone_numbers, annotation=typing.Sequence[PhoneNumber], direction="write"
                ),
                "read_only": read_only,
                "row_type": convert_and_respect_annotation_metadata(
                    object_=row_type, annotation=CompanyRowType, direction="write"
                ),
                "sales_tax_number": sales_tax_number,
                "salutation": salutation,
                "social_links": convert_and_respect_annotation_metadata(
                    object_=social_links, annotation=typing.Sequence[SocialLink], direction="write"
                ),
                "status": status,
                "tags": tags,
                "updated_at": updated_at,
                "updated_by": updated_by,
                "vat_number": vat_number,
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
                    UpdateCompanyResponse,
                    parse_obj_as(
                        type_=UpdateCompanyResponse,
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
