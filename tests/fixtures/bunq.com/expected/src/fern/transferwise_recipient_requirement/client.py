

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.transferwise_account_requirement_create import TransferwiseAccountRequirementCreate
from ..types.transferwise_account_requirement_listing import TransferwiseAccountRequirementListing
from ..types.transferwise_requirement_field import TransferwiseRequirementField
from .raw_client import AsyncRawTransferwiseRecipientRequirementClient, RawTransferwiseRecipientRequirementClient


OMIT = typing.cast(typing.Any, ...)


class TransferwiseRecipientRequirementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTransferwiseRecipientRequirementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTransferwiseRecipientRequirementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTransferwiseRecipientRequirementClient
        """
        return self._raw_client

    def list_all_transferwise_recipient_requirement_for_user_transferwise_quote(
        self, user_id: int, transferwise_quote_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TransferwiseAccountRequirementListing]:
        """
        Used to determine the recipient account requirements for Transferwise transfers.

        Parameters
        ----------
        user_id : int


        transferwise_quote_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TransferwiseAccountRequirementListing]
            Used to determine the recipient account requirements for Transferwise transfers.

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
        client.transferwise_recipient_requirement.list_all_transferwise_recipient_requirement_for_user_transferwise_quote(
            user_id=1,
            transferwise_quote_id=1,
        )
        """
        _response = self._raw_client.list_all_transferwise_recipient_requirement_for_user_transferwise_quote(
            user_id, transferwise_quote_id, request_options=request_options
        )
        return _response.data

    def create_transferwise_recipient_requirement_for_user_transferwise_quote(
        self,
        user_id: int,
        transferwise_quote_id: int,
        *,
        name_account_holder: str,
        type: str,
        country: typing.Optional[str] = OMIT,
        detail: typing.Optional[typing.Sequence[TransferwiseRequirementField]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferwiseAccountRequirementCreate:
        """
        Used to determine the recipient account requirements for Transferwise transfers.

        Parameters
        ----------
        user_id : int


        transferwise_quote_id : int


        name_account_holder : str
            The name of the account holder.

        type : str
            The chosen recipient account type. The possible options are provided dynamically in the response endpoint.

        country : typing.Optional[str]
            The country of the receiving account.

        detail : typing.Optional[typing.Sequence[TransferwiseRequirementField]]
            The fields which were specified as "required" and have since been filled by the user. Always provide the full list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferwiseAccountRequirementCreate
            Used to determine the recipient account requirements for Transferwise transfers.

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
        client.transferwise_recipient_requirement.create_transferwise_recipient_requirement_for_user_transferwise_quote(
            user_id=1,
            transferwise_quote_id=1,
            name_account_holder="name_account_holder",
            type="type",
        )
        """
        _response = self._raw_client.create_transferwise_recipient_requirement_for_user_transferwise_quote(
            user_id,
            transferwise_quote_id,
            name_account_holder=name_account_holder,
            type=type,
            country=country,
            detail=detail,
            request_options=request_options,
        )
        return _response.data


class AsyncTransferwiseRecipientRequirementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTransferwiseRecipientRequirementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTransferwiseRecipientRequirementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTransferwiseRecipientRequirementClient
        """
        return self._raw_client

    async def list_all_transferwise_recipient_requirement_for_user_transferwise_quote(
        self, user_id: int, transferwise_quote_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TransferwiseAccountRequirementListing]:
        """
        Used to determine the recipient account requirements for Transferwise transfers.

        Parameters
        ----------
        user_id : int


        transferwise_quote_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TransferwiseAccountRequirementListing]
            Used to determine the recipient account requirements for Transferwise transfers.

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
            await client.transferwise_recipient_requirement.list_all_transferwise_recipient_requirement_for_user_transferwise_quote(
                user_id=1,
                transferwise_quote_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_transferwise_recipient_requirement_for_user_transferwise_quote(
            user_id, transferwise_quote_id, request_options=request_options
        )
        return _response.data

    async def create_transferwise_recipient_requirement_for_user_transferwise_quote(
        self,
        user_id: int,
        transferwise_quote_id: int,
        *,
        name_account_holder: str,
        type: str,
        country: typing.Optional[str] = OMIT,
        detail: typing.Optional[typing.Sequence[TransferwiseRequirementField]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferwiseAccountRequirementCreate:
        """
        Used to determine the recipient account requirements for Transferwise transfers.

        Parameters
        ----------
        user_id : int


        transferwise_quote_id : int


        name_account_holder : str
            The name of the account holder.

        type : str
            The chosen recipient account type. The possible options are provided dynamically in the response endpoint.

        country : typing.Optional[str]
            The country of the receiving account.

        detail : typing.Optional[typing.Sequence[TransferwiseRequirementField]]
            The fields which were specified as "required" and have since been filled by the user. Always provide the full list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferwiseAccountRequirementCreate
            Used to determine the recipient account requirements for Transferwise transfers.

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
            await client.transferwise_recipient_requirement.create_transferwise_recipient_requirement_for_user_transferwise_quote(
                user_id=1,
                transferwise_quote_id=1,
                name_account_holder="name_account_holder",
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_transferwise_recipient_requirement_for_user_transferwise_quote(
            user_id,
            transferwise_quote_id,
            name_account_holder=name_account_holder,
            type=type,
            country=country,
            detail=detail,
            request_options=request_options,
        )
        return _response.data
