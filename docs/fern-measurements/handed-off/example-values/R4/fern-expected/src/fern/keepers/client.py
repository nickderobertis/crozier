

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawKeepersClient, RawKeepersClient


class KeepersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawKeepersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawKeepersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawKeepersClient
        """
        return self._raw_client

    def list_keeper_shifts(
        self,
        keeper_id: str,
        *,
        season: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        keeper_id : str

        season : typing.Optional[str]

        page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Shifts

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.keepers.list_keeper_shifts(
            keeper_id="KPR-from-schema",
            season="winter",
        )
        """
        _response = self._raw_client.list_keeper_shifts(
            keeper_id, season=season, page=page, request_options=request_options
        )
        return _response.data


class AsyncKeepersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawKeepersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawKeepersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawKeepersClient
        """
        return self._raw_client

    async def list_keeper_shifts(
        self,
        keeper_id: str,
        *,
        season: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        keeper_id : str

        season : typing.Optional[str]

        page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Shifts

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.keepers.list_keeper_shifts(
                keeper_id="KPR-from-schema",
                season="winter",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_keeper_shifts(
            keeper_id, season=season, page=page, request_options=request_options
        )
        return _response.data
