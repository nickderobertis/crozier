

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.transferwise_requirement_field import TransferwiseRequirementField
from ..types.transferwise_transfer_requirement_create import TransferwiseTransferRequirementCreate
from .raw_client import AsyncRawTransferwiseTransferRequirementClient, RawTransferwiseTransferRequirementClient


OMIT = typing.cast(typing.Any, ...)


class TransferwiseTransferRequirementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTransferwiseTransferRequirementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTransferwiseTransferRequirementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTransferwiseTransferRequirementClient
        """
        return self._raw_client

    def create_transferwise_transfer_requirement_for_user_transferwise_quote(
        self,
        user_id: int,
        transferwise_quote_id: int,
        *,
        recipient_id: str,
        detail: typing.Optional[typing.Sequence[TransferwiseRequirementField]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferwiseTransferRequirementCreate:
        """
        Used to determine the account requirements for Transferwise transfers.

        Parameters
        ----------
        user_id : int


        transferwise_quote_id : int


        recipient_id : str
            The id of the target account.

        detail : typing.Optional[typing.Sequence[TransferwiseRequirementField]]
            The fields which were specified as "required" and have since been filled by the user. Always provide the full list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferwiseTransferRequirementCreate
            Used to determine the account requirements for Transferwise transfers.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.transferwise_transfer_requirement.create_transferwise_transfer_requirement_for_user_transferwise_quote(
            user_id=1,
            transferwise_quote_id=1,
            recipient_id="recipient_id",
        )
        """
        _response = self._raw_client.create_transferwise_transfer_requirement_for_user_transferwise_quote(
            user_id, transferwise_quote_id, recipient_id=recipient_id, detail=detail, request_options=request_options
        )
        return _response.data


class AsyncTransferwiseTransferRequirementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTransferwiseTransferRequirementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTransferwiseTransferRequirementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTransferwiseTransferRequirementClient
        """
        return self._raw_client

    async def create_transferwise_transfer_requirement_for_user_transferwise_quote(
        self,
        user_id: int,
        transferwise_quote_id: int,
        *,
        recipient_id: str,
        detail: typing.Optional[typing.Sequence[TransferwiseRequirementField]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferwiseTransferRequirementCreate:
        """
        Used to determine the account requirements for Transferwise transfers.

        Parameters
        ----------
        user_id : int


        transferwise_quote_id : int


        recipient_id : str
            The id of the target account.

        detail : typing.Optional[typing.Sequence[TransferwiseRequirementField]]
            The fields which were specified as "required" and have since been filled by the user. Always provide the full list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferwiseTransferRequirementCreate
            Used to determine the account requirements for Transferwise transfers.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.transferwise_transfer_requirement.create_transferwise_transfer_requirement_for_user_transferwise_quote(
                user_id=1,
                transferwise_quote_id=1,
                recipient_id="recipient_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_transferwise_transfer_requirement_for_user_transferwise_quote(
            user_id, transferwise_quote_id, recipient_id=recipient_id, detail=detail, request_options=request_options
        )
        return _response.data
