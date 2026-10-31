

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.family_name import FamilyName
from ..types.test_plans_response import TestPlansResponse
from .raw_client import AsyncRawTestPlansClient, RawTestPlansClient


class TestPlansClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTestPlansClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTestPlansClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTestPlansClient
        """
        return self._raw_client

    def get_test_plans(
        self,
        *,
        q: typing.Optional[str] = None,
        families: typing.Optional[typing.Sequence[FamilyName]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestPlansResponse:
        """
        Returns list of distinct test plan names.

        Supports pagination and search filtering.

        Parameters
        ----------
        q : typing.Optional[str]
            Search term for test plan names

        families : typing.Optional[typing.Sequence[FamilyName]]
            Filter by artefact families

        limit : typing.Optional[int]
            Maximum number of results (defaults to 50 if not specified)

        offset : typing.Optional[int]
            Number of results to skip for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestPlansResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.test_plans.get_test_plans()
        """
        _response = self._raw_client.get_test_plans(
            q=q, families=families, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data


class AsyncTestPlansClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTestPlansClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTestPlansClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTestPlansClient
        """
        return self._raw_client

    async def get_test_plans(
        self,
        *,
        q: typing.Optional[str] = None,
        families: typing.Optional[typing.Sequence[FamilyName]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestPlansResponse:
        """
        Returns list of distinct test plan names.

        Supports pagination and search filtering.

        Parameters
        ----------
        q : typing.Optional[str]
            Search term for test plan names

        families : typing.Optional[typing.Sequence[FamilyName]]
            Filter by artefact families

        limit : typing.Optional[int]
            Maximum number of results (defaults to 50 if not specified)

        offset : typing.Optional[int]
            Number of results to skip for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestPlansResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.test_plans.get_test_plans()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_test_plans(
            q=q, families=families, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data
