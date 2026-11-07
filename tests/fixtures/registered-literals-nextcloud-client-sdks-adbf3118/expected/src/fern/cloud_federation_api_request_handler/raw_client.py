

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.cloud_federation_api_add_share import CloudFederationApiAddShare
from pydantic import ValidationError


class RawCloudFederationApiRequestHandlerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def add_share(
        self,
        *,
        share_with: str,
        name: str,
        provider_id: str,
        owner: str,
        protocol: str,
        share_type: str,
        resource_type: str,
        description: typing.Optional[str] = None,
        owner_display_name: typing.Optional[str] = None,
        shared_by: typing.Optional[str] = None,
        shared_by_display_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CloudFederationApiAddShare]:
        """
        Parameters
        ----------
        share_with : str
            The user who the share will be shared with

        name : str
            The resource name (e.g. document.odt)

        provider_id : str
            Resource UID on the provider side

        owner : str
            Provider specific UID of the user who owns the resource

        protocol : str
            e,.g. ['name' => 'webdav', 'options' => ['username' => 'john', 'permissions' => 31]]

        share_type : str
            'group' or 'user' share

        resource_type : str
            'file', 'calendar',...

        description : typing.Optional[str]
            Share description

        owner_display_name : typing.Optional[str]
            Display name of the user who shared the item

        shared_by : typing.Optional[str]
            Provider specific UID of the user who shared the resource

        shared_by_display_name : typing.Optional[str]
            Display name of the user who shared the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CloudFederationApiAddShare]
            The notification was successfully received. The display name of the recipient might be returned in the body
        """
        _response = self._client_wrapper.httpx_client.request(
            "index.php/ocm/shares",
            method="POST",
            params={
                "shareWith": share_with,
                "name": name,
                "description": description,
                "providerId": provider_id,
                "owner": owner,
                "ownerDisplayName": owner_display_name,
                "sharedBy": shared_by,
                "sharedByDisplayName": shared_by_display_name,
                "protocol": protocol,
                "shareType": share_type,
                "resourceType": resource_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudFederationApiAddShare,
                    parse_obj_as(
                        type_=CloudFederationApiAddShare,
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

    def receive_notification(
        self,
        *,
        notification_type: str,
        resource_type: str,
        provider_id: typing.Optional[str] = None,
        notification: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[typing.Dict[str, typing.Any]]]:
        """
        Parameters
        ----------
        notification_type : str
            Notification type, e.g. SHARE_ACCEPTED

        resource_type : str
            calendar, file, contact,...

        provider_id : typing.Optional[str]
            ID of the share

        notification : typing.Optional[str]
            The actual payload of the notification

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[typing.Dict[str, typing.Any]]]
            The notification was successfully received
        """
        _response = self._client_wrapper.httpx_client.request(
            "index.php/ocm/notifications",
            method="POST",
            params={
                "notificationType": notification_type,
                "resourceType": resource_type,
                "providerId": provider_id,
                "notification": notification,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[typing.Dict[str, typing.Any]],
                    parse_obj_as(
                        type_=typing.List[typing.Dict[str, typing.Any]],
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


class AsyncRawCloudFederationApiRequestHandlerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def add_share(
        self,
        *,
        share_with: str,
        name: str,
        provider_id: str,
        owner: str,
        protocol: str,
        share_type: str,
        resource_type: str,
        description: typing.Optional[str] = None,
        owner_display_name: typing.Optional[str] = None,
        shared_by: typing.Optional[str] = None,
        shared_by_display_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CloudFederationApiAddShare]:
        """
        Parameters
        ----------
        share_with : str
            The user who the share will be shared with

        name : str
            The resource name (e.g. document.odt)

        provider_id : str
            Resource UID on the provider side

        owner : str
            Provider specific UID of the user who owns the resource

        protocol : str
            e,.g. ['name' => 'webdav', 'options' => ['username' => 'john', 'permissions' => 31]]

        share_type : str
            'group' or 'user' share

        resource_type : str
            'file', 'calendar',...

        description : typing.Optional[str]
            Share description

        owner_display_name : typing.Optional[str]
            Display name of the user who shared the item

        shared_by : typing.Optional[str]
            Provider specific UID of the user who shared the resource

        shared_by_display_name : typing.Optional[str]
            Display name of the user who shared the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CloudFederationApiAddShare]
            The notification was successfully received. The display name of the recipient might be returned in the body
        """
        _response = await self._client_wrapper.httpx_client.request(
            "index.php/ocm/shares",
            method="POST",
            params={
                "shareWith": share_with,
                "name": name,
                "description": description,
                "providerId": provider_id,
                "owner": owner,
                "ownerDisplayName": owner_display_name,
                "sharedBy": shared_by,
                "sharedByDisplayName": shared_by_display_name,
                "protocol": protocol,
                "shareType": share_type,
                "resourceType": resource_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudFederationApiAddShare,
                    parse_obj_as(
                        type_=CloudFederationApiAddShare,
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

    async def receive_notification(
        self,
        *,
        notification_type: str,
        resource_type: str,
        provider_id: typing.Optional[str] = None,
        notification: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[typing.Dict[str, typing.Any]]]:
        """
        Parameters
        ----------
        notification_type : str
            Notification type, e.g. SHARE_ACCEPTED

        resource_type : str
            calendar, file, contact,...

        provider_id : typing.Optional[str]
            ID of the share

        notification : typing.Optional[str]
            The actual payload of the notification

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[typing.Dict[str, typing.Any]]]
            The notification was successfully received
        """
        _response = await self._client_wrapper.httpx_client.request(
            "index.php/ocm/notifications",
            method="POST",
            params={
                "notificationType": notification_type,
                "resourceType": resource_type,
                "providerId": provider_id,
                "notification": notification,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[typing.Dict[str, typing.Any]],
                    parse_obj_as(
                        type_=typing.List[typing.Dict[str, typing.Any]],
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
