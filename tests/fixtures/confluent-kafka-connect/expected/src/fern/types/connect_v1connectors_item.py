

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connect_v1connectors_item_config import ConnectV1ConnectorsItemConfig
from .connect_v1connectors_item_id import ConnectV1ConnectorsItemId


class ConnectV1ConnectorsItem(UniversalBaseModel):
    id: typing.Optional[ConnectV1ConnectorsItemId] = pydantic.Field(default=None)
    """
    The ID of task.
    """

    config: typing.Optional[ConnectV1ConnectorsItemConfig] = pydantic.Field(default=None)
    """
    Configuration parameters for the connector. These configurations
    are the minimum set of key-value pairs (KVP) which can be used to
    define how the connector connects Kafka to the external system.
    Some of these KVPs are common to all the connectors, such as
    connection parameters to Kafka, connector metadata, etc. The list
    of common connector configurations is as follows
    
      - cloud.environment
      - cloud.provider
      - connector.class
      - kafka.api.key
      - kafka.api.secret
      - kafka.endpoint
      - kafka.region
      - name
    
    A specific connector such as `GcsSink` would have additional
    parameters such as `gcs.bucket.name`, `flush.size`, etc.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
