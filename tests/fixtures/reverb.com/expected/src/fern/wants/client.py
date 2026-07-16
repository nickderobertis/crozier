

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWantsClient, RawWantsClient


class WantsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWantsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWantsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWantsClient
        """
        return self._raw_client

    def a_list_of_wanted_items_by_the_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        A list of wanted items by the user

        Parameters
        ----------
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
        client.wants.a_list_of_wanted_items_by_the_user()
        """
        _response = self._raw_client.a_list_of_wanted_items_by_the_user(request_options=request_options)
        return _response.data

    def mark_an_item_wanted_returns200on_success_or422on_failure(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Mark an item wanted. Returns 200 on success or 422 on failure.

        Parameters
        ----------
        id : str

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
        client.wants.mark_an_item_wanted_returns200on_success_or422on_failure(
            id="id",
        )
        """
        _response = self._raw_client.mark_an_item_wanted_returns200on_success_or422on_failure(
            id, request_options=request_options
        )
        return _response.data

    def unmark_an_item_wanted(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Unmark an item wanted.

        Parameters
        ----------
        id : str

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
        client.wants.unmark_an_item_wanted(
            id="id",
        )
        """
        _response = self._raw_client.unmark_an_item_wanted(id, request_options=request_options)
        return _response.data


class AsyncWantsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWantsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWantsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWantsClient
        """
        return self._raw_client

    async def a_list_of_wanted_items_by_the_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        A list of wanted items by the user

        Parameters
        ----------
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
            await client.wants.a_list_of_wanted_items_by_the_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.a_list_of_wanted_items_by_the_user(request_options=request_options)
        return _response.data

    async def mark_an_item_wanted_returns200on_success_or422on_failure(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Mark an item wanted. Returns 200 on success or 422 on failure.

        Parameters
        ----------
        id : str

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
            await client.wants.mark_an_item_wanted_returns200on_success_or422on_failure(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mark_an_item_wanted_returns200on_success_or422on_failure(
            id, request_options=request_options
        )
        return _response.data

    async def unmark_an_item_wanted(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Unmark an item wanted.

        Parameters
        ----------
        id : str

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
            await client.wants.unmark_an_item_wanted(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unmark_an_item_wanted(id, request_options=request_options)
        return _response.data
