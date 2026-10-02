

import typing

AmfEventType = typing.Union[
    typing.Literal[
        "LOCATION_REPORT",
        "PRESENCE_IN_AOI_REPORT",
        "TIMEZONE_REPORT",
        "ACCESS_TYPE_REPORT",
        "REGISTRATION_STATE_REPORT",
        "CONNECTIVITY_STATE_REPORT",
        "REACHABILITY_REPORT",
        "SUBSCRIBED_DATA_REPORT",
        "COMMUNICATION_FAILURE_REPORT",
        "UES_IN_AREA_REPORT",
        "SUBSCRIPTION_ID_CHANGE",
        "SUBSCRIPTION_ID_ADDITION",
    ],
    typing.Any,
]
