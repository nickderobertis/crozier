

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.consignment import Consignment
from .raw_client import AsyncRawConsignmentsClient, RawConsignmentsClient


class ConsignmentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConsignmentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConsignmentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConsignmentsClient
        """
        return self._raw_client

    def get_consignment(
        self, consignment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Consignment:
        """
        Parameters
        ----------
        consignment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Consignment
            The consignment, whichever way it travels.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.consignments.get_consignment(
            consignment_id="consignmentId",
        )
        """
        _response = self._raw_client.get_consignment(consignment_id, request_options=request_options)
        return _response.data


class AsyncConsignmentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConsignmentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConsignmentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConsignmentsClient
        """
        return self._raw_client

    async def get_consignment(
        self, consignment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Consignment:
        """
        Parameters
        ----------
        consignment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Consignment
            The consignment, whichever way it travels.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.consignments.get_consignment(
                consignment_id="consignmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_consignment(consignment_id, request_options=request_options)
        return _response.data
