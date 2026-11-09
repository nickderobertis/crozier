

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .login_step_display_and_wait_display_and_wait_type import LoginStepDisplayAndWaitDisplayAndWaitType


class LoginStepDisplayAndWaitDisplayAndWait(UniversalBaseModel):
    """
    Parameters for the display and wait login step
    """

    type: LoginStepDisplayAndWaitDisplayAndWaitType = pydantic.Field()
    """
    The type of thing to display
    """

    data: typing.Optional[str] = pydantic.Field(default=None)
    """
    The thing to display (raw data for QR, unicode emoji for emoji, plain string for code)
    """

    image_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    An image containing the thing to display. If present, this is recommended over using data directly. For emojis, the URL to the canonical image representation of the emoji
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
