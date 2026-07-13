

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.note_attachment_bank_switch_service_netherlands_incoming_payment_create import (
    NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentCreate,
)
from ..types.note_attachment_bank_switch_service_netherlands_incoming_payment_delete import (
    NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentDelete,
)
from ..types.note_attachment_bank_switch_service_netherlands_incoming_payment_listing import (
    NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentListing,
)
from ..types.note_attachment_bank_switch_service_netherlands_incoming_payment_read import (
    NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentRead,
)
from ..types.note_attachment_bank_switch_service_netherlands_incoming_payment_update import (
    NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentUpdate,
)
from ..types.note_attachment_bunq_me_fundraiser_result_create import NoteAttachmentBunqMeFundraiserResultCreate
from ..types.note_attachment_bunq_me_fundraiser_result_delete import NoteAttachmentBunqMeFundraiserResultDelete
from ..types.note_attachment_bunq_me_fundraiser_result_listing import NoteAttachmentBunqMeFundraiserResultListing
from ..types.note_attachment_bunq_me_fundraiser_result_read import NoteAttachmentBunqMeFundraiserResultRead
from ..types.note_attachment_bunq_me_fundraiser_result_update import NoteAttachmentBunqMeFundraiserResultUpdate
from ..types.note_attachment_draft_payment_create import NoteAttachmentDraftPaymentCreate
from ..types.note_attachment_draft_payment_delete import NoteAttachmentDraftPaymentDelete
from ..types.note_attachment_draft_payment_listing import NoteAttachmentDraftPaymentListing
from ..types.note_attachment_draft_payment_read import NoteAttachmentDraftPaymentRead
from ..types.note_attachment_draft_payment_update import NoteAttachmentDraftPaymentUpdate
from ..types.note_attachment_ideal_merchant_transaction_create import NoteAttachmentIdealMerchantTransactionCreate
from ..types.note_attachment_ideal_merchant_transaction_delete import NoteAttachmentIdealMerchantTransactionDelete
from ..types.note_attachment_ideal_merchant_transaction_listing import NoteAttachmentIdealMerchantTransactionListing
from ..types.note_attachment_ideal_merchant_transaction_read import NoteAttachmentIdealMerchantTransactionRead
from ..types.note_attachment_ideal_merchant_transaction_update import NoteAttachmentIdealMerchantTransactionUpdate
from ..types.note_attachment_master_card_action_create import NoteAttachmentMasterCardActionCreate
from ..types.note_attachment_master_card_action_delete import NoteAttachmentMasterCardActionDelete
from ..types.note_attachment_master_card_action_listing import NoteAttachmentMasterCardActionListing
from ..types.note_attachment_master_card_action_read import NoteAttachmentMasterCardActionRead
from ..types.note_attachment_master_card_action_update import NoteAttachmentMasterCardActionUpdate
from ..types.note_attachment_payment_batch_create import NoteAttachmentPaymentBatchCreate
from ..types.note_attachment_payment_batch_delete import NoteAttachmentPaymentBatchDelete
from ..types.note_attachment_payment_batch_listing import NoteAttachmentPaymentBatchListing
from ..types.note_attachment_payment_batch_read import NoteAttachmentPaymentBatchRead
from ..types.note_attachment_payment_batch_update import NoteAttachmentPaymentBatchUpdate
from ..types.note_attachment_payment_create import NoteAttachmentPaymentCreate
from ..types.note_attachment_payment_delete import NoteAttachmentPaymentDelete
from ..types.note_attachment_payment_listing import NoteAttachmentPaymentListing
from ..types.note_attachment_payment_read import NoteAttachmentPaymentRead
from ..types.note_attachment_payment_update import NoteAttachmentPaymentUpdate
from ..types.note_attachment_request_inquiry_batch_create import NoteAttachmentRequestInquiryBatchCreate
from ..types.note_attachment_request_inquiry_batch_delete import NoteAttachmentRequestInquiryBatchDelete
from ..types.note_attachment_request_inquiry_batch_listing import NoteAttachmentRequestInquiryBatchListing
from ..types.note_attachment_request_inquiry_batch_read import NoteAttachmentRequestInquiryBatchRead
from ..types.note_attachment_request_inquiry_batch_update import NoteAttachmentRequestInquiryBatchUpdate
from ..types.note_attachment_request_inquiry_create import NoteAttachmentRequestInquiryCreate
from ..types.note_attachment_request_inquiry_delete import NoteAttachmentRequestInquiryDelete
from ..types.note_attachment_request_inquiry_listing import NoteAttachmentRequestInquiryListing
from ..types.note_attachment_request_inquiry_read import NoteAttachmentRequestInquiryRead
from ..types.note_attachment_request_inquiry_update import NoteAttachmentRequestInquiryUpdate
from ..types.note_attachment_request_response_create import NoteAttachmentRequestResponseCreate
from ..types.note_attachment_request_response_delete import NoteAttachmentRequestResponseDelete
from ..types.note_attachment_request_response_listing import NoteAttachmentRequestResponseListing
from ..types.note_attachment_request_response_read import NoteAttachmentRequestResponseRead
from ..types.note_attachment_request_response_update import NoteAttachmentRequestResponseUpdate
from ..types.note_attachment_schedule_instance_create import NoteAttachmentScheduleInstanceCreate
from ..types.note_attachment_schedule_instance_delete import NoteAttachmentScheduleInstanceDelete
from ..types.note_attachment_schedule_instance_listing import NoteAttachmentScheduleInstanceListing
from ..types.note_attachment_schedule_instance_read import NoteAttachmentScheduleInstanceRead
from ..types.note_attachment_schedule_instance_update import NoteAttachmentScheduleInstanceUpdate
from ..types.note_attachment_schedule_payment_batch_create import NoteAttachmentSchedulePaymentBatchCreate
from ..types.note_attachment_schedule_payment_batch_delete import NoteAttachmentSchedulePaymentBatchDelete
from ..types.note_attachment_schedule_payment_batch_listing import NoteAttachmentSchedulePaymentBatchListing
from ..types.note_attachment_schedule_payment_batch_read import NoteAttachmentSchedulePaymentBatchRead
from ..types.note_attachment_schedule_payment_batch_update import NoteAttachmentSchedulePaymentBatchUpdate
from ..types.note_attachment_schedule_payment_create import NoteAttachmentSchedulePaymentCreate
from ..types.note_attachment_schedule_payment_delete import NoteAttachmentSchedulePaymentDelete
from ..types.note_attachment_schedule_payment_listing import NoteAttachmentSchedulePaymentListing
from ..types.note_attachment_schedule_payment_read import NoteAttachmentSchedulePaymentRead
from ..types.note_attachment_schedule_payment_update import NoteAttachmentSchedulePaymentUpdate
from ..types.note_attachment_sofort_merchant_transaction_create import NoteAttachmentSofortMerchantTransactionCreate
from ..types.note_attachment_sofort_merchant_transaction_delete import NoteAttachmentSofortMerchantTransactionDelete
from ..types.note_attachment_sofort_merchant_transaction_listing import NoteAttachmentSofortMerchantTransactionListing
from ..types.note_attachment_sofort_merchant_transaction_read import NoteAttachmentSofortMerchantTransactionRead
from ..types.note_attachment_sofort_merchant_transaction_update import NoteAttachmentSofortMerchantTransactionUpdate
from ..types.note_attachment_whitelist_result_create import NoteAttachmentWhitelistResultCreate
from ..types.note_attachment_whitelist_result_delete import NoteAttachmentWhitelistResultDelete
from ..types.note_attachment_whitelist_result_listing import NoteAttachmentWhitelistResultListing
from ..types.note_attachment_whitelist_result_read import NoteAttachmentWhitelistResultRead
from ..types.note_attachment_whitelist_result_update import NoteAttachmentWhitelistResultUpdate
from .raw_client import AsyncRawNoteAttachmentClient, RawNoteAttachmentClient


OMIT = typing.cast(typing.Any, ...)


class NoteAttachmentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNoteAttachmentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNoteAttachmentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNoteAttachmentClient
        """
        return self._raw_client

    def list_all_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentBunqMeFundraiserResultListing]:
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
        typing.List[NoteAttachmentBunqMeFundraiserResultListing]
            Used to manage attachment notes.

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
        client.note_attachment.list_all_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
            user_id=1,
            monetary_account_id=1,
            bunqme_fundraiser_result_id=1,
        )
        """
        _response = self._raw_client.list_all_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
            user_id, monetary_account_id, bunqme_fundraiser_result_id, request_options=request_options
        )
        return _response.data

    def create_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentBunqMeFundraiserResultCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        bunqme_fundraiser_result_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentBunqMeFundraiserResultCreate
            Used to manage attachment notes.

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
        client.note_attachment.create_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
            user_id=1,
            monetary_account_id=1,
            bunqme_fundraiser_result_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.create_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
            user_id,
            monetary_account_id,
            bunqme_fundraiser_result_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def read_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentBunqMeFundraiserResultRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentBunqMeFundraiserResultRead
            Used to manage attachment notes.

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
        client.note_attachment.read_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
            user_id=1,
            monetary_account_id=1,
            bunqme_fundraiser_result_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
            user_id, monetary_account_id, bunqme_fundraiser_result_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentBunqMeFundraiserResultUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        bunqme_fundraiser_result_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentBunqMeFundraiserResultUpdate
            Used to manage attachment notes.

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
        client.note_attachment.update_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
            user_id=1,
            monetary_account_id=1,
            bunqme_fundraiser_result_id=1,
            item_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.update_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
            user_id,
            monetary_account_id,
            bunqme_fundraiser_result_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def delete_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentBunqMeFundraiserResultDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentBunqMeFundraiserResultDelete
            Used to manage attachment notes.

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
        client.note_attachment.delete_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
            user_id=1,
            monetary_account_id=1,
            bunqme_fundraiser_result_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
            user_id, monetary_account_id, bunqme_fundraiser_result_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_attachment_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentDraftPaymentListing]:
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
        typing.List[NoteAttachmentDraftPaymentListing]
            Used to manage attachment notes.

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
        client.note_attachment.list_all_note_attachment_for_user_monetary_account_draft_payment(
            user_id=1,
            monetary_account_id=1,
            draft_payment_id=1,
        )
        """
        _response = self._raw_client.list_all_note_attachment_for_user_monetary_account_draft_payment(
            user_id, monetary_account_id, draft_payment_id, request_options=request_options
        )
        return _response.data

    def create_note_attachment_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentDraftPaymentCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        draft_payment_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentDraftPaymentCreate
            Used to manage attachment notes.

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
        client.note_attachment.create_note_attachment_for_user_monetary_account_draft_payment(
            user_id=1,
            monetary_account_id=1,
            draft_payment_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.create_note_attachment_for_user_monetary_account_draft_payment(
            user_id,
            monetary_account_id,
            draft_payment_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def read_note_attachment_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentDraftPaymentRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentDraftPaymentRead
            Used to manage attachment notes.

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
        client.note_attachment.read_note_attachment_for_user_monetary_account_draft_payment(
            user_id=1,
            monetary_account_id=1,
            draft_payment_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_attachment_for_user_monetary_account_draft_payment(
            user_id, monetary_account_id, draft_payment_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_attachment_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentDraftPaymentUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        draft_payment_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentDraftPaymentUpdate
            Used to manage attachment notes.

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
        client.note_attachment.update_note_attachment_for_user_monetary_account_draft_payment(
            user_id=1,
            monetary_account_id=1,
            draft_payment_id=1,
            item_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.update_note_attachment_for_user_monetary_account_draft_payment(
            user_id,
            monetary_account_id,
            draft_payment_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def delete_note_attachment_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentDraftPaymentDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentDraftPaymentDelete
            Used to manage attachment notes.

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
        client.note_attachment.delete_note_attachment_for_user_monetary_account_draft_payment(
            user_id=1,
            monetary_account_id=1,
            draft_payment_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_attachment_for_user_monetary_account_draft_payment(
            user_id, monetary_account_id, draft_payment_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentIdealMerchantTransactionListing]:
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
        typing.List[NoteAttachmentIdealMerchantTransactionListing]
            Used to manage attachment notes.

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
        client.note_attachment.list_all_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
            user_id=1,
            monetary_account_id=1,
            ideal_merchant_transaction_id=1,
        )
        """
        _response = self._raw_client.list_all_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
            user_id, monetary_account_id, ideal_merchant_transaction_id, request_options=request_options
        )
        return _response.data

    def create_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentIdealMerchantTransactionCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        ideal_merchant_transaction_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentIdealMerchantTransactionCreate
            Used to manage attachment notes.

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
        client.note_attachment.create_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
            user_id=1,
            monetary_account_id=1,
            ideal_merchant_transaction_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.create_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
            user_id,
            monetary_account_id,
            ideal_merchant_transaction_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def read_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentIdealMerchantTransactionRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentIdealMerchantTransactionRead
            Used to manage attachment notes.

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
        client.note_attachment.read_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
            user_id=1,
            monetary_account_id=1,
            ideal_merchant_transaction_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
            user_id, monetary_account_id, ideal_merchant_transaction_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentIdealMerchantTransactionUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        ideal_merchant_transaction_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentIdealMerchantTransactionUpdate
            Used to manage attachment notes.

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
        client.note_attachment.update_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
            user_id=1,
            monetary_account_id=1,
            ideal_merchant_transaction_id=1,
            item_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.update_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
            user_id,
            monetary_account_id,
            ideal_merchant_transaction_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def delete_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentIdealMerchantTransactionDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentIdealMerchantTransactionDelete
            Used to manage attachment notes.

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
        client.note_attachment.delete_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
            user_id=1,
            monetary_account_id=1,
            ideal_merchant_transaction_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
            user_id, monetary_account_id, ideal_merchant_transaction_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_attachment_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentMasterCardActionListing]:
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
        typing.List[NoteAttachmentMasterCardActionListing]
            Used to manage attachment notes.

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
        client.note_attachment.list_all_note_attachment_for_user_monetary_account_mastercard_action(
            user_id=1,
            monetary_account_id=1,
            mastercard_action_id=1,
        )
        """
        _response = self._raw_client.list_all_note_attachment_for_user_monetary_account_mastercard_action(
            user_id, monetary_account_id, mastercard_action_id, request_options=request_options
        )
        return _response.data

    def create_note_attachment_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentMasterCardActionCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        mastercard_action_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentMasterCardActionCreate
            Used to manage attachment notes.

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
        client.note_attachment.create_note_attachment_for_user_monetary_account_mastercard_action(
            user_id=1,
            monetary_account_id=1,
            mastercard_action_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.create_note_attachment_for_user_monetary_account_mastercard_action(
            user_id,
            monetary_account_id,
            mastercard_action_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def read_note_attachment_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentMasterCardActionRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentMasterCardActionRead
            Used to manage attachment notes.

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
        client.note_attachment.read_note_attachment_for_user_monetary_account_mastercard_action(
            user_id=1,
            monetary_account_id=1,
            mastercard_action_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_attachment_for_user_monetary_account_mastercard_action(
            user_id, monetary_account_id, mastercard_action_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_attachment_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentMasterCardActionUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        mastercard_action_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentMasterCardActionUpdate
            Used to manage attachment notes.

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
        client.note_attachment.update_note_attachment_for_user_monetary_account_mastercard_action(
            user_id=1,
            monetary_account_id=1,
            mastercard_action_id=1,
            item_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.update_note_attachment_for_user_monetary_account_mastercard_action(
            user_id,
            monetary_account_id,
            mastercard_action_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def delete_note_attachment_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentMasterCardActionDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentMasterCardActionDelete
            Used to manage attachment notes.

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
        client.note_attachment.delete_note_attachment_for_user_monetary_account_mastercard_action(
            user_id=1,
            monetary_account_id=1,
            mastercard_action_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_attachment_for_user_monetary_account_mastercard_action(
            user_id, monetary_account_id, mastercard_action_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_attachment_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentPaymentBatchListing]:
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
        typing.List[NoteAttachmentPaymentBatchListing]
            Used to manage attachment notes.

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
        client.note_attachment.list_all_note_attachment_for_user_monetary_account_payment_batch(
            user_id=1,
            monetary_account_id=1,
            payment_batch_id=1,
        )
        """
        _response = self._raw_client.list_all_note_attachment_for_user_monetary_account_payment_batch(
            user_id, monetary_account_id, payment_batch_id, request_options=request_options
        )
        return _response.data

    def create_note_attachment_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentPaymentBatchCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_batch_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentPaymentBatchCreate
            Used to manage attachment notes.

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
        client.note_attachment.create_note_attachment_for_user_monetary_account_payment_batch(
            user_id=1,
            monetary_account_id=1,
            payment_batch_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.create_note_attachment_for_user_monetary_account_payment_batch(
            user_id,
            monetary_account_id,
            payment_batch_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def read_note_attachment_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentPaymentBatchRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentPaymentBatchRead
            Used to manage attachment notes.

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
        client.note_attachment.read_note_attachment_for_user_monetary_account_payment_batch(
            user_id=1,
            monetary_account_id=1,
            payment_batch_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_attachment_for_user_monetary_account_payment_batch(
            user_id, monetary_account_id, payment_batch_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_attachment_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentPaymentBatchUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_batch_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentPaymentBatchUpdate
            Used to manage attachment notes.

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
        client.note_attachment.update_note_attachment_for_user_monetary_account_payment_batch(
            user_id=1,
            monetary_account_id=1,
            payment_batch_id=1,
            item_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.update_note_attachment_for_user_monetary_account_payment_batch(
            user_id,
            monetary_account_id,
            payment_batch_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def delete_note_attachment_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentPaymentBatchDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentPaymentBatchDelete
            Used to manage attachment notes.

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
        client.note_attachment.delete_note_attachment_for_user_monetary_account_payment_batch(
            user_id=1,
            monetary_account_id=1,
            payment_batch_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_attachment_for_user_monetary_account_payment_batch(
            user_id, monetary_account_id, payment_batch_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_attachment_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentPaymentListing]:
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
        typing.List[NoteAttachmentPaymentListing]
            Used to manage attachment notes.

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
        client.note_attachment.list_all_note_attachment_for_user_monetary_account_payment(
            user_id=1,
            monetary_account_id=1,
            payment_id=1,
        )
        """
        _response = self._raw_client.list_all_note_attachment_for_user_monetary_account_payment(
            user_id, monetary_account_id, payment_id, request_options=request_options
        )
        return _response.data

    def create_note_attachment_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentPaymentCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentPaymentCreate
            Used to manage attachment notes.

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
        client.note_attachment.create_note_attachment_for_user_monetary_account_payment(
            user_id=1,
            monetary_account_id=1,
            payment_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.create_note_attachment_for_user_monetary_account_payment(
            user_id,
            monetary_account_id,
            payment_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def read_note_attachment_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentPaymentRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentPaymentRead
            Used to manage attachment notes.

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
        client.note_attachment.read_note_attachment_for_user_monetary_account_payment(
            user_id=1,
            monetary_account_id=1,
            payment_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_attachment_for_user_monetary_account_payment(
            user_id, monetary_account_id, payment_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_attachment_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentPaymentUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentPaymentUpdate
            Used to manage attachment notes.

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
        client.note_attachment.update_note_attachment_for_user_monetary_account_payment(
            user_id=1,
            monetary_account_id=1,
            payment_id=1,
            item_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.update_note_attachment_for_user_monetary_account_payment(
            user_id,
            monetary_account_id,
            payment_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def delete_note_attachment_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentPaymentDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentPaymentDelete
            Used to manage attachment notes.

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
        client.note_attachment.delete_note_attachment_for_user_monetary_account_payment(
            user_id=1,
            monetary_account_id=1,
            payment_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_attachment_for_user_monetary_account_payment(
            user_id, monetary_account_id, payment_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_attachment_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentRequestInquiryBatchListing]:
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
        typing.List[NoteAttachmentRequestInquiryBatchListing]
            Used to manage attachment notes.

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
        client.note_attachment.list_all_note_attachment_for_user_monetary_account_request_inquiry_batch(
            user_id=1,
            monetary_account_id=1,
            request_inquiry_batch_id=1,
        )
        """
        _response = self._raw_client.list_all_note_attachment_for_user_monetary_account_request_inquiry_batch(
            user_id, monetary_account_id, request_inquiry_batch_id, request_options=request_options
        )
        return _response.data

    def create_note_attachment_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentRequestInquiryBatchCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_batch_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentRequestInquiryBatchCreate
            Used to manage attachment notes.

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
        client.note_attachment.create_note_attachment_for_user_monetary_account_request_inquiry_batch(
            user_id=1,
            monetary_account_id=1,
            request_inquiry_batch_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.create_note_attachment_for_user_monetary_account_request_inquiry_batch(
            user_id,
            monetary_account_id,
            request_inquiry_batch_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def read_note_attachment_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentRequestInquiryBatchRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentRequestInquiryBatchRead
            Used to manage attachment notes.

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
        client.note_attachment.read_note_attachment_for_user_monetary_account_request_inquiry_batch(
            user_id=1,
            monetary_account_id=1,
            request_inquiry_batch_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_attachment_for_user_monetary_account_request_inquiry_batch(
            user_id, monetary_account_id, request_inquiry_batch_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_attachment_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentRequestInquiryBatchUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_batch_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentRequestInquiryBatchUpdate
            Used to manage attachment notes.

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
        client.note_attachment.update_note_attachment_for_user_monetary_account_request_inquiry_batch(
            user_id=1,
            monetary_account_id=1,
            request_inquiry_batch_id=1,
            item_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.update_note_attachment_for_user_monetary_account_request_inquiry_batch(
            user_id,
            monetary_account_id,
            request_inquiry_batch_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def delete_note_attachment_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentRequestInquiryBatchDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentRequestInquiryBatchDelete
            Used to manage attachment notes.

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
        client.note_attachment.delete_note_attachment_for_user_monetary_account_request_inquiry_batch(
            user_id=1,
            monetary_account_id=1,
            request_inquiry_batch_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_attachment_for_user_monetary_account_request_inquiry_batch(
            user_id, monetary_account_id, request_inquiry_batch_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_attachment_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentRequestInquiryListing]:
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
        typing.List[NoteAttachmentRequestInquiryListing]
            Used to manage attachment notes.

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
        client.note_attachment.list_all_note_attachment_for_user_monetary_account_request_inquiry(
            user_id=1,
            monetary_account_id=1,
            request_inquiry_id=1,
        )
        """
        _response = self._raw_client.list_all_note_attachment_for_user_monetary_account_request_inquiry(
            user_id, monetary_account_id, request_inquiry_id, request_options=request_options
        )
        return _response.data

    def create_note_attachment_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentRequestInquiryCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentRequestInquiryCreate
            Used to manage attachment notes.

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
        client.note_attachment.create_note_attachment_for_user_monetary_account_request_inquiry(
            user_id=1,
            monetary_account_id=1,
            request_inquiry_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.create_note_attachment_for_user_monetary_account_request_inquiry(
            user_id,
            monetary_account_id,
            request_inquiry_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def read_note_attachment_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentRequestInquiryRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentRequestInquiryRead
            Used to manage attachment notes.

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
        client.note_attachment.read_note_attachment_for_user_monetary_account_request_inquiry(
            user_id=1,
            monetary_account_id=1,
            request_inquiry_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_attachment_for_user_monetary_account_request_inquiry(
            user_id, monetary_account_id, request_inquiry_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_attachment_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentRequestInquiryUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentRequestInquiryUpdate
            Used to manage attachment notes.

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
        client.note_attachment.update_note_attachment_for_user_monetary_account_request_inquiry(
            user_id=1,
            monetary_account_id=1,
            request_inquiry_id=1,
            item_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.update_note_attachment_for_user_monetary_account_request_inquiry(
            user_id,
            monetary_account_id,
            request_inquiry_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def delete_note_attachment_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentRequestInquiryDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentRequestInquiryDelete
            Used to manage attachment notes.

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
        client.note_attachment.delete_note_attachment_for_user_monetary_account_request_inquiry(
            user_id=1,
            monetary_account_id=1,
            request_inquiry_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_attachment_for_user_monetary_account_request_inquiry(
            user_id, monetary_account_id, request_inquiry_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_attachment_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentRequestResponseListing]:
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
        typing.List[NoteAttachmentRequestResponseListing]
            Used to manage attachment notes.

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
        client.note_attachment.list_all_note_attachment_for_user_monetary_account_request_response(
            user_id=1,
            monetary_account_id=1,
            request_response_id=1,
        )
        """
        _response = self._raw_client.list_all_note_attachment_for_user_monetary_account_request_response(
            user_id, monetary_account_id, request_response_id, request_options=request_options
        )
        return _response.data

    def create_note_attachment_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentRequestResponseCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_response_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentRequestResponseCreate
            Used to manage attachment notes.

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
        client.note_attachment.create_note_attachment_for_user_monetary_account_request_response(
            user_id=1,
            monetary_account_id=1,
            request_response_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.create_note_attachment_for_user_monetary_account_request_response(
            user_id,
            monetary_account_id,
            request_response_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def read_note_attachment_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentRequestResponseRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentRequestResponseRead
            Used to manage attachment notes.

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
        client.note_attachment.read_note_attachment_for_user_monetary_account_request_response(
            user_id=1,
            monetary_account_id=1,
            request_response_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_attachment_for_user_monetary_account_request_response(
            user_id, monetary_account_id, request_response_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_attachment_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentRequestResponseUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_response_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentRequestResponseUpdate
            Used to manage attachment notes.

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
        client.note_attachment.update_note_attachment_for_user_monetary_account_request_response(
            user_id=1,
            monetary_account_id=1,
            request_response_id=1,
            item_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.update_note_attachment_for_user_monetary_account_request_response(
            user_id,
            monetary_account_id,
            request_response_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def delete_note_attachment_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentRequestResponseDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentRequestResponseDelete
            Used to manage attachment notes.

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
        client.note_attachment.delete_note_attachment_for_user_monetary_account_request_response(
            user_id=1,
            monetary_account_id=1,
            request_response_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_attachment_for_user_monetary_account_request_response(
            user_id, monetary_account_id, request_response_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_attachment_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentSchedulePaymentBatchListing]:
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
        typing.List[NoteAttachmentSchedulePaymentBatchListing]
            Used to manage attachment notes.

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
        client.note_attachment.list_all_note_attachment_for_user_monetary_account_schedule_payment_batch(
            user_id=1,
            monetary_account_id=1,
            schedule_payment_batch_id=1,
        )
        """
        _response = self._raw_client.list_all_note_attachment_for_user_monetary_account_schedule_payment_batch(
            user_id, monetary_account_id, schedule_payment_batch_id, request_options=request_options
        )
        return _response.data

    def create_note_attachment_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentSchedulePaymentBatchCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_batch_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentSchedulePaymentBatchCreate
            Used to manage attachment notes.

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
        client.note_attachment.create_note_attachment_for_user_monetary_account_schedule_payment_batch(
            user_id=1,
            monetary_account_id=1,
            schedule_payment_batch_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.create_note_attachment_for_user_monetary_account_schedule_payment_batch(
            user_id,
            monetary_account_id,
            schedule_payment_batch_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def read_note_attachment_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentSchedulePaymentBatchRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentSchedulePaymentBatchRead
            Used to manage attachment notes.

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
        client.note_attachment.read_note_attachment_for_user_monetary_account_schedule_payment_batch(
            user_id=1,
            monetary_account_id=1,
            schedule_payment_batch_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_attachment_for_user_monetary_account_schedule_payment_batch(
            user_id, monetary_account_id, schedule_payment_batch_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_attachment_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentSchedulePaymentBatchUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_batch_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentSchedulePaymentBatchUpdate
            Used to manage attachment notes.

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
        client.note_attachment.update_note_attachment_for_user_monetary_account_schedule_payment_batch(
            user_id=1,
            monetary_account_id=1,
            schedule_payment_batch_id=1,
            item_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.update_note_attachment_for_user_monetary_account_schedule_payment_batch(
            user_id,
            monetary_account_id,
            schedule_payment_batch_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def delete_note_attachment_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentSchedulePaymentBatchDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentSchedulePaymentBatchDelete
            Used to manage attachment notes.

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
        client.note_attachment.delete_note_attachment_for_user_monetary_account_schedule_payment_batch(
            user_id=1,
            monetary_account_id=1,
            schedule_payment_batch_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_attachment_for_user_monetary_account_schedule_payment_batch(
            user_id, monetary_account_id, schedule_payment_batch_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_attachment_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentSchedulePaymentListing]:
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
        typing.List[NoteAttachmentSchedulePaymentListing]
            Used to manage attachment notes.

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
        client.note_attachment.list_all_note_attachment_for_user_monetary_account_schedule_payment(
            user_id=1,
            monetary_account_id=1,
            schedule_payment_id=1,
        )
        """
        _response = self._raw_client.list_all_note_attachment_for_user_monetary_account_schedule_payment(
            user_id, monetary_account_id, schedule_payment_id, request_options=request_options
        )
        return _response.data

    def create_note_attachment_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentSchedulePaymentCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentSchedulePaymentCreate
            Used to manage attachment notes.

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
        client.note_attachment.create_note_attachment_for_user_monetary_account_schedule_payment(
            user_id=1,
            monetary_account_id=1,
            schedule_payment_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.create_note_attachment_for_user_monetary_account_schedule_payment(
            user_id,
            monetary_account_id,
            schedule_payment_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def read_note_attachment_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentSchedulePaymentRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentSchedulePaymentRead
            Used to manage attachment notes.

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
        client.note_attachment.read_note_attachment_for_user_monetary_account_schedule_payment(
            user_id=1,
            monetary_account_id=1,
            schedule_payment_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_attachment_for_user_monetary_account_schedule_payment(
            user_id, monetary_account_id, schedule_payment_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_attachment_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentSchedulePaymentUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentSchedulePaymentUpdate
            Used to manage attachment notes.

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
        client.note_attachment.update_note_attachment_for_user_monetary_account_schedule_payment(
            user_id=1,
            monetary_account_id=1,
            schedule_payment_id=1,
            item_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.update_note_attachment_for_user_monetary_account_schedule_payment(
            user_id,
            monetary_account_id,
            schedule_payment_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def delete_note_attachment_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentSchedulePaymentDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentSchedulePaymentDelete
            Used to manage attachment notes.

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
        client.note_attachment.delete_note_attachment_for_user_monetary_account_schedule_payment(
            user_id=1,
            monetary_account_id=1,
            schedule_payment_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_attachment_for_user_monetary_account_schedule_payment(
            user_id, monetary_account_id, schedule_payment_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_attachment_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentScheduleInstanceListing]:
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
        typing.List[NoteAttachmentScheduleInstanceListing]
            Used to manage attachment notes.

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
        client.note_attachment.list_all_note_attachment_for_user_monetary_account_schedule_schedule_instance(
            user_id=1,
            monetary_account_id=1,
            schedule_id=1,
            schedule_instance_id=1,
        )
        """
        _response = self._raw_client.list_all_note_attachment_for_user_monetary_account_schedule_schedule_instance(
            user_id, monetary_account_id, schedule_id, schedule_instance_id, request_options=request_options
        )
        return _response.data

    def create_note_attachment_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentScheduleInstanceCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_id : int


        schedule_instance_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentScheduleInstanceCreate
            Used to manage attachment notes.

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
        client.note_attachment.create_note_attachment_for_user_monetary_account_schedule_schedule_instance(
            user_id=1,
            monetary_account_id=1,
            schedule_id=1,
            schedule_instance_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.create_note_attachment_for_user_monetary_account_schedule_schedule_instance(
            user_id,
            monetary_account_id,
            schedule_id,
            schedule_instance_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def read_note_attachment_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentScheduleInstanceRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentScheduleInstanceRead
            Used to manage attachment notes.

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
        client.note_attachment.read_note_attachment_for_user_monetary_account_schedule_schedule_instance(
            user_id=1,
            monetary_account_id=1,
            schedule_id=1,
            schedule_instance_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_attachment_for_user_monetary_account_schedule_schedule_instance(
            user_id, monetary_account_id, schedule_id, schedule_instance_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_attachment_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentScheduleInstanceUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_id : int


        schedule_instance_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentScheduleInstanceUpdate
            Used to manage attachment notes.

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
        client.note_attachment.update_note_attachment_for_user_monetary_account_schedule_schedule_instance(
            user_id=1,
            monetary_account_id=1,
            schedule_id=1,
            schedule_instance_id=1,
            item_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.update_note_attachment_for_user_monetary_account_schedule_schedule_instance(
            user_id,
            monetary_account_id,
            schedule_id,
            schedule_instance_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def delete_note_attachment_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentScheduleInstanceDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentScheduleInstanceDelete
            Used to manage attachment notes.

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
        client.note_attachment.delete_note_attachment_for_user_monetary_account_schedule_schedule_instance(
            user_id=1,
            monetary_account_id=1,
            schedule_id=1,
            schedule_instance_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_attachment_for_user_monetary_account_schedule_schedule_instance(
            user_id, monetary_account_id, schedule_id, schedule_instance_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentSofortMerchantTransactionListing]:
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
        typing.List[NoteAttachmentSofortMerchantTransactionListing]
            Used to manage attachment notes.

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
        client.note_attachment.list_all_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
            user_id=1,
            monetary_account_id=1,
            sofort_merchant_transaction_id=1,
        )
        """
        _response = self._raw_client.list_all_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
            user_id, monetary_account_id, sofort_merchant_transaction_id, request_options=request_options
        )
        return _response.data

    def create_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentSofortMerchantTransactionCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        sofort_merchant_transaction_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentSofortMerchantTransactionCreate
            Used to manage attachment notes.

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
        client.note_attachment.create_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
            user_id=1,
            monetary_account_id=1,
            sofort_merchant_transaction_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.create_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
            user_id,
            monetary_account_id,
            sofort_merchant_transaction_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def read_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentSofortMerchantTransactionRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentSofortMerchantTransactionRead
            Used to manage attachment notes.

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
        client.note_attachment.read_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
            user_id=1,
            monetary_account_id=1,
            sofort_merchant_transaction_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
            user_id, monetary_account_id, sofort_merchant_transaction_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentSofortMerchantTransactionUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        sofort_merchant_transaction_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentSofortMerchantTransactionUpdate
            Used to manage attachment notes.

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
        client.note_attachment.update_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
            user_id=1,
            monetary_account_id=1,
            sofort_merchant_transaction_id=1,
            item_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.update_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
            user_id,
            monetary_account_id,
            sofort_merchant_transaction_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def delete_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentSofortMerchantTransactionDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentSofortMerchantTransactionDelete
            Used to manage attachment notes.

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
        client.note_attachment.delete_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
            user_id=1,
            monetary_account_id=1,
            sofort_merchant_transaction_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
            user_id, monetary_account_id, sofort_merchant_transaction_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_attachment_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentListing]:
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
        typing.List[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentListing]
            Used to manage attachment notes.

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
        client.note_attachment.list_all_note_attachment_for_user_monetary_account_switch_service_payment(
            user_id=1,
            monetary_account_id=1,
            switch_service_payment_id=1,
        )
        """
        _response = self._raw_client.list_all_note_attachment_for_user_monetary_account_switch_service_payment(
            user_id, monetary_account_id, switch_service_payment_id, request_options=request_options
        )
        return _response.data

    def create_note_attachment_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        switch_service_payment_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentCreate
            Used to manage attachment notes.

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
        client.note_attachment.create_note_attachment_for_user_monetary_account_switch_service_payment(
            user_id=1,
            monetary_account_id=1,
            switch_service_payment_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.create_note_attachment_for_user_monetary_account_switch_service_payment(
            user_id,
            monetary_account_id,
            switch_service_payment_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def read_note_attachment_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentRead
            Used to manage attachment notes.

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
        client.note_attachment.read_note_attachment_for_user_monetary_account_switch_service_payment(
            user_id=1,
            monetary_account_id=1,
            switch_service_payment_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_attachment_for_user_monetary_account_switch_service_payment(
            user_id, monetary_account_id, switch_service_payment_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_attachment_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        switch_service_payment_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentUpdate
            Used to manage attachment notes.

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
        client.note_attachment.update_note_attachment_for_user_monetary_account_switch_service_payment(
            user_id=1,
            monetary_account_id=1,
            switch_service_payment_id=1,
            item_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.update_note_attachment_for_user_monetary_account_switch_service_payment(
            user_id,
            monetary_account_id,
            switch_service_payment_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def delete_note_attachment_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentDelete
            Used to manage attachment notes.

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
        client.note_attachment.delete_note_attachment_for_user_monetary_account_switch_service_payment(
            user_id=1,
            monetary_account_id=1,
            switch_service_payment_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_attachment_for_user_monetary_account_switch_service_payment(
            user_id, monetary_account_id, switch_service_payment_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentWhitelistResultListing]:
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
        typing.List[NoteAttachmentWhitelistResultListing]
            Used to manage attachment notes.

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
        client.note_attachment.list_all_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
            user_id=1,
            monetary_account_id=1,
            whitelist_id=1,
            whitelist_result_id=1,
        )
        """
        _response = self._raw_client.list_all_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
            user_id, monetary_account_id, whitelist_id, whitelist_result_id, request_options=request_options
        )
        return _response.data

    def create_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentWhitelistResultCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        whitelist_id : int


        whitelist_result_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentWhitelistResultCreate
            Used to manage attachment notes.

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
        client.note_attachment.create_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
            user_id=1,
            monetary_account_id=1,
            whitelist_id=1,
            whitelist_result_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.create_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
            user_id,
            monetary_account_id,
            whitelist_id,
            whitelist_result_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def read_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentWhitelistResultRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentWhitelistResultRead
            Used to manage attachment notes.

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
        client.note_attachment.read_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
            user_id=1,
            monetary_account_id=1,
            whitelist_id=1,
            whitelist_result_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
            user_id, monetary_account_id, whitelist_id, whitelist_result_id, item_id, request_options=request_options
        )
        return _response.data

    def update_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentWhitelistResultUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        whitelist_id : int


        whitelist_result_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentWhitelistResultUpdate
            Used to manage attachment notes.

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
        client.note_attachment.update_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
            user_id=1,
            monetary_account_id=1,
            whitelist_id=1,
            whitelist_result_id=1,
            item_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.update_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
            user_id,
            monetary_account_id,
            whitelist_id,
            whitelist_result_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def delete_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentWhitelistResultDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentWhitelistResultDelete
            Used to manage attachment notes.

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
        client.note_attachment.delete_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
            user_id=1,
            monetary_account_id=1,
            whitelist_id=1,
            whitelist_result_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
            user_id, monetary_account_id, whitelist_id, whitelist_result_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncNoteAttachmentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNoteAttachmentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNoteAttachmentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNoteAttachmentClient
        """
        return self._raw_client

    async def list_all_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentBunqMeFundraiserResultListing]:
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
        typing.List[NoteAttachmentBunqMeFundraiserResultListing]
            Used to manage attachment notes.

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
            await client.note_attachment.list_all_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
                user_id=1,
                monetary_account_id=1,
                bunqme_fundraiser_result_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
            user_id, monetary_account_id, bunqme_fundraiser_result_id, request_options=request_options
        )
        return _response.data

    async def create_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentBunqMeFundraiserResultCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        bunqme_fundraiser_result_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentBunqMeFundraiserResultCreate
            Used to manage attachment notes.

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
            await client.note_attachment.create_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
                user_id=1,
                monetary_account_id=1,
                bunqme_fundraiser_result_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
            user_id,
            monetary_account_id,
            bunqme_fundraiser_result_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def read_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentBunqMeFundraiserResultRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentBunqMeFundraiserResultRead
            Used to manage attachment notes.

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
            await client.note_attachment.read_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
                user_id=1,
                monetary_account_id=1,
                bunqme_fundraiser_result_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
            user_id, monetary_account_id, bunqme_fundraiser_result_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentBunqMeFundraiserResultUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        bunqme_fundraiser_result_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentBunqMeFundraiserResultUpdate
            Used to manage attachment notes.

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
            await client.note_attachment.update_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
                user_id=1,
                monetary_account_id=1,
                bunqme_fundraiser_result_id=1,
                item_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
            user_id,
            monetary_account_id,
            bunqme_fundraiser_result_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def delete_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentBunqMeFundraiserResultDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentBunqMeFundraiserResultDelete
            Used to manage attachment notes.

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
            await client.note_attachment.delete_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
                user_id=1,
                monetary_account_id=1,
                bunqme_fundraiser_result_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
            user_id, monetary_account_id, bunqme_fundraiser_result_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_attachment_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentDraftPaymentListing]:
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
        typing.List[NoteAttachmentDraftPaymentListing]
            Used to manage attachment notes.

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
            await client.note_attachment.list_all_note_attachment_for_user_monetary_account_draft_payment(
                user_id=1,
                monetary_account_id=1,
                draft_payment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_note_attachment_for_user_monetary_account_draft_payment(
            user_id, monetary_account_id, draft_payment_id, request_options=request_options
        )
        return _response.data

    async def create_note_attachment_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentDraftPaymentCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        draft_payment_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentDraftPaymentCreate
            Used to manage attachment notes.

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
            await client.note_attachment.create_note_attachment_for_user_monetary_account_draft_payment(
                user_id=1,
                monetary_account_id=1,
                draft_payment_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_attachment_for_user_monetary_account_draft_payment(
            user_id,
            monetary_account_id,
            draft_payment_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def read_note_attachment_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentDraftPaymentRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentDraftPaymentRead
            Used to manage attachment notes.

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
            await client.note_attachment.read_note_attachment_for_user_monetary_account_draft_payment(
                user_id=1,
                monetary_account_id=1,
                draft_payment_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_attachment_for_user_monetary_account_draft_payment(
            user_id, monetary_account_id, draft_payment_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_attachment_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentDraftPaymentUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        draft_payment_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentDraftPaymentUpdate
            Used to manage attachment notes.

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
            await client.note_attachment.update_note_attachment_for_user_monetary_account_draft_payment(
                user_id=1,
                monetary_account_id=1,
                draft_payment_id=1,
                item_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_attachment_for_user_monetary_account_draft_payment(
            user_id,
            monetary_account_id,
            draft_payment_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def delete_note_attachment_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentDraftPaymentDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentDraftPaymentDelete
            Used to manage attachment notes.

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
            await client.note_attachment.delete_note_attachment_for_user_monetary_account_draft_payment(
                user_id=1,
                monetary_account_id=1,
                draft_payment_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_attachment_for_user_monetary_account_draft_payment(
            user_id, monetary_account_id, draft_payment_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentIdealMerchantTransactionListing]:
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
        typing.List[NoteAttachmentIdealMerchantTransactionListing]
            Used to manage attachment notes.

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
            await client.note_attachment.list_all_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
                user_id=1,
                monetary_account_id=1,
                ideal_merchant_transaction_id=1,
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.list_all_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
                user_id, monetary_account_id, ideal_merchant_transaction_id, request_options=request_options
            )
        )
        return _response.data

    async def create_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentIdealMerchantTransactionCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        ideal_merchant_transaction_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentIdealMerchantTransactionCreate
            Used to manage attachment notes.

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
            await client.note_attachment.create_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
                user_id=1,
                monetary_account_id=1,
                ideal_merchant_transaction_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
            user_id,
            monetary_account_id,
            ideal_merchant_transaction_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def read_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentIdealMerchantTransactionRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentIdealMerchantTransactionRead
            Used to manage attachment notes.

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
            await client.note_attachment.read_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
                user_id=1,
                monetary_account_id=1,
                ideal_merchant_transaction_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
            user_id, monetary_account_id, ideal_merchant_transaction_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentIdealMerchantTransactionUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        ideal_merchant_transaction_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentIdealMerchantTransactionUpdate
            Used to manage attachment notes.

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
            await client.note_attachment.update_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
                user_id=1,
                monetary_account_id=1,
                ideal_merchant_transaction_id=1,
                item_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
            user_id,
            monetary_account_id,
            ideal_merchant_transaction_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def delete_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentIdealMerchantTransactionDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentIdealMerchantTransactionDelete
            Used to manage attachment notes.

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
            await client.note_attachment.delete_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
                user_id=1,
                monetary_account_id=1,
                ideal_merchant_transaction_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
            user_id, monetary_account_id, ideal_merchant_transaction_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_attachment_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentMasterCardActionListing]:
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
        typing.List[NoteAttachmentMasterCardActionListing]
            Used to manage attachment notes.

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
            await client.note_attachment.list_all_note_attachment_for_user_monetary_account_mastercard_action(
                user_id=1,
                monetary_account_id=1,
                mastercard_action_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_note_attachment_for_user_monetary_account_mastercard_action(
            user_id, monetary_account_id, mastercard_action_id, request_options=request_options
        )
        return _response.data

    async def create_note_attachment_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentMasterCardActionCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        mastercard_action_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentMasterCardActionCreate
            Used to manage attachment notes.

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
            await client.note_attachment.create_note_attachment_for_user_monetary_account_mastercard_action(
                user_id=1,
                monetary_account_id=1,
                mastercard_action_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_attachment_for_user_monetary_account_mastercard_action(
            user_id,
            monetary_account_id,
            mastercard_action_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def read_note_attachment_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentMasterCardActionRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentMasterCardActionRead
            Used to manage attachment notes.

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
            await client.note_attachment.read_note_attachment_for_user_monetary_account_mastercard_action(
                user_id=1,
                monetary_account_id=1,
                mastercard_action_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_attachment_for_user_monetary_account_mastercard_action(
            user_id, monetary_account_id, mastercard_action_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_attachment_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentMasterCardActionUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        mastercard_action_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentMasterCardActionUpdate
            Used to manage attachment notes.

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
            await client.note_attachment.update_note_attachment_for_user_monetary_account_mastercard_action(
                user_id=1,
                monetary_account_id=1,
                mastercard_action_id=1,
                item_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_attachment_for_user_monetary_account_mastercard_action(
            user_id,
            monetary_account_id,
            mastercard_action_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def delete_note_attachment_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentMasterCardActionDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentMasterCardActionDelete
            Used to manage attachment notes.

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
            await client.note_attachment.delete_note_attachment_for_user_monetary_account_mastercard_action(
                user_id=1,
                monetary_account_id=1,
                mastercard_action_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_attachment_for_user_monetary_account_mastercard_action(
            user_id, monetary_account_id, mastercard_action_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_attachment_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentPaymentBatchListing]:
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
        typing.List[NoteAttachmentPaymentBatchListing]
            Used to manage attachment notes.

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
            await client.note_attachment.list_all_note_attachment_for_user_monetary_account_payment_batch(
                user_id=1,
                monetary_account_id=1,
                payment_batch_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_note_attachment_for_user_monetary_account_payment_batch(
            user_id, monetary_account_id, payment_batch_id, request_options=request_options
        )
        return _response.data

    async def create_note_attachment_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentPaymentBatchCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_batch_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentPaymentBatchCreate
            Used to manage attachment notes.

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
            await client.note_attachment.create_note_attachment_for_user_monetary_account_payment_batch(
                user_id=1,
                monetary_account_id=1,
                payment_batch_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_attachment_for_user_monetary_account_payment_batch(
            user_id,
            monetary_account_id,
            payment_batch_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def read_note_attachment_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentPaymentBatchRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentPaymentBatchRead
            Used to manage attachment notes.

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
            await client.note_attachment.read_note_attachment_for_user_monetary_account_payment_batch(
                user_id=1,
                monetary_account_id=1,
                payment_batch_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_attachment_for_user_monetary_account_payment_batch(
            user_id, monetary_account_id, payment_batch_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_attachment_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentPaymentBatchUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_batch_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentPaymentBatchUpdate
            Used to manage attachment notes.

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
            await client.note_attachment.update_note_attachment_for_user_monetary_account_payment_batch(
                user_id=1,
                monetary_account_id=1,
                payment_batch_id=1,
                item_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_attachment_for_user_monetary_account_payment_batch(
            user_id,
            monetary_account_id,
            payment_batch_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def delete_note_attachment_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentPaymentBatchDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentPaymentBatchDelete
            Used to manage attachment notes.

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
            await client.note_attachment.delete_note_attachment_for_user_monetary_account_payment_batch(
                user_id=1,
                monetary_account_id=1,
                payment_batch_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_attachment_for_user_monetary_account_payment_batch(
            user_id, monetary_account_id, payment_batch_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_attachment_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentPaymentListing]:
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
        typing.List[NoteAttachmentPaymentListing]
            Used to manage attachment notes.

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
            await client.note_attachment.list_all_note_attachment_for_user_monetary_account_payment(
                user_id=1,
                monetary_account_id=1,
                payment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_note_attachment_for_user_monetary_account_payment(
            user_id, monetary_account_id, payment_id, request_options=request_options
        )
        return _response.data

    async def create_note_attachment_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentPaymentCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentPaymentCreate
            Used to manage attachment notes.

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
            await client.note_attachment.create_note_attachment_for_user_monetary_account_payment(
                user_id=1,
                monetary_account_id=1,
                payment_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_attachment_for_user_monetary_account_payment(
            user_id,
            monetary_account_id,
            payment_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def read_note_attachment_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentPaymentRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentPaymentRead
            Used to manage attachment notes.

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
            await client.note_attachment.read_note_attachment_for_user_monetary_account_payment(
                user_id=1,
                monetary_account_id=1,
                payment_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_attachment_for_user_monetary_account_payment(
            user_id, monetary_account_id, payment_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_attachment_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentPaymentUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentPaymentUpdate
            Used to manage attachment notes.

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
            await client.note_attachment.update_note_attachment_for_user_monetary_account_payment(
                user_id=1,
                monetary_account_id=1,
                payment_id=1,
                item_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_attachment_for_user_monetary_account_payment(
            user_id,
            monetary_account_id,
            payment_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def delete_note_attachment_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentPaymentDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentPaymentDelete
            Used to manage attachment notes.

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
            await client.note_attachment.delete_note_attachment_for_user_monetary_account_payment(
                user_id=1,
                monetary_account_id=1,
                payment_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_attachment_for_user_monetary_account_payment(
            user_id, monetary_account_id, payment_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_attachment_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentRequestInquiryBatchListing]:
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
        typing.List[NoteAttachmentRequestInquiryBatchListing]
            Used to manage attachment notes.

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
            await client.note_attachment.list_all_note_attachment_for_user_monetary_account_request_inquiry_batch(
                user_id=1,
                monetary_account_id=1,
                request_inquiry_batch_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_note_attachment_for_user_monetary_account_request_inquiry_batch(
            user_id, monetary_account_id, request_inquiry_batch_id, request_options=request_options
        )
        return _response.data

    async def create_note_attachment_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentRequestInquiryBatchCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_batch_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentRequestInquiryBatchCreate
            Used to manage attachment notes.

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
            await client.note_attachment.create_note_attachment_for_user_monetary_account_request_inquiry_batch(
                user_id=1,
                monetary_account_id=1,
                request_inquiry_batch_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_attachment_for_user_monetary_account_request_inquiry_batch(
            user_id,
            monetary_account_id,
            request_inquiry_batch_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def read_note_attachment_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentRequestInquiryBatchRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentRequestInquiryBatchRead
            Used to manage attachment notes.

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
            await client.note_attachment.read_note_attachment_for_user_monetary_account_request_inquiry_batch(
                user_id=1,
                monetary_account_id=1,
                request_inquiry_batch_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_attachment_for_user_monetary_account_request_inquiry_batch(
            user_id, monetary_account_id, request_inquiry_batch_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_attachment_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentRequestInquiryBatchUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_batch_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentRequestInquiryBatchUpdate
            Used to manage attachment notes.

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
            await client.note_attachment.update_note_attachment_for_user_monetary_account_request_inquiry_batch(
                user_id=1,
                monetary_account_id=1,
                request_inquiry_batch_id=1,
                item_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_attachment_for_user_monetary_account_request_inquiry_batch(
            user_id,
            monetary_account_id,
            request_inquiry_batch_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def delete_note_attachment_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentRequestInquiryBatchDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentRequestInquiryBatchDelete
            Used to manage attachment notes.

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
            await client.note_attachment.delete_note_attachment_for_user_monetary_account_request_inquiry_batch(
                user_id=1,
                monetary_account_id=1,
                request_inquiry_batch_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_attachment_for_user_monetary_account_request_inquiry_batch(
            user_id, monetary_account_id, request_inquiry_batch_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_attachment_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentRequestInquiryListing]:
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
        typing.List[NoteAttachmentRequestInquiryListing]
            Used to manage attachment notes.

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
            await client.note_attachment.list_all_note_attachment_for_user_monetary_account_request_inquiry(
                user_id=1,
                monetary_account_id=1,
                request_inquiry_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_note_attachment_for_user_monetary_account_request_inquiry(
            user_id, monetary_account_id, request_inquiry_id, request_options=request_options
        )
        return _response.data

    async def create_note_attachment_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentRequestInquiryCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentRequestInquiryCreate
            Used to manage attachment notes.

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
            await client.note_attachment.create_note_attachment_for_user_monetary_account_request_inquiry(
                user_id=1,
                monetary_account_id=1,
                request_inquiry_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_attachment_for_user_monetary_account_request_inquiry(
            user_id,
            monetary_account_id,
            request_inquiry_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def read_note_attachment_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentRequestInquiryRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentRequestInquiryRead
            Used to manage attachment notes.

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
            await client.note_attachment.read_note_attachment_for_user_monetary_account_request_inquiry(
                user_id=1,
                monetary_account_id=1,
                request_inquiry_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_attachment_for_user_monetary_account_request_inquiry(
            user_id, monetary_account_id, request_inquiry_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_attachment_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentRequestInquiryUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_inquiry_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentRequestInquiryUpdate
            Used to manage attachment notes.

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
            await client.note_attachment.update_note_attachment_for_user_monetary_account_request_inquiry(
                user_id=1,
                monetary_account_id=1,
                request_inquiry_id=1,
                item_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_attachment_for_user_monetary_account_request_inquiry(
            user_id,
            monetary_account_id,
            request_inquiry_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def delete_note_attachment_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentRequestInquiryDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentRequestInquiryDelete
            Used to manage attachment notes.

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
            await client.note_attachment.delete_note_attachment_for_user_monetary_account_request_inquiry(
                user_id=1,
                monetary_account_id=1,
                request_inquiry_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_attachment_for_user_monetary_account_request_inquiry(
            user_id, monetary_account_id, request_inquiry_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_attachment_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentRequestResponseListing]:
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
        typing.List[NoteAttachmentRequestResponseListing]
            Used to manage attachment notes.

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
            await client.note_attachment.list_all_note_attachment_for_user_monetary_account_request_response(
                user_id=1,
                monetary_account_id=1,
                request_response_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_note_attachment_for_user_monetary_account_request_response(
            user_id, monetary_account_id, request_response_id, request_options=request_options
        )
        return _response.data

    async def create_note_attachment_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentRequestResponseCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_response_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentRequestResponseCreate
            Used to manage attachment notes.

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
            await client.note_attachment.create_note_attachment_for_user_monetary_account_request_response(
                user_id=1,
                monetary_account_id=1,
                request_response_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_attachment_for_user_monetary_account_request_response(
            user_id,
            monetary_account_id,
            request_response_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def read_note_attachment_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentRequestResponseRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentRequestResponseRead
            Used to manage attachment notes.

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
            await client.note_attachment.read_note_attachment_for_user_monetary_account_request_response(
                user_id=1,
                monetary_account_id=1,
                request_response_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_attachment_for_user_monetary_account_request_response(
            user_id, monetary_account_id, request_response_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_attachment_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentRequestResponseUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_response_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentRequestResponseUpdate
            Used to manage attachment notes.

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
            await client.note_attachment.update_note_attachment_for_user_monetary_account_request_response(
                user_id=1,
                monetary_account_id=1,
                request_response_id=1,
                item_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_attachment_for_user_monetary_account_request_response(
            user_id,
            monetary_account_id,
            request_response_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def delete_note_attachment_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentRequestResponseDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentRequestResponseDelete
            Used to manage attachment notes.

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
            await client.note_attachment.delete_note_attachment_for_user_monetary_account_request_response(
                user_id=1,
                monetary_account_id=1,
                request_response_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_attachment_for_user_monetary_account_request_response(
            user_id, monetary_account_id, request_response_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_attachment_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentSchedulePaymentBatchListing]:
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
        typing.List[NoteAttachmentSchedulePaymentBatchListing]
            Used to manage attachment notes.

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
            await client.note_attachment.list_all_note_attachment_for_user_monetary_account_schedule_payment_batch(
                user_id=1,
                monetary_account_id=1,
                schedule_payment_batch_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_note_attachment_for_user_monetary_account_schedule_payment_batch(
            user_id, monetary_account_id, schedule_payment_batch_id, request_options=request_options
        )
        return _response.data

    async def create_note_attachment_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentSchedulePaymentBatchCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_batch_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentSchedulePaymentBatchCreate
            Used to manage attachment notes.

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
            await client.note_attachment.create_note_attachment_for_user_monetary_account_schedule_payment_batch(
                user_id=1,
                monetary_account_id=1,
                schedule_payment_batch_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_attachment_for_user_monetary_account_schedule_payment_batch(
            user_id,
            monetary_account_id,
            schedule_payment_batch_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def read_note_attachment_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentSchedulePaymentBatchRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentSchedulePaymentBatchRead
            Used to manage attachment notes.

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
            await client.note_attachment.read_note_attachment_for_user_monetary_account_schedule_payment_batch(
                user_id=1,
                monetary_account_id=1,
                schedule_payment_batch_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_attachment_for_user_monetary_account_schedule_payment_batch(
            user_id, monetary_account_id, schedule_payment_batch_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_attachment_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentSchedulePaymentBatchUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_batch_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentSchedulePaymentBatchUpdate
            Used to manage attachment notes.

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
            await client.note_attachment.update_note_attachment_for_user_monetary_account_schedule_payment_batch(
                user_id=1,
                monetary_account_id=1,
                schedule_payment_batch_id=1,
                item_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_attachment_for_user_monetary_account_schedule_payment_batch(
            user_id,
            monetary_account_id,
            schedule_payment_batch_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def delete_note_attachment_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentSchedulePaymentBatchDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentSchedulePaymentBatchDelete
            Used to manage attachment notes.

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
            await client.note_attachment.delete_note_attachment_for_user_monetary_account_schedule_payment_batch(
                user_id=1,
                monetary_account_id=1,
                schedule_payment_batch_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_attachment_for_user_monetary_account_schedule_payment_batch(
            user_id, monetary_account_id, schedule_payment_batch_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_attachment_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentSchedulePaymentListing]:
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
        typing.List[NoteAttachmentSchedulePaymentListing]
            Used to manage attachment notes.

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
            await client.note_attachment.list_all_note_attachment_for_user_monetary_account_schedule_payment(
                user_id=1,
                monetary_account_id=1,
                schedule_payment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_note_attachment_for_user_monetary_account_schedule_payment(
            user_id, monetary_account_id, schedule_payment_id, request_options=request_options
        )
        return _response.data

    async def create_note_attachment_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentSchedulePaymentCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentSchedulePaymentCreate
            Used to manage attachment notes.

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
            await client.note_attachment.create_note_attachment_for_user_monetary_account_schedule_payment(
                user_id=1,
                monetary_account_id=1,
                schedule_payment_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_attachment_for_user_monetary_account_schedule_payment(
            user_id,
            monetary_account_id,
            schedule_payment_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def read_note_attachment_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentSchedulePaymentRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentSchedulePaymentRead
            Used to manage attachment notes.

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
            await client.note_attachment.read_note_attachment_for_user_monetary_account_schedule_payment(
                user_id=1,
                monetary_account_id=1,
                schedule_payment_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_attachment_for_user_monetary_account_schedule_payment(
            user_id, monetary_account_id, schedule_payment_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_attachment_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentSchedulePaymentUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_payment_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentSchedulePaymentUpdate
            Used to manage attachment notes.

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
            await client.note_attachment.update_note_attachment_for_user_monetary_account_schedule_payment(
                user_id=1,
                monetary_account_id=1,
                schedule_payment_id=1,
                item_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_attachment_for_user_monetary_account_schedule_payment(
            user_id,
            monetary_account_id,
            schedule_payment_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def delete_note_attachment_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentSchedulePaymentDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentSchedulePaymentDelete
            Used to manage attachment notes.

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
            await client.note_attachment.delete_note_attachment_for_user_monetary_account_schedule_payment(
                user_id=1,
                monetary_account_id=1,
                schedule_payment_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_attachment_for_user_monetary_account_schedule_payment(
            user_id, monetary_account_id, schedule_payment_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_attachment_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentScheduleInstanceListing]:
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
        typing.List[NoteAttachmentScheduleInstanceListing]
            Used to manage attachment notes.

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
            await client.note_attachment.list_all_note_attachment_for_user_monetary_account_schedule_schedule_instance(
                user_id=1,
                monetary_account_id=1,
                schedule_id=1,
                schedule_instance_id=1,
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.list_all_note_attachment_for_user_monetary_account_schedule_schedule_instance(
                user_id, monetary_account_id, schedule_id, schedule_instance_id, request_options=request_options
            )
        )
        return _response.data

    async def create_note_attachment_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentScheduleInstanceCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_id : int


        schedule_instance_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentScheduleInstanceCreate
            Used to manage attachment notes.

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
            await client.note_attachment.create_note_attachment_for_user_monetary_account_schedule_schedule_instance(
                user_id=1,
                monetary_account_id=1,
                schedule_id=1,
                schedule_instance_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_attachment_for_user_monetary_account_schedule_schedule_instance(
            user_id,
            monetary_account_id,
            schedule_id,
            schedule_instance_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def read_note_attachment_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentScheduleInstanceRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentScheduleInstanceRead
            Used to manage attachment notes.

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
            await client.note_attachment.read_note_attachment_for_user_monetary_account_schedule_schedule_instance(
                user_id=1,
                monetary_account_id=1,
                schedule_id=1,
                schedule_instance_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_attachment_for_user_monetary_account_schedule_schedule_instance(
            user_id, monetary_account_id, schedule_id, schedule_instance_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_attachment_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentScheduleInstanceUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_id : int


        schedule_instance_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentScheduleInstanceUpdate
            Used to manage attachment notes.

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
            await client.note_attachment.update_note_attachment_for_user_monetary_account_schedule_schedule_instance(
                user_id=1,
                monetary_account_id=1,
                schedule_id=1,
                schedule_instance_id=1,
                item_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_attachment_for_user_monetary_account_schedule_schedule_instance(
            user_id,
            monetary_account_id,
            schedule_id,
            schedule_instance_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def delete_note_attachment_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentScheduleInstanceDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentScheduleInstanceDelete
            Used to manage attachment notes.

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
            await client.note_attachment.delete_note_attachment_for_user_monetary_account_schedule_schedule_instance(
                user_id=1,
                monetary_account_id=1,
                schedule_id=1,
                schedule_instance_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_attachment_for_user_monetary_account_schedule_schedule_instance(
            user_id, monetary_account_id, schedule_id, schedule_instance_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentSofortMerchantTransactionListing]:
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
        typing.List[NoteAttachmentSofortMerchantTransactionListing]
            Used to manage attachment notes.

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
            await client.note_attachment.list_all_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
                user_id=1,
                monetary_account_id=1,
                sofort_merchant_transaction_id=1,
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.list_all_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
                user_id, monetary_account_id, sofort_merchant_transaction_id, request_options=request_options
            )
        )
        return _response.data

    async def create_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentSofortMerchantTransactionCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        sofort_merchant_transaction_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentSofortMerchantTransactionCreate
            Used to manage attachment notes.

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
            await client.note_attachment.create_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
                user_id=1,
                monetary_account_id=1,
                sofort_merchant_transaction_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
            user_id,
            monetary_account_id,
            sofort_merchant_transaction_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def read_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentSofortMerchantTransactionRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentSofortMerchantTransactionRead
            Used to manage attachment notes.

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
            await client.note_attachment.read_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
                user_id=1,
                monetary_account_id=1,
                sofort_merchant_transaction_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
            user_id, monetary_account_id, sofort_merchant_transaction_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentSofortMerchantTransactionUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        sofort_merchant_transaction_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentSofortMerchantTransactionUpdate
            Used to manage attachment notes.

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
            await client.note_attachment.update_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
                user_id=1,
                monetary_account_id=1,
                sofort_merchant_transaction_id=1,
                item_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
            user_id,
            monetary_account_id,
            sofort_merchant_transaction_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def delete_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentSofortMerchantTransactionDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentSofortMerchantTransactionDelete
            Used to manage attachment notes.

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
            await client.note_attachment.delete_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
                user_id=1,
                monetary_account_id=1,
                sofort_merchant_transaction_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
            user_id, monetary_account_id, sofort_merchant_transaction_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_attachment_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentListing]:
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
        typing.List[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentListing]
            Used to manage attachment notes.

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
            await client.note_attachment.list_all_note_attachment_for_user_monetary_account_switch_service_payment(
                user_id=1,
                monetary_account_id=1,
                switch_service_payment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_note_attachment_for_user_monetary_account_switch_service_payment(
            user_id, monetary_account_id, switch_service_payment_id, request_options=request_options
        )
        return _response.data

    async def create_note_attachment_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        switch_service_payment_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentCreate
            Used to manage attachment notes.

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
            await client.note_attachment.create_note_attachment_for_user_monetary_account_switch_service_payment(
                user_id=1,
                monetary_account_id=1,
                switch_service_payment_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_attachment_for_user_monetary_account_switch_service_payment(
            user_id,
            monetary_account_id,
            switch_service_payment_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def read_note_attachment_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentRead
            Used to manage attachment notes.

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
            await client.note_attachment.read_note_attachment_for_user_monetary_account_switch_service_payment(
                user_id=1,
                monetary_account_id=1,
                switch_service_payment_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_attachment_for_user_monetary_account_switch_service_payment(
            user_id, monetary_account_id, switch_service_payment_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_attachment_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        switch_service_payment_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentUpdate
            Used to manage attachment notes.

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
            await client.note_attachment.update_note_attachment_for_user_monetary_account_switch_service_payment(
                user_id=1,
                monetary_account_id=1,
                switch_service_payment_id=1,
                item_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_attachment_for_user_monetary_account_switch_service_payment(
            user_id,
            monetary_account_id,
            switch_service_payment_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def delete_note_attachment_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentDelete
            Used to manage attachment notes.

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
            await client.note_attachment.delete_note_attachment_for_user_monetary_account_switch_service_payment(
                user_id=1,
                monetary_account_id=1,
                switch_service_payment_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_attachment_for_user_monetary_account_switch_service_payment(
            user_id, monetary_account_id, switch_service_payment_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NoteAttachmentWhitelistResultListing]:
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
        typing.List[NoteAttachmentWhitelistResultListing]
            Used to manage attachment notes.

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
            await client.note_attachment.list_all_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
                user_id=1,
                monetary_account_id=1,
                whitelist_id=1,
                whitelist_result_id=1,
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.list_all_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
                user_id, monetary_account_id, whitelist_id, whitelist_result_id, request_options=request_options
            )
        )
        return _response.data

    async def create_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentWhitelistResultCreate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        whitelist_id : int


        whitelist_result_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentWhitelistResultCreate
            Used to manage attachment notes.

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
            await client.note_attachment.create_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
                user_id=1,
                monetary_account_id=1,
                whitelist_id=1,
                whitelist_result_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
            user_id,
            monetary_account_id,
            whitelist_id,
            whitelist_result_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def read_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentWhitelistResultRead:
        """
        Used to manage attachment notes.

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
        NoteAttachmentWhitelistResultRead
            Used to manage attachment notes.

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
            await client.note_attachment.read_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
                user_id=1,
                monetary_account_id=1,
                whitelist_id=1,
                whitelist_result_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
            user_id, monetary_account_id, whitelist_id, whitelist_result_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        item_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentWhitelistResultUpdate:
        """
        Used to manage attachment notes.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        whitelist_id : int


        whitelist_result_id : int


        item_id : int


        attachment_id : int
            The reference to the uploaded file to attach to this note.

        description : typing.Optional[str]
            Optional description of the attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoteAttachmentWhitelistResultUpdate
            Used to manage attachment notes.

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
            await client.note_attachment.update_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
                user_id=1,
                monetary_account_id=1,
                whitelist_id=1,
                whitelist_result_id=1,
                item_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
            user_id,
            monetary_account_id,
            whitelist_id,
            whitelist_result_id,
            item_id,
            attachment_id=attachment_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def delete_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NoteAttachmentWhitelistResultDelete:
        """
        Used to manage attachment notes.

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
        NoteAttachmentWhitelistResultDelete
            Used to manage attachment notes.

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
            await client.note_attachment.delete_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
                user_id=1,
                monetary_account_id=1,
                whitelist_id=1,
                whitelist_result_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
            user_id, monetary_account_id, whitelist_id, whitelist_result_id, item_id, request_options=request_options
        )
        return _response.data
