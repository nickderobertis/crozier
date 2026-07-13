

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.label_monetary_account import LabelMonetaryAccount
from ..types.label_user import LabelUser
from ..types.relation_user import RelationUser
from ..types.share_detail import ShareDetail
from ..types.share_invite_monetary_account_response_listing import ShareInviteMonetaryAccountResponseListing
from ..types.share_invite_monetary_account_response_read import ShareInviteMonetaryAccountResponseRead
from ..types.share_invite_monetary_account_response_update import ShareInviteMonetaryAccountResponseUpdate
from .raw_client import AsyncRawShareInviteMonetaryAccountResponseClient, RawShareInviteMonetaryAccountResponseClient


OMIT = typing.cast(typing.Any, ...)


class ShareInviteMonetaryAccountResponseClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawShareInviteMonetaryAccountResponseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawShareInviteMonetaryAccountResponseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawShareInviteMonetaryAccountResponseClient
        """
        return self._raw_client

    def list_all_share_invite_monetary_account_response_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ShareInviteMonetaryAccountResponseListing]:
        """
        Return all the shares a user was invited to.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ShareInviteMonetaryAccountResponseListing]
            Used to view or respond to shares a user was invited to. See 'share-invite-bank-inquiry' for more information about the inquiring endpoint.

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
        client.share_invite_monetary_account_response.list_all_share_invite_monetary_account_response_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_share_invite_monetary_account_response_for_user(
            user_id, request_options=request_options
        )
        return _response.data

    def read_share_invite_monetary_account_response_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ShareInviteMonetaryAccountResponseRead:
        """
        Return the details of a specific share a user was invited to.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ShareInviteMonetaryAccountResponseRead
            Used to view or respond to shares a user was invited to. See 'share-invite-bank-inquiry' for more information about the inquiring endpoint.

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
        client.share_invite_monetary_account_response.read_share_invite_monetary_account_response_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_share_invite_monetary_account_response_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data

    def update_share_invite_monetary_account_response_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        access_type: typing.Optional[str] = OMIT,
        card_id: typing.Optional[int] = OMIT,
        counter_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        created: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        draft_share_invite_bank_id: typing.Optional[int] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        relation_user: typing.Optional[RelationUser] = OMIT,
        share_detail: typing.Optional[ShareDetail] = OMIT,
        share_type: typing.Optional[str] = OMIT,
        start_date: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        updated: typing.Optional[str] = OMIT,
        user_alias_cancelled: typing.Optional[LabelUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ShareInviteMonetaryAccountResponseUpdate:
        """
        Accept or reject a share a user was invited to.

        Parameters
        ----------
        user_id : int


        item_id : int


        access_type : typing.Optional[str]
            Type of access that is wanted, one of VIEW_BALANCE, VIEW_TRANSACTION, DRAFT_PAYMENT or FULL_TRANSIENT

        card_id : typing.Optional[int]
            The card to link to the shared monetary account. Used only if share_detail is ShareDetailCardPayment.

        counter_alias : typing.Optional[LabelMonetaryAccount]
            The monetary account and user who created the share.

        created : typing.Optional[str]
            The timestamp of the ShareInviteBankResponse creation.

        description : typing.Optional[str]
            The description of this share. It is basically the monetary account description.

        draft_share_invite_bank_id : typing.Optional[int]
            The id of the draft share invite bank.

        end_date : typing.Optional[str]
            The expiration date of this share.

        id : typing.Optional[int]
            The id of the ShareInviteBankResponse.

        monetary_account_id : typing.Optional[int]
            The id of the monetary account the ACCEPTED share applies to. null otherwise.

        relation_user : typing.Optional[RelationUser]
            All of the relation users towards this MA.

        share_detail : typing.Optional[ShareDetail]
            The share details.

        share_type : typing.Optional[str]
            The share type, either STANDARD or MUTUAL.

        start_date : typing.Optional[str]
            The start date of this share.

        status : typing.Optional[str]
            The status of the share. Can be ACTIVE, REVOKED, REJECTED.

        updated : typing.Optional[str]
            The timestamp of the ShareInviteBankResponse last update.

        user_alias_cancelled : typing.Optional[LabelUser]
            The user who cancelled the share if it has been revoked or rejected.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ShareInviteMonetaryAccountResponseUpdate
            Used to view or respond to shares a user was invited to. See 'share-invite-bank-inquiry' for more information about the inquiring endpoint.

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
        client.share_invite_monetary_account_response.update_share_invite_monetary_account_response_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.update_share_invite_monetary_account_response_for_user(
            user_id,
            item_id,
            access_type=access_type,
            card_id=card_id,
            counter_alias=counter_alias,
            created=created,
            description=description,
            draft_share_invite_bank_id=draft_share_invite_bank_id,
            end_date=end_date,
            id=id,
            monetary_account_id=monetary_account_id,
            relation_user=relation_user,
            share_detail=share_detail,
            share_type=share_type,
            start_date=start_date,
            status=status,
            updated=updated,
            user_alias_cancelled=user_alias_cancelled,
            request_options=request_options,
        )
        return _response.data


class AsyncShareInviteMonetaryAccountResponseClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawShareInviteMonetaryAccountResponseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawShareInviteMonetaryAccountResponseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawShareInviteMonetaryAccountResponseClient
        """
        return self._raw_client

    async def list_all_share_invite_monetary_account_response_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ShareInviteMonetaryAccountResponseListing]:
        """
        Return all the shares a user was invited to.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ShareInviteMonetaryAccountResponseListing]
            Used to view or respond to shares a user was invited to. See 'share-invite-bank-inquiry' for more information about the inquiring endpoint.

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
            await client.share_invite_monetary_account_response.list_all_share_invite_monetary_account_response_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_share_invite_monetary_account_response_for_user(
            user_id, request_options=request_options
        )
        return _response.data

    async def read_share_invite_monetary_account_response_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ShareInviteMonetaryAccountResponseRead:
        """
        Return the details of a specific share a user was invited to.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ShareInviteMonetaryAccountResponseRead
            Used to view or respond to shares a user was invited to. See 'share-invite-bank-inquiry' for more information about the inquiring endpoint.

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
            await client.share_invite_monetary_account_response.read_share_invite_monetary_account_response_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_share_invite_monetary_account_response_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_share_invite_monetary_account_response_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        access_type: typing.Optional[str] = OMIT,
        card_id: typing.Optional[int] = OMIT,
        counter_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        created: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        draft_share_invite_bank_id: typing.Optional[int] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        relation_user: typing.Optional[RelationUser] = OMIT,
        share_detail: typing.Optional[ShareDetail] = OMIT,
        share_type: typing.Optional[str] = OMIT,
        start_date: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        updated: typing.Optional[str] = OMIT,
        user_alias_cancelled: typing.Optional[LabelUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ShareInviteMonetaryAccountResponseUpdate:
        """
        Accept or reject a share a user was invited to.

        Parameters
        ----------
        user_id : int


        item_id : int


        access_type : typing.Optional[str]
            Type of access that is wanted, one of VIEW_BALANCE, VIEW_TRANSACTION, DRAFT_PAYMENT or FULL_TRANSIENT

        card_id : typing.Optional[int]
            The card to link to the shared monetary account. Used only if share_detail is ShareDetailCardPayment.

        counter_alias : typing.Optional[LabelMonetaryAccount]
            The monetary account and user who created the share.

        created : typing.Optional[str]
            The timestamp of the ShareInviteBankResponse creation.

        description : typing.Optional[str]
            The description of this share. It is basically the monetary account description.

        draft_share_invite_bank_id : typing.Optional[int]
            The id of the draft share invite bank.

        end_date : typing.Optional[str]
            The expiration date of this share.

        id : typing.Optional[int]
            The id of the ShareInviteBankResponse.

        monetary_account_id : typing.Optional[int]
            The id of the monetary account the ACCEPTED share applies to. null otherwise.

        relation_user : typing.Optional[RelationUser]
            All of the relation users towards this MA.

        share_detail : typing.Optional[ShareDetail]
            The share details.

        share_type : typing.Optional[str]
            The share type, either STANDARD or MUTUAL.

        start_date : typing.Optional[str]
            The start date of this share.

        status : typing.Optional[str]
            The status of the share. Can be ACTIVE, REVOKED, REJECTED.

        updated : typing.Optional[str]
            The timestamp of the ShareInviteBankResponse last update.

        user_alias_cancelled : typing.Optional[LabelUser]
            The user who cancelled the share if it has been revoked or rejected.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ShareInviteMonetaryAccountResponseUpdate
            Used to view or respond to shares a user was invited to. See 'share-invite-bank-inquiry' for more information about the inquiring endpoint.

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
            await client.share_invite_monetary_account_response.update_share_invite_monetary_account_response_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_share_invite_monetary_account_response_for_user(
            user_id,
            item_id,
            access_type=access_type,
            card_id=card_id,
            counter_alias=counter_alias,
            created=created,
            description=description,
            draft_share_invite_bank_id=draft_share_invite_bank_id,
            end_date=end_date,
            id=id,
            monetary_account_id=monetary_account_id,
            relation_user=relation_user,
            share_detail=share_detail,
            share_type=share_type,
            start_date=start_date,
            status=status,
            updated=updated,
            user_alias_cancelled=user_alias_cancelled,
            request_options=request_options,
        )
        return _response.data
