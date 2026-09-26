

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_events_kafka_config_key_pass import OtoroshiEventsKafkaConfigKeyPass
from .otoroshi_events_kafka_config_keystore import OtoroshiEventsKafkaConfigKeystore
from .otoroshi_events_kafka_config_sasl_config import OtoroshiEventsKafkaConfigSaslConfig
from .otoroshi_events_kafka_config_truststore import OtoroshiEventsKafkaConfigTruststore
from .otoroshi_events_kafka_config_type import OtoroshiEventsKafkaConfigType


class OtoroshiEventsKafkaConfig(UniversalBaseModel):
    """
    ???
    """

    type: typing.Optional[OtoroshiEventsKafkaConfigType] = pydantic.Field(default=None)
    """
    the kind of exporter
    """

    send_events: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="sendEvents"),
        pydantic.Field(alias="sendEvents", description="Send events to it, or just connect"),
    ] = None
    """
    Send events to it, or just connect
    """

    truststore: typing.Optional[OtoroshiEventsKafkaConfigTruststore] = pydantic.Field(default=None)
    """
    Optional truststore
    """

    host_validation: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hostValidation"),
        pydantic.Field(alias="hostValidation", description="Enabled TLS hostname validation"),
    ] = None
    """
    Enabled TLS hostname validation
    """

    servers: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    URLs of the kafka servers
    """

    mtls_config: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="mtlsConfig"), pydantic.Field(alias="mtlsConfig")
    ] = None
    security_protocol: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="securityProtocol"),
        pydantic.Field(alias="securityProtocol", description="Used security protocol"),
    ] = None
    """
    Used security protocol
    """

    keystore: typing.Optional[OtoroshiEventsKafkaConfigKeystore] = pydantic.Field(default=None)
    """
    Optional keystore
    """

    topic: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional kafka topic (otoroshi-events by default)
    """

    key_pass: typing_extensions.Annotated[
        typing.Optional[OtoroshiEventsKafkaConfigKeyPass],
        FieldMetadata(alias="keyPass"),
        pydantic.Field(alias="keyPass", description="Optional keypass"),
    ] = None
    """
    Optional keypass
    """

    sasl_config: typing_extensions.Annotated[
        typing.Optional[OtoroshiEventsKafkaConfigSaslConfig],
        FieldMetadata(alias="saslConfig"),
        pydantic.Field(alias="saslConfig", description="SASL configuration"),
    ] = None
    """
    SASL configuration
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
