

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.amount import Amount
from ..types.co_owner import CoOwner
from ..types.monetary_account_savings_create import MonetaryAccountSavingsCreate
from ..types.monetary_account_savings_listing import MonetaryAccountSavingsListing
from ..types.monetary_account_savings_read import MonetaryAccountSavingsRead
from ..types.monetary_account_savings_update import MonetaryAccountSavingsUpdate
from ..types.monetary_account_setting import MonetaryAccountSetting
from .raw_client import AsyncRawMonetaryAccountSavingsClient, RawMonetaryAccountSavingsClient


OMIT = typing.cast(typing.Any, ...)


class MonetaryAccountSavingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMonetaryAccountSavingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMonetaryAccountSavingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMonetaryAccountSavingsClient
        """
        return self._raw_client

    def list_all_monetary_account_savings_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[MonetaryAccountSavingsListing]:
        """
        Gets a listing of all MonetaryAccountSavingss of a given user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MonetaryAccountSavingsListing]
            With MonetaryAccountSavings you can create a new savings account.

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
        client.monetary_account_savings.list_all_monetary_account_savings_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_monetary_account_savings_for_user(
            user_id, request_options=request_options
        )
        return _response.data

    def create_monetary_account_savings_for_user(
        self,
        user_id: int,
        *,
        currency: str,
        all_co_owner: typing.Optional[typing.Sequence[CoOwner]] = OMIT,
        avatar_uuid: typing.Optional[str] = OMIT,
        daily_limit: typing.Optional[Amount] = OMIT,
        description: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        reason_description: typing.Optional[str] = OMIT,
        savings_goal: typing.Optional[Amount] = OMIT,
        setting: typing.Optional[MonetaryAccountSetting] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MonetaryAccountSavingsCreate:
        """
        Create new MonetaryAccountSavings.

        Parameters
        ----------
        user_id : int


        currency : str
            The currency of the MonetaryAccountSavings as an ISO 4217 formatted currency code.

        all_co_owner : typing.Optional[typing.Sequence[CoOwner]]
            The users the account will be joint with.

        avatar_uuid : typing.Optional[str]
            The UUID of the Avatar of the MonetaryAccountSavings.

        daily_limit : typing.Optional[Amount]
            The daily spending limit Amount of the MonetaryAccountSavings. Defaults to 1000 EUR. Currency must match the MonetaryAccountSavings's currency. Limited to 10000 EUR.

        description : typing.Optional[str]
            The description of the MonetaryAccountSavings. Defaults to 'bunq account'.

        reason : typing.Optional[str]
            The reason for voluntarily cancelling (closing) the MonetaryAccountSavings, can only be OTHER. Should only be specified if updating the status to CANCELLED.

        reason_description : typing.Optional[str]
            The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountSavings. Can be any user provided message. Should only be specified if updating the status to CANCELLED.

        savings_goal : typing.Optional[Amount]
            The Savings Goal set for this MonetaryAccountSavings.

        setting : typing.Optional[MonetaryAccountSetting]
            The settings of the MonetaryAccountSavings.

        status : typing.Optional[str]
            The status of the MonetaryAccountSavings. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountSavings. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        sub_status : typing.Optional[str]
            The sub-status of the MonetaryAccountSavings providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonetaryAccountSavingsCreate
            With MonetaryAccountSavings you can create a new savings account.

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
        client.monetary_account_savings.create_monetary_account_savings_for_user(
            user_id=1,
            currency="currency",
        )
        """
        _response = self._raw_client.create_monetary_account_savings_for_user(
            user_id,
            currency=currency,
            all_co_owner=all_co_owner,
            avatar_uuid=avatar_uuid,
            daily_limit=daily_limit,
            description=description,
            reason=reason,
            reason_description=reason_description,
            savings_goal=savings_goal,
            setting=setting,
            status=status,
            sub_status=sub_status,
            request_options=request_options,
        )
        return _response.data

    def read_monetary_account_savings_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MonetaryAccountSavingsRead:
        """
        Get a specific MonetaryAccountSavings.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonetaryAccountSavingsRead
            With MonetaryAccountSavings you can create a new savings account.

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
        client.monetary_account_savings.read_monetary_account_savings_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_monetary_account_savings_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data

    def update_monetary_account_savings_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        currency: str,
        all_co_owner: typing.Optional[typing.Sequence[CoOwner]] = OMIT,
        avatar_uuid: typing.Optional[str] = OMIT,
        daily_limit: typing.Optional[Amount] = OMIT,
        description: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        reason_description: typing.Optional[str] = OMIT,
        savings_goal: typing.Optional[Amount] = OMIT,
        setting: typing.Optional[MonetaryAccountSetting] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MonetaryAccountSavingsUpdate:
        """
        Update a specific existing MonetaryAccountSavings.

        Parameters
        ----------
        user_id : int


        item_id : int


        currency : str
            The currency of the MonetaryAccountSavings as an ISO 4217 formatted currency code.

        all_co_owner : typing.Optional[typing.Sequence[CoOwner]]
            The users the account will be joint with.

        avatar_uuid : typing.Optional[str]
            The UUID of the Avatar of the MonetaryAccountSavings.

        daily_limit : typing.Optional[Amount]
            The daily spending limit Amount of the MonetaryAccountSavings. Defaults to 1000 EUR. Currency must match the MonetaryAccountSavings's currency. Limited to 10000 EUR.

        description : typing.Optional[str]
            The description of the MonetaryAccountSavings. Defaults to 'bunq account'.

        reason : typing.Optional[str]
            The reason for voluntarily cancelling (closing) the MonetaryAccountSavings, can only be OTHER. Should only be specified if updating the status to CANCELLED.

        reason_description : typing.Optional[str]
            The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountSavings. Can be any user provided message. Should only be specified if updating the status to CANCELLED.

        savings_goal : typing.Optional[Amount]
            The Savings Goal set for this MonetaryAccountSavings.

        setting : typing.Optional[MonetaryAccountSetting]
            The settings of the MonetaryAccountSavings.

        status : typing.Optional[str]
            The status of the MonetaryAccountSavings. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountSavings. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        sub_status : typing.Optional[str]
            The sub-status of the MonetaryAccountSavings providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonetaryAccountSavingsUpdate
            With MonetaryAccountSavings you can create a new savings account.

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
        client.monetary_account_savings.update_monetary_account_savings_for_user(
            user_id=1,
            item_id=1,
            currency="currency",
        )
        """
        _response = self._raw_client.update_monetary_account_savings_for_user(
            user_id,
            item_id,
            currency=currency,
            all_co_owner=all_co_owner,
            avatar_uuid=avatar_uuid,
            daily_limit=daily_limit,
            description=description,
            reason=reason,
            reason_description=reason_description,
            savings_goal=savings_goal,
            setting=setting,
            status=status,
            sub_status=sub_status,
            request_options=request_options,
        )
        return _response.data


class AsyncMonetaryAccountSavingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMonetaryAccountSavingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMonetaryAccountSavingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMonetaryAccountSavingsClient
        """
        return self._raw_client

    async def list_all_monetary_account_savings_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[MonetaryAccountSavingsListing]:
        """
        Gets a listing of all MonetaryAccountSavingss of a given user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MonetaryAccountSavingsListing]
            With MonetaryAccountSavings you can create a new savings account.

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
            await client.monetary_account_savings.list_all_monetary_account_savings_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_monetary_account_savings_for_user(
            user_id, request_options=request_options
        )
        return _response.data

    async def create_monetary_account_savings_for_user(
        self,
        user_id: int,
        *,
        currency: str,
        all_co_owner: typing.Optional[typing.Sequence[CoOwner]] = OMIT,
        avatar_uuid: typing.Optional[str] = OMIT,
        daily_limit: typing.Optional[Amount] = OMIT,
        description: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        reason_description: typing.Optional[str] = OMIT,
        savings_goal: typing.Optional[Amount] = OMIT,
        setting: typing.Optional[MonetaryAccountSetting] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MonetaryAccountSavingsCreate:
        """
        Create new MonetaryAccountSavings.

        Parameters
        ----------
        user_id : int


        currency : str
            The currency of the MonetaryAccountSavings as an ISO 4217 formatted currency code.

        all_co_owner : typing.Optional[typing.Sequence[CoOwner]]
            The users the account will be joint with.

        avatar_uuid : typing.Optional[str]
            The UUID of the Avatar of the MonetaryAccountSavings.

        daily_limit : typing.Optional[Amount]
            The daily spending limit Amount of the MonetaryAccountSavings. Defaults to 1000 EUR. Currency must match the MonetaryAccountSavings's currency. Limited to 10000 EUR.

        description : typing.Optional[str]
            The description of the MonetaryAccountSavings. Defaults to 'bunq account'.

        reason : typing.Optional[str]
            The reason for voluntarily cancelling (closing) the MonetaryAccountSavings, can only be OTHER. Should only be specified if updating the status to CANCELLED.

        reason_description : typing.Optional[str]
            The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountSavings. Can be any user provided message. Should only be specified if updating the status to CANCELLED.

        savings_goal : typing.Optional[Amount]
            The Savings Goal set for this MonetaryAccountSavings.

        setting : typing.Optional[MonetaryAccountSetting]
            The settings of the MonetaryAccountSavings.

        status : typing.Optional[str]
            The status of the MonetaryAccountSavings. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountSavings. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        sub_status : typing.Optional[str]
            The sub-status of the MonetaryAccountSavings providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonetaryAccountSavingsCreate
            With MonetaryAccountSavings you can create a new savings account.

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
            await client.monetary_account_savings.create_monetary_account_savings_for_user(
                user_id=1,
                currency="currency",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_monetary_account_savings_for_user(
            user_id,
            currency=currency,
            all_co_owner=all_co_owner,
            avatar_uuid=avatar_uuid,
            daily_limit=daily_limit,
            description=description,
            reason=reason,
            reason_description=reason_description,
            savings_goal=savings_goal,
            setting=setting,
            status=status,
            sub_status=sub_status,
            request_options=request_options,
        )
        return _response.data

    async def read_monetary_account_savings_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MonetaryAccountSavingsRead:
        """
        Get a specific MonetaryAccountSavings.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonetaryAccountSavingsRead
            With MonetaryAccountSavings you can create a new savings account.

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
            await client.monetary_account_savings.read_monetary_account_savings_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_monetary_account_savings_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_monetary_account_savings_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        currency: str,
        all_co_owner: typing.Optional[typing.Sequence[CoOwner]] = OMIT,
        avatar_uuid: typing.Optional[str] = OMIT,
        daily_limit: typing.Optional[Amount] = OMIT,
        description: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        reason_description: typing.Optional[str] = OMIT,
        savings_goal: typing.Optional[Amount] = OMIT,
        setting: typing.Optional[MonetaryAccountSetting] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MonetaryAccountSavingsUpdate:
        """
        Update a specific existing MonetaryAccountSavings.

        Parameters
        ----------
        user_id : int


        item_id : int


        currency : str
            The currency of the MonetaryAccountSavings as an ISO 4217 formatted currency code.

        all_co_owner : typing.Optional[typing.Sequence[CoOwner]]
            The users the account will be joint with.

        avatar_uuid : typing.Optional[str]
            The UUID of the Avatar of the MonetaryAccountSavings.

        daily_limit : typing.Optional[Amount]
            The daily spending limit Amount of the MonetaryAccountSavings. Defaults to 1000 EUR. Currency must match the MonetaryAccountSavings's currency. Limited to 10000 EUR.

        description : typing.Optional[str]
            The description of the MonetaryAccountSavings. Defaults to 'bunq account'.

        reason : typing.Optional[str]
            The reason for voluntarily cancelling (closing) the MonetaryAccountSavings, can only be OTHER. Should only be specified if updating the status to CANCELLED.

        reason_description : typing.Optional[str]
            The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountSavings. Can be any user provided message. Should only be specified if updating the status to CANCELLED.

        savings_goal : typing.Optional[Amount]
            The Savings Goal set for this MonetaryAccountSavings.

        setting : typing.Optional[MonetaryAccountSetting]
            The settings of the MonetaryAccountSavings.

        status : typing.Optional[str]
            The status of the MonetaryAccountSavings. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountSavings. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        sub_status : typing.Optional[str]
            The sub-status of the MonetaryAccountSavings providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonetaryAccountSavingsUpdate
            With MonetaryAccountSavings you can create a new savings account.

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
            await client.monetary_account_savings.update_monetary_account_savings_for_user(
                user_id=1,
                item_id=1,
                currency="currency",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_monetary_account_savings_for_user(
            user_id,
            item_id,
            currency=currency,
            all_co_owner=all_co_owner,
            avatar_uuid=avatar_uuid,
            daily_limit=daily_limit,
            description=description,
            reason=reason,
            reason_description=reason_description,
            savings_goal=savings_goal,
            setting=setting,
            status=status,
            sub_status=sub_status,
            request_options=request_options,
        )
        return _response.data
