

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_key_dto import ApiKeyDto
from .raw_client import AsyncRawApiKeysClient, RawApiKeysClient


OMIT = typing.cast(typing.Any, ...)


class ApiKeysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawApiKeysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawApiKeysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawApiKeysClient
        """
        return self._raw_client

    def get_api_keys_for_current_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ApiKeyDto]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ApiKeyDto]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.api_keys.get_api_keys_for_current_user()
        """
        _response = self._raw_client.get_api_keys_for_current_user(request_options=request_options)
        return _response.data

    def create_api_key_for_current_user(
        self, *, comment: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiKeyDto:
        """
        Parameters
        ----------
        comment : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKeyDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.api_keys.create_api_key_for_current_user(
            comment="comment",
        )
        """
        _response = self._raw_client.create_api_key_for_current_user(comment=comment, request_options=request_options)
        return _response.data

    def delete_api_key_by_key_id(self, key_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        key_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.api_keys.delete_api_key_by_key_id(
            key_id="keyId",
        )
        """
        _response = self._raw_client.delete_api_key_by_key_id(key_id, request_options=request_options)
        return _response.data


class AsyncApiKeysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawApiKeysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawApiKeysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawApiKeysClient
        """
        return self._raw_client

    async def get_api_keys_for_current_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ApiKeyDto]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ApiKeyDto]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.api_keys.get_api_keys_for_current_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_keys_for_current_user(request_options=request_options)
        return _response.data

    async def create_api_key_for_current_user(
        self, *, comment: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiKeyDto:
        """
        Parameters
        ----------
        comment : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKeyDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.api_keys.create_api_key_for_current_user(
                comment="comment",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_api_key_for_current_user(
            comment=comment, request_options=request_options
        )
        return _response.data

    async def delete_api_key_by_key_id(
        self, key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        key_id : str

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.api_keys.delete_api_key_by_key_id(
                key_id="keyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_api_key_by_key_id(key_id, request_options=request_options)
        return _response.data
