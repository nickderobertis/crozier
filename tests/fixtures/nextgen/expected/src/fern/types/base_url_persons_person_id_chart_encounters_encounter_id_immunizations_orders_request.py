

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BaseUrlPersonsPersonIdChartEncountersEncounterIdImmunizationsOrdersRequest(UniversalBaseModel):
    generated_by: typing_extensions.Annotated[
        str, FieldMetadata(alias="GeneratedBy"), pydantic.Field(alias="GeneratedBy")
    ]
    location_id: typing_extensions.Annotated[str, FieldMetadata(alias="LocationId"), pydantic.Field(alias="LocationId")]
    ordering_provider_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="OrderingProviderId"), pydantic.Field(alias="OrderingProviderId")
    ]
    supervisor_provider_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="SupervisorProviderId"), pydantic.Field(alias="SupervisorProviderId")
    ]
    registry_id: typing_extensions.Annotated[str, FieldMetadata(alias="RegistryId"), pydantic.Field(alias="RegistryId")]
    comment: typing_extensions.Annotated[str, FieldMetadata(alias="Comment"), pydantic.Field(alias="Comment")]
    verbal_order_indicator: typing_extensions.Annotated[
        str, FieldMetadata(alias="VerbalOrderIndicator"), pydantic.Field(alias="VerbalOrderIndicator")
    ]
    allergies_reviewed: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="AllergiesReviewed"), pydantic.Field(alias="AllergiesReviewed")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
