

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LintConfig(UniversalBaseModel):
    """
    Configuration for lint rule selection.

        Follows ruff-inspired semantics for selecting which rules to run
        during `marimo check`.

        **Keys.**

        - `select`: list of rule code prefixes that replaces the default
          enabled set. Use `"ALL"` to select all rules.
          Example: `["MB", "MR001"]`
        - `ignore`: list of rule code prefixes to remove from the
          enabled set.
    """

    ignore: typing.Optional[typing.List[str]] = None
    select: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
