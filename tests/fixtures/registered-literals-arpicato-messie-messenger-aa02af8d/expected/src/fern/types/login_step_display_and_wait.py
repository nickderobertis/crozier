

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .login_step_display_and_wait_display_and_wait import LoginStepDisplayAndWaitDisplayAndWait


class LoginStepDisplayAndWait(UniversalBaseModel):
    """
    Display and wait login step
    """

    display_and_wait: LoginStepDisplayAndWaitDisplayAndWait = pydantic.Field()
    """
    Parameters for the display and wait login step
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
