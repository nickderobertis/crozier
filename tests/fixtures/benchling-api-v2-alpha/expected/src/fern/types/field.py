

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .field_type import FieldType
from .field_value import FieldValue
from .unit_summary import UnitSummary


class Field(UniversalBaseModel):
    display_value: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displayValue"), pydantic.Field(alias="displayValue")
    ] = None
    is_multi: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isMulti"), pydantic.Field(alias="isMulti")
    ] = None
    text_value: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="textValue"), pydantic.Field(alias="textValue")
    ] = None
    type: typing.Optional[FieldType] = None
    unit: typing.Optional[UnitSummary] = None
    value: typing.Optional[FieldValue] = pydantic.Field(default=None)
    """
    For single link fields, use the id of the item you want to link (eg. "seq_jdf8BV24").
    For multi-link fields, use an array of ids of the items you want to link (eg. ["seq_jdf8BV24"])
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
