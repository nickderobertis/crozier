

import typing

from .permission_action_config import PermissionActionConfig
from .permission_config_original_keys import PermissionConfigOriginalKeys

PermissionConfig = typing.Union[PermissionConfigOriginalKeys, PermissionActionConfig]
