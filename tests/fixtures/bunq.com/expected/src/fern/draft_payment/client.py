

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.draft_payment_create import DraftPaymentCreate
from ..types.draft_payment_entry import DraftPaymentEntry
from ..types.draft_payment_listing import DraftPaymentListing
from ..types.draft_payment_read import DraftPaymentRead
from ..types.draft_payment_update import DraftPaymentUpdate
from ..types.schedule import Schedule
from .raw_client import AsyncRawDraftPaymentClient, RawDraftPaymentClient


OMIT = typing.cast(typing.Any, ...)


class DraftPaymentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDraftPaymentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDraftPaymentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDraftPaymentClient
        """
        return self._raw_client

    def list_all_draft_payment_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DraftPaymentListing]:
        """
        Get a listing of all DraftPayments from a given MonetaryAccount.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DraftPaymentListing]
            A DraftPayment is like a regular Payment, but it needs to be accepted by the sending party before the actual Payment is done.

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
        client.draft_payment.list_all_draft_payment_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
        )
        """
        _response = self._raw_client.list_all_draft_payment_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    def create_draft_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        entries: typing.Sequence[DraftPaymentEntry],
        number_of_required_accepts: int,
        previous_updated_timestamp: typing.Optional[str] = OMIT,
        schedule: typing.Optional[Schedule] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DraftPaymentCreate:
        """
        Create a new DraftPayment.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        entries : typing.Sequence[DraftPaymentEntry]
            The list of entries in the DraftPayment. Each entry will result in a payment when the DraftPayment is accepted.

        number_of_required_accepts : int
            The number of accepts that are required for the draft payment to receive status ACCEPTED. Currently only 1 is valid.

        previous_updated_timestamp : typing.Optional[str]
            The last updated_timestamp that you received for this DraftPayment. This needs to be provided to prevent race conditions.

        schedule : typing.Optional[Schedule]
            The schedule details when creating or updating a scheduled payment.

        status : typing.Optional[str]
            The status of the DraftPayment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DraftPaymentCreate
            A DraftPayment is like a regular Payment, but it needs to be accepted by the sending party before the actual Payment is done.

        Examples
        --------
        from fern import DraftPaymentEntry, FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.draft_payment.create_draft_payment_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            entries=[DraftPaymentEntry()],
            number_of_required_accepts=1,
        )
        """
        _response = self._raw_client.create_draft_payment_for_user_monetary_account(
            user_id,
            monetary_account_id,
            entries=entries,
            number_of_required_accepts=number_of_required_accepts,
            previous_updated_timestamp=previous_updated_timestamp,
            schedule=schedule,
            status=status,
            request_options=request_options,
        )
        return _response.data

    def read_draft_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DraftPaymentRead:
        """
        Get a specific DraftPayment.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DraftPaymentRead
            A DraftPayment is like a regular Payment, but it needs to be accepted by the sending party before the actual Payment is done.

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
        client.draft_payment.read_draft_payment_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_draft_payment_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    def update_draft_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        entries: typing.Sequence[DraftPaymentEntry],
        number_of_required_accepts: int,
        previous_updated_timestamp: typing.Optional[str] = OMIT,
        schedule: typing.Optional[Schedule] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DraftPaymentUpdate:
        """
        Update a DraftPayment.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        entries : typing.Sequence[DraftPaymentEntry]
            The list of entries in the DraftPayment. Each entry will result in a payment when the DraftPayment is accepted.

        number_of_required_accepts : int
            The number of accepts that are required for the draft payment to receive status ACCEPTED. Currently only 1 is valid.

        previous_updated_timestamp : typing.Optional[str]
            The last updated_timestamp that you received for this DraftPayment. This needs to be provided to prevent race conditions.

        schedule : typing.Optional[Schedule]
            The schedule details when creating or updating a scheduled payment.

        status : typing.Optional[str]
            The status of the DraftPayment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DraftPaymentUpdate
            A DraftPayment is like a regular Payment, but it needs to be accepted by the sending party before the actual Payment is done.

        Examples
        --------
        from fern import DraftPaymentEntry, FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.draft_payment.update_draft_payment_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
            entries=[DraftPaymentEntry()],
            number_of_required_accepts=1,
        )
        """
        _response = self._raw_client.update_draft_payment_for_user_monetary_account(
            user_id,
            monetary_account_id,
            item_id,
            entries=entries,
            number_of_required_accepts=number_of_required_accepts,
            previous_updated_timestamp=previous_updated_timestamp,
            schedule=schedule,
            status=status,
            request_options=request_options,
        )
        return _response.data


class AsyncDraftPaymentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDraftPaymentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDraftPaymentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDraftPaymentClient
        """
        return self._raw_client

    async def list_all_draft_payment_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DraftPaymentListing]:
        """
        Get a listing of all DraftPayments from a given MonetaryAccount.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DraftPaymentListing]
            A DraftPayment is like a regular Payment, but it needs to be accepted by the sending party before the actual Payment is done.

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
            await client.draft_payment.list_all_draft_payment_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_draft_payment_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    async def create_draft_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        entries: typing.Sequence[DraftPaymentEntry],
        number_of_required_accepts: int,
        previous_updated_timestamp: typing.Optional[str] = OMIT,
        schedule: typing.Optional[Schedule] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DraftPaymentCreate:
        """
        Create a new DraftPayment.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        entries : typing.Sequence[DraftPaymentEntry]
            The list of entries in the DraftPayment. Each entry will result in a payment when the DraftPayment is accepted.

        number_of_required_accepts : int
            The number of accepts that are required for the draft payment to receive status ACCEPTED. Currently only 1 is valid.

        previous_updated_timestamp : typing.Optional[str]
            The last updated_timestamp that you received for this DraftPayment. This needs to be provided to prevent race conditions.

        schedule : typing.Optional[Schedule]
            The schedule details when creating or updating a scheduled payment.

        status : typing.Optional[str]
            The status of the DraftPayment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DraftPaymentCreate
            A DraftPayment is like a regular Payment, but it needs to be accepted by the sending party before the actual Payment is done.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, DraftPaymentEntry

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.draft_payment.create_draft_payment_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                entries=[DraftPaymentEntry()],
                number_of_required_accepts=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_draft_payment_for_user_monetary_account(
            user_id,
            monetary_account_id,
            entries=entries,
            number_of_required_accepts=number_of_required_accepts,
            previous_updated_timestamp=previous_updated_timestamp,
            schedule=schedule,
            status=status,
            request_options=request_options,
        )
        return _response.data

    async def read_draft_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DraftPaymentRead:
        """
        Get a specific DraftPayment.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DraftPaymentRead
            A DraftPayment is like a regular Payment, but it needs to be accepted by the sending party before the actual Payment is done.

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
            await client.draft_payment.read_draft_payment_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_draft_payment_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_draft_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        entries: typing.Sequence[DraftPaymentEntry],
        number_of_required_accepts: int,
        previous_updated_timestamp: typing.Optional[str] = OMIT,
        schedule: typing.Optional[Schedule] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DraftPaymentUpdate:
        """
        Update a DraftPayment.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        entries : typing.Sequence[DraftPaymentEntry]
            The list of entries in the DraftPayment. Each entry will result in a payment when the DraftPayment is accepted.

        number_of_required_accepts : int
            The number of accepts that are required for the draft payment to receive status ACCEPTED. Currently only 1 is valid.

        previous_updated_timestamp : typing.Optional[str]
            The last updated_timestamp that you received for this DraftPayment. This needs to be provided to prevent race conditions.

        schedule : typing.Optional[Schedule]
            The schedule details when creating or updating a scheduled payment.

        status : typing.Optional[str]
            The status of the DraftPayment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DraftPaymentUpdate
            A DraftPayment is like a regular Payment, but it needs to be accepted by the sending party before the actual Payment is done.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, DraftPaymentEntry

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.draft_payment.update_draft_payment_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
                entries=[DraftPaymentEntry()],
                number_of_required_accepts=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_draft_payment_for_user_monetary_account(
            user_id,
            monetary_account_id,
            item_id,
            entries=entries,
            number_of_required_accepts=number_of_required_accepts,
            previous_updated_timestamp=previous_updated_timestamp,
            schedule=schedule,
            status=status,
            request_options=request_options,
        )
        return _response.data
