

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.relation import Relation
from .raw_client import AsyncRawRulesClient, RawRulesClient


OMIT = typing.cast(typing.Any, ...)


class RulesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRulesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRulesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRulesClient
        """
        return self._raw_client

    def add_rule(
        self, *, relation: Relation, threshold: float, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        relation : Relation

        threshold : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rules.add_rule(
            relation="<",
            threshold=1.1,
        )
        """
        _response = self._raw_client.add_rule(relation=relation, threshold=threshold, request_options=request_options)
        return _response.data


class AsyncRulesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRulesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRulesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRulesClient
        """
        return self._raw_client

    async def add_rule(
        self, *, relation: Relation, threshold: float, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        relation : Relation

        threshold : float

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rules.add_rule(
                relation="<",
                threshold=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_rule(
            relation=relation, threshold=threshold, request_options=request_options
        )
        return _response.data
