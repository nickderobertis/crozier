

import typing

LinkEventName = typing.Union[
    typing.Literal[
        "BANK_INCOME_INSIGHTS_COMPLETED",
        "CLOSE_OAUTH",
        "ERROR",
        "EXIT",
        "FAIL_OAUTH",
        "HANDOFF",
        "OPEN",
        "OPEN_MY_PLAID",
        "OPEN_OAUTH",
        "SEARCH_INSTITUTION",
        "SELECT_AUTH_TYPE",
        "SELECT_BRAND",
        "SELECT_DEGRADED_INSTITUTION",
        "SELECT_DOWN_INSTITUTION",
        "SELECT_INSTITUTION",
        "SUBMIT_ACCOUNT_NUMBER",
        "SUBMIT_CREDENTIALS",
        "SUBMIT_DOCUMENTS",
        "SUBMIT_DOCUMENTS_ERROR",
        "SUBMIT_DOCUMENTS_SUCCESS",
        "SUBMIT_MFA",
        "SUBMIT_ROUTING_NUMBER",
        "TRANSITION_VIEW",
        "VIEW_DATA_TYPES",
    ],
    typing.Any,
]
