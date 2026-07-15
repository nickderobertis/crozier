

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pagination_coverage_mode import PaginationCoverageMode


class PaginationCoverage(UniversalBaseModel):
    limit_support: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the connector supports changing the page size by using the limit parameter.
    """

    mode: typing.Optional[PaginationCoverageMode] = pydantic.Field(default=None)
    """
    How pagination is implemented on this connector. Native mode means Apideck is using the pagination parameters of the connector. With virtual pagination, the connector does not support pagination, but Apideck emulates it.
    """

    paging_support: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the connector supports paging through results using the cursor parameter.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
