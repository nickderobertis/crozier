

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.battle_accepted_response_dto_output import BattleAcceptedResponseDtoOutput
from .raw_client import AsyncRawInternalClient, RawInternalClient


OMIT = typing.cast(typing.Any, ...)


class InternalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInternalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInternalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInternalClient
        """
        return self._raw_client

    def internal_controller_delete_user_data(
        self,
        *,
        user_id: str,
        authorization: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BattleAcceptedResponseDtoOutput:
        """
        Internal API caller only. Requires the BATTLELOG_CLEANUP_SECRET bearer credential; user sessions and forwarded identity headers do not authorize this operation.

        Parameters
        ----------
        user_id : str

        authorization : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleAcceptedResponseDtoOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.internal.internal_controller_delete_user_data(
            user_id="userId",
        )
        """
        _response = self._raw_client.internal_controller_delete_user_data(
            user_id=user_id, authorization=authorization, request_options=request_options
        )
        return _response.data


class AsyncInternalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInternalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInternalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInternalClient
        """
        return self._raw_client

    async def internal_controller_delete_user_data(
        self,
        *,
        user_id: str,
        authorization: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BattleAcceptedResponseDtoOutput:
        """
        Internal API caller only. Requires the BATTLELOG_CLEANUP_SECRET bearer credential; user sessions and forwarded identity headers do not authorize this operation.

        Parameters
        ----------
        user_id : str

        authorization : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleAcceptedResponseDtoOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.internal.internal_controller_delete_user_data(
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.internal_controller_delete_user_data(
            user_id=user_id, authorization=authorization, request_options=request_options
        )
        return _response.data
