

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .form_field_option import FormFieldOption
from .form_field_type import FormFieldType


class FormField(UniversalBaseModel):
    allow_custom_values: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Only applicable to select fields. Allow the user to add a custom value though the option select if the desired value is not in the option select list.
    """

    custom_field: typing.Optional[bool] = None
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the form field
    """

    disabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates if the form field is displayed in a “read-only” mode.
    """

    hidden: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates if the form field is not displayed but the value that is being stored on the connection.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the form field.
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    The label of the field
    """

    options: typing.Optional[typing.List[FormFieldOption]] = None
    placeholder: typing.Optional[str] = pydantic.Field(default=None)
    """
    The placeholder for the form field
    """

    prefix: typing.Optional[str] = pydantic.Field(default=None)
    """
    Prefix to display in front of the form field.
    """

    required: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates if the form field is required, which means it must be filled in before the form can be submitted
    """

    sensitive: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates if the form field contains sensitive data, which will display the value as a masked input.
    """

    suffix: typing.Optional[str] = pydantic.Field(default=None)
    """
    Suffix to display next to the form field.
    """

    type: typing.Optional[FormFieldType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
