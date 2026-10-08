

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class InvokeAiToolResponse(UniversalBaseModel):
    error: typing.Optional[str] = None
    result: typing.Any
    success: bool
    tool_name: typing_extensions.Annotated[str, FieldMetadata(alias="toolName"), pydantic.Field(alias="toolName")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
