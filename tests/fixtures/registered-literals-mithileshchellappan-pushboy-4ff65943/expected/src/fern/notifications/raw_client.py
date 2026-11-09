

import datetime as dt
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
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..types.notification_payload_priority import NotificationPayloadPriority
from ..types.paginated_publish_jobs import PaginatedPublishJobs
from ..types.publish_job import PublishJob
from ..types.queued_job_response import QueuedJobResponse
from .types.get_v1topics_topic_id_notifications_request_status import GetV1TopicsTopicIdNotificationsRequestStatus
from .types.get_v1users_user_id_notifications_request_status import GetV1UsersUserIdNotificationsRequestStatus
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawNotificationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_notifications_eligible_for_a_user(
        self,
        user_id: str,
        *,
        status: typing.Optional[GetV1UsersUserIdNotificationsRequestStatus] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaginatedPublishJobs]:
        """
        Returns direct user sends and topic sends where the user is currently subscribed and the job effective time is on or after the subscription time. This is eligibility, not delivery history.

        Parameters
        ----------
        user_id : str

        status : typing.Optional[GetV1UsersUserIdNotificationsRequestStatus]
            Exact uppercase notification job status. Omit for no status filter.

        cursor : typing.Optional[str]
            Opaque URL-safe cursor returned by the previous page.

        limit : typing.Optional[int]
            Page size. Defaults to 50 and must be between 1 and 200.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedPublishJobs]
            Eligible notification jobs ordered by effective time descending.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/users/{encode_path_param(user_id)}/notifications",
            method="GET",
            params={
                "status": status,
                "cursor": cursor,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedPublishJobs,
                    parse_obj_as(
                        type_=PaginatedPublishJobs,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def send_or_schedule_a_notification_to_one_user(
        self,
        user_id: str,
        *,
        scheduled_at: typing.Optional[dt.datetime] = OMIT,
        title: typing.Optional[str] = OMIT,
        body: typing.Optional[str] = OMIT,
        silent: typing.Optional[str] = OMIT,
        image_url: typing.Optional[str] = OMIT,
        sound: typing.Optional[str] = OMIT,
        badge: typing.Optional[int] = OMIT,
        data: typing.Optional[typing.Dict[str, str]] = OMIT,
        collapse_id: typing.Optional[str] = OMIT,
        priority: typing.Optional[NotificationPayloadPriority] = OMIT,
        ttl: typing.Optional[int] = OMIT,
        thread_id: typing.Optional[str] = OMIT,
        category: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[QueuedJobResponse]:
        """
        Parameters
        ----------
        user_id : str

        scheduled_at : typing.Optional[dt.datetime]
            Optional future RFC3339 timestamp.

        title : typing.Optional[str]

        body : typing.Optional[str]

        silent : typing.Optional[str]

        image_url : typing.Optional[str]

        sound : typing.Optional[str]

        badge : typing.Optional[int]

        data : typing.Optional[typing.Dict[str, str]]

        collapse_id : typing.Optional[str]

        priority : typing.Optional[NotificationPayloadPriority]

        ttl : typing.Optional[int]
            Seconds until expiration.

        thread_id : typing.Optional[str]

        category : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[QueuedJobResponse]
            Job queued.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/users/{encode_path_param(user_id)}/send",
            method="POST",
            json={
                "scheduled_at": scheduled_at,
                "title": title,
                "body": body,
                "silent": silent,
                "image_url": image_url,
                "sound": sound,
                "badge": badge,
                "data": data,
                "collapse_id": collapse_id,
                "priority": priority,
                "ttl": ttl,
                "thread_id": thread_id,
                "category": category,
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
                    QueuedJobResponse,
                    parse_obj_as(
                        type_=QueuedJobResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def list_notifications_for_a_topic(
        self,
        topic_id: str,
        *,
        status: typing.Optional[GetV1TopicsTopicIdNotificationsRequestStatus] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaginatedPublishJobs]:
        """
        Parameters
        ----------
        topic_id : str

        status : typing.Optional[GetV1TopicsTopicIdNotificationsRequestStatus]
            Exact uppercase notification job status. Omit for no status filter.

        cursor : typing.Optional[str]
            Opaque URL-safe cursor returned by the previous page.

        limit : typing.Optional[int]
            Page size. Defaults to 50 and must be between 1 and 200.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedPublishJobs]
            Topic notification jobs ordered by effective time descending.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/topics/{encode_path_param(topic_id)}/notifications",
            method="GET",
            params={
                "status": status,
                "cursor": cursor,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedPublishJobs,
                    parse_obj_as(
                        type_=PaginatedPublishJobs,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def send_or_schedule_a_notification_to_a_topic(
        self,
        topic_id: str,
        *,
        scheduled_at: typing.Optional[dt.datetime] = OMIT,
        title: typing.Optional[str] = OMIT,
        body: typing.Optional[str] = OMIT,
        silent: typing.Optional[str] = OMIT,
        image_url: typing.Optional[str] = OMIT,
        sound: typing.Optional[str] = OMIT,
        badge: typing.Optional[int] = OMIT,
        data: typing.Optional[typing.Dict[str, str]] = OMIT,
        collapse_id: typing.Optional[str] = OMIT,
        priority: typing.Optional[NotificationPayloadPriority] = OMIT,
        ttl: typing.Optional[int] = OMIT,
        thread_id: typing.Optional[str] = OMIT,
        category: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[QueuedJobResponse]:
        """
        Parameters
        ----------
        topic_id : str

        scheduled_at : typing.Optional[dt.datetime]
            Optional future RFC3339 timestamp.

        title : typing.Optional[str]

        body : typing.Optional[str]

        silent : typing.Optional[str]

        image_url : typing.Optional[str]

        sound : typing.Optional[str]

        badge : typing.Optional[int]

        data : typing.Optional[typing.Dict[str, str]]

        collapse_id : typing.Optional[str]

        priority : typing.Optional[NotificationPayloadPriority]

        ttl : typing.Optional[int]
            Seconds until expiration.

        thread_id : typing.Optional[str]

        category : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[QueuedJobResponse]
            Job queued.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/topics/{encode_path_param(topic_id)}/publish",
            method="POST",
            json={
                "scheduled_at": scheduled_at,
                "title": title,
                "body": body,
                "silent": silent,
                "image_url": image_url,
                "sound": sound,
                "badge": badge,
                "data": data,
                "collapse_id": collapse_id,
                "priority": priority,
                "ttl": ttl,
                "thread_id": thread_id,
                "category": category,
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
                    QueuedJobResponse,
                    parse_obj_as(
                        type_=QueuedJobResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def get_notification_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PublishJob]:
        """
        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PublishJob]
            Notification job.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/notifications/{encode_path_param(job_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PublishJob,
                    parse_obj_as(
                        type_=PublishJob,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def list_notifications_eligible_for_a_user(
        self,
        user_id: str,
        *,
        status: typing.Optional[GetV1UsersUserIdNotificationsRequestStatus] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaginatedPublishJobs]:
        """
        Returns direct user sends and topic sends where the user is currently subscribed and the job effective time is on or after the subscription time. This is eligibility, not delivery history.

        Parameters
        ----------
        user_id : str

        status : typing.Optional[GetV1UsersUserIdNotificationsRequestStatus]
            Exact uppercase notification job status. Omit for no status filter.

        cursor : typing.Optional[str]
            Opaque URL-safe cursor returned by the previous page.

        limit : typing.Optional[int]
            Page size. Defaults to 50 and must be between 1 and 200.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedPublishJobs]
            Eligible notification jobs ordered by effective time descending.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/users/{encode_path_param(user_id)}/notifications",
            method="GET",
            params={
                "status": status,
                "cursor": cursor,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedPublishJobs,
                    parse_obj_as(
                        type_=PaginatedPublishJobs,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def send_or_schedule_a_notification_to_one_user(
        self,
        user_id: str,
        *,
        scheduled_at: typing.Optional[dt.datetime] = OMIT,
        title: typing.Optional[str] = OMIT,
        body: typing.Optional[str] = OMIT,
        silent: typing.Optional[str] = OMIT,
        image_url: typing.Optional[str] = OMIT,
        sound: typing.Optional[str] = OMIT,
        badge: typing.Optional[int] = OMIT,
        data: typing.Optional[typing.Dict[str, str]] = OMIT,
        collapse_id: typing.Optional[str] = OMIT,
        priority: typing.Optional[NotificationPayloadPriority] = OMIT,
        ttl: typing.Optional[int] = OMIT,
        thread_id: typing.Optional[str] = OMIT,
        category: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[QueuedJobResponse]:
        """
        Parameters
        ----------
        user_id : str

        scheduled_at : typing.Optional[dt.datetime]
            Optional future RFC3339 timestamp.

        title : typing.Optional[str]

        body : typing.Optional[str]

        silent : typing.Optional[str]

        image_url : typing.Optional[str]

        sound : typing.Optional[str]

        badge : typing.Optional[int]

        data : typing.Optional[typing.Dict[str, str]]

        collapse_id : typing.Optional[str]

        priority : typing.Optional[NotificationPayloadPriority]

        ttl : typing.Optional[int]
            Seconds until expiration.

        thread_id : typing.Optional[str]

        category : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[QueuedJobResponse]
            Job queued.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/users/{encode_path_param(user_id)}/send",
            method="POST",
            json={
                "scheduled_at": scheduled_at,
                "title": title,
                "body": body,
                "silent": silent,
                "image_url": image_url,
                "sound": sound,
                "badge": badge,
                "data": data,
                "collapse_id": collapse_id,
                "priority": priority,
                "ttl": ttl,
                "thread_id": thread_id,
                "category": category,
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
                    QueuedJobResponse,
                    parse_obj_as(
                        type_=QueuedJobResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def list_notifications_for_a_topic(
        self,
        topic_id: str,
        *,
        status: typing.Optional[GetV1TopicsTopicIdNotificationsRequestStatus] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaginatedPublishJobs]:
        """
        Parameters
        ----------
        topic_id : str

        status : typing.Optional[GetV1TopicsTopicIdNotificationsRequestStatus]
            Exact uppercase notification job status. Omit for no status filter.

        cursor : typing.Optional[str]
            Opaque URL-safe cursor returned by the previous page.

        limit : typing.Optional[int]
            Page size. Defaults to 50 and must be between 1 and 200.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedPublishJobs]
            Topic notification jobs ordered by effective time descending.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/topics/{encode_path_param(topic_id)}/notifications",
            method="GET",
            params={
                "status": status,
                "cursor": cursor,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedPublishJobs,
                    parse_obj_as(
                        type_=PaginatedPublishJobs,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def send_or_schedule_a_notification_to_a_topic(
        self,
        topic_id: str,
        *,
        scheduled_at: typing.Optional[dt.datetime] = OMIT,
        title: typing.Optional[str] = OMIT,
        body: typing.Optional[str] = OMIT,
        silent: typing.Optional[str] = OMIT,
        image_url: typing.Optional[str] = OMIT,
        sound: typing.Optional[str] = OMIT,
        badge: typing.Optional[int] = OMIT,
        data: typing.Optional[typing.Dict[str, str]] = OMIT,
        collapse_id: typing.Optional[str] = OMIT,
        priority: typing.Optional[NotificationPayloadPriority] = OMIT,
        ttl: typing.Optional[int] = OMIT,
        thread_id: typing.Optional[str] = OMIT,
        category: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[QueuedJobResponse]:
        """
        Parameters
        ----------
        topic_id : str

        scheduled_at : typing.Optional[dt.datetime]
            Optional future RFC3339 timestamp.

        title : typing.Optional[str]

        body : typing.Optional[str]

        silent : typing.Optional[str]

        image_url : typing.Optional[str]

        sound : typing.Optional[str]

        badge : typing.Optional[int]

        data : typing.Optional[typing.Dict[str, str]]

        collapse_id : typing.Optional[str]

        priority : typing.Optional[NotificationPayloadPriority]

        ttl : typing.Optional[int]
            Seconds until expiration.

        thread_id : typing.Optional[str]

        category : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[QueuedJobResponse]
            Job queued.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/topics/{encode_path_param(topic_id)}/publish",
            method="POST",
            json={
                "scheduled_at": scheduled_at,
                "title": title,
                "body": body,
                "silent": silent,
                "image_url": image_url,
                "sound": sound,
                "badge": badge,
                "data": data,
                "collapse_id": collapse_id,
                "priority": priority,
                "ttl": ttl,
                "thread_id": thread_id,
                "category": category,
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
                    QueuedJobResponse,
                    parse_obj_as(
                        type_=QueuedJobResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def get_notification_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PublishJob]:
        """
        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PublishJob]
            Notification job.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/notifications/{encode_path_param(job_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PublishJob,
                    parse_obj_as(
                        type_=PublishJob,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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
