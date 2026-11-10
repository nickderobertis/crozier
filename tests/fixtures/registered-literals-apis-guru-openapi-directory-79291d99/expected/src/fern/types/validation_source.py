

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ValidationSource(UniversalBaseModel):
    """
    Documentation not found in the MISMO model viewer and not provided by Freddie Mac.
    """

    validation_source_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ValidationSourceName"),
        pydantic.Field(
            alias="ValidationSourceName",
            description="Documentation not found in the MISMO model viewer and not provided by Freddie Mac.",
        ),
    ] = None
    """
    Documentation not found in the MISMO model viewer and not provided by Freddie Mac.
    """

    validation_source_reference_identifier: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ValidationSourceReferenceIdentifier"),
        pydantic.Field(
            alias="ValidationSourceReferenceIdentifier",
            description="Documentation not found in the MISMO model viewer and not provided by Freddie Mac.",
        ),
    ] = None
    """
    Documentation not found in the MISMO model viewer and not provided by Freddie Mac.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
