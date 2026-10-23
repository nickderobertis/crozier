

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostWatchersResponseWatcherLastDelivery(UniversalBaseModel):
    """
    The most recent delivery of any status, or null before the first.
    """

    sent_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="sentAt"), pydantic.Field(alias="sentAt")
    ] = None
    amount: typing.Optional[str] = None
    tx_hash: typing_extensions.Annotated[str, FieldMetadata(alias="txHash"), pydantic.Field(alias="txHash")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
