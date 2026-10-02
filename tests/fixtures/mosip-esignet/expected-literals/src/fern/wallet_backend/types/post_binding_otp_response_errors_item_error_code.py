

import typing

PostBindingOtpResponseErrorsItemErrorCode = typing.Union[
    typing.Literal[
        "invalid_otp_channel", "unknown_error", "invalid_individual_id", "send_otp_failed", "invalid_captcha"
    ],
    typing.Any,
]
