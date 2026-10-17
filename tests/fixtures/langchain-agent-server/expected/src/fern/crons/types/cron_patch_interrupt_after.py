

import typing

from .cron_patch_interrupt_after_zero import CronPatchInterruptAfterZero

CronPatchInterruptAfter = typing.Union[CronPatchInterruptAfterZero, typing.List[str]]
