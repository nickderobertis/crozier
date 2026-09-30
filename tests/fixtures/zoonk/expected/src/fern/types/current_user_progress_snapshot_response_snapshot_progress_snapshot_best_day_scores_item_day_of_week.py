

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CurrentUserProgressSnapshotResponseSnapshotProgressSnapshotBestDayScoresItemDayOfWeek(enum.StrEnum):
    SUNDAY = "sunday"
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"

    def visit(
        self,
        sunday: typing.Callable[[], T_Result],
        monday: typing.Callable[[], T_Result],
        tuesday: typing.Callable[[], T_Result],
        wednesday: typing.Callable[[], T_Result],
        thursday: typing.Callable[[], T_Result],
        friday: typing.Callable[[], T_Result],
        saturday: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CurrentUserProgressSnapshotResponseSnapshotProgressSnapshotBestDayScoresItemDayOfWeek.SUNDAY:
            return sunday()
        if self is CurrentUserProgressSnapshotResponseSnapshotProgressSnapshotBestDayScoresItemDayOfWeek.MONDAY:
            return monday()
        if self is CurrentUserProgressSnapshotResponseSnapshotProgressSnapshotBestDayScoresItemDayOfWeek.TUESDAY:
            return tuesday()
        if self is CurrentUserProgressSnapshotResponseSnapshotProgressSnapshotBestDayScoresItemDayOfWeek.WEDNESDAY:
            return wednesday()
        if self is CurrentUserProgressSnapshotResponseSnapshotProgressSnapshotBestDayScoresItemDayOfWeek.THURSDAY:
            return thursday()
        if self is CurrentUserProgressSnapshotResponseSnapshotProgressSnapshotBestDayScoresItemDayOfWeek.FRIDAY:
            return friday()
        if self is CurrentUserProgressSnapshotResponseSnapshotProgressSnapshotBestDayScoresItemDayOfWeek.SATURDAY:
            return saturday()
