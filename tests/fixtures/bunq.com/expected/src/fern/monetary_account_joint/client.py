

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.amount import Amount
from ..types.co_owner import CoOwner
from ..types.monetary_account_joint_create import MonetaryAccountJointCreate
from ..types.monetary_account_joint_listing import MonetaryAccountJointListing
from ..types.monetary_account_joint_read import MonetaryAccountJointRead
from ..types.monetary_account_joint_update import MonetaryAccountJointUpdate
from ..types.monetary_account_setting import MonetaryAccountSetting
from ..types.pointer import Pointer
from .raw_client import AsyncRawMonetaryAccountJointClient, RawMonetaryAccountJointClient


OMIT = typing.cast(typing.Any, ...)


class MonetaryAccountJointClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMonetaryAccountJointClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMonetaryAccountJointClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMonetaryAccountJointClient
        """
        return self._raw_client

    def list_all_monetary_account_joint_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[MonetaryAccountJointListing]:
        """
        The endpoint for joint monetary accounts.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MonetaryAccountJointListing]
            The endpoint for joint monetary accounts.

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
        client.monetary_account_joint.list_all_monetary_account_joint_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_monetary_account_joint_for_user(user_id, request_options=request_options)
        return _response.data

    def create_monetary_account_joint_for_user(
        self,
        user_id: int,
        *,
        all_co_owner: typing.Sequence[CoOwner],
        currency: str,
        alias: typing.Optional[typing.Sequence[Pointer]] = OMIT,
        avatar_uuid: typing.Optional[str] = OMIT,
        daily_limit: typing.Optional[Amount] = OMIT,
        description: typing.Optional[str] = OMIT,
        overdraft_limit: typing.Optional[Amount] = OMIT,
        reason: typing.Optional[str] = OMIT,
        reason_description: typing.Optional[str] = OMIT,
        setting: typing.Optional[MonetaryAccountSetting] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MonetaryAccountJointCreate:
        """
        The endpoint for joint monetary accounts.

        Parameters
        ----------
        user_id : int


        all_co_owner : typing.Sequence[CoOwner]
            The users the account will be joint with.

        currency : str
            The currency of the MonetaryAccountJoint as an ISO 4217 formatted currency code.

        alias : typing.Optional[typing.Sequence[Pointer]]
            The Aliases to add to MonetaryAccountJoint. Must all be confirmed first. Can mostly be ignored.

        avatar_uuid : typing.Optional[str]
            The UUID of the Avatar of the MonetaryAccountJoint.

        daily_limit : typing.Optional[Amount]
            The daily spending limit Amount of the MonetaryAccountJoint. Defaults to 1000 EUR. Currency must match the MonetaryAccountJoint's currency. Limited to 10000 EUR.

        description : typing.Optional[str]
            The description of the MonetaryAccountJoint. Defaults to 'bunq account'.

        overdraft_limit : typing.Optional[Amount]
            The maximum Amount the MonetaryAccountJoint can be 'in the red'. Must be 0 EUR or omitted.

        reason : typing.Optional[str]
            The reason for voluntarily cancelling (closing) the MonetaryAccountJoint, can only be OTHER. Should only be specified if updating the status to CANCELLED.

        reason_description : typing.Optional[str]
            The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountJoint. Can be any user provided message. Should only be specified if updating the status to CANCELLED.

        setting : typing.Optional[MonetaryAccountSetting]
            The settings of the MonetaryAccountJoint.

        status : typing.Optional[str]
            The status of the MonetaryAccountJoint. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountJoint. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        sub_status : typing.Optional[str]
            The sub-status of the MonetaryAccountJoint providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonetaryAccountJointCreate
            The endpoint for joint monetary accounts.

        Examples
        --------
        from fern import CoOwner, FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.monetary_account_joint.create_monetary_account_joint_for_user(
            user_id=1,
            all_co_owner=[CoOwner()],
            currency="currency",
        )
        """
        _response = self._raw_client.create_monetary_account_joint_for_user(
            user_id,
            all_co_owner=all_co_owner,
            currency=currency,
            alias=alias,
            avatar_uuid=avatar_uuid,
            daily_limit=daily_limit,
            description=description,
            overdraft_limit=overdraft_limit,
            reason=reason,
            reason_description=reason_description,
            setting=setting,
            status=status,
            sub_status=sub_status,
            request_options=request_options,
        )
        return _response.data

    def read_monetary_account_joint_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MonetaryAccountJointRead:
        """
        The endpoint for joint monetary accounts.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonetaryAccountJointRead
            The endpoint for joint monetary accounts.

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
        client.monetary_account_joint.read_monetary_account_joint_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_monetary_account_joint_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data

    def update_monetary_account_joint_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        all_co_owner: typing.Sequence[CoOwner],
        currency: str,
        alias: typing.Optional[typing.Sequence[Pointer]] = OMIT,
        avatar_uuid: typing.Optional[str] = OMIT,
        daily_limit: typing.Optional[Amount] = OMIT,
        description: typing.Optional[str] = OMIT,
        overdraft_limit: typing.Optional[Amount] = OMIT,
        reason: typing.Optional[str] = OMIT,
        reason_description: typing.Optional[str] = OMIT,
        setting: typing.Optional[MonetaryAccountSetting] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MonetaryAccountJointUpdate:
        """
        The endpoint for joint monetary accounts.

        Parameters
        ----------
        user_id : int


        item_id : int


        all_co_owner : typing.Sequence[CoOwner]
            The users the account will be joint with.

        currency : str
            The currency of the MonetaryAccountJoint as an ISO 4217 formatted currency code.

        alias : typing.Optional[typing.Sequence[Pointer]]
            The Aliases to add to MonetaryAccountJoint. Must all be confirmed first. Can mostly be ignored.

        avatar_uuid : typing.Optional[str]
            The UUID of the Avatar of the MonetaryAccountJoint.

        daily_limit : typing.Optional[Amount]
            The daily spending limit Amount of the MonetaryAccountJoint. Defaults to 1000 EUR. Currency must match the MonetaryAccountJoint's currency. Limited to 10000 EUR.

        description : typing.Optional[str]
            The description of the MonetaryAccountJoint. Defaults to 'bunq account'.

        overdraft_limit : typing.Optional[Amount]
            The maximum Amount the MonetaryAccountJoint can be 'in the red'. Must be 0 EUR or omitted.

        reason : typing.Optional[str]
            The reason for voluntarily cancelling (closing) the MonetaryAccountJoint, can only be OTHER. Should only be specified if updating the status to CANCELLED.

        reason_description : typing.Optional[str]
            The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountJoint. Can be any user provided message. Should only be specified if updating the status to CANCELLED.

        setting : typing.Optional[MonetaryAccountSetting]
            The settings of the MonetaryAccountJoint.

        status : typing.Optional[str]
            The status of the MonetaryAccountJoint. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountJoint. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        sub_status : typing.Optional[str]
            The sub-status of the MonetaryAccountJoint providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonetaryAccountJointUpdate
            The endpoint for joint monetary accounts.

        Examples
        --------
        from fern import CoOwner, FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.monetary_account_joint.update_monetary_account_joint_for_user(
            user_id=1,
            item_id=1,
            all_co_owner=[CoOwner()],
            currency="currency",
        )
        """
        _response = self._raw_client.update_monetary_account_joint_for_user(
            user_id,
            item_id,
            all_co_owner=all_co_owner,
            currency=currency,
            alias=alias,
            avatar_uuid=avatar_uuid,
            daily_limit=daily_limit,
            description=description,
            overdraft_limit=overdraft_limit,
            reason=reason,
            reason_description=reason_description,
            setting=setting,
            status=status,
            sub_status=sub_status,
            request_options=request_options,
        )
        return _response.data


class AsyncMonetaryAccountJointClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMonetaryAccountJointClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMonetaryAccountJointClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMonetaryAccountJointClient
        """
        return self._raw_client

    async def list_all_monetary_account_joint_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[MonetaryAccountJointListing]:
        """
        The endpoint for joint monetary accounts.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MonetaryAccountJointListing]
            The endpoint for joint monetary accounts.

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
            await client.monetary_account_joint.list_all_monetary_account_joint_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_monetary_account_joint_for_user(
            user_id, request_options=request_options
        )
        return _response.data

    async def create_monetary_account_joint_for_user(
        self,
        user_id: int,
        *,
        all_co_owner: typing.Sequence[CoOwner],
        currency: str,
        alias: typing.Optional[typing.Sequence[Pointer]] = OMIT,
        avatar_uuid: typing.Optional[str] = OMIT,
        daily_limit: typing.Optional[Amount] = OMIT,
        description: typing.Optional[str] = OMIT,
        overdraft_limit: typing.Optional[Amount] = OMIT,
        reason: typing.Optional[str] = OMIT,
        reason_description: typing.Optional[str] = OMIT,
        setting: typing.Optional[MonetaryAccountSetting] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MonetaryAccountJointCreate:
        """
        The endpoint for joint monetary accounts.

        Parameters
        ----------
        user_id : int


        all_co_owner : typing.Sequence[CoOwner]
            The users the account will be joint with.

        currency : str
            The currency of the MonetaryAccountJoint as an ISO 4217 formatted currency code.

        alias : typing.Optional[typing.Sequence[Pointer]]
            The Aliases to add to MonetaryAccountJoint. Must all be confirmed first. Can mostly be ignored.

        avatar_uuid : typing.Optional[str]
            The UUID of the Avatar of the MonetaryAccountJoint.

        daily_limit : typing.Optional[Amount]
            The daily spending limit Amount of the MonetaryAccountJoint. Defaults to 1000 EUR. Currency must match the MonetaryAccountJoint's currency. Limited to 10000 EUR.

        description : typing.Optional[str]
            The description of the MonetaryAccountJoint. Defaults to 'bunq account'.

        overdraft_limit : typing.Optional[Amount]
            The maximum Amount the MonetaryAccountJoint can be 'in the red'. Must be 0 EUR or omitted.

        reason : typing.Optional[str]
            The reason for voluntarily cancelling (closing) the MonetaryAccountJoint, can only be OTHER. Should only be specified if updating the status to CANCELLED.

        reason_description : typing.Optional[str]
            The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountJoint. Can be any user provided message. Should only be specified if updating the status to CANCELLED.

        setting : typing.Optional[MonetaryAccountSetting]
            The settings of the MonetaryAccountJoint.

        status : typing.Optional[str]
            The status of the MonetaryAccountJoint. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountJoint. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        sub_status : typing.Optional[str]
            The sub-status of the MonetaryAccountJoint providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonetaryAccountJointCreate
            The endpoint for joint monetary accounts.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CoOwner

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.monetary_account_joint.create_monetary_account_joint_for_user(
                user_id=1,
                all_co_owner=[CoOwner()],
                currency="currency",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_monetary_account_joint_for_user(
            user_id,
            all_co_owner=all_co_owner,
            currency=currency,
            alias=alias,
            avatar_uuid=avatar_uuid,
            daily_limit=daily_limit,
            description=description,
            overdraft_limit=overdraft_limit,
            reason=reason,
            reason_description=reason_description,
            setting=setting,
            status=status,
            sub_status=sub_status,
            request_options=request_options,
        )
        return _response.data

    async def read_monetary_account_joint_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MonetaryAccountJointRead:
        """
        The endpoint for joint monetary accounts.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonetaryAccountJointRead
            The endpoint for joint monetary accounts.

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
            await client.monetary_account_joint.read_monetary_account_joint_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_monetary_account_joint_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_monetary_account_joint_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        all_co_owner: typing.Sequence[CoOwner],
        currency: str,
        alias: typing.Optional[typing.Sequence[Pointer]] = OMIT,
        avatar_uuid: typing.Optional[str] = OMIT,
        daily_limit: typing.Optional[Amount] = OMIT,
        description: typing.Optional[str] = OMIT,
        overdraft_limit: typing.Optional[Amount] = OMIT,
        reason: typing.Optional[str] = OMIT,
        reason_description: typing.Optional[str] = OMIT,
        setting: typing.Optional[MonetaryAccountSetting] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MonetaryAccountJointUpdate:
        """
        The endpoint for joint monetary accounts.

        Parameters
        ----------
        user_id : int


        item_id : int


        all_co_owner : typing.Sequence[CoOwner]
            The users the account will be joint with.

        currency : str
            The currency of the MonetaryAccountJoint as an ISO 4217 formatted currency code.

        alias : typing.Optional[typing.Sequence[Pointer]]
            The Aliases to add to MonetaryAccountJoint. Must all be confirmed first. Can mostly be ignored.

        avatar_uuid : typing.Optional[str]
            The UUID of the Avatar of the MonetaryAccountJoint.

        daily_limit : typing.Optional[Amount]
            The daily spending limit Amount of the MonetaryAccountJoint. Defaults to 1000 EUR. Currency must match the MonetaryAccountJoint's currency. Limited to 10000 EUR.

        description : typing.Optional[str]
            The description of the MonetaryAccountJoint. Defaults to 'bunq account'.

        overdraft_limit : typing.Optional[Amount]
            The maximum Amount the MonetaryAccountJoint can be 'in the red'. Must be 0 EUR or omitted.

        reason : typing.Optional[str]
            The reason for voluntarily cancelling (closing) the MonetaryAccountJoint, can only be OTHER. Should only be specified if updating the status to CANCELLED.

        reason_description : typing.Optional[str]
            The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountJoint. Can be any user provided message. Should only be specified if updating the status to CANCELLED.

        setting : typing.Optional[MonetaryAccountSetting]
            The settings of the MonetaryAccountJoint.

        status : typing.Optional[str]
            The status of the MonetaryAccountJoint. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountJoint. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        sub_status : typing.Optional[str]
            The sub-status of the MonetaryAccountJoint providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonetaryAccountJointUpdate
            The endpoint for joint monetary accounts.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CoOwner

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.monetary_account_joint.update_monetary_account_joint_for_user(
                user_id=1,
                item_id=1,
                all_co_owner=[CoOwner()],
                currency="currency",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_monetary_account_joint_for_user(
            user_id,
            item_id,
            all_co_owner=all_co_owner,
            currency=currency,
            alias=alias,
            avatar_uuid=avatar_uuid,
            daily_limit=daily_limit,
            description=description,
            overdraft_limit=overdraft_limit,
            reason=reason,
            reason_description=reason_description,
            setting=setting,
            status=status,
            sub_status=sub_status,
            request_options=request_options,
        )
        return _response.data
