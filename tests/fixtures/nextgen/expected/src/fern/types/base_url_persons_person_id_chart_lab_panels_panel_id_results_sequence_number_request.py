

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BaseUrlPersonsPersonIdChartLabPanelsPanelIdResultsSequenceNumberRequest(UniversalBaseModel):
    component_key: typing_extensions.Annotated[
        str, FieldMetadata(alias="ComponentKey"), pydantic.Field(alias="ComponentKey")
    ]
    component_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="ComponentDescription"), pydantic.Field(alias="ComponentDescription")
    ]
    value: typing_extensions.Annotated[str, FieldMetadata(alias="Value"), pydantic.Field(alias="Value")]
    unit: typing_extensions.Annotated[str, FieldMetadata(alias="Unit"), pydantic.Field(alias="Unit")]
    range: typing_extensions.Annotated[str, FieldMetadata(alias="Range"), pydantic.Field(alias="Range")]
    comment: typing_extensions.Annotated[str, FieldMetadata(alias="Comment"), pydantic.Field(alias="Comment")]
    abnormal_flag: typing_extensions.Annotated[
        str, FieldMetadata(alias="AbnormalFlag"), pydantic.Field(alias="AbnormalFlag")
    ]
    code_system: typing_extensions.Annotated[str, FieldMetadata(alias="CodeSystem"), pydantic.Field(alias="CodeSystem")]
    observation_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="ObservationDate"), pydantic.Field(alias="ObservationDate")
    ]
    loinc_code: typing_extensions.Annotated[str, FieldMetadata(alias="LoincCode"), pydantic.Field(alias="LoincCode")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
