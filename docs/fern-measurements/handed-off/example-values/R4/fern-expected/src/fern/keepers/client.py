

import datetime as dt
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
        q: typing.Optional[str] = None,
        rostered_on: typing.Optional[dt.datetime] = None,
        rostered_after: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        keeper_id : str

        season : typing.Optional[str]

        page : typing.Optional[int]

        q : typing.Optional[str]

        rostered_on : typing.Optional[dt.datetime]

        rostered_after : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Shifts

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.keepers.list_keeper_shifts(
            keeper_id="KPR-from-schema",
            season="winter",
            rostered_on=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.list_keeper_shifts(
            keeper_id,
            season=season,
            page=page,
            q=q,
            rostered_on=rostered_on,
            rostered_after=rostered_after,
            request_options=request_options,
        )
        return _response.data

    def list_keeper_callbacks(
        self, *, since: typing.Optional[dt.datetime] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        since : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Callbacks

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.keepers.list_keeper_callbacks()
        """
        _response = self._raw_client.list_keeper_callbacks(since=since, request_options=request_options)
        return _response.data

    def search_keepers(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        q : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Keepers

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.keepers.search_keepers()
        """
        _response = self._raw_client.search_keepers(q=q, request_options=request_options)
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
        q: typing.Optional[str] = None,
        rostered_on: typing.Optional[dt.datetime] = None,
        rostered_after: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        keeper_id : str

        season : typing.Optional[str]

        page : typing.Optional[int]

        q : typing.Optional[str]

        rostered_on : typing.Optional[dt.datetime]

        rostered_after : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Shifts

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.keepers.list_keeper_shifts(
                keeper_id="KPR-from-schema",
                season="winter",
                rostered_on=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_keeper_shifts(
            keeper_id,
            season=season,
            page=page,
            q=q,
            rostered_on=rostered_on,
            rostered_after=rostered_after,
            request_options=request_options,
        )
        return _response.data

    async def list_keeper_callbacks(
        self, *, since: typing.Optional[dt.datetime] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        since : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Callbacks

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.keepers.list_keeper_callbacks()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_keeper_callbacks(since=since, request_options=request_options)
        return _response.data

    async def search_keepers(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        q : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Keepers

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.keepers.search_keepers()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_keepers(q=q, request_options=request_options)
        return _response.data
