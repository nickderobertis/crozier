

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .education import Education
from .email import Email
from .experience import Experience
from .person_job_company_industry import PersonJobCompanyIndustry
from .person_job_company_location_continent import PersonJobCompanyLocationContinent
from .person_job_company_location_country import PersonJobCompanyLocationCountry
from .person_job_company_location_metro import PersonJobCompanyLocationMetro
from .person_job_company_size import PersonJobCompanySize
from .person_job_title_levels import PersonJobTitleLevels
from .person_job_title_role import PersonJobTitleRole
from .person_job_title_sub_role import PersonJobTitleSubRole
from .person_location_continent import PersonLocationContinent
from .person_location_country import PersonLocationCountry
from .person_location_metro import PersonLocationMetro
from .person_sex import PersonSex
from .profiles import Profiles
from .street_address import StreetAddress
from .version_status import VersionStatus


class Person(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    PDL persistent ID
    """

    full_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The first and the last name fields appended with a space
    """

    first_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    A person's first name
    """

    middle_initial: typing.Optional[str] = pydantic.Field(default=None)
    """
    A person's middle initial
    """

    middle_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    A person's middle name
    """

    last_initial: typing.Optional[str] = pydantic.Field(default=None)
    """
    A person's last initial
    """

    last_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    A person's last name
    """

    sex: typing.Optional[PersonSex] = pydantic.Field(default=None)
    """
    The person's sex
    """

    birth_year: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Approximated birth date associated with this person profile. If a profile has a birth_date, the birth_data_fuzzy field will match
    """

    birth_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Birth date associated with this person profile
    """

    linkedin_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Main linkedin profile for this record based on source agreement
    """

    linkedin_username: typing.Optional[str] = pydantic.Field(default=None)
    """
    Main linkedin username for this record based on source agreement
    """

    linkedin_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Main linkedin profile id for this record based on source agreement
    """

    facebook_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    facebook profile
    """

    facebook_username: typing.Optional[str] = pydantic.Field(default=None)
    """
    facebook username
    """

    facebook_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    persistent facebook id associated with a person's facebook profile
    """

    twitter_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Twitter URL
    """

    twitter_username: typing.Optional[str] = pydantic.Field(default=None)
    """
    Twitter Username
    """

    github_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Main github profile for this record based on source agreement
    """

    github_username: typing.Optional[str] = pydantic.Field(default=None)
    """
    Main github profile username for this record based on source agreement
    """

    work_email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Current Professional email
    """

    personal_emails: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of all emails tagged as type = personal
    """

    mobile_phone: typing.Optional[str] = pydantic.Field(default=None)
    """
    Highly confident direct dial mobile phone associated with this person
    """

    industry: typing.Optional[str] = pydantic.Field(default=None)
    """
    The most relevant industry for this record based primarily on their tagged personal industries and secondarily on the industries of the companies that they have worked for
    """

    job_title: typing.Optional[str] = pydantic.Field(default=None)
    """
    A person's current job title
    """

    job_title_role: typing.Optional[PersonJobTitleRole] = pydantic.Field(default=None)
    """
    A person's current job title derived role
    """

    job_title_sub_role: typing.Optional[PersonJobTitleSubRole] = pydantic.Field(default=None)
    """
    A person's job title derived subrole. Each subrole maps to a role
    """

    job_title_levels: typing.Optional[PersonJobTitleLevels] = pydantic.Field(default=None)
    """
    A person's current job title derived levels
    """

    job_company_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A person's current company's PDL ID
    """

    job_company_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    A person's current company's name
    """

    job_company_website: typing.Optional[str] = pydantic.Field(default=None)
    """
    A person's current company's website
    """

    job_company_size: typing.Optional[PersonJobCompanySize] = pydantic.Field(default=None)
    """
    A person's current company's size range
    """

    job_company_founded: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    A person's current company's founded date
    """

    job_company_industry: typing.Optional[PersonJobCompanyIndustry] = pydantic.Field(default=None)
    """
    A person's current company's industry
    """

    job_company_linkedin_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    A person's current company's linkedin url
    """

    job_company_linkedin_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A person's current company's linkedin id
    """

    job_company_facebook_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    A person's current company's facebook url
    """

    job_company_twitter_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    A person's current company's twitter url
    """

    job_company_location_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    A person's current company's HQ canonical location
    """

    job_company_location_locality: typing.Optional[str] = pydantic.Field(default=None)
    """
    A person's current company's HQ locality
    """

    job_company_location_metro: typing.Optional[PersonJobCompanyLocationMetro] = pydantic.Field(default=None)
    """
    A person's current company's HQ metro area
    """

    job_company_location_region: typing.Optional[str] = pydantic.Field(default=None)
    """
    A person's current company's HQ region
    """

    job_company_location_geo: typing.Optional[str] = pydantic.Field(default=None)
    """
    A person's current company's HQ geo
    """

    job_company_location_street_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    A person's current company's HQ street_address
    """

    job_company_location_address_line2: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="job_company_location_address_line_2"),
        pydantic.Field(
            alias="job_company_location_address_line_2", description="A person's current company's HQ address line 2"
        ),
    ] = None
    """
    A person's current company's HQ address line 2
    """

    job_company_location_postal_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    A person's current company's HQ postal code
    """

    job_company_location_country: typing.Optional[PersonJobCompanyLocationCountry] = pydantic.Field(default=None)
    """
    A person's current company's HQ country
    """

    job_company_location_continent: typing.Optional[PersonJobCompanyLocationContinent] = pydantic.Field(default=None)
    """
    A person's current company's HQ continent
    """

    job_last_updated: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Indicates the timestamp of the most recent source that agrees with this information
    """

    job_start_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Indicates the start period of the object. Can be accurate to the day (YYYY-MM-DD), month (YYYY-MM) or year (YYYY)
    """

    location_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    the current canonical location of the person
    """

    location_locality: typing.Optional[str] = pydantic.Field(default=None)
    """
    the current locality of the person
    """

    location_metro: typing.Optional[PersonLocationMetro] = pydantic.Field(default=None)
    """
    the current MSA of the person
    """

    location_region: typing.Optional[str] = pydantic.Field(default=None)
    """
    the current region of the person
    """

    location_country: typing.Optional[PersonLocationCountry] = pydantic.Field(default=None)
    """
    the current country of the person
    """

    location_continent: typing.Optional[PersonLocationContinent] = pydantic.Field(default=None)
    """
    the current continent of the person
    """

    location_street_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    the current street address of the person
    """

    location_address_line2: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="location_address_line_2"),
        pydantic.Field(alias="location_address_line_2", description="the current address line 2 of the person"),
    ] = None
    """
    the current address line 2 of the person
    """

    location_postal_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    the current postal code of the person
    """

    location_geo: typing.Optional[str] = pydantic.Field(default=None)
    """
    the current geo of the person
    """

    location_last_updated: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Indicates the timestamp of the most recent source that agrees with this information
    """

    phone_numbers: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Phone numbers associated with this person profile in E164 format
    """

    emails: typing.Optional[typing.List[Email]] = None
    interests: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Interests associated with the profile
    """

    skills: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Skills associated with the profile
    """

    location_names: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    list of all canonical location names associated with the person
    """

    regions: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of regions associated with the person
    """

    countries: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    list of countries associated with a person
    """

    street_address: typing.Optional[typing.List[StreetAddress]] = None
    experience: typing.Optional[typing.List[Experience]] = None
    education: typing.Optional[typing.List[Education]] = None
    profiles: typing.Optional[typing.List[Profiles]] = pydantic.Field(default=None)
    """
    Social media profiles associated with this person profile
    """

    operation_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Currently only in data license deliveries. Allows PDL employees to identify the timestamp and operations performed on the internal data to return a record in a delivery.
    """

    version_status: typing.Optional[VersionStatus] = pydantic.Field(default=None)
    """
    Allows customers track the pervious and current dataset version, any other persistent IDs that were merged into this record using improved entity resolution, and the status of the record
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
