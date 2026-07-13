

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.currency_cloud_beneficiary_create import CurrencyCloudBeneficiaryCreate
from ..types.currency_cloud_beneficiary_listing import CurrencyCloudBeneficiaryListing
from ..types.currency_cloud_beneficiary_read import CurrencyCloudBeneficiaryRead
from .raw_client import AsyncRawCurrencyCloudBeneficiaryClient, RawCurrencyCloudBeneficiaryClient


OMIT = typing.cast(typing.Any, ...)


class CurrencyCloudBeneficiaryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCurrencyCloudBeneficiaryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCurrencyCloudBeneficiaryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCurrencyCloudBeneficiaryClient
        """
        return self._raw_client

    def list_all_currency_cloud_beneficiary_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CurrencyCloudBeneficiaryListing]:
        """
        Endpoint to manage CurrencyCloud beneficiaries.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CurrencyCloudBeneficiaryListing]
            Endpoint to manage CurrencyCloud beneficiaries.

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
        client.currency_cloud_beneficiary.list_all_currency_cloud_beneficiary_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_currency_cloud_beneficiary_for_user(
            user_id, request_options=request_options
        )
        return _response.data

    def create_currency_cloud_beneficiary_for_user(
        self,
        user_id: int,
        *,
        all_field: typing.Sequence[str],
        country: str,
        currency: str,
        legal_entity_type: str,
        name: str,
        payment_type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CurrencyCloudBeneficiaryCreate:
        """
        Endpoint to manage CurrencyCloud beneficiaries.

        Parameters
        ----------
        user_id : int


        all_field : typing.Sequence[str]
            All fields that were required by CurrencyCloud. Obtained through the CurrencyCloudBeneficiaryRequirement listing.

        country : str
            The country of the beneficiary.

        currency : str
            The currency of the beneficiary.

        legal_entity_type : str
            The legal entity type of the beneficiary.

        name : str
            The name of the beneficiary.

        payment_type : str
            The payment type this requirement is for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrencyCloudBeneficiaryCreate
            Endpoint to manage CurrencyCloud beneficiaries.

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
        client.currency_cloud_beneficiary.create_currency_cloud_beneficiary_for_user(
            user_id=1,
            all_field=["all_field"],
            country="country",
            currency="currency",
            legal_entity_type="legal_entity_type",
            name="name",
            payment_type="payment_type",
        )
        """
        _response = self._raw_client.create_currency_cloud_beneficiary_for_user(
            user_id,
            all_field=all_field,
            country=country,
            currency=currency,
            legal_entity_type=legal_entity_type,
            name=name,
            payment_type=payment_type,
            request_options=request_options,
        )
        return _response.data

    def read_currency_cloud_beneficiary_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CurrencyCloudBeneficiaryRead:
        """
        Endpoint to manage CurrencyCloud beneficiaries.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrencyCloudBeneficiaryRead
            Endpoint to manage CurrencyCloud beneficiaries.

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
        client.currency_cloud_beneficiary.read_currency_cloud_beneficiary_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_currency_cloud_beneficiary_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncCurrencyCloudBeneficiaryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCurrencyCloudBeneficiaryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCurrencyCloudBeneficiaryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCurrencyCloudBeneficiaryClient
        """
        return self._raw_client

    async def list_all_currency_cloud_beneficiary_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CurrencyCloudBeneficiaryListing]:
        """
        Endpoint to manage CurrencyCloud beneficiaries.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CurrencyCloudBeneficiaryListing]
            Endpoint to manage CurrencyCloud beneficiaries.

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
            await client.currency_cloud_beneficiary.list_all_currency_cloud_beneficiary_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_currency_cloud_beneficiary_for_user(
            user_id, request_options=request_options
        )
        return _response.data

    async def create_currency_cloud_beneficiary_for_user(
        self,
        user_id: int,
        *,
        all_field: typing.Sequence[str],
        country: str,
        currency: str,
        legal_entity_type: str,
        name: str,
        payment_type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CurrencyCloudBeneficiaryCreate:
        """
        Endpoint to manage CurrencyCloud beneficiaries.

        Parameters
        ----------
        user_id : int


        all_field : typing.Sequence[str]
            All fields that were required by CurrencyCloud. Obtained through the CurrencyCloudBeneficiaryRequirement listing.

        country : str
            The country of the beneficiary.

        currency : str
            The currency of the beneficiary.

        legal_entity_type : str
            The legal entity type of the beneficiary.

        name : str
            The name of the beneficiary.

        payment_type : str
            The payment type this requirement is for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrencyCloudBeneficiaryCreate
            Endpoint to manage CurrencyCloud beneficiaries.

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
            await client.currency_cloud_beneficiary.create_currency_cloud_beneficiary_for_user(
                user_id=1,
                all_field=["all_field"],
                country="country",
                currency="currency",
                legal_entity_type="legal_entity_type",
                name="name",
                payment_type="payment_type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_currency_cloud_beneficiary_for_user(
            user_id,
            all_field=all_field,
            country=country,
            currency=currency,
            legal_entity_type=legal_entity_type,
            name=name,
            payment_type=payment_type,
            request_options=request_options,
        )
        return _response.data

    async def read_currency_cloud_beneficiary_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CurrencyCloudBeneficiaryRead:
        """
        Endpoint to manage CurrencyCloud beneficiaries.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrencyCloudBeneficiaryRead
            Endpoint to manage CurrencyCloud beneficiaries.

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
            await client.currency_cloud_beneficiary.read_currency_cloud_beneficiary_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_currency_cloud_beneficiary_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data
