

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .q_name import QName


class XmlGregorianCalendar(UniversalBaseModel):
    year: typing.Optional[int] = None
    month: typing.Optional[int] = None
    day: typing.Optional[int] = None
    timezone: typing.Optional[int] = None
    hour: typing.Optional[int] = None
    minute: typing.Optional[int] = None
    second: typing.Optional[int] = None
    millisecond: typing.Optional[int] = None
    fractional_second: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="fractionalSecond"), pydantic.Field(alias="fractionalSecond")
    ] = None
    eon: typing.Optional[int] = None
    eon_and_year: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="eonAndYear"), pydantic.Field(alias="eonAndYear")
    ] = None
    x_ml_schema_type: typing_extensions.Annotated[
        typing.Optional[QName], FieldMetadata(alias="xMLSchemaType"), pydantic.Field(alias="xMLSchemaType")
    ] = None
    valid: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
