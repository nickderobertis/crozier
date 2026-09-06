

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
from ..types.page_series_dto import PageSeriesDto
from ..types.validation_error_response import ValidationErrorResponse
from .types.get_series_by_collection_id_request_read_status_item import GetSeriesByCollectionIdRequestReadStatusItem
from .types.get_series_by_collection_id_request_status_item import GetSeriesByCollectionIdRequestStatusItem
from pydantic import ValidationError


class RawCollectionSeriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_series_by_collection_id(
        self,
        id: str,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        status: typing.Optional[
            typing.Union[
                GetSeriesByCollectionIdRequestStatusItem, typing.Sequence[GetSeriesByCollectionIdRequestStatusItem]
            ]
        ] = None,
        read_status: typing.Optional[
            typing.Union[
                GetSeriesByCollectionIdRequestReadStatusItem,
                typing.Sequence[GetSeriesByCollectionIdRequestReadStatusItem],
            ]
        ] = None,
        publisher: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        language: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        genre: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        age_rating: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        release_year: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        deleted: typing.Optional[bool] = None,
        complete: typing.Optional[bool] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        author: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageSeriesDto]:
        """
        Parameters
        ----------
        id : str

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        status : typing.Optional[typing.Union[GetSeriesByCollectionIdRequestStatusItem, typing.Sequence[GetSeriesByCollectionIdRequestStatusItem]]]

        read_status : typing.Optional[typing.Union[GetSeriesByCollectionIdRequestReadStatusItem, typing.Sequence[GetSeriesByCollectionIdRequestReadStatusItem]]]

        publisher : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        language : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        genre : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        age_rating : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        release_year : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        deleted : typing.Optional[bool]

        complete : typing.Optional[bool]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        author : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Author criteria in the format: name,role. Multiple author criteria are supported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageSeriesDto]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/collections/{encode_path_param(id)}/series",
            method="GET",
            params={
                "library_id": library_id,
                "status": status,
                "read_status": read_status,
                "publisher": publisher,
                "language": language,
                "genre": genre,
                "tag": tag,
                "age_rating": age_rating,
                "release_year": release_year,
                "deleted": deleted,
                "complete": complete,
                "unpaged": unpaged,
                "page": page,
                "size": size,
                "author": author,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageSeriesDto,
                    parse_obj_as(
                        type_=PageSeriesDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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


class AsyncRawCollectionSeriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_series_by_collection_id(
        self,
        id: str,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        status: typing.Optional[
            typing.Union[
                GetSeriesByCollectionIdRequestStatusItem, typing.Sequence[GetSeriesByCollectionIdRequestStatusItem]
            ]
        ] = None,
        read_status: typing.Optional[
            typing.Union[
                GetSeriesByCollectionIdRequestReadStatusItem,
                typing.Sequence[GetSeriesByCollectionIdRequestReadStatusItem],
            ]
        ] = None,
        publisher: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        language: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        genre: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        age_rating: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        release_year: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        deleted: typing.Optional[bool] = None,
        complete: typing.Optional[bool] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        author: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageSeriesDto]:
        """
        Parameters
        ----------
        id : str

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        status : typing.Optional[typing.Union[GetSeriesByCollectionIdRequestStatusItem, typing.Sequence[GetSeriesByCollectionIdRequestStatusItem]]]

        read_status : typing.Optional[typing.Union[GetSeriesByCollectionIdRequestReadStatusItem, typing.Sequence[GetSeriesByCollectionIdRequestReadStatusItem]]]

        publisher : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        language : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        genre : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        age_rating : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        release_year : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        deleted : typing.Optional[bool]

        complete : typing.Optional[bool]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        author : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Author criteria in the format: name,role. Multiple author criteria are supported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageSeriesDto]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/collections/{encode_path_param(id)}/series",
            method="GET",
            params={
                "library_id": library_id,
                "status": status,
                "read_status": read_status,
                "publisher": publisher,
                "language": language,
                "genre": genre,
                "tag": tag,
                "age_rating": age_rating,
                "release_year": release_year,
                "deleted": deleted,
                "complete": complete,
                "unpaged": unpaged,
                "page": page,
                "size": size,
                "author": author,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageSeriesDto,
                    parse_obj_as(
                        type_=PageSeriesDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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
