

import typing

GetLeadsV3RequestStatus = typing.Union[
    typing.Literal[
        "New",
        "Contacted",
        "Tour Scheduled",
        "Tour Completed",
        "Tour No Show",
        "Discovery Day Scheduled",
        "Discovery Day Completed",
        "Discovery Day No Show",
        "Waitlisted",
        "Enrolled",
        "Lost",
        "No Status",
    ],
    typing.Any,
]
