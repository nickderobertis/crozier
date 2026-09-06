

import typing

from ...types.topic_automation_config import TopicAutomationConfig
from .patch_project_automation_config_batch_size import PatchProjectAutomationConfigBatchSize
from .patch_project_automation_config_btql_filter import PatchProjectAutomationConfigBtqlFilter
from .patch_project_automation_config_environment_filter import PatchProjectAutomationConfigEnvironmentFilter
from .patch_project_automation_config_object_type import PatchProjectAutomationConfigObjectType

PatchProjectAutomationConfig = typing.Union[
    PatchProjectAutomationConfigBtqlFilter,
    PatchProjectAutomationConfigBatchSize,
    PatchProjectAutomationConfigObjectType,
    PatchProjectAutomationConfigEnvironmentFilter,
    TopicAutomationConfig,
    typing.Optional[typing.Any],
]
