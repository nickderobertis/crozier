

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .date_selection_form_field_type import DateSelectionFormFieldType


class DateSelectionFormField(UniversalBaseModel):
    days_allowed_in_future: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="daysAllowedInFuture"), pydantic.Field(alias="daysAllowedInFuture")
    ] = None
    default_today: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="defaultToday"),
        pydantic.Field(
            alias="defaultToday", description="Whether the value of this field should default to the current day"
        ),
    ] = None
    """
    Whether the value of this field should default to the current day
    """

    type: typing.Optional[DateSelectionFormFieldType] = pydantic.Field(default=None)
    """
    The type of this form field. Type declares how this field behaves and dictates the additional properties passed along with the required properties like label and key
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
