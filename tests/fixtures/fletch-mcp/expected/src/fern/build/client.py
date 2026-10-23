

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawBuildClient, RawBuildClient
from .types.get_builds_id_response import GetBuildsIdResponse
from .types.get_projects_response import GetProjectsResponse


class BuildClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBuildClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBuildClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBuildClient
        """
        return self._raw_client

    def list_this_accounts_projects(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetProjectsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectsResponse
            Projects

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.build.list_this_accounts_projects()
        """
        _response = self._raw_client.list_this_accounts_projects(request_options=request_options)
        return _response.data

    def get_one_builds_status_contracts_and_toolchain_report(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBuildsIdResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBuildsIdResponse
            The build

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.build.get_one_builds_status_contracts_and_toolchain_report(
            id="id",
        )
        """
        _response = self._raw_client.get_one_builds_status_contracts_and_toolchain_report(
            id, request_options=request_options
        )
        return _response.data


class AsyncBuildClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBuildClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBuildClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBuildClient
        """
        return self._raw_client

    async def list_this_accounts_projects(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetProjectsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectsResponse
            Projects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.build.list_this_accounts_projects()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_this_accounts_projects(request_options=request_options)
        return _response.data

    async def get_one_builds_status_contracts_and_toolchain_report(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBuildsIdResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBuildsIdResponse
            The build

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.build.get_one_builds_status_contracts_and_toolchain_report(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_one_builds_status_contracts_and_toolchain_report(
            id, request_options=request_options
        )
        return _response.data
