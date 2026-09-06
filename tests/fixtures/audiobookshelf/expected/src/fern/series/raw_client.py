

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.not_found_error import NotFoundError
from ..types.series import Series
from ..types.series_description import SeriesDescription
from ..types.series_id import SeriesId
from ..types.series_name import SeriesName
from ..types.series_with_progress_and_rss import SeriesWithProgressAndRss
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSeriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_series(
        self, id: SeriesId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SeriesWithProgressAndRss]:
        """
        Get a series by ID.

        Parameters
        ----------
        id : SeriesId
            The ID of the series.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SeriesWithProgressAndRss]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/series/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeriesWithProgressAndRss,
                    parse_obj_as(
                        type_=SeriesWithProgressAndRss,
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

    def update_series(
        self,
        id: SeriesId,
        *,
        name: typing.Optional[SeriesName] = OMIT,
        description: typing.Optional[SeriesDescription] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Series]:
        """
        Update a series by ID.

        Parameters
        ----------
        id : SeriesId
            The ID of the series.

        name : typing.Optional[SeriesName]

        description : typing.Optional[SeriesDescription]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Series]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/series/{encode_path_param(id)}",
            method="PATCH",
            json={
                "name": name,
                "description": description,
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
                    Series,
                    parse_obj_as(
                        type_=Series,
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


class AsyncRawSeriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_series(
        self, id: SeriesId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SeriesWithProgressAndRss]:
        """
        Get a series by ID.

        Parameters
        ----------
        id : SeriesId
            The ID of the series.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SeriesWithProgressAndRss]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/series/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeriesWithProgressAndRss,
                    parse_obj_as(
                        type_=SeriesWithProgressAndRss,
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

    async def update_series(
        self,
        id: SeriesId,
        *,
        name: typing.Optional[SeriesName] = OMIT,
        description: typing.Optional[SeriesDescription] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Series]:
        """
        Update a series by ID.

        Parameters
        ----------
        id : SeriesId
            The ID of the series.

        name : typing.Optional[SeriesName]

        description : typing.Optional[SeriesDescription]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Series]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/series/{encode_path_param(id)}",
            method="PATCH",
            json={
                "name": name,
                "description": description,
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
                    Series,
                    parse_obj_as(
                        type_=Series,
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
