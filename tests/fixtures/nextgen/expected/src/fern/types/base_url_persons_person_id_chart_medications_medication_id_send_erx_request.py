

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BaseUrlPersonsPersonIdChartMedicationsMedicationIdSendErxRequest(UniversalBaseModel):
    pharmacy_id: typing_extensions.Annotated[str, FieldMetadata(alias="PharmacyId"), pydantic.Field(alias="PharmacyId")]
    pbm_id: typing_extensions.Annotated[str, FieldMetadata(alias="PbmId"), pydantic.Field(alias="PbmId")]
    formulary_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="FormularyId"), pydantic.Field(alias="FormularyId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
