

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ingest_response_model import IngestResponseModel
from .ingest_response_object import IngestResponseObject
from .ingested_doc import IngestedDoc


class IngestResponse(UniversalBaseModel):
    object: IngestResponseObject
    model: IngestResponseModel
    data: typing.List[IngestedDoc]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
