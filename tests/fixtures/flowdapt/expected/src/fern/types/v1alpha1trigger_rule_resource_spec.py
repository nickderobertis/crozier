

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1alpha1trigger_rule_action import V1Alpha1TriggerRuleAction
from .v1alpha1trigger_rule_resource_spec_rule import V1Alpha1TriggerRuleResourceSpecRule
from .v1alpha1trigger_rule_type import V1Alpha1TriggerRuleType


class V1Alpha1TriggerRuleResourceSpec(UniversalBaseModel):
    type: typing.Optional[V1Alpha1TriggerRuleType] = None
    rule: V1Alpha1TriggerRuleResourceSpecRule
    action: V1Alpha1TriggerRuleAction

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
