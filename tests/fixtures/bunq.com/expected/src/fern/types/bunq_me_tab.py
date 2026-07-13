

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bunq_me_tab_entry import BunqMeTabEntry


class BunqMeTab(UniversalBaseModel):
    bunqme_tab_entry: BunqMeTabEntry = pydantic.Field()
    """
    The bunq.me entry containing the payment information.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the bunq.me. Ignored in POST requests but can be used for cancelling the bunq.me by setting status as CANCELLED with a PUT request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
