

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.me_deletion import MeDeletion
from ..types.me_deletion_response import MeDeletionResponse
from ..types.me_response import MeResponse
from .raw_client import AsyncRawAccountClient, RawAccountClient


OMIT = typing.cast(typing.Any, ...)


class AccountClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAccountClient
        """
        return self._raw_client

    def get_current_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> MeResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MeResponse
            Current user and account state

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.account.get_current_user()
        """
        _response = self._raw_client.get_current_user(request_options=request_options)
        return _response.data

    def delete_current_user(
        self, *, request: MeDeletion, request_options: typing.Optional[RequestOptions] = None
    ) -> MeDeletionResponse:
        """
        Parameters
        ----------
        request : MeDeletion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MeDeletionResponse
            Account deleted with provider revocation outcome

        Examples
        --------
        from fern import FernApi, MeDeletionZero

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.account.delete_current_user(
            request=MeDeletionZero(),
        )
        """
        _response = self._raw_client.delete_current_user(request=request, request_options=request_options)
        return _response.data

    def update_current_user(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MeResponse:
        """
        Parameters
        ----------
        name : typing.Optional[str]
            Display name

        username : typing.Optional[str]
            Username shown in profile URLs and mentions

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MeResponse
            Updated user and account state

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.account.update_current_user()
        """
        _response = self._raw_client.update_current_user(name=name, username=username, request_options=request_options)
        return _response.data


class AsyncAccountClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAccountClient
        """
        return self._raw_client

    async def get_current_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> MeResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MeResponse
            Current user and account state

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.account.get_current_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_current_user(request_options=request_options)
        return _response.data

    async def delete_current_user(
        self, *, request: MeDeletion, request_options: typing.Optional[RequestOptions] = None
    ) -> MeDeletionResponse:
        """
        Parameters
        ----------
        request : MeDeletion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MeDeletionResponse
            Account deleted with provider revocation outcome

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, MeDeletionZero

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.account.delete_current_user(
                request=MeDeletionZero(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_current_user(request=request, request_options=request_options)
        return _response.data

    async def update_current_user(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MeResponse:
        """
        Parameters
        ----------
        name : typing.Optional[str]
            Display name

        username : typing.Optional[str]
            Username shown in profile URLs and mentions

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MeResponse
            Updated user and account state

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.account.update_current_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_current_user(
            name=name, username=username, request_options=request_options
        )
        return _response.data
