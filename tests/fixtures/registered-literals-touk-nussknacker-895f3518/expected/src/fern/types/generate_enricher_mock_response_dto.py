

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .expression import Expression


class GenerateEnricherMockResponseDto(UniversalBaseModel):
    enricher_mock_expression: typing_extensions.Annotated[
        Expression, FieldMetadata(alias="enricherMockExpression"), pydantic.Field(alias="enricherMockExpression")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
