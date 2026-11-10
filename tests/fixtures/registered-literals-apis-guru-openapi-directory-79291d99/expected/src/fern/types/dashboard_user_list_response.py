

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cursor import Cursor
from .dashboard_user import DashboardUser
from .request_id import RequestId


class DashboardUserListResponse(UniversalBaseModel):
    """
    Paginated list of dashboard users
    """

    dashboard_users: typing.List[DashboardUser] = pydantic.Field()
    """
    List of dashboard users
    """

    next_cursor: typing.Optional[Cursor] = None
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
