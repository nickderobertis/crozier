

import typing

JobStagesStageName = typing.Union[
    typing.Literal[
        "DeviceOrdered",
        "DevicePrepared",
        "Dispatched",
        "Delivered",
        "PickedUp",
        "AtAzureDC",
        "DataCopy",
        "Completed",
        "CompletedWithErrors",
        "Cancelled",
        "Failed_IssueReportedAtCustomer",
        "Failed_IssueDetectedAtAzureDC",
        "Aborted",
        "CompletedWithWarnings",
        "ReadyToDispatchFromAzureDC",
        "ReadyToReceiveAtAzureDC",
    ],
    typing.Any,
]
