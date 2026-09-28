

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SchoolRefreshProcess(UniversalBaseModel):
    """
    School Refresh Process.
    """

    task_name: str
    last_data_refresh_at: str = pydantic.Field()
    """
    Display timestamp: YYYY-MM-DD HH:mm EDT; the suffix is literal.
    """

    status: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
