

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.credential_response import CredentialResponse
from .raw_client import AsyncRawOpenIdForVerifiableCredentialsClient, RawOpenIdForVerifiableCredentialsClient


OMIT = typing.cast(typing.Any, ...)


class OpenIdForVerifiableCredentialsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOpenIdForVerifiableCredentialsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOpenIdForVerifiableCredentialsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOpenIdForVerifiableCredentialsClient
        """
        return self._raw_client

    def issue_a_credential(
        self,
        *,
        format: typing.Optional[str] = OMIT,
        credential_definition: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        types: typing.Optional[typing.Sequence[str]] = OMIT,
        proof: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CredentialResponse:
        """
        Parameters
        ----------
        format : typing.Optional[str]

        credential_definition : typing.Optional[typing.Dict[str, typing.Any]]

        types : typing.Optional[typing.Sequence[str]]

        proof : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CredentialResponse
            Credential or deferred credential response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.open_id_for_verifiable_credentials.issue_a_credential()
        """
        _response = self._raw_client.issue_a_credential(
            format=format,
            credential_definition=credential_definition,
            types=types,
            proof=proof,
            request_options=request_options,
        )
        return _response.data

    def retrieve_a_deferred_credential(
        self, *, acceptance_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CredentialResponse:
        """
        The route uses the spelling implemented by the service: defered-credential.

        Parameters
        ----------
        acceptance_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CredentialResponse
            Credential or deferred credential response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.open_id_for_verifiable_credentials.retrieve_a_deferred_credential(
            acceptance_token="acceptance_token",
        )
        """
        _response = self._raw_client.retrieve_a_deferred_credential(
            acceptance_token=acceptance_token, request_options=request_options
        )
        return _response.data


class AsyncOpenIdForVerifiableCredentialsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOpenIdForVerifiableCredentialsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOpenIdForVerifiableCredentialsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOpenIdForVerifiableCredentialsClient
        """
        return self._raw_client

    async def issue_a_credential(
        self,
        *,
        format: typing.Optional[str] = OMIT,
        credential_definition: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        types: typing.Optional[typing.Sequence[str]] = OMIT,
        proof: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CredentialResponse:
        """
        Parameters
        ----------
        format : typing.Optional[str]

        credential_definition : typing.Optional[typing.Dict[str, typing.Any]]

        types : typing.Optional[typing.Sequence[str]]

        proof : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CredentialResponse
            Credential or deferred credential response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.open_id_for_verifiable_credentials.issue_a_credential()


        asyncio.run(main())
        """
        _response = await self._raw_client.issue_a_credential(
            format=format,
            credential_definition=credential_definition,
            types=types,
            proof=proof,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_a_deferred_credential(
        self, *, acceptance_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CredentialResponse:
        """
        The route uses the spelling implemented by the service: defered-credential.

        Parameters
        ----------
        acceptance_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CredentialResponse
            Credential or deferred credential response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.open_id_for_verifiable_credentials.retrieve_a_deferred_credential(
                acceptance_token="acceptance_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_deferred_credential(
            acceptance_token=acceptance_token, request_options=request_options
        )
        return _response.data
