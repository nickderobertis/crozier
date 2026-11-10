

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dashboard_user_id import DashboardUserId
from .dashboard_user_status import DashboardUserStatus
from .email_address import EmailAddress
from .request_id import RequestId
from .timestamp import Timestamp


class DashboardUserGetResponse(UniversalBaseModel):
    """
    Account information associated with a team member with access to the Plaid dashboard.
    """

    created_at: Timestamp
    email_address: EmailAddress
    id: DashboardUserId
    request_id: RequestId
    status: DashboardUserStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
