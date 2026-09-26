

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.contact_channel_verify_response import ContactChannelVerifyResponse
from .types.contacts_prompt_submit_response import ContactsPromptSubmitResponse
from .types.contacts_record_submit_request_expected_channels_item import ContactsRecordSubmitRequestExpectedChannelsItem
from .types.contacts_record_submit_request_operation import ContactsRecordSubmitRequestOperation
from .types.contacts_record_submit_response import ContactsRecordSubmitResponse
from .types.contacts_upsert_request_assistant_metadata import ContactsUpsertRequestAssistantMetadata
from .types.contacts_upsert_request_auto_approve_threshold import ContactsUpsertRequestAutoApproveThreshold
from .types.contacts_upsert_request_channels_item import ContactsUpsertRequestChannelsItem
from .types.contacts_upsert_response import ContactsUpsertResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawContactsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def upsert(
        self,
        *,
        display_name: str,
        id: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        auto_approve_threshold: typing.Optional[ContactsUpsertRequestAutoApproveThreshold] = OMIT,
        contact_type: typing.Optional[str] = OMIT,
        assistant_metadata: typing.Optional[ContactsUpsertRequestAssistantMetadata] = OMIT,
        channels: typing.Optional[typing.Sequence[ContactsUpsertRequestChannelsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContactsUpsertResponse]:
        """
        Gateway-native contact upsert (dual-writes the gateway ACL store and the assistant info mirror). Matches by id, then by any provided (type, address) channel, else creates.

        Parameters
        ----------
        display_name : str
            Required on every upsert, including updates by id

        id : typing.Optional[str]
            Existing contact id to update; omit to create or match by channel

        notes : typing.Optional[str]

        auto_approve_threshold : typing.Optional[ContactsUpsertRequestAutoApproveThreshold]
            Per-contact auto-approve ceiling. Omit to preserve; null clears.

        contact_type : typing.Optional[str]

        assistant_metadata : typing.Optional[ContactsUpsertRequestAssistantMetadata]
            Required when contactType is 'assistant'

        channels : typing.Optional[typing.Sequence[ContactsUpsertRequestChannelsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContactsUpsertResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/contacts",
            method="POST",
            json={
                "id": id,
                "displayName": display_name,
                "notes": notes,
                "autoApproveThreshold": auto_approve_threshold,
                "contactType": contact_type,
                "assistantMetadata": convert_and_respect_annotation_metadata(
                    object_=assistant_metadata, annotation=ContactsUpsertRequestAssistantMetadata, direction="write"
                ),
                "channels": convert_and_respect_annotation_metadata(
                    object_=channels, annotation=typing.Sequence[ContactsUpsertRequestChannelsItem], direction="write"
                ),
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
                    ContactsUpsertResponse,
                    parse_obj_as(
                        type_=ContactsUpsertResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def contact_delete(
        self, contact_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Deletes a non-guardian contact from the gateway ACL store and the assistant mirror. 404 when the contact exists in neither; 403 for guardian contacts.

        Parameters
        ----------
        contact_id : str
            The contact id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/contacts/{encode_path_param(contact_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def prompt_submit(
        self,
        *,
        request_id: str,
        address: typing.Optional[str] = OMIT,
        channel_type: typing.Optional[str] = OMIT,
        role: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        verify: typing.Optional[bool] = OMIT,
        cancelled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContactsPromptSubmitResponse]:
        """
        Completes a contact_request the assistant broadcast: writes the contact and channel gateway-first, then unblocks the waiting prompt.

        Parameters
        ----------
        request_id : str
            The contact_request id broadcast by the assistant

        address : typing.Optional[str]
            Required unless cancelled is true

        channel_type : typing.Optional[str]
            Required unless cancelled is true

        role : typing.Optional[str]

        display_name : typing.Optional[str]

        contact_id : typing.Optional[str]
            The contact the parked form targets, echoed back from the broadcast. The parked form is authoritative.

        verify : typing.Optional[bool]
            The form's 'mark verified' checkbox as the guardian left it. Omit only from clients that predate the checkbox; the parked command's flag is then used instead.

        cancelled : typing.Optional[bool]
            The guardian dismissed the form. Unblocks the waiting command without writing.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContactsPromptSubmitResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/contacts/prompt/submit",
            method="POST",
            json={
                "requestId": request_id,
                "address": address,
                "channelType": channel_type,
                "role": role,
                "displayName": display_name,
                "contactId": contact_id,
                "verify": verify,
                "cancelled": cancelled,
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
                    ContactsPromptSubmitResponse,
                    parse_obj_as(
                        type_=ContactsPromptSubmitResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def record_submit(
        self,
        *,
        request_id: str,
        operation: typing.Optional[ContactsRecordSubmitRequestOperation] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        donor_contact_id: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        expected_channels: typing.Optional[typing.Sequence[ContactsRecordSubmitRequestExpectedChannelsItem]] = OMIT,
        cancelled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContactsRecordSubmitResponse]:
        """
        Completes a contact_record_request the assistant broadcast: writes the record the guardian confirmed, then unblocks the waiting command. A create or update writes display name and notes, never a channel; a merge moves the donor's channels to the survivor and deletes the donor. A cancelled submission unblocks the command without writing.

        Parameters
        ----------
        request_id : str
            The contact_record_request id broadcast by the assistant

        operation : typing.Optional[ContactsRecordSubmitRequestOperation]
            Required unless cancelled is true

        contact_id : typing.Optional[str]
            Required to update or delete, and the survivor of a merge

        donor_contact_id : typing.Optional[str]
            The contact merged away. Required for a merge.

        display_name : typing.Optional[str]

        notes : typing.Optional[str]

        expected_channels : typing.Optional[typing.Sequence[ContactsRecordSubmitRequestExpectedChannelsItem]]
            The channels the delete confirmation listed. The delete is refused if the contact's channels changed since.

        cancelled : typing.Optional[bool]
            The guardian dismissed the form. Unblocks the waiting command without writing.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContactsRecordSubmitResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/contacts/record/submit",
            method="POST",
            json={
                "requestId": request_id,
                "operation": operation,
                "contactId": contact_id,
                "donorContactId": donor_contact_id,
                "displayName": display_name,
                "notes": notes,
                "expectedChannels": convert_and_respect_annotation_metadata(
                    object_=expected_channels,
                    annotation=typing.Sequence[ContactsRecordSubmitRequestExpectedChannelsItem],
                    direction="write",
                ),
                "cancelled": cancelled,
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
                    ContactsRecordSubmitResponse,
                    parse_obj_as(
                        type_=ContactsRecordSubmitResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def contact_channel_verify(
        self, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ContactChannelVerifyResponse]:
        """
        Guardian-only manual attestation: marks the channel active/verified in the gateway store (source of truth) with a best-effort assistant mirror. Idempotent.

        Parameters
        ----------
        channel_id : str
            The contact-channel id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContactChannelVerifyResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/contact-channels/{encode_path_param(channel_id)}/verify",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactChannelVerifyResponse,
                    parse_obj_as(
                        type_=ContactChannelVerifyResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawContactsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def upsert(
        self,
        *,
        display_name: str,
        id: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        auto_approve_threshold: typing.Optional[ContactsUpsertRequestAutoApproveThreshold] = OMIT,
        contact_type: typing.Optional[str] = OMIT,
        assistant_metadata: typing.Optional[ContactsUpsertRequestAssistantMetadata] = OMIT,
        channels: typing.Optional[typing.Sequence[ContactsUpsertRequestChannelsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContactsUpsertResponse]:
        """
        Gateway-native contact upsert (dual-writes the gateway ACL store and the assistant info mirror). Matches by id, then by any provided (type, address) channel, else creates.

        Parameters
        ----------
        display_name : str
            Required on every upsert, including updates by id

        id : typing.Optional[str]
            Existing contact id to update; omit to create or match by channel

        notes : typing.Optional[str]

        auto_approve_threshold : typing.Optional[ContactsUpsertRequestAutoApproveThreshold]
            Per-contact auto-approve ceiling. Omit to preserve; null clears.

        contact_type : typing.Optional[str]

        assistant_metadata : typing.Optional[ContactsUpsertRequestAssistantMetadata]
            Required when contactType is 'assistant'

        channels : typing.Optional[typing.Sequence[ContactsUpsertRequestChannelsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContactsUpsertResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/contacts",
            method="POST",
            json={
                "id": id,
                "displayName": display_name,
                "notes": notes,
                "autoApproveThreshold": auto_approve_threshold,
                "contactType": contact_type,
                "assistantMetadata": convert_and_respect_annotation_metadata(
                    object_=assistant_metadata, annotation=ContactsUpsertRequestAssistantMetadata, direction="write"
                ),
                "channels": convert_and_respect_annotation_metadata(
                    object_=channels, annotation=typing.Sequence[ContactsUpsertRequestChannelsItem], direction="write"
                ),
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
                    ContactsUpsertResponse,
                    parse_obj_as(
                        type_=ContactsUpsertResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def contact_delete(
        self, contact_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Deletes a non-guardian contact from the gateway ACL store and the assistant mirror. 404 when the contact exists in neither; 403 for guardian contacts.

        Parameters
        ----------
        contact_id : str
            The contact id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/contacts/{encode_path_param(contact_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def prompt_submit(
        self,
        *,
        request_id: str,
        address: typing.Optional[str] = OMIT,
        channel_type: typing.Optional[str] = OMIT,
        role: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        verify: typing.Optional[bool] = OMIT,
        cancelled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContactsPromptSubmitResponse]:
        """
        Completes a contact_request the assistant broadcast: writes the contact and channel gateway-first, then unblocks the waiting prompt.

        Parameters
        ----------
        request_id : str
            The contact_request id broadcast by the assistant

        address : typing.Optional[str]
            Required unless cancelled is true

        channel_type : typing.Optional[str]
            Required unless cancelled is true

        role : typing.Optional[str]

        display_name : typing.Optional[str]

        contact_id : typing.Optional[str]
            The contact the parked form targets, echoed back from the broadcast. The parked form is authoritative.

        verify : typing.Optional[bool]
            The form's 'mark verified' checkbox as the guardian left it. Omit only from clients that predate the checkbox; the parked command's flag is then used instead.

        cancelled : typing.Optional[bool]
            The guardian dismissed the form. Unblocks the waiting command without writing.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContactsPromptSubmitResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/contacts/prompt/submit",
            method="POST",
            json={
                "requestId": request_id,
                "address": address,
                "channelType": channel_type,
                "role": role,
                "displayName": display_name,
                "contactId": contact_id,
                "verify": verify,
                "cancelled": cancelled,
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
                    ContactsPromptSubmitResponse,
                    parse_obj_as(
                        type_=ContactsPromptSubmitResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def record_submit(
        self,
        *,
        request_id: str,
        operation: typing.Optional[ContactsRecordSubmitRequestOperation] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        donor_contact_id: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        expected_channels: typing.Optional[typing.Sequence[ContactsRecordSubmitRequestExpectedChannelsItem]] = OMIT,
        cancelled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContactsRecordSubmitResponse]:
        """
        Completes a contact_record_request the assistant broadcast: writes the record the guardian confirmed, then unblocks the waiting command. A create or update writes display name and notes, never a channel; a merge moves the donor's channels to the survivor and deletes the donor. A cancelled submission unblocks the command without writing.

        Parameters
        ----------
        request_id : str
            The contact_record_request id broadcast by the assistant

        operation : typing.Optional[ContactsRecordSubmitRequestOperation]
            Required unless cancelled is true

        contact_id : typing.Optional[str]
            Required to update or delete, and the survivor of a merge

        donor_contact_id : typing.Optional[str]
            The contact merged away. Required for a merge.

        display_name : typing.Optional[str]

        notes : typing.Optional[str]

        expected_channels : typing.Optional[typing.Sequence[ContactsRecordSubmitRequestExpectedChannelsItem]]
            The channels the delete confirmation listed. The delete is refused if the contact's channels changed since.

        cancelled : typing.Optional[bool]
            The guardian dismissed the form. Unblocks the waiting command without writing.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContactsRecordSubmitResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/contacts/record/submit",
            method="POST",
            json={
                "requestId": request_id,
                "operation": operation,
                "contactId": contact_id,
                "donorContactId": donor_contact_id,
                "displayName": display_name,
                "notes": notes,
                "expectedChannels": convert_and_respect_annotation_metadata(
                    object_=expected_channels,
                    annotation=typing.Sequence[ContactsRecordSubmitRequestExpectedChannelsItem],
                    direction="write",
                ),
                "cancelled": cancelled,
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
                    ContactsRecordSubmitResponse,
                    parse_obj_as(
                        type_=ContactsRecordSubmitResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def contact_channel_verify(
        self, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ContactChannelVerifyResponse]:
        """
        Guardian-only manual attestation: marks the channel active/verified in the gateway store (source of truth) with a best-effort assistant mirror. Idempotent.

        Parameters
        ----------
        channel_id : str
            The contact-channel id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContactChannelVerifyResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/contact-channels/{encode_path_param(channel_id)}/verify",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactChannelVerifyResponse,
                    parse_obj_as(
                        type_=ContactChannelVerifyResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
