

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dashboard_user_id_nullable import DashboardUserIdNullable
from .source import Source
from .timestamp import Timestamp


class WatchlistScreeningAuditTrail(UniversalBaseModel):
    """
    Information about the last change made to the parent object specifying what caused the change as well as when it occurred.
    """

    dashboard_user_id: typing.Optional[DashboardUserIdNullable] = None
    source: Source
    timestamp: Timestamp

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
