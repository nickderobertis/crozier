

import typing

from .cron_patch_stream_mode_one import CronPatchStreamModeOne
from .cron_patch_stream_mode_zero_item import CronPatchStreamModeZeroItem

CronPatchStreamMode = typing.Union[typing.List[CronPatchStreamModeZeroItem], CronPatchStreamModeOne]
