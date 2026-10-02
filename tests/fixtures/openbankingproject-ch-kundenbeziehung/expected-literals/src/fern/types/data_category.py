

import typing

DataCategory = typing.Union[
    typing.Literal[
        "basicData",
        "identification",
        "contactInformation",
        "addressData",
        "kycData",
        "riskProfile",
        "complianceData",
        "extendedData",
    ],
    typing.Any,
]
