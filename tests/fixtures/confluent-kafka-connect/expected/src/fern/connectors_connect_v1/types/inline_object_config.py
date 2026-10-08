

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class InlineObjectConfig(UniversalBaseModel):
    """
    Configuration parameters for the connector. All values should be strings.
    """

    connector_class: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="connector.class"),
        pydantic.Field(
            alias="connector.class",
            description="\\[Required for Managed Connector, Ignored for Custom Connector\\] The connector class name, e.g., BigQuerySink, GcsSink, etc.",
        ),
    ]
    """
    \\[Required for Managed Connector, Ignored for Custom Connector\\] The connector class name, e.g., BigQuerySink, GcsSink, etc.
    """

    name: str = pydantic.Field()
    """
    Name or alias of the class (plugin) for this connector. For custom connector, it must be the same as the name of the connector to create.
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

    confluent_connector_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="confluent.connector.type"),
        pydantic.Field(
            alias="confluent.connector.type", description="\\[Required for Custom Connector\\] The connector type."
        ),
    ] = None
    """
    \\[Required for Custom Connector\\] The connector type.
    """

    confluent_custom_plugin_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="confluent.custom.plugin.id"),
        pydantic.Field(
            alias="confluent.custom.plugin.id",
            description="\\[Required for Custom Connector\\] The custom plugin id of custom connector, e.g., `ccp-lq5m06`",
        ),
    ] = None
    """
    \\[Required for Custom Connector\\] The custom plugin id of custom connector, e.g., `ccp-lq5m06`
    """

    confluent_custom_connection_endpoints: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="confluent.custom.connection.endpoints"),
        pydantic.Field(
            alias="confluent.custom.connection.endpoints",
            description="\\[Optional for Custom Connector\\] Egress endpoint(s) for the connector to use when attaching to the sink or source data system.",
        ),
    ] = None
    """
    \\[Optional for Custom Connector\\] Egress endpoint(s) for the connector to use when attaching to the sink or source data system.
    """

    confluent_custom_schema_registry_auto: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="confluent.custom.schema.registry.auto"),
        pydantic.Field(
            alias="confluent.custom.schema.registry.auto",
            description="\\[Optional for Custom Connector\\] Automatically add the required schema registry properties in a custom connector config if schema registry is enabled.",
        ),
    ] = None
    """
    \\[Optional for Custom Connector\\] Automatically add the required schema registry properties in a custom connector config if schema registry is enabled.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
