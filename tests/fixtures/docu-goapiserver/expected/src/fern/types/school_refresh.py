

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .school_refresh_process import SchoolRefreshProcess


class SchoolRefresh(UniversalBaseModel):
    """
    School Refresh.
    """

    school_name: str
    school_id: str = pydantic.Field()
    """
    School id.
    """

    processes: typing.List[SchoolRefreshProcess]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
