

import typing

EventProtocols = typing.Union[
    typing.Literal["SSH", "SFTP", "SCP", "FTP", "DAV", "HTTP", "HTTPShare", "DataRetention", "EventAction", "OIDC"],
    typing.Any,
]
