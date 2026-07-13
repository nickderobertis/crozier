

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.address import Address
from ..types.amount import Amount
from ..types.avatar import Avatar
from ..types.billing_contract_subscription import BillingContractSubscription
from ..types.customer import Customer
from ..types.customer_limit import CustomerLimit
from ..types.label_user import LabelUser
from ..types.notification_filter import NotificationFilter
from ..types.pointer import Pointer
from ..types.relation_user import RelationUser
from ..types.tax_resident import TaxResident
from ..types.ubo import Ubo
from ..types.user_company_read import UserCompanyRead
from ..types.user_company_update import UserCompanyUpdate
from .raw_client import AsyncRawUserCompanyClient, RawUserCompanyClient


OMIT = typing.cast(typing.Any, ...)


class UserCompanyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserCompanyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserCompanyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserCompanyClient
        """
        return self._raw_client

    def read_user_company(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserCompanyRead:
        """
        Get a specific company.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserCompanyRead
            With UserCompany you can retrieve information regarding the authenticated UserCompany and update specific fields.<br/><br/>Notification filters can be set on a UserCompany level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.

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
        client.user_company.read_user_company(
            item_id=1,
        )
        """
        _response = self._raw_client.read_user_company(item_id, request_options=request_options)
        return _response.data

    def update_user_company(
        self,
        item_id: int,
        *,
        address_main: typing.Optional[Address] = OMIT,
        address_postal: typing.Optional[Address] = OMIT,
        alias: typing.Optional[typing.Sequence[Pointer]] = OMIT,
        avatar: typing.Optional[Avatar] = OMIT,
        avatar_uuid: typing.Optional[str] = OMIT,
        billing_contract: typing.Optional[typing.Sequence[BillingContractSubscription]] = OMIT,
        chamber_of_commerce_number: typing.Optional[str] = OMIT,
        counter_bank_iban: typing.Optional[str] = OMIT,
        country: typing.Optional[str] = OMIT,
        created: typing.Optional[str] = OMIT,
        customer: typing.Optional[Customer] = OMIT,
        customer_limit: typing.Optional[CustomerLimit] = OMIT,
        daily_limit_without_confirmation_login: typing.Optional[Amount] = OMIT,
        deny_reason: typing.Optional[str] = OMIT,
        directors: typing.Optional[typing.Sequence[LabelUser]] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        language: typing.Optional[str] = OMIT,
        legal_form: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        notification_filters: typing.Optional[typing.Sequence[NotificationFilter]] = OMIT,
        public_nick_name: typing.Optional[str] = OMIT,
        public_uuid: typing.Optional[str] = OMIT,
        region: typing.Optional[str] = OMIT,
        relations: typing.Optional[typing.Sequence[RelationUser]] = OMIT,
        sector_of_industry: typing.Optional[str] = OMIT,
        session_timeout: typing.Optional[int] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        tax_resident: typing.Optional[typing.Sequence[TaxResident]] = OMIT,
        type_of_business_entity: typing.Optional[str] = OMIT,
        ubo: typing.Optional[typing.Sequence[Ubo]] = OMIT,
        updated: typing.Optional[str] = OMIT,
        version_terms_of_service: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserCompanyUpdate:
        """
        Modify a specific company's data.

        Parameters
        ----------
        item_id : int


        address_main : typing.Optional[Address]
            The company's main address.

        address_postal : typing.Optional[Address]
            The company's postal address.

        alias : typing.Optional[typing.Sequence[Pointer]]
            The aliases of the account.

        avatar : typing.Optional[Avatar]
            The company's avatar.

        avatar_uuid : typing.Optional[str]
            The public UUID of the company's avatar.

        billing_contract : typing.Optional[typing.Sequence[BillingContractSubscription]]
            The subscription of the company.

        chamber_of_commerce_number : typing.Optional[str]
            The company's chamber of commerce number.

        counter_bank_iban : typing.Optional[str]
            The company's other bank account IBAN, through which we verify it.

        country : typing.Optional[str]
            The country as an ISO 3166-1 alpha-2 country code.

        created : typing.Optional[str]
            The timestamp of the company object's creation.

        customer : typing.Optional[Customer]
            The customer profile of the company.

        customer_limit : typing.Optional[CustomerLimit]
            The customer limits of the company.

        daily_limit_without_confirmation_login : typing.Optional[Amount]
            The amount the company can pay in the session without asking for credentials.

        deny_reason : typing.Optional[str]
            The user deny reason.

        directors : typing.Optional[typing.Sequence[LabelUser]]
            The existing bunq aliases for the company's directors.

        display_name : typing.Optional[str]
            The company's display name.

        id : typing.Optional[int]
            The id of the modified company.

        language : typing.Optional[str]
            The person's preferred language. Formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, seperated by an underscore.

        legal_form : typing.Optional[str]
            The company's legal form.

        name : typing.Optional[str]
            The company name.

        notification_filters : typing.Optional[typing.Sequence[NotificationFilter]]
            The types of notifications that will result in a push notification or URL callback for this UserCompany.

        public_nick_name : typing.Optional[str]
            The company's public nick name.

        public_uuid : typing.Optional[str]
            The company's public UUID.

        region : typing.Optional[str]
            The person's preferred region. Formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, seperated by an underscore.

        relations : typing.Optional[typing.Sequence[RelationUser]]
            The relations for this user.

        sector_of_industry : typing.Optional[str]
            The sector of industry.

        session_timeout : typing.Optional[int]
            The setting for the session timeout of the company in seconds.

        status : typing.Optional[str]
            The user status. Can be: ACTIVE, SIGNUP, RECOVERY.

        sub_status : typing.Optional[str]
            The user sub-status. Can be: NONE, FACE_RESET, APPROVAL, APPROVAL_DIRECTOR, APPROVAL_PARENT, APPROVAL_SUPPORT, COUNTER_IBAN, IDEAL or SUBMIT.

        tax_resident : typing.Optional[typing.Sequence[TaxResident]]
            The user's tax residence numbers for different countries.

        type_of_business_entity : typing.Optional[str]
            The type of business entity.

        ubo : typing.Optional[typing.Sequence[Ubo]]
            The names of the company's ultimate beneficiary owners. Minimum zero, maximum four.

        updated : typing.Optional[str]
            The timestamp of the company object's last update.

        version_terms_of_service : typing.Optional[str]
            The version of the terms of service accepted by the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserCompanyUpdate
            With UserCompany you can retrieve information regarding the authenticated UserCompany and update specific fields.<br/><br/>Notification filters can be set on a UserCompany level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.

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
        client.user_company.update_user_company(
            item_id=1,
        )
        """
        _response = self._raw_client.update_user_company(
            item_id,
            address_main=address_main,
            address_postal=address_postal,
            alias=alias,
            avatar=avatar,
            avatar_uuid=avatar_uuid,
            billing_contract=billing_contract,
            chamber_of_commerce_number=chamber_of_commerce_number,
            counter_bank_iban=counter_bank_iban,
            country=country,
            created=created,
            customer=customer,
            customer_limit=customer_limit,
            daily_limit_without_confirmation_login=daily_limit_without_confirmation_login,
            deny_reason=deny_reason,
            directors=directors,
            display_name=display_name,
            id=id,
            language=language,
            legal_form=legal_form,
            name=name,
            notification_filters=notification_filters,
            public_nick_name=public_nick_name,
            public_uuid=public_uuid,
            region=region,
            relations=relations,
            sector_of_industry=sector_of_industry,
            session_timeout=session_timeout,
            status=status,
            sub_status=sub_status,
            tax_resident=tax_resident,
            type_of_business_entity=type_of_business_entity,
            ubo=ubo,
            updated=updated,
            version_terms_of_service=version_terms_of_service,
            request_options=request_options,
        )
        return _response.data


class AsyncUserCompanyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserCompanyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserCompanyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserCompanyClient
        """
        return self._raw_client

    async def read_user_company(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserCompanyRead:
        """
        Get a specific company.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserCompanyRead
            With UserCompany you can retrieve information regarding the authenticated UserCompany and update specific fields.<br/><br/>Notification filters can be set on a UserCompany level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.

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
            await client.user_company.read_user_company(
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_user_company(item_id, request_options=request_options)
        return _response.data

    async def update_user_company(
        self,
        item_id: int,
        *,
        address_main: typing.Optional[Address] = OMIT,
        address_postal: typing.Optional[Address] = OMIT,
        alias: typing.Optional[typing.Sequence[Pointer]] = OMIT,
        avatar: typing.Optional[Avatar] = OMIT,
        avatar_uuid: typing.Optional[str] = OMIT,
        billing_contract: typing.Optional[typing.Sequence[BillingContractSubscription]] = OMIT,
        chamber_of_commerce_number: typing.Optional[str] = OMIT,
        counter_bank_iban: typing.Optional[str] = OMIT,
        country: typing.Optional[str] = OMIT,
        created: typing.Optional[str] = OMIT,
        customer: typing.Optional[Customer] = OMIT,
        customer_limit: typing.Optional[CustomerLimit] = OMIT,
        daily_limit_without_confirmation_login: typing.Optional[Amount] = OMIT,
        deny_reason: typing.Optional[str] = OMIT,
        directors: typing.Optional[typing.Sequence[LabelUser]] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        language: typing.Optional[str] = OMIT,
        legal_form: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        notification_filters: typing.Optional[typing.Sequence[NotificationFilter]] = OMIT,
        public_nick_name: typing.Optional[str] = OMIT,
        public_uuid: typing.Optional[str] = OMIT,
        region: typing.Optional[str] = OMIT,
        relations: typing.Optional[typing.Sequence[RelationUser]] = OMIT,
        sector_of_industry: typing.Optional[str] = OMIT,
        session_timeout: typing.Optional[int] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        tax_resident: typing.Optional[typing.Sequence[TaxResident]] = OMIT,
        type_of_business_entity: typing.Optional[str] = OMIT,
        ubo: typing.Optional[typing.Sequence[Ubo]] = OMIT,
        updated: typing.Optional[str] = OMIT,
        version_terms_of_service: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserCompanyUpdate:
        """
        Modify a specific company's data.

        Parameters
        ----------
        item_id : int


        address_main : typing.Optional[Address]
            The company's main address.

        address_postal : typing.Optional[Address]
            The company's postal address.

        alias : typing.Optional[typing.Sequence[Pointer]]
            The aliases of the account.

        avatar : typing.Optional[Avatar]
            The company's avatar.

        avatar_uuid : typing.Optional[str]
            The public UUID of the company's avatar.

        billing_contract : typing.Optional[typing.Sequence[BillingContractSubscription]]
            The subscription of the company.

        chamber_of_commerce_number : typing.Optional[str]
            The company's chamber of commerce number.

        counter_bank_iban : typing.Optional[str]
            The company's other bank account IBAN, through which we verify it.

        country : typing.Optional[str]
            The country as an ISO 3166-1 alpha-2 country code.

        created : typing.Optional[str]
            The timestamp of the company object's creation.

        customer : typing.Optional[Customer]
            The customer profile of the company.

        customer_limit : typing.Optional[CustomerLimit]
            The customer limits of the company.

        daily_limit_without_confirmation_login : typing.Optional[Amount]
            The amount the company can pay in the session without asking for credentials.

        deny_reason : typing.Optional[str]
            The user deny reason.

        directors : typing.Optional[typing.Sequence[LabelUser]]
            The existing bunq aliases for the company's directors.

        display_name : typing.Optional[str]
            The company's display name.

        id : typing.Optional[int]
            The id of the modified company.

        language : typing.Optional[str]
            The person's preferred language. Formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, seperated by an underscore.

        legal_form : typing.Optional[str]
            The company's legal form.

        name : typing.Optional[str]
            The company name.

        notification_filters : typing.Optional[typing.Sequence[NotificationFilter]]
            The types of notifications that will result in a push notification or URL callback for this UserCompany.

        public_nick_name : typing.Optional[str]
            The company's public nick name.

        public_uuid : typing.Optional[str]
            The company's public UUID.

        region : typing.Optional[str]
            The person's preferred region. Formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, seperated by an underscore.

        relations : typing.Optional[typing.Sequence[RelationUser]]
            The relations for this user.

        sector_of_industry : typing.Optional[str]
            The sector of industry.

        session_timeout : typing.Optional[int]
            The setting for the session timeout of the company in seconds.

        status : typing.Optional[str]
            The user status. Can be: ACTIVE, SIGNUP, RECOVERY.

        sub_status : typing.Optional[str]
            The user sub-status. Can be: NONE, FACE_RESET, APPROVAL, APPROVAL_DIRECTOR, APPROVAL_PARENT, APPROVAL_SUPPORT, COUNTER_IBAN, IDEAL or SUBMIT.

        tax_resident : typing.Optional[typing.Sequence[TaxResident]]
            The user's tax residence numbers for different countries.

        type_of_business_entity : typing.Optional[str]
            The type of business entity.

        ubo : typing.Optional[typing.Sequence[Ubo]]
            The names of the company's ultimate beneficiary owners. Minimum zero, maximum four.

        updated : typing.Optional[str]
            The timestamp of the company object's last update.

        version_terms_of_service : typing.Optional[str]
            The version of the terms of service accepted by the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserCompanyUpdate
            With UserCompany you can retrieve information regarding the authenticated UserCompany and update specific fields.<br/><br/>Notification filters can be set on a UserCompany level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.

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
            await client.user_company.update_user_company(
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_user_company(
            item_id,
            address_main=address_main,
            address_postal=address_postal,
            alias=alias,
            avatar=avatar,
            avatar_uuid=avatar_uuid,
            billing_contract=billing_contract,
            chamber_of_commerce_number=chamber_of_commerce_number,
            counter_bank_iban=counter_bank_iban,
            country=country,
            created=created,
            customer=customer,
            customer_limit=customer_limit,
            daily_limit_without_confirmation_login=daily_limit_without_confirmation_login,
            deny_reason=deny_reason,
            directors=directors,
            display_name=display_name,
            id=id,
            language=language,
            legal_form=legal_form,
            name=name,
            notification_filters=notification_filters,
            public_nick_name=public_nick_name,
            public_uuid=public_uuid,
            region=region,
            relations=relations,
            sector_of_industry=sector_of_industry,
            session_timeout=session_timeout,
            status=status,
            sub_status=sub_status,
            tax_resident=tax_resident,
            type_of_business_entity=type_of_business_entity,
            ubo=ubo,
            updated=updated,
            version_terms_of_service=version_terms_of_service,
            request_options=request_options,
        )
        return _response.data
