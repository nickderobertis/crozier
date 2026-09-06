

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PromptDataNullishMcpValue_Id(UniversalBaseModel):
    type: typing.Literal["id"] = "id"
    id: str
    is_disabled: typing.Optional[bool] = None
    enabled_tools: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PromptDataNullishMcpValue_Url(UniversalBaseModel):
    type: typing.Literal["url"] = "url"
    url: str
    is_disabled: typing.Optional[bool] = None
    enabled_tools: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PromptDataNullishMcpValue = typing_extensions.Annotated[
    typing.Union[PromptDataNullishMcpValue_Id, PromptDataNullishMcpValue_Url], pydantic.Field(discriminator="type")
]
