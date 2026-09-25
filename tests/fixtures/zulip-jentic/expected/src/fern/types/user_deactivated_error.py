

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UserDeactivatedError(UniversalBaseModel):
    """
    ### User account deactivated

    A typical failed json response for when user's account is deactivated.

    **Changes**: As of Zulip 5.0 (feature level 76), these errors use the
    HTTP 401 status code. Before this feature level, they used the HTTP 403
    status code.
    """

    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    code: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
