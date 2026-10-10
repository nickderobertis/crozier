

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .annotated_signature import AnnotatedSignature


class GenericProperty(UniversalBaseModel):
    signatures: typing.List[AnnotatedSignature]
    sequence_number: typing_extensions.Annotated[
        float, FieldMetadata(alias="sequenceNumber"), pydantic.Field(alias="sequenceNumber")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
