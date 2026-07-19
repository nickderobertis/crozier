

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TemplatesGetTemplateSnapshotResponseType(enum.StrEnum):
    CLASSIC = "classic"
    CLUSTER = "cluster"
    SLEEPTIME = "sleeptime"
    ROUND_ROBIN = "round_robin"
    SUPERVISOR = "supervisor"
    DYNAMIC = "dynamic"
    VOICE_SLEEPTIME = "voice_sleeptime"

    def visit(
        self,
        classic: typing.Callable[[], T_Result],
        cluster: typing.Callable[[], T_Result],
        sleeptime: typing.Callable[[], T_Result],
        round_robin: typing.Callable[[], T_Result],
        supervisor: typing.Callable[[], T_Result],
        dynamic: typing.Callable[[], T_Result],
        voice_sleeptime: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TemplatesGetTemplateSnapshotResponseType.CLASSIC:
            return classic()
        if self is TemplatesGetTemplateSnapshotResponseType.CLUSTER:
            return cluster()
        if self is TemplatesGetTemplateSnapshotResponseType.SLEEPTIME:
            return sleeptime()
        if self is TemplatesGetTemplateSnapshotResponseType.ROUND_ROBIN:
            return round_robin()
        if self is TemplatesGetTemplateSnapshotResponseType.SUPERVISOR:
            return supervisor()
        if self is TemplatesGetTemplateSnapshotResponseType.DYNAMIC:
            return dynamic()
        if self is TemplatesGetTemplateSnapshotResponseType.VOICE_SLEEPTIME:
            return voice_sleeptime()
