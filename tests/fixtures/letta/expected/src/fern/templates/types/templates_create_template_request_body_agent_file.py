

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TemplatesCreateTemplateRequestBodyAgentFile(UniversalBaseModel):
    """
    Create a template from an uploaded agent file
    """

    agent_file: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    The agent file to use as a template, this should be a JSON file exported from the platform
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional custom name for the template. If not provided, a random name will be generated.
    """

    update_existing_tools: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, update existing custom tools source_code and json_schema (source_type cannot be changed)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
