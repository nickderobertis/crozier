

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.content_get_content_by_id_response import ContentGetContentByIdResponse
from .types.content_get_content_by_tag_and_type_response import ContentGetContentByTagAndTypeResponse
from .types.content_get_content_type_response import ContentGetContentTypeResponse
from .types.content_rss_news_articles_response import ContentRssNewsArticlesResponse
from .types.content_search_content_by_tag_and_type_response import ContentSearchContentByTagAndTypeResponse
from .types.content_search_content_with_text_response import ContentSearchContentWithTextResponse
from .types.content_search_help_articles_response import ContentSearchHelpArticlesResponse
from pydantic import ValidationError


class RawContentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getcontentbyid(
        self,
        id: int,
        locale: str,
        *,
        head: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContentGetContentByIdResponse]:
        """
        Returns a content item referenced by id

        Parameters
        ----------
        id : int


        locale : str


        head : typing.Optional[bool]
            false

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContentGetContentByIdResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Content/GetContentById/{encode_path_param(id)}/{encode_path_param(locale)}/",
            method="GET",
            params={
                "head": head,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentGetContentByIdResponse,
                    parse_obj_as(
                        type_=ContentGetContentByIdResponse,
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

    def getcontentbytagandtype(
        self,
        tag: str,
        type: str,
        locale: str,
        *,
        head: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContentGetContentByTagAndTypeResponse]:
        """
        Returns the newest item that matches a given tag and Content Type.

        Parameters
        ----------
        tag : str


        type : str


        locale : str


        head : typing.Optional[bool]
            Not used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContentGetContentByTagAndTypeResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Content/GetContentByTagAndType/{encode_path_param(tag)}/{encode_path_param(type)}/{encode_path_param(locale)}/",
            method="GET",
            params={
                "head": head,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentGetContentByTagAndTypeResponse,
                    parse_obj_as(
                        type_=ContentGetContentByTagAndTypeResponse,
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

    def getcontenttype(
        self, type: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ContentGetContentTypeResponse]:
        """
        Gets an object describing a particular variant of content.

        Parameters
        ----------
        type : str


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContentGetContentTypeResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Content/GetContentType/{encode_path_param(type)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentGetContentTypeResponse,
                    parse_obj_as(
                        type_=ContentGetContentTypeResponse,
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

    def rssnewsarticles(
        self,
        page_token: str,
        *,
        categoryfilter: typing.Optional[str] = None,
        includebody: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContentRssNewsArticlesResponse]:
        """
        Returns a JSON string response that is the RSS feed for news articles.

        Parameters
        ----------
        page_token : str
            Zero-based pagination token for paging through result sets.

        categoryfilter : typing.Optional[str]
            Optionally filter response to only include news items in a certain category.

        includebody : typing.Optional[bool]
            Optionally include full content body for each news item.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContentRssNewsArticlesResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Content/Rss/NewsArticles/{encode_path_param(page_token)}/",
            method="GET",
            params={
                "categoryfilter": categoryfilter,
                "includebody": includebody,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentRssNewsArticlesResponse,
                    parse_obj_as(
                        type_=ContentRssNewsArticlesResponse,
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

    def searchcontentwithtext(
        self,
        locale: str,
        *,
        ctype: typing.Optional[str] = None,
        currentpage: typing.Optional[int] = None,
        head: typing.Optional[bool] = None,
        searchtext: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContentSearchContentWithTextResponse]:
        """
        Gets content based on querystring information passed in. Provides basic search and text search capabilities.

        Parameters
        ----------
        locale : str


        ctype : typing.Optional[str]
            Content type tag: Help, News, etc. Supply multiple ctypes separated by space.

        currentpage : typing.Optional[int]
            Page number for the search results, starting with page 1.

        head : typing.Optional[bool]
            Not used.

        searchtext : typing.Optional[str]
            Word or phrase for the search.

        source : typing.Optional[str]
            For analytics, hint at the part of the app that triggered the search. Optional.

        tag : typing.Optional[str]
            Tag used on the content to be searched.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContentSearchContentWithTextResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Content/Search/{encode_path_param(locale)}/",
            method="GET",
            params={
                "ctype": ctype,
                "currentpage": currentpage,
                "head": head,
                "searchtext": searchtext,
                "source": source,
                "tag": tag,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentSearchContentWithTextResponse,
                    parse_obj_as(
                        type_=ContentSearchContentWithTextResponse,
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

    def searchcontentbytagandtype(
        self,
        tag: str,
        type: str,
        locale: str,
        *,
        currentpage: typing.Optional[int] = None,
        head: typing.Optional[bool] = None,
        itemsperpage: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContentSearchContentByTagAndTypeResponse]:
        """
        Searches for Content Items that match the given Tag and Content Type.

        Parameters
        ----------
        tag : str


        type : str


        locale : str


        currentpage : typing.Optional[int]
            Page number for the search results starting with page 1.

        head : typing.Optional[bool]
            Not used.

        itemsperpage : typing.Optional[int]
            Not used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContentSearchContentByTagAndTypeResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Content/SearchContentByTagAndType/{encode_path_param(tag)}/{encode_path_param(type)}/{encode_path_param(locale)}/",
            method="GET",
            params={
                "currentpage": currentpage,
                "head": head,
                "itemsperpage": itemsperpage,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentSearchContentByTagAndTypeResponse,
                    parse_obj_as(
                        type_=ContentSearchContentByTagAndTypeResponse,
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

    def searchhelparticles(
        self, searchtext: str, size: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ContentSearchHelpArticlesResponse]:
        """
        Search for Help Articles.

        Parameters
        ----------
        searchtext : str


        size : str


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContentSearchHelpArticlesResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Content/SearchHelpArticles/{encode_path_param(searchtext)}/{encode_path_param(size)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentSearchHelpArticlesResponse,
                    parse_obj_as(
                        type_=ContentSearchHelpArticlesResponse,
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


class AsyncRawContentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getcontentbyid(
        self,
        id: int,
        locale: str,
        *,
        head: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContentGetContentByIdResponse]:
        """
        Returns a content item referenced by id

        Parameters
        ----------
        id : int


        locale : str


        head : typing.Optional[bool]
            false

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContentGetContentByIdResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Content/GetContentById/{encode_path_param(id)}/{encode_path_param(locale)}/",
            method="GET",
            params={
                "head": head,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentGetContentByIdResponse,
                    parse_obj_as(
                        type_=ContentGetContentByIdResponse,
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

    async def getcontentbytagandtype(
        self,
        tag: str,
        type: str,
        locale: str,
        *,
        head: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContentGetContentByTagAndTypeResponse]:
        """
        Returns the newest item that matches a given tag and Content Type.

        Parameters
        ----------
        tag : str


        type : str


        locale : str


        head : typing.Optional[bool]
            Not used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContentGetContentByTagAndTypeResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Content/GetContentByTagAndType/{encode_path_param(tag)}/{encode_path_param(type)}/{encode_path_param(locale)}/",
            method="GET",
            params={
                "head": head,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentGetContentByTagAndTypeResponse,
                    parse_obj_as(
                        type_=ContentGetContentByTagAndTypeResponse,
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

    async def getcontenttype(
        self, type: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ContentGetContentTypeResponse]:
        """
        Gets an object describing a particular variant of content.

        Parameters
        ----------
        type : str


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContentGetContentTypeResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Content/GetContentType/{encode_path_param(type)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentGetContentTypeResponse,
                    parse_obj_as(
                        type_=ContentGetContentTypeResponse,
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

    async def rssnewsarticles(
        self,
        page_token: str,
        *,
        categoryfilter: typing.Optional[str] = None,
        includebody: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContentRssNewsArticlesResponse]:
        """
        Returns a JSON string response that is the RSS feed for news articles.

        Parameters
        ----------
        page_token : str
            Zero-based pagination token for paging through result sets.

        categoryfilter : typing.Optional[str]
            Optionally filter response to only include news items in a certain category.

        includebody : typing.Optional[bool]
            Optionally include full content body for each news item.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContentRssNewsArticlesResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Content/Rss/NewsArticles/{encode_path_param(page_token)}/",
            method="GET",
            params={
                "categoryfilter": categoryfilter,
                "includebody": includebody,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentRssNewsArticlesResponse,
                    parse_obj_as(
                        type_=ContentRssNewsArticlesResponse,
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

    async def searchcontentwithtext(
        self,
        locale: str,
        *,
        ctype: typing.Optional[str] = None,
        currentpage: typing.Optional[int] = None,
        head: typing.Optional[bool] = None,
        searchtext: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContentSearchContentWithTextResponse]:
        """
        Gets content based on querystring information passed in. Provides basic search and text search capabilities.

        Parameters
        ----------
        locale : str


        ctype : typing.Optional[str]
            Content type tag: Help, News, etc. Supply multiple ctypes separated by space.

        currentpage : typing.Optional[int]
            Page number for the search results, starting with page 1.

        head : typing.Optional[bool]
            Not used.

        searchtext : typing.Optional[str]
            Word or phrase for the search.

        source : typing.Optional[str]
            For analytics, hint at the part of the app that triggered the search. Optional.

        tag : typing.Optional[str]
            Tag used on the content to be searched.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContentSearchContentWithTextResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Content/Search/{encode_path_param(locale)}/",
            method="GET",
            params={
                "ctype": ctype,
                "currentpage": currentpage,
                "head": head,
                "searchtext": searchtext,
                "source": source,
                "tag": tag,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentSearchContentWithTextResponse,
                    parse_obj_as(
                        type_=ContentSearchContentWithTextResponse,
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

    async def searchcontentbytagandtype(
        self,
        tag: str,
        type: str,
        locale: str,
        *,
        currentpage: typing.Optional[int] = None,
        head: typing.Optional[bool] = None,
        itemsperpage: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContentSearchContentByTagAndTypeResponse]:
        """
        Searches for Content Items that match the given Tag and Content Type.

        Parameters
        ----------
        tag : str


        type : str


        locale : str


        currentpage : typing.Optional[int]
            Page number for the search results starting with page 1.

        head : typing.Optional[bool]
            Not used.

        itemsperpage : typing.Optional[int]
            Not used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContentSearchContentByTagAndTypeResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Content/SearchContentByTagAndType/{encode_path_param(tag)}/{encode_path_param(type)}/{encode_path_param(locale)}/",
            method="GET",
            params={
                "currentpage": currentpage,
                "head": head,
                "itemsperpage": itemsperpage,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentSearchContentByTagAndTypeResponse,
                    parse_obj_as(
                        type_=ContentSearchContentByTagAndTypeResponse,
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

    async def searchhelparticles(
        self, searchtext: str, size: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ContentSearchHelpArticlesResponse]:
        """
        Search for Help Articles.

        Parameters
        ----------
        searchtext : str


        size : str


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContentSearchHelpArticlesResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Content/SearchHelpArticles/{encode_path_param(searchtext)}/{encode_path_param(size)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentSearchHelpArticlesResponse,
                    parse_obj_as(
                        type_=ContentSearchHelpArticlesResponse,
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
