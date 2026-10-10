

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ToolInfo_Mcp(UniversalBaseModel):
    type: typing.Literal["mcp"] = "mcp"
    name: str
    server_id: str
    server_name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ToolInfo_TruefoundrySystem(UniversalBaseModel):
    type: typing.Literal["truefoundry-system"] = "truefoundry-system"
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ToolInfo = typing_extensions.Annotated[
    typing.Union[ToolInfo_Mcp, ToolInfo_TruefoundrySystem], pydantic.Field(discriminator="type")
]
