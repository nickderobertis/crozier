

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2cancel_table_runs_data import V2CancelTableRunsData


class V2CancelTableRunsResponse(UniversalBaseModel):
    """
    Count of canceled table cell runs.
    """

    data: V2CancelTableRunsData = pydantic.Field()
    """
    Response data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
