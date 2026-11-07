

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.transfer_send_info import TransferSendInfo
from .raw_client import AsyncRawTransferClient, RawTransferClient


OMIT = typing.cast(typing.Any, ...)


class TransferClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTransferClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTransferClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTransferClient
        """
        return self._raw_client

    def receive(
        self, id4n: str, *, organization_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Taking ownership can be forbidden by a previous owner. See methods prepare and getInfo

        Parameters
        ----------
        id4n : str
            This ID4N identifies the object to take hold of

        organization_id : str
            Organization to take the ownership of the ID. If the sender chose to keep the ownership, this organization becomes the holder. Otherwise, it becomes the new owner.

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
        client.transfer.receive(
            id4n="id4n",
            organization_id="de.id4i",
        )
        """
        _response = self._raw_client.receive(id4n, organization_id=organization_id, request_options=request_options)
        return _response.data

    def get_send_info(self, id4n: str, *, request_options: typing.Optional[RequestOptions] = None) -> TransferSendInfo:
        """
        Parameters
        ----------
        id4n : str
            The ID4N to retrieve information about

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferSendInfo
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.transfer.get_send_info(
            id4n="id4n",
        )
        """
        _response = self._raw_client.get_send_info(id4n, request_options=request_options)
        return _response.data

    def prepare(
        self,
        id4n: str,
        *,
        keep_ownership: bool,
        open_for_claims: bool,
        recipient_organization_ids: typing.Sequence[str],
        holder_organization_id: typing.Optional[str] = OMIT,
        owner_organization_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id4n : str
            The ID4N to prepare for transfer

        keep_ownership : bool
            Keep the public ownership while transferring the object

        open_for_claims : bool
            Allow anyone who knows (or can scan) the ID4N to claim ownership of this object

        recipient_organization_ids : typing.Sequence[str]
            Allow only these organizations to obtain this object

        holder_organization_id : typing.Optional[str]
            The current holder of the object

        owner_organization_id : typing.Optional[str]
            The current publicly visible owner of the object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.transfer.prepare(
            id4n="id4n",
            keep_ownership=True,
            open_for_claims=False,
            recipient_organization_ids=["de.acme", "com.porsche", "de.bluerain"],
        )
        """
        _response = self._raw_client.prepare(
            id4n,
            keep_ownership=keep_ownership,
            open_for_claims=open_for_claims,
            recipient_organization_ids=recipient_organization_ids,
            holder_organization_id=holder_organization_id,
            owner_organization_id=owner_organization_id,
            request_options=request_options,
        )
        return _response.data


class AsyncTransferClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTransferClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTransferClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTransferClient
        """
        return self._raw_client

    async def receive(
        self, id4n: str, *, organization_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Taking ownership can be forbidden by a previous owner. See methods prepare and getInfo

        Parameters
        ----------
        id4n : str
            This ID4N identifies the object to take hold of

        organization_id : str
            Organization to take the ownership of the ID. If the sender chose to keep the ownership, this organization becomes the holder. Otherwise, it becomes the new owner.

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
            await client.transfer.receive(
                id4n="id4n",
                organization_id="de.id4i",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.receive(
            id4n, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def get_send_info(
        self, id4n: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TransferSendInfo:
        """
        Parameters
        ----------
        id4n : str
            The ID4N to retrieve information about

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferSendInfo
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.transfer.get_send_info(
                id4n="id4n",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_send_info(id4n, request_options=request_options)
        return _response.data

    async def prepare(
        self,
        id4n: str,
        *,
        keep_ownership: bool,
        open_for_claims: bool,
        recipient_organization_ids: typing.Sequence[str],
        holder_organization_id: typing.Optional[str] = OMIT,
        owner_organization_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id4n : str
            The ID4N to prepare for transfer

        keep_ownership : bool
            Keep the public ownership while transferring the object

        open_for_claims : bool
            Allow anyone who knows (or can scan) the ID4N to claim ownership of this object

        recipient_organization_ids : typing.Sequence[str]
            Allow only these organizations to obtain this object

        holder_organization_id : typing.Optional[str]
            The current holder of the object

        owner_organization_id : typing.Optional[str]
            The current publicly visible owner of the object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.transfer.prepare(
                id4n="id4n",
                keep_ownership=True,
                open_for_claims=False,
                recipient_organization_ids=["de.acme", "com.porsche", "de.bluerain"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.prepare(
            id4n,
            keep_ownership=keep_ownership,
            open_for_claims=open_for_claims,
            recipient_organization_ids=recipient_organization_ids,
            holder_organization_id=holder_organization_id,
            owner_organization_id=owner_organization_id,
            request_options=request_options,
        )
        return _response.data
