

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .labeled import Labeled


class FilterBase(Labeled):
    unit: typing.Optional[str] = None
    tooltip: typing.Optional[str] = None
    pattern: typing.Optional[str] = None
    allow_drop_file: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowDropFile"), pydantic.Field(alias="allowDropFile")
    ] = None
    default_value: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="defaultValue"),
        pydantic.Field(alias="defaultValue"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
