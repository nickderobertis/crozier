

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.address import Address
from ..types.company_create import CompanyCreate
from ..types.company_listing import CompanyListing
from ..types.company_read import CompanyRead
from ..types.company_update import CompanyUpdate
from ..types.company_vat_number import CompanyVatNumber
from ..types.ubo import Ubo
from .raw_client import AsyncRawCompanyClient, RawCompanyClient


OMIT = typing.cast(typing.Any, ...)


class CompanyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCompanyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCompanyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCompanyClient
        """
        return self._raw_client

    def list_all_company_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CompanyListing]:
        """
        Create and manage companies.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CompanyListing]
            Create and manage companies.

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
        client.company.list_all_company_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_company_for_user(user_id, request_options=request_options)
        return _response.data

    def create_company_for_user(
        self,
        user_id: int,
        *,
        address_main: Address,
        address_postal: Address,
        country: str,
        legal_form: str,
        name: str,
        subscription_type: str,
        avatar_uuid: typing.Optional[str] = OMIT,
        chamber_of_commerce_number: typing.Optional[str] = OMIT,
        signup_track_type: typing.Optional[str] = OMIT,
        ubo: typing.Optional[typing.Sequence[Ubo]] = OMIT,
        vat_number: typing.Optional[CompanyVatNumber] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompanyCreate:
        """
        Create and manage companies.

        Parameters
        ----------
        user_id : int


        address_main : Address
            The company's main address.

        address_postal : Address
            The company's postal address.

        country : str
            The country where the company is registered.

        legal_form : str
            The company's legal form.

        name : str
            The company name.

        subscription_type : str
            The subscription type for the company.

        avatar_uuid : typing.Optional[str]
            The public UUID of the company's avatar.

        chamber_of_commerce_number : typing.Optional[str]
            The company's chamber of commerce number.

        signup_track_type : typing.Optional[str]
            The type of signup track the user is following.

        ubo : typing.Optional[typing.Sequence[Ubo]]
            The names and birth dates of the company's ultimate beneficiary owners. Minimum zero, maximum four.

        vat_number : typing.Optional[CompanyVatNumber]
            All the vat numbers of the company

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompanyCreate
            Create and manage companies.

        Examples
        --------
        from fern import Address, FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.company.create_company_for_user(
            user_id=1,
            address_main=Address(),
            address_postal=Address(),
            country="country",
            legal_form="legal_form",
            name="name",
            subscription_type="subscription_type",
        )
        """
        _response = self._raw_client.create_company_for_user(
            user_id,
            address_main=address_main,
            address_postal=address_postal,
            country=country,
            legal_form=legal_form,
            name=name,
            subscription_type=subscription_type,
            avatar_uuid=avatar_uuid,
            chamber_of_commerce_number=chamber_of_commerce_number,
            signup_track_type=signup_track_type,
            ubo=ubo,
            vat_number=vat_number,
            request_options=request_options,
        )
        return _response.data

    def read_company_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CompanyRead:
        """
        Create and manage companies.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompanyRead
            Create and manage companies.

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
        client.company.read_company_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_company_for_user(user_id, item_id, request_options=request_options)
        return _response.data

    def update_company_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        address_main: Address,
        address_postal: Address,
        country: str,
        legal_form: str,
        name: str,
        subscription_type: str,
        avatar_uuid: typing.Optional[str] = OMIT,
        chamber_of_commerce_number: typing.Optional[str] = OMIT,
        signup_track_type: typing.Optional[str] = OMIT,
        ubo: typing.Optional[typing.Sequence[Ubo]] = OMIT,
        vat_number: typing.Optional[CompanyVatNumber] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompanyUpdate:
        """
        Create and manage companies.

        Parameters
        ----------
        user_id : int


        item_id : int


        address_main : Address
            The company's main address.

        address_postal : Address
            The company's postal address.

        country : str
            The country where the company is registered.

        legal_form : str
            The company's legal form.

        name : str
            The company name.

        subscription_type : str
            The subscription type for the company.

        avatar_uuid : typing.Optional[str]
            The public UUID of the company's avatar.

        chamber_of_commerce_number : typing.Optional[str]
            The company's chamber of commerce number.

        signup_track_type : typing.Optional[str]
            The type of signup track the user is following.

        ubo : typing.Optional[typing.Sequence[Ubo]]
            The names and birth dates of the company's ultimate beneficiary owners. Minimum zero, maximum four.

        vat_number : typing.Optional[CompanyVatNumber]
            All the vat numbers of the company

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompanyUpdate
            Create and manage companies.

        Examples
        --------
        from fern import Address, FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.company.update_company_for_user(
            user_id=1,
            item_id=1,
            address_main=Address(),
            address_postal=Address(),
            country="country",
            legal_form="legal_form",
            name="name",
            subscription_type="subscription_type",
        )
        """
        _response = self._raw_client.update_company_for_user(
            user_id,
            item_id,
            address_main=address_main,
            address_postal=address_postal,
            country=country,
            legal_form=legal_form,
            name=name,
            subscription_type=subscription_type,
            avatar_uuid=avatar_uuid,
            chamber_of_commerce_number=chamber_of_commerce_number,
            signup_track_type=signup_track_type,
            ubo=ubo,
            vat_number=vat_number,
            request_options=request_options,
        )
        return _response.data


class AsyncCompanyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCompanyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCompanyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCompanyClient
        """
        return self._raw_client

    async def list_all_company_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CompanyListing]:
        """
        Create and manage companies.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CompanyListing]
            Create and manage companies.

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
            await client.company.list_all_company_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_company_for_user(user_id, request_options=request_options)
        return _response.data

    async def create_company_for_user(
        self,
        user_id: int,
        *,
        address_main: Address,
        address_postal: Address,
        country: str,
        legal_form: str,
        name: str,
        subscription_type: str,
        avatar_uuid: typing.Optional[str] = OMIT,
        chamber_of_commerce_number: typing.Optional[str] = OMIT,
        signup_track_type: typing.Optional[str] = OMIT,
        ubo: typing.Optional[typing.Sequence[Ubo]] = OMIT,
        vat_number: typing.Optional[CompanyVatNumber] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompanyCreate:
        """
        Create and manage companies.

        Parameters
        ----------
        user_id : int


        address_main : Address
            The company's main address.

        address_postal : Address
            The company's postal address.

        country : str
            The country where the company is registered.

        legal_form : str
            The company's legal form.

        name : str
            The company name.

        subscription_type : str
            The subscription type for the company.

        avatar_uuid : typing.Optional[str]
            The public UUID of the company's avatar.

        chamber_of_commerce_number : typing.Optional[str]
            The company's chamber of commerce number.

        signup_track_type : typing.Optional[str]
            The type of signup track the user is following.

        ubo : typing.Optional[typing.Sequence[Ubo]]
            The names and birth dates of the company's ultimate beneficiary owners. Minimum zero, maximum four.

        vat_number : typing.Optional[CompanyVatNumber]
            All the vat numbers of the company

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompanyCreate
            Create and manage companies.

        Examples
        --------
        import asyncio

        from fern import Address, AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.company.create_company_for_user(
                user_id=1,
                address_main=Address(),
                address_postal=Address(),
                country="country",
                legal_form="legal_form",
                name="name",
                subscription_type="subscription_type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_company_for_user(
            user_id,
            address_main=address_main,
            address_postal=address_postal,
            country=country,
            legal_form=legal_form,
            name=name,
            subscription_type=subscription_type,
            avatar_uuid=avatar_uuid,
            chamber_of_commerce_number=chamber_of_commerce_number,
            signup_track_type=signup_track_type,
            ubo=ubo,
            vat_number=vat_number,
            request_options=request_options,
        )
        return _response.data

    async def read_company_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CompanyRead:
        """
        Create and manage companies.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompanyRead
            Create and manage companies.

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
            await client.company.read_company_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_company_for_user(user_id, item_id, request_options=request_options)
        return _response.data

    async def update_company_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        address_main: Address,
        address_postal: Address,
        country: str,
        legal_form: str,
        name: str,
        subscription_type: str,
        avatar_uuid: typing.Optional[str] = OMIT,
        chamber_of_commerce_number: typing.Optional[str] = OMIT,
        signup_track_type: typing.Optional[str] = OMIT,
        ubo: typing.Optional[typing.Sequence[Ubo]] = OMIT,
        vat_number: typing.Optional[CompanyVatNumber] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompanyUpdate:
        """
        Create and manage companies.

        Parameters
        ----------
        user_id : int


        item_id : int


        address_main : Address
            The company's main address.

        address_postal : Address
            The company's postal address.

        country : str
            The country where the company is registered.

        legal_form : str
            The company's legal form.

        name : str
            The company name.

        subscription_type : str
            The subscription type for the company.

        avatar_uuid : typing.Optional[str]
            The public UUID of the company's avatar.

        chamber_of_commerce_number : typing.Optional[str]
            The company's chamber of commerce number.

        signup_track_type : typing.Optional[str]
            The type of signup track the user is following.

        ubo : typing.Optional[typing.Sequence[Ubo]]
            The names and birth dates of the company's ultimate beneficiary owners. Minimum zero, maximum four.

        vat_number : typing.Optional[CompanyVatNumber]
            All the vat numbers of the company

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompanyUpdate
            Create and manage companies.

        Examples
        --------
        import asyncio

        from fern import Address, AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.company.update_company_for_user(
                user_id=1,
                item_id=1,
                address_main=Address(),
                address_postal=Address(),
                country="country",
                legal_form="legal_form",
                name="name",
                subscription_type="subscription_type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_company_for_user(
            user_id,
            item_id,
            address_main=address_main,
            address_postal=address_postal,
            country=country,
            legal_form=legal_form,
            name=name,
            subscription_type=subscription_type,
            avatar_uuid=avatar_uuid,
            chamber_of_commerce_number=chamber_of_commerce_number,
            signup_track_type=signup_track_type,
            ubo=ubo,
            vat_number=vat_number,
            request_options=request_options,
        )
        return _response.data
