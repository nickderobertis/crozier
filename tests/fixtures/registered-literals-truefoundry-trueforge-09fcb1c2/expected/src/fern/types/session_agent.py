

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_spec import AgentSpec


class SessionAgent_Inline(UniversalBaseModel):
    type: typing.Literal["inline"] = "inline"
    spec: AgentSpec

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SessionAgent_Reference(UniversalBaseModel):
    type: typing.Literal["reference"] = "reference"
    id: str
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SessionAgent = typing_extensions.Annotated[
    typing.Union[SessionAgent_Inline, SessionAgent_Reference], pydantic.Field(discriminator="type")
]
