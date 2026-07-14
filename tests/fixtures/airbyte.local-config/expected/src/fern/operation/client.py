

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.check_operation_read import CheckOperationRead
from ..types.connection_id import ConnectionId
from ..types.operation_id import OperationId
from ..types.operation_read import OperationRead
from ..types.operation_read_list import OperationReadList
from ..types.operator_configuration import OperatorConfiguration
from ..types.operator_dbt import OperatorDbt
from ..types.operator_normalization import OperatorNormalization
from ..types.operator_type import OperatorType
from ..types.operator_webhook import OperatorWebhook
from ..types.workspace_id import WorkspaceId
from .raw_client import AsyncRawOperationClient, RawOperationClient


OMIT = typing.cast(typing.Any, ...)


class OperationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOperationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOperationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOperationClient
        """
        return self._raw_client

    def check_operation(
        self,
        *,
        operator_type: OperatorType,
        dbt: typing.Optional[OperatorDbt] = OMIT,
        normalization: typing.Optional[OperatorNormalization] = OMIT,
        webhook: typing.Optional[OperatorWebhook] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckOperationRead:
        """
        Parameters
        ----------
        operator_type : OperatorType

        dbt : typing.Optional[OperatorDbt]

        normalization : typing.Optional[OperatorNormalization]

        webhook : typing.Optional[OperatorWebhook]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckOperationRead
            Successful operation

        Examples
        --------
        from fern import FernApi, OperatorType

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.operation.check_operation(
            operator_type=OperatorType.NORMALIZATION,
        )
        """
        _response = self._raw_client.check_operation(
            operator_type=operator_type,
            dbt=dbt,
            normalization=normalization,
            webhook=webhook,
            request_options=request_options,
        )
        return _response.data

    def create_operation(
        self,
        *,
        name: str,
        operator_configuration: OperatorConfiguration,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OperationRead:
        """
        Parameters
        ----------
        name : str

        operator_configuration : OperatorConfiguration

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OperationRead
            Successful operation

        Examples
        --------
        from fern import FernApi, OperatorConfiguration, OperatorType

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.operation.create_operation(
            name="name",
            operator_configuration=OperatorConfiguration(
                operator_type=OperatorType.NORMALIZATION,
            ),
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.create_operation(
            name=name,
            operator_configuration=operator_configuration,
            workspace_id=workspace_id,
            request_options=request_options,
        )
        return _response.data

    def delete_operation(
        self, *, operation_id: OperationId, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        operation_id : OperationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.operation.delete_operation(
            operation_id="operationId",
        )
        """
        _response = self._raw_client.delete_operation(operation_id=operation_id, request_options=request_options)
        return _response.data

    def get_operation(
        self, *, operation_id: OperationId, request_options: typing.Optional[RequestOptions] = None
    ) -> OperationRead:
        """
        Parameters
        ----------
        operation_id : OperationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OperationRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.operation.get_operation(
            operation_id="operationId",
        )
        """
        _response = self._raw_client.get_operation(operation_id=operation_id, request_options=request_options)
        return _response.data

    def list_operations_for_connection(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> OperationReadList:
        """
        List operations for connection.

        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OperationReadList
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.operation.list_operations_for_connection(
            connection_id="connectionId",
        )
        """
        _response = self._raw_client.list_operations_for_connection(
            connection_id=connection_id, request_options=request_options
        )
        return _response.data

    def update_operation(
        self,
        *,
        name: str,
        operation_id: OperationId,
        operator_configuration: OperatorConfiguration,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OperationRead:
        """
        Parameters
        ----------
        name : str

        operation_id : OperationId

        operator_configuration : OperatorConfiguration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OperationRead
            Successful operation

        Examples
        --------
        from fern import FernApi, OperatorConfiguration, OperatorType

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.operation.update_operation(
            name="name",
            operation_id="operationId",
            operator_configuration=OperatorConfiguration(
                operator_type=OperatorType.NORMALIZATION,
            ),
        )
        """
        _response = self._raw_client.update_operation(
            name=name,
            operation_id=operation_id,
            operator_configuration=operator_configuration,
            request_options=request_options,
        )
        return _response.data


class AsyncOperationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOperationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOperationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOperationClient
        """
        return self._raw_client

    async def check_operation(
        self,
        *,
        operator_type: OperatorType,
        dbt: typing.Optional[OperatorDbt] = OMIT,
        normalization: typing.Optional[OperatorNormalization] = OMIT,
        webhook: typing.Optional[OperatorWebhook] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckOperationRead:
        """
        Parameters
        ----------
        operator_type : OperatorType

        dbt : typing.Optional[OperatorDbt]

        normalization : typing.Optional[OperatorNormalization]

        webhook : typing.Optional[OperatorWebhook]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckOperationRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OperatorType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.operation.check_operation(
                operator_type=OperatorType.NORMALIZATION,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.check_operation(
            operator_type=operator_type,
            dbt=dbt,
            normalization=normalization,
            webhook=webhook,
            request_options=request_options,
        )
        return _response.data

    async def create_operation(
        self,
        *,
        name: str,
        operator_configuration: OperatorConfiguration,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OperationRead:
        """
        Parameters
        ----------
        name : str

        operator_configuration : OperatorConfiguration

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OperationRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OperatorConfiguration, OperatorType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.operation.create_operation(
                name="name",
                operator_configuration=OperatorConfiguration(
                    operator_type=OperatorType.NORMALIZATION,
                ),
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_operation(
            name=name,
            operator_configuration=operator_configuration,
            workspace_id=workspace_id,
            request_options=request_options,
        )
        return _response.data

    async def delete_operation(
        self, *, operation_id: OperationId, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        operation_id : OperationId

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.operation.delete_operation(
                operation_id="operationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_operation(operation_id=operation_id, request_options=request_options)
        return _response.data

    async def get_operation(
        self, *, operation_id: OperationId, request_options: typing.Optional[RequestOptions] = None
    ) -> OperationRead:
        """
        Parameters
        ----------
        operation_id : OperationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OperationRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.operation.get_operation(
                operation_id="operationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_operation(operation_id=operation_id, request_options=request_options)
        return _response.data

    async def list_operations_for_connection(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> OperationReadList:
        """
        List operations for connection.

        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OperationReadList
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.operation.list_operations_for_connection(
                connection_id="connectionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_operations_for_connection(
            connection_id=connection_id, request_options=request_options
        )
        return _response.data

    async def update_operation(
        self,
        *,
        name: str,
        operation_id: OperationId,
        operator_configuration: OperatorConfiguration,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OperationRead:
        """
        Parameters
        ----------
        name : str

        operation_id : OperationId

        operator_configuration : OperatorConfiguration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OperationRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OperatorConfiguration, OperatorType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.operation.update_operation(
                name="name",
                operation_id="operationId",
                operator_configuration=OperatorConfiguration(
                    operator_type=OperatorType.NORMALIZATION,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_operation(
            name=name,
            operation_id=operation_id,
            operator_configuration=operator_configuration,
            request_options=request_options,
        )
        return _response.data
