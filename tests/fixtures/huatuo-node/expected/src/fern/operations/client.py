

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.apis_v1components_observation_scope import ApisV1ComponentsObservationScope
from ..types.operation_kind import OperationKind
from ..types.operation_response import OperationResponse
from .raw_client import AsyncRawOperationsClient, RawOperationsClient
from .types.start_operation_request_spec import StartOperationRequestSpec


OMIT = typing.cast(typing.Any, ...)


class OperationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOperationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOperationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOperationsClient
        """
        return self._raw_client

    def start_operation(
        self,
        *,
        duration_seconds: int,
        kind: OperationKind,
        request_id: str,
        scope: ApisV1ComponentsObservationScope,
        spec: StartOperationRequestSpec,
        container_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OperationResponse:
        """
        Parameters
        ----------
        duration_seconds : int

        kind : OperationKind

        request_id : str

        scope : ApisV1ComponentsObservationScope

        spec : StartOperationRequestSpec

        container_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OperationResponse
            Existing idempotent Operation.

        Examples
        --------
        from fern import (
            ApisV1ComponentsObservationScope,
            FernApi,
            OperationKind,
            ProfilingLanguage,
            ProfilingMode,
            ProfilingOperationSpec,
            ProfilingType,
        )

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.operations.start_operation(
            duration_seconds=1000000,
            kind=OperationKind.PROFILING,
            request_id="request_id",
            scope=ApisV1ComponentsObservationScope.HOST,
            spec=ProfilingOperationSpec(
                language=ProfilingLanguage.C,
                mode=ProfilingMode.ON_CPU,
                type=ProfilingType.CPU,
            ),
        )
        """
        _response = self._raw_client.start_operation(
            duration_seconds=duration_seconds,
            kind=kind,
            request_id=request_id,
            scope=scope,
            spec=spec,
            container_id=container_id,
            request_options=request_options,
        )
        return _response.data

    def get_operation(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OperationResponse:
        """
        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OperationResponse
            Operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.operations.get_operation(
            request_id="request_id",
        )
        """
        _response = self._raw_client.get_operation(request_id, request_options=request_options)
        return _response.data

    def stop_operation(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OperationResponse:
        """
        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OperationResponse
            Operation already stopping or terminal.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.operations.stop_operation(
            request_id="request_id",
        )
        """
        _response = self._raw_client.stop_operation(request_id, request_options=request_options)
        return _response.data


class AsyncOperationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOperationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOperationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOperationsClient
        """
        return self._raw_client

    async def start_operation(
        self,
        *,
        duration_seconds: int,
        kind: OperationKind,
        request_id: str,
        scope: ApisV1ComponentsObservationScope,
        spec: StartOperationRequestSpec,
        container_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OperationResponse:
        """
        Parameters
        ----------
        duration_seconds : int

        kind : OperationKind

        request_id : str

        scope : ApisV1ComponentsObservationScope

        spec : StartOperationRequestSpec

        container_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OperationResponse
            Existing idempotent Operation.

        Examples
        --------
        import asyncio

        from fern import (
            ApisV1ComponentsObservationScope,
            AsyncFernApi,
            OperationKind,
            ProfilingLanguage,
            ProfilingMode,
            ProfilingOperationSpec,
            ProfilingType,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.operations.start_operation(
                duration_seconds=1000000,
                kind=OperationKind.PROFILING,
                request_id="request_id",
                scope=ApisV1ComponentsObservationScope.HOST,
                spec=ProfilingOperationSpec(
                    language=ProfilingLanguage.C,
                    mode=ProfilingMode.ON_CPU,
                    type=ProfilingType.CPU,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_operation(
            duration_seconds=duration_seconds,
            kind=kind,
            request_id=request_id,
            scope=scope,
            spec=spec,
            container_id=container_id,
            request_options=request_options,
        )
        return _response.data

    async def get_operation(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OperationResponse:
        """
        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OperationResponse
            Operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.operations.get_operation(
                request_id="request_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_operation(request_id, request_options=request_options)
        return _response.data

    async def stop_operation(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OperationResponse:
        """
        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OperationResponse
            Operation already stopping or terminal.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.operations.stop_operation(
                request_id="request_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stop_operation(request_id, request_options=request_options)
        return _response.data
