

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .free_form_text_form_field_canned_responses import FreeFormTextFormFieldCannedResponses
from .free_form_text_form_field_default_keyboard import FreeFormTextFormFieldDefaultKeyboard
from .free_form_text_form_field_type import FreeFormTextFormFieldType


class FreeFormTextFormField(UniversalBaseModel):
    canned_responses: typing_extensions.Annotated[
        typing.Optional[FreeFormTextFormFieldCannedResponses],
        FieldMetadata(alias="cannedResponses"),
        pydantic.Field(alias="cannedResponses"),
    ] = None
    default_keyboard: typing_extensions.Annotated[
        typing.Optional[FreeFormTextFormFieldDefaultKeyboard],
        FieldMetadata(alias="defaultKeyboard"),
        pydantic.Field(alias="defaultKeyboard"),
    ] = None
    number_of_lines: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="numberOfLines"), pydantic.Field(alias="numberOfLines")
    ] = None
    type: typing.Optional[FreeFormTextFormFieldType] = pydantic.Field(default=None)
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
