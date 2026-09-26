

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawRulesetsClient, RawRulesetsClient
from .types.ruleset_create_request_data import RulesetCreateRequestData


OMIT = typing.cast(typing.Any, ...)


class RulesetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRulesetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRulesetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRulesetsClient
        """
        return self._raw_client

    def list_rulesets(
        self,
        *,
        page_offset: typing.Optional[int] = None,
        page_limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        page_offset : typing.Optional[int]
            Page offset for pagination

        page_limit : typing.Optional[int]
            Page limit for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rulesets.list_rulesets()
        """
        _response = self._raw_client.list_rulesets(
            page_offset=page_offset, page_limit=page_limit, request_options=request_options
        )
        return _response.data

    def create_ruleset(
        self,
        *,
        data: typing.Optional[RulesetCreateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        data : typing.Optional[RulesetCreateRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rulesets.create_ruleset()
        """
        _response = self._raw_client.create_ruleset(data=data, request_options=request_options)
        return _response.data


class AsyncRulesetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRulesetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRulesetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRulesetsClient
        """
        return self._raw_client

    async def list_rulesets(
        self,
        *,
        page_offset: typing.Optional[int] = None,
        page_limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        page_offset : typing.Optional[int]
            Page offset for pagination

        page_limit : typing.Optional[int]
            Page limit for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rulesets.list_rulesets()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_rulesets(
            page_offset=page_offset, page_limit=page_limit, request_options=request_options
        )
        return _response.data

    async def create_ruleset(
        self,
        *,
        data: typing.Optional[RulesetCreateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        data : typing.Optional[RulesetCreateRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rulesets.create_ruleset()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_ruleset(data=data, request_options=request_options)
        return _response.data
