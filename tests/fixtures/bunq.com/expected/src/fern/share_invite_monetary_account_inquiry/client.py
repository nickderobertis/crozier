

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.label_monetary_account import LabelMonetaryAccount
from ..types.label_user import LabelUser
from ..types.share_detail import ShareDetail
from ..types.share_invite_monetary_account_inquiry_create import ShareInviteMonetaryAccountInquiryCreate
from ..types.share_invite_monetary_account_inquiry_listing import ShareInviteMonetaryAccountInquiryListing
from ..types.share_invite_monetary_account_inquiry_read import ShareInviteMonetaryAccountInquiryRead
from ..types.share_invite_monetary_account_inquiry_update import ShareInviteMonetaryAccountInquiryUpdate
from .raw_client import AsyncRawShareInviteMonetaryAccountInquiryClient, RawShareInviteMonetaryAccountInquiryClient


OMIT = typing.cast(typing.Any, ...)


class ShareInviteMonetaryAccountInquiryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawShareInviteMonetaryAccountInquiryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawShareInviteMonetaryAccountInquiryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawShareInviteMonetaryAccountInquiryClient
        """
        return self._raw_client

    def list_all_share_invite_monetary_account_inquiry_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ShareInviteMonetaryAccountInquiryListing]:
        """
        [DEPRECATED - use /share-invite-monetary-account-response] Get a list with all the share inquiries for a monetary account, only if the requesting user has permission to change the details of the various ones.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ShareInviteMonetaryAccountInquiryListing]
            [DEPRECATED - use /share-invite-monetary-account-response] Used to share a monetary account with another bunq user, as in the 'Connect' feature in the bunq app. Allow the creation of share inquiries that, in the same way as request inquiries, can be revoked by the user creating them or accepted/rejected by the other party.

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
        client.share_invite_monetary_account_inquiry.list_all_share_invite_monetary_account_inquiry_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
        )
        """
        _response = self._raw_client.list_all_share_invite_monetary_account_inquiry_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    def create_share_invite_monetary_account_inquiry_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        *,
        access_type: typing.Optional[str] = OMIT,
        alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        counter_user_alias: typing.Optional[LabelUser] = OMIT,
        draft_share_invite_bank_id: typing.Optional[int] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        relationship: typing.Optional[str] = OMIT,
        share_detail: typing.Optional[ShareDetail] = OMIT,
        share_type: typing.Optional[str] = OMIT,
        start_date: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        user_alias_created: typing.Optional[LabelUser] = OMIT,
        user_alias_revoked: typing.Optional[LabelUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ShareInviteMonetaryAccountInquiryCreate:
        """
        [DEPRECATED - use /share-invite-monetary-account-response] Create a new share inquiry for a monetary account, specifying the permission the other bunq user will have on it.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        access_type : typing.Optional[str]
            Type of access that is in place.

        alias : typing.Optional[LabelMonetaryAccount]
            The label of the monetary account that's being shared.

        counter_user_alias : typing.Optional[LabelUser]
            The label of the user to share with.

        draft_share_invite_bank_id : typing.Optional[int]
            DEPRECATED: USE `access_type` INSTEAD | The id of the draft share invite bank.

        end_date : typing.Optional[str]
            DEPRECATED: USE `access_type` INSTEAD | The expiration date of this share.

        id : typing.Optional[int]
            The id of the newly created share invite.

        monetary_account_id : typing.Optional[int]
            The id of the monetary account the share applies to.

        relationship : typing.Optional[str]
            The relationship: COMPANY_DIRECTOR, COMPANY_EMPLOYEE, etc

        share_detail : typing.Optional[ShareDetail]
            DEPRECATED: USE `access_type` INSTEAD | The share details. Only one of these objects may be passed.

        share_type : typing.Optional[str]
            DEPRECATED: USE `access_type` INSTEAD | The share type, either STANDARD or MUTUAL.

        start_date : typing.Optional[str]
            DEPRECATED: USE `access_type` INSTEAD | The start date of this share.

        status : typing.Optional[str]
            The status of the share. Can be ACTIVE, REVOKED, REJECTED.

        user_alias_created : typing.Optional[LabelUser]
            The user who created the share.

        user_alias_revoked : typing.Optional[LabelUser]
            The user who revoked the share.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ShareInviteMonetaryAccountInquiryCreate
            [DEPRECATED - use /share-invite-monetary-account-response] Used to share a monetary account with another bunq user, as in the 'Connect' feature in the bunq app. Allow the creation of share inquiries that, in the same way as request inquiries, can be revoked by the user creating them or accepted/rejected by the other party.

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
        client.share_invite_monetary_account_inquiry.create_share_invite_monetary_account_inquiry_for_user_monetary_account(
            user_id=1,
            monetary_account_id_=1,
        )
        """
        _response = self._raw_client.create_share_invite_monetary_account_inquiry_for_user_monetary_account(
            user_id,
            monetary_account_id_,
            access_type=access_type,
            alias=alias,
            counter_user_alias=counter_user_alias,
            draft_share_invite_bank_id=draft_share_invite_bank_id,
            end_date=end_date,
            id=id,
            monetary_account_id=monetary_account_id,
            relationship=relationship,
            share_detail=share_detail,
            share_type=share_type,
            start_date=start_date,
            status=status,
            user_alias_created=user_alias_created,
            user_alias_revoked=user_alias_revoked,
            request_options=request_options,
        )
        return _response.data

    def read_share_invite_monetary_account_inquiry_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ShareInviteMonetaryAccountInquiryRead:
        """
        [DEPRECATED - use /share-invite-monetary-account-response] Get the details of a specific share inquiry.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ShareInviteMonetaryAccountInquiryRead
            [DEPRECATED - use /share-invite-monetary-account-response] Used to share a monetary account with another bunq user, as in the 'Connect' feature in the bunq app. Allow the creation of share inquiries that, in the same way as request inquiries, can be revoked by the user creating them or accepted/rejected by the other party.

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
        client.share_invite_monetary_account_inquiry.read_share_invite_monetary_account_inquiry_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_share_invite_monetary_account_inquiry_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    def update_share_invite_monetary_account_inquiry_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        item_id: int,
        *,
        access_type: typing.Optional[str] = OMIT,
        alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        counter_user_alias: typing.Optional[LabelUser] = OMIT,
        draft_share_invite_bank_id: typing.Optional[int] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        relationship: typing.Optional[str] = OMIT,
        share_detail: typing.Optional[ShareDetail] = OMIT,
        share_type: typing.Optional[str] = OMIT,
        start_date: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        user_alias_created: typing.Optional[LabelUser] = OMIT,
        user_alias_revoked: typing.Optional[LabelUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ShareInviteMonetaryAccountInquiryUpdate:
        """
        [DEPRECATED - use /share-invite-monetary-account-response] Update the details of a share. This includes updating status (revoking or cancelling it), granted permission and validity period of this share.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        item_id : int


        access_type : typing.Optional[str]
            Type of access that is in place.

        alias : typing.Optional[LabelMonetaryAccount]
            The label of the monetary account that's being shared.

        counter_user_alias : typing.Optional[LabelUser]
            The label of the user to share with.

        draft_share_invite_bank_id : typing.Optional[int]
            DEPRECATED: USE `access_type` INSTEAD | The id of the draft share invite bank.

        end_date : typing.Optional[str]
            DEPRECATED: USE `access_type` INSTEAD | The expiration date of this share.

        id : typing.Optional[int]
            The id of the newly created share invite.

        monetary_account_id : typing.Optional[int]
            The id of the monetary account the share applies to.

        relationship : typing.Optional[str]
            The relationship: COMPANY_DIRECTOR, COMPANY_EMPLOYEE, etc

        share_detail : typing.Optional[ShareDetail]
            DEPRECATED: USE `access_type` INSTEAD | The share details. Only one of these objects may be passed.

        share_type : typing.Optional[str]
            DEPRECATED: USE `access_type` INSTEAD | The share type, either STANDARD or MUTUAL.

        start_date : typing.Optional[str]
            DEPRECATED: USE `access_type` INSTEAD | The start date of this share.

        status : typing.Optional[str]
            The status of the share. Can be ACTIVE, REVOKED, REJECTED.

        user_alias_created : typing.Optional[LabelUser]
            The user who created the share.

        user_alias_revoked : typing.Optional[LabelUser]
            The user who revoked the share.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ShareInviteMonetaryAccountInquiryUpdate
            [DEPRECATED - use /share-invite-monetary-account-response] Used to share a monetary account with another bunq user, as in the 'Connect' feature in the bunq app. Allow the creation of share inquiries that, in the same way as request inquiries, can be revoked by the user creating them or accepted/rejected by the other party.

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
        client.share_invite_monetary_account_inquiry.update_share_invite_monetary_account_inquiry_for_user_monetary_account(
            user_id=1,
            monetary_account_id_=1,
            item_id=1,
        )
        """
        _response = self._raw_client.update_share_invite_monetary_account_inquiry_for_user_monetary_account(
            user_id,
            monetary_account_id_,
            item_id,
            access_type=access_type,
            alias=alias,
            counter_user_alias=counter_user_alias,
            draft_share_invite_bank_id=draft_share_invite_bank_id,
            end_date=end_date,
            id=id,
            monetary_account_id=monetary_account_id,
            relationship=relationship,
            share_detail=share_detail,
            share_type=share_type,
            start_date=start_date,
            status=status,
            user_alias_created=user_alias_created,
            user_alias_revoked=user_alias_revoked,
            request_options=request_options,
        )
        return _response.data


class AsyncShareInviteMonetaryAccountInquiryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawShareInviteMonetaryAccountInquiryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawShareInviteMonetaryAccountInquiryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawShareInviteMonetaryAccountInquiryClient
        """
        return self._raw_client

    async def list_all_share_invite_monetary_account_inquiry_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ShareInviteMonetaryAccountInquiryListing]:
        """
        [DEPRECATED - use /share-invite-monetary-account-response] Get a list with all the share inquiries for a monetary account, only if the requesting user has permission to change the details of the various ones.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ShareInviteMonetaryAccountInquiryListing]
            [DEPRECATED - use /share-invite-monetary-account-response] Used to share a monetary account with another bunq user, as in the 'Connect' feature in the bunq app. Allow the creation of share inquiries that, in the same way as request inquiries, can be revoked by the user creating them or accepted/rejected by the other party.

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
            await client.share_invite_monetary_account_inquiry.list_all_share_invite_monetary_account_inquiry_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_share_invite_monetary_account_inquiry_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    async def create_share_invite_monetary_account_inquiry_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        *,
        access_type: typing.Optional[str] = OMIT,
        alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        counter_user_alias: typing.Optional[LabelUser] = OMIT,
        draft_share_invite_bank_id: typing.Optional[int] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        relationship: typing.Optional[str] = OMIT,
        share_detail: typing.Optional[ShareDetail] = OMIT,
        share_type: typing.Optional[str] = OMIT,
        start_date: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        user_alias_created: typing.Optional[LabelUser] = OMIT,
        user_alias_revoked: typing.Optional[LabelUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ShareInviteMonetaryAccountInquiryCreate:
        """
        [DEPRECATED - use /share-invite-monetary-account-response] Create a new share inquiry for a monetary account, specifying the permission the other bunq user will have on it.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        access_type : typing.Optional[str]
            Type of access that is in place.

        alias : typing.Optional[LabelMonetaryAccount]
            The label of the monetary account that's being shared.

        counter_user_alias : typing.Optional[LabelUser]
            The label of the user to share with.

        draft_share_invite_bank_id : typing.Optional[int]
            DEPRECATED: USE `access_type` INSTEAD | The id of the draft share invite bank.

        end_date : typing.Optional[str]
            DEPRECATED: USE `access_type` INSTEAD | The expiration date of this share.

        id : typing.Optional[int]
            The id of the newly created share invite.

        monetary_account_id : typing.Optional[int]
            The id of the monetary account the share applies to.

        relationship : typing.Optional[str]
            The relationship: COMPANY_DIRECTOR, COMPANY_EMPLOYEE, etc

        share_detail : typing.Optional[ShareDetail]
            DEPRECATED: USE `access_type` INSTEAD | The share details. Only one of these objects may be passed.

        share_type : typing.Optional[str]
            DEPRECATED: USE `access_type` INSTEAD | The share type, either STANDARD or MUTUAL.

        start_date : typing.Optional[str]
            DEPRECATED: USE `access_type` INSTEAD | The start date of this share.

        status : typing.Optional[str]
            The status of the share. Can be ACTIVE, REVOKED, REJECTED.

        user_alias_created : typing.Optional[LabelUser]
            The user who created the share.

        user_alias_revoked : typing.Optional[LabelUser]
            The user who revoked the share.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ShareInviteMonetaryAccountInquiryCreate
            [DEPRECATED - use /share-invite-monetary-account-response] Used to share a monetary account with another bunq user, as in the 'Connect' feature in the bunq app. Allow the creation of share inquiries that, in the same way as request inquiries, can be revoked by the user creating them or accepted/rejected by the other party.

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
            await client.share_invite_monetary_account_inquiry.create_share_invite_monetary_account_inquiry_for_user_monetary_account(
                user_id=1,
                monetary_account_id_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_share_invite_monetary_account_inquiry_for_user_monetary_account(
            user_id,
            monetary_account_id_,
            access_type=access_type,
            alias=alias,
            counter_user_alias=counter_user_alias,
            draft_share_invite_bank_id=draft_share_invite_bank_id,
            end_date=end_date,
            id=id,
            monetary_account_id=monetary_account_id,
            relationship=relationship,
            share_detail=share_detail,
            share_type=share_type,
            start_date=start_date,
            status=status,
            user_alias_created=user_alias_created,
            user_alias_revoked=user_alias_revoked,
            request_options=request_options,
        )
        return _response.data

    async def read_share_invite_monetary_account_inquiry_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ShareInviteMonetaryAccountInquiryRead:
        """
        [DEPRECATED - use /share-invite-monetary-account-response] Get the details of a specific share inquiry.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ShareInviteMonetaryAccountInquiryRead
            [DEPRECATED - use /share-invite-monetary-account-response] Used to share a monetary account with another bunq user, as in the 'Connect' feature in the bunq app. Allow the creation of share inquiries that, in the same way as request inquiries, can be revoked by the user creating them or accepted/rejected by the other party.

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
            await client.share_invite_monetary_account_inquiry.read_share_invite_monetary_account_inquiry_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_share_invite_monetary_account_inquiry_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_share_invite_monetary_account_inquiry_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        item_id: int,
        *,
        access_type: typing.Optional[str] = OMIT,
        alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        counter_user_alias: typing.Optional[LabelUser] = OMIT,
        draft_share_invite_bank_id: typing.Optional[int] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        relationship: typing.Optional[str] = OMIT,
        share_detail: typing.Optional[ShareDetail] = OMIT,
        share_type: typing.Optional[str] = OMIT,
        start_date: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        user_alias_created: typing.Optional[LabelUser] = OMIT,
        user_alias_revoked: typing.Optional[LabelUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ShareInviteMonetaryAccountInquiryUpdate:
        """
        [DEPRECATED - use /share-invite-monetary-account-response] Update the details of a share. This includes updating status (revoking or cancelling it), granted permission and validity period of this share.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        item_id : int


        access_type : typing.Optional[str]
            Type of access that is in place.

        alias : typing.Optional[LabelMonetaryAccount]
            The label of the monetary account that's being shared.

        counter_user_alias : typing.Optional[LabelUser]
            The label of the user to share with.

        draft_share_invite_bank_id : typing.Optional[int]
            DEPRECATED: USE `access_type` INSTEAD | The id of the draft share invite bank.

        end_date : typing.Optional[str]
            DEPRECATED: USE `access_type` INSTEAD | The expiration date of this share.

        id : typing.Optional[int]
            The id of the newly created share invite.

        monetary_account_id : typing.Optional[int]
            The id of the monetary account the share applies to.

        relationship : typing.Optional[str]
            The relationship: COMPANY_DIRECTOR, COMPANY_EMPLOYEE, etc

        share_detail : typing.Optional[ShareDetail]
            DEPRECATED: USE `access_type` INSTEAD | The share details. Only one of these objects may be passed.

        share_type : typing.Optional[str]
            DEPRECATED: USE `access_type` INSTEAD | The share type, either STANDARD or MUTUAL.

        start_date : typing.Optional[str]
            DEPRECATED: USE `access_type` INSTEAD | The start date of this share.

        status : typing.Optional[str]
            The status of the share. Can be ACTIVE, REVOKED, REJECTED.

        user_alias_created : typing.Optional[LabelUser]
            The user who created the share.

        user_alias_revoked : typing.Optional[LabelUser]
            The user who revoked the share.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ShareInviteMonetaryAccountInquiryUpdate
            [DEPRECATED - use /share-invite-monetary-account-response] Used to share a monetary account with another bunq user, as in the 'Connect' feature in the bunq app. Allow the creation of share inquiries that, in the same way as request inquiries, can be revoked by the user creating them or accepted/rejected by the other party.

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
            await client.share_invite_monetary_account_inquiry.update_share_invite_monetary_account_inquiry_for_user_monetary_account(
                user_id=1,
                monetary_account_id_=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_share_invite_monetary_account_inquiry_for_user_monetary_account(
            user_id,
            monetary_account_id_,
            item_id,
            access_type=access_type,
            alias=alias,
            counter_user_alias=counter_user_alias,
            draft_share_invite_bank_id=draft_share_invite_bank_id,
            end_date=end_date,
            id=id,
            monetary_account_id=monetary_account_id,
            relationship=relationship,
            share_detail=share_detail,
            share_type=share_type,
            start_date=start_date,
            status=status,
            user_alias_created=user_alias_created,
            user_alias_revoked=user_alias_revoked,
            request_options=request_options,
        )
        return _response.data
