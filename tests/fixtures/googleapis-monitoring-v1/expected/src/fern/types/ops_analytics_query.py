

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OpsAnalyticsQuery(UniversalBaseModel):
    """
    Preview: A query that produces an aggregated response and supporting data. This is a preview feature and may be subject to change before final release.
    """

    sql: typing.Optional[str] = pydantic.Field(default=None)
    """
    A SQL query to fetch time series, category series, or numeric series data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
