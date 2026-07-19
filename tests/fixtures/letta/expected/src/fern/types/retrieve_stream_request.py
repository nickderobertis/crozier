

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RetrieveStreamRequest(UniversalBaseModel):
    starting_after: typing.Optional[int] = pydantic.Field(default=None)
    """
    Sequence id to use as a cursor for pagination. Response will start streaming after this chunk sequence id
    """

    include_pings: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to include periodic keepalive ping messages in the stream to prevent connection timeouts.
    """

    poll_interval: typing.Optional[float] = pydantic.Field(default=None)
    """
    Seconds to wait between polls when no new data.
    """

    batch_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of entries to read per batch.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
