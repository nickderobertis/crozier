

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mcp_remote_config_oauth import McpRemoteConfigOauth


class McpAddRequestConfig_Local(UniversalBaseModel):
    type: typing.Literal["local"] = "local"
    command: typing.List[str]
    environment: typing.Optional[typing.Dict[str, str]] = None
    enabled: typing.Optional[bool] = None
    timeout: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class McpAddRequestConfig_Remote(UniversalBaseModel):
    type: typing.Literal["remote"] = "remote"
    url: str
    enabled: typing.Optional[bool] = None
    headers: typing.Optional[typing.Dict[str, str]] = None
    oauth: typing.Optional[McpRemoteConfigOauth] = None
    timeout: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


McpAddRequestConfig = typing_extensions.Annotated[
    typing.Union[McpAddRequestConfig_Local, McpAddRequestConfig_Remote], pydantic.Field(discriminator="type")
]
