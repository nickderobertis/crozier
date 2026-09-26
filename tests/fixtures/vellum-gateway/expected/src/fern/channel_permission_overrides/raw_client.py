

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.channel_permission_override_delete_request_contact_type import (
    ChannelPermissionOverrideDeleteRequestContactType,
)
from .types.channel_permission_override_delete_request_selector import ChannelPermissionOverrideDeleteRequestSelector
from .types.channel_permission_override_delete_response import ChannelPermissionOverrideDeleteResponse
from .types.channel_permission_override_set_request_contact_type import ChannelPermissionOverrideSetRequestContactType
from .types.channel_permission_override_set_request_selector import ChannelPermissionOverrideSetRequestSelector
from .types.channel_permission_override_set_request_threshold import ChannelPermissionOverrideSetRequestThreshold
from .types.channel_permission_override_set_response import ChannelPermissionOverrideSetResponse
from .types.channel_permission_overrides_list_response import ChannelPermissionOverridesListResponse
from .types.channel_permission_resolve_request_channel_type import ChannelPermissionResolveRequestChannelType
from .types.channel_permission_resolve_request_contact_type import ChannelPermissionResolveRequestContactType
from .types.channel_permission_resolve_response import ChannelPermissionResolveResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawChannelPermissionOverridesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ChannelPermissionOverridesListResponse]:
        """
        Returns every persisted cell (cascade selector × contact-type → RiskThreshold). Unset cells fall through the cascade; the list contains only explicit overrides.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChannelPermissionOverridesListResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/channel-permission-overrides",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChannelPermissionOverridesListResponse,
                    parse_obj_as(
                        type_=ChannelPermissionOverridesListResponse,
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

    def channel_permission_override_set(
        self,
        *,
        selector: ChannelPermissionOverrideSetRequestSelector,
        contact_type: ChannelPermissionOverrideSetRequestContactType,
        threshold: ChannelPermissionOverrideSetRequestThreshold,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ChannelPermissionOverrideSetResponse]:
        """
        Upserts one cell, identified by the selector × contact-type in the body. The adapter must be a known channel id.

        Parameters
        ----------
        selector : ChannelPermissionOverrideSetRequestSelector

        contact_type : ChannelPermissionOverrideSetRequestContactType

        threshold : ChannelPermissionOverrideSetRequestThreshold

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChannelPermissionOverrideSetResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/channel-permission-overrides",
            method="PUT",
            json={
                "selector": convert_and_respect_annotation_metadata(
                    object_=selector, annotation=ChannelPermissionOverrideSetRequestSelector, direction="write"
                ),
                "contactType": contact_type,
                "threshold": threshold,
                "note": note,
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
                    ChannelPermissionOverrideSetResponse,
                    parse_obj_as(
                        type_=ChannelPermissionOverrideSetResponse,
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

    def channel_permission_resolve(
        self,
        *,
        adapter: str,
        contact_type: ChannelPermissionResolveRequestContactType,
        channel_type: typing.Optional[ChannelPermissionResolveRequestChannelType] = OMIT,
        channel_external_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ChannelPermissionResolveResponse]:
        """
        Read-only cascade resolution for one coordinate: walks channel → channel_type → adapter → workspace for the given selector keys and contact-type, returning the winning cell's threshold and scope, or null when no cell matches (the caller then falls through to the global thresholds). Same resolver the runtime evaluator uses over IPC.

        Parameters
        ----------
        adapter : str

        contact_type : ChannelPermissionResolveRequestContactType

        channel_type : typing.Optional[ChannelPermissionResolveRequestChannelType]

        channel_external_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChannelPermissionResolveResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/channel-permission-overrides/resolve",
            method="POST",
            json={
                "adapter": adapter,
                "channelType": channel_type,
                "channelExternalId": channel_external_id,
                "contactType": contact_type,
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
                    ChannelPermissionResolveResponse,
                    parse_obj_as(
                        type_=ChannelPermissionResolveResponse,
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

    def channel_permission_override_delete(
        self,
        *,
        selector: ChannelPermissionOverrideDeleteRequestSelector,
        contact_type: ChannelPermissionOverrideDeleteRequestContactType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ChannelPermissionOverrideDeleteResponse]:
        """
        Removes one cell by its composite key (selector × contact-type), letting the next cascade tier up win. Returns whether a cell was removed.

        Parameters
        ----------
        selector : ChannelPermissionOverrideDeleteRequestSelector

        contact_type : ChannelPermissionOverrideDeleteRequestContactType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChannelPermissionOverrideDeleteResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/channel-permission-overrides/delete",
            method="POST",
            json={
                "selector": convert_and_respect_annotation_metadata(
                    object_=selector, annotation=ChannelPermissionOverrideDeleteRequestSelector, direction="write"
                ),
                "contactType": contact_type,
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
                    ChannelPermissionOverrideDeleteResponse,
                    parse_obj_as(
                        type_=ChannelPermissionOverrideDeleteResponse,
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


class AsyncRawChannelPermissionOverridesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ChannelPermissionOverridesListResponse]:
        """
        Returns every persisted cell (cascade selector × contact-type → RiskThreshold). Unset cells fall through the cascade; the list contains only explicit overrides.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChannelPermissionOverridesListResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/channel-permission-overrides",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChannelPermissionOverridesListResponse,
                    parse_obj_as(
                        type_=ChannelPermissionOverridesListResponse,
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

    async def channel_permission_override_set(
        self,
        *,
        selector: ChannelPermissionOverrideSetRequestSelector,
        contact_type: ChannelPermissionOverrideSetRequestContactType,
        threshold: ChannelPermissionOverrideSetRequestThreshold,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ChannelPermissionOverrideSetResponse]:
        """
        Upserts one cell, identified by the selector × contact-type in the body. The adapter must be a known channel id.

        Parameters
        ----------
        selector : ChannelPermissionOverrideSetRequestSelector

        contact_type : ChannelPermissionOverrideSetRequestContactType

        threshold : ChannelPermissionOverrideSetRequestThreshold

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChannelPermissionOverrideSetResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/channel-permission-overrides",
            method="PUT",
            json={
                "selector": convert_and_respect_annotation_metadata(
                    object_=selector, annotation=ChannelPermissionOverrideSetRequestSelector, direction="write"
                ),
                "contactType": contact_type,
                "threshold": threshold,
                "note": note,
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
                    ChannelPermissionOverrideSetResponse,
                    parse_obj_as(
                        type_=ChannelPermissionOverrideSetResponse,
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

    async def channel_permission_resolve(
        self,
        *,
        adapter: str,
        contact_type: ChannelPermissionResolveRequestContactType,
        channel_type: typing.Optional[ChannelPermissionResolveRequestChannelType] = OMIT,
        channel_external_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ChannelPermissionResolveResponse]:
        """
        Read-only cascade resolution for one coordinate: walks channel → channel_type → adapter → workspace for the given selector keys and contact-type, returning the winning cell's threshold and scope, or null when no cell matches (the caller then falls through to the global thresholds). Same resolver the runtime evaluator uses over IPC.

        Parameters
        ----------
        adapter : str

        contact_type : ChannelPermissionResolveRequestContactType

        channel_type : typing.Optional[ChannelPermissionResolveRequestChannelType]

        channel_external_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChannelPermissionResolveResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/channel-permission-overrides/resolve",
            method="POST",
            json={
                "adapter": adapter,
                "channelType": channel_type,
                "channelExternalId": channel_external_id,
                "contactType": contact_type,
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
                    ChannelPermissionResolveResponse,
                    parse_obj_as(
                        type_=ChannelPermissionResolveResponse,
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

    async def channel_permission_override_delete(
        self,
        *,
        selector: ChannelPermissionOverrideDeleteRequestSelector,
        contact_type: ChannelPermissionOverrideDeleteRequestContactType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ChannelPermissionOverrideDeleteResponse]:
        """
        Removes one cell by its composite key (selector × contact-type), letting the next cascade tier up win. Returns whether a cell was removed.

        Parameters
        ----------
        selector : ChannelPermissionOverrideDeleteRequestSelector

        contact_type : ChannelPermissionOverrideDeleteRequestContactType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChannelPermissionOverrideDeleteResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/channel-permission-overrides/delete",
            method="POST",
            json={
                "selector": convert_and_respect_annotation_metadata(
                    object_=selector, annotation=ChannelPermissionOverrideDeleteRequestSelector, direction="write"
                ),
                "contactType": contact_type,
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
                    ChannelPermissionOverrideDeleteResponse,
                    parse_obj_as(
                        type_=ChannelPermissionOverrideDeleteResponse,
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
