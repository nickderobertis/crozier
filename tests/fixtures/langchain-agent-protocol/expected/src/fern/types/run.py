

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .run_status import RunStatus
from .run_stream import RunStream


class Run(RunStream):
    run_id: str = pydantic.Field()
    """
    The ID of the run.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    The time the run was created.
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    The last time the run was updated.
    """

    status: RunStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
