

import typing

RequestIndication = typing.Union[
    typing.Literal[
        "UE_REQ_PDU_SES_MOD",
        "UE_REQ_PDU_SES_REL",
        "PDU_SES_MOB",
        "NW_REQ_PDU_SES_AUTH",
        "NW_REQ_PDU_SES_MOD",
        "NW_REQ_PDU_SES_REL",
        "EBI_ASSIGNMENT_REQ",
    ],
    typing.Any,
]
