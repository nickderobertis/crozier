

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.connect_v1alter_offset_request_info import ConnectV1AlterOffsetRequestInfo
from ..types.connect_v1alter_offset_request_type import ConnectV1AlterOffsetRequestType
from ..types.connect_v1alter_offset_status import ConnectV1AlterOffsetStatus
from ..types.connect_v1connector_offsets import ConnectV1ConnectorOffsets
from .raw_client import AsyncRawOffsetsConnectV1Client, RawOffsetsConnectV1Client
from .types.connect_v1alter_offset_request_offsets_item import ConnectV1AlterOffsetRequestOffsetsItem


OMIT = typing.cast(typing.Any, ...)


class OffsetsConnectV1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOffsetsConnectV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOffsetsConnectV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOffsetsConnectV1Client
        """
        return self._raw_client

    def get_connectv1connector_offsets(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectV1ConnectorOffsets:
        """
        [![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy)

        Get the current offsets for the connector. The offsets provide information on the point in the source system,
        from which the connector is pulling in data. The offsets of a connector are continuously observed periodically and are queryable via this API.

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
        ConnectV1ConnectorOffsets
            Connector Offsets.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.offsets_connect_v1.get_connectv1connector_offsets(
            environment_id="environment_id",
            kafka_cluster_id="kafka_cluster_id",
            connector_name="connector_name",
        )
        """
        _response = self._raw_client.get_connectv1connector_offsets(
            environment_id, kafka_cluster_id, connector_name, request_options=request_options
        )
        return _response.data

    def alter_connectv1connector_offsets_request(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        type: ConnectV1AlterOffsetRequestType,
        offsets: typing.Optional[typing.Sequence[ConnectV1AlterOffsetRequestOffsetsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectV1AlterOffsetRequestInfo:
        """
        [![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy)

        Request to alter the offsets of a connector. This supports the ability to PATCH/DELETE the offsets of a connector.
        Note, you will see momentary downtime as this will internally stop the connector, while the offsets are being altered.
        You can only make one alter offsets request at a time for a connector.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        connector_name : str
            The unique name of the connector.

        type : ConnectV1AlterOffsetRequestType

        offsets : typing.Optional[typing.Sequence[ConnectV1AlterOffsetRequestOffsetsItem]]
            Array of offsets which are categorised into partitions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectV1AlterOffsetRequestInfo
            Accepted

        Examples
        --------
        from fern.offsets_connect_v1 import ConnectV1AlterOffsetRequestOffsetsItem

        from fern import ConnectV1AlterOffsetRequestType, FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.offsets_connect_v1.alter_connectv1connector_offsets_request(
            environment_id="environment_id",
            kafka_cluster_id="kafka_cluster_id",
            connector_name="connector_name",
            type=ConnectV1AlterOffsetRequestType.PATCH,
            offsets=[
                ConnectV1AlterOffsetRequestOffsetsItem(
                    partition={"kafka_partition": 0, "kafka_topic": "topic_A"},
                    offset={"kafka_offset": 1000},
                )
            ],
        )
        """
        _response = self._raw_client.alter_connectv1connector_offsets_request(
            environment_id,
            kafka_cluster_id,
            connector_name,
            type=type,
            offsets=offsets,
            request_options=request_options,
        )
        return _response.data

    def get_connectv1connector_offsets_request_status(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectV1AlterOffsetStatus:
        """
        [![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy)

        Get the status of the previous alter offset request.

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
        ConnectV1AlterOffsetStatus
            Connector Offsets Request Status.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.offsets_connect_v1.get_connectv1connector_offsets_request_status(
            environment_id="environment_id",
            kafka_cluster_id="kafka_cluster_id",
            connector_name="connector_name",
        )
        """
        _response = self._raw_client.get_connectv1connector_offsets_request_status(
            environment_id, kafka_cluster_id, connector_name, request_options=request_options
        )
        return _response.data


class AsyncOffsetsConnectV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOffsetsConnectV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOffsetsConnectV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOffsetsConnectV1Client
        """
        return self._raw_client

    async def get_connectv1connector_offsets(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectV1ConnectorOffsets:
        """
        [![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy)

        Get the current offsets for the connector. The offsets provide information on the point in the source system,
        from which the connector is pulling in data. The offsets of a connector are continuously observed periodically and are queryable via this API.

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
        ConnectV1ConnectorOffsets
            Connector Offsets.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.offsets_connect_v1.get_connectv1connector_offsets(
                environment_id="environment_id",
                kafka_cluster_id="kafka_cluster_id",
                connector_name="connector_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_connectv1connector_offsets(
            environment_id, kafka_cluster_id, connector_name, request_options=request_options
        )
        return _response.data

    async def alter_connectv1connector_offsets_request(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        type: ConnectV1AlterOffsetRequestType,
        offsets: typing.Optional[typing.Sequence[ConnectV1AlterOffsetRequestOffsetsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectV1AlterOffsetRequestInfo:
        """
        [![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy)

        Request to alter the offsets of a connector. This supports the ability to PATCH/DELETE the offsets of a connector.
        Note, you will see momentary downtime as this will internally stop the connector, while the offsets are being altered.
        You can only make one alter offsets request at a time for a connector.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        connector_name : str
            The unique name of the connector.

        type : ConnectV1AlterOffsetRequestType

        offsets : typing.Optional[typing.Sequence[ConnectV1AlterOffsetRequestOffsetsItem]]
            Array of offsets which are categorised into partitions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectV1AlterOffsetRequestInfo
            Accepted

        Examples
        --------
        import asyncio

        from fern.offsets_connect_v1 import ConnectV1AlterOffsetRequestOffsetsItem

        from fern import AsyncFernApi, ConnectV1AlterOffsetRequestType

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.offsets_connect_v1.alter_connectv1connector_offsets_request(
                environment_id="environment_id",
                kafka_cluster_id="kafka_cluster_id",
                connector_name="connector_name",
                type=ConnectV1AlterOffsetRequestType.PATCH,
                offsets=[
                    ConnectV1AlterOffsetRequestOffsetsItem(
                        partition={"kafka_partition": 0, "kafka_topic": "topic_A"},
                        offset={"kafka_offset": 1000},
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.alter_connectv1connector_offsets_request(
            environment_id,
            kafka_cluster_id,
            connector_name,
            type=type,
            offsets=offsets,
            request_options=request_options,
        )
        return _response.data

    async def get_connectv1connector_offsets_request_status(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectV1AlterOffsetStatus:
        """
        [![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy)

        Get the status of the previous alter offset request.

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
        ConnectV1AlterOffsetStatus
            Connector Offsets Request Status.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.offsets_connect_v1.get_connectv1connector_offsets_request_status(
                environment_id="environment_id",
                kafka_cluster_id="kafka_cluster_id",
                connector_name="connector_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_connectv1connector_offsets_request_status(
            environment_id, kafka_cluster_id, connector_name, request_options=request_options
        )
        return _response.data
