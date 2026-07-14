

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_status_state import AccountStatusState


class AccountStatus(UniversalBaseModel):
    """
    A summary of account status
    """

    state: typing.Optional[AccountStatusState] = pydantic.Field(default=None)
    """
    The status of the account
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
