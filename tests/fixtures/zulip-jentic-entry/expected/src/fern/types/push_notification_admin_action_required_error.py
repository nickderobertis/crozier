

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PushNotificationAdminActionRequiredError(UniversalBaseModel):
    """
    ## Admin action required

    A typical failed JSON response for when there is a push notification
    configuration issue on the server, such as invalid credentials,
    an expired plan, or an unregistered organization. Admin action is required.
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
