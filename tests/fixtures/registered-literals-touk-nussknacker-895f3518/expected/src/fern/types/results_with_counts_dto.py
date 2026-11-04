

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .map_node_id_v import MapNodeIdV
from .test_results_dto import TestResultsDto


class ResultsWithCountsDto(UniversalBaseModel):
    timestamp: dt.datetime
    results: TestResultsDto
    counts: MapNodeIdV
    assertions_results: typing_extensions.Annotated[
        MapNodeIdV, FieldMetadata(alias="assertionsResults"), pydantic.Field(alias="assertionsResults")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
