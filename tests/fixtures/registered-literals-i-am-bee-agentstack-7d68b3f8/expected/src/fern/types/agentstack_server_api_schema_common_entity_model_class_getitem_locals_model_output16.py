

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .vector_store_stats import VectorStoreStats


class AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput16(UniversalBaseModel):
    id: str
    name: typing.Optional[str] = None
    model_id: str
    dimension: int
    created_at: typing.Optional[dt.datetime] = None
    last_active_at: typing.Optional[dt.datetime] = None
    created_by: str
    stats: typing.Optional[VectorStoreStats] = None
    context_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
