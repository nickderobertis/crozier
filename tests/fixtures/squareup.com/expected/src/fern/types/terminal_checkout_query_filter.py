

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .time_range import TimeRange


class TerminalCheckoutQueryFilter(UniversalBaseModel):
    """ """

    created_at: typing.Optional[TimeRange] = None
    device_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `TerminalCheckout` objects associated with a specific device. If no device is specified, then all
    `TerminalCheckout` objects for the merchant are displayed.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Filtered results with the desired status of the `TerminalCheckout`.
    Options: PENDING, IN_PROGRESS, CANCELED, COMPLETED
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
