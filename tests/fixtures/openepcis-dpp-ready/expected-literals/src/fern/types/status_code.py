

import typing

StatusCode = typing.Union[
    typing.Literal[
        "Success",
        "SuccessCreated",
        "SuccessAccepted",
        "SuccessNoContent",
        "ClientErrorBadRequest",
        "ClientNotAuthorized",
        "ClientForbidden",
        "ClientMethodNotAllowed",
        "ClientErrorResourceNotFound",
        "ClientResourceConflict",
        "ServerInternalError",
        "ServerNotImplemented",
        "ServerErrorBadGateway",
    ],
    typing.Any,
]
