

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.amount import Amount
from ..types.monetary_account_bank_create import MonetaryAccountBankCreate
from ..types.monetary_account_bank_listing import MonetaryAccountBankListing
from ..types.monetary_account_bank_read import MonetaryAccountBankRead
from ..types.monetary_account_bank_update import MonetaryAccountBankUpdate
from ..types.monetary_account_setting import MonetaryAccountSetting
from .raw_client import AsyncRawMonetaryAccountBankClient, RawMonetaryAccountBankClient


OMIT = typing.cast(typing.Any, ...)


class MonetaryAccountBankClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMonetaryAccountBankClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMonetaryAccountBankClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMonetaryAccountBankClient
        """
        return self._raw_client

    def list_all_monetary_account_bank_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[MonetaryAccountBankListing]:
        """
        Gets a listing of all MonetaryAccountBanks of a given user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MonetaryAccountBankListing]
            With MonetaryAccountBank you can create a new bank account, retrieve information regarding your existing MonetaryAccountBanks and update specific fields of an existing MonetaryAccountBank. Examples of fields that can be updated are the description, the daily limit and the avatar of the account.<br/><br/>Notification filters can be set on a monetary account level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.

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
        client.monetary_account_bank.list_all_monetary_account_bank_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_monetary_account_bank_for_user(user_id, request_options=request_options)
        return _response.data

    def create_monetary_account_bank_for_user(
        self,
        user_id: int,
        *,
        currency: str,
        avatar_uuid: typing.Optional[str] = OMIT,
        country_iban: typing.Optional[str] = OMIT,
        daily_limit: typing.Optional[Amount] = OMIT,
        description: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        reason_description: typing.Optional[str] = OMIT,
        setting: typing.Optional[MonetaryAccountSetting] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MonetaryAccountBankCreate:
        """
        Create new MonetaryAccountBank.

        Parameters
        ----------
        user_id : int


        currency : str
            The currency of the MonetaryAccountBank as an ISO 4217 formatted currency code.

        avatar_uuid : typing.Optional[str]
            The UUID of the Avatar of the MonetaryAccountBank.

        country_iban : typing.Optional[str]
            The country of the monetary account IBAN.

        daily_limit : typing.Optional[Amount]
            The daily spending limit Amount of the MonetaryAccountBank. Defaults to 1000 EUR. Currency must match the MonetaryAccountBank's currency. Limited to 10000 EUR.

        description : typing.Optional[str]
            The description of the MonetaryAccountBank. Defaults to 'bunq account'.

        display_name : typing.Optional[str]
            The legal name of the user / company using this monetary account.

        reason : typing.Optional[str]
            The reason for voluntarily cancelling (closing) the MonetaryAccountBank, can only be OTHER. Should only be specified if updating the status to CANCELLED.

        reason_description : typing.Optional[str]
            The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountBank. Can be any user provided message. Should only be specified if updating the status to CANCELLED.

        setting : typing.Optional[MonetaryAccountSetting]
            The settings of the MonetaryAccountBank.

        status : typing.Optional[str]
            The status of the MonetaryAccountBank. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountBank. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        sub_status : typing.Optional[str]
            The sub-status of the MonetaryAccountBank providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonetaryAccountBankCreate
            With MonetaryAccountBank you can create a new bank account, retrieve information regarding your existing MonetaryAccountBanks and update specific fields of an existing MonetaryAccountBank. Examples of fields that can be updated are the description, the daily limit and the avatar of the account.<br/><br/>Notification filters can be set on a monetary account level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.

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
        client.monetary_account_bank.create_monetary_account_bank_for_user(
            user_id=1,
            currency="currency",
        )
        """
        _response = self._raw_client.create_monetary_account_bank_for_user(
            user_id,
            currency=currency,
            avatar_uuid=avatar_uuid,
            country_iban=country_iban,
            daily_limit=daily_limit,
            description=description,
            display_name=display_name,
            reason=reason,
            reason_description=reason_description,
            setting=setting,
            status=status,
            sub_status=sub_status,
            request_options=request_options,
        )
        return _response.data

    def read_monetary_account_bank_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MonetaryAccountBankRead:
        """
        Get a specific MonetaryAccountBank.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonetaryAccountBankRead
            With MonetaryAccountBank you can create a new bank account, retrieve information regarding your existing MonetaryAccountBanks and update specific fields of an existing MonetaryAccountBank. Examples of fields that can be updated are the description, the daily limit and the avatar of the account.<br/><br/>Notification filters can be set on a monetary account level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.

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
        client.monetary_account_bank.read_monetary_account_bank_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_monetary_account_bank_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data

    def update_monetary_account_bank_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        currency: str,
        avatar_uuid: typing.Optional[str] = OMIT,
        country_iban: typing.Optional[str] = OMIT,
        daily_limit: typing.Optional[Amount] = OMIT,
        description: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        reason_description: typing.Optional[str] = OMIT,
        setting: typing.Optional[MonetaryAccountSetting] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MonetaryAccountBankUpdate:
        """
        Update a specific existing MonetaryAccountBank.

        Parameters
        ----------
        user_id : int


        item_id : int


        currency : str
            The currency of the MonetaryAccountBank as an ISO 4217 formatted currency code.

        avatar_uuid : typing.Optional[str]
            The UUID of the Avatar of the MonetaryAccountBank.

        country_iban : typing.Optional[str]
            The country of the monetary account IBAN.

        daily_limit : typing.Optional[Amount]
            The daily spending limit Amount of the MonetaryAccountBank. Defaults to 1000 EUR. Currency must match the MonetaryAccountBank's currency. Limited to 10000 EUR.

        description : typing.Optional[str]
            The description of the MonetaryAccountBank. Defaults to 'bunq account'.

        display_name : typing.Optional[str]
            The legal name of the user / company using this monetary account.

        reason : typing.Optional[str]
            The reason for voluntarily cancelling (closing) the MonetaryAccountBank, can only be OTHER. Should only be specified if updating the status to CANCELLED.

        reason_description : typing.Optional[str]
            The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountBank. Can be any user provided message. Should only be specified if updating the status to CANCELLED.

        setting : typing.Optional[MonetaryAccountSetting]
            The settings of the MonetaryAccountBank.

        status : typing.Optional[str]
            The status of the MonetaryAccountBank. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountBank. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        sub_status : typing.Optional[str]
            The sub-status of the MonetaryAccountBank providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonetaryAccountBankUpdate
            With MonetaryAccountBank you can create a new bank account, retrieve information regarding your existing MonetaryAccountBanks and update specific fields of an existing MonetaryAccountBank. Examples of fields that can be updated are the description, the daily limit and the avatar of the account.<br/><br/>Notification filters can be set on a monetary account level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.

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
        client.monetary_account_bank.update_monetary_account_bank_for_user(
            user_id=1,
            item_id=1,
            currency="currency",
        )
        """
        _response = self._raw_client.update_monetary_account_bank_for_user(
            user_id,
            item_id,
            currency=currency,
            avatar_uuid=avatar_uuid,
            country_iban=country_iban,
            daily_limit=daily_limit,
            description=description,
            display_name=display_name,
            reason=reason,
            reason_description=reason_description,
            setting=setting,
            status=status,
            sub_status=sub_status,
            request_options=request_options,
        )
        return _response.data


class AsyncMonetaryAccountBankClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMonetaryAccountBankClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMonetaryAccountBankClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMonetaryAccountBankClient
        """
        return self._raw_client

    async def list_all_monetary_account_bank_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[MonetaryAccountBankListing]:
        """
        Gets a listing of all MonetaryAccountBanks of a given user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MonetaryAccountBankListing]
            With MonetaryAccountBank you can create a new bank account, retrieve information regarding your existing MonetaryAccountBanks and update specific fields of an existing MonetaryAccountBank. Examples of fields that can be updated are the description, the daily limit and the avatar of the account.<br/><br/>Notification filters can be set on a monetary account level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.

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
            await client.monetary_account_bank.list_all_monetary_account_bank_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_monetary_account_bank_for_user(
            user_id, request_options=request_options
        )
        return _response.data

    async def create_monetary_account_bank_for_user(
        self,
        user_id: int,
        *,
        currency: str,
        avatar_uuid: typing.Optional[str] = OMIT,
        country_iban: typing.Optional[str] = OMIT,
        daily_limit: typing.Optional[Amount] = OMIT,
        description: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        reason_description: typing.Optional[str] = OMIT,
        setting: typing.Optional[MonetaryAccountSetting] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MonetaryAccountBankCreate:
        """
        Create new MonetaryAccountBank.

        Parameters
        ----------
        user_id : int


        currency : str
            The currency of the MonetaryAccountBank as an ISO 4217 formatted currency code.

        avatar_uuid : typing.Optional[str]
            The UUID of the Avatar of the MonetaryAccountBank.

        country_iban : typing.Optional[str]
            The country of the monetary account IBAN.

        daily_limit : typing.Optional[Amount]
            The daily spending limit Amount of the MonetaryAccountBank. Defaults to 1000 EUR. Currency must match the MonetaryAccountBank's currency. Limited to 10000 EUR.

        description : typing.Optional[str]
            The description of the MonetaryAccountBank. Defaults to 'bunq account'.

        display_name : typing.Optional[str]
            The legal name of the user / company using this monetary account.

        reason : typing.Optional[str]
            The reason for voluntarily cancelling (closing) the MonetaryAccountBank, can only be OTHER. Should only be specified if updating the status to CANCELLED.

        reason_description : typing.Optional[str]
            The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountBank. Can be any user provided message. Should only be specified if updating the status to CANCELLED.

        setting : typing.Optional[MonetaryAccountSetting]
            The settings of the MonetaryAccountBank.

        status : typing.Optional[str]
            The status of the MonetaryAccountBank. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountBank. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        sub_status : typing.Optional[str]
            The sub-status of the MonetaryAccountBank providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonetaryAccountBankCreate
            With MonetaryAccountBank you can create a new bank account, retrieve information regarding your existing MonetaryAccountBanks and update specific fields of an existing MonetaryAccountBank. Examples of fields that can be updated are the description, the daily limit and the avatar of the account.<br/><br/>Notification filters can be set on a monetary account level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.

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
            await client.monetary_account_bank.create_monetary_account_bank_for_user(
                user_id=1,
                currency="currency",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_monetary_account_bank_for_user(
            user_id,
            currency=currency,
            avatar_uuid=avatar_uuid,
            country_iban=country_iban,
            daily_limit=daily_limit,
            description=description,
            display_name=display_name,
            reason=reason,
            reason_description=reason_description,
            setting=setting,
            status=status,
            sub_status=sub_status,
            request_options=request_options,
        )
        return _response.data

    async def read_monetary_account_bank_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MonetaryAccountBankRead:
        """
        Get a specific MonetaryAccountBank.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonetaryAccountBankRead
            With MonetaryAccountBank you can create a new bank account, retrieve information regarding your existing MonetaryAccountBanks and update specific fields of an existing MonetaryAccountBank. Examples of fields that can be updated are the description, the daily limit and the avatar of the account.<br/><br/>Notification filters can be set on a monetary account level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.

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
            await client.monetary_account_bank.read_monetary_account_bank_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_monetary_account_bank_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_monetary_account_bank_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        currency: str,
        avatar_uuid: typing.Optional[str] = OMIT,
        country_iban: typing.Optional[str] = OMIT,
        daily_limit: typing.Optional[Amount] = OMIT,
        description: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        reason_description: typing.Optional[str] = OMIT,
        setting: typing.Optional[MonetaryAccountSetting] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MonetaryAccountBankUpdate:
        """
        Update a specific existing MonetaryAccountBank.

        Parameters
        ----------
        user_id : int


        item_id : int


        currency : str
            The currency of the MonetaryAccountBank as an ISO 4217 formatted currency code.

        avatar_uuid : typing.Optional[str]
            The UUID of the Avatar of the MonetaryAccountBank.

        country_iban : typing.Optional[str]
            The country of the monetary account IBAN.

        daily_limit : typing.Optional[Amount]
            The daily spending limit Amount of the MonetaryAccountBank. Defaults to 1000 EUR. Currency must match the MonetaryAccountBank's currency. Limited to 10000 EUR.

        description : typing.Optional[str]
            The description of the MonetaryAccountBank. Defaults to 'bunq account'.

        display_name : typing.Optional[str]
            The legal name of the user / company using this monetary account.

        reason : typing.Optional[str]
            The reason for voluntarily cancelling (closing) the MonetaryAccountBank, can only be OTHER. Should only be specified if updating the status to CANCELLED.

        reason_description : typing.Optional[str]
            The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountBank. Can be any user provided message. Should only be specified if updating the status to CANCELLED.

        setting : typing.Optional[MonetaryAccountSetting]
            The settings of the MonetaryAccountBank.

        status : typing.Optional[str]
            The status of the MonetaryAccountBank. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountBank. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        sub_status : typing.Optional[str]
            The sub-status of the MonetaryAccountBank providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonetaryAccountBankUpdate
            With MonetaryAccountBank you can create a new bank account, retrieve information regarding your existing MonetaryAccountBanks and update specific fields of an existing MonetaryAccountBank. Examples of fields that can be updated are the description, the daily limit and the avatar of the account.<br/><br/>Notification filters can be set on a monetary account level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.

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
            await client.monetary_account_bank.update_monetary_account_bank_for_user(
                user_id=1,
                item_id=1,
                currency="currency",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_monetary_account_bank_for_user(
            user_id,
            item_id,
            currency=currency,
            avatar_uuid=avatar_uuid,
            country_iban=country_iban,
            daily_limit=daily_limit,
            description=description,
            display_name=display_name,
            reason=reason,
            reason_description=reason_description,
            setting=setting,
            status=status,
            sub_status=sub_status,
            request_options=request_options,
        )
        return _response.data
