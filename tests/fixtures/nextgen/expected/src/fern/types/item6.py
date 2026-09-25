

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Item6(UniversalBaseModel):
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    id: str
    provider_id: typing_extensions.Annotated[str, FieldMetadata(alias="providerId"), pydantic.Field(alias="providerId")]
    encounter_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterId"), pydantic.Field(alias="encounterId")
    ]
    first_name: typing_extensions.Annotated[str, FieldMetadata(alias="firstName"), pydantic.Field(alias="firstName")]
    last_name: typing_extensions.Annotated[str, FieldMetadata(alias="lastName"), pydantic.Field(alias="lastName")]
    email: str
    active_date: typing_extensions.Annotated[str, FieldMetadata(alias="activeDate"), pydantic.Field(alias="activeDate")]
    inactive_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="inactiveDate"), pydantic.Field(alias="inactiveDate")
    ]
    address: str
    city: str
    state: str
    zip: str
    home_phone: typing_extensions.Annotated[str, FieldMetadata(alias="homePhone"), pydantic.Field(alias="homePhone")]
    cell_phone: typing_extensions.Annotated[str, FieldMetadata(alias="cellPhone"), pydantic.Field(alias="cellPhone")]
    fax: str
    agency_name: typing_extensions.Annotated[str, FieldMetadata(alias="agencyName"), pydantic.Field(alias="agencyName")]
    agency_type: typing_extensions.Annotated[str, FieldMetadata(alias="agencyType"), pydantic.Field(alias="agencyType")]
    patient_relationship: typing_extensions.Annotated[
        str, FieldMetadata(alias="patientRelationship"), pydantic.Field(alias="patientRelationship")
    ]
    support_role: typing_extensions.Annotated[
        str, FieldMetadata(alias="supportRole"), pydantic.Field(alias="supportRole")
    ]
    specialty: str
    role_class: typing_extensions.Annotated[str, FieldMetadata(alias="roleClass"), pydantic.Field(alias="roleClass")]
    role_code: typing_extensions.Annotated[str, FieldMetadata(alias="roleCode"), pydantic.Field(alias="roleCode")]
    is_read_only: typing_extensions.Annotated[
        str, FieldMetadata(alias="isReadOnly"), pydantic.Field(alias="isReadOnly")
    ]
    status: str
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
