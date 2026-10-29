

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .semantics import Semantics


class EntityHistoryExecutionStatusInfosItem(UniversalBaseModel):
    label: typing.Optional[str] = None
    description: typing.Optional[str] = None
    type_info: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="typeInfo"), pydantic.Field(alias="typeInfo")
    ] = None
    value: typing.Optional[str] = None
    semantics: typing.Optional[typing.List[Semantics]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
