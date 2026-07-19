

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TemplatesCreateTemplateNoProjectRequest_Agent(UniversalBaseModel):
    """
    The type of template to create, currently only agent templates are supported
    """

    type: typing.Literal["agent"] = "agent"
    agent_id: str
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TemplatesCreateTemplateNoProjectRequest_AgentFile(UniversalBaseModel):
    """
    The type of template to create, currently only agent templates are supported
    """

    type: typing.Literal["agent_file"] = "agent_file"
    agent_file: typing.Dict[str, typing.Any]
    name: typing.Optional[str] = None
    update_existing_tools: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


TemplatesCreateTemplateNoProjectRequest = typing_extensions.Annotated[
    typing.Union[TemplatesCreateTemplateNoProjectRequest_Agent, TemplatesCreateTemplateNoProjectRequest_AgentFile],
    pydantic.Field(discriminator="type"),
]
