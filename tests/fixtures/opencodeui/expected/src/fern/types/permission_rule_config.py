

import typing

from .permission_action_config import PermissionActionConfig
from .permission_object_config import PermissionObjectConfig

PermissionRuleConfig = typing.Union[PermissionActionConfig, PermissionObjectConfig]
