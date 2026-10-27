

import typing

ChatMessageFromUserUserIdentityType = typing.Union[
    typing.Literal[
        "aadUser",
        "onPremiseAadUser",
        "anonymousGuest",
        "federatedUser",
        "personalMicrosoftAccountUser",
        "skypeUser",
        "phoneUser",
        "emailUser",
        "azureCommunicationServicesUser",
    ],
    typing.Any,
]
