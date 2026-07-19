

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TemplatesCreateTemplateRequestBodyAgent(UniversalBaseModel):
    """
    Create a template from an existing agent
    """

    agent_id: str = pydantic.Field()
    """
    The ID of the agent to use as a template, can be from any project
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional custom name for the template. If not provided, a random name will be generated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
