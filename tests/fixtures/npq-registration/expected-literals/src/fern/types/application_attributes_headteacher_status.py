

import typing

ApplicationAttributesHeadteacherStatus = typing.Union[
    typing.Literal[
        "no",
        "yes_when_course_starts",
        "yes_in_first_two_years",
        "yes_over_two_years",
        "yes_in_first_five_years",
        "yes_over_five_years",
    ],
    typing.Any,
]
