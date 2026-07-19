

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ToolCallNode(UniversalBaseModel):
    """
    Typed child override for prefilled arguments.

    When used in a ChildToolRule, if this child is selected next, its `args` will be
    applied as prefilled arguments (overriding overlapping LLM-provided values).
    """

    name: str = pydantic.Field()
    """
    The name of the child tool to invoke next.
    """

    args: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Optional prefilled arguments for this child tool. Keys must match the tool's parameter names and values must satisfy the tool's JSON schema. Supports partial prefill; non-overlapping parameters are left to the model.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
