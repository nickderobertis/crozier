

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .field_element import FieldElement


class InclusionProofProofItemRight(UniversalBaseModel):
    right: typing_extensions.Annotated[
        typing.Optional[FieldElement], FieldMetadata(alias="Right"), pydantic.Field(alias="Right")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
