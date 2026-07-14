

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.create_topic_post_pm_response import CreateTopicPostPmResponse
from .types.get_post_response import GetPostResponse
from .types.list_posts_response import ListPostsResponse
from .types.lock_post_response import LockPostResponse
from .types.perform_post_action_response import PerformPostActionResponse
from .types.post_replies_response_item import PostRepliesResponseItem
from .types.update_post_request_post import UpdatePostRequestPost
from .types.update_post_response import UpdatePostResponse


OMIT = typing.cast(typing.Any, ...)


class RawPostsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def perform_post_action(
        self,
        *,
        api_key: str,
        api_username: str,
        id: int,
        post_action_type_id: int,
        flag_topic: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PerformPostActionResponse]:
        """
        Parameters
        ----------
        api_key : str

        api_username : str

        id : int

        post_action_type_id : int

        flag_topic : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PerformPostActionResponse]
            post updated
        """
        _response = self._client_wrapper.httpx_client.request(
            "post_actions.json",
            method="POST",
            json={
                "flag_topic": flag_topic,
                "id": id,
                "post_action_type_id": post_action_type_id,
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
                    PerformPostActionResponse,
                    parse_obj_as(
                        type_=PerformPostActionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_posts(
        self,
        *,
        api_key: str,
        api_username: str,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListPostsResponse]:
        """
        Parameters
        ----------
        api_key : str

        api_username : str

        before : typing.Optional[str]
            Load posts with an id lower than this value. Useful for pagination.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListPostsResponse]
            latest posts
        """
        _response = self._client_wrapper.httpx_client.request(
            "posts.json",
            method="GET",
            params={
                "before": before,
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
                    ListPostsResponse,
                    parse_obj_as(
                        type_=ListPostsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_topic_post_pm(
        self,
        *,
        raw: str,
        archetype: typing.Optional[str] = OMIT,
        category: typing.Optional[int] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        embed_url: typing.Optional[str] = OMIT,
        external_id: typing.Optional[str] = OMIT,
        target_recipients: typing.Optional[str] = OMIT,
        target_usernames: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        topic_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateTopicPostPmResponse]:
        """
        Parameters
        ----------
        raw : str

        archetype : typing.Optional[str]
            Required for new private message.

        category : typing.Optional[int]
            Optional if creating a new topic, and ignored if creating
            a new post.

        created_at : typing.Optional[str]

        embed_url : typing.Optional[str]
            Provide a URL from a remote system to associate a forum
            topic with that URL, typically for using Discourse as a comments
            system for an external blog.

        external_id : typing.Optional[str]
            Provide an external_id from a remote system to associate
            a forum topic with that id.

        target_recipients : typing.Optional[str]
            Required for private message, comma separated.

        target_usernames : typing.Optional[str]
            Deprecated. Use target_recipients instead.

        title : typing.Optional[str]
            Required if creating a new topic or new private message.

        topic_id : typing.Optional[int]
            Required if creating a new post.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateTopicPostPmResponse]
            post created
        """
        _response = self._client_wrapper.httpx_client.request(
            "posts.json",
            method="POST",
            json={
                "archetype": archetype,
                "category": category,
                "created_at": created_at,
                "embed_url": embed_url,
                "external_id": external_id,
                "raw": raw,
                "target_recipients": target_recipients,
                "target_usernames": target_usernames,
                "title": title,
                "topic_id": topic_id,
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
                    CreateTopicPostPmResponse,
                    parse_obj_as(
                        type_=CreateTopicPostPmResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_post(
        self, id: str, *, api_key: str, api_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetPostResponse]:
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
        HttpResponse[GetPostResponse]
            latest posts
        """
        _response = self._client_wrapper.httpx_client.request(
            f"posts/{jsonable_encoder(id)}.json",
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
                    GetPostResponse,
                    parse_obj_as(
                        type_=GetPostResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_post(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        post: typing.Optional[UpdatePostRequestPost] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdatePostResponse]:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        post : typing.Optional[UpdatePostRequestPost]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdatePostResponse]
            post updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"posts/{jsonable_encoder(id)}.json",
            method="PUT",
            json={
                "post": convert_and_respect_annotation_metadata(
                    object_=post, annotation=UpdatePostRequestPost, direction="write"
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
                    UpdatePostResponse,
                    parse_obj_as(
                        type_=UpdatePostResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_post(
        self,
        id: int,
        *,
        force_destroy: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        force_destroy : typing.Optional[bool]
            The `SiteSetting.can_permanently_delete` needs to be
            enabled first before this param can be used. Also this endpoint
            needs to be called first without `force_destroy` and then followed
            up with a second call 5 minutes later with `force_destroy` to
            permanently delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"posts/{jsonable_encoder(id)}.json",
            method="DELETE",
            json={
                "force_destroy": force_destroy,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def lock_post(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        locked: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LockPostResponse]:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        locked : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LockPostResponse]
            post updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"posts/{jsonable_encoder(id)}/locked.json",
            method="PUT",
            json={
                "locked": locked,
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
                    LockPostResponse,
                    parse_obj_as(
                        type_=LockPostResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_replies(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[PostRepliesResponseItem]]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[PostRepliesResponseItem]]
            post replies
        """
        _response = self._client_wrapper.httpx_client.request(
            f"posts/{jsonable_encoder(id)}/replies.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PostRepliesResponseItem],
                    parse_obj_as(
                        type_=typing.List[PostRepliesResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawPostsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def perform_post_action(
        self,
        *,
        api_key: str,
        api_username: str,
        id: int,
        post_action_type_id: int,
        flag_topic: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PerformPostActionResponse]:
        """
        Parameters
        ----------
        api_key : str

        api_username : str

        id : int

        post_action_type_id : int

        flag_topic : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PerformPostActionResponse]
            post updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            "post_actions.json",
            method="POST",
            json={
                "flag_topic": flag_topic,
                "id": id,
                "post_action_type_id": post_action_type_id,
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
                    PerformPostActionResponse,
                    parse_obj_as(
                        type_=PerformPostActionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_posts(
        self,
        *,
        api_key: str,
        api_username: str,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListPostsResponse]:
        """
        Parameters
        ----------
        api_key : str

        api_username : str

        before : typing.Optional[str]
            Load posts with an id lower than this value. Useful for pagination.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListPostsResponse]
            latest posts
        """
        _response = await self._client_wrapper.httpx_client.request(
            "posts.json",
            method="GET",
            params={
                "before": before,
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
                    ListPostsResponse,
                    parse_obj_as(
                        type_=ListPostsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_topic_post_pm(
        self,
        *,
        raw: str,
        archetype: typing.Optional[str] = OMIT,
        category: typing.Optional[int] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        embed_url: typing.Optional[str] = OMIT,
        external_id: typing.Optional[str] = OMIT,
        target_recipients: typing.Optional[str] = OMIT,
        target_usernames: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        topic_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateTopicPostPmResponse]:
        """
        Parameters
        ----------
        raw : str

        archetype : typing.Optional[str]
            Required for new private message.

        category : typing.Optional[int]
            Optional if creating a new topic, and ignored if creating
            a new post.

        created_at : typing.Optional[str]

        embed_url : typing.Optional[str]
            Provide a URL from a remote system to associate a forum
            topic with that URL, typically for using Discourse as a comments
            system for an external blog.

        external_id : typing.Optional[str]
            Provide an external_id from a remote system to associate
            a forum topic with that id.

        target_recipients : typing.Optional[str]
            Required for private message, comma separated.

        target_usernames : typing.Optional[str]
            Deprecated. Use target_recipients instead.

        title : typing.Optional[str]
            Required if creating a new topic or new private message.

        topic_id : typing.Optional[int]
            Required if creating a new post.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateTopicPostPmResponse]
            post created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "posts.json",
            method="POST",
            json={
                "archetype": archetype,
                "category": category,
                "created_at": created_at,
                "embed_url": embed_url,
                "external_id": external_id,
                "raw": raw,
                "target_recipients": target_recipients,
                "target_usernames": target_usernames,
                "title": title,
                "topic_id": topic_id,
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
                    CreateTopicPostPmResponse,
                    parse_obj_as(
                        type_=CreateTopicPostPmResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_post(
        self, id: str, *, api_key: str, api_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetPostResponse]:
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
        AsyncHttpResponse[GetPostResponse]
            latest posts
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"posts/{jsonable_encoder(id)}.json",
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
                    GetPostResponse,
                    parse_obj_as(
                        type_=GetPostResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_post(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        post: typing.Optional[UpdatePostRequestPost] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdatePostResponse]:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        post : typing.Optional[UpdatePostRequestPost]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdatePostResponse]
            post updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"posts/{jsonable_encoder(id)}.json",
            method="PUT",
            json={
                "post": convert_and_respect_annotation_metadata(
                    object_=post, annotation=UpdatePostRequestPost, direction="write"
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
                    UpdatePostResponse,
                    parse_obj_as(
                        type_=UpdatePostResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_post(
        self,
        id: int,
        *,
        force_destroy: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        force_destroy : typing.Optional[bool]
            The `SiteSetting.can_permanently_delete` needs to be
            enabled first before this param can be used. Also this endpoint
            needs to be called first without `force_destroy` and then followed
            up with a second call 5 minutes later with `force_destroy` to
            permanently delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"posts/{jsonable_encoder(id)}.json",
            method="DELETE",
            json={
                "force_destroy": force_destroy,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def lock_post(
        self,
        id: str,
        *,
        api_key: str,
        api_username: str,
        locked: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LockPostResponse]:
        """
        Parameters
        ----------
        id : str

        api_key : str

        api_username : str

        locked : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LockPostResponse]
            post updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"posts/{jsonable_encoder(id)}/locked.json",
            method="PUT",
            json={
                "locked": locked,
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
                    LockPostResponse,
                    parse_obj_as(
                        type_=LockPostResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_replies(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[PostRepliesResponseItem]]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[PostRepliesResponseItem]]
            post replies
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"posts/{jsonable_encoder(id)}/replies.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PostRepliesResponseItem],
                    parse_obj_as(
                        type_=typing.List[PostRepliesResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
