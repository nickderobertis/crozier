

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .q_name import QName


class Duration(UniversalBaseModel):
    x_ml_schema_type: typing_extensions.Annotated[
        typing.Optional[QName], FieldMetadata(alias="xMLSchemaType"), pydantic.Field(alias="xMLSchemaType")
    ] = None
    sign: typing.Optional[int] = None
    years: typing.Optional[int] = None
    months: typing.Optional[int] = None
    days: typing.Optional[int] = None
    hours: typing.Optional[int] = None
    minutes: typing.Optional[int] = None
    seconds: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
