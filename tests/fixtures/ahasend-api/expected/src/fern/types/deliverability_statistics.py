

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeliverabilityStatistics(UniversalBaseModel):
    from_timestamp: dt.datetime = pydantic.Field()
    """
    Start time of the statistics bucket
    """

    to_timestamp: dt.datetime = pydantic.Field()
    """
    End time of the statistics bucket
    """

    reception_count: int = pydantic.Field()
    """
    Number of messages accepted for delivery
    """

    delivered_count: int = pydantic.Field()
    """
    Number of messages delivered
    """

    deferred_count: int = pydantic.Field()
    """
    Number of messages deferred
    """

    bounced_count: int = pydantic.Field()
    """
    Number of messages bounced
    """

    failed_count: int = pydantic.Field()
    """
    Number of messages failed
    """

    suppressed_count: int = pydantic.Field()
    """
    Number of messages suppressed
    """

    opened_count: int = pydantic.Field()
    """
    Number of messages opened at least once
    """

    clicked_count: int = pydantic.Field()
    """
    Number of messages that have at least one link in them clicked.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
