

import typing

PostSendOtpResponseErrorsItemErrorCode = typing.Union[
    typing.Literal[
        "invalid_transaction",
        "invalid_transaction_id",
        "invalid_identifier",
        "invalid_otp_channel",
        "invalid_captcha",
        "send_otp_failed",
        "unknown_error",
    ],
    typing.Any,
]
