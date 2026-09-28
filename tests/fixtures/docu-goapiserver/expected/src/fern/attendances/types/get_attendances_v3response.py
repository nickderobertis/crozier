

import typing

from ...types.attendance import Attendance
from ...types.attendance_aggregate import AttendanceAggregate

GetAttendancesV3Response = typing.Union[typing.List[Attendance], typing.List[AttendanceAggregate]]
