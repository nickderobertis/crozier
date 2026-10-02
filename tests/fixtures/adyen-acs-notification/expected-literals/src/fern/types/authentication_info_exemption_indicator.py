

import typing

AuthenticationInfoExemptionIndicator = typing.Union[
    typing.Literal[
        "lowValue",
        "secureCorporate",
        "trustedBeneficiary",
        "transactionRiskAnalysis",
        "acquirerExemption",
        "noExemptionApplied",
        "visaDAFExemption",
    ],
    typing.Any,
]
