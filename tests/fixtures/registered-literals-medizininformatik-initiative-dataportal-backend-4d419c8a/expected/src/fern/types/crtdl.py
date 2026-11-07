

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ccdl import Ccdl
from .data_extraction_query import DataExtractionQuery


class Crtdl(UniversalBaseModel):
    display: typing.Optional[str] = None
    cohort_definition: typing_extensions.Annotated[
        typing.Optional[Ccdl], FieldMetadata(alias="cohortDefinition"), pydantic.Field(alias="cohortDefinition")
    ] = None
    data_extraction: typing_extensions.Annotated[
        typing.Optional[DataExtractionQuery],
        FieldMetadata(alias="dataExtraction"),
        pydantic.Field(alias="dataExtraction"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
