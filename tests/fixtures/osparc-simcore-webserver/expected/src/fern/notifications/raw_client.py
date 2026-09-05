

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.channel import Channel
from ..types.envelope_list_template_get import EnvelopeListTemplateGet
from ..types.envelope_task_get import EnvelopeTaskGet
from ..types.envelope_template_preview_get import EnvelopeTemplatePreviewGet
from ..types.group_id_int import GroupIdInt
from ..types.message_content import MessageContent
from ..types.template_ref import TemplateRef
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawNotificationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def send_message(
        self,
        *,
        channel: Channel,
        content: MessageContent,
        group_ids: typing.Optional[typing.Sequence[GroupIdInt]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeTaskGet]:
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
        HttpResponse[EnvelopeTaskGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/notifications/messages:send",
            method="POST",
            json={
                "channel": channel,
                "groupIds": group_ids,
                "content": convert_and_respect_annotation_metadata(
                    object_=content, annotation=MessageContent, direction="write"
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
                    EnvelopeTaskGet,
                    parse_obj_as(
                        type_=EnvelopeTaskGet,
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

    def preview_template(
        self,
        *,
        ref: TemplateRef,
        context: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeTemplatePreviewGet]:
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
        HttpResponse[EnvelopeTemplatePreviewGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/notifications/templates:preview",
            method="POST",
            json={
                "ref": convert_and_respect_annotation_metadata(object_=ref, annotation=TemplateRef, direction="write"),
                "context": context,
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
                    EnvelopeTemplatePreviewGet,
                    parse_obj_as(
                        type_=EnvelopeTemplatePreviewGet,
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

    def search_templates(
        self,
        *,
        channel: typing.Optional[Channel] = None,
        template_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeListTemplateGet]:
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
        HttpResponse[EnvelopeListTemplateGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/notifications/templates:search",
            method="GET",
            params={
                "channel": channel,
                "template_name": template_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListTemplateGet,
                    parse_obj_as(
                        type_=EnvelopeListTemplateGet,
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


class AsyncRawNotificationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def send_message(
        self,
        *,
        channel: Channel,
        content: MessageContent,
        group_ids: typing.Optional[typing.Sequence[GroupIdInt]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeTaskGet]:
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
        AsyncHttpResponse[EnvelopeTaskGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/notifications/messages:send",
            method="POST",
            json={
                "channel": channel,
                "groupIds": group_ids,
                "content": convert_and_respect_annotation_metadata(
                    object_=content, annotation=MessageContent, direction="write"
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
                    EnvelopeTaskGet,
                    parse_obj_as(
                        type_=EnvelopeTaskGet,
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

    async def preview_template(
        self,
        *,
        ref: TemplateRef,
        context: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeTemplatePreviewGet]:
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
        AsyncHttpResponse[EnvelopeTemplatePreviewGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/notifications/templates:preview",
            method="POST",
            json={
                "ref": convert_and_respect_annotation_metadata(object_=ref, annotation=TemplateRef, direction="write"),
                "context": context,
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
                    EnvelopeTemplatePreviewGet,
                    parse_obj_as(
                        type_=EnvelopeTemplatePreviewGet,
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

    async def search_templates(
        self,
        *,
        channel: typing.Optional[Channel] = None,
        template_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeListTemplateGet]:
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
        AsyncHttpResponse[EnvelopeListTemplateGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/notifications/templates:search",
            method="GET",
            params={
                "channel": channel,
                "template_name": template_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListTemplateGet,
                    parse_obj_as(
                        type_=EnvelopeListTemplateGet,
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
