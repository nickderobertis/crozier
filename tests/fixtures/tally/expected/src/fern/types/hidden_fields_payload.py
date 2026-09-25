

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .hidden_field import HiddenField


class HiddenFieldsPayload(UniversalBaseModel):
    """
    Payload for HIDDEN_FIELDS block type. Used for hidden form fields.
    """

    hidden_fields: typing_extensions.Annotated[
        typing.List[HiddenField],
        FieldMetadata(alias="hiddenFields"),
        pydantic.Field(
            alias="hiddenFields",
            description="Array of hidden fields. Each hidden field captures a value from URL query parameters matching the field name.",
        ),
    ]
    """
    Array of hidden fields. Each hidden field captures a value from URL query parameters matching the field name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
