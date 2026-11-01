

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.authority import Authority
from ..types.credential import Credential
from .raw_client import AsyncRawAuthClient, RawAuthClient


class AuthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthClient
        """
        return self._raw_client

    def list_the_credentials_associated_with_the_authenticated_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Credential]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Credential]
            A list of credentials associated with this user.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.list_the_credentials_associated_with_the_authenticated_user()
        """
        _response = self._raw_client.list_the_credentials_associated_with_the_authenticated_user(
            request_options=request_options
        )
        return _response.data

    def scopes(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        List available token scopes

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            A list of scopes

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.scopes()
        """
        _response = self._raw_client.scopes(request_options=request_options)
        return _response.data

    def verify_token_and_return_details_of_the_owning_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Authority:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Authority
            Token is valid

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.verify_token_and_return_details_of_the_owning_user()
        """
        _response = self._raw_client.verify_token_and_return_details_of_the_owning_user(request_options=request_options)
        return _response.data


class AsyncAuthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthClient
        """
        return self._raw_client

    async def list_the_credentials_associated_with_the_authenticated_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Credential]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Credential]
            A list of credentials associated with this user.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.list_the_credentials_associated_with_the_authenticated_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_the_credentials_associated_with_the_authenticated_user(
            request_options=request_options
        )
        return _response.data

    async def scopes(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        List available token scopes

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            A list of scopes

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.scopes()


        asyncio.run(main())
        """
        _response = await self._raw_client.scopes(request_options=request_options)
        return _response.data

    async def verify_token_and_return_details_of_the_owning_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Authority:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Authority
            Token is valid

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.verify_token_and_return_details_of_the_owning_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_token_and_return_details_of_the_owning_user(
            request_options=request_options
        )
        return _response.data
