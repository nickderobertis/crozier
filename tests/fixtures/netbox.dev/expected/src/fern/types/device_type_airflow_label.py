

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DeviceTypeAirflowLabel(str, enum.Enum):
    FRONT_TO_REAR = "Front to rear"
    REAR_TO_FRONT = "Rear to front"
    LEFT_TO_RIGHT = "Left to right"
    RIGHT_TO_LEFT = "Right to left"
    SIDE_TO_REAR = "Side to rear"
    PASSIVE = "Passive"
    MIXED = "Mixed"

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
        if self is DeviceTypeAirflowLabel.FRONT_TO_REAR:
            return front_to_rear()
        if self is DeviceTypeAirflowLabel.REAR_TO_FRONT:
            return rear_to_front()
        if self is DeviceTypeAirflowLabel.LEFT_TO_RIGHT:
            return left_to_right()
        if self is DeviceTypeAirflowLabel.RIGHT_TO_LEFT:
            return right_to_left()
        if self is DeviceTypeAirflowLabel.SIDE_TO_REAR:
            return side_to_rear()
        if self is DeviceTypeAirflowLabel.PASSIVE:
            return passive()
        if self is DeviceTypeAirflowLabel.MIXED:
            return mixed()
