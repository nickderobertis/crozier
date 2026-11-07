

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address import Address
from .event_index import EventIndex
from .event_type import EventType


class Event(UniversalBaseModel):
    """
    A transaction or other event that affects the wallet including miner payouts, siafund claims, and file contract payouts.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The event's ID
    """

    index: typing.Optional[EventIndex] = pydantic.Field(default=None)
    """
    Information about the block that triggered the creation of this event
    """

    confirmations: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of blocks on top of the block that triggered the creation of this event
    """

    type: typing.Optional[EventType] = pydantic.Field(default=None)
    """
    The type of the event
    """

    data: typing.Optional[typing.Dict[str, typing.Any]] = None
    maturity_height: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maturityHeight"),
        pydantic.Field(alias="maturityHeight", description="The block height at which the payout matures."),
    ] = None
    """
    The block height at which the payout matures.
    """

    timestamp: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time the event was created
    """

    relevant: typing.Optional[typing.List[Address]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
