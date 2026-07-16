

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .gift_card_activity import GiftCardActivity


class ListGiftCardActivitiesResponse(UniversalBaseModel):
    """
    A response that contains one or more `GiftCardActivity`. The response might contain a set of `Error` objects
    if the request resulted in errors.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    When a response is truncated, it includes a cursor that you can use in a
    subsequent request to fetch the next set of activities. If empty, this is
    the final response.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    gift_card_activities: typing.Optional[typing.List[GiftCardActivity]] = pydantic.Field(default=None)
    """
    Gift card activities retrieved.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
