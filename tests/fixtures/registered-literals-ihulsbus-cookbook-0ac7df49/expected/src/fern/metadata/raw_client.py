

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..error.types.error import Error
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.unauthorized_error import UnauthorizedError
from .types.metadata_search_response import MetadataSearchResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMetadataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search_metadata(
        self,
        *,
        recipe_id: typing.Optional[str] = OMIT,
        category_id: typing.Optional[str] = OMIT,
        tag_id: typing.Optional[str] = OMIT,
        difficulty_level_id: typing.Optional[str] = OMIT,
        cuisine_type_id: typing.Optional[str] = OMIT,
        min_prep_time: typing.Optional[int] = OMIT,
        max_prep_time: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MetadataSearchResponse]:
        """
        Search through metadata

        Parameters
        ----------
        recipe_id : typing.Optional[str]
            ID of a recipe to base the search on

        category_id : typing.Optional[str]
            ID of a category to base the search on

        tag_id : typing.Optional[str]
            ID of a tag to base the search on

        difficulty_level_id : typing.Optional[str]
            ID of a difficulty level to base the search on

        cuisine_type_id : typing.Optional[str]
            ID of a cuisine type to base the search on

        min_prep_time : typing.Optional[int]
            minimum preparation time in minutes

        max_prep_time : typing.Optional[int]
            maximum preparation time in minutes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MetadataSearchResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "metadata/search",
            method="POST",
            json={
                "recipe_id": recipe_id,
                "category_id": category_id,
                "tag_id": tag_id,
                "difficulty_level_id": difficulty_level_id,
                "cuisine_type_id": cuisine_type_id,
                "min_prep_time": min_prep_time,
                "max_prep_time": max_prep_time,
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
                    MetadataSearchResponse,
                    parse_obj_as(
                        type_=MetadataSearchResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
                        Error,
                        parse_obj_as(
                            type_=Error,
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


class AsyncRawMetadataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search_metadata(
        self,
        *,
        recipe_id: typing.Optional[str] = OMIT,
        category_id: typing.Optional[str] = OMIT,
        tag_id: typing.Optional[str] = OMIT,
        difficulty_level_id: typing.Optional[str] = OMIT,
        cuisine_type_id: typing.Optional[str] = OMIT,
        min_prep_time: typing.Optional[int] = OMIT,
        max_prep_time: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MetadataSearchResponse]:
        """
        Search through metadata

        Parameters
        ----------
        recipe_id : typing.Optional[str]
            ID of a recipe to base the search on

        category_id : typing.Optional[str]
            ID of a category to base the search on

        tag_id : typing.Optional[str]
            ID of a tag to base the search on

        difficulty_level_id : typing.Optional[str]
            ID of a difficulty level to base the search on

        cuisine_type_id : typing.Optional[str]
            ID of a cuisine type to base the search on

        min_prep_time : typing.Optional[int]
            minimum preparation time in minutes

        max_prep_time : typing.Optional[int]
            maximum preparation time in minutes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MetadataSearchResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "metadata/search",
            method="POST",
            json={
                "recipe_id": recipe_id,
                "category_id": category_id,
                "tag_id": tag_id,
                "difficulty_level_id": difficulty_level_id,
                "cuisine_type_id": cuisine_type_id,
                "min_prep_time": min_prep_time,
                "max_prep_time": max_prep_time,
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
                    MetadataSearchResponse,
                    parse_obj_as(
                        type_=MetadataSearchResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
                        Error,
                        parse_obj_as(
                            type_=Error,
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
