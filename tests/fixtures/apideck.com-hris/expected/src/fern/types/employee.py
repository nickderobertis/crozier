

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .company_id import CompanyId
from .company_name import CompanyName
from .created_at import CreatedAt
from .created_by import CreatedBy
from .custom_field import CustomField
from .description import Description
from .division import Division
from .email import Email
from .employee_compensations_item import EmployeeCompensationsItem
from .employee_employment_role import EmployeeEmploymentRole
from .employee_jobs_item import EmployeeJobsItem
from .employee_leaving_reason import EmployeeLeavingReason
from .employee_manager import EmployeeManager
from .employee_number import EmployeeNumber
from .employee_partner import EmployeePartner
from .employee_social_links_item import EmployeeSocialLinksItem
from .employee_team import EmployeeTeam
from .employment_status import EmploymentStatus
from .first_name import FirstName
from .gender import Gender
from .id import Id
from .language import Language
from .last_name import LastName
from .middle_name import MiddleName
from .phone_number import PhoneNumber
from .photo_url import PhotoUrl
from .row_version import RowVersion
from .title import Title
from .updated_at import UpdatedAt
from .updated_by import UpdatedBy


class Employee(UniversalBaseModel):
    addresses: typing.Optional[typing.List[Address]] = None
    birthday: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date of birth of the person.
    """

    company_id: typing.Optional[CompanyId] = None
    company_name: typing.Optional[CompanyName] = None
    compensations: typing.Optional[typing.List[EmployeeCompensationsItem]] = None
    country_of_birth: typing.Optional[str] = pydantic.Field(default=None)
    """
    Country code according to ISO 3166-1 alpha-2.
    """

    created_at: typing.Optional[CreatedAt] = None
    created_by: typing.Optional[CreatedBy] = None
    custom_fields: typing.Optional[typing.List[CustomField]] = None
    deceased_on: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date the person deceased.
    """

    deleted: typing.Optional[bool] = None
    department: typing.Optional[str] = pydantic.Field(default=None)
    """
    The department the person is currently in. [Deprecated](https://developers.apideck.com/changelog) in favor of the dedicated department_id and department_name field.
    """

    department_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier of the department ID this employee belongs to.
    """

    department_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the department this employee belongs to.
    """

    description: typing.Optional[Description] = None
    dietary_preference: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicate the employee's dietary preference.
    """

    direct_reports: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The direct reports refer to the individuals who report directly to a person in the organizational hierarchy.
    """

    display_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name used to display the employee, often a combination of their first and last names.
    """

    division: typing.Optional[Division] = None
    division_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier of the division this employee belongs to.
    """

    emails: typing.Optional[typing.List[Email]] = None
    employee_number: typing.Optional[EmployeeNumber] = None
    employment_end_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    An End Date is the date that the employee ended working at the company
    """

    employment_role: typing.Optional[EmployeeEmploymentRole] = None
    employment_start_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    A Start Date is the date that the employee started working at the company
    """

    employment_status: typing.Optional[EmploymentStatus] = None
    first_name: typing.Optional[FirstName] = None
    food_allergies: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Indicate the employee's food allergies.
    """

    gender: typing.Optional[Gender] = None
    id: typing.Optional[Id] = None
    initials: typing.Optional[str] = pydantic.Field(default=None)
    """
    The initials of the person, usually derived from their first, middle, and last names.
    """

    jobs: typing.Optional[typing.List[EmployeeJobsItem]] = None
    languages: typing.Optional[typing.List[typing.Optional[Language]]] = None
    last_name: typing.Optional[LastName] = None
    leaving_reason: typing.Optional[EmployeeLeavingReason] = pydantic.Field(default=None)
    """
    The reason because the employment ended.
    """

    manager: typing.Optional[EmployeeManager] = None
    marital_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The marital status of the employee.
    """

    middle_name: typing.Optional[MiddleName] = None
    nationalities: typing.Optional[typing.List[typing.Optional[str]]] = None
    partner: typing.Optional[EmployeePartner] = None
    phone_numbers: typing.Optional[typing.List[PhoneNumber]] = None
    photo_url: typing.Optional[PhotoUrl] = None
    preferred_language: typing.Optional[Language] = None
    preferred_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name the employee prefers to be addressed by, which may be different from their legal name.
    """

    pronouns: typing.Optional[str] = pydantic.Field(default=None)
    """
    The preferred pronouns of the person.
    """

    record_url: typing.Optional[str] = None
    row_version: typing.Optional[RowVersion] = None
    salutation: typing.Optional[str] = pydantic.Field(default=None)
    """
    A formal salutation for the person. For example, 'Mr', 'Mrs'
    """

    social_links: typing.Optional[typing.List[EmployeeSocialLinksItem]] = None
    social_security_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier assigned by the government. This field is considered sensitive information and may be subject to special security and privacy restrictions.
    """

    source: typing.Optional[str] = pydantic.Field(default=None)
    """
    When the employee is imported as a new hire, this field indicates what system (e.g. the name of the ATS) this employee was imported from.
    """

    source_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier of the employee in the system this employee was imported from (e.g. the ID in the ATS).
    """

    tags: typing.Optional[typing.List[str]] = None
    tax_code: typing.Optional[str] = None
    tax_id: typing.Optional[str] = None
    team: typing.Optional[EmployeeTeam] = pydantic.Field(default=None)
    """
    The team the person is currently in.
    """

    timezone: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time zone related to the resource. The value is a string containing a standard time zone identifier, e.g. Europe/London.
    """

    title: typing.Optional[Title] = None
    updated_at: typing.Optional[UpdatedAt] = None
    updated_by: typing.Optional[UpdatedBy] = None
    works_remote: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates if the employee works from a remote location.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
