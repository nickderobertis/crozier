

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SettingForm(UniversalBaseModel):
    """
    A single form group in a setting definition.
    """

    form_schema: typing_extensions.Annotated[
        typing.List[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="formSchema"),
        pydantic.Field(alias="formSchema", description="FormKit-compatible schema used to render the form fields."),
    ]
    """
    FormKit-compatible schema used to render the form fields.
    """

    group: str = pydantic.Field()
    """
    Stable form group name used to store submitted values.
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Display label shown for this form group.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
