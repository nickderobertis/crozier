

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.connect_v1connector import ConnectV1Connector
from ..types.connect_v1connector_expansion_map import ConnectV1ConnectorExpansionMap
from ..types.connect_v1connector_with_offsets import ConnectV1ConnectorWithOffsets
from ..types.inline_response200 import InlineResponse200
from .raw_client import AsyncRawConnectorsConnectV1Client, RawConnectorsConnectV1Client
from .types.get_connectv1connector_config_response import GetConnectv1ConnectorConfigResponse
from .types.inline_object_config import InlineObjectConfig
from .types.inline_object_offsets_item import InlineObjectOffsetsItem
from .types.list_connectv1connectors_with_expansions_request_expand import (
    ListConnectv1ConnectorsWithExpansionsRequestExpand,
)


OMIT = typing.cast(typing.Any, ...)


class ConnectorsConnectV1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConnectorsConnectV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConnectorsConnectV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConnectorsConnectV1Client
        """
        return self._raw_client

    def list_connectv1connectors(
        self, environment_id: str, kafka_cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Retrieve a list of "names" of the active connectors. You can then make a [read request](#operation/readConnectv1Connector) for a specific connector by name.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Connector.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.connectors_connect_v1.list_connectv1connectors(
            environment_id="environment_id",
            kafka_cluster_id="kafka_cluster_id",
        )
        """
        _response = self._raw_client.list_connectv1connectors(
            environment_id, kafka_cluster_id, request_options=request_options
        )
        return _response.data

    def create_connectv1connector(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        config: typing.Optional[InlineObjectConfig] = OMIT,
        offsets: typing.Optional[typing.Sequence[InlineObjectOffsetsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectV1ConnectorWithOffsets:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Create a new connector. Returns the new connector information if successful.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        name : typing.Optional[str]
            Name of the connector to create.

        config : typing.Optional[InlineObjectConfig]
            Configuration parameters for the connector. All values should be strings.

        offsets : typing.Optional[typing.Sequence[InlineObjectOffsetsItem]]
            Array of offsets which are categorised into partitions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectV1ConnectorWithOffsets
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.connectors_connect_v1.create_connectv1connector(
            environment_id="environment_id",
            kafka_cluster_id="kafka_cluster_id",
        )
        """
        _response = self._raw_client.create_connectv1connector(
            environment_id, kafka_cluster_id, name=name, config=config, offsets=offsets, request_options=request_options
        )
        return _response.data

    def list_connectv1connectors_with_expansions(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        *,
        expand: typing.Optional[ListConnectv1ConnectorsWithExpansionsRequestExpand] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectV1ConnectorExpansionMap:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Retrieve an object with the queried expansions of all connectors. Without `expand` query parameter, this list connector’s endpoint will return a [list of only the connector names](#operation/listConnectv1Connectors).

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        expand : typing.Optional[ListConnectv1ConnectorsWithExpansionsRequestExpand]
            - id : Returns metadata of each connector such as id and id type.
            - info : Returns metadata of each connector such as the configuration, task
            information, and type of connector.
            - status : Returns additional state information of each connector including their status and tasks.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectV1ConnectorExpansionMap
            Connector.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.connectors_connect_v1.list_connectv1connectors_with_expansions(
            environment_id="environment_id",
            kafka_cluster_id="kafka_cluster_id",
        )
        """
        _response = self._raw_client.list_connectv1connectors_with_expansions(
            environment_id, kafka_cluster_id, expand=expand, request_options=request_options
        )
        return _response.data

    def get_connectv1connector_config(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetConnectv1ConnectorConfigResponse:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Get the configuration for the connector.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        connector_name : str
            The unique name of the connector.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConnectv1ConnectorConfigResponse
            Connector.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.connectors_connect_v1.get_connectv1connector_config(
            environment_id="environment_id",
            kafka_cluster_id="kafka_cluster_id",
            connector_name="connector_name",
        )
        """
        _response = self._raw_client.get_connectv1connector_config(
            environment_id, kafka_cluster_id, connector_name, request_options=request_options
        )
        return _response.data

    def create_or_update_connectv1connector_config(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        connector_class: str,
        name: str,
        kafka_api_key: str,
        kafka_api_secret: str,
        confluent_connector_type: typing.Optional[str] = OMIT,
        confluent_custom_plugin_id: typing.Optional[str] = OMIT,
        confluent_custom_connection_endpoints: typing.Optional[str] = OMIT,
        confluent_custom_schema_registry_auto: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectV1Connector:
        """
        Create a new connector using the given configuration, or update the configuration for an existing connector. Returns information about the connector after the change has been made.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        connector_name : str
            The unique name of the connector.

        connector_class : str
            \\[Required for Managed Connector, Ignored for Custom Connector\\] The connector class name. E.g. BigQuerySink, GcsSink, etc.

        name : str
            Name or alias of the class (plugin) for this connector.

        kafka_api_key : str
            The kafka cluster api key.

        kafka_api_secret : str
            The kafka cluster api secret key.

        confluent_connector_type : typing.Optional[str]
            \\[Required for Custom Connector\\] The connector type.

        confluent_custom_plugin_id : typing.Optional[str]
            \\[Required for Custom Connector\\] The custom plugin id of custom connector, e.g., `ccp-lq5m06`

        confluent_custom_connection_endpoints : typing.Optional[str]
            \\[Optional for Custom Connector\\] Egress endpoint(s) for the connector to use when attaching to the sink or source data system.

        confluent_custom_schema_registry_auto : typing.Optional[str]
            \\[Optional for Custom Connector\\] Automatically add the required schema registry properties in a custom connector config if schema registry is enabled.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectV1Connector
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.connectors_connect_v1.create_or_update_connectv1connector_config(
            environment_id="environment_id",
            kafka_cluster_id="kafka_cluster_id",
            connector_name="connector_name",
            connector_class="GcsSink",
            name="MyGcsLogsBucketConnector",
            kafka_api_key="****************",
            kafka_api_secret="****************",
        )
        """
        _response = self._raw_client.create_or_update_connectv1connector_config(
            environment_id,
            kafka_cluster_id,
            connector_name,
            connector_class=connector_class,
            name=name,
            kafka_api_key=kafka_api_key,
            kafka_api_secret=kafka_api_secret,
            confluent_connector_type=confluent_connector_type,
            confluent_custom_plugin_id=confluent_custom_plugin_id,
            confluent_custom_connection_endpoints=confluent_custom_connection_endpoints,
            confluent_custom_schema_registry_auto=confluent_custom_schema_registry_auto,
            request_options=request_options,
        )
        return _response.data

    def read_connectv1connector(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectV1Connector:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Get information about the connector.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        connector_name : str
            The unique name of the connector.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectV1Connector
            Connector.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.connectors_connect_v1.read_connectv1connector(
            environment_id="environment_id",
            kafka_cluster_id="kafka_cluster_id",
            connector_name="connector_name",
        )
        """
        _response = self._raw_client.read_connectv1connector(
            environment_id, kafka_cluster_id, connector_name, request_options=request_options
        )
        return _response.data

    def delete_connectv1connector(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InlineResponse200:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Delete a connector. Halts all tasks and deletes the connector configuration.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        connector_name : str
            The unique name of the connector.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InlineResponse200
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.connectors_connect_v1.delete_connectv1connector(
            environment_id="environment_id",
            kafka_cluster_id="kafka_cluster_id",
            connector_name="connector_name",
        )
        """
        _response = self._raw_client.delete_connectv1connector(
            environment_id, kafka_cluster_id, connector_name, request_options=request_options
        )
        return _response.data


class AsyncConnectorsConnectV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConnectorsConnectV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConnectorsConnectV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConnectorsConnectV1Client
        """
        return self._raw_client

    async def list_connectv1connectors(
        self, environment_id: str, kafka_cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Retrieve a list of "names" of the active connectors. You can then make a [read request](#operation/readConnectv1Connector) for a specific connector by name.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Connector.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.connectors_connect_v1.list_connectv1connectors(
                environment_id="environment_id",
                kafka_cluster_id="kafka_cluster_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_connectv1connectors(
            environment_id, kafka_cluster_id, request_options=request_options
        )
        return _response.data

    async def create_connectv1connector(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        config: typing.Optional[InlineObjectConfig] = OMIT,
        offsets: typing.Optional[typing.Sequence[InlineObjectOffsetsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectV1ConnectorWithOffsets:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Create a new connector. Returns the new connector information if successful.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        name : typing.Optional[str]
            Name of the connector to create.

        config : typing.Optional[InlineObjectConfig]
            Configuration parameters for the connector. All values should be strings.

        offsets : typing.Optional[typing.Sequence[InlineObjectOffsetsItem]]
            Array of offsets which are categorised into partitions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectV1ConnectorWithOffsets
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.connectors_connect_v1.create_connectv1connector(
                environment_id="environment_id",
                kafka_cluster_id="kafka_cluster_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_connectv1connector(
            environment_id, kafka_cluster_id, name=name, config=config, offsets=offsets, request_options=request_options
        )
        return _response.data

    async def list_connectv1connectors_with_expansions(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        *,
        expand: typing.Optional[ListConnectv1ConnectorsWithExpansionsRequestExpand] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectV1ConnectorExpansionMap:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Retrieve an object with the queried expansions of all connectors. Without `expand` query parameter, this list connector’s endpoint will return a [list of only the connector names](#operation/listConnectv1Connectors).

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        expand : typing.Optional[ListConnectv1ConnectorsWithExpansionsRequestExpand]
            - id : Returns metadata of each connector such as id and id type.
            - info : Returns metadata of each connector such as the configuration, task
            information, and type of connector.
            - status : Returns additional state information of each connector including their status and tasks.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectV1ConnectorExpansionMap
            Connector.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.connectors_connect_v1.list_connectv1connectors_with_expansions(
                environment_id="environment_id",
                kafka_cluster_id="kafka_cluster_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_connectv1connectors_with_expansions(
            environment_id, kafka_cluster_id, expand=expand, request_options=request_options
        )
        return _response.data

    async def get_connectv1connector_config(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetConnectv1ConnectorConfigResponse:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Get the configuration for the connector.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        connector_name : str
            The unique name of the connector.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConnectv1ConnectorConfigResponse
            Connector.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.connectors_connect_v1.get_connectv1connector_config(
                environment_id="environment_id",
                kafka_cluster_id="kafka_cluster_id",
                connector_name="connector_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_connectv1connector_config(
            environment_id, kafka_cluster_id, connector_name, request_options=request_options
        )
        return _response.data

    async def create_or_update_connectv1connector_config(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        connector_class: str,
        name: str,
        kafka_api_key: str,
        kafka_api_secret: str,
        confluent_connector_type: typing.Optional[str] = OMIT,
        confluent_custom_plugin_id: typing.Optional[str] = OMIT,
        confluent_custom_connection_endpoints: typing.Optional[str] = OMIT,
        confluent_custom_schema_registry_auto: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectV1Connector:
        """
        Create a new connector using the given configuration, or update the configuration for an existing connector. Returns information about the connector after the change has been made.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        connector_name : str
            The unique name of the connector.

        connector_class : str
            \\[Required for Managed Connector, Ignored for Custom Connector\\] The connector class name. E.g. BigQuerySink, GcsSink, etc.

        name : str
            Name or alias of the class (plugin) for this connector.

        kafka_api_key : str
            The kafka cluster api key.

        kafka_api_secret : str
            The kafka cluster api secret key.

        confluent_connector_type : typing.Optional[str]
            \\[Required for Custom Connector\\] The connector type.

        confluent_custom_plugin_id : typing.Optional[str]
            \\[Required for Custom Connector\\] The custom plugin id of custom connector, e.g., `ccp-lq5m06`

        confluent_custom_connection_endpoints : typing.Optional[str]
            \\[Optional for Custom Connector\\] Egress endpoint(s) for the connector to use when attaching to the sink or source data system.

        confluent_custom_schema_registry_auto : typing.Optional[str]
            \\[Optional for Custom Connector\\] Automatically add the required schema registry properties in a custom connector config if schema registry is enabled.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectV1Connector
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.connectors_connect_v1.create_or_update_connectv1connector_config(
                environment_id="environment_id",
                kafka_cluster_id="kafka_cluster_id",
                connector_name="connector_name",
                connector_class="GcsSink",
                name="MyGcsLogsBucketConnector",
                kafka_api_key="****************",
                kafka_api_secret="****************",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_or_update_connectv1connector_config(
            environment_id,
            kafka_cluster_id,
            connector_name,
            connector_class=connector_class,
            name=name,
            kafka_api_key=kafka_api_key,
            kafka_api_secret=kafka_api_secret,
            confluent_connector_type=confluent_connector_type,
            confluent_custom_plugin_id=confluent_custom_plugin_id,
            confluent_custom_connection_endpoints=confluent_custom_connection_endpoints,
            confluent_custom_schema_registry_auto=confluent_custom_schema_registry_auto,
            request_options=request_options,
        )
        return _response.data

    async def read_connectv1connector(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectV1Connector:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Get information about the connector.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        connector_name : str
            The unique name of the connector.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectV1Connector
            Connector.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.connectors_connect_v1.read_connectv1connector(
                environment_id="environment_id",
                kafka_cluster_id="kafka_cluster_id",
                connector_name="connector_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_connectv1connector(
            environment_id, kafka_cluster_id, connector_name, request_options=request_options
        )
        return _response.data

    async def delete_connectv1connector(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InlineResponse200:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Delete a connector. Halts all tasks and deletes the connector configuration.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        connector_name : str
            The unique name of the connector.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InlineResponse200
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.connectors_connect_v1.delete_connectv1connector(
                environment_id="environment_id",
                kafka_cluster_id="kafka_cluster_id",
                connector_name="connector_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_connectv1connector(
            environment_id, kafka_cluster_id, connector_name, request_options=request_options
        )
        return _response.data
