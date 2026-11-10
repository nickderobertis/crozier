

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ingestion_error import IngestionError
from .ingestion_success import IngestionSuccess


class IngestionResponse(UniversalBaseModel):
    successes: typing.List[IngestionSuccess]
    errors: typing.List[IngestionError]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
