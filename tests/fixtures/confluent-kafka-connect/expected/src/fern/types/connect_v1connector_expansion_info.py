

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connect_v1connector_expansion_info_config import ConnectV1ConnectorExpansionInfoConfig


class ConnectV1ConnectorExpansionInfo(UniversalBaseModel):
    """
    Metadata of the connector.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the connector.
    """

    config: typing.Optional[ConnectV1ConnectorExpansionInfoConfig] = pydantic.Field(default=None)
    """
    Configuration parameters for the connector. These configurations
    are the minimum set of key-value pairs (KVP) which are used to
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
    
    For example, a connector like `GcsSink` would have additional
    parameters such as `gcs.bucket.name`, `flush.size`, etc.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
