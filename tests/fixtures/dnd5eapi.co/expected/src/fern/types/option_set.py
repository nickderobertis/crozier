

from __future__ import annotations

import typing

from .option_set_equipment_category import OptionSetEquipmentCategory
from .option_set_option_set_type import OptionSetOptionSetType

if typing.TYPE_CHECKING:
    from .option_set_options_array import OptionSetOptionsArray
OptionSet = typing.Union["OptionSetOptionsArray", OptionSetEquipmentCategory, OptionSetOptionSetType]
