

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.channel import Channel
from ..types.envelope_list_template_get import EnvelopeListTemplateGet
from ..types.envelope_task_get import EnvelopeTaskGet
from ..types.envelope_template_preview_get import EnvelopeTemplatePreviewGet
from ..types.group_id_int import GroupIdInt
from ..types.message_content import MessageContent
from ..types.template_ref import TemplateRef
from .raw_client import AsyncRawNotificationsClient, RawNotificationsClient


OMIT = typing.cast(typing.Any, ...)


class NotificationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNotificationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNotificationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNotificationsClient
        """
        return self._raw_client

    def send_message(
        self,
        *,
        channel: Channel,
        content: MessageContent,
        group_ids: typing.Optional[typing.Sequence[GroupIdInt]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeTaskGet:
        """
        Parameters
        ----------
        channel : Channel

        content : MessageContent

        group_ids : typing.Optional[typing.Sequence[GroupIdInt]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTaskGet
            Successful Response

        Examples
        --------
        from fern import Channel, FernApi, MessageContent

        client = FernApi()
        client.notifications.send_message(
            channel=Channel.EMAIL,
            content=MessageContent(
                subject="subject",
            ),
        )
        """
        _response = self._raw_client.send_message(
            channel=channel, content=content, group_ids=group_ids, request_options=request_options
        )
        return _response.data

    def preview_template(
        self,
        *,
        ref: TemplateRef,
        context: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeTemplatePreviewGet:
        """
        Generates a preview of a notification template with the provided data.

        This endpoint renders the specified notification template using the supplied
        template data, allowing users to see how the final notification will appear
        before sending it.

        Returns a rendered version of the notification template with all variables
        substituted with the provided data.

        Parameters
        ----------
        ref : TemplateRef

        context : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTemplatePreviewGet
            Successful Response

        Examples
        --------
        from fern import Channel, FernApi, TemplateRef

        client = FernApi()
        client.notifications.preview_template(
            ref=TemplateRef(
                channel=Channel.EMAIL,
                template_name="templateName",
            ),
            context={"key": "value"},
        )
        """
        _response = self._raw_client.preview_template(ref=ref, context=context, request_options=request_options)
        return _response.data

    def search_templates(
        self,
        *,
        channel: typing.Optional[Channel] = None,
        template_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListTemplateGet:
        """
        Search for available notification templates by channel and/or template name.
        Both channel and template_name support wildcard patterns for flexible matching.

        Returns templates with their context schema defining required variables for rendering.

        Parameters
        ----------
        channel : typing.Optional[Channel]

        template_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListTemplateGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.notifications.search_templates()
        """
        _response = self._raw_client.search_templates(
            channel=channel, template_name=template_name, request_options=request_options
        )
        return _response.data


class AsyncNotificationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNotificationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNotificationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNotificationsClient
        """
        return self._raw_client

    async def send_message(
        self,
        *,
        channel: Channel,
        content: MessageContent,
        group_ids: typing.Optional[typing.Sequence[GroupIdInt]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeTaskGet:
        """
        Parameters
        ----------
        channel : Channel

        content : MessageContent

        group_ids : typing.Optional[typing.Sequence[GroupIdInt]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTaskGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Channel, MessageContent

        client = AsyncFernApi()


        async def main() -> None:
            await client.notifications.send_message(
                channel=Channel.EMAIL,
                content=MessageContent(
                    subject="subject",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_message(
            channel=channel, content=content, group_ids=group_ids, request_options=request_options
        )
        return _response.data

    async def preview_template(
        self,
        *,
        ref: TemplateRef,
        context: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeTemplatePreviewGet:
        """
        Generates a preview of a notification template with the provided data.

        This endpoint renders the specified notification template using the supplied
        template data, allowing users to see how the final notification will appear
        before sending it.

        Returns a rendered version of the notification template with all variables
        substituted with the provided data.

        Parameters
        ----------
        ref : TemplateRef

        context : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTemplatePreviewGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Channel, TemplateRef

        client = AsyncFernApi()


        async def main() -> None:
            await client.notifications.preview_template(
                ref=TemplateRef(
                    channel=Channel.EMAIL,
                    template_name="templateName",
                ),
                context={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.preview_template(ref=ref, context=context, request_options=request_options)
        return _response.data

    async def search_templates(
        self,
        *,
        channel: typing.Optional[Channel] = None,
        template_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListTemplateGet:
        """
        Search for available notification templates by channel and/or template name.
        Both channel and template_name support wildcard patterns for flexible matching.

        Returns templates with their context schema defining required variables for rendering.

        Parameters
        ----------
        channel : typing.Optional[Channel]

        template_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListTemplateGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.notifications.search_templates()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_templates(
            channel=channel, template_name=template_name, request_options=request_options
        )
        return _response.data
