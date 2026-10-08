

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ConnectV1ConnectorsItemConfig(UniversalBaseModel):
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

    cloud_environment: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="cloud.environment"),
        pydantic.Field(alias="cloud.environment", description="The cloud environment type."),
    ]
    """
    The cloud environment type.
    """

    cloud_provider: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="cloud.provider"),
        pydantic.Field(alias="cloud.provider", description="The cloud service provider, e.g. aws, azure, etc."),
    ]
    """
    The cloud service provider, e.g. aws, azure, etc.
    """

    connector_class: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="connector.class"),
        pydantic.Field(
            alias="connector.class", description="The connector class name. E.g. BigQuerySink, GcsSink, etc."
        ),
    ]
    """
    The connector class name. E.g. BigQuerySink, GcsSink, etc.
    """

    name: str = pydantic.Field()
    """
    Name or alias of the class (plugin) for this connector.
    """

    kafka_endpoint: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="kafka.endpoint"),
        pydantic.Field(alias="kafka.endpoint", description="The kafka cluster endpoint."),
    ]
    """
    The kafka cluster endpoint.
    """

    kafka_region: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="kafka.region"),
        pydantic.Field(alias="kafka.region", description="The kafka cluster region."),
    ]
    """
    The kafka cluster region.
    """

    kafka_api_key: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="kafka.api.key"),
        pydantic.Field(alias="kafka.api.key", description="The kafka cluster api key."),
    ]
    """
    The kafka cluster api key.
    """

    kafka_api_secret: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="kafka.api.secret"),
        pydantic.Field(alias="kafka.api.secret", description="The kafka cluster api secret key."),
    ]
    """
    The kafka cluster api secret key.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
