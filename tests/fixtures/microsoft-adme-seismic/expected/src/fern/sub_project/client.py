

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.sub_project import SubProject
from .raw_client import AsyncRawSubProjectClient, RawSubProjectClient


class SubProjectClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSubProjectClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSubProjectClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSubProjectClient
        """
        return self._raw_client

    def sub_project_list(
        self, tenantid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SubProject]:
        """
        <ul><li>Return the list of sub-projects in a tenant.</li><li>Required roles: users.datalake.admin</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SubProject]
            Retrieved the list of subprojects in the tenant successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.sub_project.sub_project_list(
            tenantid="tenantid",
        )
        """
        _response = self._raw_client.sub_project_list(tenantid, request_options=request_options)
        return _response.data


class AsyncSubProjectClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSubProjectClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSubProjectClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSubProjectClient
        """
        return self._raw_client

    async def sub_project_list(
        self, tenantid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SubProject]:
        """
        <ul><li>Return the list of sub-projects in a tenant.</li><li>Required roles: users.datalake.admin</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SubProject]
            Retrieved the list of subprojects in the tenant successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.sub_project.sub_project_list(
                tenantid="tenantid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sub_project_list(tenantid, request_options=request_options)
        return _response.data
