

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawContributorsClient, RawContributorsClient
from .types.contributor_get_by_id_response import ContributorGetByIdResponse
from .types.contributor_get_top_contributors_response import ContributorGetTopContributorsResponse


class ContributorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawContributorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawContributorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawContributorsClient
        """
        return self._raw_client

    def contributor_get_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContributorGetByIdResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContributorGetByIdResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contributors.contributor_get_by_id(
            id="id",
        )
        """
        _response = self._raw_client.contributor_get_by_id(id, request_options=request_options)
        return _response.data

    def contributor_get_top_contributors(
        self,
        *,
        limit: typing.Optional[float] = None,
        cursor: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContributorGetTopContributorsResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[float]

        cursor : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContributorGetTopContributorsResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contributors.contributor_get_top_contributors()
        """
        _response = self._raw_client.contributor_get_top_contributors(
            limit=limit, cursor=cursor, request_options=request_options
        )
        return _response.data


class AsyncContributorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawContributorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawContributorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawContributorsClient
        """
        return self._raw_client

    async def contributor_get_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContributorGetByIdResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContributorGetByIdResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contributors.contributor_get_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contributor_get_by_id(id, request_options=request_options)
        return _response.data

    async def contributor_get_top_contributors(
        self,
        *,
        limit: typing.Optional[float] = None,
        cursor: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContributorGetTopContributorsResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[float]

        cursor : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContributorGetTopContributorsResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contributors.contributor_get_top_contributors()


        asyncio.run(main())
        """
        _response = await self._raw_client.contributor_get_top_contributors(
            limit=limit, cursor=cursor, request_options=request_options
        )
        return _response.data
