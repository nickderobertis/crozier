

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.inline_response2002 import InlineResponse2002
from ..types.inline_response2003 import InlineResponse2003
from .raw_client import AsyncRawManagedConnectorPluginsConnectV1Client, RawManagedConnectorPluginsConnectV1Client


OMIT = typing.cast(typing.Any, ...)


class ManagedConnectorPluginsConnectV1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawManagedConnectorPluginsConnectV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawManagedConnectorPluginsConnectV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawManagedConnectorPluginsConnectV1Client
        """
        return self._raw_client

    def list_connectv1connector_plugins(
        self, environment_id: str, kafka_cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[InlineResponse2002]:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Return a list of Managed Connector plugins installed in the Kafka Connect cluster.

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
        typing.List[InlineResponse2002]
            Connector Plugin.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.managed_connector_plugins_connect_v1.list_connectv1connector_plugins(
            environment_id="environment_id",
            kafka_cluster_id="kafka_cluster_id",
        )
        """
        _response = self._raw_client.list_connectv1connector_plugins(
            environment_id, kafka_cluster_id, request_options=request_options
        )
        return _response.data

    def validate_connectv1connector_plugin(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        plugin_name: str,
        *,
        request: typing.Dict[str, str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InlineResponse2003:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Validate the provided configuration values against the configuration definition. This API performs per config validation and returns suggested values and validation error messages.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        plugin_name : str
            The unique name of the connector plugin.

        request : typing.Dict[str, str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InlineResponse2003
            Connector Plugin.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.managed_connector_plugins_connect_v1.validate_connectv1connector_plugin(
            environment_id="environment_id",
            kafka_cluster_id="kafka_cluster_id",
            plugin_name="plugin_name",
            request={
                "cloud.environment": "prod",
                "cloud.provider": "aws",
                "connector.class": "GcsSink",
                "data.format": "BYTES",
                "flush.size": "500",
                "gcs.bucket.name": "APILogsBucket",
                "gcs.credentials.config": "****************",
                "kafka.api.key": "****************",
                "kafka.api.secret": "****************",
                "kafka.endpoint": "SASL_SSL://pkc-xxxxx.us-west-2.aws.confluent.cloud:9092",
                "kafka.region": "us-west-2",
                "name": "MyGcsLogsBucketConnector",
                "tasks.max": "2",
                "time.interval": "DAILY",
                "topics": "APILogsTopic",
            },
        )
        """
        _response = self._raw_client.validate_connectv1connector_plugin(
            environment_id, kafka_cluster_id, plugin_name, request=request, request_options=request_options
        )
        return _response.data


class AsyncManagedConnectorPluginsConnectV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawManagedConnectorPluginsConnectV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawManagedConnectorPluginsConnectV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawManagedConnectorPluginsConnectV1Client
        """
        return self._raw_client

    async def list_connectv1connector_plugins(
        self, environment_id: str, kafka_cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[InlineResponse2002]:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Return a list of Managed Connector plugins installed in the Kafka Connect cluster.

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
        typing.List[InlineResponse2002]
            Connector Plugin.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.managed_connector_plugins_connect_v1.list_connectv1connector_plugins(
                environment_id="environment_id",
                kafka_cluster_id="kafka_cluster_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_connectv1connector_plugins(
            environment_id, kafka_cluster_id, request_options=request_options
        )
        return _response.data

    async def validate_connectv1connector_plugin(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        plugin_name: str,
        *,
        request: typing.Dict[str, str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InlineResponse2003:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Validate the provided configuration values against the configuration definition. This API performs per config validation and returns suggested values and validation error messages.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        plugin_name : str
            The unique name of the connector plugin.

        request : typing.Dict[str, str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InlineResponse2003
            Connector Plugin.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.managed_connector_plugins_connect_v1.validate_connectv1connector_plugin(
                environment_id="environment_id",
                kafka_cluster_id="kafka_cluster_id",
                plugin_name="plugin_name",
                request={
                    "cloud.environment": "prod",
                    "cloud.provider": "aws",
                    "connector.class": "GcsSink",
                    "data.format": "BYTES",
                    "flush.size": "500",
                    "gcs.bucket.name": "APILogsBucket",
                    "gcs.credentials.config": "****************",
                    "kafka.api.key": "****************",
                    "kafka.api.secret": "****************",
                    "kafka.endpoint": "SASL_SSL://pkc-xxxxx.us-west-2.aws.confluent.cloud:9092",
                    "kafka.region": "us-west-2",
                    "name": "MyGcsLogsBucketConnector",
                    "tasks.max": "2",
                    "time.interval": "DAILY",
                    "topics": "APILogsTopic",
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.validate_connectv1connector_plugin(
            environment_id, kafka_cluster_id, plugin_name, request=request, request_options=request_options
        )
        return _response.data
