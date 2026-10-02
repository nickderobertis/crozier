

import typing

DocPagesExtract404ResponseCode = typing.Union[
    typing.Literal[
        "Unknown",
        "InvalidArg",
        "DocNotOpen",
        "DocOpenFailed",
        "DocPasswordRequired",
        "DocPasswordIncorrect",
        "SharePasswordRequired",
        "Aborted",
        "Network",
        "Unauthenticated",
        "Forbidden",
        "NotFound",
        "WireFormat",
        "RuntimeUnavailable",
        "InvalidReference",
        "WeakAnnotationSessionConflict",
        "LayerVersionConflict",
        "NotImplemented",
        "MalformedPdf",
        "SigningPending",
        "SigningExpired",
        "SigningVersionMismatch",
        "SignatureRefused",
        "ProtectedDocument",
        "StaleBase",
    ],
    typing.Any,
]
