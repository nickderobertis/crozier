

import typing

from .cron_patch_interrupt_before_zero import CronPatchInterruptBeforeZero

CronPatchInterruptBefore = typing.Union[CronPatchInterruptBeforeZero, typing.List[str]]
