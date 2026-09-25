

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BaseUrlPersonsPersonIdChartCareTeamMembersCareTeamMemberIdRequest(UniversalBaseModel):
    provider_id: typing_extensions.Annotated[str, FieldMetadata(alias="providerId"), pydantic.Field(alias="providerId")]
    first_name: typing_extensions.Annotated[str, FieldMetadata(alias="firstName"), pydantic.Field(alias="firstName")]
    last_name: typing_extensions.Annotated[str, FieldMetadata(alias="lastName"), pydantic.Field(alias="lastName")]
    email: str
    active_date: typing_extensions.Annotated[str, FieldMetadata(alias="activeDate"), pydantic.Field(alias="activeDate")]
    address: str
    agency_name: typing_extensions.Annotated[str, FieldMetadata(alias="agencyName"), pydantic.Field(alias="agencyName")]
    agency_type: typing_extensions.Annotated[str, FieldMetadata(alias="agencyType"), pydantic.Field(alias="agencyType")]
    cell_phone: typing_extensions.Annotated[str, FieldMetadata(alias="cellPhone"), pydantic.Field(alias="cellPhone")]
    city: str
    fax: str
    home_phone: typing_extensions.Annotated[str, FieldMetadata(alias="homePhone"), pydantic.Field(alias="homePhone")]
    inactive_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="inactiveDate"), pydantic.Field(alias="inactiveDate")
    ]
    patient_relationship: typing_extensions.Annotated[
        str, FieldMetadata(alias="patientRelationship"), pydantic.Field(alias="patientRelationship")
    ]
    state: str
    support_role: typing_extensions.Annotated[
        str, FieldMetadata(alias="supportRole"), pydantic.Field(alias="supportRole")
    ]
    zip: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
