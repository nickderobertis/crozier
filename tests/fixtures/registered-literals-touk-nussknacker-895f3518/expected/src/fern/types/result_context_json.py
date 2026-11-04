

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .context_id_dto import ContextIdDto
from .map_json import MapJson


class ResultContextJson(UniversalBaseModel):
    id: ContextIdDto
    timestamp: dt.datetime
    variables: MapJson

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
