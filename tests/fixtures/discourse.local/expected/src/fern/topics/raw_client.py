

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.create_topic_timer_response import CreateTopicTimerResponse
from .types.get_specific_posts_from_topic_response import GetSpecificPostsFromTopicResponse
from .types.get_topic_response import GetTopicResponse
from .types.invite_to_topic_response import InviteToTopicResponse
from .types.list_latest_topics_response import ListLatestTopicsResponse
from .types.list_top_topics_response import ListTopTopicsResponse
from .types.set_notification_level_request_notification_level import SetNotificationLevelRequestNotificationLevel
from .types.set_notification_level_response import SetNotificationLevelResponse
from .types.update_topic_request_topic import UpdateTopicRequestTopic
from .types.update_topic_response import UpdateTopicResponse
from .types.update_topic_status_request_enabled import UpdateTopicStatusRequestEnabled
from .types.update_topic_status_request_status import UpdateTopicStatusRequestStatus
from .types.update_topic_status_response import UpdateTopicStatusResponse
from .types.update_topic_timestamp_response import UpdateTopicTimestampResponse


OMIT = typing.cast(typing.Any, ...)


class RawTopicsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_latest_topics(
        self,
        *,
        api_key: str,
        api_username: str,
        order: typing.Optional[str] = None,
        ascending: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListLatestTopicsResponse]:
        """
        Parameters
        ----------
        api_key : str

        api_username : str

        order : typing.Optional[str]
            Enum: `default`, `created`, `activity`, `views`, `posts`, `category`,
            `likes`, `op_likes`, `posters`

        ascending : typing.Optional[str]
            Defaults to `desc`, add `ascending=true` to sort asc

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListLatestTopicsResponse]
            topic updated
        """
        _response = self._client_wrapper.httpx_client.request(
            "latest.json",
            method="GET",
            params={
                "order": order,
                "ascending": ascending,
            },
            headers={
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListLatestTopicsResponse,
                    parse_obj_as(
                        type_=ListLatestTopicsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_topic(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        topic: typing.Optional[UpdateTopicRequestTopic] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateTopicResponse]:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        topic : typing.Optional[UpdateTopicRequestTopic]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateTopicResponse]
            topic updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"t/-/{jsonable_encoder(id)}.json",
            method="PUT",
            json={
                "topic": convert_and_respect_annotation_metadata(
                    object_=topic, annotation=UpdateTopicRequestTopic, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateTopicResponse,
                    parse_obj_as(
                        type_=UpdateTopicResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_topic_by_external_id(
        self, external_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        external_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"t/external_id/{jsonable_encoder(external_id)}.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_topic(
        self, id: str, *, api_key: str, api_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetTopicResponse]:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetTopicResponse]
            specific posts
        """
        _response = self._client_wrapper.httpx_client.request(
            f"t/{jsonable_encoder(id)}.json",
            method="GET",
            headers={
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTopicResponse,
                    parse_obj_as(
                        type_=GetTopicResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def remove_topic(
        self, id: str, *, api_key: str, api_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"t/{jsonable_encoder(id)}.json",
            method="DELETE",
            headers={
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def bookmark_topic(
        self, id: str, *, api_key: str, api_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"t/{jsonable_encoder(id)}/bookmark.json",
            method="PUT",
            headers={
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_topic_timestamp(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        timestamp: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateTopicTimestampResponse]:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        timestamp : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateTopicTimestampResponse]
            topic updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"t/{jsonable_encoder(id)}/change-timestamp.json",
            method="PUT",
            json={
                "timestamp": timestamp,
            },
            headers={
                "content-type": "application/json",
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateTopicTimestampResponse,
                    parse_obj_as(
                        type_=UpdateTopicTimestampResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def invite_to_topic(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        email: typing.Optional[str] = OMIT,
        user: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[InviteToTopicResponse]:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        email : typing.Optional[str]

        user : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InviteToTopicResponse]
            topic updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"t/{jsonable_encoder(id)}/invite.json",
            method="POST",
            json={
                "email": email,
                "user": user,
            },
            headers={
                "content-type": "application/json",
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InviteToTopicResponse,
                    parse_obj_as(
                        type_=InviteToTopicResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def set_notification_level(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        notification_level: SetNotificationLevelRequestNotificationLevel,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SetNotificationLevelResponse]:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        notification_level : SetNotificationLevelRequestNotificationLevel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SetNotificationLevelResponse]
            topic updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"t/{jsonable_encoder(id)}/notifications.json",
            method="POST",
            json={
                "notification_level": notification_level,
            },
            headers={
                "content-type": "application/json",
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SetNotificationLevelResponse,
                    parse_obj_as(
                        type_=SetNotificationLevelResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_specific_posts_from_topic(
        self, id: str, *, api_key: str, api_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetSpecificPostsFromTopicResponse]:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetSpecificPostsFromTopicResponse]
            specific posts
        """
        _response = self._client_wrapper.httpx_client.request(
            f"t/{jsonable_encoder(id)}/posts.json",
            method="GET",
            headers={
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSpecificPostsFromTopicResponse,
                    parse_obj_as(
                        type_=GetSpecificPostsFromTopicResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_topic_status(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        enabled: UpdateTopicStatusRequestEnabled,
        status: UpdateTopicStatusRequestStatus,
        until: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateTopicStatusResponse]:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        enabled : UpdateTopicStatusRequestEnabled

        status : UpdateTopicStatusRequestStatus

        until : typing.Optional[str]
            Only required for `pinned` and `pinned_globally`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateTopicStatusResponse]
            topic updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"t/{jsonable_encoder(id)}/status.json",
            method="PUT",
            json={
                "enabled": enabled,
                "status": status,
                "until": until,
            },
            headers={
                "content-type": "application/json",
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateTopicStatusResponse,
                    parse_obj_as(
                        type_=UpdateTopicStatusResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_topic_timer(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        based_on_last_post: typing.Optional[bool] = OMIT,
        category_id: typing.Optional[int] = OMIT,
        status_type: typing.Optional[str] = OMIT,
        time: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateTopicTimerResponse]:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        based_on_last_post : typing.Optional[bool]

        category_id : typing.Optional[int]

        status_type : typing.Optional[str]

        time : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateTopicTimerResponse]
            topic updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"t/{jsonable_encoder(id)}/timer.json",
            method="POST",
            json={
                "based_on_last_post": based_on_last_post,
                "category_id": category_id,
                "status_type": status_type,
                "time": time,
            },
            headers={
                "content-type": "application/json",
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateTopicTimerResponse,
                    parse_obj_as(
                        type_=CreateTopicTimerResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_top_topics(
        self,
        *,
        api_key: str,
        api_username: str,
        period: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListTopTopicsResponse]:
        """
        Parameters
        ----------
        api_key : str

        api_username : str

        period : typing.Optional[str]
            Enum: `all`, `yearly`, `quarterly`, `monthly`, `weekly`, `daily`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListTopTopicsResponse]
            response
        """
        _response = self._client_wrapper.httpx_client.request(
            "top.json",
            method="GET",
            params={
                "period": period,
            },
            headers={
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListTopTopicsResponse,
                    parse_obj_as(
                        type_=ListTopTopicsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawTopicsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_latest_topics(
        self,
        *,
        api_key: str,
        api_username: str,
        order: typing.Optional[str] = None,
        ascending: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListLatestTopicsResponse]:
        """
        Parameters
        ----------
        api_key : str

        api_username : str

        order : typing.Optional[str]
            Enum: `default`, `created`, `activity`, `views`, `posts`, `category`,
            `likes`, `op_likes`, `posters`

        ascending : typing.Optional[str]
            Defaults to `desc`, add `ascending=true` to sort asc

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListLatestTopicsResponse]
            topic updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            "latest.json",
            method="GET",
            params={
                "order": order,
                "ascending": ascending,
            },
            headers={
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListLatestTopicsResponse,
                    parse_obj_as(
                        type_=ListLatestTopicsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_topic(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        topic: typing.Optional[UpdateTopicRequestTopic] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateTopicResponse]:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        topic : typing.Optional[UpdateTopicRequestTopic]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateTopicResponse]
            topic updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"t/-/{jsonable_encoder(id)}.json",
            method="PUT",
            json={
                "topic": convert_and_respect_annotation_metadata(
                    object_=topic, annotation=UpdateTopicRequestTopic, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateTopicResponse,
                    parse_obj_as(
                        type_=UpdateTopicResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_topic_by_external_id(
        self, external_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        external_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"t/external_id/{jsonable_encoder(external_id)}.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_topic(
        self, id: str, *, api_key: str, api_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetTopicResponse]:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetTopicResponse]
            specific posts
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"t/{jsonable_encoder(id)}.json",
            method="GET",
            headers={
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTopicResponse,
                    parse_obj_as(
                        type_=GetTopicResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def remove_topic(
        self, id: str, *, api_key: str, api_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"t/{jsonable_encoder(id)}.json",
            method="DELETE",
            headers={
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def bookmark_topic(
        self, id: str, *, api_key: str, api_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"t/{jsonable_encoder(id)}/bookmark.json",
            method="PUT",
            headers={
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_topic_timestamp(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        timestamp: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateTopicTimestampResponse]:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        timestamp : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateTopicTimestampResponse]
            topic updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"t/{jsonable_encoder(id)}/change-timestamp.json",
            method="PUT",
            json={
                "timestamp": timestamp,
            },
            headers={
                "content-type": "application/json",
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateTopicTimestampResponse,
                    parse_obj_as(
                        type_=UpdateTopicTimestampResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def invite_to_topic(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        email: typing.Optional[str] = OMIT,
        user: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[InviteToTopicResponse]:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        email : typing.Optional[str]

        user : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InviteToTopicResponse]
            topic updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"t/{jsonable_encoder(id)}/invite.json",
            method="POST",
            json={
                "email": email,
                "user": user,
            },
            headers={
                "content-type": "application/json",
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InviteToTopicResponse,
                    parse_obj_as(
                        type_=InviteToTopicResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def set_notification_level(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        notification_level: SetNotificationLevelRequestNotificationLevel,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SetNotificationLevelResponse]:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        notification_level : SetNotificationLevelRequestNotificationLevel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SetNotificationLevelResponse]
            topic updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"t/{jsonable_encoder(id)}/notifications.json",
            method="POST",
            json={
                "notification_level": notification_level,
            },
            headers={
                "content-type": "application/json",
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SetNotificationLevelResponse,
                    parse_obj_as(
                        type_=SetNotificationLevelResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_specific_posts_from_topic(
        self, id: str, *, api_key: str, api_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetSpecificPostsFromTopicResponse]:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetSpecificPostsFromTopicResponse]
            specific posts
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"t/{jsonable_encoder(id)}/posts.json",
            method="GET",
            headers={
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSpecificPostsFromTopicResponse,
                    parse_obj_as(
                        type_=GetSpecificPostsFromTopicResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_topic_status(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        enabled: UpdateTopicStatusRequestEnabled,
        status: UpdateTopicStatusRequestStatus,
        until: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateTopicStatusResponse]:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        enabled : UpdateTopicStatusRequestEnabled

        status : UpdateTopicStatusRequestStatus

        until : typing.Optional[str]
            Only required for `pinned` and `pinned_globally`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateTopicStatusResponse]
            topic updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"t/{jsonable_encoder(id)}/status.json",
            method="PUT",
            json={
                "enabled": enabled,
                "status": status,
                "until": until,
            },
            headers={
                "content-type": "application/json",
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateTopicStatusResponse,
                    parse_obj_as(
                        type_=UpdateTopicStatusResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_topic_timer(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        based_on_last_post: typing.Optional[bool] = OMIT,
        category_id: typing.Optional[int] = OMIT,
        status_type: typing.Optional[str] = OMIT,
        time: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateTopicTimerResponse]:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        based_on_last_post : typing.Optional[bool]

        category_id : typing.Optional[int]

        status_type : typing.Optional[str]

        time : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateTopicTimerResponse]
            topic updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"t/{jsonable_encoder(id)}/timer.json",
            method="POST",
            json={
                "based_on_last_post": based_on_last_post,
                "category_id": category_id,
                "status_type": status_type,
                "time": time,
            },
            headers={
                "content-type": "application/json",
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateTopicTimerResponse,
                    parse_obj_as(
                        type_=CreateTopicTimerResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_top_topics(
        self,
        *,
        api_key: str,
        api_username: str,
        period: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListTopTopicsResponse]:
        """
        Parameters
        ----------
        api_key : str

        api_username : str

        period : typing.Optional[str]
            Enum: `all`, `yearly`, `quarterly`, `monthly`, `weekly`, `daily`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListTopTopicsResponse]
            response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "top.json",
            method="GET",
            params={
                "period": period,
            },
            headers={
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListTopTopicsResponse,
                    parse_obj_as(
                        type_=ListTopTopicsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
