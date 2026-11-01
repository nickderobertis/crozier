

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.error_response import ErrorResponse
from ..types.tag import Tag
from ..types.tag_set import TagSet
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTagClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_tags(
        self,
        *,
        owned_by: typing.Optional[str] = None,
        tag_set: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Tag]]:
        """
        Retrieve tags.

        Parameters
        ----------
        owned_by : typing.Optional[str]
            Restrict results to those owned by this user.

        tag_set : typing.Optional[str]
            Restrict results to tags belonging to this tag set.

        url_words : typing.Optional[str]
            Restrict results by urlWords. Should be used with ownedBy when searching for one of your own tags.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Tag]]
            A list of tags
        """
        _response = self._client_wrapper.httpx_client.request(
            "tags",
            method="GET",
            params={
                "ownedBy": owned_by,
                "tagSet": tag_set,
                "urlWords": url_words,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Tag],
                    parse_obj_as(
                        type_=typing.List[Tag],
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

    def create_a_new_tag(
        self,
        *,
        name: str,
        colour: typing.Optional[str] = OMIT,
        tag_set: typing.Optional[TagSet] = OMIT,
        url_words: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Tag]:
        """
        Parameters
        ----------
        name : str

        colour : typing.Optional[str]

        tag_set : typing.Optional[TagSet]

        url_words : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Tag]
            Tag created
        """
        _response = self._client_wrapper.httpx_client.request(
            "tags",
            method="POST",
            json={
                "colour": colour,
                "name": name,
                "tagSet": convert_and_respect_annotation_metadata(
                    object_=tag_set, annotation=TagSet, direction="write"
                ),
                "urlWords": url_words,
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
                    Tag,
                    parse_obj_as(
                        type_=Tag,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def retrieve_a_single_tag_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Tag]:
        """
        Parameters
        ----------
        id : str
            Id of the tag to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Tag]
            The tag
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tags/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tag,
                    parse_obj_as(
                        type_=Tag,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def list_tag_sets(
        self,
        *,
        owned_by: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[TagSet]]:
        """
        Retrieve tag sets.

        Parameters
        ----------
        owned_by : typing.Optional[str]
            Restrict results to those owned by this user.

        url_words : typing.Optional[str]
            Restrict results by urlWords. Should be used with ownedBy when searching for one of your own tag sets.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[TagSet]]
            A list of tag sets
        """
        _response = self._client_wrapper.httpx_client.request(
            "tagsets",
            method="GET",
            params={
                "ownedBy": owned_by,
                "urlWords": url_words,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TagSet],
                    parse_obj_as(
                        type_=typing.List[TagSet],
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

    def create_a_new_tag_set(
        self, *, name: str, url_words: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TagSet]:
        """
        Parameters
        ----------
        name : str

        url_words : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TagSet]
            Tagset created
        """
        _response = self._client_wrapper.httpx_client.request(
            "tagsets",
            method="POST",
            json={
                "name": name,
                "urlWords": url_words,
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
                    TagSet,
                    parse_obj_as(
                        type_=TagSet,
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

    def retrieve_a_single_tag_set_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TagSet]:
        """
        Parameters
        ----------
        id : str
            Id of the tag set to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TagSet]
            The tag set
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tagsets/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TagSet,
                    parse_obj_as(
                        type_=TagSet,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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


class AsyncRawTagClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_tags(
        self,
        *,
        owned_by: typing.Optional[str] = None,
        tag_set: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Tag]]:
        """
        Retrieve tags.

        Parameters
        ----------
        owned_by : typing.Optional[str]
            Restrict results to those owned by this user.

        tag_set : typing.Optional[str]
            Restrict results to tags belonging to this tag set.

        url_words : typing.Optional[str]
            Restrict results by urlWords. Should be used with ownedBy when searching for one of your own tags.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Tag]]
            A list of tags
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tags",
            method="GET",
            params={
                "ownedBy": owned_by,
                "tagSet": tag_set,
                "urlWords": url_words,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Tag],
                    parse_obj_as(
                        type_=typing.List[Tag],
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

    async def create_a_new_tag(
        self,
        *,
        name: str,
        colour: typing.Optional[str] = OMIT,
        tag_set: typing.Optional[TagSet] = OMIT,
        url_words: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Tag]:
        """
        Parameters
        ----------
        name : str

        colour : typing.Optional[str]

        tag_set : typing.Optional[TagSet]

        url_words : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Tag]
            Tag created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tags",
            method="POST",
            json={
                "colour": colour,
                "name": name,
                "tagSet": convert_and_respect_annotation_metadata(
                    object_=tag_set, annotation=TagSet, direction="write"
                ),
                "urlWords": url_words,
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
                    Tag,
                    parse_obj_as(
                        type_=Tag,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def retrieve_a_single_tag_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Tag]:
        """
        Parameters
        ----------
        id : str
            Id of the tag to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Tag]
            The tag
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tags/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tag,
                    parse_obj_as(
                        type_=Tag,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def list_tag_sets(
        self,
        *,
        owned_by: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[TagSet]]:
        """
        Retrieve tag sets.

        Parameters
        ----------
        owned_by : typing.Optional[str]
            Restrict results to those owned by this user.

        url_words : typing.Optional[str]
            Restrict results by urlWords. Should be used with ownedBy when searching for one of your own tag sets.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[TagSet]]
            A list of tag sets
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tagsets",
            method="GET",
            params={
                "ownedBy": owned_by,
                "urlWords": url_words,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TagSet],
                    parse_obj_as(
                        type_=typing.List[TagSet],
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

    async def create_a_new_tag_set(
        self, *, name: str, url_words: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TagSet]:
        """
        Parameters
        ----------
        name : str

        url_words : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TagSet]
            Tagset created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tagsets",
            method="POST",
            json={
                "name": name,
                "urlWords": url_words,
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
                    TagSet,
                    parse_obj_as(
                        type_=TagSet,
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

    async def retrieve_a_single_tag_set_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TagSet]:
        """
        Parameters
        ----------
        id : str
            Id of the tag set to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TagSet]
            The tag set
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tagsets/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TagSet,
                    parse_obj_as(
                        type_=TagSet,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
