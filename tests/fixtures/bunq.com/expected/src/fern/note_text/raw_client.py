

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
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


OMIT = typing.cast(typing.Any, ...)


class RawNoteTextClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_note_text_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteTextBunqMeFundraiserResultListing]]:
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
        HttpResponse[typing.List[NoteTextBunqMeFundraiserResultListing]]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/bunqme-fundraiser-result/{jsonable_encoder(bunqme_fundraiser_result_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextBunqMeFundraiserResultListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextBunqMeFundraiserResultListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_text_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextBunqMeFundraiserResultCreate]:
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
        HttpResponse[NoteTextBunqMeFundraiserResultCreate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/bunqme-fundraiser-result/{jsonable_encoder(bunqme_fundraiser_result_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextBunqMeFundraiserResultCreate,
                    parse_obj_as(
                        type_=NoteTextBunqMeFundraiserResultCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_text_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextBunqMeFundraiserResultRead]:
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
        HttpResponse[NoteTextBunqMeFundraiserResultRead]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/bunqme-fundraiser-result/{jsonable_encoder(bunqme_fundraiser_result_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextBunqMeFundraiserResultRead,
                    parse_obj_as(
                        type_=NoteTextBunqMeFundraiserResultRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_note_text_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextBunqMeFundraiserResultUpdate]:
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
        HttpResponse[NoteTextBunqMeFundraiserResultUpdate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/bunqme-fundraiser-result/{jsonable_encoder(bunqme_fundraiser_result_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextBunqMeFundraiserResultUpdate,
                    parse_obj_as(
                        type_=NoteTextBunqMeFundraiserResultUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_text_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextBunqMeFundraiserResultDelete]:
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
        HttpResponse[NoteTextBunqMeFundraiserResultDelete]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/bunqme-fundraiser-result/{jsonable_encoder(bunqme_fundraiser_result_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextBunqMeFundraiserResultDelete,
                    parse_obj_as(
                        type_=NoteTextBunqMeFundraiserResultDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_text_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteTextDraftPaymentListing]]:
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
        HttpResponse[typing.List[NoteTextDraftPaymentListing]]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/draft-payment/{jsonable_encoder(draft_payment_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextDraftPaymentListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextDraftPaymentListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_text_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextDraftPaymentCreate]:
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
        HttpResponse[NoteTextDraftPaymentCreate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/draft-payment/{jsonable_encoder(draft_payment_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextDraftPaymentCreate,
                    parse_obj_as(
                        type_=NoteTextDraftPaymentCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_text_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextDraftPaymentRead]:
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
        HttpResponse[NoteTextDraftPaymentRead]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/draft-payment/{jsonable_encoder(draft_payment_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextDraftPaymentRead,
                    parse_obj_as(
                        type_=NoteTextDraftPaymentRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_note_text_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextDraftPaymentUpdate]:
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
        HttpResponse[NoteTextDraftPaymentUpdate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/draft-payment/{jsonable_encoder(draft_payment_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextDraftPaymentUpdate,
                    parse_obj_as(
                        type_=NoteTextDraftPaymentUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_text_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextDraftPaymentDelete]:
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
        HttpResponse[NoteTextDraftPaymentDelete]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/draft-payment/{jsonable_encoder(draft_payment_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextDraftPaymentDelete,
                    parse_obj_as(
                        type_=NoteTextDraftPaymentDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_text_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteTextIdealMerchantTransactionListing]]:
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
        HttpResponse[typing.List[NoteTextIdealMerchantTransactionListing]]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/ideal-merchant-transaction/{jsonable_encoder(ideal_merchant_transaction_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextIdealMerchantTransactionListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextIdealMerchantTransactionListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_text_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextIdealMerchantTransactionCreate]:
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
        HttpResponse[NoteTextIdealMerchantTransactionCreate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/ideal-merchant-transaction/{jsonable_encoder(ideal_merchant_transaction_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextIdealMerchantTransactionCreate,
                    parse_obj_as(
                        type_=NoteTextIdealMerchantTransactionCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_text_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextIdealMerchantTransactionRead]:
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
        HttpResponse[NoteTextIdealMerchantTransactionRead]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/ideal-merchant-transaction/{jsonable_encoder(ideal_merchant_transaction_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextIdealMerchantTransactionRead,
                    parse_obj_as(
                        type_=NoteTextIdealMerchantTransactionRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_note_text_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextIdealMerchantTransactionUpdate]:
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
        HttpResponse[NoteTextIdealMerchantTransactionUpdate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/ideal-merchant-transaction/{jsonable_encoder(ideal_merchant_transaction_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextIdealMerchantTransactionUpdate,
                    parse_obj_as(
                        type_=NoteTextIdealMerchantTransactionUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_text_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextIdealMerchantTransactionDelete]:
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
        HttpResponse[NoteTextIdealMerchantTransactionDelete]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/ideal-merchant-transaction/{jsonable_encoder(ideal_merchant_transaction_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextIdealMerchantTransactionDelete,
                    parse_obj_as(
                        type_=NoteTextIdealMerchantTransactionDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_text_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteTextMasterCardActionListing]]:
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
        HttpResponse[typing.List[NoteTextMasterCardActionListing]]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/mastercard-action/{jsonable_encoder(mastercard_action_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextMasterCardActionListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextMasterCardActionListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_text_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextMasterCardActionCreate]:
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
        HttpResponse[NoteTextMasterCardActionCreate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/mastercard-action/{jsonable_encoder(mastercard_action_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextMasterCardActionCreate,
                    parse_obj_as(
                        type_=NoteTextMasterCardActionCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_text_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextMasterCardActionRead]:
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
        HttpResponse[NoteTextMasterCardActionRead]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/mastercard-action/{jsonable_encoder(mastercard_action_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextMasterCardActionRead,
                    parse_obj_as(
                        type_=NoteTextMasterCardActionRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_note_text_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextMasterCardActionUpdate]:
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
        HttpResponse[NoteTextMasterCardActionUpdate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/mastercard-action/{jsonable_encoder(mastercard_action_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextMasterCardActionUpdate,
                    parse_obj_as(
                        type_=NoteTextMasterCardActionUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_text_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextMasterCardActionDelete]:
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
        HttpResponse[NoteTextMasterCardActionDelete]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/mastercard-action/{jsonable_encoder(mastercard_action_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextMasterCardActionDelete,
                    parse_obj_as(
                        type_=NoteTextMasterCardActionDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_text_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteTextPaymentBatchListing]]:
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
        HttpResponse[typing.List[NoteTextPaymentBatchListing]]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment-batch/{jsonable_encoder(payment_batch_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextPaymentBatchListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextPaymentBatchListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_text_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextPaymentBatchCreate]:
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
        HttpResponse[NoteTextPaymentBatchCreate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment-batch/{jsonable_encoder(payment_batch_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextPaymentBatchCreate,
                    parse_obj_as(
                        type_=NoteTextPaymentBatchCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_text_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextPaymentBatchRead]:
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
        HttpResponse[NoteTextPaymentBatchRead]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment-batch/{jsonable_encoder(payment_batch_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextPaymentBatchRead,
                    parse_obj_as(
                        type_=NoteTextPaymentBatchRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_note_text_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextPaymentBatchUpdate]:
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
        HttpResponse[NoteTextPaymentBatchUpdate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment-batch/{jsonable_encoder(payment_batch_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextPaymentBatchUpdate,
                    parse_obj_as(
                        type_=NoteTextPaymentBatchUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_text_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextPaymentBatchDelete]:
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
        HttpResponse[NoteTextPaymentBatchDelete]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment-batch/{jsonable_encoder(payment_batch_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextPaymentBatchDelete,
                    parse_obj_as(
                        type_=NoteTextPaymentBatchDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_text_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteTextPaymentListing]]:
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
        HttpResponse[typing.List[NoteTextPaymentListing]]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment/{jsonable_encoder(payment_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextPaymentListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextPaymentListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_text_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextPaymentCreate]:
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
        HttpResponse[NoteTextPaymentCreate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment/{jsonable_encoder(payment_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextPaymentCreate,
                    parse_obj_as(
                        type_=NoteTextPaymentCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_text_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextPaymentRead]:
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
        HttpResponse[NoteTextPaymentRead]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment/{jsonable_encoder(payment_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextPaymentRead,
                    parse_obj_as(
                        type_=NoteTextPaymentRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_note_text_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextPaymentUpdate]:
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
        HttpResponse[NoteTextPaymentUpdate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment/{jsonable_encoder(payment_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextPaymentUpdate,
                    parse_obj_as(
                        type_=NoteTextPaymentUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_text_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextPaymentDelete]:
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
        HttpResponse[NoteTextPaymentDelete]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment/{jsonable_encoder(payment_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextPaymentDelete,
                    parse_obj_as(
                        type_=NoteTextPaymentDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_text_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteTextRequestInquiryBatchListing]]:
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
        HttpResponse[typing.List[NoteTextRequestInquiryBatchListing]]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry-batch/{jsonable_encoder(request_inquiry_batch_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextRequestInquiryBatchListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextRequestInquiryBatchListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_text_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextRequestInquiryBatchCreate]:
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
        HttpResponse[NoteTextRequestInquiryBatchCreate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry-batch/{jsonable_encoder(request_inquiry_batch_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextRequestInquiryBatchCreate,
                    parse_obj_as(
                        type_=NoteTextRequestInquiryBatchCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_text_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextRequestInquiryBatchRead]:
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
        HttpResponse[NoteTextRequestInquiryBatchRead]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry-batch/{jsonable_encoder(request_inquiry_batch_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextRequestInquiryBatchRead,
                    parse_obj_as(
                        type_=NoteTextRequestInquiryBatchRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_note_text_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextRequestInquiryBatchUpdate]:
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
        HttpResponse[NoteTextRequestInquiryBatchUpdate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry-batch/{jsonable_encoder(request_inquiry_batch_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextRequestInquiryBatchUpdate,
                    parse_obj_as(
                        type_=NoteTextRequestInquiryBatchUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_text_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextRequestInquiryBatchDelete]:
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
        HttpResponse[NoteTextRequestInquiryBatchDelete]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry-batch/{jsonable_encoder(request_inquiry_batch_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextRequestInquiryBatchDelete,
                    parse_obj_as(
                        type_=NoteTextRequestInquiryBatchDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_text_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteTextRequestInquiryListing]]:
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
        HttpResponse[typing.List[NoteTextRequestInquiryListing]]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry/{jsonable_encoder(request_inquiry_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextRequestInquiryListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextRequestInquiryListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_text_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextRequestInquiryCreate]:
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
        HttpResponse[NoteTextRequestInquiryCreate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry/{jsonable_encoder(request_inquiry_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextRequestInquiryCreate,
                    parse_obj_as(
                        type_=NoteTextRequestInquiryCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_text_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextRequestInquiryRead]:
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
        HttpResponse[NoteTextRequestInquiryRead]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry/{jsonable_encoder(request_inquiry_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextRequestInquiryRead,
                    parse_obj_as(
                        type_=NoteTextRequestInquiryRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_note_text_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextRequestInquiryUpdate]:
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
        HttpResponse[NoteTextRequestInquiryUpdate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry/{jsonable_encoder(request_inquiry_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextRequestInquiryUpdate,
                    parse_obj_as(
                        type_=NoteTextRequestInquiryUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_text_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextRequestInquiryDelete]:
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
        HttpResponse[NoteTextRequestInquiryDelete]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry/{jsonable_encoder(request_inquiry_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextRequestInquiryDelete,
                    parse_obj_as(
                        type_=NoteTextRequestInquiryDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_text_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteTextRequestResponseListing]]:
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
        HttpResponse[typing.List[NoteTextRequestResponseListing]]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-response/{jsonable_encoder(request_response_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextRequestResponseListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextRequestResponseListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_text_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextRequestResponseCreate]:
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
        HttpResponse[NoteTextRequestResponseCreate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-response/{jsonable_encoder(request_response_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextRequestResponseCreate,
                    parse_obj_as(
                        type_=NoteTextRequestResponseCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_text_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextRequestResponseRead]:
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
        HttpResponse[NoteTextRequestResponseRead]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-response/{jsonable_encoder(request_response_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextRequestResponseRead,
                    parse_obj_as(
                        type_=NoteTextRequestResponseRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_note_text_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextRequestResponseUpdate]:
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
        HttpResponse[NoteTextRequestResponseUpdate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-response/{jsonable_encoder(request_response_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextRequestResponseUpdate,
                    parse_obj_as(
                        type_=NoteTextRequestResponseUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_text_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextRequestResponseDelete]:
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
        HttpResponse[NoteTextRequestResponseDelete]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-response/{jsonable_encoder(request_response_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextRequestResponseDelete,
                    parse_obj_as(
                        type_=NoteTextRequestResponseDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_text_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteTextSchedulePaymentBatchListing]]:
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
        HttpResponse[typing.List[NoteTextSchedulePaymentBatchListing]]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment-batch/{jsonable_encoder(schedule_payment_batch_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextSchedulePaymentBatchListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextSchedulePaymentBatchListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_text_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextSchedulePaymentBatchCreate]:
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
        HttpResponse[NoteTextSchedulePaymentBatchCreate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment-batch/{jsonable_encoder(schedule_payment_batch_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextSchedulePaymentBatchCreate,
                    parse_obj_as(
                        type_=NoteTextSchedulePaymentBatchCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_text_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextSchedulePaymentBatchRead]:
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
        HttpResponse[NoteTextSchedulePaymentBatchRead]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment-batch/{jsonable_encoder(schedule_payment_batch_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextSchedulePaymentBatchRead,
                    parse_obj_as(
                        type_=NoteTextSchedulePaymentBatchRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_note_text_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextSchedulePaymentBatchUpdate]:
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
        HttpResponse[NoteTextSchedulePaymentBatchUpdate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment-batch/{jsonable_encoder(schedule_payment_batch_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextSchedulePaymentBatchUpdate,
                    parse_obj_as(
                        type_=NoteTextSchedulePaymentBatchUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_text_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextSchedulePaymentBatchDelete]:
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
        HttpResponse[NoteTextSchedulePaymentBatchDelete]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment-batch/{jsonable_encoder(schedule_payment_batch_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextSchedulePaymentBatchDelete,
                    parse_obj_as(
                        type_=NoteTextSchedulePaymentBatchDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_text_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteTextSchedulePaymentListing]]:
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
        HttpResponse[typing.List[NoteTextSchedulePaymentListing]]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment/{jsonable_encoder(schedule_payment_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextSchedulePaymentListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextSchedulePaymentListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_text_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextSchedulePaymentCreate]:
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
        HttpResponse[NoteTextSchedulePaymentCreate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment/{jsonable_encoder(schedule_payment_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextSchedulePaymentCreate,
                    parse_obj_as(
                        type_=NoteTextSchedulePaymentCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_text_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextSchedulePaymentRead]:
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
        HttpResponse[NoteTextSchedulePaymentRead]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment/{jsonable_encoder(schedule_payment_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextSchedulePaymentRead,
                    parse_obj_as(
                        type_=NoteTextSchedulePaymentRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_note_text_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextSchedulePaymentUpdate]:
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
        HttpResponse[NoteTextSchedulePaymentUpdate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment/{jsonable_encoder(schedule_payment_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextSchedulePaymentUpdate,
                    parse_obj_as(
                        type_=NoteTextSchedulePaymentUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_text_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextSchedulePaymentDelete]:
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
        HttpResponse[NoteTextSchedulePaymentDelete]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment/{jsonable_encoder(schedule_payment_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextSchedulePaymentDelete,
                    parse_obj_as(
                        type_=NoteTextSchedulePaymentDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_text_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteTextScheduleInstanceListing]]:
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
        HttpResponse[typing.List[NoteTextScheduleInstanceListing]]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule/{jsonable_encoder(schedule_id)}/schedule-instance/{jsonable_encoder(schedule_instance_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextScheduleInstanceListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextScheduleInstanceListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_text_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextScheduleInstanceCreate]:
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
        HttpResponse[NoteTextScheduleInstanceCreate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule/{jsonable_encoder(schedule_id)}/schedule-instance/{jsonable_encoder(schedule_instance_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextScheduleInstanceCreate,
                    parse_obj_as(
                        type_=NoteTextScheduleInstanceCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_text_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextScheduleInstanceRead]:
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
        HttpResponse[NoteTextScheduleInstanceRead]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule/{jsonable_encoder(schedule_id)}/schedule-instance/{jsonable_encoder(schedule_instance_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextScheduleInstanceRead,
                    parse_obj_as(
                        type_=NoteTextScheduleInstanceRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[NoteTextScheduleInstanceUpdate]:
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
        HttpResponse[NoteTextScheduleInstanceUpdate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule/{jsonable_encoder(schedule_id)}/schedule-instance/{jsonable_encoder(schedule_instance_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextScheduleInstanceUpdate,
                    parse_obj_as(
                        type_=NoteTextScheduleInstanceUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_text_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextScheduleInstanceDelete]:
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
        HttpResponse[NoteTextScheduleInstanceDelete]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule/{jsonable_encoder(schedule_id)}/schedule-instance/{jsonable_encoder(schedule_instance_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextScheduleInstanceDelete,
                    parse_obj_as(
                        type_=NoteTextScheduleInstanceDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_text_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteTextSofortMerchantTransactionListing]]:
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
        HttpResponse[typing.List[NoteTextSofortMerchantTransactionListing]]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/sofort-merchant-transaction/{jsonable_encoder(sofort_merchant_transaction_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextSofortMerchantTransactionListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextSofortMerchantTransactionListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_text_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextSofortMerchantTransactionCreate]:
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
        HttpResponse[NoteTextSofortMerchantTransactionCreate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/sofort-merchant-transaction/{jsonable_encoder(sofort_merchant_transaction_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextSofortMerchantTransactionCreate,
                    parse_obj_as(
                        type_=NoteTextSofortMerchantTransactionCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_text_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextSofortMerchantTransactionRead]:
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
        HttpResponse[NoteTextSofortMerchantTransactionRead]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/sofort-merchant-transaction/{jsonable_encoder(sofort_merchant_transaction_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextSofortMerchantTransactionRead,
                    parse_obj_as(
                        type_=NoteTextSofortMerchantTransactionRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_note_text_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextSofortMerchantTransactionUpdate]:
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
        HttpResponse[NoteTextSofortMerchantTransactionUpdate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/sofort-merchant-transaction/{jsonable_encoder(sofort_merchant_transaction_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextSofortMerchantTransactionUpdate,
                    parse_obj_as(
                        type_=NoteTextSofortMerchantTransactionUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_text_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextSofortMerchantTransactionDelete]:
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
        HttpResponse[NoteTextSofortMerchantTransactionDelete]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/sofort-merchant-transaction/{jsonable_encoder(sofort_merchant_transaction_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextSofortMerchantTransactionDelete,
                    parse_obj_as(
                        type_=NoteTextSofortMerchantTransactionDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_text_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteTextBankSwitchServiceNetherlandsIncomingPaymentListing]]:
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
        HttpResponse[typing.List[NoteTextBankSwitchServiceNetherlandsIncomingPaymentListing]]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/switch-service-payment/{jsonable_encoder(switch_service_payment_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextBankSwitchServiceNetherlandsIncomingPaymentListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextBankSwitchServiceNetherlandsIncomingPaymentListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_text_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextBankSwitchServiceNetherlandsIncomingPaymentCreate]:
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
        HttpResponse[NoteTextBankSwitchServiceNetherlandsIncomingPaymentCreate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/switch-service-payment/{jsonable_encoder(switch_service_payment_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextBankSwitchServiceNetherlandsIncomingPaymentCreate,
                    parse_obj_as(
                        type_=NoteTextBankSwitchServiceNetherlandsIncomingPaymentCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_text_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextBankSwitchServiceNetherlandsIncomingPaymentRead]:
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
        HttpResponse[NoteTextBankSwitchServiceNetherlandsIncomingPaymentRead]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/switch-service-payment/{jsonable_encoder(switch_service_payment_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextBankSwitchServiceNetherlandsIncomingPaymentRead,
                    parse_obj_as(
                        type_=NoteTextBankSwitchServiceNetherlandsIncomingPaymentRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_note_text_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextBankSwitchServiceNetherlandsIncomingPaymentUpdate]:
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
        HttpResponse[NoteTextBankSwitchServiceNetherlandsIncomingPaymentUpdate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/switch-service-payment/{jsonable_encoder(switch_service_payment_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextBankSwitchServiceNetherlandsIncomingPaymentUpdate,
                    parse_obj_as(
                        type_=NoteTextBankSwitchServiceNetherlandsIncomingPaymentUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_text_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextBankSwitchServiceNetherlandsIncomingPaymentDelete]:
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
        HttpResponse[NoteTextBankSwitchServiceNetherlandsIncomingPaymentDelete]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/switch-service-payment/{jsonable_encoder(switch_service_payment_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextBankSwitchServiceNetherlandsIncomingPaymentDelete,
                    parse_obj_as(
                        type_=NoteTextBankSwitchServiceNetherlandsIncomingPaymentDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_note_text_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NoteTextWhitelistResultListing]]:
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
        HttpResponse[typing.List[NoteTextWhitelistResultListing]]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/whitelist/{jsonable_encoder(whitelist_id)}/whitelist-result/{jsonable_encoder(whitelist_result_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextWhitelistResultListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextWhitelistResultListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_note_text_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextWhitelistResultCreate]:
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
        HttpResponse[NoteTextWhitelistResultCreate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/whitelist/{jsonable_encoder(whitelist_id)}/whitelist-result/{jsonable_encoder(whitelist_result_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextWhitelistResultCreate,
                    parse_obj_as(
                        type_=NoteTextWhitelistResultCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_note_text_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextWhitelistResultRead]:
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
        HttpResponse[NoteTextWhitelistResultRead]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/whitelist/{jsonable_encoder(whitelist_id)}/whitelist-result/{jsonable_encoder(whitelist_result_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextWhitelistResultRead,
                    parse_obj_as(
                        type_=NoteTextWhitelistResultRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[NoteTextWhitelistResultUpdate]:
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
        HttpResponse[NoteTextWhitelistResultUpdate]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/whitelist/{jsonable_encoder(whitelist_id)}/whitelist-result/{jsonable_encoder(whitelist_result_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextWhitelistResultUpdate,
                    parse_obj_as(
                        type_=NoteTextWhitelistResultUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_note_text_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NoteTextWhitelistResultDelete]:
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
        HttpResponse[NoteTextWhitelistResultDelete]
            Used to manage text notes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/whitelist/{jsonable_encoder(whitelist_id)}/whitelist-result/{jsonable_encoder(whitelist_result_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextWhitelistResultDelete,
                    parse_obj_as(
                        type_=NoteTextWhitelistResultDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawNoteTextClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_note_text_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteTextBunqMeFundraiserResultListing]]:
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
        AsyncHttpResponse[typing.List[NoteTextBunqMeFundraiserResultListing]]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/bunqme-fundraiser-result/{jsonable_encoder(bunqme_fundraiser_result_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextBunqMeFundraiserResultListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextBunqMeFundraiserResultListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_text_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextBunqMeFundraiserResultCreate]:
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
        AsyncHttpResponse[NoteTextBunqMeFundraiserResultCreate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/bunqme-fundraiser-result/{jsonable_encoder(bunqme_fundraiser_result_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextBunqMeFundraiserResultCreate,
                    parse_obj_as(
                        type_=NoteTextBunqMeFundraiserResultCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_text_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextBunqMeFundraiserResultRead]:
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
        AsyncHttpResponse[NoteTextBunqMeFundraiserResultRead]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/bunqme-fundraiser-result/{jsonable_encoder(bunqme_fundraiser_result_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextBunqMeFundraiserResultRead,
                    parse_obj_as(
                        type_=NoteTextBunqMeFundraiserResultRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_note_text_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextBunqMeFundraiserResultUpdate]:
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
        AsyncHttpResponse[NoteTextBunqMeFundraiserResultUpdate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/bunqme-fundraiser-result/{jsonable_encoder(bunqme_fundraiser_result_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextBunqMeFundraiserResultUpdate,
                    parse_obj_as(
                        type_=NoteTextBunqMeFundraiserResultUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_text_for_user_monetary_account_bunqme_fundraiser_result(
        self,
        user_id: int,
        monetary_account_id: int,
        bunqme_fundraiser_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextBunqMeFundraiserResultDelete]:
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
        AsyncHttpResponse[NoteTextBunqMeFundraiserResultDelete]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/bunqme-fundraiser-result/{jsonable_encoder(bunqme_fundraiser_result_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextBunqMeFundraiserResultDelete,
                    parse_obj_as(
                        type_=NoteTextBunqMeFundraiserResultDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_text_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteTextDraftPaymentListing]]:
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
        AsyncHttpResponse[typing.List[NoteTextDraftPaymentListing]]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/draft-payment/{jsonable_encoder(draft_payment_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextDraftPaymentListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextDraftPaymentListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_text_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextDraftPaymentCreate]:
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
        AsyncHttpResponse[NoteTextDraftPaymentCreate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/draft-payment/{jsonable_encoder(draft_payment_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextDraftPaymentCreate,
                    parse_obj_as(
                        type_=NoteTextDraftPaymentCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_text_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextDraftPaymentRead]:
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
        AsyncHttpResponse[NoteTextDraftPaymentRead]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/draft-payment/{jsonable_encoder(draft_payment_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextDraftPaymentRead,
                    parse_obj_as(
                        type_=NoteTextDraftPaymentRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_note_text_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextDraftPaymentUpdate]:
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
        AsyncHttpResponse[NoteTextDraftPaymentUpdate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/draft-payment/{jsonable_encoder(draft_payment_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextDraftPaymentUpdate,
                    parse_obj_as(
                        type_=NoteTextDraftPaymentUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_text_for_user_monetary_account_draft_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        draft_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextDraftPaymentDelete]:
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
        AsyncHttpResponse[NoteTextDraftPaymentDelete]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/draft-payment/{jsonable_encoder(draft_payment_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextDraftPaymentDelete,
                    parse_obj_as(
                        type_=NoteTextDraftPaymentDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_text_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteTextIdealMerchantTransactionListing]]:
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
        AsyncHttpResponse[typing.List[NoteTextIdealMerchantTransactionListing]]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/ideal-merchant-transaction/{jsonable_encoder(ideal_merchant_transaction_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextIdealMerchantTransactionListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextIdealMerchantTransactionListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_text_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextIdealMerchantTransactionCreate]:
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
        AsyncHttpResponse[NoteTextIdealMerchantTransactionCreate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/ideal-merchant-transaction/{jsonable_encoder(ideal_merchant_transaction_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextIdealMerchantTransactionCreate,
                    parse_obj_as(
                        type_=NoteTextIdealMerchantTransactionCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_text_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextIdealMerchantTransactionRead]:
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
        AsyncHttpResponse[NoteTextIdealMerchantTransactionRead]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/ideal-merchant-transaction/{jsonable_encoder(ideal_merchant_transaction_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextIdealMerchantTransactionRead,
                    parse_obj_as(
                        type_=NoteTextIdealMerchantTransactionRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_note_text_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextIdealMerchantTransactionUpdate]:
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
        AsyncHttpResponse[NoteTextIdealMerchantTransactionUpdate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/ideal-merchant-transaction/{jsonable_encoder(ideal_merchant_transaction_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextIdealMerchantTransactionUpdate,
                    parse_obj_as(
                        type_=NoteTextIdealMerchantTransactionUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_text_for_user_monetary_account_ideal_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        ideal_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextIdealMerchantTransactionDelete]:
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
        AsyncHttpResponse[NoteTextIdealMerchantTransactionDelete]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/ideal-merchant-transaction/{jsonable_encoder(ideal_merchant_transaction_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextIdealMerchantTransactionDelete,
                    parse_obj_as(
                        type_=NoteTextIdealMerchantTransactionDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_text_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteTextMasterCardActionListing]]:
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
        AsyncHttpResponse[typing.List[NoteTextMasterCardActionListing]]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/mastercard-action/{jsonable_encoder(mastercard_action_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextMasterCardActionListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextMasterCardActionListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_text_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextMasterCardActionCreate]:
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
        AsyncHttpResponse[NoteTextMasterCardActionCreate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/mastercard-action/{jsonable_encoder(mastercard_action_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextMasterCardActionCreate,
                    parse_obj_as(
                        type_=NoteTextMasterCardActionCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_text_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextMasterCardActionRead]:
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
        AsyncHttpResponse[NoteTextMasterCardActionRead]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/mastercard-action/{jsonable_encoder(mastercard_action_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextMasterCardActionRead,
                    parse_obj_as(
                        type_=NoteTextMasterCardActionRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_note_text_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextMasterCardActionUpdate]:
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
        AsyncHttpResponse[NoteTextMasterCardActionUpdate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/mastercard-action/{jsonable_encoder(mastercard_action_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextMasterCardActionUpdate,
                    parse_obj_as(
                        type_=NoteTextMasterCardActionUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_text_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextMasterCardActionDelete]:
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
        AsyncHttpResponse[NoteTextMasterCardActionDelete]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/mastercard-action/{jsonable_encoder(mastercard_action_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextMasterCardActionDelete,
                    parse_obj_as(
                        type_=NoteTextMasterCardActionDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_text_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteTextPaymentBatchListing]]:
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
        AsyncHttpResponse[typing.List[NoteTextPaymentBatchListing]]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment-batch/{jsonable_encoder(payment_batch_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextPaymentBatchListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextPaymentBatchListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_text_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextPaymentBatchCreate]:
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
        AsyncHttpResponse[NoteTextPaymentBatchCreate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment-batch/{jsonable_encoder(payment_batch_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextPaymentBatchCreate,
                    parse_obj_as(
                        type_=NoteTextPaymentBatchCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_text_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextPaymentBatchRead]:
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
        AsyncHttpResponse[NoteTextPaymentBatchRead]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment-batch/{jsonable_encoder(payment_batch_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextPaymentBatchRead,
                    parse_obj_as(
                        type_=NoteTextPaymentBatchRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_note_text_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextPaymentBatchUpdate]:
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
        AsyncHttpResponse[NoteTextPaymentBatchUpdate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment-batch/{jsonable_encoder(payment_batch_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextPaymentBatchUpdate,
                    parse_obj_as(
                        type_=NoteTextPaymentBatchUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_text_for_user_monetary_account_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextPaymentBatchDelete]:
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
        AsyncHttpResponse[NoteTextPaymentBatchDelete]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment-batch/{jsonable_encoder(payment_batch_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextPaymentBatchDelete,
                    parse_obj_as(
                        type_=NoteTextPaymentBatchDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_text_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteTextPaymentListing]]:
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
        AsyncHttpResponse[typing.List[NoteTextPaymentListing]]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment/{jsonable_encoder(payment_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextPaymentListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextPaymentListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_text_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextPaymentCreate]:
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
        AsyncHttpResponse[NoteTextPaymentCreate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment/{jsonable_encoder(payment_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextPaymentCreate,
                    parse_obj_as(
                        type_=NoteTextPaymentCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_text_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextPaymentRead]:
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
        AsyncHttpResponse[NoteTextPaymentRead]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment/{jsonable_encoder(payment_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextPaymentRead,
                    parse_obj_as(
                        type_=NoteTextPaymentRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_note_text_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextPaymentUpdate]:
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
        AsyncHttpResponse[NoteTextPaymentUpdate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment/{jsonable_encoder(payment_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextPaymentUpdate,
                    parse_obj_as(
                        type_=NoteTextPaymentUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_text_for_user_monetary_account_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextPaymentDelete]:
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
        AsyncHttpResponse[NoteTextPaymentDelete]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment/{jsonable_encoder(payment_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextPaymentDelete,
                    parse_obj_as(
                        type_=NoteTextPaymentDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_text_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteTextRequestInquiryBatchListing]]:
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
        AsyncHttpResponse[typing.List[NoteTextRequestInquiryBatchListing]]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry-batch/{jsonable_encoder(request_inquiry_batch_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextRequestInquiryBatchListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextRequestInquiryBatchListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_text_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextRequestInquiryBatchCreate]:
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
        AsyncHttpResponse[NoteTextRequestInquiryBatchCreate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry-batch/{jsonable_encoder(request_inquiry_batch_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextRequestInquiryBatchCreate,
                    parse_obj_as(
                        type_=NoteTextRequestInquiryBatchCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_text_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextRequestInquiryBatchRead]:
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
        AsyncHttpResponse[NoteTextRequestInquiryBatchRead]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry-batch/{jsonable_encoder(request_inquiry_batch_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextRequestInquiryBatchRead,
                    parse_obj_as(
                        type_=NoteTextRequestInquiryBatchRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_note_text_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextRequestInquiryBatchUpdate]:
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
        AsyncHttpResponse[NoteTextRequestInquiryBatchUpdate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry-batch/{jsonable_encoder(request_inquiry_batch_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextRequestInquiryBatchUpdate,
                    parse_obj_as(
                        type_=NoteTextRequestInquiryBatchUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_text_for_user_monetary_account_request_inquiry_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextRequestInquiryBatchDelete]:
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
        AsyncHttpResponse[NoteTextRequestInquiryBatchDelete]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry-batch/{jsonable_encoder(request_inquiry_batch_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextRequestInquiryBatchDelete,
                    parse_obj_as(
                        type_=NoteTextRequestInquiryBatchDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_text_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteTextRequestInquiryListing]]:
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
        AsyncHttpResponse[typing.List[NoteTextRequestInquiryListing]]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry/{jsonable_encoder(request_inquiry_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextRequestInquiryListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextRequestInquiryListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_text_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextRequestInquiryCreate]:
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
        AsyncHttpResponse[NoteTextRequestInquiryCreate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry/{jsonable_encoder(request_inquiry_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextRequestInquiryCreate,
                    parse_obj_as(
                        type_=NoteTextRequestInquiryCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_text_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextRequestInquiryRead]:
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
        AsyncHttpResponse[NoteTextRequestInquiryRead]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry/{jsonable_encoder(request_inquiry_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextRequestInquiryRead,
                    parse_obj_as(
                        type_=NoteTextRequestInquiryRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_note_text_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextRequestInquiryUpdate]:
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
        AsyncHttpResponse[NoteTextRequestInquiryUpdate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry/{jsonable_encoder(request_inquiry_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextRequestInquiryUpdate,
                    parse_obj_as(
                        type_=NoteTextRequestInquiryUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_text_for_user_monetary_account_request_inquiry(
        self,
        user_id: int,
        monetary_account_id: int,
        request_inquiry_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextRequestInquiryDelete]:
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
        AsyncHttpResponse[NoteTextRequestInquiryDelete]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry/{jsonable_encoder(request_inquiry_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextRequestInquiryDelete,
                    parse_obj_as(
                        type_=NoteTextRequestInquiryDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_text_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteTextRequestResponseListing]]:
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
        AsyncHttpResponse[typing.List[NoteTextRequestResponseListing]]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-response/{jsonable_encoder(request_response_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextRequestResponseListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextRequestResponseListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_text_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextRequestResponseCreate]:
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
        AsyncHttpResponse[NoteTextRequestResponseCreate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-response/{jsonable_encoder(request_response_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextRequestResponseCreate,
                    parse_obj_as(
                        type_=NoteTextRequestResponseCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_text_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextRequestResponseRead]:
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
        AsyncHttpResponse[NoteTextRequestResponseRead]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-response/{jsonable_encoder(request_response_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextRequestResponseRead,
                    parse_obj_as(
                        type_=NoteTextRequestResponseRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_note_text_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextRequestResponseUpdate]:
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
        AsyncHttpResponse[NoteTextRequestResponseUpdate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-response/{jsonable_encoder(request_response_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextRequestResponseUpdate,
                    parse_obj_as(
                        type_=NoteTextRequestResponseUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_text_for_user_monetary_account_request_response(
        self,
        user_id: int,
        monetary_account_id: int,
        request_response_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextRequestResponseDelete]:
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
        AsyncHttpResponse[NoteTextRequestResponseDelete]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-response/{jsonable_encoder(request_response_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextRequestResponseDelete,
                    parse_obj_as(
                        type_=NoteTextRequestResponseDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_text_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteTextSchedulePaymentBatchListing]]:
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
        AsyncHttpResponse[typing.List[NoteTextSchedulePaymentBatchListing]]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment-batch/{jsonable_encoder(schedule_payment_batch_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextSchedulePaymentBatchListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextSchedulePaymentBatchListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_text_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextSchedulePaymentBatchCreate]:
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
        AsyncHttpResponse[NoteTextSchedulePaymentBatchCreate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment-batch/{jsonable_encoder(schedule_payment_batch_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextSchedulePaymentBatchCreate,
                    parse_obj_as(
                        type_=NoteTextSchedulePaymentBatchCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_text_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextSchedulePaymentBatchRead]:
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
        AsyncHttpResponse[NoteTextSchedulePaymentBatchRead]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment-batch/{jsonable_encoder(schedule_payment_batch_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextSchedulePaymentBatchRead,
                    parse_obj_as(
                        type_=NoteTextSchedulePaymentBatchRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_note_text_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextSchedulePaymentBatchUpdate]:
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
        AsyncHttpResponse[NoteTextSchedulePaymentBatchUpdate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment-batch/{jsonable_encoder(schedule_payment_batch_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextSchedulePaymentBatchUpdate,
                    parse_obj_as(
                        type_=NoteTextSchedulePaymentBatchUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_text_for_user_monetary_account_schedule_payment_batch(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_batch_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextSchedulePaymentBatchDelete]:
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
        AsyncHttpResponse[NoteTextSchedulePaymentBatchDelete]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment-batch/{jsonable_encoder(schedule_payment_batch_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextSchedulePaymentBatchDelete,
                    parse_obj_as(
                        type_=NoteTextSchedulePaymentBatchDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_text_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteTextSchedulePaymentListing]]:
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
        AsyncHttpResponse[typing.List[NoteTextSchedulePaymentListing]]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment/{jsonable_encoder(schedule_payment_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextSchedulePaymentListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextSchedulePaymentListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_text_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextSchedulePaymentCreate]:
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
        AsyncHttpResponse[NoteTextSchedulePaymentCreate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment/{jsonable_encoder(schedule_payment_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextSchedulePaymentCreate,
                    parse_obj_as(
                        type_=NoteTextSchedulePaymentCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_text_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextSchedulePaymentRead]:
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
        AsyncHttpResponse[NoteTextSchedulePaymentRead]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment/{jsonable_encoder(schedule_payment_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextSchedulePaymentRead,
                    parse_obj_as(
                        type_=NoteTextSchedulePaymentRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_note_text_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextSchedulePaymentUpdate]:
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
        AsyncHttpResponse[NoteTextSchedulePaymentUpdate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment/{jsonable_encoder(schedule_payment_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextSchedulePaymentUpdate,
                    parse_obj_as(
                        type_=NoteTextSchedulePaymentUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_text_for_user_monetary_account_schedule_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextSchedulePaymentDelete]:
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
        AsyncHttpResponse[NoteTextSchedulePaymentDelete]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment/{jsonable_encoder(schedule_payment_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextSchedulePaymentDelete,
                    parse_obj_as(
                        type_=NoteTextSchedulePaymentDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_text_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteTextScheduleInstanceListing]]:
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
        AsyncHttpResponse[typing.List[NoteTextScheduleInstanceListing]]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule/{jsonable_encoder(schedule_id)}/schedule-instance/{jsonable_encoder(schedule_instance_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextScheduleInstanceListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextScheduleInstanceListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_text_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextScheduleInstanceCreate]:
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
        AsyncHttpResponse[NoteTextScheduleInstanceCreate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule/{jsonable_encoder(schedule_id)}/schedule-instance/{jsonable_encoder(schedule_instance_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextScheduleInstanceCreate,
                    parse_obj_as(
                        type_=NoteTextScheduleInstanceCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_text_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextScheduleInstanceRead]:
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
        AsyncHttpResponse[NoteTextScheduleInstanceRead]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule/{jsonable_encoder(schedule_id)}/schedule-instance/{jsonable_encoder(schedule_instance_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextScheduleInstanceRead,
                    parse_obj_as(
                        type_=NoteTextScheduleInstanceRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[NoteTextScheduleInstanceUpdate]:
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
        AsyncHttpResponse[NoteTextScheduleInstanceUpdate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule/{jsonable_encoder(schedule_id)}/schedule-instance/{jsonable_encoder(schedule_instance_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextScheduleInstanceUpdate,
                    parse_obj_as(
                        type_=NoteTextScheduleInstanceUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_text_for_user_monetary_account_schedule_schedule_instance(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        schedule_instance_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextScheduleInstanceDelete]:
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
        AsyncHttpResponse[NoteTextScheduleInstanceDelete]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule/{jsonable_encoder(schedule_id)}/schedule-instance/{jsonable_encoder(schedule_instance_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextScheduleInstanceDelete,
                    parse_obj_as(
                        type_=NoteTextScheduleInstanceDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_text_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteTextSofortMerchantTransactionListing]]:
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
        AsyncHttpResponse[typing.List[NoteTextSofortMerchantTransactionListing]]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/sofort-merchant-transaction/{jsonable_encoder(sofort_merchant_transaction_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextSofortMerchantTransactionListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextSofortMerchantTransactionListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_text_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextSofortMerchantTransactionCreate]:
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
        AsyncHttpResponse[NoteTextSofortMerchantTransactionCreate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/sofort-merchant-transaction/{jsonable_encoder(sofort_merchant_transaction_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextSofortMerchantTransactionCreate,
                    parse_obj_as(
                        type_=NoteTextSofortMerchantTransactionCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_text_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextSofortMerchantTransactionRead]:
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
        AsyncHttpResponse[NoteTextSofortMerchantTransactionRead]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/sofort-merchant-transaction/{jsonable_encoder(sofort_merchant_transaction_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextSofortMerchantTransactionRead,
                    parse_obj_as(
                        type_=NoteTextSofortMerchantTransactionRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_note_text_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextSofortMerchantTransactionUpdate]:
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
        AsyncHttpResponse[NoteTextSofortMerchantTransactionUpdate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/sofort-merchant-transaction/{jsonable_encoder(sofort_merchant_transaction_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextSofortMerchantTransactionUpdate,
                    parse_obj_as(
                        type_=NoteTextSofortMerchantTransactionUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_text_for_user_monetary_account_sofort_merchant_transaction(
        self,
        user_id: int,
        monetary_account_id: int,
        sofort_merchant_transaction_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextSofortMerchantTransactionDelete]:
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
        AsyncHttpResponse[NoteTextSofortMerchantTransactionDelete]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/sofort-merchant-transaction/{jsonable_encoder(sofort_merchant_transaction_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextSofortMerchantTransactionDelete,
                    parse_obj_as(
                        type_=NoteTextSofortMerchantTransactionDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_text_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteTextBankSwitchServiceNetherlandsIncomingPaymentListing]]:
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
        AsyncHttpResponse[typing.List[NoteTextBankSwitchServiceNetherlandsIncomingPaymentListing]]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/switch-service-payment/{jsonable_encoder(switch_service_payment_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextBankSwitchServiceNetherlandsIncomingPaymentListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextBankSwitchServiceNetherlandsIncomingPaymentListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_text_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextBankSwitchServiceNetherlandsIncomingPaymentCreate]:
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
        AsyncHttpResponse[NoteTextBankSwitchServiceNetherlandsIncomingPaymentCreate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/switch-service-payment/{jsonable_encoder(switch_service_payment_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextBankSwitchServiceNetherlandsIncomingPaymentCreate,
                    parse_obj_as(
                        type_=NoteTextBankSwitchServiceNetherlandsIncomingPaymentCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_text_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextBankSwitchServiceNetherlandsIncomingPaymentRead]:
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
        AsyncHttpResponse[NoteTextBankSwitchServiceNetherlandsIncomingPaymentRead]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/switch-service-payment/{jsonable_encoder(switch_service_payment_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextBankSwitchServiceNetherlandsIncomingPaymentRead,
                    parse_obj_as(
                        type_=NoteTextBankSwitchServiceNetherlandsIncomingPaymentRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_note_text_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        item_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextBankSwitchServiceNetherlandsIncomingPaymentUpdate]:
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
        AsyncHttpResponse[NoteTextBankSwitchServiceNetherlandsIncomingPaymentUpdate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/switch-service-payment/{jsonable_encoder(switch_service_payment_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextBankSwitchServiceNetherlandsIncomingPaymentUpdate,
                    parse_obj_as(
                        type_=NoteTextBankSwitchServiceNetherlandsIncomingPaymentUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_text_for_user_monetary_account_switch_service_payment(
        self,
        user_id: int,
        monetary_account_id: int,
        switch_service_payment_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextBankSwitchServiceNetherlandsIncomingPaymentDelete]:
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
        AsyncHttpResponse[NoteTextBankSwitchServiceNetherlandsIncomingPaymentDelete]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/switch-service-payment/{jsonable_encoder(switch_service_payment_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextBankSwitchServiceNetherlandsIncomingPaymentDelete,
                    parse_obj_as(
                        type_=NoteTextBankSwitchServiceNetherlandsIncomingPaymentDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_note_text_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NoteTextWhitelistResultListing]]:
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
        AsyncHttpResponse[typing.List[NoteTextWhitelistResultListing]]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/whitelist/{jsonable_encoder(whitelist_id)}/whitelist-result/{jsonable_encoder(whitelist_result_id)}/note-text",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NoteTextWhitelistResultListing],
                    parse_obj_as(
                        type_=typing.List[NoteTextWhitelistResultListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_note_text_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextWhitelistResultCreate]:
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
        AsyncHttpResponse[NoteTextWhitelistResultCreate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/whitelist/{jsonable_encoder(whitelist_id)}/whitelist-result/{jsonable_encoder(whitelist_result_id)}/note-text",
            method="POST",
            json={
                "content": content,
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
                    NoteTextWhitelistResultCreate,
                    parse_obj_as(
                        type_=NoteTextWhitelistResultCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_note_text_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextWhitelistResultRead]:
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
        AsyncHttpResponse[NoteTextWhitelistResultRead]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/whitelist/{jsonable_encoder(whitelist_id)}/whitelist-result/{jsonable_encoder(whitelist_result_id)}/note-text/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextWhitelistResultRead,
                    parse_obj_as(
                        type_=NoteTextWhitelistResultRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[NoteTextWhitelistResultUpdate]:
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
        AsyncHttpResponse[NoteTextWhitelistResultUpdate]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/whitelist/{jsonable_encoder(whitelist_id)}/whitelist-result/{jsonable_encoder(whitelist_result_id)}/note-text/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "content": content,
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
                    NoteTextWhitelistResultUpdate,
                    parse_obj_as(
                        type_=NoteTextWhitelistResultUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_note_text_for_user_monetary_account_whitelist_whitelist_result(
        self,
        user_id: int,
        monetary_account_id: int,
        whitelist_id: int,
        whitelist_result_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NoteTextWhitelistResultDelete]:
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
        AsyncHttpResponse[NoteTextWhitelistResultDelete]
            Used to manage text notes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/whitelist/{jsonable_encoder(whitelist_id)}/whitelist-result/{jsonable_encoder(whitelist_result_id)}/note-text/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NoteTextWhitelistResultDelete,
                    parse_obj_as(
                        type_=NoteTextWhitelistResultDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
