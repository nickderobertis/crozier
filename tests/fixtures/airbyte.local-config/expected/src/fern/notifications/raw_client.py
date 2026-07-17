

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.customerio_notification_configuration import CustomerioNotificationConfiguration
from ..types.invalid_input_exception_info import InvalidInputExceptionInfo
from ..types.not_found_known_exception_info import NotFoundKnownExceptionInfo
from ..types.notification_read import NotificationRead
from ..types.notification_type import NotificationType
from ..types.slack_notification_configuration import SlackNotificationConfiguration
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawNotificationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def try_notification_config(
        self,
        *,
        notification_type: NotificationType,
        send_on_failure: bool,
        send_on_success: bool,
        customerio_configuration: typing.Optional[CustomerioNotificationConfiguration] = OMIT,
        slack_configuration: typing.Optional[SlackNotificationConfiguration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NotificationRead]:
        """
        Parameters
        ----------
        notification_type : NotificationType

        send_on_failure : bool

        send_on_success : bool

        customerio_configuration : typing.Optional[CustomerioNotificationConfiguration]

        slack_configuration : typing.Optional[SlackNotificationConfiguration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NotificationRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/notifications/try",
            method="POST",
            json={
                "customerioConfiguration": customerio_configuration,
                "notificationType": notification_type,
                "sendOnFailure": send_on_failure,
                "sendOnSuccess": send_on_success,
                "slackConfiguration": convert_and_respect_annotation_metadata(
                    object_=slack_configuration, annotation=SlackNotificationConfiguration, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationRead,
                    parse_obj_as(
                        type_=NotificationRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
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


class AsyncRawNotificationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def try_notification_config(
        self,
        *,
        notification_type: NotificationType,
        send_on_failure: bool,
        send_on_success: bool,
        customerio_configuration: typing.Optional[CustomerioNotificationConfiguration] = OMIT,
        slack_configuration: typing.Optional[SlackNotificationConfiguration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NotificationRead]:
        """
        Parameters
        ----------
        notification_type : NotificationType

        send_on_failure : bool

        send_on_success : bool

        customerio_configuration : typing.Optional[CustomerioNotificationConfiguration]

        slack_configuration : typing.Optional[SlackNotificationConfiguration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NotificationRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/notifications/try",
            method="POST",
            json={
                "customerioConfiguration": customerio_configuration,
                "notificationType": notification_type,
                "sendOnFailure": send_on_failure,
                "sendOnSuccess": send_on_success,
                "slackConfiguration": convert_and_respect_annotation_metadata(
                    object_=slack_configuration, annotation=SlackNotificationConfiguration, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationRead,
                    parse_obj_as(
                        type_=NotificationRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
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
