

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DeviceAirflowValue(str, enum.Enum):
    FRONT_TO_REAR = "front-to-rear"
    REAR_TO_FRONT = "rear-to-front"
    LEFT_TO_RIGHT = "left-to-right"
    RIGHT_TO_LEFT = "right-to-left"
    SIDE_TO_REAR = "side-to-rear"
    PASSIVE = "passive"
    MIXED = "mixed"

    def visit(
        self,
        front_to_rear: typing.Callable[[], T_Result],
        rear_to_front: typing.Callable[[], T_Result],
        left_to_right: typing.Callable[[], T_Result],
        right_to_left: typing.Callable[[], T_Result],
        side_to_rear: typing.Callable[[], T_Result],
        passive: typing.Callable[[], T_Result],
        mixed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DeviceAirflowValue.FRONT_TO_REAR:
            return front_to_rear()
        if self is DeviceAirflowValue.REAR_TO_FRONT:
            return rear_to_front()
        if self is DeviceAirflowValue.LEFT_TO_RIGHT:
            return left_to_right()
        if self is DeviceAirflowValue.RIGHT_TO_LEFT:
            return right_to_left()
        if self is DeviceAirflowValue.SIDE_TO_REAR:
            return side_to_rear()
        if self is DeviceAirflowValue.PASSIVE:
            return passive()
        if self is DeviceAirflowValue.MIXED:
            return mixed()
