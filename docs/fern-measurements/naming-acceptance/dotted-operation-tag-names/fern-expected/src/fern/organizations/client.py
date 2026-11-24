

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawOrganizationsClient, RawOrganizationsClient


class OrganizationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOrganizationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOrganizationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOrganizationsClient
        """
        return self._raw_client

    def org_invitation_list_mine(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.organizations.org_invitation_list_mine()
        """
        _response = self._raw_client.org_invitation_list_mine(request_options=request_options)
        return _response.data


class AsyncOrganizationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOrganizationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOrganizationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOrganizationsClient
        """
        return self._raw_client

    async def org_invitation_list_mine(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.organizations.org_invitation_list_mine()


        asyncio.run(main())
        """
        _response = await self._raw_client.org_invitation_list_mine(request_options=request_options)
        return _response.data
