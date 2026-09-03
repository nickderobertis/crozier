

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .screening_result_adverse_media import ScreeningResultAdverseMedia
from .screening_result_pep_check import ScreeningResultPepCheck
from .screening_result_sanctions_list import ScreeningResultSanctionsList


class ScreeningResult(UniversalBaseModel):
    sanctions_list: typing_extensions.Annotated[
        typing.Optional[ScreeningResultSanctionsList],
        FieldMetadata(alias="sanctionsList"),
        pydantic.Field(alias="sanctionsList"),
    ] = None
    pep_check: typing_extensions.Annotated[
        typing.Optional[ScreeningResultPepCheck], FieldMetadata(alias="pepCheck"), pydantic.Field(alias="pepCheck")
    ] = None
    adverse_media: typing_extensions.Annotated[
        typing.Optional[ScreeningResultAdverseMedia],
        FieldMetadata(alias="adverseMedia"),
        pydantic.Field(alias="adverseMedia"),
    ] = None
    last_screening_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastScreeningDate"),
        pydantic.Field(alias="lastScreeningDate"),
    ] = None
    next_screening_date: typing_extensions.Annotated[
        typing.Optional[dt.date], FieldMetadata(alias="nextScreeningDate"), pydantic.Field(alias="nextScreeningDate")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
