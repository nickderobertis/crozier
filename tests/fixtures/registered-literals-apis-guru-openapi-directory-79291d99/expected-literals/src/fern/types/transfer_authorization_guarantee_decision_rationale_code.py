

import typing

TransferAuthorizationGuaranteeDecisionRationaleCode = typing.Union[
    typing.Literal[
        "RETURN_BANK",
        "RETURN_CUSTOMER",
        "GUARANTEE_LIMIT_REACHED",
        "RISK_ESTIMATE_UNAVAILABLE",
        "REQUIRED_PARAM_MISSING",
    ],
    typing.Any,
]
