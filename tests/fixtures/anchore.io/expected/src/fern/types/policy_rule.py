

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .policy_rule_action import PolicyRuleAction
from .policy_rule_params_item import PolicyRuleParamsItem


class PolicyRule(UniversalBaseModel):
    """
    A rule that defines and decision value if the match is found true for a given image.
    """

    action: PolicyRuleAction
    gate: str
    id: typing.Optional[str] = None
    params: typing.Optional[typing.List[PolicyRuleParamsItem]] = None
    trigger: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
