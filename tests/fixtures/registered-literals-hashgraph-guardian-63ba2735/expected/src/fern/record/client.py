

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.record_action_dto import RecordActionDto
from ..types.record_status_dto import RecordStatusDto
from ..types.running_details_dto import RunningDetailsDto
from ..types.running_result_dto import RunningResultDto
from .raw_client import AsyncRawRecordClient, RawRecordClient


OMIT = typing.cast(typing.Any, ...)


class RecordClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRecordClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRecordClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRecordClient
        """
        return self._raw_client

    def record_api_get_record_status(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RecordStatusDto:
        """
        Get recording or running status. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordStatusDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.record.record_api_get_record_status(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.record_api_get_record_status(policy_id, request_options=request_options)
        return _response.data

    def record_api_start_record(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Start recording. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.record.record_api_start_record(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.record_api_start_record(policy_id, request_options=request_options)
        return _response.data

    def record_api_stop_record(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Stop recording. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.record.record_api_stop_record(
            policy_id="policyId",
        )
        """
        with self._raw_client.record_api_stop_record(policy_id, request_options=request_options) as r:
            yield from r.data

    def record_api_get_record_actions(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RecordActionDto]:
        """
        Get recorded actions. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RecordActionDto]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.record.record_api_get_record_actions(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.record_api_get_record_actions(policy_id, request_options=request_options)
        return _response.data

    def record_api_run_record(
        self, policy_id: str, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Run record from a zip file. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.record.record_api_run_record(
            policy_id="policyId",
            request="string",
        )
        """
        _response = self._raw_client.record_api_run_record(policy_id, request=request, request_options=request_options)
        return _response.data

    def record_api_stop_running(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Stop running. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.record.record_api_stop_running(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.record_api_stop_running(policy_id, request_options=request_options)
        return _response.data

    def record_api_get_record_results(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RunningResultDto:
        """
        Get running results. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RunningResultDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.record.record_api_get_record_results(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.record_api_get_record_results(policy_id, request_options=request_options)
        return _response.data

    def record_api_get_record_details(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RunningDetailsDto:
        """
        Get running details. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RunningDetailsDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.record.record_api_get_record_details(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.record_api_get_record_details(policy_id, request_options=request_options)
        return _response.data

    def record_api_fast_forward(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Fast Forward. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.record.record_api_fast_forward(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.record_api_fast_forward(policy_id, request_options=request_options)
        return _response.data

    def record_api_retry_step(self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> bool:
        """
        Retry step. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.record.record_api_retry_step(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.record_api_retry_step(policy_id, request_options=request_options)
        return _response.data

    def record_api_skip_step(self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> bool:
        """
        Skip step. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.record.record_api_skip_step(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.record_api_skip_step(policy_id, request_options=request_options)
        return _response.data


class AsyncRecordClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRecordClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRecordClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRecordClient
        """
        return self._raw_client

    async def record_api_get_record_status(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RecordStatusDto:
        """
        Get recording or running status. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordStatusDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.record.record_api_get_record_status(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_api_get_record_status(policy_id, request_options=request_options)
        return _response.data

    async def record_api_start_record(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Start recording. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.record.record_api_start_record(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_api_start_record(policy_id, request_options=request_options)
        return _response.data

    async def record_api_stop_record(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Stop recording. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.record.record_api_stop_record(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        async with self._raw_client.record_api_stop_record(policy_id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def record_api_get_record_actions(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RecordActionDto]:
        """
        Get recorded actions. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RecordActionDto]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.record.record_api_get_record_actions(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_api_get_record_actions(policy_id, request_options=request_options)
        return _response.data

    async def record_api_run_record(
        self, policy_id: str, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Run record from a zip file. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.record.record_api_run_record(
                policy_id="policyId",
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_api_run_record(
            policy_id, request=request, request_options=request_options
        )
        return _response.data

    async def record_api_stop_running(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Stop running. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.record.record_api_stop_running(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_api_stop_running(policy_id, request_options=request_options)
        return _response.data

    async def record_api_get_record_results(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RunningResultDto:
        """
        Get running results. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RunningResultDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.record.record_api_get_record_results(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_api_get_record_results(policy_id, request_options=request_options)
        return _response.data

    async def record_api_get_record_details(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RunningDetailsDto:
        """
        Get running details. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RunningDetailsDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.record.record_api_get_record_details(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_api_get_record_details(policy_id, request_options=request_options)
        return _response.data

    async def record_api_fast_forward(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Fast Forward. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.record.record_api_fast_forward(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_api_fast_forward(policy_id, request_options=request_options)
        return _response.data

    async def record_api_retry_step(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Retry step. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.record.record_api_retry_step(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_api_retry_step(policy_id, request_options=request_options)
        return _response.data

    async def record_api_skip_step(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Skip step. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.record.record_api_skip_step(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_api_skip_step(policy_id, request_options=request_options)
        return _response.data
