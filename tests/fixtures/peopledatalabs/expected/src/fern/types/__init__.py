



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .company import Company
    from .company_industry import CompanyIndustry
    from .company_location import CompanyLocation
    from .company_location_continent import CompanyLocationContinent
    from .company_location_country import CompanyLocationCountry
    from .company_location_metro import CompanyLocationMetro
    from .company_size import CompanySize
    from .company_type import CompanyType
    from .education import Education
    from .email import Email
    from .email_type import EmailType
    from .experience import Experience
    from .experience_company import ExperienceCompany
    from .experience_company_industry import ExperienceCompanyIndustry
    from .experience_company_location import ExperienceCompanyLocation
    from .experience_company_location_continent import ExperienceCompanyLocationContinent
    from .experience_company_location_country import ExperienceCompanyLocationCountry
    from .experience_company_location_metro import ExperienceCompanyLocationMetro
    from .experience_company_size import ExperienceCompanySize
    from .ip import Ip
    from .ip_data import IpData
    from .ip_data_company import IpDataCompany
    from .ip_data_company_confidence import IpDataCompanyConfidence
    from .ip_data_company_size import IpDataCompanySize
    from .ip_data_ip import IpDataIp
    from .ip_data_ip_metadata import IpDataIpMetadata
    from .ip_data_person import IpDataPerson
    from .ip_data_person_confidence import IpDataPersonConfidence
    from .ip_data_person_job_title_levels import IpDataPersonJobTitleLevels
    from .ip_data_person_job_title_role import IpDataPersonJobTitleRole
    from .ip_data_person_job_title_sub_role import IpDataPersonJobTitleSubRole
    from .job_title import JobTitle
    from .location import Location
    from .location_continent import LocationContinent
    from .location_country import LocationCountry
    from .person import Person
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
    from .person_retrieve import PersonRetrieve
    from .person_retrieve_bulk import PersonRetrieveBulk
    from .person_sex import PersonSex
    from .profiles import Profiles
    from .profiles_network import ProfilesNetwork
    from .school import School
    from .school_location import SchoolLocation
    from .school_location_continent import SchoolLocationContinent
    from .school_location_country import SchoolLocationCountry
    from .school_type import SchoolType
    from .skill import Skill
    from .street_address import StreetAddress
    from .street_address_continent import StreetAddressContinent
    from .street_address_metro import StreetAddressMetro
    from .title import Title
    from .title_role import TitleRole
    from .title_sub_role import TitleSubRole
    from .version_status import VersionStatus
    from .version_status_status import VersionStatusStatus
