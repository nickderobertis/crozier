

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class InvalidEntityTypeErrorErrorDetails(UniversalBaseModel):
    """
    Additional error details specific to the error type
    """

    entity_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="entityType"),
        pydantic.Field(alias="entityType", description="The actual entity type of the requested entity"),
    ] = None
    """
    The actual entity type of the requested entity
    """

    expected_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="expectedType"),
        pydantic.Field(alias="expectedType", description="The expected entity type for this operation"),
    ] = None
    """
    The expected entity type for this operation
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
