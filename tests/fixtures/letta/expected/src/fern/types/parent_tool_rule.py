

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ParentToolRule(UniversalBaseModel):
    """
    A ToolRule that only allows a child tool to be called if the parent has been called.
    """

    tool_name: str = pydantic.Field()
    """
    The name of the tool. Must exist in the database for the user's organization.
    """

    prompt_template: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional template string (ignored).
    """

    children: typing.List[str] = pydantic.Field()
    """
    The children tools that can be invoked.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
