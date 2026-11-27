

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .string_select_form_field_form_factor import StringSelectFormFieldFormFactor
from .string_select_form_field_option import StringSelectFormFieldOption
from .string_select_form_field_type import StringSelectFormFieldType


class StringSelectFormField(UniversalBaseModel):
    form_factor: typing_extensions.Annotated[
        typing.Optional[StringSelectFormFieldFormFactor],
        FieldMetadata(alias="formFactor"),
        pydantic.Field(alias="formFactor"),
    ] = None
    max_selections: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxSelections"), pydantic.Field(alias="maxSelections")
    ] = None
    options: typing.Optional[typing.List[StringSelectFormFieldOption]] = None
    type: typing.Optional[StringSelectFormFieldType] = pydantic.Field(default=None)
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
