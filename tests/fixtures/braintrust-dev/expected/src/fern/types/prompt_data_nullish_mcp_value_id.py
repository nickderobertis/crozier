

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PromptDataNullishMcpValueId(UniversalBaseModel):
    id: str
    is_disabled: typing.Optional[bool] = None
    enabled_tools: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    If omitted, all tools are enabled
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
