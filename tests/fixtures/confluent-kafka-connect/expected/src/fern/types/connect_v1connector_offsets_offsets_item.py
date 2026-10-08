

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConnectV1ConnectorOffsetsOffsetsItem(UniversalBaseModel):
    partition: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The partition information. For sink connectors this is the kafka topic and 
    partition. For source connectors this is depends on the partitions defined by the 
    source connector. For example, the table which this task is pulling data from in a
    JDBC based MySQL source connector.
    """

    offset: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The offset of the partition. For sink connectors this is the kafka offset. For 
    source connectors this is depends on the offset defined by the source connector. 
    For example, the timestamp and incrementing column info in a table, for a JDBC based 
    MySQL source connector.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
