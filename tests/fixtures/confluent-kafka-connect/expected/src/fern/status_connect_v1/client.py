

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.connect_v1connectors import ConnectV1Connectors
from ..types.inline_response2001 import InlineResponse2001
from .raw_client import AsyncRawStatusConnectV1Client, RawStatusConnectV1Client


class StatusConnectV1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStatusConnectV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStatusConnectV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStatusConnectV1Client
        """
        return self._raw_client

    def read_connectv1connector_status(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InlineResponse2001:
        """
        Get current status of the connector. This includes whether it is running, failed, or paused. Also includes which worker it is assigned to, error information if it has failed, and the state of all its tasks.

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
        InlineResponse2001
            Connector.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.status_connect_v1.read_connectv1connector_status(
            environment_id="environment_id",
            kafka_cluster_id="kafka_cluster_id",
            connector_name="connector_name",
        )
        """
        _response = self._raw_client.read_connectv1connector_status(
            environment_id, kafka_cluster_id, connector_name, request_options=request_options
        )
        return _response.data

    def list_connectv1connector_tasks(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectV1Connectors:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Get a list of tasks currently running for the connector.

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
        ConnectV1Connectors
            Connector Task.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.status_connect_v1.list_connectv1connector_tasks(
            environment_id="environment_id",
            kafka_cluster_id="kafka_cluster_id",
            connector_name="connector_name",
        )
        """
        _response = self._raw_client.list_connectv1connector_tasks(
            environment_id, kafka_cluster_id, connector_name, request_options=request_options
        )
        return _response.data


class AsyncStatusConnectV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStatusConnectV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStatusConnectV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStatusConnectV1Client
        """
        return self._raw_client

    async def read_connectv1connector_status(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InlineResponse2001:
        """
        Get current status of the connector. This includes whether it is running, failed, or paused. Also includes which worker it is assigned to, error information if it has failed, and the state of all its tasks.

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
        InlineResponse2001
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
            await client.status_connect_v1.read_connectv1connector_status(
                environment_id="environment_id",
                kafka_cluster_id="kafka_cluster_id",
                connector_name="connector_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_connectv1connector_status(
            environment_id, kafka_cluster_id, connector_name, request_options=request_options
        )
        return _response.data

    async def list_connectv1connector_tasks(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectV1Connectors:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Get a list of tasks currently running for the connector.

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
        ConnectV1Connectors
            Connector Task.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.status_connect_v1.list_connectv1connector_tasks(
                environment_id="environment_id",
                kafka_cluster_id="kafka_cluster_id",
                connector_name="connector_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_connectv1connector_tasks(
            environment_id, kafka_cluster_id, connector_name, request_options=request_options
        )
        return _response.data
