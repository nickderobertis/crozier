

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.list_bolts_request_finish import ListBoltsRequestFinish
from .raw_client import AsyncRawBoltsClient, RawBoltsClient
from .types.get_bolts_by_weave_request_weave import GetBoltsByWeaveRequestWeave
from .types.list_bolts_request_weave import ListBoltsRequestWeave


class BoltsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBoltsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBoltsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBoltsClient
        """
        return self._raw_client

    def list_bolts(
        self,
        *,
        weave: ListBoltsRequestWeave,
        finish: typing.Optional[ListBoltsRequestFinish] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        weave : ListBoltsRequestWeave

        finish : typing.Optional[ListBoltsRequestFinish]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Bolts of cloth.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.bolts.list_bolts(
            weave="plain",
        )
        """
        _response = self._raw_client.list_bolts(weave=weave, finish=finish, request_options=request_options)
        return _response.data

    def get_bolts_by_weave(
        self, weave: GetBoltsByWeaveRequestWeave, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        weave : GetBoltsByWeaveRequestWeave

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Bolts woven one way.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.bolts.get_bolts_by_weave(
            weave="plain",
        )
        """
        _response = self._raw_client.get_bolts_by_weave(weave, request_options=request_options)
        return _response.data


class AsyncBoltsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBoltsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBoltsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBoltsClient
        """
        return self._raw_client

    async def list_bolts(
        self,
        *,
        weave: ListBoltsRequestWeave,
        finish: typing.Optional[ListBoltsRequestFinish] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        weave : ListBoltsRequestWeave

        finish : typing.Optional[ListBoltsRequestFinish]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Bolts of cloth.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.bolts.list_bolts(
                weave="plain",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_bolts(weave=weave, finish=finish, request_options=request_options)
        return _response.data

    async def get_bolts_by_weave(
        self, weave: GetBoltsByWeaveRequestWeave, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        weave : GetBoltsByWeaveRequestWeave

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Bolts woven one way.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.bolts.get_bolts_by_weave(
                weave="plain",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_bolts_by_weave(weave, request_options=request_options)
        return _response.data
