

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MissionResetSnapshotUrl(enum.StrEnum):
    V1MISSION_CONTROL = "/v1/mission-control"

    def visit(self, v1mission_control: typing.Callable[[], T_Result]) -> T_Result:
        if self is MissionResetSnapshotUrl.V1MISSION_CONTROL:
            return v1mission_control()
