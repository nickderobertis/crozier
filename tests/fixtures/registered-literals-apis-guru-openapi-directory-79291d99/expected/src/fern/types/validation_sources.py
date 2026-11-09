

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .validation_source import ValidationSource


class ValidationSources(UniversalBaseModel):
    """
    Documentation not found in the MISMO model viewer and not provided by Freddie Mac.
    """

    validation_source: typing_extensions.Annotated[
        typing.List[ValidationSource],
        FieldMetadata(alias="VALIDATION_SOURCE"),
        pydantic.Field(
            alias="VALIDATION_SOURCE",
            description="Documentation not found in the MISMO model viewer and not provided by Freddie Mac.",
        ),
    ]
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
