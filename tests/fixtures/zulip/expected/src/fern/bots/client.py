

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.json_success import JsonSuccess
from .raw_client import AsyncRawBotsClient, RawBotsClient
from .types.get_bot_storage_response import GetBotStorageResponse


OMIT = typing.cast(typing.Any, ...)


class BotsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBotsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBotsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBotsClient
        """
        return self._raw_client

    def get_bot_storage(
        self, *, keys: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBotStorageResponse:
        """
        !!! warn ""

            **Note:** This endpoint is only available to [bot user](/help/bots-overview)
            accounts.

        Retrieve [data stored](/help/interactive-bots-api#bot_handlerstorage)
        for a bot user.

        **Changes**: Prior to Zulip 12.0 (feature level 494), users who
        were not bots could access this endpoint.

        Parameters
        ----------
        keys : typing.Optional[str]
            A JSON-encoded list of keys for data in the bot's storage.

            If not provided, then all data that's stored for the bot is
            returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBotStorageResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.bots.get_bot_storage()
        """
        _response = self._raw_client.get_bot_storage(keys=keys, request_options=request_options)
        return _response.data

    def update_bot_storage(
        self, *, storage: typing.Dict[str, str], request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        !!! warn ""

            **Note:** This endpoint is only available to [bot user](/help/bots-overview)
            accounts.

        Add or update [data stored](/help/interactive-bots-api#bot_handlerstorage)
        for a bot user.

        Each bot has a limited storage set by the server, which normally is a
        default of 10,000,000 characters.

        **Changes**: Prior to Zulip 12.0 (feature level 494), users who
        were not bots could access this endpoint.

        Parameters
        ----------
        storage : typing.Dict[str, str]
            A JSON-encoded dictionary mapping string keys to string values
            that will be added to the bot's storage.

            If the bot's storage already has a specific key, then the value
            stored for that key will be updated for the new value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.bots.update_bot_storage(
            storage={"foo": "bar"},
        )
        """
        _response = self._raw_client.update_bot_storage(storage=storage, request_options=request_options)
        return _response.data

    def remove_bot_storage(
        self,
        *,
        keys: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        !!! warn ""

            **Note:** This endpoint is only available to [bot user](/help/bots-overview)
            accounts.

        Delete [data stored](/help/interactive-bots-api#bot_handlerstorage)
        for a bot user.

        **Changes**: Prior to Zulip 12.0 (feature level 494), users who
        were not bots could access this endpoint.

        Parameters
        ----------
        keys : typing.Optional[typing.Sequence[str]]
            A JSON-encoded list of keys to delete from the bot's storage.

            If not provided, then all data that's stored for the bot is
            deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.bots.remove_bot_storage()
        """
        _response = self._raw_client.remove_bot_storage(keys=keys, request_options=request_options)
        return _response.data


class AsyncBotsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBotsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBotsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBotsClient
        """
        return self._raw_client

    async def get_bot_storage(
        self, *, keys: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBotStorageResponse:
        """
        !!! warn ""

            **Note:** This endpoint is only available to [bot user](/help/bots-overview)
            accounts.

        Retrieve [data stored](/help/interactive-bots-api#bot_handlerstorage)
        for a bot user.

        **Changes**: Prior to Zulip 12.0 (feature level 494), users who
        were not bots could access this endpoint.

        Parameters
        ----------
        keys : typing.Optional[str]
            A JSON-encoded list of keys for data in the bot's storage.

            If not provided, then all data that's stored for the bot is
            returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBotStorageResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.bots.get_bot_storage()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_bot_storage(keys=keys, request_options=request_options)
        return _response.data

    async def update_bot_storage(
        self, *, storage: typing.Dict[str, str], request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        !!! warn ""

            **Note:** This endpoint is only available to [bot user](/help/bots-overview)
            accounts.

        Add or update [data stored](/help/interactive-bots-api#bot_handlerstorage)
        for a bot user.

        Each bot has a limited storage set by the server, which normally is a
        default of 10,000,000 characters.

        **Changes**: Prior to Zulip 12.0 (feature level 494), users who
        were not bots could access this endpoint.

        Parameters
        ----------
        storage : typing.Dict[str, str]
            A JSON-encoded dictionary mapping string keys to string values
            that will be added to the bot's storage.

            If the bot's storage already has a specific key, then the value
            stored for that key will be updated for the new value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.bots.update_bot_storage(
                storage={"foo": "bar"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_bot_storage(storage=storage, request_options=request_options)
        return _response.data

    async def remove_bot_storage(
        self,
        *,
        keys: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        !!! warn ""

            **Note:** This endpoint is only available to [bot user](/help/bots-overview)
            accounts.

        Delete [data stored](/help/interactive-bots-api#bot_handlerstorage)
        for a bot user.

        **Changes**: Prior to Zulip 12.0 (feature level 494), users who
        were not bots could access this endpoint.

        Parameters
        ----------
        keys : typing.Optional[typing.Sequence[str]]
            A JSON-encoded list of keys to delete from the bot's storage.

            If not provided, then all data that's stored for the bot is
            deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.bots.remove_bot_storage()


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_bot_storage(keys=keys, request_options=request_options)
        return _response.data
