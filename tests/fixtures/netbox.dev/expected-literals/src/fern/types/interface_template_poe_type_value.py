

import typing

InterfaceTemplatePoeTypeValue = typing.Union[
    typing.Literal[
        "type1-ieee802.3af",
        "type2-ieee802.3at",
        "type2-ieee802.3az",
        "type3-ieee802.3bt",
        "type4-ieee802.3bt",
        "passive-24v-2pair",
        "passive-24v-4pair",
        "passive-48v-2pair",
        "passive-48v-4pair",
    ],
    typing.Any,
]
