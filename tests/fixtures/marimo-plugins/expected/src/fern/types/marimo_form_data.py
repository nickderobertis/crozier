

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MarimoFormData(UniversalBaseModel):
    label: typing.Optional[str] = None
    element_id: typing_extensions.Annotated[str, FieldMetadata(alias="elementId"), pydantic.Field(alias="elementId")]
    bordered: typing.Optional[bool] = None
    loading: typing.Optional[bool] = None
    submit_button_label: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="submitButtonLabel"), pydantic.Field(alias="submitButtonLabel")
    ] = None
    submit_button_tooltip: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="submitButtonTooltip"), pydantic.Field(alias="submitButtonTooltip")
    ] = None
    submit_button_disabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="submitButtonDisabled"), pydantic.Field(alias="submitButtonDisabled")
    ] = None
    clear_on_submit: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="clearOnSubmit"), pydantic.Field(alias="clearOnSubmit")
    ] = None
    show_clear_button: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="showClearButton"), pydantic.Field(alias="showClearButton")
    ] = None
    clear_button_label: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="clearButtonLabel"), pydantic.Field(alias="clearButtonLabel")
    ] = None
    clear_button_tooltip: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="clearButtonTooltip"), pydantic.Field(alias="clearButtonTooltip")
    ] = None
    should_validate: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="shouldValidate"), pydantic.Field(alias="shouldValidate")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
