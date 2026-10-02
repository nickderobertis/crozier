

import typing

OtoroshiSslCertCertType = typing.Union[
    typing.Literal["client", "ca", "letsEncrypt", "keypair", "selfSigned", "certificate"], typing.Any
]
