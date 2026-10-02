

import typing

OauthScope = typing.Union[
    typing.Literal[
        "AdminGroups",
        "AdvancedWriteActions",
        "BnetWrite",
        "DestinyUnlockValueQuery",
        "EditUserData",
        "MoveEquipDestinyItems",
        "PartnerOfferGrant",
        "ReadAndApplyTokens",
        "ReadBasicUserProfile",
        "ReadDestinyInventoryAndVault",
        "ReadDestinyVendorsAndAdvisors",
        "ReadGroups",
        "ReadUserData",
        "UserPiiRead",
        "WriteGroups",
    ],
    typing.Any,
]
