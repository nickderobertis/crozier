

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .project_automation_config_logs_action import ProjectAutomationConfigLogsAction


class ProjectAutomationConfigLogs(UniversalBaseModel):
    btql_filter: str = pydantic.Field()
    """
    BTQL filter to identify rows for the automation rule
    """

    interval_seconds: float = pydantic.Field()
    """
    Perform the triggered action at most once in this interval of seconds
    """

    action: ProjectAutomationConfigLogsAction = pydantic.Field()
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
