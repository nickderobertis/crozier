

import typing

LoginMethods = typing.Union[
    typing.Literal[
        "publickey",
        "password",
        "password-over-SSH",
        "keyboard-interactive",
        "publickey+password",
        "publickey+keyboard-interactive",
        "TLSCertificate",
        "TLSCertificate+password",
    ],
    typing.Any,
]
