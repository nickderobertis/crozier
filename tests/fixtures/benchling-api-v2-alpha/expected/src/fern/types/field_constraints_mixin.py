

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .app_config_field_type import AppConfigFieldType


class FieldConstraintsMixin(UniversalBaseModel):
    is_multi: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isMulti"),
        pydantic.Field(alias="isMulti", description="Schema field's isMulti property, or null for either."),
    ] = None
    """
    Schema field's isMulti property, or null for either.
    """

    is_required: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isRequired"),
        pydantic.Field(alias="isRequired", description="Schema field's isRequired property, or null for either."),
    ] = None
    """
    Schema field's isRequired property, or null for either.
    """

    type: typing.Optional[AppConfigFieldType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
