

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.sandbox_user_person import SandboxUserPerson
from ..types.sandbox_user_person_create import SandboxUserPersonCreate
from .raw_client import AsyncRawSandboxUserPersonClient, RawSandboxUserPersonClient


OMIT = typing.cast(typing.Any, ...)


class SandboxUserPersonClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSandboxUserPersonClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSandboxUserPersonClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSandboxUserPersonClient
        """
        return self._raw_client

    def create_sandbox_user_person(
        self, *, request: SandboxUserPerson, request_options: typing.Optional[RequestOptions] = None
    ) -> SandboxUserPersonCreate:
        """
        Used to create a sandbox userPerson.

        Parameters
        ----------
        request : SandboxUserPerson

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxUserPersonCreate
            Used to create a sandbox userPerson.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.sandbox_user_person.create_sandbox_user_person(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.create_sandbox_user_person(request=request, request_options=request_options)
        return _response.data


class AsyncSandboxUserPersonClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSandboxUserPersonClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSandboxUserPersonClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSandboxUserPersonClient
        """
        return self._raw_client

    async def create_sandbox_user_person(
        self, *, request: SandboxUserPerson, request_options: typing.Optional[RequestOptions] = None
    ) -> SandboxUserPersonCreate:
        """
        Used to create a sandbox userPerson.

        Parameters
        ----------
        request : SandboxUserPerson

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxUserPersonCreate
            Used to create a sandbox userPerson.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.sandbox_user_person.create_sandbox_user_person(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_sandbox_user_person(request=request, request_options=request_options)
        return _response.data
