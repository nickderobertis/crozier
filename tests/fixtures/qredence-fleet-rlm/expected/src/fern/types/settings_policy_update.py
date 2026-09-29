

import typing

from .settings_policy_update_one import SettingsPolicyUpdateOne
from .settings_policy_update_value import SettingsPolicyUpdateValue

SettingsPolicyUpdate = typing.Union[SettingsPolicyUpdateValue, SettingsPolicyUpdateOne]
