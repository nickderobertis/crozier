

import typing

TimeOffRequestStatus = typing.Union[
    typing.Literal["requested", "approved", "declined", "cancelled", "deleted", "other"], typing.Any
]
