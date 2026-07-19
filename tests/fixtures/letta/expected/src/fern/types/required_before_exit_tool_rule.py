

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RequiredBeforeExitToolRule(UniversalBaseModel):
    """
    Represents a tool rule configuration where this tool must be called before the agent loop can exit.
    """

    tool_name: str = pydantic.Field()
    """
    The name of the tool. Must exist in the database for the user's organization.
    """

    prompt_template: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional template string (ignored).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
