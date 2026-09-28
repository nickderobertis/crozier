

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawContactsClient, RawContactsClient
from .types.contact_channel_verify_response import ContactChannelVerifyResponse
from .types.contacts_prompt_submit_response import ContactsPromptSubmitResponse
from .types.contacts_record_submit_request_expected_channels_item import ContactsRecordSubmitRequestExpectedChannelsItem
from .types.contacts_record_submit_request_operation import ContactsRecordSubmitRequestOperation
from .types.contacts_record_submit_response import ContactsRecordSubmitResponse
from .types.contacts_upsert_request_assistant_metadata import ContactsUpsertRequestAssistantMetadata
from .types.contacts_upsert_request_auto_approve_threshold import ContactsUpsertRequestAutoApproveThreshold
from .types.contacts_upsert_request_channels_item import ContactsUpsertRequestChannelsItem
from .types.contacts_upsert_response import ContactsUpsertResponse


OMIT = typing.cast(typing.Any, ...)


class ContactsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawContactsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawContactsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawContactsClient
        """
        return self._raw_client

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
    ) -> ContactsUpsertResponse:
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
        ContactsUpsertResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contacts.upsert(
            display_name="displayName",
        )
        """
        _response = self._raw_client.upsert(
            display_name=display_name,
            id=id,
            notes=notes,
            auto_approve_threshold=auto_approve_threshold,
            contact_type=contact_type,
            assistant_metadata=assistant_metadata,
            channels=channels,
            request_options=request_options,
        )
        return _response.data

    def contact_delete(self, contact_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contacts.contact_delete(
            contact_id="contact_id",
        )
        """
        _response = self._raw_client.contact_delete(contact_id, request_options=request_options)
        return _response.data

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
    ) -> ContactsPromptSubmitResponse:
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
        ContactsPromptSubmitResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contacts.prompt_submit(
            request_id="requestId",
        )
        """
        _response = self._raw_client.prompt_submit(
            request_id=request_id,
            address=address,
            channel_type=channel_type,
            role=role,
            display_name=display_name,
            contact_id=contact_id,
            verify=verify,
            cancelled=cancelled,
            request_options=request_options,
        )
        return _response.data

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
    ) -> ContactsRecordSubmitResponse:
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
        ContactsRecordSubmitResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contacts.record_submit(
            request_id="requestId",
        )
        """
        _response = self._raw_client.record_submit(
            request_id=request_id,
            operation=operation,
            contact_id=contact_id,
            donor_contact_id=donor_contact_id,
            display_name=display_name,
            notes=notes,
            expected_channels=expected_channels,
            cancelled=cancelled,
            request_options=request_options,
        )
        return _response.data

    def contact_channel_verify(
        self, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContactChannelVerifyResponse:
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
        ContactChannelVerifyResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contacts.contact_channel_verify(
            channel_id="channel_id",
        )
        """
        _response = self._raw_client.contact_channel_verify(channel_id, request_options=request_options)
        return _response.data


class AsyncContactsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawContactsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawContactsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawContactsClient
        """
        return self._raw_client

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
    ) -> ContactsUpsertResponse:
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
        ContactsUpsertResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.contacts.upsert(
                display_name="displayName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upsert(
            display_name=display_name,
            id=id,
            notes=notes,
            auto_approve_threshold=auto_approve_threshold,
            contact_type=contact_type,
            assistant_metadata=assistant_metadata,
            channels=channels,
            request_options=request_options,
        )
        return _response.data

    async def contact_delete(self, contact_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.contacts.contact_delete(
                contact_id="contact_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_delete(contact_id, request_options=request_options)
        return _response.data

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
    ) -> ContactsPromptSubmitResponse:
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
        ContactsPromptSubmitResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.contacts.prompt_submit(
                request_id="requestId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.prompt_submit(
            request_id=request_id,
            address=address,
            channel_type=channel_type,
            role=role,
            display_name=display_name,
            contact_id=contact_id,
            verify=verify,
            cancelled=cancelled,
            request_options=request_options,
        )
        return _response.data

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
    ) -> ContactsRecordSubmitResponse:
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
        ContactsRecordSubmitResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.contacts.record_submit(
                request_id="requestId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_submit(
            request_id=request_id,
            operation=operation,
            contact_id=contact_id,
            donor_contact_id=donor_contact_id,
            display_name=display_name,
            notes=notes,
            expected_channels=expected_channels,
            cancelled=cancelled,
            request_options=request_options,
        )
        return _response.data

    async def contact_channel_verify(
        self, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContactChannelVerifyResponse:
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
        ContactChannelVerifyResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.contacts.contact_channel_verify(
                channel_id="channel_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_channel_verify(channel_id, request_options=request_options)
        return _response.data
