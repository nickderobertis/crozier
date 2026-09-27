

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SseEventToolResult(UniversalBaseModel):
    tool_call_id: typing.Optional[str] = None
    tool_name: typing.Optional[str] = None
    tool_display_name: typing.Optional[str] = None
    tool_display_name_key: typing.Optional[str] = None
    result: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Tool reply payload (any JSON).
    """

    error: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
