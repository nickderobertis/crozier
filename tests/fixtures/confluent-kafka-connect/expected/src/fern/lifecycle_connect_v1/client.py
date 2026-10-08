

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawLifecycleConnectV1Client, RawLifecycleConnectV1Client


class LifecycleConnectV1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLifecycleConnectV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLifecycleConnectV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLifecycleConnectV1Client
        """
        return self._raw_client

    def pause_connectv1connector(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Pause the connector and its tasks. Stops message processing until the connector is resumed. This call is asynchronous and the tasks will not transition to PAUSED state at the same time.

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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.lifecycle_connect_v1.pause_connectv1connector(
            environment_id="environment_id",
            kafka_cluster_id="kafka_cluster_id",
            connector_name="connector_name",
        )
        """
        _response = self._raw_client.pause_connectv1connector(
            environment_id, kafka_cluster_id, connector_name, request_options=request_options
        )
        return _response.data

    def resume_connectv1connector(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Resume a paused connector or do nothing if the connector is not paused. This call is asynchronous and the tasks will not transition to RUNNING state at the same time.

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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.lifecycle_connect_v1.resume_connectv1connector(
            environment_id="environment_id",
            kafka_cluster_id="kafka_cluster_id",
            connector_name="connector_name",
        )
        """
        _response = self._raw_client.resume_connectv1connector(
            environment_id, kafka_cluster_id, connector_name, request_options=request_options
        )
        return _response.data


class AsyncLifecycleConnectV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLifecycleConnectV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLifecycleConnectV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLifecycleConnectV1Client
        """
        return self._raw_client

    async def pause_connectv1connector(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Pause the connector and its tasks. Stops message processing until the connector is resumed. This call is asynchronous and the tasks will not transition to PAUSED state at the same time.

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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.lifecycle_connect_v1.pause_connectv1connector(
                environment_id="environment_id",
                kafka_cluster_id="kafka_cluster_id",
                connector_name="connector_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pause_connectv1connector(
            environment_id, kafka_cluster_id, connector_name, request_options=request_options
        )
        return _response.data

    async def resume_connectv1connector(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Resume a paused connector or do nothing if the connector is not paused. This call is asynchronous and the tasks will not transition to RUNNING state at the same time.

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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.lifecycle_connect_v1.resume_connectv1connector(
                environment_id="environment_id",
                kafka_cluster_id="kafka_cluster_id",
                connector_name="connector_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resume_connectv1connector(
            environment_id, kafka_cluster_id, connector_name, request_options=request_options
        )
        return _response.data
