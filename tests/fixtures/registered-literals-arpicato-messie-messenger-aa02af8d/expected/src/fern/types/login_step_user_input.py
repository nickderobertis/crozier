

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .login_step_user_input_user_input import LoginStepUserInputUserInput


class LoginStepUserInput(UniversalBaseModel):
    """
    User input login step
    """

    user_input: LoginStepUserInputUserInput = pydantic.Field()
    """
    Parameters for the user input login step
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
