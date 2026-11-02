

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .handover_any_of_const import HandoverAnyOfConst
from .handover_any_of_enum import HandoverAnyOfEnum
from .handover_one_of_const import HandoverOneOfConst
from .handover_one_of_enum import HandoverOneOfEnum


class Order(UniversalBaseModel):
    by_const: typing_extensions.Annotated[
        typing.Optional[HandoverOneOfConst], FieldMetadata(alias="byConst"), pydantic.Field(alias="byConst")
    ] = None
    any_const: typing_extensions.Annotated[
        typing.Optional[HandoverAnyOfConst], FieldMetadata(alias="anyConst"), pydantic.Field(alias="anyConst")
    ] = None
    by_enum: typing_extensions.Annotated[
        typing.Optional[HandoverOneOfEnum], FieldMetadata(alias="byEnum"), pydantic.Field(alias="byEnum")
    ] = None
    any_enum: typing_extensions.Annotated[
        typing.Optional[HandoverAnyOfEnum], FieldMetadata(alias="anyEnum"), pydantic.Field(alias="anyEnum")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
