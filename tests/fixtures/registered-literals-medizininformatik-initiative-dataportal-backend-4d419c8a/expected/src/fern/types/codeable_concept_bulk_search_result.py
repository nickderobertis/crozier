

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .codeable_concept_entry import CodeableConceptEntry


class CodeableConceptBulkSearchResult(UniversalBaseModel):
    found: typing.Optional[typing.List[CodeableConceptEntry]] = None
    not_found: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="notFound"), pydantic.Field(alias="notFound")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
