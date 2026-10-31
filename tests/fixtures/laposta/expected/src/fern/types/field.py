

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .field_datatype import FieldDatatype
from .field_datatype_display import FieldDatatypeDisplay
from .field_state import FieldState


class Field(UniversalBaseModel):
    """
    The field object
    """

    field_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the field in question
    """

    list_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the list to which the field belongs
    """

    timezone: typing.Optional[str] = pydantic.Field(default=None)
    """
    The account timezone used for datetime fields
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    Date and time of creation
    """

    created_iso: typing.Optional[str] = pydantic.Field(default=None)
    """
    Date and time of creation in ISO format
    """

    modified: typing.Optional[str] = pydantic.Field(default=None)
    """
    Always null. Field modification times are not stored and this field is kept for backwards compatibility.
    """

    state: typing.Optional[FieldState] = pydantic.Field(default=None)
    """
    The status of the field in question: either active or deleted
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the field (for displaying purposes)
    """

    tag: typing.Optional[str] = pydantic.Field(default=None)
    """
    The subscriber variable for usage in campaigns (not modifyable)
    """

    custom_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the field (for use in member API calls)
    """

    defaultvalue: typing.Optional[str] = pydantic.Field(default=None)
    """
    The default value (will be used in the absence of this field)
    """

    datatype: typing.Optional[FieldDatatype] = pydantic.Field(default=None)
    """
    The data type of the field in question (text, numeric, date, select_single, select_multiple or labels). The labels type belongs to the Labels field, which comes into being by itself as soon as your list has at least one label; you do not create that field yourself.
    """

    datatype_display: typing.Optional[FieldDatatypeDisplay] = pydantic.Field(default=None)
    """
    Only applicable for select_single: the desired display (select, radio)
    """

    options: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    An array of the available options (for select_single, select_multiple or labels). For a labels field, these are the labels of this list.
    """

    options_full: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    An array of the available options, including IDs (for select_single, select_multiple or labels).
    """

    required: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Is this a mandatory field? (true or false)
    """

    in_form: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Does this field occur in the subscription form? (true or false)
    """

    in_list: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Does this field occur while browsing the list? (true or false)
    """

    autocomplete: typing.Optional[str] = pydantic.Field(default=None)
    """
    The value for the html autocomplete attribute (string)
    """

    pos: typing.Optional[str] = pydantic.Field(default=None)
    """
    The position of this field in the list, as a string containing a number.
    """

    is_email: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this is the email field of the list.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
