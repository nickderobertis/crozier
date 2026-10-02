

import typing

PostSendLinkedOtpResponseErrorsItemErrorCode = typing.Union[
    typing.Literal[
        "invalid_transaction",
        "invalid_transaction_id",
        "invalid_identifier",
        "invalid_otp_channel",
        "send_otp_failed",
        "unknown_error",
    ],
    typing.Any,
]
