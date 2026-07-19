

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RequiresApprovalToolRule(UniversalBaseModel):
    """
    Represents a tool rule configuration which requires approval before the tool can be invoked.
    """

    tool_name: str = pydantic.Field()
    """
    The name of the tool. Must exist in the database for the user's organization.
    """

    prompt_template: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional template string (ignored). Rendering uses fast built-in formatting for performance.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
