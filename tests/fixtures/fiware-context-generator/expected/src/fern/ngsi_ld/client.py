

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawNgsiLdClient, RawNgsiLdClient
from .types.get_ngsi_ld_v1entities_request_type import GetNgsiLdV1EntitiesRequestType


class NgsiLdClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNgsiLdClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNgsiLdClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNgsiLdClient
        """
        return self._raw_client

    def get_ngsi_ld_v1entities(
        self, *, type: GetNgsiLdV1EntitiesRequestType, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Retrieve a set of entities which matches a specific query from an NGSI-LD system

        Parameters
        ----------
        type : GetNgsiLdV1EntitiesRequestType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        from fern.ngsi_ld import GetNgsiLdV1EntitiesRequestType

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.ngsi_ld.get_ngsi_ld_v1entities(
            type=GetNgsiLdV1EntitiesRequestType.ORGANIZATION,
        )
        """
        _response = self._raw_client.get_ngsi_ld_v1entities(type=type, request_options=request_options)
        return _response.data


class AsyncNgsiLdClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNgsiLdClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNgsiLdClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNgsiLdClient
        """
        return self._raw_client

    async def get_ngsi_ld_v1entities(
        self, *, type: GetNgsiLdV1EntitiesRequestType, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Retrieve a set of entities which matches a specific query from an NGSI-LD system

        Parameters
        ----------
        type : GetNgsiLdV1EntitiesRequestType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        import asyncio

        from fern.ngsi_ld import GetNgsiLdV1EntitiesRequestType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.ngsi_ld.get_ngsi_ld_v1entities(
                type=GetNgsiLdV1EntitiesRequestType.ORGANIZATION,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_ngsi_ld_v1entities(type=type, request_options=request_options)
        return _response.data
