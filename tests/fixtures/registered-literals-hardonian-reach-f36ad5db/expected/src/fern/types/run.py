

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_status import RunStatus
from .run_tier import RunTier


class Run(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique run identifier
    """

    status: RunStatus
    tier: typing.Optional[RunTier] = None
    capabilities: typing.Optional[typing.List[str]] = None
    created_at: dt.datetime
    completed_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
