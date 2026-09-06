

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.update_system_models_checkin_result import UpdateSystemModelsCheckinResult
from .raw_client import AsyncRawUpdatesystemClient, RawUpdatesystemClient


class UpdatesystemClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUpdatesystemClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUpdatesystemClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUpdatesystemClient
        """
        return self._raw_client

    def getcachedfiles(
        self, client_id: str, *, expired: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The ClientID of the Client

        expired : bool
            Only Expired Files (true|false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.updatesystem.getcachedfiles(
            client_id="ClientID",
            expired=True,
        )
        """
        _response = self._raw_client.getcachedfiles(client_id, expired=expired, request_options=request_options)
        return _response.data

    def getcheckin(
        self,
        *,
        client_id: str,
        preview: bool,
        run_all_inventories: typing.Optional[bool] = None,
        transaction_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSystemModelsCheckinResult:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The Client ID to check-in.  If this is a new client ID it will be added to Clients.

        preview : bool
            Get Pkgs w\\o updating Datetimes(true|false)

        run_all_inventories : typing.Optional[bool]
            Force return inventories. Defaults to false.

        transaction_id : typing.Optional[str]
            Optional. The 'NextTransactionID' from the previous check-in. Used to detect duplicate client IDs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemModelsCheckinResult
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.updatesystem.getcheckin(
            client_id="ClientID",
            preview=True,
        )
        """
        _response = self._raw_client.getcheckin(
            client_id=client_id,
            preview=preview,
            run_all_inventories=run_all_inventories,
            transaction_id=transaction_id,
            request_options=request_options,
        )
        return _response.data


class AsyncUpdatesystemClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUpdatesystemClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUpdatesystemClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUpdatesystemClient
        """
        return self._raw_client

    async def getcachedfiles(
        self, client_id: str, *, expired: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The ClientID of the Client

        expired : bool
            Only Expired Files (true|false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.updatesystem.getcachedfiles(
                client_id="ClientID",
                expired=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getcachedfiles(client_id, expired=expired, request_options=request_options)
        return _response.data

    async def getcheckin(
        self,
        *,
        client_id: str,
        preview: bool,
        run_all_inventories: typing.Optional[bool] = None,
        transaction_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSystemModelsCheckinResult:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The Client ID to check-in.  If this is a new client ID it will be added to Clients.

        preview : bool
            Get Pkgs w\\o updating Datetimes(true|false)

        run_all_inventories : typing.Optional[bool]
            Force return inventories. Defaults to false.

        transaction_id : typing.Optional[str]
            Optional. The 'NextTransactionID' from the previous check-in. Used to detect duplicate client IDs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemModelsCheckinResult
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.updatesystem.getcheckin(
                client_id="ClientID",
                preview=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getcheckin(
            client_id=client_id,
            preview=preview,
            run_all_inventories=run_all_inventories,
            transaction_id=transaction_id,
            request_options=request_options,
        )
        return _response.data
