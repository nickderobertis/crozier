

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PostSearchRequestSort(UniversalBaseModel):
    """
    A set of criteria, `direction` and `timestamp` keys, that orders the results. The **only** supported timestamp value is `"last_edited_time"`. Supported `direction` values are `"ascending"` and `"descending"`. If `sort` is not provided, then the most recently edited results are returned first.
    """

    direction: typing.Optional[str] = pydantic.Field(default=None)
    """
    The direction to sort. Possible values include `ascending` and `descending`.
    """

    timestamp: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the timestamp to sort against. Possible values include `last_edited_time`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
