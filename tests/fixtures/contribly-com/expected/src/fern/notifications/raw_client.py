

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.notification_preview import NotificationPreview
from pydantic import ValidationError


class RawNotificationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_notifications_contributions_id_preview(
        self, id: str, *, message: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[NotificationPreview]:
        """
        Parameters
        ----------
        id : str
            Id of the contribution to preview a notification for

        message : str
            Type of message to preview.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NotificationPreview]
            Notification preview
        """
        _response = self._client_wrapper.httpx_client.request(
            f"notifications/contributions/{encode_path_param(id)}/preview",
            method="GET",
            params={
                "message": message,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationPreview,
                    parse_obj_as(
                        type_=NotificationPreview,
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

    async def get_notifications_contributions_id_preview(
        self, id: str, *, message: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[NotificationPreview]:
        """
        Parameters
        ----------
        id : str
            Id of the contribution to preview a notification for

        message : str
            Type of message to preview.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NotificationPreview]
            Notification preview
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"notifications/contributions/{encode_path_param(id)}/preview",
            method="GET",
            params={
                "message": message,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationPreview,
                    parse_obj_as(
                        type_=NotificationPreview,
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
