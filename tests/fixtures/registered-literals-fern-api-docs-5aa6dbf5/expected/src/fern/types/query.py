

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .query_status import QueryStatus


class Query(UniversalBaseModel):
    query_id: str
    conversation_id: str
    domain: str
    text: str
    role: str
    source: str
    created_at: dt.datetime
    time_to_first_token: typing.Optional[float] = None
    subqueries: typing.Optional[typing.List[str]] = None
    status: typing.Optional[QueryStatus] = None
    origin_page: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
