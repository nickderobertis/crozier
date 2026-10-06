

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.forbidden_error import ForbiddenError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.deleted_post_response import DeletedPostResponse
from ..types.error_result_user_is_not_post_creator import ErrorResultUserIsNotPostCreator
from ..types.full_text_posts_search_posts_full_text_search_get_request_limit import (
    FullTextPostsSearchPostsFullTextSearchGetRequestLimit,
)
from ..types.full_text_posts_search_posts_full_text_search_get_request_offset import (
    FullTextPostsSearchPostsFullTextSearchGetRequestOffset,
)
from ..types.get_posts_order import GetPostsOrder
from ..types.get_user_posts_posts_user_posts_get_request_limit import GetUserPostsPostsUserPostsGetRequestLimit
from ..types.get_user_posts_posts_user_posts_get_request_offset import GetUserPostsPostsUserPostsGetRequestOffset
from ..types.http_validation_error import HttpValidationError
from ..types.post_response import PostResponse
from ..types.posts_response import PostsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPostsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_user_posts(
        self,
        *,
        creator_id: int,
        offset: typing.Optional[GetUserPostsPostsUserPostsGetRequestOffset] = None,
        limit: typing.Optional[GetUserPostsPostsUserPostsGetRequestLimit] = None,
        order: typing.Optional[GetPostsOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostsResponse]:
        """
        Получение всех постов пользователя

        Parameters
        ----------
        creator_id : int

        offset : typing.Optional[GetUserPostsPostsUserPostsGetRequestOffset]

        limit : typing.Optional[GetUserPostsPostsUserPostsGetRequestLimit]

        order : typing.Optional[GetPostsOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostsResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "posts/user_posts",
            method="GET",
            params={
                "creator_id": creator_id,
                "offset": offset,
                "limit": limit,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostsResponse,
                    parse_obj_as(
                        type_=PostsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def full_text_posts_search(
        self,
        *,
        query_string: str,
        offset: typing.Optional[FullTextPostsSearchPostsFullTextSearchGetRequestOffset] = None,
        limit: typing.Optional[FullTextPostsSearchPostsFullTextSearchGetRequestLimit] = None,
        order: typing.Optional[GetPostsOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostsResponse]:
        """
        Получение всех постов пользователя

        Parameters
        ----------
        query_string : str

        offset : typing.Optional[FullTextPostsSearchPostsFullTextSearchGetRequestOffset]

        limit : typing.Optional[FullTextPostsSearchPostsFullTextSearchGetRequestLimit]

        order : typing.Optional[GetPostsOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostsResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "posts/full_text_search",
            method="GET",
            params={
                "query_string": query_string,
                "offset": offset,
                "limit": limit,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostsResponse,
                    parse_obj_as(
                        type_=PostsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def create_post(
        self, *, authorization: str, text_content: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostResponse]:
        """
        Создание поста

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        text_content : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "posts/create_post",
            method="POST",
            json={
                "text_content": text_content,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostResponse,
                    parse_obj_as(
                        type_=PostResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def delete_post(
        self, *, authorization: str, post_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeletedPostResponse]:
        """
        Удание поста пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        post_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeletedPostResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "posts/delete_post",
            method="DELETE",
            json={
                "post_id": post_id,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeletedPostResponse,
                    parse_obj_as(
                        type_=DeletedPostResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResultUserIsNotPostCreator,
                        parse_obj_as(
                            type_=ErrorResultUserIsNotPostCreator,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def update_post(
        self,
        *,
        authorization: str,
        post_id: str,
        text_content: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostResponse]:
        """
        Обнволение поста пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        post_id : str

        text_content : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "posts/update_post",
            method="PATCH",
            json={
                "post_id": post_id,
                "text_content": text_content,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostResponse,
                    parse_obj_as(
                        type_=PostResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResultUserIsNotPostCreator,
                        parse_obj_as(
                            type_=ErrorResultUserIsNotPostCreator,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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


class AsyncRawPostsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_user_posts(
        self,
        *,
        creator_id: int,
        offset: typing.Optional[GetUserPostsPostsUserPostsGetRequestOffset] = None,
        limit: typing.Optional[GetUserPostsPostsUserPostsGetRequestLimit] = None,
        order: typing.Optional[GetPostsOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostsResponse]:
        """
        Получение всех постов пользователя

        Parameters
        ----------
        creator_id : int

        offset : typing.Optional[GetUserPostsPostsUserPostsGetRequestOffset]

        limit : typing.Optional[GetUserPostsPostsUserPostsGetRequestLimit]

        order : typing.Optional[GetPostsOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostsResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "posts/user_posts",
            method="GET",
            params={
                "creator_id": creator_id,
                "offset": offset,
                "limit": limit,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostsResponse,
                    parse_obj_as(
                        type_=PostsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def full_text_posts_search(
        self,
        *,
        query_string: str,
        offset: typing.Optional[FullTextPostsSearchPostsFullTextSearchGetRequestOffset] = None,
        limit: typing.Optional[FullTextPostsSearchPostsFullTextSearchGetRequestLimit] = None,
        order: typing.Optional[GetPostsOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostsResponse]:
        """
        Получение всех постов пользователя

        Parameters
        ----------
        query_string : str

        offset : typing.Optional[FullTextPostsSearchPostsFullTextSearchGetRequestOffset]

        limit : typing.Optional[FullTextPostsSearchPostsFullTextSearchGetRequestLimit]

        order : typing.Optional[GetPostsOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostsResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "posts/full_text_search",
            method="GET",
            params={
                "query_string": query_string,
                "offset": offset,
                "limit": limit,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostsResponse,
                    parse_obj_as(
                        type_=PostsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def create_post(
        self, *, authorization: str, text_content: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostResponse]:
        """
        Создание поста

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        text_content : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "posts/create_post",
            method="POST",
            json={
                "text_content": text_content,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostResponse,
                    parse_obj_as(
                        type_=PostResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def delete_post(
        self, *, authorization: str, post_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeletedPostResponse]:
        """
        Удание поста пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        post_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeletedPostResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "posts/delete_post",
            method="DELETE",
            json={
                "post_id": post_id,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeletedPostResponse,
                    parse_obj_as(
                        type_=DeletedPostResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResultUserIsNotPostCreator,
                        parse_obj_as(
                            type_=ErrorResultUserIsNotPostCreator,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def update_post(
        self,
        *,
        authorization: str,
        post_id: str,
        text_content: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostResponse]:
        """
        Обнволение поста пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        post_id : str

        text_content : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "posts/update_post",
            method="PATCH",
            json={
                "post_id": post_id,
                "text_content": text_content,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostResponse,
                    parse_obj_as(
                        type_=PostResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResultUserIsNotPostCreator,
                        parse_obj_as(
                            type_=ErrorResultUserIsNotPostCreator,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
