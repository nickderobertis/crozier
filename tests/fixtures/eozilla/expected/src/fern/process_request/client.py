

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.job_info import JobInfo
from ..types.output import Output
from ..types.response_type import ResponseType
from ..types.subscriber import Subscriber
from .raw_client import AsyncRawProcessRequestClient, RawProcessRequestClient


OMIT = typing.cast(typing.Any, ...)


class ProcessRequestClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProcessRequestClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProcessRequestClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProcessRequestClient
        """
        return self._raw_client

    def execute_process(
        self,
        process_id: str,
        *,
        inputs: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        outputs: typing.Optional[typing.Dict[str, Output]] = OMIT,
        response: typing.Optional[ResponseType] = OMIT,
        subscriber: typing.Optional[Subscriber] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobInfo:
        """
        Create a new job.

        For more information, see [OGC API — Processes — Part 1 Section 7.11](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_create_job).

        Parameters
        ----------
        process_id : str

        inputs : typing.Optional[typing.Dict[str, typing.Any]]

        outputs : typing.Optional[typing.Dict[str, Output]]

        response : typing.Optional[ResponseType]

        subscriber : typing.Optional[Subscriber]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobInfo
            Started asynchronous execution. Created job.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.process_request.execute_process(
            process_id="processID",
        )
        """
        _response = self._raw_client.execute_process(
            process_id,
            inputs=inputs,
            outputs=outputs,
            response=response,
            subscriber=subscriber,
            request_options=request_options,
        )
        return _response.data


class AsyncProcessRequestClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProcessRequestClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProcessRequestClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProcessRequestClient
        """
        return self._raw_client

    async def execute_process(
        self,
        process_id: str,
        *,
        inputs: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        outputs: typing.Optional[typing.Dict[str, Output]] = OMIT,
        response: typing.Optional[ResponseType] = OMIT,
        subscriber: typing.Optional[Subscriber] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobInfo:
        """
        Create a new job.

        For more information, see [OGC API — Processes — Part 1 Section 7.11](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_create_job).

        Parameters
        ----------
        process_id : str

        inputs : typing.Optional[typing.Dict[str, typing.Any]]

        outputs : typing.Optional[typing.Dict[str, Output]]

        response : typing.Optional[ResponseType]

        subscriber : typing.Optional[Subscriber]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobInfo
            Started asynchronous execution. Created job.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.process_request.execute_process(
                process_id="processID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_process(
            process_id,
            inputs=inputs,
            outputs=outputs,
            response=response,
            subscriber=subscriber,
            request_options=request_options,
        )
        return _response.data
