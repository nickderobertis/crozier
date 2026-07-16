

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class IgnoresIgnoreResponse(UniversalBaseModel):
    ignore_flags: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ignoreFlags"), pydantic.Field(alias="ignoreFlags")
    ] = None
    is_ignored: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isIgnored"), pydantic.Field(alias="isIgnored")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
