

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .field import Field


class Mention(UniversalBaseModel):
    """
    A dynamic placeholder that references another field's value. Used to personalize form content (e.g., "Hello @name").
    """

    uuid_: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="uuid"),
        pydantic.Field(alias="uuid", description="Unique identifier for this mention."),
    ]
    """
    Unique identifier for this mention.
    """

    field: Field = pydantic.Field()
    """
    The field being referenced. Its value replaces the mention placeholder at runtime.
    """

    default_value: typing_extensions.Annotated[
        typing.Optional[typing.Any],
        FieldMetadata(alias="defaultValue"),
        pydantic.Field(
            alias="defaultValue", description="Fallback value displayed when the referenced field has no data."
        ),
    ] = None
    """
    Fallback value displayed when the referenced field has no data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
