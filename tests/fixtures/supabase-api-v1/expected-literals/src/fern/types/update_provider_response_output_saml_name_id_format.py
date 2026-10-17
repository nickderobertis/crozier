

import typing

UpdateProviderResponseOutputSamlNameIdFormat = typing.Union[
    typing.Literal[
        "urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified",
        "urn:oasis:names:tc:SAML:2.0:nameid-format:transient",
        "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",
        "urn:oasis:names:tc:SAML:2.0:nameid-format:persistent",
    ],
    typing.Any,
]
