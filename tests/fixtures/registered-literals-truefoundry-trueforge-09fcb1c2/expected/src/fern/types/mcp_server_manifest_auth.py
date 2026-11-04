

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class McpServerManifestAuth_Dcr(UniversalBaseModel):
    """
    Optional auth settings. Omit when the server needs no credentials.
    """

    type: typing.Literal["dcr"] = "dcr"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class McpServerManifestAuth_Header(UniversalBaseModel):
    """
    Optional auth settings. Omit when the server needs no credentials.
    """

    type: typing.Literal["header"] = "header"
    headers: typing.Dict[str, str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


McpServerManifestAuth = typing_extensions.Annotated[
    typing.Union[McpServerManifestAuth_Dcr, McpServerManifestAuth_Header], pydantic.Field(discriminator="type")
]
