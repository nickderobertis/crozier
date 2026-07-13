

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.payment_auto_allocate_create import PaymentAutoAllocateCreate
from ..types.payment_auto_allocate_definition import PaymentAutoAllocateDefinition
from ..types.payment_auto_allocate_delete import PaymentAutoAllocateDelete
from ..types.payment_auto_allocate_listing import PaymentAutoAllocateListing
from ..types.payment_auto_allocate_read import PaymentAutoAllocateRead
from ..types.payment_auto_allocate_update import PaymentAutoAllocateUpdate
from ..types.payment_auto_allocate_user_listing import PaymentAutoAllocateUserListing
from .raw_client import AsyncRawPaymentAutoAllocateClient, RawPaymentAutoAllocateClient


OMIT = typing.cast(typing.Any, ...)


class PaymentAutoAllocateClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPaymentAutoAllocateClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPaymentAutoAllocateClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPaymentAutoAllocateClient
        """
        return self._raw_client

    def list_all_payment_auto_allocate_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PaymentAutoAllocateListing]:
        """
        Manage a users automatic payment auto allocated settings.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PaymentAutoAllocateListing]
            Manage a users automatic payment auto allocated settings.

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
        client.payment_auto_allocate.list_all_payment_auto_allocate_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
        )
        """
        _response = self._raw_client.list_all_payment_auto_allocate_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    def create_payment_auto_allocate_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        definition: typing.Sequence[PaymentAutoAllocateDefinition],
        payment_id: int,
        type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentAutoAllocateCreate:
        """
        Manage a users automatic payment auto allocated settings.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        definition : typing.Sequence[PaymentAutoAllocateDefinition]
            The definition of how the money should be allocated.

        payment_id : int
            The payment that should be used to define the triggers for the payment auto allocate.

        type : str
            Whether a payment should be sorted ONCE or RECURRING.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentAutoAllocateCreate
            Manage a users automatic payment auto allocated settings.

        Examples
        --------
        from fern import FernApi, PaymentAutoAllocateDefinition

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.payment_auto_allocate.create_payment_auto_allocate_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            definition=[
                PaymentAutoAllocateDefinition(
                    type="type",
                )
            ],
            payment_id=1,
            type="type",
        )
        """
        _response = self._raw_client.create_payment_auto_allocate_for_user_monetary_account(
            user_id,
            monetary_account_id,
            definition=definition,
            payment_id=payment_id,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def read_payment_auto_allocate_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentAutoAllocateRead:
        """
        Manage a users automatic payment auto allocated settings.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentAutoAllocateRead
            Manage a users automatic payment auto allocated settings.

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
        client.payment_auto_allocate.read_payment_auto_allocate_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_payment_auto_allocate_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    def update_payment_auto_allocate_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        definition: typing.Sequence[PaymentAutoAllocateDefinition],
        payment_id: int,
        type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentAutoAllocateUpdate:
        """
        Manage a users automatic payment auto allocated settings.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        definition : typing.Sequence[PaymentAutoAllocateDefinition]
            The definition of how the money should be allocated.

        payment_id : int
            The payment that should be used to define the triggers for the payment auto allocate.

        type : str
            Whether a payment should be sorted ONCE or RECURRING.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentAutoAllocateUpdate
            Manage a users automatic payment auto allocated settings.

        Examples
        --------
        from fern import FernApi, PaymentAutoAllocateDefinition

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.payment_auto_allocate.update_payment_auto_allocate_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
            definition=[
                PaymentAutoAllocateDefinition(
                    type="type",
                )
            ],
            payment_id=1,
            type="type",
        )
        """
        _response = self._raw_client.update_payment_auto_allocate_for_user_monetary_account(
            user_id,
            monetary_account_id,
            item_id,
            definition=definition,
            payment_id=payment_id,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def delete_payment_auto_allocate_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentAutoAllocateDelete:
        """
        Manage a users automatic payment auto allocated settings.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentAutoAllocateDelete
            Manage a users automatic payment auto allocated settings.

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
        client.payment_auto_allocate.delete_payment_auto_allocate_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_payment_auto_allocate_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_payment_auto_allocate_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PaymentAutoAllocateUserListing]:
        """
        List a users automatic payment auto allocated settings.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PaymentAutoAllocateUserListing]
            List a users automatic payment auto allocated settings.

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
        client.payment_auto_allocate.list_all_payment_auto_allocate_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_payment_auto_allocate_for_user(user_id, request_options=request_options)
        return _response.data


class AsyncPaymentAutoAllocateClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPaymentAutoAllocateClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPaymentAutoAllocateClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPaymentAutoAllocateClient
        """
        return self._raw_client

    async def list_all_payment_auto_allocate_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PaymentAutoAllocateListing]:
        """
        Manage a users automatic payment auto allocated settings.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PaymentAutoAllocateListing]
            Manage a users automatic payment auto allocated settings.

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
            await client.payment_auto_allocate.list_all_payment_auto_allocate_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_payment_auto_allocate_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    async def create_payment_auto_allocate_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        definition: typing.Sequence[PaymentAutoAllocateDefinition],
        payment_id: int,
        type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentAutoAllocateCreate:
        """
        Manage a users automatic payment auto allocated settings.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        definition : typing.Sequence[PaymentAutoAllocateDefinition]
            The definition of how the money should be allocated.

        payment_id : int
            The payment that should be used to define the triggers for the payment auto allocate.

        type : str
            Whether a payment should be sorted ONCE or RECURRING.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentAutoAllocateCreate
            Manage a users automatic payment auto allocated settings.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PaymentAutoAllocateDefinition

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.payment_auto_allocate.create_payment_auto_allocate_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                definition=[
                    PaymentAutoAllocateDefinition(
                        type="type",
                    )
                ],
                payment_id=1,
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_payment_auto_allocate_for_user_monetary_account(
            user_id,
            monetary_account_id,
            definition=definition,
            payment_id=payment_id,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def read_payment_auto_allocate_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentAutoAllocateRead:
        """
        Manage a users automatic payment auto allocated settings.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentAutoAllocateRead
            Manage a users automatic payment auto allocated settings.

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
            await client.payment_auto_allocate.read_payment_auto_allocate_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_payment_auto_allocate_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_payment_auto_allocate_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        definition: typing.Sequence[PaymentAutoAllocateDefinition],
        payment_id: int,
        type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentAutoAllocateUpdate:
        """
        Manage a users automatic payment auto allocated settings.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        definition : typing.Sequence[PaymentAutoAllocateDefinition]
            The definition of how the money should be allocated.

        payment_id : int
            The payment that should be used to define the triggers for the payment auto allocate.

        type : str
            Whether a payment should be sorted ONCE or RECURRING.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentAutoAllocateUpdate
            Manage a users automatic payment auto allocated settings.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PaymentAutoAllocateDefinition

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.payment_auto_allocate.update_payment_auto_allocate_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
                definition=[
                    PaymentAutoAllocateDefinition(
                        type="type",
                    )
                ],
                payment_id=1,
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_payment_auto_allocate_for_user_monetary_account(
            user_id,
            monetary_account_id,
            item_id,
            definition=definition,
            payment_id=payment_id,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def delete_payment_auto_allocate_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentAutoAllocateDelete:
        """
        Manage a users automatic payment auto allocated settings.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentAutoAllocateDelete
            Manage a users automatic payment auto allocated settings.

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
            await client.payment_auto_allocate.delete_payment_auto_allocate_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_payment_auto_allocate_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_payment_auto_allocate_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PaymentAutoAllocateUserListing]:
        """
        List a users automatic payment auto allocated settings.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PaymentAutoAllocateUserListing]
            List a users automatic payment auto allocated settings.

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
            await client.payment_auto_allocate.list_all_payment_auto_allocate_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_payment_auto_allocate_for_user(
            user_id, request_options=request_options
        )
        return _response.data
