

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .capture_rule_source import CaptureRuleSource


class CaptureRule(UniversalBaseModel):
    """
    a rule extracting a value from the matched request into scenario state
    """

    source: CaptureRuleSource
    expression: str
    into: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
