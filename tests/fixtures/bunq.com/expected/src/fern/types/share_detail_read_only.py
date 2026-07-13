

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ShareDetailReadOnly(UniversalBaseModel):
    view_balance: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If set to true, the invited user will be able to view the account balance.
    """

    view_new_events: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If set to true, the invited user will be able to view events starting from the time the share became active.
    """

    view_old_events: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If set to true, the invited user will be able to view events from before the share was active.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
