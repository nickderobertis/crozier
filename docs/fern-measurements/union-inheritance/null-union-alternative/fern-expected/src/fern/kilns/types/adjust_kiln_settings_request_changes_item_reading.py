

import typing

from .adjust_kiln_settings_request_changes_item_reading_one_item import (
    AdjustKilnSettingsRequestChangesItemReadingOneItem,
)
from .adjust_kiln_settings_request_changes_item_reading_zero import AdjustKilnSettingsRequestChangesItemReadingZero

AdjustKilnSettingsRequestChangesItemReading = typing.Union[
    typing.Optional[AdjustKilnSettingsRequestChangesItemReadingZero],
    typing.List[typing.Optional[AdjustKilnSettingsRequestChangesItemReadingOneItem]],
]
