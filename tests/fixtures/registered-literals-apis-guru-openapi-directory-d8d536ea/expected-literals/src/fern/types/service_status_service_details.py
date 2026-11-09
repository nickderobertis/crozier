

import typing

ServiceStatusServiceDetails = typing.Union[
    typing.Literal[
        "acceptingCaseUpdates",
        "notAcceptingCaseUpdates",
        "acceptingCaseTrack",
        "notAcceptingCaseTrack",
        "acceptingAutoDocOrders",
        "acceptingManualDocOrders",
        "notAcceptingAutoDocOrdersLimitExceeded",
        "notAcceptingManualDocOrdersLimitExceeded",
        "notAcceptingDocOrders",
    ],
    typing.Any,
]
