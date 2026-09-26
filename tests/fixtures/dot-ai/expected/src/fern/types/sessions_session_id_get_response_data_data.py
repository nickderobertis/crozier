

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SessionsSessionIdGetResponseDataData(UniversalBaseModel):
    """
    Session data
    """

    tool_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="toolName"),
        pydantic.Field(alias="toolName", description="Tool that created this session"),
    ] = None
    """
    Tool that created this session
    """

    intent: typing.Optional[str] = pydantic.Field(default=None)
    """
    User intent for this session
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
