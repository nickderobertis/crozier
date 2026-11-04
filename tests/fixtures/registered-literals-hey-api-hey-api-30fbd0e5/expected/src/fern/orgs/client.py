

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.membership import Membership
from .raw_client import AsyncRawOrgsClient, RawOrgsClient
from .types.orgs_list_response import OrgsListResponse


class OrgsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOrgsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOrgsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOrgsClient
        """
        return self._raw_client

    def list(
        self, *, offset: int, limit: int, request_options: typing.Optional[RequestOptions] = None
    ) -> OrgsListResponse:
        """
        Get all orgs you are a member of

        Parameters
        ----------
        offset : int
            Number of items to skip in order to deliver paginated results

        limit : int
            Maximum items to return in each paginated response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrgsListResponse
            A paginated result set

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orgs.list(
            offset=1,
            limit=1,
        )
        """
        _response = self._raw_client.list(offset=offset, limit=limit, request_options=request_options)
        return _response.data

    def memberships_list(
        self, org_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Membership]:
        """
        List all memberships of an org

        Parameters
        ----------
        org_id : str
            Id of an org

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Membership]
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orgs.memberships_list(
            org_id="org_id",
        )
        """
        _response = self._raw_client.memberships_list(org_id, request_options=request_options)
        return _response.data


class AsyncOrgsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOrgsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOrgsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOrgsClient
        """
        return self._raw_client

    async def list(
        self, *, offset: int, limit: int, request_options: typing.Optional[RequestOptions] = None
    ) -> OrgsListResponse:
        """
        Get all orgs you are a member of

        Parameters
        ----------
        offset : int
            Number of items to skip in order to deliver paginated results

        limit : int
            Maximum items to return in each paginated response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrgsListResponse
            A paginated result set

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orgs.list(
                offset=1,
                limit=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(offset=offset, limit=limit, request_options=request_options)
        return _response.data

    async def memberships_list(
        self, org_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Membership]:
        """
        List all memberships of an org

        Parameters
        ----------
        org_id : str
            Id of an org

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Membership]
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orgs.memberships_list(
                org_id="org_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.memberships_list(org_id, request_options=request_options)
        return _response.data
