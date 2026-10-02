

import typing

AtsEventType = typing.Union[
    typing.Literal[
        "ats.job.created",
        "ats.job.updated",
        "ats.job.deleted",
        "ats.applicant.created",
        "ats.applicant.updated",
        "ats.applicant.deleted",
    ],
    typing.Any,
]
