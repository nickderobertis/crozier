

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .login_step_user_input_user_input_fields_item_type import LoginStepUserInputUserInputFieldsItemType


class LoginStepUserInputUserInputFieldsItem(UniversalBaseModel):
    """
    A field that the user can fill.
    """

    type: LoginStepUserInputUserInputFieldsItemType = pydantic.Field()
    """
    The type of field.
    """

    id: str = pydantic.Field()
    """
    The internal ID of the field. This must be used as the key in the object when submitting the data back to the bridge.
    """

    name: str = pydantic.Field()
    """
    The name of the field shown to the user.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A more detailed description of the field shown to the user.
    """

    pattern: typing.Optional[str] = pydantic.Field(default=None)
    """
    A regular expression that the field value must match.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
