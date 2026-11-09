

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.dashboard_response import DashboardResponse
from ...types.paginated_meta import PaginatedMeta


class DashboardsListResponse(UniversalBaseModel):
    meta: typing.Optional[PaginatedMeta] = None
    data: typing.Optional[typing.List[DashboardResponse]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
