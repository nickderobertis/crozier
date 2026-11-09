

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BarSourceDataLawSchoolArrayItem(UniversalBaseModel):
    law_school: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lawSchool"), pydantic.Field(alias="lawSchool")
    ] = None
    law_school_graduated_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lawSchoolGraduatedDate"),
        pydantic.Field(alias="lawSchoolGraduatedDate"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
