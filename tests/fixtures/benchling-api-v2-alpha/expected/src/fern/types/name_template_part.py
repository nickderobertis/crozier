

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NameTemplatePart(UniversalBaseModel):
    datetime_format: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="datetimeFormat"), pydantic.Field(alias="datetimeFormat")
    ] = None
    field_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="fieldId"), pydantic.Field(alias="fieldId")
    ] = None
    text: typing.Optional[str] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
