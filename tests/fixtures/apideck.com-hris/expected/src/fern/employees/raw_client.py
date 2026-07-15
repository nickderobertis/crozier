

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
from ..types.company_id import CompanyId
from ..types.company_name import CompanyName
from ..types.create_employee_response import CreateEmployeeResponse
from ..types.created_at import CreatedAt
from ..types.created_by import CreatedBy
from ..types.custom_field import CustomField
from ..types.delete_employee_response import DeleteEmployeeResponse
from ..types.description import Description
from ..types.division import Division
from ..types.email import Email
from ..types.employee_compensations_item import EmployeeCompensationsItem
from ..types.employee_employment_role import EmployeeEmploymentRole
from ..types.employee_jobs_item import EmployeeJobsItem
from ..types.employee_leaving_reason import EmployeeLeavingReason
from ..types.employee_manager import EmployeeManager
from ..types.employee_number import EmployeeNumber
from ..types.employee_partner import EmployeePartner
from ..types.employee_social_links_item import EmployeeSocialLinksItem
from ..types.employee_team import EmployeeTeam
from ..types.employees_filter import EmployeesFilter
from ..types.employees_sort import EmployeesSort
from ..types.employment_status import EmploymentStatus
from ..types.first_name import FirstName
from ..types.gender import Gender
from ..types.get_employee_response import GetEmployeeResponse
from ..types.get_employees_response import GetEmployeesResponse
from ..types.id import Id
from ..types.language import Language
from ..types.last_name import LastName
from ..types.middle_name import MiddleName
from ..types.not_found_response import NotFoundResponse
from ..types.payment_required_response import PaymentRequiredResponse
from ..types.phone_number import PhoneNumber
from ..types.photo_url import PhotoUrl
from ..types.row_version import RowVersion
from ..types.title import Title
from ..types.unauthorized_response import UnauthorizedResponse
from ..types.unprocessable_response import UnprocessableResponse
from ..types.update_employee_response import UpdateEmployeeResponse
from ..types.updated_at import UpdatedAt
from ..types.updated_by import UpdatedBy


OMIT = typing.cast(typing.Any, ...)


class RawEmployeesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[EmployeesFilter] = None,
        sort: typing.Optional[EmployeesSort] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetEmployeesResponse]:
        """
        List Employees

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[EmployeesFilter]
            Apply filters

        sort : typing.Optional[EmployeesSort]
            Apply sorting

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetEmployeesResponse]
            Employees
        """
        _response = self._client_wrapper.httpx_client.request(
            "hris/employees",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=EmployeesFilter, direction="write"
                ),
                "sort": convert_and_respect_annotation_metadata(
                    object_=sort, annotation=EmployeesSort, direction="write"
                ),
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetEmployeesResponse,
                    parse_obj_as(
                        type_=GetEmployeesResponse,
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
        raw: typing.Optional[bool] = None,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        birthday: typing.Optional[dt.date] = OMIT,
        company_id: typing.Optional[CompanyId] = OMIT,
        company_name: typing.Optional[CompanyName] = OMIT,
        compensations: typing.Optional[typing.Sequence[EmployeeCompensationsItem]] = OMIT,
        country_of_birth: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        deceased_on: typing.Optional[dt.date] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        department: typing.Optional[str] = OMIT,
        department_id: typing.Optional[str] = OMIT,
        department_name: typing.Optional[str] = OMIT,
        description: typing.Optional[Description] = OMIT,
        dietary_preference: typing.Optional[str] = OMIT,
        direct_reports: typing.Optional[typing.Sequence[str]] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        division: typing.Optional[Division] = OMIT,
        division_id: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        employee_number: typing.Optional[EmployeeNumber] = OMIT,
        employment_end_date: typing.Optional[str] = OMIT,
        employment_role: typing.Optional[EmployeeEmploymentRole] = OMIT,
        employment_start_date: typing.Optional[str] = OMIT,
        employment_status: typing.Optional[EmploymentStatus] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        food_allergies: typing.Optional[typing.Sequence[str]] = OMIT,
        gender: typing.Optional[Gender] = OMIT,
        id: typing.Optional[Id] = OMIT,
        initials: typing.Optional[str] = OMIT,
        jobs: typing.Optional[typing.Sequence[EmployeeJobsItem]] = OMIT,
        languages: typing.Optional[typing.Sequence[typing.Optional[Language]]] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        leaving_reason: typing.Optional[EmployeeLeavingReason] = OMIT,
        manager: typing.Optional[EmployeeManager] = OMIT,
        marital_status: typing.Optional[str] = OMIT,
        middle_name: typing.Optional[MiddleName] = OMIT,
        nationalities: typing.Optional[typing.Sequence[typing.Optional[str]]] = OMIT,
        partner: typing.Optional[EmployeePartner] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        photo_url: typing.Optional[PhotoUrl] = OMIT,
        preferred_language: typing.Optional[Language] = OMIT,
        preferred_name: typing.Optional[str] = OMIT,
        pronouns: typing.Optional[str] = OMIT,
        record_url: typing.Optional[str] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        salutation: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[EmployeeSocialLinksItem]] = OMIT,
        social_security_number: typing.Optional[str] = OMIT,
        source: typing.Optional[str] = OMIT,
        source_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        tax_code: typing.Optional[str] = OMIT,
        tax_id: typing.Optional[str] = OMIT,
        team: typing.Optional[EmployeeTeam] = OMIT,
        timezone: typing.Optional[str] = OMIT,
        title: typing.Optional[Title] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        works_remote: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateEmployeeResponse]:
        """
        Create Employee

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        addresses : typing.Optional[typing.Sequence[Address]]

        birthday : typing.Optional[dt.date]
            The date of birth of the person.

        company_id : typing.Optional[CompanyId]

        company_name : typing.Optional[CompanyName]

        compensations : typing.Optional[typing.Sequence[EmployeeCompensationsItem]]

        country_of_birth : typing.Optional[str]
            Country code according to ISO 3166-1 alpha-2.

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        deceased_on : typing.Optional[dt.date]
            The date the person deceased.

        deleted : typing.Optional[bool]

        department : typing.Optional[str]
            The department the person is currently in. [Deprecated](https://developers.apideck.com/changelog) in favor of the dedicated department_id and department_name field.

        department_id : typing.Optional[str]
            Unique identifier of the department ID this employee belongs to.

        department_name : typing.Optional[str]
            Name of the department this employee belongs to.

        description : typing.Optional[Description]

        dietary_preference : typing.Optional[str]
            Indicate the employee's dietary preference.

        direct_reports : typing.Optional[typing.Sequence[str]]
            The direct reports refer to the individuals who report directly to a person in the organizational hierarchy.

        display_name : typing.Optional[str]
            The name used to display the employee, often a combination of their first and last names.

        division : typing.Optional[Division]

        division_id : typing.Optional[str]
            Unique identifier of the division this employee belongs to.

        emails : typing.Optional[typing.Sequence[Email]]

        employee_number : typing.Optional[EmployeeNumber]

        employment_end_date : typing.Optional[str]
            An End Date is the date that the employee ended working at the company

        employment_role : typing.Optional[EmployeeEmploymentRole]

        employment_start_date : typing.Optional[str]
            A Start Date is the date that the employee started working at the company

        employment_status : typing.Optional[EmploymentStatus]

        first_name : typing.Optional[FirstName]

        food_allergies : typing.Optional[typing.Sequence[str]]
            Indicate the employee's food allergies.

        gender : typing.Optional[Gender]

        id : typing.Optional[Id]

        initials : typing.Optional[str]
            The initials of the person, usually derived from their first, middle, and last names.

        jobs : typing.Optional[typing.Sequence[EmployeeJobsItem]]

        languages : typing.Optional[typing.Sequence[typing.Optional[Language]]]

        last_name : typing.Optional[LastName]

        leaving_reason : typing.Optional[EmployeeLeavingReason]
            The reason because the employment ended.

        manager : typing.Optional[EmployeeManager]

        marital_status : typing.Optional[str]
            The marital status of the employee.

        middle_name : typing.Optional[MiddleName]

        nationalities : typing.Optional[typing.Sequence[typing.Optional[str]]]

        partner : typing.Optional[EmployeePartner]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        photo_url : typing.Optional[PhotoUrl]

        preferred_language : typing.Optional[Language]

        preferred_name : typing.Optional[str]
            The name the employee prefers to be addressed by, which may be different from their legal name.

        pronouns : typing.Optional[str]
            The preferred pronouns of the person.

        record_url : typing.Optional[str]

        row_version : typing.Optional[RowVersion]

        salutation : typing.Optional[str]
            A formal salutation for the person. For example, 'Mr', 'Mrs'

        social_links : typing.Optional[typing.Sequence[EmployeeSocialLinksItem]]

        social_security_number : typing.Optional[str]
            A unique identifier assigned by the government. This field is considered sensitive information and may be subject to special security and privacy restrictions.

        source : typing.Optional[str]
            When the employee is imported as a new hire, this field indicates what system (e.g. the name of the ATS) this employee was imported from.

        source_id : typing.Optional[str]
            Unique identifier of the employee in the system this employee was imported from (e.g. the ID in the ATS).

        tags : typing.Optional[typing.Sequence[str]]

        tax_code : typing.Optional[str]

        tax_id : typing.Optional[str]

        team : typing.Optional[EmployeeTeam]
            The team the person is currently in.

        timezone : typing.Optional[str]
            The time zone related to the resource. The value is a string containing a standard time zone identifier, e.g. Europe/London.

        title : typing.Optional[Title]

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        works_remote : typing.Optional[bool]
            Indicates if the employee works from a remote location.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateEmployeeResponse]
            Employees
        """
        _response = self._client_wrapper.httpx_client.request(
            "hris/employees",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "addresses": convert_and_respect_annotation_metadata(
                    object_=addresses, annotation=typing.Sequence[Address], direction="write"
                ),
                "birthday": birthday,
                "company_id": company_id,
                "company_name": company_name,
                "compensations": convert_and_respect_annotation_metadata(
                    object_=compensations, annotation=typing.Sequence[EmployeeCompensationsItem], direction="write"
                ),
                "country_of_birth": country_of_birth,
                "created_at": created_at,
                "created_by": created_by,
                "custom_fields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=typing.Sequence[CustomField], direction="write"
                ),
                "deceased_on": deceased_on,
                "deleted": deleted,
                "department": department,
                "department_id": department_id,
                "department_name": department_name,
                "description": description,
                "dietary_preference": dietary_preference,
                "direct_reports": direct_reports,
                "display_name": display_name,
                "division": division,
                "division_id": division_id,
                "emails": convert_and_respect_annotation_metadata(
                    object_=emails, annotation=typing.Sequence[Email], direction="write"
                ),
                "employee_number": employee_number,
                "employment_end_date": employment_end_date,
                "employment_role": convert_and_respect_annotation_metadata(
                    object_=employment_role, annotation=EmployeeEmploymentRole, direction="write"
                ),
                "employment_start_date": employment_start_date,
                "employment_status": employment_status,
                "first_name": first_name,
                "food_allergies": food_allergies,
                "gender": gender,
                "id": id,
                "initials": initials,
                "jobs": convert_and_respect_annotation_metadata(
                    object_=jobs, annotation=typing.Sequence[EmployeeJobsItem], direction="write"
                ),
                "languages": languages,
                "last_name": last_name,
                "leaving_reason": leaving_reason,
                "manager": convert_and_respect_annotation_metadata(
                    object_=manager, annotation=EmployeeManager, direction="write"
                ),
                "marital_status": marital_status,
                "middle_name": middle_name,
                "nationalities": nationalities,
                "partner": convert_and_respect_annotation_metadata(
                    object_=partner, annotation=EmployeePartner, direction="write"
                ),
                "phone_numbers": convert_and_respect_annotation_metadata(
                    object_=phone_numbers, annotation=typing.Sequence[PhoneNumber], direction="write"
                ),
                "photo_url": photo_url,
                "preferred_language": preferred_language,
                "preferred_name": preferred_name,
                "pronouns": pronouns,
                "record_url": record_url,
                "row_version": row_version,
                "salutation": salutation,
                "social_links": convert_and_respect_annotation_metadata(
                    object_=social_links, annotation=typing.Sequence[EmployeeSocialLinksItem], direction="write"
                ),
                "social_security_number": social_security_number,
                "source": source,
                "source_id": source_id,
                "tags": tags,
                "tax_code": tax_code,
                "tax_id": tax_id,
                "team": convert_and_respect_annotation_metadata(
                    object_=team, annotation=typing.Optional[EmployeeTeam], direction="write"
                ),
                "timezone": timezone,
                "title": title,
                "updated_at": updated_at,
                "updated_by": updated_by,
                "works_remote": works_remote,
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
                    CreateEmployeeResponse,
                    parse_obj_as(
                        type_=CreateEmployeeResponse,
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
    ) -> HttpResponse[GetEmployeeResponse]:
        """
        Get Employee

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
        HttpResponse[GetEmployeeResponse]
            Employees
        """
        _response = self._client_wrapper.httpx_client.request(
            f"hris/employees/{jsonable_encoder(id)}",
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
                    GetEmployeeResponse,
                    parse_obj_as(
                        type_=GetEmployeeResponse,
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
    ) -> HttpResponse[DeleteEmployeeResponse]:
        """
        Delete Employee

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
        HttpResponse[DeleteEmployeeResponse]
            Employees
        """
        _response = self._client_wrapper.httpx_client.request(
            f"hris/employees/{jsonable_encoder(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteEmployeeResponse,
                    parse_obj_as(
                        type_=DeleteEmployeeResponse,
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
        raw: typing.Optional[bool] = None,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        birthday: typing.Optional[dt.date] = OMIT,
        company_id: typing.Optional[CompanyId] = OMIT,
        company_name: typing.Optional[CompanyName] = OMIT,
        compensations: typing.Optional[typing.Sequence[EmployeeCompensationsItem]] = OMIT,
        country_of_birth: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        deceased_on: typing.Optional[dt.date] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        department: typing.Optional[str] = OMIT,
        department_id: typing.Optional[str] = OMIT,
        department_name: typing.Optional[str] = OMIT,
        description: typing.Optional[Description] = OMIT,
        dietary_preference: typing.Optional[str] = OMIT,
        direct_reports: typing.Optional[typing.Sequence[str]] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        division: typing.Optional[Division] = OMIT,
        division_id: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        employee_number: typing.Optional[EmployeeNumber] = OMIT,
        employment_end_date: typing.Optional[str] = OMIT,
        employment_role: typing.Optional[EmployeeEmploymentRole] = OMIT,
        employment_start_date: typing.Optional[str] = OMIT,
        employment_status: typing.Optional[EmploymentStatus] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        food_allergies: typing.Optional[typing.Sequence[str]] = OMIT,
        gender: typing.Optional[Gender] = OMIT,
        id: typing.Optional[Id] = OMIT,
        initials: typing.Optional[str] = OMIT,
        jobs: typing.Optional[typing.Sequence[EmployeeJobsItem]] = OMIT,
        languages: typing.Optional[typing.Sequence[typing.Optional[Language]]] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        leaving_reason: typing.Optional[EmployeeLeavingReason] = OMIT,
        manager: typing.Optional[EmployeeManager] = OMIT,
        marital_status: typing.Optional[str] = OMIT,
        middle_name: typing.Optional[MiddleName] = OMIT,
        nationalities: typing.Optional[typing.Sequence[typing.Optional[str]]] = OMIT,
        partner: typing.Optional[EmployeePartner] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        photo_url: typing.Optional[PhotoUrl] = OMIT,
        preferred_language: typing.Optional[Language] = OMIT,
        preferred_name: typing.Optional[str] = OMIT,
        pronouns: typing.Optional[str] = OMIT,
        record_url: typing.Optional[str] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        salutation: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[EmployeeSocialLinksItem]] = OMIT,
        social_security_number: typing.Optional[str] = OMIT,
        source: typing.Optional[str] = OMIT,
        source_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        tax_code: typing.Optional[str] = OMIT,
        tax_id: typing.Optional[str] = OMIT,
        team: typing.Optional[EmployeeTeam] = OMIT,
        timezone: typing.Optional[str] = OMIT,
        title: typing.Optional[Title] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        works_remote: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateEmployeeResponse]:
        """
        Update Employee

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        addresses : typing.Optional[typing.Sequence[Address]]

        birthday : typing.Optional[dt.date]
            The date of birth of the person.

        company_id : typing.Optional[CompanyId]

        company_name : typing.Optional[CompanyName]

        compensations : typing.Optional[typing.Sequence[EmployeeCompensationsItem]]

        country_of_birth : typing.Optional[str]
            Country code according to ISO 3166-1 alpha-2.

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        deceased_on : typing.Optional[dt.date]
            The date the person deceased.

        deleted : typing.Optional[bool]

        department : typing.Optional[str]
            The department the person is currently in. [Deprecated](https://developers.apideck.com/changelog) in favor of the dedicated department_id and department_name field.

        department_id : typing.Optional[str]
            Unique identifier of the department ID this employee belongs to.

        department_name : typing.Optional[str]
            Name of the department this employee belongs to.

        description : typing.Optional[Description]

        dietary_preference : typing.Optional[str]
            Indicate the employee's dietary preference.

        direct_reports : typing.Optional[typing.Sequence[str]]
            The direct reports refer to the individuals who report directly to a person in the organizational hierarchy.

        display_name : typing.Optional[str]
            The name used to display the employee, often a combination of their first and last names.

        division : typing.Optional[Division]

        division_id : typing.Optional[str]
            Unique identifier of the division this employee belongs to.

        emails : typing.Optional[typing.Sequence[Email]]

        employee_number : typing.Optional[EmployeeNumber]

        employment_end_date : typing.Optional[str]
            An End Date is the date that the employee ended working at the company

        employment_role : typing.Optional[EmployeeEmploymentRole]

        employment_start_date : typing.Optional[str]
            A Start Date is the date that the employee started working at the company

        employment_status : typing.Optional[EmploymentStatus]

        first_name : typing.Optional[FirstName]

        food_allergies : typing.Optional[typing.Sequence[str]]
            Indicate the employee's food allergies.

        gender : typing.Optional[Gender]

        id : typing.Optional[Id]

        initials : typing.Optional[str]
            The initials of the person, usually derived from their first, middle, and last names.

        jobs : typing.Optional[typing.Sequence[EmployeeJobsItem]]

        languages : typing.Optional[typing.Sequence[typing.Optional[Language]]]

        last_name : typing.Optional[LastName]

        leaving_reason : typing.Optional[EmployeeLeavingReason]
            The reason because the employment ended.

        manager : typing.Optional[EmployeeManager]

        marital_status : typing.Optional[str]
            The marital status of the employee.

        middle_name : typing.Optional[MiddleName]

        nationalities : typing.Optional[typing.Sequence[typing.Optional[str]]]

        partner : typing.Optional[EmployeePartner]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        photo_url : typing.Optional[PhotoUrl]

        preferred_language : typing.Optional[Language]

        preferred_name : typing.Optional[str]
            The name the employee prefers to be addressed by, which may be different from their legal name.

        pronouns : typing.Optional[str]
            The preferred pronouns of the person.

        record_url : typing.Optional[str]

        row_version : typing.Optional[RowVersion]

        salutation : typing.Optional[str]
            A formal salutation for the person. For example, 'Mr', 'Mrs'

        social_links : typing.Optional[typing.Sequence[EmployeeSocialLinksItem]]

        social_security_number : typing.Optional[str]
            A unique identifier assigned by the government. This field is considered sensitive information and may be subject to special security and privacy restrictions.

        source : typing.Optional[str]
            When the employee is imported as a new hire, this field indicates what system (e.g. the name of the ATS) this employee was imported from.

        source_id : typing.Optional[str]
            Unique identifier of the employee in the system this employee was imported from (e.g. the ID in the ATS).

        tags : typing.Optional[typing.Sequence[str]]

        tax_code : typing.Optional[str]

        tax_id : typing.Optional[str]

        team : typing.Optional[EmployeeTeam]
            The team the person is currently in.

        timezone : typing.Optional[str]
            The time zone related to the resource. The value is a string containing a standard time zone identifier, e.g. Europe/London.

        title : typing.Optional[Title]

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        works_remote : typing.Optional[bool]
            Indicates if the employee works from a remote location.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateEmployeeResponse]
            Employees
        """
        _response = self._client_wrapper.httpx_client.request(
            f"hris/employees/{jsonable_encoder(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "addresses": convert_and_respect_annotation_metadata(
                    object_=addresses, annotation=typing.Sequence[Address], direction="write"
                ),
                "birthday": birthday,
                "company_id": company_id,
                "company_name": company_name,
                "compensations": convert_and_respect_annotation_metadata(
                    object_=compensations, annotation=typing.Sequence[EmployeeCompensationsItem], direction="write"
                ),
                "country_of_birth": country_of_birth,
                "created_at": created_at,
                "created_by": created_by,
                "custom_fields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=typing.Sequence[CustomField], direction="write"
                ),
                "deceased_on": deceased_on,
                "deleted": deleted,
                "department": department,
                "department_id": department_id,
                "department_name": department_name,
                "description": description,
                "dietary_preference": dietary_preference,
                "direct_reports": direct_reports,
                "display_name": display_name,
                "division": division,
                "division_id": division_id,
                "emails": convert_and_respect_annotation_metadata(
                    object_=emails, annotation=typing.Sequence[Email], direction="write"
                ),
                "employee_number": employee_number,
                "employment_end_date": employment_end_date,
                "employment_role": convert_and_respect_annotation_metadata(
                    object_=employment_role, annotation=EmployeeEmploymentRole, direction="write"
                ),
                "employment_start_date": employment_start_date,
                "employment_status": employment_status,
                "first_name": first_name,
                "food_allergies": food_allergies,
                "gender": gender,
                "id": id,
                "initials": initials,
                "jobs": convert_and_respect_annotation_metadata(
                    object_=jobs, annotation=typing.Sequence[EmployeeJobsItem], direction="write"
                ),
                "languages": languages,
                "last_name": last_name,
                "leaving_reason": leaving_reason,
                "manager": convert_and_respect_annotation_metadata(
                    object_=manager, annotation=EmployeeManager, direction="write"
                ),
                "marital_status": marital_status,
                "middle_name": middle_name,
                "nationalities": nationalities,
                "partner": convert_and_respect_annotation_metadata(
                    object_=partner, annotation=EmployeePartner, direction="write"
                ),
                "phone_numbers": convert_and_respect_annotation_metadata(
                    object_=phone_numbers, annotation=typing.Sequence[PhoneNumber], direction="write"
                ),
                "photo_url": photo_url,
                "preferred_language": preferred_language,
                "preferred_name": preferred_name,
                "pronouns": pronouns,
                "record_url": record_url,
                "row_version": row_version,
                "salutation": salutation,
                "social_links": convert_and_respect_annotation_metadata(
                    object_=social_links, annotation=typing.Sequence[EmployeeSocialLinksItem], direction="write"
                ),
                "social_security_number": social_security_number,
                "source": source,
                "source_id": source_id,
                "tags": tags,
                "tax_code": tax_code,
                "tax_id": tax_id,
                "team": convert_and_respect_annotation_metadata(
                    object_=team, annotation=typing.Optional[EmployeeTeam], direction="write"
                ),
                "timezone": timezone,
                "title": title,
                "updated_at": updated_at,
                "updated_by": updated_by,
                "works_remote": works_remote,
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
                    UpdateEmployeeResponse,
                    parse_obj_as(
                        type_=UpdateEmployeeResponse,
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


class AsyncRawEmployeesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[EmployeesFilter] = None,
        sort: typing.Optional[EmployeesSort] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetEmployeesResponse]:
        """
        List Employees

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[EmployeesFilter]
            Apply filters

        sort : typing.Optional[EmployeesSort]
            Apply sorting

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetEmployeesResponse]
            Employees
        """
        _response = await self._client_wrapper.httpx_client.request(
            "hris/employees",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=EmployeesFilter, direction="write"
                ),
                "sort": convert_and_respect_annotation_metadata(
                    object_=sort, annotation=EmployeesSort, direction="write"
                ),
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetEmployeesResponse,
                    parse_obj_as(
                        type_=GetEmployeesResponse,
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
        raw: typing.Optional[bool] = None,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        birthday: typing.Optional[dt.date] = OMIT,
        company_id: typing.Optional[CompanyId] = OMIT,
        company_name: typing.Optional[CompanyName] = OMIT,
        compensations: typing.Optional[typing.Sequence[EmployeeCompensationsItem]] = OMIT,
        country_of_birth: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        deceased_on: typing.Optional[dt.date] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        department: typing.Optional[str] = OMIT,
        department_id: typing.Optional[str] = OMIT,
        department_name: typing.Optional[str] = OMIT,
        description: typing.Optional[Description] = OMIT,
        dietary_preference: typing.Optional[str] = OMIT,
        direct_reports: typing.Optional[typing.Sequence[str]] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        division: typing.Optional[Division] = OMIT,
        division_id: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        employee_number: typing.Optional[EmployeeNumber] = OMIT,
        employment_end_date: typing.Optional[str] = OMIT,
        employment_role: typing.Optional[EmployeeEmploymentRole] = OMIT,
        employment_start_date: typing.Optional[str] = OMIT,
        employment_status: typing.Optional[EmploymentStatus] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        food_allergies: typing.Optional[typing.Sequence[str]] = OMIT,
        gender: typing.Optional[Gender] = OMIT,
        id: typing.Optional[Id] = OMIT,
        initials: typing.Optional[str] = OMIT,
        jobs: typing.Optional[typing.Sequence[EmployeeJobsItem]] = OMIT,
        languages: typing.Optional[typing.Sequence[typing.Optional[Language]]] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        leaving_reason: typing.Optional[EmployeeLeavingReason] = OMIT,
        manager: typing.Optional[EmployeeManager] = OMIT,
        marital_status: typing.Optional[str] = OMIT,
        middle_name: typing.Optional[MiddleName] = OMIT,
        nationalities: typing.Optional[typing.Sequence[typing.Optional[str]]] = OMIT,
        partner: typing.Optional[EmployeePartner] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        photo_url: typing.Optional[PhotoUrl] = OMIT,
        preferred_language: typing.Optional[Language] = OMIT,
        preferred_name: typing.Optional[str] = OMIT,
        pronouns: typing.Optional[str] = OMIT,
        record_url: typing.Optional[str] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        salutation: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[EmployeeSocialLinksItem]] = OMIT,
        social_security_number: typing.Optional[str] = OMIT,
        source: typing.Optional[str] = OMIT,
        source_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        tax_code: typing.Optional[str] = OMIT,
        tax_id: typing.Optional[str] = OMIT,
        team: typing.Optional[EmployeeTeam] = OMIT,
        timezone: typing.Optional[str] = OMIT,
        title: typing.Optional[Title] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        works_remote: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateEmployeeResponse]:
        """
        Create Employee

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        addresses : typing.Optional[typing.Sequence[Address]]

        birthday : typing.Optional[dt.date]
            The date of birth of the person.

        company_id : typing.Optional[CompanyId]

        company_name : typing.Optional[CompanyName]

        compensations : typing.Optional[typing.Sequence[EmployeeCompensationsItem]]

        country_of_birth : typing.Optional[str]
            Country code according to ISO 3166-1 alpha-2.

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        deceased_on : typing.Optional[dt.date]
            The date the person deceased.

        deleted : typing.Optional[bool]

        department : typing.Optional[str]
            The department the person is currently in. [Deprecated](https://developers.apideck.com/changelog) in favor of the dedicated department_id and department_name field.

        department_id : typing.Optional[str]
            Unique identifier of the department ID this employee belongs to.

        department_name : typing.Optional[str]
            Name of the department this employee belongs to.

        description : typing.Optional[Description]

        dietary_preference : typing.Optional[str]
            Indicate the employee's dietary preference.

        direct_reports : typing.Optional[typing.Sequence[str]]
            The direct reports refer to the individuals who report directly to a person in the organizational hierarchy.

        display_name : typing.Optional[str]
            The name used to display the employee, often a combination of their first and last names.

        division : typing.Optional[Division]

        division_id : typing.Optional[str]
            Unique identifier of the division this employee belongs to.

        emails : typing.Optional[typing.Sequence[Email]]

        employee_number : typing.Optional[EmployeeNumber]

        employment_end_date : typing.Optional[str]
            An End Date is the date that the employee ended working at the company

        employment_role : typing.Optional[EmployeeEmploymentRole]

        employment_start_date : typing.Optional[str]
            A Start Date is the date that the employee started working at the company

        employment_status : typing.Optional[EmploymentStatus]

        first_name : typing.Optional[FirstName]

        food_allergies : typing.Optional[typing.Sequence[str]]
            Indicate the employee's food allergies.

        gender : typing.Optional[Gender]

        id : typing.Optional[Id]

        initials : typing.Optional[str]
            The initials of the person, usually derived from their first, middle, and last names.

        jobs : typing.Optional[typing.Sequence[EmployeeJobsItem]]

        languages : typing.Optional[typing.Sequence[typing.Optional[Language]]]

        last_name : typing.Optional[LastName]

        leaving_reason : typing.Optional[EmployeeLeavingReason]
            The reason because the employment ended.

        manager : typing.Optional[EmployeeManager]

        marital_status : typing.Optional[str]
            The marital status of the employee.

        middle_name : typing.Optional[MiddleName]

        nationalities : typing.Optional[typing.Sequence[typing.Optional[str]]]

        partner : typing.Optional[EmployeePartner]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        photo_url : typing.Optional[PhotoUrl]

        preferred_language : typing.Optional[Language]

        preferred_name : typing.Optional[str]
            The name the employee prefers to be addressed by, which may be different from their legal name.

        pronouns : typing.Optional[str]
            The preferred pronouns of the person.

        record_url : typing.Optional[str]

        row_version : typing.Optional[RowVersion]

        salutation : typing.Optional[str]
            A formal salutation for the person. For example, 'Mr', 'Mrs'

        social_links : typing.Optional[typing.Sequence[EmployeeSocialLinksItem]]

        social_security_number : typing.Optional[str]
            A unique identifier assigned by the government. This field is considered sensitive information and may be subject to special security and privacy restrictions.

        source : typing.Optional[str]
            When the employee is imported as a new hire, this field indicates what system (e.g. the name of the ATS) this employee was imported from.

        source_id : typing.Optional[str]
            Unique identifier of the employee in the system this employee was imported from (e.g. the ID in the ATS).

        tags : typing.Optional[typing.Sequence[str]]

        tax_code : typing.Optional[str]

        tax_id : typing.Optional[str]

        team : typing.Optional[EmployeeTeam]
            The team the person is currently in.

        timezone : typing.Optional[str]
            The time zone related to the resource. The value is a string containing a standard time zone identifier, e.g. Europe/London.

        title : typing.Optional[Title]

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        works_remote : typing.Optional[bool]
            Indicates if the employee works from a remote location.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateEmployeeResponse]
            Employees
        """
        _response = await self._client_wrapper.httpx_client.request(
            "hris/employees",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "addresses": convert_and_respect_annotation_metadata(
                    object_=addresses, annotation=typing.Sequence[Address], direction="write"
                ),
                "birthday": birthday,
                "company_id": company_id,
                "company_name": company_name,
                "compensations": convert_and_respect_annotation_metadata(
                    object_=compensations, annotation=typing.Sequence[EmployeeCompensationsItem], direction="write"
                ),
                "country_of_birth": country_of_birth,
                "created_at": created_at,
                "created_by": created_by,
                "custom_fields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=typing.Sequence[CustomField], direction="write"
                ),
                "deceased_on": deceased_on,
                "deleted": deleted,
                "department": department,
                "department_id": department_id,
                "department_name": department_name,
                "description": description,
                "dietary_preference": dietary_preference,
                "direct_reports": direct_reports,
                "display_name": display_name,
                "division": division,
                "division_id": division_id,
                "emails": convert_and_respect_annotation_metadata(
                    object_=emails, annotation=typing.Sequence[Email], direction="write"
                ),
                "employee_number": employee_number,
                "employment_end_date": employment_end_date,
                "employment_role": convert_and_respect_annotation_metadata(
                    object_=employment_role, annotation=EmployeeEmploymentRole, direction="write"
                ),
                "employment_start_date": employment_start_date,
                "employment_status": employment_status,
                "first_name": first_name,
                "food_allergies": food_allergies,
                "gender": gender,
                "id": id,
                "initials": initials,
                "jobs": convert_and_respect_annotation_metadata(
                    object_=jobs, annotation=typing.Sequence[EmployeeJobsItem], direction="write"
                ),
                "languages": languages,
                "last_name": last_name,
                "leaving_reason": leaving_reason,
                "manager": convert_and_respect_annotation_metadata(
                    object_=manager, annotation=EmployeeManager, direction="write"
                ),
                "marital_status": marital_status,
                "middle_name": middle_name,
                "nationalities": nationalities,
                "partner": convert_and_respect_annotation_metadata(
                    object_=partner, annotation=EmployeePartner, direction="write"
                ),
                "phone_numbers": convert_and_respect_annotation_metadata(
                    object_=phone_numbers, annotation=typing.Sequence[PhoneNumber], direction="write"
                ),
                "photo_url": photo_url,
                "preferred_language": preferred_language,
                "preferred_name": preferred_name,
                "pronouns": pronouns,
                "record_url": record_url,
                "row_version": row_version,
                "salutation": salutation,
                "social_links": convert_and_respect_annotation_metadata(
                    object_=social_links, annotation=typing.Sequence[EmployeeSocialLinksItem], direction="write"
                ),
                "social_security_number": social_security_number,
                "source": source,
                "source_id": source_id,
                "tags": tags,
                "tax_code": tax_code,
                "tax_id": tax_id,
                "team": convert_and_respect_annotation_metadata(
                    object_=team, annotation=typing.Optional[EmployeeTeam], direction="write"
                ),
                "timezone": timezone,
                "title": title,
                "updated_at": updated_at,
                "updated_by": updated_by,
                "works_remote": works_remote,
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
                    CreateEmployeeResponse,
                    parse_obj_as(
                        type_=CreateEmployeeResponse,
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
    ) -> AsyncHttpResponse[GetEmployeeResponse]:
        """
        Get Employee

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
        AsyncHttpResponse[GetEmployeeResponse]
            Employees
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"hris/employees/{jsonable_encoder(id)}",
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
                    GetEmployeeResponse,
                    parse_obj_as(
                        type_=GetEmployeeResponse,
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
    ) -> AsyncHttpResponse[DeleteEmployeeResponse]:
        """
        Delete Employee

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
        AsyncHttpResponse[DeleteEmployeeResponse]
            Employees
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"hris/employees/{jsonable_encoder(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteEmployeeResponse,
                    parse_obj_as(
                        type_=DeleteEmployeeResponse,
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
        raw: typing.Optional[bool] = None,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        birthday: typing.Optional[dt.date] = OMIT,
        company_id: typing.Optional[CompanyId] = OMIT,
        company_name: typing.Optional[CompanyName] = OMIT,
        compensations: typing.Optional[typing.Sequence[EmployeeCompensationsItem]] = OMIT,
        country_of_birth: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        deceased_on: typing.Optional[dt.date] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        department: typing.Optional[str] = OMIT,
        department_id: typing.Optional[str] = OMIT,
        department_name: typing.Optional[str] = OMIT,
        description: typing.Optional[Description] = OMIT,
        dietary_preference: typing.Optional[str] = OMIT,
        direct_reports: typing.Optional[typing.Sequence[str]] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        division: typing.Optional[Division] = OMIT,
        division_id: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        employee_number: typing.Optional[EmployeeNumber] = OMIT,
        employment_end_date: typing.Optional[str] = OMIT,
        employment_role: typing.Optional[EmployeeEmploymentRole] = OMIT,
        employment_start_date: typing.Optional[str] = OMIT,
        employment_status: typing.Optional[EmploymentStatus] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        food_allergies: typing.Optional[typing.Sequence[str]] = OMIT,
        gender: typing.Optional[Gender] = OMIT,
        id: typing.Optional[Id] = OMIT,
        initials: typing.Optional[str] = OMIT,
        jobs: typing.Optional[typing.Sequence[EmployeeJobsItem]] = OMIT,
        languages: typing.Optional[typing.Sequence[typing.Optional[Language]]] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        leaving_reason: typing.Optional[EmployeeLeavingReason] = OMIT,
        manager: typing.Optional[EmployeeManager] = OMIT,
        marital_status: typing.Optional[str] = OMIT,
        middle_name: typing.Optional[MiddleName] = OMIT,
        nationalities: typing.Optional[typing.Sequence[typing.Optional[str]]] = OMIT,
        partner: typing.Optional[EmployeePartner] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        photo_url: typing.Optional[PhotoUrl] = OMIT,
        preferred_language: typing.Optional[Language] = OMIT,
        preferred_name: typing.Optional[str] = OMIT,
        pronouns: typing.Optional[str] = OMIT,
        record_url: typing.Optional[str] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        salutation: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[EmployeeSocialLinksItem]] = OMIT,
        social_security_number: typing.Optional[str] = OMIT,
        source: typing.Optional[str] = OMIT,
        source_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        tax_code: typing.Optional[str] = OMIT,
        tax_id: typing.Optional[str] = OMIT,
        team: typing.Optional[EmployeeTeam] = OMIT,
        timezone: typing.Optional[str] = OMIT,
        title: typing.Optional[Title] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        works_remote: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateEmployeeResponse]:
        """
        Update Employee

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        addresses : typing.Optional[typing.Sequence[Address]]

        birthday : typing.Optional[dt.date]
            The date of birth of the person.

        company_id : typing.Optional[CompanyId]

        company_name : typing.Optional[CompanyName]

        compensations : typing.Optional[typing.Sequence[EmployeeCompensationsItem]]

        country_of_birth : typing.Optional[str]
            Country code according to ISO 3166-1 alpha-2.

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        deceased_on : typing.Optional[dt.date]
            The date the person deceased.

        deleted : typing.Optional[bool]

        department : typing.Optional[str]
            The department the person is currently in. [Deprecated](https://developers.apideck.com/changelog) in favor of the dedicated department_id and department_name field.

        department_id : typing.Optional[str]
            Unique identifier of the department ID this employee belongs to.

        department_name : typing.Optional[str]
            Name of the department this employee belongs to.

        description : typing.Optional[Description]

        dietary_preference : typing.Optional[str]
            Indicate the employee's dietary preference.

        direct_reports : typing.Optional[typing.Sequence[str]]
            The direct reports refer to the individuals who report directly to a person in the organizational hierarchy.

        display_name : typing.Optional[str]
            The name used to display the employee, often a combination of their first and last names.

        division : typing.Optional[Division]

        division_id : typing.Optional[str]
            Unique identifier of the division this employee belongs to.

        emails : typing.Optional[typing.Sequence[Email]]

        employee_number : typing.Optional[EmployeeNumber]

        employment_end_date : typing.Optional[str]
            An End Date is the date that the employee ended working at the company

        employment_role : typing.Optional[EmployeeEmploymentRole]

        employment_start_date : typing.Optional[str]
            A Start Date is the date that the employee started working at the company

        employment_status : typing.Optional[EmploymentStatus]

        first_name : typing.Optional[FirstName]

        food_allergies : typing.Optional[typing.Sequence[str]]
            Indicate the employee's food allergies.

        gender : typing.Optional[Gender]

        id : typing.Optional[Id]

        initials : typing.Optional[str]
            The initials of the person, usually derived from their first, middle, and last names.

        jobs : typing.Optional[typing.Sequence[EmployeeJobsItem]]

        languages : typing.Optional[typing.Sequence[typing.Optional[Language]]]

        last_name : typing.Optional[LastName]

        leaving_reason : typing.Optional[EmployeeLeavingReason]
            The reason because the employment ended.

        manager : typing.Optional[EmployeeManager]

        marital_status : typing.Optional[str]
            The marital status of the employee.

        middle_name : typing.Optional[MiddleName]

        nationalities : typing.Optional[typing.Sequence[typing.Optional[str]]]

        partner : typing.Optional[EmployeePartner]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        photo_url : typing.Optional[PhotoUrl]

        preferred_language : typing.Optional[Language]

        preferred_name : typing.Optional[str]
            The name the employee prefers to be addressed by, which may be different from their legal name.

        pronouns : typing.Optional[str]
            The preferred pronouns of the person.

        record_url : typing.Optional[str]

        row_version : typing.Optional[RowVersion]

        salutation : typing.Optional[str]
            A formal salutation for the person. For example, 'Mr', 'Mrs'

        social_links : typing.Optional[typing.Sequence[EmployeeSocialLinksItem]]

        social_security_number : typing.Optional[str]
            A unique identifier assigned by the government. This field is considered sensitive information and may be subject to special security and privacy restrictions.

        source : typing.Optional[str]
            When the employee is imported as a new hire, this field indicates what system (e.g. the name of the ATS) this employee was imported from.

        source_id : typing.Optional[str]
            Unique identifier of the employee in the system this employee was imported from (e.g. the ID in the ATS).

        tags : typing.Optional[typing.Sequence[str]]

        tax_code : typing.Optional[str]

        tax_id : typing.Optional[str]

        team : typing.Optional[EmployeeTeam]
            The team the person is currently in.

        timezone : typing.Optional[str]
            The time zone related to the resource. The value is a string containing a standard time zone identifier, e.g. Europe/London.

        title : typing.Optional[Title]

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        works_remote : typing.Optional[bool]
            Indicates if the employee works from a remote location.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateEmployeeResponse]
            Employees
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"hris/employees/{jsonable_encoder(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "addresses": convert_and_respect_annotation_metadata(
                    object_=addresses, annotation=typing.Sequence[Address], direction="write"
                ),
                "birthday": birthday,
                "company_id": company_id,
                "company_name": company_name,
                "compensations": convert_and_respect_annotation_metadata(
                    object_=compensations, annotation=typing.Sequence[EmployeeCompensationsItem], direction="write"
                ),
                "country_of_birth": country_of_birth,
                "created_at": created_at,
                "created_by": created_by,
                "custom_fields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=typing.Sequence[CustomField], direction="write"
                ),
                "deceased_on": deceased_on,
                "deleted": deleted,
                "department": department,
                "department_id": department_id,
                "department_name": department_name,
                "description": description,
                "dietary_preference": dietary_preference,
                "direct_reports": direct_reports,
                "display_name": display_name,
                "division": division,
                "division_id": division_id,
                "emails": convert_and_respect_annotation_metadata(
                    object_=emails, annotation=typing.Sequence[Email], direction="write"
                ),
                "employee_number": employee_number,
                "employment_end_date": employment_end_date,
                "employment_role": convert_and_respect_annotation_metadata(
                    object_=employment_role, annotation=EmployeeEmploymentRole, direction="write"
                ),
                "employment_start_date": employment_start_date,
                "employment_status": employment_status,
                "first_name": first_name,
                "food_allergies": food_allergies,
                "gender": gender,
                "id": id,
                "initials": initials,
                "jobs": convert_and_respect_annotation_metadata(
                    object_=jobs, annotation=typing.Sequence[EmployeeJobsItem], direction="write"
                ),
                "languages": languages,
                "last_name": last_name,
                "leaving_reason": leaving_reason,
                "manager": convert_and_respect_annotation_metadata(
                    object_=manager, annotation=EmployeeManager, direction="write"
                ),
                "marital_status": marital_status,
                "middle_name": middle_name,
                "nationalities": nationalities,
                "partner": convert_and_respect_annotation_metadata(
                    object_=partner, annotation=EmployeePartner, direction="write"
                ),
                "phone_numbers": convert_and_respect_annotation_metadata(
                    object_=phone_numbers, annotation=typing.Sequence[PhoneNumber], direction="write"
                ),
                "photo_url": photo_url,
                "preferred_language": preferred_language,
                "preferred_name": preferred_name,
                "pronouns": pronouns,
                "record_url": record_url,
                "row_version": row_version,
                "salutation": salutation,
                "social_links": convert_and_respect_annotation_metadata(
                    object_=social_links, annotation=typing.Sequence[EmployeeSocialLinksItem], direction="write"
                ),
                "social_security_number": social_security_number,
                "source": source,
                "source_id": source_id,
                "tags": tags,
                "tax_code": tax_code,
                "tax_id": tax_id,
                "team": convert_and_respect_annotation_metadata(
                    object_=team, annotation=typing.Optional[EmployeeTeam], direction="write"
                ),
                "timezone": timezone,
                "title": title,
                "updated_at": updated_at,
                "updated_by": updated_by,
                "works_remote": works_remote,
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
                    UpdateEmployeeResponse,
                    parse_obj_as(
                        type_=UpdateEmployeeResponse,
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
