

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.process_description import ProcessDescription
from .raw_client import AsyncRawProcessDescriptionClient, RawProcessDescriptionClient


class ProcessDescriptionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProcessDescriptionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProcessDescriptionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProcessDescriptionClient
        """
        return self._raw_client

    def get_process(
        self, process_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProcessDescription:
        """
        The process description contains information about inputs and outputs and a link to the execution-endpoint for the process. The Core does not mandate the use of a specific process description to specify the interface of a process. That said, the Core requirements class makes the following recommendation:

        Implementations **should** consider supporting the OGC process description.

        For more information, see [OGC API — Processes — Part 1 Section 7.10](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_process_description).

        Parameters
        ----------
        process_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessDescription
            A process description.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.process_description.get_process(
            process_id="processID",
        )
        """
        _response = self._raw_client.get_process(process_id, request_options=request_options)
        return _response.data


class AsyncProcessDescriptionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProcessDescriptionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProcessDescriptionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProcessDescriptionClient
        """
        return self._raw_client

    async def get_process(
        self, process_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProcessDescription:
        """
        The process description contains information about inputs and outputs and a link to the execution-endpoint for the process. The Core does not mandate the use of a specific process description to specify the interface of a process. That said, the Core requirements class makes the following recommendation:

        Implementations **should** consider supporting the OGC process description.

        For more information, see [OGC API — Processes — Part 1 Section 7.10](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_process_description).

        Parameters
        ----------
        process_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessDescription
            A process description.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.process_description.get_process(
                process_id="processID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_process(process_id, request_options=request_options)
        return _response.data