_dynamic_imports: typing.Dict[str, str] = {
    "Company": ".company",
    "CompanyIndustry": ".company_industry",
    "CompanyLocation": ".company_location",
    "CompanyLocationContinent": ".company_location_continent",
    "CompanyLocationCountry": ".company_location_country",
    "CompanyLocationMetro": ".company_location_metro",
    "CompanySize": ".company_size",
    "CompanyType": ".company_type",
    "Education": ".education",
    "Email": ".email",
    "EmailType": ".email_type",
    "Experience": ".experience",
    "ExperienceCompany": ".experience_company",
    "ExperienceCompanyIndustry": ".experience_company_industry",
    "ExperienceCompanyLocation": ".experience_company_location",
    "ExperienceCompanyLocationContinent": ".experience_company_location_continent",
    "ExperienceCompanyLocationCountry": ".experience_company_location_country",
    "ExperienceCompanyLocationMetro": ".experience_company_location_metro",
    "ExperienceCompanySize": ".experience_company_size",
    "Ip": ".ip",
    "IpData": ".ip_data",
    "IpDataCompany": ".ip_data_company",
    "IpDataCompanyConfidence": ".ip_data_company_confidence",
    "IpDataCompanySize": ".ip_data_company_size",
    "IpDataIp": ".ip_data_ip",
    "IpDataIpMetadata": ".ip_data_ip_metadata",
    "IpDataPerson": ".ip_data_person",
    "IpDataPersonConfidence": ".ip_data_person_confidence",
    "IpDataPersonJobTitleLevels": ".ip_data_person_job_title_levels",
    "IpDataPersonJobTitleRole": ".ip_data_person_job_title_role",
    "IpDataPersonJobTitleSubRole": ".ip_data_person_job_title_sub_role",
    "JobTitle": ".job_title",
    "Location": ".location",
    "LocationContinent": ".location_continent",
    "LocationCountry": ".location_country",
    "Person": ".person",
    "PersonJobCompanyIndustry": ".person_job_company_industry",
    "PersonJobCompanyLocationContinent": ".person_job_company_location_continent",
    "PersonJobCompanyLocationCountry": ".person_job_company_location_country",
    "PersonJobCompanyLocationMetro": ".person_job_company_location_metro",
    "PersonJobCompanySize": ".person_job_company_size",
    "PersonJobTitleLevels": ".person_job_title_levels",
    "PersonJobTitleRole": ".person_job_title_role",
    "PersonJobTitleSubRole": ".person_job_title_sub_role",
    "PersonLocationContinent": ".person_location_continent",
    "PersonLocationCountry": ".person_location_country",
    "PersonLocationMetro": ".person_location_metro",
    "PersonRetrieve": ".person_retrieve",
    "PersonRetrieveBulk": ".person_retrieve_bulk",
    "PersonSex": ".person_sex",
    "Profiles": ".profiles",
    "ProfilesNetwork": ".profiles_network",
    "School": ".school",
    "SchoolLocation": ".school_location",
    "SchoolLocationContinent": ".school_location_continent",
    "SchoolLocationCountry": ".school_location_country",
    "SchoolType": ".school_type",
    "Skill": ".skill",
    "StreetAddress": ".street_address",
    "StreetAddressContinent": ".street_address_continent",
    "StreetAddressMetro": ".street_address_metro",
    "Title": ".title",
    "TitleRole": ".title_role",
    "TitleSubRole": ".title_sub_role",
    "VersionStatus": ".version_status",
    "VersionStatusStatus": ".version_status_status",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "Company",
    "CompanyIndustry",
    "CompanyLocation",
    "CompanyLocationContinent",
    "CompanyLocationCountry",
    "CompanyLocationMetro",
    "CompanySize",
    "CompanyType",
    "Education",
    "Email",
    "EmailType",
    "Experience",
    "ExperienceCompany",
    "ExperienceCompanyIndustry",
    "ExperienceCompanyLocation",
    "ExperienceCompanyLocationContinent",
    "ExperienceCompanyLocationCountry",
    "ExperienceCompanyLocationMetro",
    "ExperienceCompanySize",
    "Ip",
    "IpData",
    "IpDataCompany",
    "IpDataCompanyConfidence",
    "IpDataCompanySize",
    "IpDataIp",
    "IpDataIpMetadata",
    "IpDataPerson",
    "IpDataPersonConfidence",
    "IpDataPersonJobTitleLevels",
    "IpDataPersonJobTitleRole",
    "IpDataPersonJobTitleSubRole",
    "JobTitle",
    "Location",
    "LocationContinent",
    "LocationCountry",
    "Person",
    "PersonJobCompanyIndustry",
    "PersonJobCompanyLocationContinent",
    "PersonJobCompanyLocationCountry",
    "PersonJobCompanyLocationMetro",
    "PersonJobCompanySize",
    "PersonJobTitleLevels",
    "PersonJobTitleRole",
    "PersonJobTitleSubRole",
    "PersonLocationContinent",
    "PersonLocationCountry",
    "PersonLocationMetro",
    "PersonRetrieve",
    "PersonRetrieveBulk",
    "PersonSex",
    "Profiles",
    "ProfilesNetwork",
    "School",
    "SchoolLocation",
    "SchoolLocationContinent",
    "SchoolLocationCountry",
    "SchoolType",
    "Skill",
    "StreetAddress",
    "StreetAddressContinent",
    "StreetAddressMetro",
    "Title",
    "TitleRole",
    "TitleSubRole",
    "VersionStatus",
    "VersionStatusStatus",
]
