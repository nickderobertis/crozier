

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cursor import Cursor
from .identity_verification import IdentityVerification
from .request_id import RequestId


class IdentityVerificationListResponse(UniversalBaseModel):
    """
    Paginated list of Plaid sessions.
    """

    identity_verifications: typing.List[IdentityVerification] = pydantic.Field()
    """
    List of Plaid sessions
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
