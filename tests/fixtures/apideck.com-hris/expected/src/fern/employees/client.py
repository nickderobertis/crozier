

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.address import Address
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
from ..types.phone_number import PhoneNumber
from ..types.photo_url import PhotoUrl
from ..types.row_version import RowVersion
from ..types.title import Title
from ..types.update_employee_response import UpdateEmployeeResponse
from ..types.updated_at import UpdatedAt
from ..types.updated_by import UpdatedBy
from .raw_client import AsyncRawEmployeesClient, RawEmployeesClient


OMIT = typing.cast(typing.Any, ...)


class EmployeesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEmployeesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEmployeesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEmployeesClient
        """
        return self._raw_client

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
    ) -> GetEmployeesResponse:
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
        GetEmployeesResponse
            Employees

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.employees.all_(
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.all_(
            raw=raw,
            cursor=cursor,
            limit=limit,
            filter=filter,
            sort=sort,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

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
    ) -> CreateEmployeeResponse:
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
        CreateEmployeeResponse
            Employees

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.employees.add()
        """
        _response = self._raw_client.add(
            raw=raw,
            addresses=addresses,
            birthday=birthday,
            company_id=company_id,
            company_name=company_name,
            compensations=compensations,
            country_of_birth=country_of_birth,
            created_at=created_at,
            created_by=created_by,
            custom_fields=custom_fields,
            deceased_on=deceased_on,
            deleted=deleted,
            department=department,
            department_id=department_id,
            department_name=department_name,
            description=description,
            dietary_preference=dietary_preference,
            direct_reports=direct_reports,
            display_name=display_name,
            division=division,
            division_id=division_id,
            emails=emails,
            employee_number=employee_number,
            employment_end_date=employment_end_date,
            employment_role=employment_role,
            employment_start_date=employment_start_date,
            employment_status=employment_status,
            first_name=first_name,
            food_allergies=food_allergies,
            gender=gender,
            id=id,
            initials=initials,
            jobs=jobs,
            languages=languages,
            last_name=last_name,
            leaving_reason=leaving_reason,
            manager=manager,
            marital_status=marital_status,
            middle_name=middle_name,
            nationalities=nationalities,
            partner=partner,
            phone_numbers=phone_numbers,
            photo_url=photo_url,
            preferred_language=preferred_language,
            preferred_name=preferred_name,
            pronouns=pronouns,
            record_url=record_url,
            row_version=row_version,
            salutation=salutation,
            social_links=social_links,
            social_security_number=social_security_number,
            source=source,
            source_id=source_id,
            tags=tags,
            tax_code=tax_code,
            tax_id=tax_id,
            team=team,
            timezone=timezone,
            title=title,
            updated_at=updated_at,
            updated_by=updated_by,
            works_remote=works_remote,
            request_options=request_options,
        )
        return _response.data

    def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetEmployeeResponse:
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
        GetEmployeeResponse
            Employees

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.employees.one(
            id="id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteEmployeeResponse:
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
        DeleteEmployeeResponse
            Employees

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.employees.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

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
    ) -> UpdateEmployeeResponse:
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
        UpdateEmployeeResponse
            Employees

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.employees.update(
            id_="id",
        )
        """
        _response = self._raw_client.update(
            id_,
            raw=raw,
            addresses=addresses,
            birthday=birthday,
            company_id=company_id,
            company_name=company_name,
            compensations=compensations,
            country_of_birth=country_of_birth,
            created_at=created_at,
            created_by=created_by,
            custom_fields=custom_fields,
            deceased_on=deceased_on,
            deleted=deleted,
            department=department,
            department_id=department_id,
            department_name=department_name,
            description=description,
            dietary_preference=dietary_preference,
            direct_reports=direct_reports,
            display_name=display_name,
            division=division,
            division_id=division_id,
            emails=emails,
            employee_number=employee_number,
            employment_end_date=employment_end_date,
            employment_role=employment_role,
            employment_start_date=employment_start_date,
            employment_status=employment_status,
            first_name=first_name,
            food_allergies=food_allergies,
            gender=gender,
            id=id,
            initials=initials,
            jobs=jobs,
            languages=languages,
            last_name=last_name,
            leaving_reason=leaving_reason,
            manager=manager,
            marital_status=marital_status,
            middle_name=middle_name,
            nationalities=nationalities,
            partner=partner,
            phone_numbers=phone_numbers,
            photo_url=photo_url,
            preferred_language=preferred_language,
            preferred_name=preferred_name,
            pronouns=pronouns,
            record_url=record_url,
            row_version=row_version,
            salutation=salutation,
            social_links=social_links,
            social_security_number=social_security_number,
            source=source,
            source_id=source_id,
            tags=tags,
            tax_code=tax_code,
            tax_id=tax_id,
            team=team,
            timezone=timezone,
            title=title,
            updated_at=updated_at,
            updated_by=updated_by,
            works_remote=works_remote,
            request_options=request_options,
        )
        return _response.data


class AsyncEmployeesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEmployeesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEmployeesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEmployeesClient
        """
        return self._raw_client

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
    ) -> GetEmployeesResponse:
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
        GetEmployeesResponse
            Employees

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.employees.all_(
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(
            raw=raw,
            cursor=cursor,
            limit=limit,
            filter=filter,
            sort=sort,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

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
    ) -> CreateEmployeeResponse:
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
        CreateEmployeeResponse
            Employees

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.employees.add()


        asyncio.run(main())
        """
        _response = await self._raw_client.add(
            raw=raw,
            addresses=addresses,
            birthday=birthday,
            company_id=company_id,
            company_name=company_name,
            compensations=compensations,
            country_of_birth=country_of_birth,
            created_at=created_at,
            created_by=created_by,
            custom_fields=custom_fields,
            deceased_on=deceased_on,
            deleted=deleted,
            department=department,
            department_id=department_id,
            department_name=department_name,
            description=description,
            dietary_preference=dietary_preference,
            direct_reports=direct_reports,
            display_name=display_name,
            division=division,
            division_id=division_id,
            emails=emails,
            employee_number=employee_number,
            employment_end_date=employment_end_date,
            employment_role=employment_role,
            employment_start_date=employment_start_date,
            employment_status=employment_status,
            first_name=first_name,
            food_allergies=food_allergies,
            gender=gender,
            id=id,
            initials=initials,
            jobs=jobs,
            languages=languages,
            last_name=last_name,
            leaving_reason=leaving_reason,
            manager=manager,
            marital_status=marital_status,
            middle_name=middle_name,
            nationalities=nationalities,
            partner=partner,
            phone_numbers=phone_numbers,
            photo_url=photo_url,
            preferred_language=preferred_language,
            preferred_name=preferred_name,
            pronouns=pronouns,
            record_url=record_url,
            row_version=row_version,
            salutation=salutation,
            social_links=social_links,
            social_security_number=social_security_number,
            source=source,
            source_id=source_id,
            tags=tags,
            tax_code=tax_code,
            tax_id=tax_id,
            team=team,
            timezone=timezone,
            title=title,
            updated_at=updated_at,
            updated_by=updated_by,
            works_remote=works_remote,
            request_options=request_options,
        )
        return _response.data

    async def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetEmployeeResponse:
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
        GetEmployeeResponse
            Employees

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.employees.one(
                id="id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteEmployeeResponse:
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
        DeleteEmployeeResponse
            Employees

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.employees.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

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
    ) -> UpdateEmployeeResponse:
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
        UpdateEmployeeResponse
            Employees

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.employees.update(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id_,
            raw=raw,
            addresses=addresses,
            birthday=birthday,
            company_id=company_id,
            company_name=company_name,
            compensations=compensations,
            country_of_birth=country_of_birth,
            created_at=created_at,
            created_by=created_by,
            custom_fields=custom_fields,
            deceased_on=deceased_on,
            deleted=deleted,
            department=department,
            department_id=department_id,
            department_name=department_name,
            description=description,
            dietary_preference=dietary_preference,
            direct_reports=direct_reports,
            display_name=display_name,
            division=division,
            division_id=division_id,
            emails=emails,
            employee_number=employee_number,
            employment_end_date=employment_end_date,
            employment_role=employment_role,
            employment_start_date=employment_start_date,
            employment_status=employment_status,
            first_name=first_name,
            food_allergies=food_allergies,
            gender=gender,
            id=id,
            initials=initials,
            jobs=jobs,
            languages=languages,
            last_name=last_name,
            leaving_reason=leaving_reason,
            manager=manager,
            marital_status=marital_status,
            middle_name=middle_name,
            nationalities=nationalities,
            partner=partner,
            phone_numbers=phone_numbers,
            photo_url=photo_url,
            preferred_language=preferred_language,
            preferred_name=preferred_name,
            pronouns=pronouns,
            record_url=record_url,
            row_version=row_version,
            salutation=salutation,
            social_links=social_links,
            social_security_number=social_security_number,
            source=source,
            source_id=source_id,
            tags=tags,
            tax_code=tax_code,
            tax_id=tax_id,
            team=team,
            timezone=timezone,
            title=title,
            updated_at=updated_at,
            updated_by=updated_by,
            works_remote=works_remote,
            request_options=request_options,
        )
        return _response.data
