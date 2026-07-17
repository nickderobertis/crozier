

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawNoteAttachmentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteAttachmentBunqMeFundraiserResultListing]]:
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
        HttpResponse[typing.List[NoteAttachmentBunqMeFundraiserResultListing]]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/bunqme-fundraiser-result/{encode_path_param(bunqme_fundraiser_result_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentBunqMeFundraiserResultListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentBunqMeFundraiserResultListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentBunqMeFundraiserResultCreate]:
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
        HttpResponse[NoteAttachmentBunqMeFundraiserResultCreate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/bunqme-fundraiser-result/{encode_path_param(bunqme_fundraiser_result_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentBunqMeFundraiserResultCreate,
                    parse_obj_as(
                        type_=NoteAttachmentBunqMeFundraiserResultCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentBunqMeFundraiserResultRead]:
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
        HttpResponse[NoteAttachmentBunqMeFundraiserResultRead]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/bunqme-fundraiser-result/{encode_path_param(bunqme_fundraiser_result_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentBunqMeFundraiserResultRead,
                    parse_obj_as(
                        type_=NoteAttachmentBunqMeFundraiserResultRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[NoteAttachmentBunqMeFundraiserResultUpdate]:
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
        HttpResponse[NoteAttachmentBunqMeFundraiserResultUpdate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/bunqme-fundraiser-result/{encode_path_param(bunqme_fundraiser_result_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentBunqMeFundraiserResultUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentBunqMeFundraiserResultUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentBunqMeFundraiserResultDelete]:
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
        HttpResponse[NoteAttachmentBunqMeFundraiserResultDelete]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/bunqme-fundraiser-result/{encode_path_param(bunqme_fundraiser_result_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentBunqMeFundraiserResultDelete,
                    parse_obj_as(
                        type_=NoteAttachmentBunqMeFundraiserResultDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_attachment_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteAttachmentDraftPaymentListing]]:
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
        HttpResponse[typing.List[NoteAttachmentDraftPaymentListing]]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/draft-payment/{encode_path_param(draft_payment_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentDraftPaymentListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentDraftPaymentListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_attachment_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentDraftPaymentCreate]:
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
        HttpResponse[NoteAttachmentDraftPaymentCreate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/draft-payment/{encode_path_param(draft_payment_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentDraftPaymentCreate,
                    parse_obj_as(
                        type_=NoteAttachmentDraftPaymentCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_attachment_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentDraftPaymentRead]:
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
        HttpResponse[NoteAttachmentDraftPaymentRead]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/draft-payment/{encode_path_param(draft_payment_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentDraftPaymentRead,
                    parse_obj_as(
                        type_=NoteAttachmentDraftPaymentRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[NoteAttachmentDraftPaymentUpdate]:
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
        HttpResponse[NoteAttachmentDraftPaymentUpdate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/draft-payment/{encode_path_param(draft_payment_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentDraftPaymentUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentDraftPaymentUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_attachment_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentDraftPaymentDelete]:
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
        HttpResponse[NoteAttachmentDraftPaymentDelete]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/draft-payment/{encode_path_param(draft_payment_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentDraftPaymentDelete,
                    parse_obj_as(
                        type_=NoteAttachmentDraftPaymentDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteAttachmentIdealMerchantTransactionListing]]:
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
        HttpResponse[typing.List[NoteAttachmentIdealMerchantTransactionListing]]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/ideal-merchant-transaction/{encode_path_param(ideal_merchant_transaction_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentIdealMerchantTransactionListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentIdealMerchantTransactionListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentIdealMerchantTransactionCreate]:
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
        HttpResponse[NoteAttachmentIdealMerchantTransactionCreate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/ideal-merchant-transaction/{encode_path_param(ideal_merchant_transaction_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentIdealMerchantTransactionCreate,
                    parse_obj_as(
                        type_=NoteAttachmentIdealMerchantTransactionCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentIdealMerchantTransactionRead]:
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
        HttpResponse[NoteAttachmentIdealMerchantTransactionRead]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/ideal-merchant-transaction/{encode_path_param(ideal_merchant_transaction_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentIdealMerchantTransactionRead,
                    parse_obj_as(
                        type_=NoteAttachmentIdealMerchantTransactionRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[NoteAttachmentIdealMerchantTransactionUpdate]:
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
        HttpResponse[NoteAttachmentIdealMerchantTransactionUpdate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/ideal-merchant-transaction/{encode_path_param(ideal_merchant_transaction_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentIdealMerchantTransactionUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentIdealMerchantTransactionUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentIdealMerchantTransactionDelete]:
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
        HttpResponse[NoteAttachmentIdealMerchantTransactionDelete]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/ideal-merchant-transaction/{encode_path_param(ideal_merchant_transaction_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentIdealMerchantTransactionDelete,
                    parse_obj_as(
                        type_=NoteAttachmentIdealMerchantTransactionDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_attachment_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteAttachmentMasterCardActionListing]]:
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
        HttpResponse[typing.List[NoteAttachmentMasterCardActionListing]]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/mastercard-action/{encode_path_param(mastercard_action_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentMasterCardActionListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentMasterCardActionListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_attachment_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentMasterCardActionCreate]:
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
        HttpResponse[NoteAttachmentMasterCardActionCreate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/mastercard-action/{encode_path_param(mastercard_action_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentMasterCardActionCreate,
                    parse_obj_as(
                        type_=NoteAttachmentMasterCardActionCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_attachment_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentMasterCardActionRead]:
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
        HttpResponse[NoteAttachmentMasterCardActionRead]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/mastercard-action/{encode_path_param(mastercard_action_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentMasterCardActionRead,
                    parse_obj_as(
                        type_=NoteAttachmentMasterCardActionRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[NoteAttachmentMasterCardActionUpdate]:
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
        HttpResponse[NoteAttachmentMasterCardActionUpdate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/mastercard-action/{encode_path_param(mastercard_action_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentMasterCardActionUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentMasterCardActionUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_attachment_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentMasterCardActionDelete]:
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
        HttpResponse[NoteAttachmentMasterCardActionDelete]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/mastercard-action/{encode_path_param(mastercard_action_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentMasterCardActionDelete,
                    parse_obj_as(
                        type_=NoteAttachmentMasterCardActionDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_attachment_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteAttachmentPaymentBatchListing]]:
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
        HttpResponse[typing.List[NoteAttachmentPaymentBatchListing]]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/payment-batch/{encode_path_param(payment_batch_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentPaymentBatchListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentPaymentBatchListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_attachment_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentPaymentBatchCreate]:
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
        HttpResponse[NoteAttachmentPaymentBatchCreate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/payment-batch/{encode_path_param(payment_batch_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentPaymentBatchCreate,
                    parse_obj_as(
                        type_=NoteAttachmentPaymentBatchCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_attachment_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentPaymentBatchRead]:
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
        HttpResponse[NoteAttachmentPaymentBatchRead]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/payment-batch/{encode_path_param(payment_batch_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentPaymentBatchRead,
                    parse_obj_as(
                        type_=NoteAttachmentPaymentBatchRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[NoteAttachmentPaymentBatchUpdate]:
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
        HttpResponse[NoteAttachmentPaymentBatchUpdate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/payment-batch/{encode_path_param(payment_batch_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentPaymentBatchUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentPaymentBatchUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_attachment_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentPaymentBatchDelete]:
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
        HttpResponse[NoteAttachmentPaymentBatchDelete]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/payment-batch/{encode_path_param(payment_batch_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentPaymentBatchDelete,
                    parse_obj_as(
                        type_=NoteAttachmentPaymentBatchDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_attachment_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteAttachmentPaymentListing]]:
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
        HttpResponse[typing.List[NoteAttachmentPaymentListing]]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/payment/{encode_path_param(payment_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentPaymentListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentPaymentListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_attachment_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentPaymentCreate]:
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
        HttpResponse[NoteAttachmentPaymentCreate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/payment/{encode_path_param(payment_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentPaymentCreate,
                    parse_obj_as(
                        type_=NoteAttachmentPaymentCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_attachment_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentPaymentRead]:
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
        HttpResponse[NoteAttachmentPaymentRead]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/payment/{encode_path_param(payment_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentPaymentRead,
                    parse_obj_as(
                        type_=NoteAttachmentPaymentRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[NoteAttachmentPaymentUpdate]:
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
        HttpResponse[NoteAttachmentPaymentUpdate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/payment/{encode_path_param(payment_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentPaymentUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentPaymentUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_attachment_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentPaymentDelete]:
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
        HttpResponse[NoteAttachmentPaymentDelete]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/payment/{encode_path_param(payment_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentPaymentDelete,
                    parse_obj_as(
                        type_=NoteAttachmentPaymentDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_attachment_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteAttachmentRequestInquiryBatchListing]]:
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
        HttpResponse[typing.List[NoteAttachmentRequestInquiryBatchListing]]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-inquiry-batch/{encode_path_param(request_inquiry_batch_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentRequestInquiryBatchListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentRequestInquiryBatchListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_attachment_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentRequestInquiryBatchCreate]:
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
        HttpResponse[NoteAttachmentRequestInquiryBatchCreate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-inquiry-batch/{encode_path_param(request_inquiry_batch_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentRequestInquiryBatchCreate,
                    parse_obj_as(
                        type_=NoteAttachmentRequestInquiryBatchCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_attachment_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentRequestInquiryBatchRead]:
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
        HttpResponse[NoteAttachmentRequestInquiryBatchRead]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-inquiry-batch/{encode_path_param(request_inquiry_batch_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentRequestInquiryBatchRead,
                    parse_obj_as(
                        type_=NoteAttachmentRequestInquiryBatchRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[NoteAttachmentRequestInquiryBatchUpdate]:
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
        HttpResponse[NoteAttachmentRequestInquiryBatchUpdate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-inquiry-batch/{encode_path_param(request_inquiry_batch_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentRequestInquiryBatchUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentRequestInquiryBatchUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_attachment_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentRequestInquiryBatchDelete]:
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
        HttpResponse[NoteAttachmentRequestInquiryBatchDelete]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-inquiry-batch/{encode_path_param(request_inquiry_batch_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentRequestInquiryBatchDelete,
                    parse_obj_as(
                        type_=NoteAttachmentRequestInquiryBatchDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_attachment_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteAttachmentRequestInquiryListing]]:
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
        HttpResponse[typing.List[NoteAttachmentRequestInquiryListing]]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-inquiry/{encode_path_param(request_inquiry_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentRequestInquiryListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentRequestInquiryListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_attachment_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentRequestInquiryCreate]:
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
        HttpResponse[NoteAttachmentRequestInquiryCreate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-inquiry/{encode_path_param(request_inquiry_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentRequestInquiryCreate,
                    parse_obj_as(
                        type_=NoteAttachmentRequestInquiryCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_attachment_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentRequestInquiryRead]:
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
        HttpResponse[NoteAttachmentRequestInquiryRead]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-inquiry/{encode_path_param(request_inquiry_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentRequestInquiryRead,
                    parse_obj_as(
                        type_=NoteAttachmentRequestInquiryRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[NoteAttachmentRequestInquiryUpdate]:
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
        HttpResponse[NoteAttachmentRequestInquiryUpdate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-inquiry/{encode_path_param(request_inquiry_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentRequestInquiryUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentRequestInquiryUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_attachment_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentRequestInquiryDelete]:
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
        HttpResponse[NoteAttachmentRequestInquiryDelete]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-inquiry/{encode_path_param(request_inquiry_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentRequestInquiryDelete,
                    parse_obj_as(
                        type_=NoteAttachmentRequestInquiryDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_attachment_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteAttachmentRequestResponseListing]]:
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
        HttpResponse[typing.List[NoteAttachmentRequestResponseListing]]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-response/{encode_path_param(request_response_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentRequestResponseListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentRequestResponseListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_attachment_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentRequestResponseCreate]:
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
        HttpResponse[NoteAttachmentRequestResponseCreate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-response/{encode_path_param(request_response_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentRequestResponseCreate,
                    parse_obj_as(
                        type_=NoteAttachmentRequestResponseCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_attachment_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentRequestResponseRead]:
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
        HttpResponse[NoteAttachmentRequestResponseRead]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-response/{encode_path_param(request_response_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentRequestResponseRead,
                    parse_obj_as(
                        type_=NoteAttachmentRequestResponseRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[NoteAttachmentRequestResponseUpdate]:
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
        HttpResponse[NoteAttachmentRequestResponseUpdate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-response/{encode_path_param(request_response_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentRequestResponseUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentRequestResponseUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_attachment_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentRequestResponseDelete]:
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
        HttpResponse[NoteAttachmentRequestResponseDelete]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-response/{encode_path_param(request_response_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentRequestResponseDelete,
                    parse_obj_as(
                        type_=NoteAttachmentRequestResponseDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_attachment_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteAttachmentSchedulePaymentBatchListing]]:
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
        HttpResponse[typing.List[NoteAttachmentSchedulePaymentBatchListing]]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment-batch/{encode_path_param(schedule_payment_batch_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentSchedulePaymentBatchListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentSchedulePaymentBatchListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_attachment_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentSchedulePaymentBatchCreate]:
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
        HttpResponse[NoteAttachmentSchedulePaymentBatchCreate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment-batch/{encode_path_param(schedule_payment_batch_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentSchedulePaymentBatchCreate,
                    parse_obj_as(
                        type_=NoteAttachmentSchedulePaymentBatchCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_attachment_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentSchedulePaymentBatchRead]:
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
        HttpResponse[NoteAttachmentSchedulePaymentBatchRead]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment-batch/{encode_path_param(schedule_payment_batch_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentSchedulePaymentBatchRead,
                    parse_obj_as(
                        type_=NoteAttachmentSchedulePaymentBatchRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[NoteAttachmentSchedulePaymentBatchUpdate]:
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
        HttpResponse[NoteAttachmentSchedulePaymentBatchUpdate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment-batch/{encode_path_param(schedule_payment_batch_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentSchedulePaymentBatchUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentSchedulePaymentBatchUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_attachment_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentSchedulePaymentBatchDelete]:
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
        HttpResponse[NoteAttachmentSchedulePaymentBatchDelete]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment-batch/{encode_path_param(schedule_payment_batch_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentSchedulePaymentBatchDelete,
                    parse_obj_as(
                        type_=NoteAttachmentSchedulePaymentBatchDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_attachment_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteAttachmentSchedulePaymentListing]]:
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
        HttpResponse[typing.List[NoteAttachmentSchedulePaymentListing]]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment/{encode_path_param(schedule_payment_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentSchedulePaymentListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentSchedulePaymentListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_attachment_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentSchedulePaymentCreate]:
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
        HttpResponse[NoteAttachmentSchedulePaymentCreate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment/{encode_path_param(schedule_payment_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentSchedulePaymentCreate,
                    parse_obj_as(
                        type_=NoteAttachmentSchedulePaymentCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_attachment_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentSchedulePaymentRead]:
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
        HttpResponse[NoteAttachmentSchedulePaymentRead]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment/{encode_path_param(schedule_payment_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentSchedulePaymentRead,
                    parse_obj_as(
                        type_=NoteAttachmentSchedulePaymentRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[NoteAttachmentSchedulePaymentUpdate]:
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
        HttpResponse[NoteAttachmentSchedulePaymentUpdate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment/{encode_path_param(schedule_payment_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentSchedulePaymentUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentSchedulePaymentUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_attachment_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentSchedulePaymentDelete]:
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
        HttpResponse[NoteAttachmentSchedulePaymentDelete]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment/{encode_path_param(schedule_payment_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentSchedulePaymentDelete,
                    parse_obj_as(
                        type_=NoteAttachmentSchedulePaymentDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_attachment_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteAttachmentScheduleInstanceListing]]:
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
        HttpResponse[typing.List[NoteAttachmentScheduleInstanceListing]]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule/{encode_path_param(schedule_id)}/schedule-instance/{encode_path_param(schedule_instance_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentScheduleInstanceListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentScheduleInstanceListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[NoteAttachmentScheduleInstanceCreate]:
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
        HttpResponse[NoteAttachmentScheduleInstanceCreate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule/{encode_path_param(schedule_id)}/schedule-instance/{encode_path_param(schedule_instance_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentScheduleInstanceCreate,
                    parse_obj_as(
                        type_=NoteAttachmentScheduleInstanceCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_attachment_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentScheduleInstanceRead]:
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
        HttpResponse[NoteAttachmentScheduleInstanceRead]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule/{encode_path_param(schedule_id)}/schedule-instance/{encode_path_param(schedule_instance_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentScheduleInstanceRead,
                    parse_obj_as(
                        type_=NoteAttachmentScheduleInstanceRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[NoteAttachmentScheduleInstanceUpdate]:
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
        HttpResponse[NoteAttachmentScheduleInstanceUpdate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule/{encode_path_param(schedule_id)}/schedule-instance/{encode_path_param(schedule_instance_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentScheduleInstanceUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentScheduleInstanceUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_attachment_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentScheduleInstanceDelete]:
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
        HttpResponse[NoteAttachmentScheduleInstanceDelete]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule/{encode_path_param(schedule_id)}/schedule-instance/{encode_path_param(schedule_instance_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentScheduleInstanceDelete,
                    parse_obj_as(
                        type_=NoteAttachmentScheduleInstanceDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteAttachmentSofortMerchantTransactionListing]]:
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
        HttpResponse[typing.List[NoteAttachmentSofortMerchantTransactionListing]]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/sofort-merchant-transaction/{encode_path_param(sofort_merchant_transaction_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentSofortMerchantTransactionListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentSofortMerchantTransactionListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentSofortMerchantTransactionCreate]:
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
        HttpResponse[NoteAttachmentSofortMerchantTransactionCreate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/sofort-merchant-transaction/{encode_path_param(sofort_merchant_transaction_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentSofortMerchantTransactionCreate,
                    parse_obj_as(
                        type_=NoteAttachmentSofortMerchantTransactionCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentSofortMerchantTransactionRead]:
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
        HttpResponse[NoteAttachmentSofortMerchantTransactionRead]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/sofort-merchant-transaction/{encode_path_param(sofort_merchant_transaction_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentSofortMerchantTransactionRead,
                    parse_obj_as(
                        type_=NoteAttachmentSofortMerchantTransactionRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[NoteAttachmentSofortMerchantTransactionUpdate]:
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
        HttpResponse[NoteAttachmentSofortMerchantTransactionUpdate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/sofort-merchant-transaction/{encode_path_param(sofort_merchant_transaction_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentSofortMerchantTransactionUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentSofortMerchantTransactionUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentSofortMerchantTransactionDelete]:
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
        HttpResponse[NoteAttachmentSofortMerchantTransactionDelete]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/sofort-merchant-transaction/{encode_path_param(sofort_merchant_transaction_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentSofortMerchantTransactionDelete,
                    parse_obj_as(
                        type_=NoteAttachmentSofortMerchantTransactionDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_attachment_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentListing]]:
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
        HttpResponse[typing.List[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentListing]]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/switch-service-payment/{encode_path_param(switch_service_payment_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_attachment_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentCreate]:
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
        HttpResponse[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentCreate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/switch-service-payment/{encode_path_param(switch_service_payment_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentCreate,
                    parse_obj_as(
                        type_=NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_attachment_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentRead]:
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
        HttpResponse[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentRead]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/switch-service-payment/{encode_path_param(switch_service_payment_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentRead,
                    parse_obj_as(
                        type_=NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentUpdate]:
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
        HttpResponse[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentUpdate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/switch-service-payment/{encode_path_param(switch_service_payment_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_attachment_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentDelete]:
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
        HttpResponse[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentDelete]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/switch-service-payment/{encode_path_param(switch_service_payment_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentDelete,
                    parse_obj_as(
                        type_=NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteAttachmentWhitelistResultListing]]:
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
        HttpResponse[typing.List[NoteAttachmentWhitelistResultListing]]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/whitelist/{encode_path_param(whitelist_id)}/whitelist-result/{encode_path_param(whitelist_result_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentWhitelistResultListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentWhitelistResultListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[NoteAttachmentWhitelistResultCreate]:
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
        HttpResponse[NoteAttachmentWhitelistResultCreate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/whitelist/{encode_path_param(whitelist_id)}/whitelist-result/{encode_path_param(whitelist_result_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentWhitelistResultCreate,
                    parse_obj_as(
                        type_=NoteAttachmentWhitelistResultCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentWhitelistResultRead]:
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
        HttpResponse[NoteAttachmentWhitelistResultRead]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/whitelist/{encode_path_param(whitelist_id)}/whitelist-result/{encode_path_param(whitelist_result_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentWhitelistResultRead,
                    parse_obj_as(
                        type_=NoteAttachmentWhitelistResultRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[NoteAttachmentWhitelistResultUpdate]:
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
        HttpResponse[NoteAttachmentWhitelistResultUpdate]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/whitelist/{encode_path_param(whitelist_id)}/whitelist-result/{encode_path_param(whitelist_result_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentWhitelistResultUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentWhitelistResultUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteAttachmentWhitelistResultDelete]:
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
        HttpResponse[NoteAttachmentWhitelistResultDelete]
            Used to manage attachment notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/whitelist/{encode_path_param(whitelist_id)}/whitelist-result/{encode_path_param(whitelist_result_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentWhitelistResultDelete,
                    parse_obj_as(
                        type_=NoteAttachmentWhitelistResultDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawNoteAttachmentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteAttachmentBunqMeFundraiserResultListing]]:
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
        AsyncHttpResponse[typing.List[NoteAttachmentBunqMeFundraiserResultListing]]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/bunqme-fundraiser-result/{encode_path_param(bunqme_fundraiser_result_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentBunqMeFundraiserResultListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentBunqMeFundraiserResultListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentBunqMeFundraiserResultCreate]:
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
        AsyncHttpResponse[NoteAttachmentBunqMeFundraiserResultCreate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/bunqme-fundraiser-result/{encode_path_param(bunqme_fundraiser_result_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentBunqMeFundraiserResultCreate,
                    parse_obj_as(
                        type_=NoteAttachmentBunqMeFundraiserResultCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentBunqMeFundraiserResultRead]:
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
        AsyncHttpResponse[NoteAttachmentBunqMeFundraiserResultRead]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/bunqme-fundraiser-result/{encode_path_param(bunqme_fundraiser_result_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentBunqMeFundraiserResultRead,
                    parse_obj_as(
                        type_=NoteAttachmentBunqMeFundraiserResultRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[NoteAttachmentBunqMeFundraiserResultUpdate]:
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
        AsyncHttpResponse[NoteAttachmentBunqMeFundraiserResultUpdate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/bunqme-fundraiser-result/{encode_path_param(bunqme_fundraiser_result_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentBunqMeFundraiserResultUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentBunqMeFundraiserResultUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentBunqMeFundraiserResultDelete]:
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
        AsyncHttpResponse[NoteAttachmentBunqMeFundraiserResultDelete]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/bunqme-fundraiser-result/{encode_path_param(bunqme_fundraiser_result_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentBunqMeFundraiserResultDelete,
                    parse_obj_as(
                        type_=NoteAttachmentBunqMeFundraiserResultDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_attachment_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteAttachmentDraftPaymentListing]]:
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
        AsyncHttpResponse[typing.List[NoteAttachmentDraftPaymentListing]]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/draft-payment/{encode_path_param(draft_payment_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentDraftPaymentListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentDraftPaymentListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_attachment_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentDraftPaymentCreate]:
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
        AsyncHttpResponse[NoteAttachmentDraftPaymentCreate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/draft-payment/{encode_path_param(draft_payment_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentDraftPaymentCreate,
                    parse_obj_as(
                        type_=NoteAttachmentDraftPaymentCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_attachment_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentDraftPaymentRead]:
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
        AsyncHttpResponse[NoteAttachmentDraftPaymentRead]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/draft-payment/{encode_path_param(draft_payment_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentDraftPaymentRead,
                    parse_obj_as(
                        type_=NoteAttachmentDraftPaymentRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[NoteAttachmentDraftPaymentUpdate]:
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
        AsyncHttpResponse[NoteAttachmentDraftPaymentUpdate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/draft-payment/{encode_path_param(draft_payment_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentDraftPaymentUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentDraftPaymentUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_attachment_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentDraftPaymentDelete]:
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
        AsyncHttpResponse[NoteAttachmentDraftPaymentDelete]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/draft-payment/{encode_path_param(draft_payment_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentDraftPaymentDelete,
                    parse_obj_as(
                        type_=NoteAttachmentDraftPaymentDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteAttachmentIdealMerchantTransactionListing]]:
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
        AsyncHttpResponse[typing.List[NoteAttachmentIdealMerchantTransactionListing]]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/ideal-merchant-transaction/{encode_path_param(ideal_merchant_transaction_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentIdealMerchantTransactionListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentIdealMerchantTransactionListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentIdealMerchantTransactionCreate]:
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
        AsyncHttpResponse[NoteAttachmentIdealMerchantTransactionCreate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/ideal-merchant-transaction/{encode_path_param(ideal_merchant_transaction_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentIdealMerchantTransactionCreate,
                    parse_obj_as(
                        type_=NoteAttachmentIdealMerchantTransactionCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentIdealMerchantTransactionRead]:
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
        AsyncHttpResponse[NoteAttachmentIdealMerchantTransactionRead]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/ideal-merchant-transaction/{encode_path_param(ideal_merchant_transaction_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentIdealMerchantTransactionRead,
                    parse_obj_as(
                        type_=NoteAttachmentIdealMerchantTransactionRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[NoteAttachmentIdealMerchantTransactionUpdate]:
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
        AsyncHttpResponse[NoteAttachmentIdealMerchantTransactionUpdate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/ideal-merchant-transaction/{encode_path_param(ideal_merchant_transaction_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentIdealMerchantTransactionUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentIdealMerchantTransactionUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentIdealMerchantTransactionDelete]:
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
        AsyncHttpResponse[NoteAttachmentIdealMerchantTransactionDelete]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/ideal-merchant-transaction/{encode_path_param(ideal_merchant_transaction_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentIdealMerchantTransactionDelete,
                    parse_obj_as(
                        type_=NoteAttachmentIdealMerchantTransactionDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_attachment_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteAttachmentMasterCardActionListing]]:
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
        AsyncHttpResponse[typing.List[NoteAttachmentMasterCardActionListing]]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/mastercard-action/{encode_path_param(mastercard_action_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentMasterCardActionListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentMasterCardActionListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_attachment_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentMasterCardActionCreate]:
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
        AsyncHttpResponse[NoteAttachmentMasterCardActionCreate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/mastercard-action/{encode_path_param(mastercard_action_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentMasterCardActionCreate,
                    parse_obj_as(
                        type_=NoteAttachmentMasterCardActionCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_attachment_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentMasterCardActionRead]:
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
        AsyncHttpResponse[NoteAttachmentMasterCardActionRead]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/mastercard-action/{encode_path_param(mastercard_action_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentMasterCardActionRead,
                    parse_obj_as(
                        type_=NoteAttachmentMasterCardActionRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[NoteAttachmentMasterCardActionUpdate]:
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
        AsyncHttpResponse[NoteAttachmentMasterCardActionUpdate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/mastercard-action/{encode_path_param(mastercard_action_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentMasterCardActionUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentMasterCardActionUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_attachment_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentMasterCardActionDelete]:
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
        AsyncHttpResponse[NoteAttachmentMasterCardActionDelete]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/mastercard-action/{encode_path_param(mastercard_action_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentMasterCardActionDelete,
                    parse_obj_as(
                        type_=NoteAttachmentMasterCardActionDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_attachment_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteAttachmentPaymentBatchListing]]:
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
        AsyncHttpResponse[typing.List[NoteAttachmentPaymentBatchListing]]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/payment-batch/{encode_path_param(payment_batch_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentPaymentBatchListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentPaymentBatchListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_attachment_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentPaymentBatchCreate]:
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
        AsyncHttpResponse[NoteAttachmentPaymentBatchCreate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/payment-batch/{encode_path_param(payment_batch_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentPaymentBatchCreate,
                    parse_obj_as(
                        type_=NoteAttachmentPaymentBatchCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_attachment_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentPaymentBatchRead]:
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
        AsyncHttpResponse[NoteAttachmentPaymentBatchRead]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/payment-batch/{encode_path_param(payment_batch_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentPaymentBatchRead,
                    parse_obj_as(
                        type_=NoteAttachmentPaymentBatchRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[NoteAttachmentPaymentBatchUpdate]:
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
        AsyncHttpResponse[NoteAttachmentPaymentBatchUpdate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/payment-batch/{encode_path_param(payment_batch_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentPaymentBatchUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentPaymentBatchUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_attachment_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentPaymentBatchDelete]:
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
        AsyncHttpResponse[NoteAttachmentPaymentBatchDelete]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/payment-batch/{encode_path_param(payment_batch_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentPaymentBatchDelete,
                    parse_obj_as(
                        type_=NoteAttachmentPaymentBatchDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_attachment_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteAttachmentPaymentListing]]:
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
        AsyncHttpResponse[typing.List[NoteAttachmentPaymentListing]]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/payment/{encode_path_param(payment_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentPaymentListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentPaymentListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_attachment_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentPaymentCreate]:
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
        AsyncHttpResponse[NoteAttachmentPaymentCreate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/payment/{encode_path_param(payment_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentPaymentCreate,
                    parse_obj_as(
                        type_=NoteAttachmentPaymentCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_attachment_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentPaymentRead]:
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
        AsyncHttpResponse[NoteAttachmentPaymentRead]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/payment/{encode_path_param(payment_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentPaymentRead,
                    parse_obj_as(
                        type_=NoteAttachmentPaymentRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[NoteAttachmentPaymentUpdate]:
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
        AsyncHttpResponse[NoteAttachmentPaymentUpdate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/payment/{encode_path_param(payment_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentPaymentUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentPaymentUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_attachment_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentPaymentDelete]:
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
        AsyncHttpResponse[NoteAttachmentPaymentDelete]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/payment/{encode_path_param(payment_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentPaymentDelete,
                    parse_obj_as(
                        type_=NoteAttachmentPaymentDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_attachment_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteAttachmentRequestInquiryBatchListing]]:
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
        AsyncHttpResponse[typing.List[NoteAttachmentRequestInquiryBatchListing]]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-inquiry-batch/{encode_path_param(request_inquiry_batch_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentRequestInquiryBatchListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentRequestInquiryBatchListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_attachment_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentRequestInquiryBatchCreate]:
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
        AsyncHttpResponse[NoteAttachmentRequestInquiryBatchCreate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-inquiry-batch/{encode_path_param(request_inquiry_batch_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentRequestInquiryBatchCreate,
                    parse_obj_as(
                        type_=NoteAttachmentRequestInquiryBatchCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_attachment_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentRequestInquiryBatchRead]:
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
        AsyncHttpResponse[NoteAttachmentRequestInquiryBatchRead]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-inquiry-batch/{encode_path_param(request_inquiry_batch_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentRequestInquiryBatchRead,
                    parse_obj_as(
                        type_=NoteAttachmentRequestInquiryBatchRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[NoteAttachmentRequestInquiryBatchUpdate]:
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
        AsyncHttpResponse[NoteAttachmentRequestInquiryBatchUpdate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-inquiry-batch/{encode_path_param(request_inquiry_batch_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentRequestInquiryBatchUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentRequestInquiryBatchUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_attachment_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentRequestInquiryBatchDelete]:
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
        AsyncHttpResponse[NoteAttachmentRequestInquiryBatchDelete]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-inquiry-batch/{encode_path_param(request_inquiry_batch_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentRequestInquiryBatchDelete,
                    parse_obj_as(
                        type_=NoteAttachmentRequestInquiryBatchDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_attachment_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteAttachmentRequestInquiryListing]]:
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
        AsyncHttpResponse[typing.List[NoteAttachmentRequestInquiryListing]]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-inquiry/{encode_path_param(request_inquiry_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentRequestInquiryListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentRequestInquiryListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_attachment_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentRequestInquiryCreate]:
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
        AsyncHttpResponse[NoteAttachmentRequestInquiryCreate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-inquiry/{encode_path_param(request_inquiry_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentRequestInquiryCreate,
                    parse_obj_as(
                        type_=NoteAttachmentRequestInquiryCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_attachment_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentRequestInquiryRead]:
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
        AsyncHttpResponse[NoteAttachmentRequestInquiryRead]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-inquiry/{encode_path_param(request_inquiry_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentRequestInquiryRead,
                    parse_obj_as(
                        type_=NoteAttachmentRequestInquiryRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[NoteAttachmentRequestInquiryUpdate]:
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
        AsyncHttpResponse[NoteAttachmentRequestInquiryUpdate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-inquiry/{encode_path_param(request_inquiry_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentRequestInquiryUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentRequestInquiryUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_attachment_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentRequestInquiryDelete]:
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
        AsyncHttpResponse[NoteAttachmentRequestInquiryDelete]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-inquiry/{encode_path_param(request_inquiry_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentRequestInquiryDelete,
                    parse_obj_as(
                        type_=NoteAttachmentRequestInquiryDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_attachment_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteAttachmentRequestResponseListing]]:
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
        AsyncHttpResponse[typing.List[NoteAttachmentRequestResponseListing]]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-response/{encode_path_param(request_response_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentRequestResponseListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentRequestResponseListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_attachment_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentRequestResponseCreate]:
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
        AsyncHttpResponse[NoteAttachmentRequestResponseCreate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-response/{encode_path_param(request_response_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentRequestResponseCreate,
                    parse_obj_as(
                        type_=NoteAttachmentRequestResponseCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_attachment_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentRequestResponseRead]:
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
        AsyncHttpResponse[NoteAttachmentRequestResponseRead]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-response/{encode_path_param(request_response_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentRequestResponseRead,
                    parse_obj_as(
                        type_=NoteAttachmentRequestResponseRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[NoteAttachmentRequestResponseUpdate]:
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
        AsyncHttpResponse[NoteAttachmentRequestResponseUpdate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-response/{encode_path_param(request_response_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentRequestResponseUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentRequestResponseUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_attachment_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentRequestResponseDelete]:
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
        AsyncHttpResponse[NoteAttachmentRequestResponseDelete]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-response/{encode_path_param(request_response_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentRequestResponseDelete,
                    parse_obj_as(
                        type_=NoteAttachmentRequestResponseDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_attachment_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteAttachmentSchedulePaymentBatchListing]]:
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
        AsyncHttpResponse[typing.List[NoteAttachmentSchedulePaymentBatchListing]]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment-batch/{encode_path_param(schedule_payment_batch_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentSchedulePaymentBatchListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentSchedulePaymentBatchListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_attachment_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentSchedulePaymentBatchCreate]:
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
        AsyncHttpResponse[NoteAttachmentSchedulePaymentBatchCreate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment-batch/{encode_path_param(schedule_payment_batch_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentSchedulePaymentBatchCreate,
                    parse_obj_as(
                        type_=NoteAttachmentSchedulePaymentBatchCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_attachment_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentSchedulePaymentBatchRead]:
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
        AsyncHttpResponse[NoteAttachmentSchedulePaymentBatchRead]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment-batch/{encode_path_param(schedule_payment_batch_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentSchedulePaymentBatchRead,
                    parse_obj_as(
                        type_=NoteAttachmentSchedulePaymentBatchRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[NoteAttachmentSchedulePaymentBatchUpdate]:
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
        AsyncHttpResponse[NoteAttachmentSchedulePaymentBatchUpdate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment-batch/{encode_path_param(schedule_payment_batch_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentSchedulePaymentBatchUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentSchedulePaymentBatchUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_attachment_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentSchedulePaymentBatchDelete]:
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
        AsyncHttpResponse[NoteAttachmentSchedulePaymentBatchDelete]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment-batch/{encode_path_param(schedule_payment_batch_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentSchedulePaymentBatchDelete,
                    parse_obj_as(
                        type_=NoteAttachmentSchedulePaymentBatchDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_attachment_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteAttachmentSchedulePaymentListing]]:
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
        AsyncHttpResponse[typing.List[NoteAttachmentSchedulePaymentListing]]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment/{encode_path_param(schedule_payment_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentSchedulePaymentListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentSchedulePaymentListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_attachment_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentSchedulePaymentCreate]:
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
        AsyncHttpResponse[NoteAttachmentSchedulePaymentCreate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment/{encode_path_param(schedule_payment_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentSchedulePaymentCreate,
                    parse_obj_as(
                        type_=NoteAttachmentSchedulePaymentCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_attachment_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentSchedulePaymentRead]:
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
        AsyncHttpResponse[NoteAttachmentSchedulePaymentRead]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment/{encode_path_param(schedule_payment_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentSchedulePaymentRead,
                    parse_obj_as(
                        type_=NoteAttachmentSchedulePaymentRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[NoteAttachmentSchedulePaymentUpdate]:
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
        AsyncHttpResponse[NoteAttachmentSchedulePaymentUpdate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment/{encode_path_param(schedule_payment_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentSchedulePaymentUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentSchedulePaymentUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_attachment_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentSchedulePaymentDelete]:
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
        AsyncHttpResponse[NoteAttachmentSchedulePaymentDelete]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment/{encode_path_param(schedule_payment_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentSchedulePaymentDelete,
                    parse_obj_as(
                        type_=NoteAttachmentSchedulePaymentDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_attachment_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteAttachmentScheduleInstanceListing]]:
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
        AsyncHttpResponse[typing.List[NoteAttachmentScheduleInstanceListing]]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule/{encode_path_param(schedule_id)}/schedule-instance/{encode_path_param(schedule_instance_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentScheduleInstanceListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentScheduleInstanceListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[NoteAttachmentScheduleInstanceCreate]:
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
        AsyncHttpResponse[NoteAttachmentScheduleInstanceCreate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule/{encode_path_param(schedule_id)}/schedule-instance/{encode_path_param(schedule_instance_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentScheduleInstanceCreate,
                    parse_obj_as(
                        type_=NoteAttachmentScheduleInstanceCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_attachment_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentScheduleInstanceRead]:
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
        AsyncHttpResponse[NoteAttachmentScheduleInstanceRead]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule/{encode_path_param(schedule_id)}/schedule-instance/{encode_path_param(schedule_instance_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentScheduleInstanceRead,
                    parse_obj_as(
                        type_=NoteAttachmentScheduleInstanceRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[NoteAttachmentScheduleInstanceUpdate]:
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
        AsyncHttpResponse[NoteAttachmentScheduleInstanceUpdate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule/{encode_path_param(schedule_id)}/schedule-instance/{encode_path_param(schedule_instance_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentScheduleInstanceUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentScheduleInstanceUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_attachment_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentScheduleInstanceDelete]:
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
        AsyncHttpResponse[NoteAttachmentScheduleInstanceDelete]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule/{encode_path_param(schedule_id)}/schedule-instance/{encode_path_param(schedule_instance_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentScheduleInstanceDelete,
                    parse_obj_as(
                        type_=NoteAttachmentScheduleInstanceDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteAttachmentSofortMerchantTransactionListing]]:
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
        AsyncHttpResponse[typing.List[NoteAttachmentSofortMerchantTransactionListing]]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/sofort-merchant-transaction/{encode_path_param(sofort_merchant_transaction_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentSofortMerchantTransactionListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentSofortMerchantTransactionListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentSofortMerchantTransactionCreate]:
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
        AsyncHttpResponse[NoteAttachmentSofortMerchantTransactionCreate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/sofort-merchant-transaction/{encode_path_param(sofort_merchant_transaction_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentSofortMerchantTransactionCreate,
                    parse_obj_as(
                        type_=NoteAttachmentSofortMerchantTransactionCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentSofortMerchantTransactionRead]:
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
        AsyncHttpResponse[NoteAttachmentSofortMerchantTransactionRead]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/sofort-merchant-transaction/{encode_path_param(sofort_merchant_transaction_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentSofortMerchantTransactionRead,
                    parse_obj_as(
                        type_=NoteAttachmentSofortMerchantTransactionRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[NoteAttachmentSofortMerchantTransactionUpdate]:
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
        AsyncHttpResponse[NoteAttachmentSofortMerchantTransactionUpdate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/sofort-merchant-transaction/{encode_path_param(sofort_merchant_transaction_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentSofortMerchantTransactionUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentSofortMerchantTransactionUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentSofortMerchantTransactionDelete]:
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
        AsyncHttpResponse[NoteAttachmentSofortMerchantTransactionDelete]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/sofort-merchant-transaction/{encode_path_param(sofort_merchant_transaction_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentSofortMerchantTransactionDelete,
                    parse_obj_as(
                        type_=NoteAttachmentSofortMerchantTransactionDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_attachment_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentListing]]:
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
        AsyncHttpResponse[typing.List[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentListing]]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/switch-service-payment/{encode_path_param(switch_service_payment_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_attachment_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        *,
        attachment_id: int,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentCreate]:
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
        AsyncHttpResponse[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentCreate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/switch-service-payment/{encode_path_param(switch_service_payment_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentCreate,
                    parse_obj_as(
                        type_=NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_attachment_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentRead]:
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
        AsyncHttpResponse[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentRead]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/switch-service-payment/{encode_path_param(switch_service_payment_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentRead,
                    parse_obj_as(
                        type_=NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentUpdate]:
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
        AsyncHttpResponse[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentUpdate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/switch-service-payment/{encode_path_param(switch_service_payment_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_attachment_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentDelete]:
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
        AsyncHttpResponse[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentDelete]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/switch-service-payment/{encode_path_param(switch_service_payment_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentDelete,
                    parse_obj_as(
                        type_=NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteAttachmentWhitelistResultListing]]:
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
        AsyncHttpResponse[typing.List[NoteAttachmentWhitelistResultListing]]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/whitelist/{encode_path_param(whitelist_id)}/whitelist-result/{encode_path_param(whitelist_result_id)}/note-attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteAttachmentWhitelistResultListing],
                    parse_obj_as(
                        type_=typing.List[NoteAttachmentWhitelistResultListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[NoteAttachmentWhitelistResultCreate]:
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
        AsyncHttpResponse[NoteAttachmentWhitelistResultCreate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/whitelist/{encode_path_param(whitelist_id)}/whitelist-result/{encode_path_param(whitelist_result_id)}/note-attachment",
            method="POST",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentWhitelistResultCreate,
                    parse_obj_as(
                        type_=NoteAttachmentWhitelistResultCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentWhitelistResultRead]:
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
        AsyncHttpResponse[NoteAttachmentWhitelistResultRead]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/whitelist/{encode_path_param(whitelist_id)}/whitelist-result/{encode_path_param(whitelist_result_id)}/note-attachment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentWhitelistResultRead,
                    parse_obj_as(
                        type_=NoteAttachmentWhitelistResultRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[NoteAttachmentWhitelistResultUpdate]:
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
        AsyncHttpResponse[NoteAttachmentWhitelistResultUpdate]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/whitelist/{encode_path_param(whitelist_id)}/whitelist-result/{encode_path_param(whitelist_result_id)}/note-attachment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "attachment_id": attachment_id,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentWhitelistResultUpdate,
                    parse_obj_as(
                        type_=NoteAttachmentWhitelistResultUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteAttachmentWhitelistResultDelete]:
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
        AsyncHttpResponse[NoteAttachmentWhitelistResultDelete]
            Used to manage attachment notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/whitelist/{encode_path_param(whitelist_id)}/whitelist-result/{encode_path_param(whitelist_result_id)}/note-attachment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteAttachmentWhitelistResultDelete,
                    parse_obj_as(
                        type_=NoteAttachmentWhitelistResultDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
