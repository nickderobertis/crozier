

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .login_step_user_input_user_input_fields_item import LoginStepUserInputUserInputFieldsItem


class LoginStepUserInputUserInput(UniversalBaseModel):
    """
    Parameters for the user input login step
    """

    fields: typing.List[LoginStepUserInputUserInputFieldsItem] = pydantic.Field()
    """
    The list of fields that the user is requested to fill.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
