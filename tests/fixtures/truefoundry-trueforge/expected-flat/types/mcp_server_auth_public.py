

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class McpServerAuthPublic_Dcr(UniversalBaseModel):
    """
    Auth mechanism when configured (no secrets). Omit when the server needs no credentials.
    """

    type: typing.Literal["dcr"] = "dcr"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class McpServerAuthPublic_Header(UniversalBaseModel):
    """
    Auth mechanism when configured (no secrets). Omit when the server needs no credentials.
    """

    type: typing.Literal["header"] = "header"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


McpServerAuthPublic = typing_extensions.Annotated[
    typing.Union[McpServerAuthPublic_Dcr, McpServerAuthPublic_Header], pydantic.Field(discriminator="type")
]
