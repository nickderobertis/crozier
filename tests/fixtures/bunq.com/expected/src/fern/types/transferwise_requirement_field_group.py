

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transferwise_requirement_field_group_validation_async import TransferwiseRequirementFieldGroupValidationAsync
from .transferwise_requirement_field_group_values_allowed import TransferwiseRequirementFieldGroupValuesAllowed


class TransferwiseRequirementFieldGroup(UniversalBaseModel):
    display_format: typing.Optional[str] = pydantic.Field(default=None)
    """
    Formatting mask to guide user input.
    """

    example: typing.Optional[str] = pydantic.Field(default=None)
    """
    An example value for this field.
    """

    key: typing.Optional[str] = pydantic.Field(default=None)
    """
    The key of the field. This is the value to send as input.
    """

    max_length: typing.Optional[str] = pydantic.Field(default=None)
    """
    The maximum length of the field's value.
    """

    min_length: typing.Optional[str] = pydantic.Field(default=None)
    """
    The minimum length of the field's value.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The field name.
    """

    refresh_requirements_on_change: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates that any changes in this field affect the requirements, if this field is changed, the requirements endpoint must be called again to recheck if there are any additional requirements.
    """

    required: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the field is required.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The field's input type: "text", "select" or "radio".
    """

    validation_async: typing.Optional[TransferwiseRequirementFieldGroupValidationAsync] = pydantic.Field(default=None)
    """
    Details of an endpoint which may be used to validate the user input.
    """

    validation_regexp: typing.Optional[str] = pydantic.Field(default=None)
    """
    A regular expression which may be used to validate the user input.
    """

    values_allowed: typing.Optional[TransferwiseRequirementFieldGroupValuesAllowed] = pydantic.Field(default=None)
    """
    Shows which values are allowed for fields of type "select" or "radio".
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
