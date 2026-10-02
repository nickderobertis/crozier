

import typing

GetAttendancesV3RequestSortBy = typing.Union[
    typing.Literal[
        "group_asc",
        "group_desc",
        "attendance_days_asc",
        "attendance_days_desc",
        "total_records_asc",
        "total_records_desc",
        "sum_hours_asc",
        "sum_hours_desc",
        "avg_hours_asc",
        "avg_hours_desc",
        "distinct_students_asc",
        "distinct_students_desc",
    ],
    typing.Any,
]
