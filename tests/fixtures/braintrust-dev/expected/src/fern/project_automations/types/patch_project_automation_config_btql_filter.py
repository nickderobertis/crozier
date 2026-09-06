

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .patch_project_automation_config_btql_filter_action import PatchProjectAutomationConfigBtqlFilterAction
from .patch_project_automation_config_btql_filter_event_type import PatchProjectAutomationConfigBtqlFilterEventType


class PatchProjectAutomationConfigBtqlFilter(UniversalBaseModel):
    event_type: PatchProjectAutomationConfigBtqlFilterEventType = pydantic.Field()
    """
    The type of automation.
    """

    btql_filter: str = pydantic.Field()
    """
    BTQL filter to identify rows for the automation rule
    """

    interval_seconds: float = pydantic.Field()
    """
    Perform the triggered action at most once in this interval of seconds
    """

    action: PatchProjectAutomationConfigBtqlFilterAction = pydantic.Field()
    """
    The action to take when the automation rule is triggered
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
