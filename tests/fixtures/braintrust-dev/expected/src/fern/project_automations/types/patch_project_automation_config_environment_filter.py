

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .patch_project_automation_config_environment_filter_action import (
    PatchProjectAutomationConfigEnvironmentFilterAction,
)
from .patch_project_automation_config_environment_filter_event_type import (
    PatchProjectAutomationConfigEnvironmentFilterEventType,
)


class PatchProjectAutomationConfigEnvironmentFilter(UniversalBaseModel):
    event_type: PatchProjectAutomationConfigEnvironmentFilterEventType = pydantic.Field()
    """
    The type of automation.
    """

    environment_filter: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Optional list of environment slugs to filter by
    """

    action: PatchProjectAutomationConfigEnvironmentFilterAction = pydantic.Field()
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
