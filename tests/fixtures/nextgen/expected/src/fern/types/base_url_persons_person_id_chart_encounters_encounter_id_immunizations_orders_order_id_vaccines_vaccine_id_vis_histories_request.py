

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BaseUrlPersonsPersonIdChartEncountersEncounterIdImmunizationsOrdersOrderIdVaccinesVaccineIdVisHistoriesRequest(
    UniversalBaseModel
):
    vaccine_vis_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="VaccineVisId"), pydantic.Field(alias="VaccineVisId")
    ]
    vis_give_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="VisGiveDate"), pydantic.Field(alias="VisGiveDate")
    ]
    vis_publish_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="VisPublishDate"), pydantic.Field(alias="VisPublishDate")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
