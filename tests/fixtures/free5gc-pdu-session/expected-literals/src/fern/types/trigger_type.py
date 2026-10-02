

import typing

TriggerType = typing.Union[
    typing.Literal[
        "QUOTA_THRESHOLD",
        "QHT",
        "FINAL",
        "QUOTA_EXHAUSTED",
        "VALIDITY_TIME",
        "OTHER_QUOTA_TYPE",
        "FORCED_REAUTHORISATION",
        "UNUSED_QUOTA_TIMER",
        "ABNORMAL_RELEASE",
        "QOS_CHANGE",
        "VOLUME_LIMIT",
        "TIME_LIMIT",
        "PLMN_CHANGE",
        "USER_LOCATION_CHANGE",
        "RAT_CHANGE",
        "UE_TIMEZONE_CHANGE",
        "TARIFF_TIME_CHANGE",
        "MAX_NUMBER_OF_CHANGES_IN CHARGING_CONDITIONS",
        "MANAGEMENT_INTERVENTION",
        "CHANGE_OF_UE_PRESENCE_IN PRESENCE_REPORTING_AREA",
        "CHANGE_OF_3GPP_PS_DATA_OFF_STATUS",
        "SERVING_NODE_CHANGE",
        "REMOVAL_OF_UPF",
        "ADDITION_OF_UPF",
    ],
    typing.Any,
]
