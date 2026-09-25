

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok84(UniversalBaseModel):
    id: str
    first_name: typing_extensions.Annotated[str, FieldMetadata(alias="firstName"), pydantic.Field(alias="firstName")]
    last_name: typing_extensions.Annotated[str, FieldMetadata(alias="lastName"), pydantic.Field(alias="lastName")]
    middle_name: typing_extensions.Annotated[str, FieldMetadata(alias="middleName"), pydantic.Field(alias="middleName")]
    nickname: str
    address_line1: typing_extensions.Annotated[
        str, FieldMetadata(alias="addressLine1"), pydantic.Field(alias="addressLine1")
    ]
    address_line2: typing_extensions.Annotated[
        str, FieldMetadata(alias="addressLine2"), pydantic.Field(alias="addressLine2")
    ]
    city: str
    state: str
    zip: str
    country: str
    home_phone: typing_extensions.Annotated[str, FieldMetadata(alias="homePhone"), pydantic.Field(alias="homePhone")]
    date_of_birth: typing_extensions.Annotated[
        str, FieldMetadata(alias="dateOfBirth"), pydantic.Field(alias="dateOfBirth")
    ]
    sex: str
    current_gender: typing_extensions.Annotated[
        str, FieldMetadata(alias="currentGender"), pydantic.Field(alias="currentGender")
    ]
    social_security_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="socialSecurityNumber"), pydantic.Field(alias="socialSecurityNumber")
    ]
    person_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="personNumber"), pydantic.Field(alias="personNumber")
    ]
    medical_record_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="medicalRecordNumber"), pydantic.Field(alias="medicalRecordNumber")
    ]
    other_id_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="otherIdNumber"), pydantic.Field(alias="otherIdNumber")
    ]
    is_enterprise_chart: typing_extensions.Annotated[
        str, FieldMetadata(alias="isEnterpriseChart"), pydantic.Field(alias="isEnterpriseChart")
    ]
    is_patient: typing_extensions.Annotated[str, FieldMetadata(alias="isPatient"), pydantic.Field(alias="isPatient")]
    can_add_to_inclusion_list: typing_extensions.Annotated[
        str, FieldMetadata(alias="canAddToInclusionList"), pydantic.Field(alias="canAddToInclusionList")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
