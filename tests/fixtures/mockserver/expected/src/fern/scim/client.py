

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.expectation import Expectation
from .raw_client import AsyncRawScimClient, RawScimClient


OMIT = typing.cast(typing.Any, ...)


class ScimClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawScimClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawScimClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawScimClient
        """
        return self._raw_client

    def mock_scim_provider(
        self,
        *,
        base_path: typing.Optional[str] = OMIT,
        require_bearer_token: typing.Optional[bool] = OMIT,
        expected_bearer_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Expectation]:
        """
        Generates a set of expectations that emulate a SCIM 2.0 provisioning provider (Users, Groups and ServiceProviderConfig endpoints) and adds them. An empty body uses the default provider configuration.

        Parameters
        ----------
        base_path : typing.Optional[str]
            base path the SCIM endpoints are served under

        require_bearer_token : typing.Optional[bool]
            whether requests must present a bearer token

        expected_bearer_token : typing.Optional[str]
            bearer token that incoming requests must present when required

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Expectation]
            SCIM provider expectations created

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.scim.mock_scim_provider(
            base_path="/scim/v2",
            require_bearer_token=True,
        )
        """
        _response = self._raw_client.mock_scim_provider(
            base_path=base_path,
            require_bearer_token=require_bearer_token,
            expected_bearer_token=expected_bearer_token,
            request_options=request_options,
        )
        return _response.data


class AsyncScimClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawScimClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawScimClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawScimClient
        """
        return self._raw_client

    async def mock_scim_provider(
        self,
        *,
        base_path: typing.Optional[str] = OMIT,
        require_bearer_token: typing.Optional[bool] = OMIT,
        expected_bearer_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Expectation]:
        """
        Generates a set of expectations that emulate a SCIM 2.0 provisioning provider (Users, Groups and ServiceProviderConfig endpoints) and adds them. An empty body uses the default provider configuration.

        Parameters
        ----------
        base_path : typing.Optional[str]
            base path the SCIM endpoints are served under

        require_bearer_token : typing.Optional[bool]
            whether requests must present a bearer token

        expected_bearer_token : typing.Optional[str]
            bearer token that incoming requests must present when required

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Expectation]
            SCIM provider expectations created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.scim.mock_scim_provider(
                base_path="/scim/v2",
                require_bearer_token=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mock_scim_provider(
            base_path=base_path,
            require_bearer_token=require_bearer_token,
            expected_bearer_token=expected_bearer_token,
            request_options=request_options,
        )
        return _response.data
