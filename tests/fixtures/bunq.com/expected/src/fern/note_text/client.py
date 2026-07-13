

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.note_text_bank_switch_service_netherlands_incoming_payment_create import (
    NoteTextBankSwitchServiceNetherlandsIncomingPaymentCreate,
)
from ..types.note_text_bank_switch_service_netherlands_incoming_payment_delete import (
    NoteTextBankSwitchServiceNetherlandsIncomingPaymentDelete,
)
from ..types.note_text_bank_switch_service_netherlands_incoming_payment_listing import (
    NoteTextBankSwitchServiceNetherlandsIncomingPaymentListing,
)
from ..types.note_text_bank_switch_service_netherlands_incoming_payment_read import (
    NoteTextBankSwitchServiceNetherlandsIncomingPaymentRead,
)
from ..types.note_text_bank_switch_service_netherlands_incoming_payment_update import (
    NoteTextBankSwitchServiceNetherlandsIncomingPaymentUpdate,
)
from ..types.note_text_bunq_me_fundraiser_result_create import NoteTextBunqMeFundraiserResultCreate
from ..types.note_text_bunq_me_fundraiser_result_delete import NoteTextBunqMeFundraiserResultDelete
from ..types.note_text_bunq_me_fundraiser_result_listing import NoteTextBunqMeFundraiserResultListing
from ..types.note_text_bunq_me_fundraiser_result_read import NoteTextBunqMeFundraiserResultRead
from ..types.note_text_bunq_me_fundraiser_result_update import NoteTextBunqMeFundraiserResultUpdate
from ..types.note_text_draft_payment_create import NoteTextDraftPaymentCreate
from ..types.note_text_draft_payment_delete import NoteTextDraftPaymentDelete
from ..types.note_text_draft_payment_listing import NoteTextDraftPaymentListing
from ..types.note_text_draft_payment_read import NoteTextDraftPaymentRead
from ..types.note_text_draft_payment_update import NoteTextDraftPaymentUpdate
from ..types.note_text_ideal_merchant_transaction_create import NoteTextIdealMerchantTransactionCreate
from ..types.note_text_ideal_merchant_transaction_delete import NoteTextIdealMerchantTransactionDelete
from ..types.note_text_ideal_merchant_transaction_listing import NoteTextIdealMerchantTransactionListing
from ..types.note_text_ideal_merchant_transaction_read import NoteTextIdealMerchantTransactionRead
from ..types.note_text_ideal_merchant_transaction_update import NoteTextIdealMerchantTransactionUpdate
from ..types.note_text_master_card_action_create import NoteTextMasterCardActionCreate
from ..types.note_text_master_card_action_delete import NoteTextMasterCardActionDelete
from ..types.note_text_master_card_action_listing import NoteTextMasterCardActionListing
from ..types.note_text_master_card_action_read import NoteTextMasterCardActionRead
from ..types.note_text_master_card_action_update import NoteTextMasterCardActionUpdate
from ..types.note_text_payment_batch_create import NoteTextPaymentBatchCreate
from ..types.note_text_payment_batch_delete import NoteTextPaymentBatchDelete
from ..types.note_text_payment_batch_listing import NoteTextPaymentBatchListing
from ..types.note_text_payment_batch_read import NoteTextPaymentBatchRead
from ..types.note_text_payment_batch_update import NoteTextPaymentBatchUpdate
from ..types.note_text_payment_create import NoteTextPaymentCreate
from ..types.note_text_payment_delete import NoteTextPaymentDelete
from ..types.note_text_payment_listing import NoteTextPaymentListing
from ..types.note_text_payment_read import NoteTextPaymentRead
from ..types.note_text_payment_update import NoteTextPaymentUpdate
from ..types.note_text_request_inquiry_batch_create import NoteTextRequestInquiryBatchCreate
from ..types.note_text_request_inquiry_batch_delete import NoteTextRequestInquiryBatchDelete
from ..types.note_text_request_inquiry_batch_listing import NoteTextRequestInquiryBatchListing
from ..types.note_text_request_inquiry_batch_read import NoteTextRequestInquiryBatchRead
from ..types.note_text_request_inquiry_batch_update import NoteTextRequestInquiryBatchUpdate
from ..types.note_text_request_inquiry_create import NoteTextRequestInquiryCreate
from ..types.note_text_request_inquiry_delete import NoteTextRequestInquiryDelete
from ..types.note_text_request_inquiry_listing import NoteTextRequestInquiryListing
from ..types.note_text_request_inquiry_read import NoteTextRequestInquiryRead
from ..types.note_text_request_inquiry_update import NoteTextRequestInquiryUpdate
from ..types.note_text_request_response_create import NoteTextRequestResponseCreate
from ..types.note_text_request_response_delete import NoteTextRequestResponseDelete
from ..types.note_text_request_response_listing import NoteTextRequestResponseListing
from ..types.note_text_request_response_read import NoteTextRequestResponseRead
from ..types.note_text_request_response_update import NoteTextRequestResponseUpdate
from ..types.note_text_schedule_instance_create import NoteTextScheduleInstanceCreate
from ..types.note_text_schedule_instance_delete import NoteTextScheduleInstanceDelete
from ..types.note_text_schedule_instance_listing import NoteTextScheduleInstanceListing
from ..types.note_text_schedule_instance_read import NoteTextScheduleInstanceRead
from ..types.note_text_schedule_instance_update import NoteTextScheduleInstanceUpdate
from ..types.note_text_schedule_payment_batch_create import NoteTextSchedulePaymentBatchCreate
from ..types.note_text_schedule_payment_batch_delete import NoteTextSchedulePaymentBatchDelete
from ..types.note_text_schedule_payment_batch_listing import NoteTextSchedulePaymentBatchListing
from ..types.note_text_schedule_payment_batch_read import NoteTextSchedulePaymentBatchRead
from ..types.note_text_schedule_payment_batch_update import NoteTextSchedulePaymentBatchUpdate
from ..types.note_text_schedule_payment_create import NoteTextSchedulePaymentCreate
from ..types.note_text_schedule_payment_delete import NoteTextSchedulePaymentDelete
from ..types.note_text_schedule_payment_listing import NoteTextSchedulePaymentListing
from ..types.note_text_schedule_payment_read import NoteTextSchedulePaymentRead
from ..types.note_text_schedule_payment_update import NoteTextSchedulePaymentUpdate
from ..types.note_text_sofort_merchant_transaction_create import NoteTextSofortMerchantTransactionCreate
from ..types.note_text_sofort_merchant_transaction_delete import NoteTextSofortMerchantTransactionDelete
from ..types.note_text_sofort_merchant_transaction_listing import NoteTextSofortMerchantTransactionListing
from ..types.note_text_sofort_merchant_transaction_read import NoteTextSofortMerchantTransactionRead
from ..types.note_text_sofort_merchant_transaction_update import NoteTextSofortMerchantTransactionUpdate
from ..types.note_text_whitelist_result_create import NoteTextWhitelistResultCreate
from ..types.note_text_whitelist_result_delete import NoteTextWhitelistResultDelete
from ..types.note_text_whitelist_result_listing import NoteTextWhitelistResultListing
from ..types.note_text_whitelist_result_read import NoteTextWhitelistResultRead
from ..types.note_text_whitelist_result_update import NoteTextWhitelistResultUpdate
from .raw_client import AsyncRawNoteTextClient, RawNoteTextClient


OMIT = typing.cast(typing.Any, ...)


class NoteTextClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNoteTextClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNoteTextClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNoteTextClient
        """
        return self._raw_client

    def list_all_note_text_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextBunqMeFundraiserResultListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        bunqme_fundraiser_result_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextBunqMeFundraiserResultListing]
            Used to manage text notes.

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
        client.note_text.list_all_note_text_for_user_monetary_account_bunqme_fundraiser_result(
            user_id=1,
            monetary_account_id=1,
            bunqme_fundraiser_result_id=1,
        )
        """
        _response = self._raw_client.list_all_note_text_for_user_monetary_account_bunqme_fundraiser_result(
            user_id, monetary_account_id, bunqme_fundraiser_result_id, request_options=request_options
        )
        return _response.data

    def create_note_text_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextBunqMeFundraiserResultCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        bunqme_fundraiser_result_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextBunqMeFundraiserResultCreate
            Used to manage text notes.

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
        client.note_text.create_note_text_for_user_monetary_account_bunqme_fundraiser_result(
            user_id=1,
            monetary_account_id=1,
            bunqme_fundraiser_result_id=1,
        )
        """
        _response = self._raw_client.create_note_text_for_user_monetary_account_bunqme_fundraiser_result(
            user_id, monetary_account_id, bunqme_fundraiser_result_id, content=content, request_options=request_options
        )
        return _response.data

    def read_note_text_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextBunqMeFundraiserResultRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        bunqme_fundraiser_result_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextBunqMeFundraiserResultRead
            Used to manage text notes.

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
        client.note_text.read_note_text_for_user_monetary_account_bunqme_fundraiser_result(
            user_id=1,
            monetary_account_id=1,
            bunqme_fundraiser_result_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_text_for_user_monetary_account_bunqme_fundraiser_result(
            user_id, monetary_account_id, bunqme_fundraiser_result_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_text_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextBunqMeFundraiserResultUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        bunqme_fundraiser_result_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextBunqMeFundraiserResultUpdate
            Used to manage text notes.

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
        client.note_text.update_note_text_for_user_monetary_account_bunqme_fundraiser_result(
            user_id=1,
            monetary_account_id=1,
            bunqme_fundraiser_result_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.update_note_text_for_user_monetary_account_bunqme_fundraiser_result(
            user_id,
            monetary_account_id,
            bunqme_fundraiser_result_id,
            item_id,
            content=content,
            request_options=request_options,
        )
        return _response.data

    def delete_note_text_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextBunqMeFundraiserResultDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        bunqme_fundraiser_result_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextBunqMeFundraiserResultDelete
            Used to manage text notes.

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
        client.note_text.delete_note_text_for_user_monetary_account_bunqme_fundraiser_result(
            user_id=1,
            monetary_account_id=1,
            bunqme_fundraiser_result_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_text_for_user_monetary_account_bunqme_fundraiser_result(
            user_id, monetary_account_id, bunqme_fundraiser_result_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_text_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextDraftPaymentListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        draft_payment_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextDraftPaymentListing]
            Used to manage text notes.

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
        client.note_text.list_all_note_text_for_user_monetary_account_draft_payment(
            user_id=1,
            monetary_account_id=1,
            draft_payment_id=1,
        )
        """
        _response = self._raw_client.list_all_note_text_for_user_monetary_account_draft_payment(
            user_id, monetary_account_id, draft_payment_id, request_options=request_options
        )
        return _response.data

    def create_note_text_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextDraftPaymentCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        draft_payment_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextDraftPaymentCreate
            Used to manage text notes.

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
        client.note_text.create_note_text_for_user_monetary_account_draft_payment(
            user_id=1,
            monetary_account_id=1,
            draft_payment_id=1,
        )
        """
        _response = self._raw_client.create_note_text_for_user_monetary_account_draft_payment(
            user_id, monetary_account_id, draft_payment_id, content=content, request_options=request_options
        )
        return _response.data

    def read_note_text_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextDraftPaymentRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        draft_payment_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextDraftPaymentRead
            Used to manage text notes.

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
        client.note_text.read_note_text_for_user_monetary_account_draft_payment(
            user_id=1,
            monetary_account_id=1,
            draft_payment_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_text_for_user_monetary_account_draft_payment(
            user_id, monetary_account_id, draft_payment_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_text_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextDraftPaymentUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        draft_payment_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextDraftPaymentUpdate
            Used to manage text notes.

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
        client.note_text.update_note_text_for_user_monetary_account_draft_payment(
            user_id=1,
            monetary_account_id=1,
            draft_payment_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.update_note_text_for_user_monetary_account_draft_payment(
            user_id, monetary_account_id, draft_payment_id, item_id, content=content, request_options=request_options
        )
        return _response.data

    def delete_note_text_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextDraftPaymentDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        draft_payment_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextDraftPaymentDelete
            Used to manage text notes.

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
        client.note_text.delete_note_text_for_user_monetary_account_draft_payment(
            user_id=1,
            monetary_account_id=1,
            draft_payment_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_text_for_user_monetary_account_draft_payment(
            user_id, monetary_account_id, draft_payment_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_text_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextIdealMerchantTransactionListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        ideal_merchant_transaction_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextIdealMerchantTransactionListing]
            Used to manage text notes.

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
        client.note_text.list_all_note_text_for_user_monetary_account_ideal_merchant_transaction(
            user_id=1,
            monetary_account_id=1,
            ideal_merchant_transaction_id=1,
        )
        """
        _response = self._raw_client.list_all_note_text_for_user_monetary_account_ideal_merchant_transaction(
            user_id, monetary_account_id, ideal_merchant_transaction_id, request_options=request_options
        )
        return _response.data

    def create_note_text_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextIdealMerchantTransactionCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        ideal_merchant_transaction_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextIdealMerchantTransactionCreate
            Used to manage text notes.

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
        client.note_text.create_note_text_for_user_monetary_account_ideal_merchant_transaction(
            user_id=1,
            monetary_account_id=1,
            ideal_merchant_transaction_id=1,
        )
        """
        _response = self._raw_client.create_note_text_for_user_monetary_account_ideal_merchant_transaction(
            user_id,
            monetary_account_id,
            ideal_merchant_transaction_id,
            content=content,
            request_options=request_options,
        )
        return _response.data

    def read_note_text_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextIdealMerchantTransactionRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        ideal_merchant_transaction_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextIdealMerchantTransactionRead
            Used to manage text notes.

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
        client.note_text.read_note_text_for_user_monetary_account_ideal_merchant_transaction(
            user_id=1,
            monetary_account_id=1,
            ideal_merchant_transaction_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_text_for_user_monetary_account_ideal_merchant_transaction(
            user_id, monetary_account_id, ideal_merchant_transaction_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_text_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextIdealMerchantTransactionUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        ideal_merchant_transaction_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextIdealMerchantTransactionUpdate
            Used to manage text notes.

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
        client.note_text.update_note_text_for_user_monetary_account_ideal_merchant_transaction(
            user_id=1,
            monetary_account_id=1,
            ideal_merchant_transaction_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.update_note_text_for_user_monetary_account_ideal_merchant_transaction(
            user_id,
            monetary_account_id,
            ideal_merchant_transaction_id,
            item_id,
            content=content,
            request_options=request_options,
        )
        return _response.data

    def delete_note_text_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextIdealMerchantTransactionDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        ideal_merchant_transaction_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextIdealMerchantTransactionDelete
            Used to manage text notes.

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
        client.note_text.delete_note_text_for_user_monetary_account_ideal_merchant_transaction(
            user_id=1,
            monetary_account_id=1,
            ideal_merchant_transaction_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_text_for_user_monetary_account_ideal_merchant_transaction(
            user_id, monetary_account_id, ideal_merchant_transaction_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_text_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextMasterCardActionListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        mastercard_action_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextMasterCardActionListing]
            Used to manage text notes.

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
        client.note_text.list_all_note_text_for_user_monetary_account_mastercard_action(
            user_id=1,
            monetary_account_id=1,
            mastercard_action_id=1,
        )
        """
        _response = self._raw_client.list_all_note_text_for_user_monetary_account_mastercard_action(
            user_id, monetary_account_id, mastercard_action_id, request_options=request_options
        )
        return _response.data

    def create_note_text_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextMasterCardActionCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        mastercard_action_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextMasterCardActionCreate
            Used to manage text notes.

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
        client.note_text.create_note_text_for_user_monetary_account_mastercard_action(
            user_id=1,
            monetary_account_id=1,
            mastercard_action_id=1,
        )
        """
        _response = self._raw_client.create_note_text_for_user_monetary_account_mastercard_action(
            user_id, monetary_account_id, mastercard_action_id, content=content, request_options=request_options
        )
        return _response.data

    def read_note_text_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextMasterCardActionRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        mastercard_action_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextMasterCardActionRead
            Used to manage text notes.

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
        client.note_text.read_note_text_for_user_monetary_account_mastercard_action(
            user_id=1,
            monetary_account_id=1,
            mastercard_action_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_text_for_user_monetary_account_mastercard_action(
            user_id, monetary_account_id, mastercard_action_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_text_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextMasterCardActionUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        mastercard_action_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextMasterCardActionUpdate
            Used to manage text notes.

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
        client.note_text.update_note_text_for_user_monetary_account_mastercard_action(
            user_id=1,
            monetary_account_id=1,
            mastercard_action_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.update_note_text_for_user_monetary_account_mastercard_action(
            user_id,
            monetary_account_id,
            mastercard_action_id,
            item_id,
            content=content,
            request_options=request_options,
        )
        return _response.data

    def delete_note_text_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextMasterCardActionDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        mastercard_action_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextMasterCardActionDelete
            Used to manage text notes.

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
        client.note_text.delete_note_text_for_user_monetary_account_mastercard_action(
            user_id=1,
            monetary_account_id=1,
            mastercard_action_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_text_for_user_monetary_account_mastercard_action(
            user_id, monetary_account_id, mastercard_action_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_text_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextPaymentBatchListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_batch_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextPaymentBatchListing]
            Used to manage text notes.

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
        client.note_text.list_all_note_text_for_user_monetary_account_payment_batch(
            user_id=1,
            monetary_account_id=1,
            payment_batch_id=1,
        )
        """
        _response = self._raw_client.list_all_note_text_for_user_monetary_account_payment_batch(
            user_id, monetary_account_id, payment_batch_id, request_options=request_options
        )
        return _response.data

    def create_note_text_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextPaymentBatchCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_batch_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextPaymentBatchCreate
            Used to manage text notes.

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
        client.note_text.create_note_text_for_user_monetary_account_payment_batch(
            user_id=1,
            monetary_account_id=1,
            payment_batch_id=1,
        )
        """
        _response = self._raw_client.create_note_text_for_user_monetary_account_payment_batch(
            user_id, monetary_account_id, payment_batch_id, content=content, request_options=request_options
        )
        return _response.data

    def read_note_text_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextPaymentBatchRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_batch_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextPaymentBatchRead
            Used to manage text notes.

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
        client.note_text.read_note_text_for_user_monetary_account_payment_batch(
            user_id=1,
            monetary_account_id=1,
            payment_batch_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_text_for_user_monetary_account_payment_batch(
            user_id, monetary_account_id, payment_batch_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_text_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextPaymentBatchUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_batch_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextPaymentBatchUpdate
            Used to manage text notes.

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
        client.note_text.update_note_text_for_user_monetary_account_payment_batch(
            user_id=1,
            monetary_account_id=1,
            payment_batch_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.update_note_text_for_user_monetary_account_payment_batch(
            user_id, monetary_account_id, payment_batch_id, item_id, content=content, request_options=request_options
        )
        return _response.data

    def delete_note_text_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextPaymentBatchDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_batch_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextPaymentBatchDelete
            Used to manage text notes.

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
        client.note_text.delete_note_text_for_user_monetary_account_payment_batch(
            user_id=1,
            monetary_account_id=1,
            payment_batch_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_text_for_user_monetary_account_payment_batch(
            user_id, monetary_account_id, payment_batch_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_text_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextPaymentListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextPaymentListing]
            Used to manage text notes.

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
        client.note_text.list_all_note_text_for_user_monetary_account_payment(
            user_id=1,
            monetary_account_id=1,
            payment_id=1,
        )
        """
        _response = self._raw_client.list_all_note_text_for_user_monetary_account_payment(
            user_id, monetary_account_id, payment_id, request_options=request_options
        )
        return _response.data

    def create_note_text_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextPaymentCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextPaymentCreate
            Used to manage text notes.

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
        client.note_text.create_note_text_for_user_monetary_account_payment(
            user_id=1,
            monetary_account_id=1,
            payment_id=1,
        )
        """
        _response = self._raw_client.create_note_text_for_user_monetary_account_payment(
            user_id, monetary_account_id, payment_id, content=content, request_options=request_options
        )
        return _response.data

    def read_note_text_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextPaymentRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextPaymentRead
            Used to manage text notes.

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
        client.note_text.read_note_text_for_user_monetary_account_payment(
            user_id=1,
            monetary_account_id=1,
            payment_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_text_for_user_monetary_account_payment(
            user_id, monetary_account_id, payment_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_text_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextPaymentUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextPaymentUpdate
            Used to manage text notes.

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
        client.note_text.update_note_text_for_user_monetary_account_payment(
            user_id=1,
            monetary_account_id=1,
            payment_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.update_note_text_for_user_monetary_account_payment(
            user_id, monetary_account_id, payment_id, item_id, content=content, request_options=request_options
        )
        return _response.data

    def delete_note_text_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextPaymentDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextPaymentDelete
            Used to manage text notes.

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
        client.note_text.delete_note_text_for_user_monetary_account_payment(
            user_id=1,
            monetary_account_id=1,
            payment_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_text_for_user_monetary_account_payment(
            user_id, monetary_account_id, payment_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_text_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextRequestInquiryBatchListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_batch_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextRequestInquiryBatchListing]
            Used to manage text notes.

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
        client.note_text.list_all_note_text_for_user_monetary_account_request_inquiry_batch(
            user_id=1,
            monetary_account_id=1,
            request_inquiry_batch_id=1,
        )
        """
        _response = self._raw_client.list_all_note_text_for_user_monetary_account_request_inquiry_batch(
            user_id, monetary_account_id, request_inquiry_batch_id, request_options=request_options
        )
        return _response.data

    def create_note_text_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextRequestInquiryBatchCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_batch_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextRequestInquiryBatchCreate
            Used to manage text notes.

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
        client.note_text.create_note_text_for_user_monetary_account_request_inquiry_batch(
            user_id=1,
            monetary_account_id=1,
            request_inquiry_batch_id=1,
        )
        """
        _response = self._raw_client.create_note_text_for_user_monetary_account_request_inquiry_batch(
            user_id, monetary_account_id, request_inquiry_batch_id, content=content, request_options=request_options
        )
        return _response.data

    def read_note_text_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextRequestInquiryBatchRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_batch_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextRequestInquiryBatchRead
            Used to manage text notes.

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
        client.note_text.read_note_text_for_user_monetary_account_request_inquiry_batch(
            user_id=1,
            monetary_account_id=1,
            request_inquiry_batch_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_text_for_user_monetary_account_request_inquiry_batch(
            user_id, monetary_account_id, request_inquiry_batch_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_text_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextRequestInquiryBatchUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_batch_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextRequestInquiryBatchUpdate
            Used to manage text notes.

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
        client.note_text.update_note_text_for_user_monetary_account_request_inquiry_batch(
            user_id=1,
            monetary_account_id=1,
            request_inquiry_batch_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.update_note_text_for_user_monetary_account_request_inquiry_batch(
            user_id,
            monetary_account_id,
            request_inquiry_batch_id,
            item_id,
            content=content,
            request_options=request_options,
        )
        return _response.data

    def delete_note_text_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextRequestInquiryBatchDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_batch_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextRequestInquiryBatchDelete
            Used to manage text notes.

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
        client.note_text.delete_note_text_for_user_monetary_account_request_inquiry_batch(
            user_id=1,
            monetary_account_id=1,
            request_inquiry_batch_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_text_for_user_monetary_account_request_inquiry_batch(
            user_id, monetary_account_id, request_inquiry_batch_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_text_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextRequestInquiryListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextRequestInquiryListing]
            Used to manage text notes.

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
        client.note_text.list_all_note_text_for_user_monetary_account_request_inquiry(
            user_id=1,
            monetary_account_id=1,
            request_inquiry_id=1,
        )
        """
        _response = self._raw_client.list_all_note_text_for_user_monetary_account_request_inquiry(
            user_id, monetary_account_id, request_inquiry_id, request_options=request_options
        )
        return _response.data

    def create_note_text_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextRequestInquiryCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextRequestInquiryCreate
            Used to manage text notes.

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
        client.note_text.create_note_text_for_user_monetary_account_request_inquiry(
            user_id=1,
            monetary_account_id=1,
            request_inquiry_id=1,
        )
        """
        _response = self._raw_client.create_note_text_for_user_monetary_account_request_inquiry(
            user_id, monetary_account_id, request_inquiry_id, content=content, request_options=request_options
        )
        return _response.data

    def read_note_text_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextRequestInquiryRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextRequestInquiryRead
            Used to manage text notes.

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
        client.note_text.read_note_text_for_user_monetary_account_request_inquiry(
            user_id=1,
            monetary_account_id=1,
            request_inquiry_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_text_for_user_monetary_account_request_inquiry(
            user_id, monetary_account_id, request_inquiry_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_text_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextRequestInquiryUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextRequestInquiryUpdate
            Used to manage text notes.

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
        client.note_text.update_note_text_for_user_monetary_account_request_inquiry(
            user_id=1,
            monetary_account_id=1,
            request_inquiry_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.update_note_text_for_user_monetary_account_request_inquiry(
            user_id, monetary_account_id, request_inquiry_id, item_id, content=content, request_options=request_options
        )
        return _response.data

    def delete_note_text_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextRequestInquiryDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextRequestInquiryDelete
            Used to manage text notes.

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
        client.note_text.delete_note_text_for_user_monetary_account_request_inquiry(
            user_id=1,
            monetary_account_id=1,
            request_inquiry_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_text_for_user_monetary_account_request_inquiry(
            user_id, monetary_account_id, request_inquiry_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_text_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextRequestResponseListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_response_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextRequestResponseListing]
            Used to manage text notes.

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
        client.note_text.list_all_note_text_for_user_monetary_account_request_response(
            user_id=1,
            monetary_account_id=1,
            request_response_id=1,
        )
        """
        _response = self._raw_client.list_all_note_text_for_user_monetary_account_request_response(
            user_id, monetary_account_id, request_response_id, request_options=request_options
        )
        return _response.data

    def create_note_text_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextRequestResponseCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_response_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextRequestResponseCreate
            Used to manage text notes.

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
        client.note_text.create_note_text_for_user_monetary_account_request_response(
            user_id=1,
            monetary_account_id=1,
            request_response_id=1,
        )
        """
        _response = self._raw_client.create_note_text_for_user_monetary_account_request_response(
            user_id, monetary_account_id, request_response_id, content=content, request_options=request_options
        )
        return _response.data

    def read_note_text_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextRequestResponseRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_response_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextRequestResponseRead
            Used to manage text notes.

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
        client.note_text.read_note_text_for_user_monetary_account_request_response(
            user_id=1,
            monetary_account_id=1,
            request_response_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_text_for_user_monetary_account_request_response(
            user_id, monetary_account_id, request_response_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_text_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextRequestResponseUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_response_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextRequestResponseUpdate
            Used to manage text notes.

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
        client.note_text.update_note_text_for_user_monetary_account_request_response(
            user_id=1,
            monetary_account_id=1,
            request_response_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.update_note_text_for_user_monetary_account_request_response(
            user_id, monetary_account_id, request_response_id, item_id, content=content, request_options=request_options
        )
        return _response.data

    def delete_note_text_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextRequestResponseDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_response_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextRequestResponseDelete
            Used to manage text notes.

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
        client.note_text.delete_note_text_for_user_monetary_account_request_response(
            user_id=1,
            monetary_account_id=1,
            request_response_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_text_for_user_monetary_account_request_response(
            user_id, monetary_account_id, request_response_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_text_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextSchedulePaymentBatchListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_batch_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextSchedulePaymentBatchListing]
            Used to manage text notes.

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
        client.note_text.list_all_note_text_for_user_monetary_account_schedule_payment_batch(
            user_id=1,
            monetary_account_id=1,
            schedule_payment_batch_id=1,
        )
        """
        _response = self._raw_client.list_all_note_text_for_user_monetary_account_schedule_payment_batch(
            user_id, monetary_account_id, schedule_payment_batch_id, request_options=request_options
        )
        return _response.data

    def create_note_text_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextSchedulePaymentBatchCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_batch_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextSchedulePaymentBatchCreate
            Used to manage text notes.

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
        client.note_text.create_note_text_for_user_monetary_account_schedule_payment_batch(
            user_id=1,
            monetary_account_id=1,
            schedule_payment_batch_id=1,
        )
        """
        _response = self._raw_client.create_note_text_for_user_monetary_account_schedule_payment_batch(
            user_id, monetary_account_id, schedule_payment_batch_id, content=content, request_options=request_options
        )
        return _response.data

    def read_note_text_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextSchedulePaymentBatchRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_batch_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextSchedulePaymentBatchRead
            Used to manage text notes.

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
        client.note_text.read_note_text_for_user_monetary_account_schedule_payment_batch(
            user_id=1,
            monetary_account_id=1,
            schedule_payment_batch_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_text_for_user_monetary_account_schedule_payment_batch(
            user_id, monetary_account_id, schedule_payment_batch_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_text_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextSchedulePaymentBatchUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_batch_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextSchedulePaymentBatchUpdate
            Used to manage text notes.

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
        client.note_text.update_note_text_for_user_monetary_account_schedule_payment_batch(
            user_id=1,
            monetary_account_id=1,
            schedule_payment_batch_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.update_note_text_for_user_monetary_account_schedule_payment_batch(
            user_id,
            monetary_account_id,
            schedule_payment_batch_id,
            item_id,
            content=content,
            request_options=request_options,
        )
        return _response.data

    def delete_note_text_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextSchedulePaymentBatchDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_batch_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextSchedulePaymentBatchDelete
            Used to manage text notes.

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
        client.note_text.delete_note_text_for_user_monetary_account_schedule_payment_batch(
            user_id=1,
            monetary_account_id=1,
            schedule_payment_batch_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_text_for_user_monetary_account_schedule_payment_batch(
            user_id, monetary_account_id, schedule_payment_batch_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_text_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextSchedulePaymentListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextSchedulePaymentListing]
            Used to manage text notes.

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
        client.note_text.list_all_note_text_for_user_monetary_account_schedule_payment(
            user_id=1,
            monetary_account_id=1,
            schedule_payment_id=1,
        )
        """
        _response = self._raw_client.list_all_note_text_for_user_monetary_account_schedule_payment(
            user_id, monetary_account_id, schedule_payment_id, request_options=request_options
        )
        return _response.data

    def create_note_text_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextSchedulePaymentCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextSchedulePaymentCreate
            Used to manage text notes.

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
        client.note_text.create_note_text_for_user_monetary_account_schedule_payment(
            user_id=1,
            monetary_account_id=1,
            schedule_payment_id=1,
        )
        """
        _response = self._raw_client.create_note_text_for_user_monetary_account_schedule_payment(
            user_id, monetary_account_id, schedule_payment_id, content=content, request_options=request_options
        )
        return _response.data

    def read_note_text_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextSchedulePaymentRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextSchedulePaymentRead
            Used to manage text notes.

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
        client.note_text.read_note_text_for_user_monetary_account_schedule_payment(
            user_id=1,
            monetary_account_id=1,
            schedule_payment_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_text_for_user_monetary_account_schedule_payment(
            user_id, monetary_account_id, schedule_payment_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_text_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextSchedulePaymentUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextSchedulePaymentUpdate
            Used to manage text notes.

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
        client.note_text.update_note_text_for_user_monetary_account_schedule_payment(
            user_id=1,
            monetary_account_id=1,
            schedule_payment_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.update_note_text_for_user_monetary_account_schedule_payment(
            user_id, monetary_account_id, schedule_payment_id, item_id, content=content, request_options=request_options
        )
        return _response.data

    def delete_note_text_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextSchedulePaymentDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextSchedulePaymentDelete
            Used to manage text notes.

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
        client.note_text.delete_note_text_for_user_monetary_account_schedule_payment(
            user_id=1,
            monetary_account_id=1,
            schedule_payment_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_text_for_user_monetary_account_schedule_payment(
            user_id, monetary_account_id, schedule_payment_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_text_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextScheduleInstanceListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_id : int


        schedule_instance_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextScheduleInstanceListing]
            Used to manage text notes.

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
        client.note_text.list_all_note_text_for_user_monetary_account_schedule_schedule_instance(
            user_id=1,
            monetary_account_id=1,
            schedule_id=1,
            schedule_instance_id=1,
        )
        """
        _response = self._raw_client.list_all_note_text_for_user_monetary_account_schedule_schedule_instance(
            user_id, monetary_account_id, schedule_id, schedule_instance_id, request_options=request_options
        )
        return _response.data

    def create_note_text_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextScheduleInstanceCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_id : int


        schedule_instance_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextScheduleInstanceCreate
            Used to manage text notes.

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
        client.note_text.create_note_text_for_user_monetary_account_schedule_schedule_instance(
            user_id=1,
            monetary_account_id=1,
            schedule_id=1,
            schedule_instance_id=1,
        )
        """
        _response = self._raw_client.create_note_text_for_user_monetary_account_schedule_schedule_instance(
            user_id,
            monetary_account_id,
            schedule_id,
            schedule_instance_id,
            content=content,
            request_options=request_options,
        )
        return _response.data

    def read_note_text_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextScheduleInstanceRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_id : int


        schedule_instance_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextScheduleInstanceRead
            Used to manage text notes.

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
        client.note_text.read_note_text_for_user_monetary_account_schedule_schedule_instance(
            user_id=1,
            monetary_account_id=1,
            schedule_id=1,
            schedule_instance_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_text_for_user_monetary_account_schedule_schedule_instance(
            user_id, monetary_account_id, schedule_id, schedule_instance_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_text_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextScheduleInstanceUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_id : int


        schedule_instance_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextScheduleInstanceUpdate
            Used to manage text notes.

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
        client.note_text.update_note_text_for_user_monetary_account_schedule_schedule_instance(
            user_id=1,
            monetary_account_id=1,
            schedule_id=1,
            schedule_instance_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.update_note_text_for_user_monetary_account_schedule_schedule_instance(
            user_id,
            monetary_account_id,
            schedule_id,
            schedule_instance_id,
            item_id,
            content=content,
            request_options=request_options,
        )
        return _response.data

    def delete_note_text_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextScheduleInstanceDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_id : int


        schedule_instance_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextScheduleInstanceDelete
            Used to manage text notes.

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
        client.note_text.delete_note_text_for_user_monetary_account_schedule_schedule_instance(
            user_id=1,
            monetary_account_id=1,
            schedule_id=1,
            schedule_instance_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_text_for_user_monetary_account_schedule_schedule_instance(
            user_id, monetary_account_id, schedule_id, schedule_instance_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_text_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextSofortMerchantTransactionListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        sofort_merchant_transaction_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextSofortMerchantTransactionListing]
            Used to manage text notes.

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
        client.note_text.list_all_note_text_for_user_monetary_account_sofort_merchant_transaction(
            user_id=1,
            monetary_account_id=1,
            sofort_merchant_transaction_id=1,
        )
        """
        _response = self._raw_client.list_all_note_text_for_user_monetary_account_sofort_merchant_transaction(
            user_id, monetary_account_id, sofort_merchant_transaction_id, request_options=request_options
        )
        return _response.data

    def create_note_text_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextSofortMerchantTransactionCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        sofort_merchant_transaction_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextSofortMerchantTransactionCreate
            Used to manage text notes.

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
        client.note_text.create_note_text_for_user_monetary_account_sofort_merchant_transaction(
            user_id=1,
            monetary_account_id=1,
            sofort_merchant_transaction_id=1,
        )
        """
        _response = self._raw_client.create_note_text_for_user_monetary_account_sofort_merchant_transaction(
            user_id,
            monetary_account_id,
            sofort_merchant_transaction_id,
            content=content,
            request_options=request_options,
        )
        return _response.data

    def read_note_text_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextSofortMerchantTransactionRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        sofort_merchant_transaction_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextSofortMerchantTransactionRead
            Used to manage text notes.

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
        client.note_text.read_note_text_for_user_monetary_account_sofort_merchant_transaction(
            user_id=1,
            monetary_account_id=1,
            sofort_merchant_transaction_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_text_for_user_monetary_account_sofort_merchant_transaction(
            user_id, monetary_account_id, sofort_merchant_transaction_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_text_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextSofortMerchantTransactionUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        sofort_merchant_transaction_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextSofortMerchantTransactionUpdate
            Used to manage text notes.

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
        client.note_text.update_note_text_for_user_monetary_account_sofort_merchant_transaction(
            user_id=1,
            monetary_account_id=1,
            sofort_merchant_transaction_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.update_note_text_for_user_monetary_account_sofort_merchant_transaction(
            user_id,
            monetary_account_id,
            sofort_merchant_transaction_id,
            item_id,
            content=content,
            request_options=request_options,
        )
        return _response.data

    def delete_note_text_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextSofortMerchantTransactionDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        sofort_merchant_transaction_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextSofortMerchantTransactionDelete
            Used to manage text notes.

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
        client.note_text.delete_note_text_for_user_monetary_account_sofort_merchant_transaction(
            user_id=1,
            monetary_account_id=1,
            sofort_merchant_transaction_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_text_for_user_monetary_account_sofort_merchant_transaction(
            user_id, monetary_account_id, sofort_merchant_transaction_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_text_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextBankSwitchServiceNetherlandsIncomingPaymentListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        switch_service_payment_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextBankSwitchServiceNetherlandsIncomingPaymentListing]
            Used to manage text notes.

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
        client.note_text.list_all_note_text_for_user_monetary_account_switch_service_payment(
            user_id=1,
            monetary_account_id=1,
            switch_service_payment_id=1,
        )
        """
        _response = self._raw_client.list_all_note_text_for_user_monetary_account_switch_service_payment(
            user_id, monetary_account_id, switch_service_payment_id, request_options=request_options
        )
        return _response.data

    def create_note_text_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextBankSwitchServiceNetherlandsIncomingPaymentCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        switch_service_payment_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextBankSwitchServiceNetherlandsIncomingPaymentCreate
            Used to manage text notes.

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
        client.note_text.create_note_text_for_user_monetary_account_switch_service_payment(
            user_id=1,
            monetary_account_id=1,
            switch_service_payment_id=1,
        )
        """
        _response = self._raw_client.create_note_text_for_user_monetary_account_switch_service_payment(
            user_id, monetary_account_id, switch_service_payment_id, content=content, request_options=request_options
        )
        return _response.data

    def read_note_text_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextBankSwitchServiceNetherlandsIncomingPaymentRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        switch_service_payment_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextBankSwitchServiceNetherlandsIncomingPaymentRead
            Used to manage text notes.

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
        client.note_text.read_note_text_for_user_monetary_account_switch_service_payment(
            user_id=1,
            monetary_account_id=1,
            switch_service_payment_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_text_for_user_monetary_account_switch_service_payment(
            user_id, monetary_account_id, switch_service_payment_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_text_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextBankSwitchServiceNetherlandsIncomingPaymentUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        switch_service_payment_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextBankSwitchServiceNetherlandsIncomingPaymentUpdate
            Used to manage text notes.

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
        client.note_text.update_note_text_for_user_monetary_account_switch_service_payment(
            user_id=1,
            monetary_account_id=1,
            switch_service_payment_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.update_note_text_for_user_monetary_account_switch_service_payment(
            user_id,
            monetary_account_id,
            switch_service_payment_id,
            item_id,
            content=content,
            request_options=request_options,
        )
        return _response.data

    def delete_note_text_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextBankSwitchServiceNetherlandsIncomingPaymentDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        switch_service_payment_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextBankSwitchServiceNetherlandsIncomingPaymentDelete
            Used to manage text notes.

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
        client.note_text.delete_note_text_for_user_monetary_account_switch_service_payment(
            user_id=1,
            monetary_account_id=1,
            switch_service_payment_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_text_for_user_monetary_account_switch_service_payment(
            user_id, monetary_account_id, switch_service_payment_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_text_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextWhitelistResultListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        whitelist_id : int


        whitelist_result_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextWhitelistResultListing]
            Used to manage text notes.

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
        client.note_text.list_all_note_text_for_user_monetary_account_whitelist_whitelist_result(
            user_id=1,
            monetary_account_id=1,
            whitelist_id=1,
            whitelist_result_id=1,
        )
        """
        _response = self._raw_client.list_all_note_text_for_user_monetary_account_whitelist_whitelist_result(
            user_id, monetary_account_id, whitelist_id, whitelist_result_id, request_options=request_options
        )
        return _response.data

    def create_note_text_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextWhitelistResultCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        whitelist_id : int


        whitelist_result_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextWhitelistResultCreate
            Used to manage text notes.

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
        client.note_text.create_note_text_for_user_monetary_account_whitelist_whitelist_result(
            user_id=1,
            monetary_account_id=1,
            whitelist_id=1,
            whitelist_result_id=1,
        )
        """
        _response = self._raw_client.create_note_text_for_user_monetary_account_whitelist_whitelist_result(
            user_id,
            monetary_account_id,
            whitelist_id,
            whitelist_result_id,
            content=content,
            request_options=request_options,
        )
        return _response.data

    def read_note_text_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextWhitelistResultRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        whitelist_id : int


        whitelist_result_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextWhitelistResultRead
            Used to manage text notes.

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
        client.note_text.read_note_text_for_user_monetary_account_whitelist_whitelist_result(
            user_id=1,
            monetary_account_id=1,
            whitelist_id=1,
            whitelist_result_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_text_for_user_monetary_account_whitelist_whitelist_result(
            user_id, monetary_account_id, whitelist_id, whitelist_result_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_text_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextWhitelistResultUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        whitelist_id : int


        whitelist_result_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextWhitelistResultUpdate
            Used to manage text notes.

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
        client.note_text.update_note_text_for_user_monetary_account_whitelist_whitelist_result(
            user_id=1,
            monetary_account_id=1,
            whitelist_id=1,
            whitelist_result_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.update_note_text_for_user_monetary_account_whitelist_whitelist_result(
            user_id,
            monetary_account_id,
            whitelist_id,
            whitelist_result_id,
            item_id,
            content=content,
            request_options=request_options,
        )
        return _response.data

    def delete_note_text_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextWhitelistResultDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        whitelist_id : int


        whitelist_result_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextWhitelistResultDelete
            Used to manage text notes.

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
        client.note_text.delete_note_text_for_user_monetary_account_whitelist_whitelist_result(
            user_id=1,
            monetary_account_id=1,
            whitelist_id=1,
            whitelist_result_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_text_for_user_monetary_account_whitelist_whitelist_result(
            user_id, monetary_account_id, whitelist_id, whitelist_result_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncNoteTextClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNoteTextClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNoteTextClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNoteTextClient
        """
        return self._raw_client

    async def list_all_note_text_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextBunqMeFundraiserResultListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        bunqme_fundraiser_result_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextBunqMeFundraiserResultListing]
            Used to manage text notes.

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
            await client.note_text.list_all_note_text_for_user_monetary_account_bunqme_fundraiser_result(
                user_id=1,
                monetary_account_id=1,
                bunqme_fundraiser_result_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_note_text_for_user_monetary_account_bunqme_fundraiser_result(
            user_id, monetary_account_id, bunqme_fundraiser_result_id, request_options=request_options
        )
        return _response.data

    async def create_note_text_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextBunqMeFundraiserResultCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        bunqme_fundraiser_result_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextBunqMeFundraiserResultCreate
            Used to manage text notes.

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
            await client.note_text.create_note_text_for_user_monetary_account_bunqme_fundraiser_result(
                user_id=1,
                monetary_account_id=1,
                bunqme_fundraiser_result_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_text_for_user_monetary_account_bunqme_fundraiser_result(
            user_id, monetary_account_id, bunqme_fundraiser_result_id, content=content, request_options=request_options
        )
        return _response.data

    async def read_note_text_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextBunqMeFundraiserResultRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        bunqme_fundraiser_result_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextBunqMeFundraiserResultRead
            Used to manage text notes.

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
            await client.note_text.read_note_text_for_user_monetary_account_bunqme_fundraiser_result(
                user_id=1,
                monetary_account_id=1,
                bunqme_fundraiser_result_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_text_for_user_monetary_account_bunqme_fundraiser_result(
            user_id, monetary_account_id, bunqme_fundraiser_result_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_text_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextBunqMeFundraiserResultUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        bunqme_fundraiser_result_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextBunqMeFundraiserResultUpdate
            Used to manage text notes.

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
            await client.note_text.update_note_text_for_user_monetary_account_bunqme_fundraiser_result(
                user_id=1,
                monetary_account_id=1,
                bunqme_fundraiser_result_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_text_for_user_monetary_account_bunqme_fundraiser_result(
            user_id,
            monetary_account_id,
            bunqme_fundraiser_result_id,
            item_id,
            content=content,
            request_options=request_options,
        )
        return _response.data

    async def delete_note_text_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextBunqMeFundraiserResultDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        bunqme_fundraiser_result_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextBunqMeFundraiserResultDelete
            Used to manage text notes.

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
            await client.note_text.delete_note_text_for_user_monetary_account_bunqme_fundraiser_result(
                user_id=1,
                monetary_account_id=1,
                bunqme_fundraiser_result_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_text_for_user_monetary_account_bunqme_fundraiser_result(
            user_id, monetary_account_id, bunqme_fundraiser_result_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_text_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextDraftPaymentListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        draft_payment_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextDraftPaymentListing]
            Used to manage text notes.

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
            await client.note_text.list_all_note_text_for_user_monetary_account_draft_payment(
                user_id=1,
                monetary_account_id=1,
                draft_payment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_note_text_for_user_monetary_account_draft_payment(
            user_id, monetary_account_id, draft_payment_id, request_options=request_options
        )
        return _response.data

    async def create_note_text_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextDraftPaymentCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        draft_payment_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextDraftPaymentCreate
            Used to manage text notes.

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
            await client.note_text.create_note_text_for_user_monetary_account_draft_payment(
                user_id=1,
                monetary_account_id=1,
                draft_payment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_text_for_user_monetary_account_draft_payment(
            user_id, monetary_account_id, draft_payment_id, content=content, request_options=request_options
        )
        return _response.data

    async def read_note_text_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextDraftPaymentRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        draft_payment_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextDraftPaymentRead
            Used to manage text notes.

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
            await client.note_text.read_note_text_for_user_monetary_account_draft_payment(
                user_id=1,
                monetary_account_id=1,
                draft_payment_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_text_for_user_monetary_account_draft_payment(
            user_id, monetary_account_id, draft_payment_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_text_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextDraftPaymentUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        draft_payment_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextDraftPaymentUpdate
            Used to manage text notes.

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
            await client.note_text.update_note_text_for_user_monetary_account_draft_payment(
                user_id=1,
                monetary_account_id=1,
                draft_payment_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_text_for_user_monetary_account_draft_payment(
            user_id, monetary_account_id, draft_payment_id, item_id, content=content, request_options=request_options
        )
        return _response.data

    async def delete_note_text_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextDraftPaymentDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        draft_payment_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextDraftPaymentDelete
            Used to manage text notes.

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
            await client.note_text.delete_note_text_for_user_monetary_account_draft_payment(
                user_id=1,
                monetary_account_id=1,
                draft_payment_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_text_for_user_monetary_account_draft_payment(
            user_id, monetary_account_id, draft_payment_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_text_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextIdealMerchantTransactionListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        ideal_merchant_transaction_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextIdealMerchantTransactionListing]
            Used to manage text notes.

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
            await client.note_text.list_all_note_text_for_user_monetary_account_ideal_merchant_transaction(
                user_id=1,
                monetary_account_id=1,
                ideal_merchant_transaction_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_note_text_for_user_monetary_account_ideal_merchant_transaction(
            user_id, monetary_account_id, ideal_merchant_transaction_id, request_options=request_options
        )
        return _response.data

    async def create_note_text_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextIdealMerchantTransactionCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        ideal_merchant_transaction_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextIdealMerchantTransactionCreate
            Used to manage text notes.

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
            await client.note_text.create_note_text_for_user_monetary_account_ideal_merchant_transaction(
                user_id=1,
                monetary_account_id=1,
                ideal_merchant_transaction_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_text_for_user_monetary_account_ideal_merchant_transaction(
            user_id,
            monetary_account_id,
            ideal_merchant_transaction_id,
            content=content,
            request_options=request_options,
        )
        return _response.data

    async def read_note_text_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextIdealMerchantTransactionRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        ideal_merchant_transaction_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextIdealMerchantTransactionRead
            Used to manage text notes.

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
            await client.note_text.read_note_text_for_user_monetary_account_ideal_merchant_transaction(
                user_id=1,
                monetary_account_id=1,
                ideal_merchant_transaction_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_text_for_user_monetary_account_ideal_merchant_transaction(
            user_id, monetary_account_id, ideal_merchant_transaction_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_text_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextIdealMerchantTransactionUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        ideal_merchant_transaction_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextIdealMerchantTransactionUpdate
            Used to manage text notes.

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
            await client.note_text.update_note_text_for_user_monetary_account_ideal_merchant_transaction(
                user_id=1,
                monetary_account_id=1,
                ideal_merchant_transaction_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_text_for_user_monetary_account_ideal_merchant_transaction(
            user_id,
            monetary_account_id,
            ideal_merchant_transaction_id,
            item_id,
            content=content,
            request_options=request_options,
        )
        return _response.data

    async def delete_note_text_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextIdealMerchantTransactionDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        ideal_merchant_transaction_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextIdealMerchantTransactionDelete
            Used to manage text notes.

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
            await client.note_text.delete_note_text_for_user_monetary_account_ideal_merchant_transaction(
                user_id=1,
                monetary_account_id=1,
                ideal_merchant_transaction_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_text_for_user_monetary_account_ideal_merchant_transaction(
            user_id, monetary_account_id, ideal_merchant_transaction_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_text_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextMasterCardActionListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        mastercard_action_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextMasterCardActionListing]
            Used to manage text notes.

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
            await client.note_text.list_all_note_text_for_user_monetary_account_mastercard_action(
                user_id=1,
                monetary_account_id=1,
                mastercard_action_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_note_text_for_user_monetary_account_mastercard_action(
            user_id, monetary_account_id, mastercard_action_id, request_options=request_options
        )
        return _response.data

    async def create_note_text_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextMasterCardActionCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        mastercard_action_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextMasterCardActionCreate
            Used to manage text notes.

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
            await client.note_text.create_note_text_for_user_monetary_account_mastercard_action(
                user_id=1,
                monetary_account_id=1,
                mastercard_action_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_text_for_user_monetary_account_mastercard_action(
            user_id, monetary_account_id, mastercard_action_id, content=content, request_options=request_options
        )
        return _response.data

    async def read_note_text_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextMasterCardActionRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        mastercard_action_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextMasterCardActionRead
            Used to manage text notes.

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
            await client.note_text.read_note_text_for_user_monetary_account_mastercard_action(
                user_id=1,
                monetary_account_id=1,
                mastercard_action_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_text_for_user_monetary_account_mastercard_action(
            user_id, monetary_account_id, mastercard_action_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_text_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextMasterCardActionUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        mastercard_action_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextMasterCardActionUpdate
            Used to manage text notes.

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
            await client.note_text.update_note_text_for_user_monetary_account_mastercard_action(
                user_id=1,
                monetary_account_id=1,
                mastercard_action_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_text_for_user_monetary_account_mastercard_action(
            user_id,
            monetary_account_id,
            mastercard_action_id,
            item_id,
            content=content,
            request_options=request_options,
        )
        return _response.data

    async def delete_note_text_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextMasterCardActionDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        mastercard_action_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextMasterCardActionDelete
            Used to manage text notes.

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
            await client.note_text.delete_note_text_for_user_monetary_account_mastercard_action(
                user_id=1,
                monetary_account_id=1,
                mastercard_action_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_text_for_user_monetary_account_mastercard_action(
            user_id, monetary_account_id, mastercard_action_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_text_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextPaymentBatchListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_batch_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextPaymentBatchListing]
            Used to manage text notes.

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
            await client.note_text.list_all_note_text_for_user_monetary_account_payment_batch(
                user_id=1,
                monetary_account_id=1,
                payment_batch_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_note_text_for_user_monetary_account_payment_batch(
            user_id, monetary_account_id, payment_batch_id, request_options=request_options
        )
        return _response.data

    async def create_note_text_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextPaymentBatchCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_batch_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextPaymentBatchCreate
            Used to manage text notes.

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
            await client.note_text.create_note_text_for_user_monetary_account_payment_batch(
                user_id=1,
                monetary_account_id=1,
                payment_batch_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_text_for_user_monetary_account_payment_batch(
            user_id, monetary_account_id, payment_batch_id, content=content, request_options=request_options
        )
        return _response.data

    async def read_note_text_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextPaymentBatchRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_batch_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextPaymentBatchRead
            Used to manage text notes.

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
            await client.note_text.read_note_text_for_user_monetary_account_payment_batch(
                user_id=1,
                monetary_account_id=1,
                payment_batch_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_text_for_user_monetary_account_payment_batch(
            user_id, monetary_account_id, payment_batch_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_text_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextPaymentBatchUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_batch_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextPaymentBatchUpdate
            Used to manage text notes.

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
            await client.note_text.update_note_text_for_user_monetary_account_payment_batch(
                user_id=1,
                monetary_account_id=1,
                payment_batch_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_text_for_user_monetary_account_payment_batch(
            user_id, monetary_account_id, payment_batch_id, item_id, content=content, request_options=request_options
        )
        return _response.data

    async def delete_note_text_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextPaymentBatchDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_batch_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextPaymentBatchDelete
            Used to manage text notes.

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
            await client.note_text.delete_note_text_for_user_monetary_account_payment_batch(
                user_id=1,
                monetary_account_id=1,
                payment_batch_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_text_for_user_monetary_account_payment_batch(
            user_id, monetary_account_id, payment_batch_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_text_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextPaymentListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextPaymentListing]
            Used to manage text notes.

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
            await client.note_text.list_all_note_text_for_user_monetary_account_payment(
                user_id=1,
                monetary_account_id=1,
                payment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_note_text_for_user_monetary_account_payment(
            user_id, monetary_account_id, payment_id, request_options=request_options
        )
        return _response.data

    async def create_note_text_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextPaymentCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextPaymentCreate
            Used to manage text notes.

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
            await client.note_text.create_note_text_for_user_monetary_account_payment(
                user_id=1,
                monetary_account_id=1,
                payment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_text_for_user_monetary_account_payment(
            user_id, monetary_account_id, payment_id, content=content, request_options=request_options
        )
        return _response.data

    async def read_note_text_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextPaymentRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextPaymentRead
            Used to manage text notes.

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
            await client.note_text.read_note_text_for_user_monetary_account_payment(
                user_id=1,
                monetary_account_id=1,
                payment_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_text_for_user_monetary_account_payment(
            user_id, monetary_account_id, payment_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_text_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextPaymentUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextPaymentUpdate
            Used to manage text notes.

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
            await client.note_text.update_note_text_for_user_monetary_account_payment(
                user_id=1,
                monetary_account_id=1,
                payment_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_text_for_user_monetary_account_payment(
            user_id, monetary_account_id, payment_id, item_id, content=content, request_options=request_options
        )
        return _response.data

    async def delete_note_text_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextPaymentDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextPaymentDelete
            Used to manage text notes.

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
            await client.note_text.delete_note_text_for_user_monetary_account_payment(
                user_id=1,
                monetary_account_id=1,
                payment_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_text_for_user_monetary_account_payment(
            user_id, monetary_account_id, payment_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_text_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextRequestInquiryBatchListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_batch_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextRequestInquiryBatchListing]
            Used to manage text notes.

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
            await client.note_text.list_all_note_text_for_user_monetary_account_request_inquiry_batch(
                user_id=1,
                monetary_account_id=1,
                request_inquiry_batch_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_note_text_for_user_monetary_account_request_inquiry_batch(
            user_id, monetary_account_id, request_inquiry_batch_id, request_options=request_options
        )
        return _response.data

    async def create_note_text_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextRequestInquiryBatchCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_batch_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextRequestInquiryBatchCreate
            Used to manage text notes.

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
            await client.note_text.create_note_text_for_user_monetary_account_request_inquiry_batch(
                user_id=1,
                monetary_account_id=1,
                request_inquiry_batch_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_text_for_user_monetary_account_request_inquiry_batch(
            user_id, monetary_account_id, request_inquiry_batch_id, content=content, request_options=request_options
        )
        return _response.data

    async def read_note_text_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextRequestInquiryBatchRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_batch_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextRequestInquiryBatchRead
            Used to manage text notes.

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
            await client.note_text.read_note_text_for_user_monetary_account_request_inquiry_batch(
                user_id=1,
                monetary_account_id=1,
                request_inquiry_batch_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_text_for_user_monetary_account_request_inquiry_batch(
            user_id, monetary_account_id, request_inquiry_batch_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_text_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextRequestInquiryBatchUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_batch_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextRequestInquiryBatchUpdate
            Used to manage text notes.

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
            await client.note_text.update_note_text_for_user_monetary_account_request_inquiry_batch(
                user_id=1,
                monetary_account_id=1,
                request_inquiry_batch_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_text_for_user_monetary_account_request_inquiry_batch(
            user_id,
            monetary_account_id,
            request_inquiry_batch_id,
            item_id,
            content=content,
            request_options=request_options,
        )
        return _response.data

    async def delete_note_text_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextRequestInquiryBatchDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_batch_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextRequestInquiryBatchDelete
            Used to manage text notes.

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
            await client.note_text.delete_note_text_for_user_monetary_account_request_inquiry_batch(
                user_id=1,
                monetary_account_id=1,
                request_inquiry_batch_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_text_for_user_monetary_account_request_inquiry_batch(
            user_id, monetary_account_id, request_inquiry_batch_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_text_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextRequestInquiryListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextRequestInquiryListing]
            Used to manage text notes.

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
            await client.note_text.list_all_note_text_for_user_monetary_account_request_inquiry(
                user_id=1,
                monetary_account_id=1,
                request_inquiry_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_note_text_for_user_monetary_account_request_inquiry(
            user_id, monetary_account_id, request_inquiry_id, request_options=request_options
        )
        return _response.data

    async def create_note_text_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextRequestInquiryCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextRequestInquiryCreate
            Used to manage text notes.

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
            await client.note_text.create_note_text_for_user_monetary_account_request_inquiry(
                user_id=1,
                monetary_account_id=1,
                request_inquiry_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_text_for_user_monetary_account_request_inquiry(
            user_id, monetary_account_id, request_inquiry_id, content=content, request_options=request_options
        )
        return _response.data

    async def read_note_text_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextRequestInquiryRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextRequestInquiryRead
            Used to manage text notes.

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
            await client.note_text.read_note_text_for_user_monetary_account_request_inquiry(
                user_id=1,
                monetary_account_id=1,
                request_inquiry_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_text_for_user_monetary_account_request_inquiry(
            user_id, monetary_account_id, request_inquiry_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_text_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextRequestInquiryUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextRequestInquiryUpdate
            Used to manage text notes.

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
            await client.note_text.update_note_text_for_user_monetary_account_request_inquiry(
                user_id=1,
                monetary_account_id=1,
                request_inquiry_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_text_for_user_monetary_account_request_inquiry(
            user_id, monetary_account_id, request_inquiry_id, item_id, content=content, request_options=request_options
        )
        return _response.data

    async def delete_note_text_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextRequestInquiryDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextRequestInquiryDelete
            Used to manage text notes.

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
            await client.note_text.delete_note_text_for_user_monetary_account_request_inquiry(
                user_id=1,
                monetary_account_id=1,
                request_inquiry_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_text_for_user_monetary_account_request_inquiry(
            user_id, monetary_account_id, request_inquiry_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_text_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextRequestResponseListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_response_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextRequestResponseListing]
            Used to manage text notes.

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
            await client.note_text.list_all_note_text_for_user_monetary_account_request_response(
                user_id=1,
                monetary_account_id=1,
                request_response_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_note_text_for_user_monetary_account_request_response(
            user_id, monetary_account_id, request_response_id, request_options=request_options
        )
        return _response.data

    async def create_note_text_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextRequestResponseCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_response_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextRequestResponseCreate
            Used to manage text notes.

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
            await client.note_text.create_note_text_for_user_monetary_account_request_response(
                user_id=1,
                monetary_account_id=1,
                request_response_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_text_for_user_monetary_account_request_response(
            user_id, monetary_account_id, request_response_id, content=content, request_options=request_options
        )
        return _response.data

    async def read_note_text_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextRequestResponseRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_response_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextRequestResponseRead
            Used to manage text notes.

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
            await client.note_text.read_note_text_for_user_monetary_account_request_response(
                user_id=1,
                monetary_account_id=1,
                request_response_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_text_for_user_monetary_account_request_response(
            user_id, monetary_account_id, request_response_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_text_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextRequestResponseUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_response_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextRequestResponseUpdate
            Used to manage text notes.

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
            await client.note_text.update_note_text_for_user_monetary_account_request_response(
                user_id=1,
                monetary_account_id=1,
                request_response_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_text_for_user_monetary_account_request_response(
            user_id, monetary_account_id, request_response_id, item_id, content=content, request_options=request_options
        )
        return _response.data

    async def delete_note_text_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextRequestResponseDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_response_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextRequestResponseDelete
            Used to manage text notes.

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
            await client.note_text.delete_note_text_for_user_monetary_account_request_response(
                user_id=1,
                monetary_account_id=1,
                request_response_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_text_for_user_monetary_account_request_response(
            user_id, monetary_account_id, request_response_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_text_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextSchedulePaymentBatchListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_batch_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextSchedulePaymentBatchListing]
            Used to manage text notes.

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
            await client.note_text.list_all_note_text_for_user_monetary_account_schedule_payment_batch(
                user_id=1,
                monetary_account_id=1,
                schedule_payment_batch_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_note_text_for_user_monetary_account_schedule_payment_batch(
            user_id, monetary_account_id, schedule_payment_batch_id, request_options=request_options
        )
        return _response.data

    async def create_note_text_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextSchedulePaymentBatchCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_batch_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextSchedulePaymentBatchCreate
            Used to manage text notes.

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
            await client.note_text.create_note_text_for_user_monetary_account_schedule_payment_batch(
                user_id=1,
                monetary_account_id=1,
                schedule_payment_batch_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_text_for_user_monetary_account_schedule_payment_batch(
            user_id, monetary_account_id, schedule_payment_batch_id, content=content, request_options=request_options
        )
        return _response.data

    async def read_note_text_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextSchedulePaymentBatchRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_batch_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextSchedulePaymentBatchRead
            Used to manage text notes.

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
            await client.note_text.read_note_text_for_user_monetary_account_schedule_payment_batch(
                user_id=1,
                monetary_account_id=1,
                schedule_payment_batch_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_text_for_user_monetary_account_schedule_payment_batch(
            user_id, monetary_account_id, schedule_payment_batch_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_text_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextSchedulePaymentBatchUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_batch_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextSchedulePaymentBatchUpdate
            Used to manage text notes.

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
            await client.note_text.update_note_text_for_user_monetary_account_schedule_payment_batch(
                user_id=1,
                monetary_account_id=1,
                schedule_payment_batch_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_text_for_user_monetary_account_schedule_payment_batch(
            user_id,
            monetary_account_id,
            schedule_payment_batch_id,
            item_id,
            content=content,
            request_options=request_options,
        )
        return _response.data

    async def delete_note_text_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextSchedulePaymentBatchDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_batch_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextSchedulePaymentBatchDelete
            Used to manage text notes.

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
            await client.note_text.delete_note_text_for_user_monetary_account_schedule_payment_batch(
                user_id=1,
                monetary_account_id=1,
                schedule_payment_batch_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_text_for_user_monetary_account_schedule_payment_batch(
            user_id, monetary_account_id, schedule_payment_batch_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_text_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextSchedulePaymentListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextSchedulePaymentListing]
            Used to manage text notes.

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
            await client.note_text.list_all_note_text_for_user_monetary_account_schedule_payment(
                user_id=1,
                monetary_account_id=1,
                schedule_payment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_note_text_for_user_monetary_account_schedule_payment(
            user_id, monetary_account_id, schedule_payment_id, request_options=request_options
        )
        return _response.data

    async def create_note_text_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextSchedulePaymentCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextSchedulePaymentCreate
            Used to manage text notes.

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
            await client.note_text.create_note_text_for_user_monetary_account_schedule_payment(
                user_id=1,
                monetary_account_id=1,
                schedule_payment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_text_for_user_monetary_account_schedule_payment(
            user_id, monetary_account_id, schedule_payment_id, content=content, request_options=request_options
        )
        return _response.data

    async def read_note_text_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextSchedulePaymentRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextSchedulePaymentRead
            Used to manage text notes.

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
            await client.note_text.read_note_text_for_user_monetary_account_schedule_payment(
                user_id=1,
                monetary_account_id=1,
                schedule_payment_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_text_for_user_monetary_account_schedule_payment(
            user_id, monetary_account_id, schedule_payment_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_text_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextSchedulePaymentUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextSchedulePaymentUpdate
            Used to manage text notes.

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
            await client.note_text.update_note_text_for_user_monetary_account_schedule_payment(
                user_id=1,
                monetary_account_id=1,
                schedule_payment_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_text_for_user_monetary_account_schedule_payment(
            user_id, monetary_account_id, schedule_payment_id, item_id, content=content, request_options=request_options
        )
        return _response.data

    async def delete_note_text_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextSchedulePaymentDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextSchedulePaymentDelete
            Used to manage text notes.

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
            await client.note_text.delete_note_text_for_user_monetary_account_schedule_payment(
                user_id=1,
                monetary_account_id=1,
                schedule_payment_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_text_for_user_monetary_account_schedule_payment(
            user_id, monetary_account_id, schedule_payment_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_text_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextScheduleInstanceListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_id : int


        schedule_instance_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextScheduleInstanceListing]
            Used to manage text notes.

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
            await client.note_text.list_all_note_text_for_user_monetary_account_schedule_schedule_instance(
                user_id=1,
                monetary_account_id=1,
                schedule_id=1,
                schedule_instance_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_note_text_for_user_monetary_account_schedule_schedule_instance(
            user_id, monetary_account_id, schedule_id, schedule_instance_id, request_options=request_options
        )
        return _response.data

    async def create_note_text_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextScheduleInstanceCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_id : int


        schedule_instance_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextScheduleInstanceCreate
            Used to manage text notes.

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
            await client.note_text.create_note_text_for_user_monetary_account_schedule_schedule_instance(
                user_id=1,
                monetary_account_id=1,
                schedule_id=1,
                schedule_instance_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_text_for_user_monetary_account_schedule_schedule_instance(
            user_id,
            monetary_account_id,
            schedule_id,
            schedule_instance_id,
            content=content,
            request_options=request_options,
        )
        return _response.data

    async def read_note_text_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextScheduleInstanceRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_id : int


        schedule_instance_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextScheduleInstanceRead
            Used to manage text notes.

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
            await client.note_text.read_note_text_for_user_monetary_account_schedule_schedule_instance(
                user_id=1,
                monetary_account_id=1,
                schedule_id=1,
                schedule_instance_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_text_for_user_monetary_account_schedule_schedule_instance(
            user_id, monetary_account_id, schedule_id, schedule_instance_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_text_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextScheduleInstanceUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_id : int


        schedule_instance_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextScheduleInstanceUpdate
            Used to manage text notes.

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
            await client.note_text.update_note_text_for_user_monetary_account_schedule_schedule_instance(
                user_id=1,
                monetary_account_id=1,
                schedule_id=1,
                schedule_instance_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_text_for_user_monetary_account_schedule_schedule_instance(
            user_id,
            monetary_account_id,
            schedule_id,
            schedule_instance_id,
            item_id,
            content=content,
            request_options=request_options,
        )
        return _response.data

    async def delete_note_text_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextScheduleInstanceDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_id : int


        schedule_instance_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextScheduleInstanceDelete
            Used to manage text notes.

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
            await client.note_text.delete_note_text_for_user_monetary_account_schedule_schedule_instance(
                user_id=1,
                monetary_account_id=1,
                schedule_id=1,
                schedule_instance_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_text_for_user_monetary_account_schedule_schedule_instance(
            user_id, monetary_account_id, schedule_id, schedule_instance_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_text_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextSofortMerchantTransactionListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        sofort_merchant_transaction_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextSofortMerchantTransactionListing]
            Used to manage text notes.

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
            await client.note_text.list_all_note_text_for_user_monetary_account_sofort_merchant_transaction(
                user_id=1,
                monetary_account_id=1,
                sofort_merchant_transaction_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_note_text_for_user_monetary_account_sofort_merchant_transaction(
            user_id, monetary_account_id, sofort_merchant_transaction_id, request_options=request_options
        )
        return _response.data

    async def create_note_text_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextSofortMerchantTransactionCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        sofort_merchant_transaction_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextSofortMerchantTransactionCreate
            Used to manage text notes.

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
            await client.note_text.create_note_text_for_user_monetary_account_sofort_merchant_transaction(
                user_id=1,
                monetary_account_id=1,
                sofort_merchant_transaction_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_text_for_user_monetary_account_sofort_merchant_transaction(
            user_id,
            monetary_account_id,
            sofort_merchant_transaction_id,
            content=content,
            request_options=request_options,
        )
        return _response.data

    async def read_note_text_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextSofortMerchantTransactionRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        sofort_merchant_transaction_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextSofortMerchantTransactionRead
            Used to manage text notes.

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
            await client.note_text.read_note_text_for_user_monetary_account_sofort_merchant_transaction(
                user_id=1,
                monetary_account_id=1,
                sofort_merchant_transaction_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_text_for_user_monetary_account_sofort_merchant_transaction(
            user_id, monetary_account_id, sofort_merchant_transaction_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_text_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextSofortMerchantTransactionUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        sofort_merchant_transaction_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextSofortMerchantTransactionUpdate
            Used to manage text notes.

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
            await client.note_text.update_note_text_for_user_monetary_account_sofort_merchant_transaction(
                user_id=1,
                monetary_account_id=1,
                sofort_merchant_transaction_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_text_for_user_monetary_account_sofort_merchant_transaction(
            user_id,
            monetary_account_id,
            sofort_merchant_transaction_id,
            item_id,
            content=content,
            request_options=request_options,
        )
        return _response.data

    async def delete_note_text_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextSofortMerchantTransactionDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        sofort_merchant_transaction_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextSofortMerchantTransactionDelete
            Used to manage text notes.

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
            await client.note_text.delete_note_text_for_user_monetary_account_sofort_merchant_transaction(
                user_id=1,
                monetary_account_id=1,
                sofort_merchant_transaction_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_text_for_user_monetary_account_sofort_merchant_transaction(
            user_id, monetary_account_id, sofort_merchant_transaction_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_text_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextBankSwitchServiceNetherlandsIncomingPaymentListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        switch_service_payment_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextBankSwitchServiceNetherlandsIncomingPaymentListing]
            Used to manage text notes.

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
            await client.note_text.list_all_note_text_for_user_monetary_account_switch_service_payment(
                user_id=1,
                monetary_account_id=1,
                switch_service_payment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_note_text_for_user_monetary_account_switch_service_payment(
            user_id, monetary_account_id, switch_service_payment_id, request_options=request_options
        )
        return _response.data

    async def create_note_text_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextBankSwitchServiceNetherlandsIncomingPaymentCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        switch_service_payment_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextBankSwitchServiceNetherlandsIncomingPaymentCreate
            Used to manage text notes.

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
            await client.note_text.create_note_text_for_user_monetary_account_switch_service_payment(
                user_id=1,
                monetary_account_id=1,
                switch_service_payment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_text_for_user_monetary_account_switch_service_payment(
            user_id, monetary_account_id, switch_service_payment_id, content=content, request_options=request_options
        )
        return _response.data

    async def read_note_text_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextBankSwitchServiceNetherlandsIncomingPaymentRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        switch_service_payment_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextBankSwitchServiceNetherlandsIncomingPaymentRead
            Used to manage text notes.

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
            await client.note_text.read_note_text_for_user_monetary_account_switch_service_payment(
                user_id=1,
                monetary_account_id=1,
                switch_service_payment_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_text_for_user_monetary_account_switch_service_payment(
            user_id, monetary_account_id, switch_service_payment_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_text_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextBankSwitchServiceNetherlandsIncomingPaymentUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        switch_service_payment_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextBankSwitchServiceNetherlandsIncomingPaymentUpdate
            Used to manage text notes.

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
            await client.note_text.update_note_text_for_user_monetary_account_switch_service_payment(
                user_id=1,
                monetary_account_id=1,
                switch_service_payment_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_text_for_user_monetary_account_switch_service_payment(
            user_id,
            monetary_account_id,
            switch_service_payment_id,
            item_id,
            content=content,
            request_options=request_options,
        )
        return _response.data

    async def delete_note_text_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextBankSwitchServiceNetherlandsIncomingPaymentDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        switch_service_payment_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextBankSwitchServiceNetherlandsIncomingPaymentDelete
            Used to manage text notes.

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
            await client.note_text.delete_note_text_for_user_monetary_account_switch_service_payment(
                user_id=1,
                monetary_account_id=1,
                switch_service_payment_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_text_for_user_monetary_account_switch_service_payment(
            user_id, monetary_account_id, switch_service_payment_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_text_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteTextWhitelistResultListing]:
        """
        Manage the notes for a given user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        whitelist_id : int


        whitelist_result_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteTextWhitelistResultListing]
            Used to manage text notes.

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
            await client.note_text.list_all_note_text_for_user_monetary_account_whitelist_whitelist_result(
                user_id=1,
                monetary_account_id=1,
                whitelist_id=1,
                whitelist_result_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_note_text_for_user_monetary_account_whitelist_whitelist_result(
            user_id, monetary_account_id, whitelist_id, whitelist_result_id, request_options=request_options
        )
        return _response.data

    async def create_note_text_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextWhitelistResultCreate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        whitelist_id : int


        whitelist_result_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextWhitelistResultCreate
            Used to manage text notes.

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
            await client.note_text.create_note_text_for_user_monetary_account_whitelist_whitelist_result(
                user_id=1,
                monetary_account_id=1,
                whitelist_id=1,
                whitelist_result_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_text_for_user_monetary_account_whitelist_whitelist_result(
            user_id,
            monetary_account_id,
            whitelist_id,
            whitelist_result_id,
            content=content,
            request_options=request_options,
        )
        return _response.data

    async def read_note_text_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextWhitelistResultRead:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        whitelist_id : int


        whitelist_result_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextWhitelistResultRead
            Used to manage text notes.

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
            await client.note_text.read_note_text_for_user_monetary_account_whitelist_whitelist_result(
                user_id=1,
                monetary_account_id=1,
                whitelist_id=1,
                whitelist_result_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_text_for_user_monetary_account_whitelist_whitelist_result(
            user_id, monetary_account_id, whitelist_id, whitelist_result_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_text_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextWhitelistResultUpdate:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        whitelist_id : int


        whitelist_result_id : int


        item_id : int


        content : typing.Optional[str]
            The content of the note.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextWhitelistResultUpdate
            Used to manage text notes.

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
            await client.note_text.update_note_text_for_user_monetary_account_whitelist_whitelist_result(
                user_id=1,
                monetary_account_id=1,
                whitelist_id=1,
                whitelist_result_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_text_for_user_monetary_account_whitelist_whitelist_result(
            user_id,
            monetary_account_id,
            whitelist_id,
            whitelist_result_id,
            item_id,
            content=content,
            request_options=request_options,
        )
        return _response.data

    async def delete_note_text_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteTextWhitelistResultDelete:
        """
        Used to manage text notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        whitelist_id : int


        whitelist_result_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteTextWhitelistResultDelete
            Used to manage text notes.

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
            await client.note_text.delete_note_text_for_user_monetary_account_whitelist_whitelist_result(
                user_id=1,
                monetary_account_id=1,
                whitelist_id=1,
                whitelist_result_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_text_for_user_monetary_account_whitelist_whitelist_result(
            user_id, monetary_account_id, whitelist_id, whitelist_result_id, item_id, request_options=request_options
        )
        return _response.data
