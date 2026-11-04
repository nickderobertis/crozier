

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.scoped_secret_result_body import ScopedSecretResultBody
from .raw_client import AsyncRawSasClient, RawSasClient


class SasClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSasClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSasClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSasClient
        """
        return self._raw_client

    def get_api_v1sas(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ScopedSecretResultBody]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ScopedSecretResultBody]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sas.get_api_v1sas()
        """
        _response = self._raw_client.get_api_v1sas(request_options=request_options)
        return _response.data


class AsyncSasClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSasClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSasClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSasClient
        """
        return self._raw_client

    async def get_api_v1sas(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ScopedSecretResultBody]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ScopedSecretResultBody]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sas.get_api_v1sas()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v1sas(request_options=request_options)
        return _response.data
