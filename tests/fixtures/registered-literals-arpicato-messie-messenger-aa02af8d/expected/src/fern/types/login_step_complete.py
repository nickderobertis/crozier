

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .login_step_complete_complete import LoginStepCompleteComplete


class LoginStepComplete(UniversalBaseModel):
    """
    Login complete
    """

    complete: LoginStepCompleteComplete = pydantic.Field()
    """
    Information about the completed login
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
