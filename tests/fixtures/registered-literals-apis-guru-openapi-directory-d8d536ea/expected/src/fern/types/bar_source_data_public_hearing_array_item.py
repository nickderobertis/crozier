

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BarSourceDataPublicHearingArrayItem(UniversalBaseModel):
    conduct: typing.Optional[str] = None
    date: typing.Optional[dt.datetime] = None
    issued_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="issuedBy"), pydantic.Field(alias="issuedBy")
    ] = None
    order: typing.Optional[str] = None
    respondent: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
