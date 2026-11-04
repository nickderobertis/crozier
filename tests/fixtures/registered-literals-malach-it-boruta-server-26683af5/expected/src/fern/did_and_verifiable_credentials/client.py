

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawDidAndVerifiableCredentialsClient, RawDidAndVerifiableCredentialsClient


class DidAndVerifiableCredentialsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDidAndVerifiableCredentialsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDidAndVerifiableCredentialsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDidAndVerifiableCredentialsClient
        """
        return self._raw_client

    def resolve_a_verifiable_credential_status(
        self, status: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        status : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Resolved status

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.did_and_verifiable_credentials.resolve_a_verifiable_credential_status(
            status="status",
        )
        """
        _response = self._raw_client.resolve_a_verifiable_credential_status(status, request_options=request_options)
        return _response.data


class AsyncDidAndVerifiableCredentialsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDidAndVerifiableCredentialsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDidAndVerifiableCredentialsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDidAndVerifiableCredentialsClient
        """
        return self._raw_client

    async def resolve_a_verifiable_credential_status(
        self, status: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        status : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Resolved status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.did_and_verifiable_credentials.resolve_a_verifiable_credential_status(
                status="status",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resolve_a_verifiable_credential_status(
            status, request_options=request_options
        )
        return _response.data
