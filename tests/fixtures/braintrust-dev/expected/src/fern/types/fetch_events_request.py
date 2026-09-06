

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .fetch_limit import FetchLimit
from .fetch_pagination_cursor import FetchPaginationCursor
from .max_root_span_id import MaxRootSpanId
from .max_xact_id import MaxXactId
from .version import Version


class FetchEventsRequest(UniversalBaseModel):
    limit: typing.Optional[FetchLimit] = None
    cursor: typing.Optional[FetchPaginationCursor] = None
    max_xact_id: typing.Optional[MaxXactId] = None
    max_root_span_id: typing.Optional[MaxRootSpanId] = None
    version: typing.Optional[Version] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
