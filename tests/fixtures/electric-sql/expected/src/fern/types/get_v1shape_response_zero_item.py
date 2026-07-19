

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_v1shape_response_zero_item_headers import GetV1ShapeResponseZeroItemHeaders


class GetV1ShapeResponseZeroItem(UniversalBaseModel):
    """
    Message object
    """

    headers: GetV1ShapeResponseZeroItemHeaders = pydantic.Field()
    """
    Metadata about the message.
    
    Messages can be `control` messages, providing information or
    instructions to the client. Or they can be operations that
    performed a certain `operation` on a row of data in the shape.
    
    Control messages include:
    - `up-to-date`: Indicates the client has received all available data
    - `must-refetch`: Indicates the client must discard local data and re-sync
    - `snapshot-end`: Marks the end of a subset snapshot, includes PostgreSQL
      snapshot metadata (xmin, xmax, xip_list) for tracking which changes to skip
    """

    key: typing.Optional[str] = pydantic.Field(default=None)
    """
    Row ID
    """

    value: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The row data.
    
    Note that this does not necessarily contain the whole row:
    
    - for inserts it will contain the whole row
    - for updates it will contain the primary key and the changed values
    - for deletes it will contain just the primary key
    
    The values are strings that are formatted according to Postgres' display settings.
    Some Postgres types support several display settings, we format values consistently according to the following display settings:
    
    - `bytea_output = 'hex'`
    - `DateStyle = 'ISO, DMY'`
    - `TimeZone = 'UTC'`
    - `IntervalStyle = 'iso_8601'`
    - `extra_float_digits = 1`
    """

    old_value: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The previous value for changed columns on an update.
    
    Only present on update messages when `replica=full`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
