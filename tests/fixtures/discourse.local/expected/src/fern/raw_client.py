

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .types.search_response import SearchResponse


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search(
        self,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SearchResponse]:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            The query string needs to be url encoded and is made up of the following options:
            - Search term. This is just a string. Usually it would be the first item in the query.
            - `@<username>`: Use the `@` followed by the username to specify posts by this user.
            - `#<category>`: Use the `#` followed by the category slug to search within this category.
            - `tags:`: `api,solved` or for posts that have all the specified tags `api+solved`.
            - `before:`: `yyyy-mm-dd`
            - `after:`: `yyyy-mm-dd`
            - `order:`: `latest`, `likes`, `views`, `latest_topic`
            - `assigned:`: username (without `@`)
            - `in:`: `title`, `likes`, `personal`, `messages`, `seen`, `unseen`, `posted`, `created`, `watching`, `tracking`, `bookmarks`, `assigned`, `unassigned`, `first`, `pinned`, `wiki`
            - `with:`: `images`
            - `status:`: `open`, `closed`, `public`, `archived`, `noreplies`, `single_user`, `solved`, `unsolved`
            - `group:`: group_name or group_id
            - `group_messages:`: group_name or group_id
            - `min_posts:`: 1
            - `max_posts:`: 10
            - `min_views:`: 1
            - `max_views:`: 10
            
            If you are using cURL you can use the `-G` and the `--data-urlencode` flags to encode the query:
            
            ```
            curl -i -sS -X GET -G "http://localhost:4200/search.json" \
            --data-urlencode 'q=wordpress @scossar #fun after:2020-01-01'
            ```
        
        page : typing.Optional[int]
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        HttpResponse[SearchResponse]
            success response
        """
        _response = self._client_wrapper.httpx_client.request(
            "search.json",
            method="GET",
            params={
                "q": q,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchResponse,
                    parse_obj_as(
                        type_=SearchResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search(
        self,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SearchResponse]:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            The query string needs to be url encoded and is made up of the following options:
            - Search term. This is just a string. Usually it would be the first item in the query.
            - `@<username>`: Use the `@` followed by the username to specify posts by this user.
            - `#<category>`: Use the `#` followed by the category slug to search within this category.
            - `tags:`: `api,solved` or for posts that have all the specified tags `api+solved`.
            - `before:`: `yyyy-mm-dd`
            - `after:`: `yyyy-mm-dd`
            - `order:`: `latest`, `likes`, `views`, `latest_topic`
            - `assigned:`: username (without `@`)
            - `in:`: `title`, `likes`, `personal`, `messages`, `seen`, `unseen`, `posted`, `created`, `watching`, `tracking`, `bookmarks`, `assigned`, `unassigned`, `first`, `pinned`, `wiki`
            - `with:`: `images`
            - `status:`: `open`, `closed`, `public`, `archived`, `noreplies`, `single_user`, `solved`, `unsolved`
            - `group:`: group_name or group_id
            - `group_messages:`: group_name or group_id
            - `min_posts:`: 1
            - `max_posts:`: 10
            - `min_views:`: 1
            - `max_views:`: 10
            
            If you are using cURL you can use the `-G` and the `--data-urlencode` flags to encode the query:
            
            ```
            curl -i -sS -X GET -G "http://localhost:4200/search.json" \
            --data-urlencode 'q=wordpress @scossar #fun after:2020-01-01'
            ```
        
        page : typing.Optional[int]
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        AsyncHttpResponse[SearchResponse]
            success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "search.json",
            method="GET",
            params={
                "q": q,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchResponse,
                    parse_obj_as(
                        type_=SearchResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
