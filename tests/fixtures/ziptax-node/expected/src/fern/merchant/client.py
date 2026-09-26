

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_merchant_response import CreateMerchantResponse
from ..types.delete_merchant_credentials_response import DeleteMerchantCredentialsResponse
from ..types.delete_merchant_response import DeleteMerchantResponse
from ..types.get_merchant_credentials_response import GetMerchantCredentialsResponse
from ..types.get_merchant_response import GetMerchantResponse
from ..types.item import Item
from ..types.set_merchant_credentials_response import SetMerchantCredentialsResponse
from ..types.update_merchant_response import UpdateMerchantResponse
from ..types.update_struct import UpdateStruct
from .raw_client import AsyncRawMerchantClient, RawMerchantClient
from .types.create_merchant_request_merchant_type import CreateMerchantRequestMerchantType


OMIT = typing.cast(typing.Any, ...)


class MerchantClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMerchantClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMerchantClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMerchantClient
        """
        return self._raw_client

    def create_merchant(
        self,
        *,
        merchant_name: str,
        contact_first: typing.Optional[str] = OMIT,
        contact_last: typing.Optional[str] = OMIT,
        contact_email: typing.Optional[str] = OMIT,
        send_taxcloud_invite: typing.Optional[bool] = OMIT,
        reference_id: typing.Optional[str] = OMIT,
        merchant_type: typing.Optional[CreateMerchantRequestMerchantType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateMerchantResponse:
        """
        Creates a new merchant under the authenticated account. Requires X-API-KEY header.

        Parameters
        ----------
        merchant_name : str
            Legal or trading name of the merchant business. Required; must be 1–255 characters.

        contact_first : typing.Optional[str]
            First name of the merchant's primary contact. Optional.

        contact_last : typing.Optional[str]
            Last name of the merchant's primary contact. Optional.

        contact_email : typing.Optional[str]
            Email address of the merchant's primary contact; used for TaxCloud invitations and notifications. Optional.

        send_taxcloud_invite : typing.Optional[bool]
            Sends invite to set up and connect a TaxCloud account to a merchant who does not already use TaxCloud. To connect a TaxCloud account for a merchant who already uses TaxCloud, use the "Set Merchant Credentials" function. Ignored when merchant_type is 'self-managed'.

        reference_id : typing.Optional[str]
            The ID you use in your own system to identify this merchant.

        merchant_type : typing.Optional[CreateMerchantRequestMerchantType]
            The merchant's compliance model, chosen once at creation. 'taxcloud' (the default) starts the TaxCloud invite process, so TaxCloud can handle registration, filing, and remittance for the merchant. 'self-managed' skips the invite entirely and the merchant is active as soon as the call returns, with the merchant remaining responsible for their own compliance. 'connected' and 'offline' are deprecated aliases for 'taxcloud' and 'self-managed' respectively; they are still accepted but should not be used in new integrations.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateMerchantResponse
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.merchant.create_merchant(
            merchant_name="merchantName",
        )
        """
        _response = self._raw_client.create_merchant(
            merchant_name=merchant_name,
            contact_first=contact_first,
            contact_last=contact_last,
            contact_email=contact_email,
            send_taxcloud_invite=send_taxcloud_invite,
            reference_id=reference_id,
            merchant_type=merchant_type,
            request_options=request_options,
        )
        return _response.data

    def delete_merchant_credentials(
        self, *, merchant_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteMerchantCredentialsResponse:
        """
        Deletes TaxCloud credentials for a merchant. The caller must own the merchant.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant whose TaxCloud credentials are being deleted. The merchant must be owned by the calling account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteMerchantCredentialsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.merchant.delete_merchant_credentials(
            merchant_id="merchantId",
        )
        """
        _response = self._raw_client.delete_merchant_credentials(
            merchant_id=merchant_id, request_options=request_options
        )
        return _response.data

    def get_merchant_credentials(
        self, *, merchant_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMerchantCredentialsResponse:
        """
        Retrieves TaxCloud credentials for a merchant. The caller must own the merchant.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant whose TaxCloud credentials are being retrieved. The merchant must be owned by the calling account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMerchantCredentialsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.merchant.get_merchant_credentials(
            merchant_id="merchantId",
        )
        """
        _response = self._raw_client.get_merchant_credentials(merchant_id=merchant_id, request_options=request_options)
        return _response.data

    def set_merchant_credentials(
        self,
        *,
        api_key: str,
        connection_id: str,
        merchant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SetMerchantCredentialsResponse:
        """
        Sets or updates TaxCloud credentials for a merchant. Credentials are encrypted at rest with AES-256-GCM. On success an asynchronous webhook notification is sent to the configured endpoint.

        Parameters
        ----------
        api_key : str
            TaxCloud API key to associate with the merchant. Stored encrypted at rest with AES-256-GCM.

        connection_id : str
            TaxCloud connection ID that pairs with the API key to identify the merchant's TaxCloud integration.

        merchant_id : str
            UUID of the merchant whose TaxCloud credentials are being set. The merchant must be owned by the calling account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SetMerchantCredentialsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.merchant.set_merchant_credentials(
            api_key="apiKey",
            connection_id="connectionId",
            merchant_id="merchantId",
        )
        """
        _response = self._raw_client.set_merchant_credentials(
            api_key=api_key, connection_id=connection_id, merchant_id=merchant_id, request_options=request_options
        )
        return _response.data

    def delete_merchant(
        self, *, merchant_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteMerchantResponse:
        """
        Soft-deletes a merchant by setting deleted_at to now. The caller must own the merchant. If the merchant is not owned by the caller, or is already soft-deleted (deleted_at <= now), the ownership check returns 403. A 404 is only reachable in a rare race after the ownership check passes.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant to soft-delete. The merchant must be owned by the calling account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteMerchantResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.merchant.delete_merchant(
            merchant_id="merchantId",
        )
        """
        _response = self._raw_client.delete_merchant(merchant_id=merchant_id, request_options=request_options)
        return _response.data

    def get_merchant(
        self, *, merchant_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMerchantResponse:
        """
        Returns a single merchant by UUID. The caller must own the merchant. Cross-account reads are blocked. Soft-deleted merchants (deleted_at <= now) are treated as non-existent and return 404.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant to retrieve. The merchant must be owned by the calling account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMerchantResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.merchant.get_merchant(
            merchant_id="merchantId",
        )
        """
        _response = self._raw_client.get_merchant(merchant_id=merchant_id, request_options=request_options)
        return _response.data

    def list_merchants(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[Item]]:
        """
        Returns every active merchant owned by the calling account. A merchant is considered active when its deleted_at is NULL or set to a future date. Soft-deleted merchants (deleted_at <= now) are excluded from results.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[Item]]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.merchant.list_merchants()
        """
        _response = self._raw_client.list_merchants(request_options=request_options)
        return _response.data

    def update_merchant(
        self, *, merchant_id: str, update: UpdateStruct, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateMerchantResponse:
        """
        Updates an existing merchant. The caller must own the merchant. Cross-account modification is blocked. Soft-deleted merchants (deleted_at <= now), and merchants owned by another account, fail the ownership check and return 403.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant to update. The merchant must be owned by the calling account.

        update : UpdateStruct
            New field values for the merchant

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateMerchantResponse
            OK

        Examples
        --------
        from fern import FernApi, UpdateStruct

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.merchant.update_merchant(
            merchant_id="merchantId",
            update=UpdateStruct(
                merchant_name="merchantName",
            ),
        )
        """
        _response = self._raw_client.update_merchant(
            merchant_id=merchant_id, update=update, request_options=request_options
        )
        return _response.data


class AsyncMerchantClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMerchantClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMerchantClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMerchantClient
        """
        return self._raw_client

    async def create_merchant(
        self,
        *,
        merchant_name: str,
        contact_first: typing.Optional[str] = OMIT,
        contact_last: typing.Optional[str] = OMIT,
        contact_email: typing.Optional[str] = OMIT,
        send_taxcloud_invite: typing.Optional[bool] = OMIT,
        reference_id: typing.Optional[str] = OMIT,
        merchant_type: typing.Optional[CreateMerchantRequestMerchantType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateMerchantResponse:
        """
        Creates a new merchant under the authenticated account. Requires X-API-KEY header.

        Parameters
        ----------
        merchant_name : str
            Legal or trading name of the merchant business. Required; must be 1–255 characters.

        contact_first : typing.Optional[str]
            First name of the merchant's primary contact. Optional.

        contact_last : typing.Optional[str]
            Last name of the merchant's primary contact. Optional.

        contact_email : typing.Optional[str]
            Email address of the merchant's primary contact; used for TaxCloud invitations and notifications. Optional.

        send_taxcloud_invite : typing.Optional[bool]
            Sends invite to set up and connect a TaxCloud account to a merchant who does not already use TaxCloud. To connect a TaxCloud account for a merchant who already uses TaxCloud, use the "Set Merchant Credentials" function. Ignored when merchant_type is 'self-managed'.

        reference_id : typing.Optional[str]
            The ID you use in your own system to identify this merchant.

        merchant_type : typing.Optional[CreateMerchantRequestMerchantType]
            The merchant's compliance model, chosen once at creation. 'taxcloud' (the default) starts the TaxCloud invite process, so TaxCloud can handle registration, filing, and remittance for the merchant. 'self-managed' skips the invite entirely and the merchant is active as soon as the call returns, with the merchant remaining responsible for their own compliance. 'connected' and 'offline' are deprecated aliases for 'taxcloud' and 'self-managed' respectively; they are still accepted but should not be used in new integrations.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateMerchantResponse
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.merchant.create_merchant(
                merchant_name="merchantName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_merchant(
            merchant_name=merchant_name,
            contact_first=contact_first,
            contact_last=contact_last,
            contact_email=contact_email,
            send_taxcloud_invite=send_taxcloud_invite,
            reference_id=reference_id,
            merchant_type=merchant_type,
            request_options=request_options,
        )
        return _response.data

    async def delete_merchant_credentials(
        self, *, merchant_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteMerchantCredentialsResponse:
        """
        Deletes TaxCloud credentials for a merchant. The caller must own the merchant.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant whose TaxCloud credentials are being deleted. The merchant must be owned by the calling account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteMerchantCredentialsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.merchant.delete_merchant_credentials(
                merchant_id="merchantId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_merchant_credentials(
            merchant_id=merchant_id, request_options=request_options
        )
        return _response.data

    async def get_merchant_credentials(
        self, *, merchant_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMerchantCredentialsResponse:
        """
        Retrieves TaxCloud credentials for a merchant. The caller must own the merchant.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant whose TaxCloud credentials are being retrieved. The merchant must be owned by the calling account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMerchantCredentialsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.merchant.get_merchant_credentials(
                merchant_id="merchantId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_merchant_credentials(
            merchant_id=merchant_id, request_options=request_options
        )
        return _response.data

    async def set_merchant_credentials(
        self,
        *,
        api_key: str,
        connection_id: str,
        merchant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SetMerchantCredentialsResponse:
        """
        Sets or updates TaxCloud credentials for a merchant. Credentials are encrypted at rest with AES-256-GCM. On success an asynchronous webhook notification is sent to the configured endpoint.

        Parameters
        ----------
        api_key : str
            TaxCloud API key to associate with the merchant. Stored encrypted at rest with AES-256-GCM.

        connection_id : str
            TaxCloud connection ID that pairs with the API key to identify the merchant's TaxCloud integration.

        merchant_id : str
            UUID of the merchant whose TaxCloud credentials are being set. The merchant must be owned by the calling account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SetMerchantCredentialsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.merchant.set_merchant_credentials(
                api_key="apiKey",
                connection_id="connectionId",
                merchant_id="merchantId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_merchant_credentials(
            api_key=api_key, connection_id=connection_id, merchant_id=merchant_id, request_options=request_options
        )
        return _response.data

    async def delete_merchant(
        self, *, merchant_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteMerchantResponse:
        """
        Soft-deletes a merchant by setting deleted_at to now. The caller must own the merchant. If the merchant is not owned by the caller, or is already soft-deleted (deleted_at <= now), the ownership check returns 403. A 404 is only reachable in a rare race after the ownership check passes.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant to soft-delete. The merchant must be owned by the calling account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteMerchantResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.merchant.delete_merchant(
                merchant_id="merchantId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_merchant(merchant_id=merchant_id, request_options=request_options)
        return _response.data

    async def get_merchant(
        self, *, merchant_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMerchantResponse:
        """
        Returns a single merchant by UUID. The caller must own the merchant. Cross-account reads are blocked. Soft-deleted merchants (deleted_at <= now) are treated as non-existent and return 404.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant to retrieve. The merchant must be owned by the calling account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMerchantResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.merchant.get_merchant(
                merchant_id="merchantId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_merchant(merchant_id=merchant_id, request_options=request_options)
        return _response.data

    async def list_merchants(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[Item]]:
        """
        Returns every active merchant owned by the calling account. A merchant is considered active when its deleted_at is NULL or set to a future date. Soft-deleted merchants (deleted_at <= now) are excluded from results.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[Item]]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.merchant.list_merchants()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_merchants(request_options=request_options)
        return _response.data

    async def update_merchant(
        self, *, merchant_id: str, update: UpdateStruct, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateMerchantResponse:
        """
        Updates an existing merchant. The caller must own the merchant. Cross-account modification is blocked. Soft-deleted merchants (deleted_at <= now), and merchants owned by another account, fail the ownership check and return 403.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant to update. The merchant must be owned by the calling account.

        update : UpdateStruct
            New field values for the merchant

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateMerchantResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, UpdateStruct

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.merchant.update_merchant(
                merchant_id="merchantId",
                update=UpdateStruct(
                    merchant_name="merchantName",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_merchant(
            merchant_id=merchant_id, update=update, request_options=request_options
        )
        return _response.data
