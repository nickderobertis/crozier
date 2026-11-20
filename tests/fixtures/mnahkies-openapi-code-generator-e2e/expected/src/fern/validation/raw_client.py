

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.internal_server_error import InternalServerError
from ..types.animal import Animal
from ..types.enumerations import Enumerations
from ..types.enumerations_colors import EnumerationsColors
from ..types.random_number import RandomNumber
from .types.get_responses_default_response import GetResponsesDefaultResponse
from .types.post_validation_optional_body_response import PostValidationOptionalBodyResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawValidationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_validation_numbers_random_number(
        self,
        *,
        max: typing.Optional[float] = None,
        min: typing.Optional[float] = None,
        forbidden: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RandomNumber]:
        """
        Parameters
        ----------
        max : typing.Optional[float]

        min : typing.Optional[float]

        forbidden : typing.Optional[typing.Union[float, typing.Sequence[float]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RandomNumber]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            "validation/numbers/random-number",
            method="GET",
            params={
                "max": max,
                "min": min,
                "forbidden": forbidden,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RandomNumber,
                    parse_obj_as(
                        type_=RandomNumber,
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

    def post_validation_enums(
        self,
        *,
        colors: EnumerationsColors,
        star_ratings: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Enumerations]:
        """
        Parameters
        ----------
        colors : EnumerationsColors

        star_ratings : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Enumerations]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "validation/enums",
            method="POST",
            json={
                "colors": colors,
                "starRatings": star_ratings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Enumerations,
                    parse_obj_as(
                        type_=Enumerations,
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

    def post_validation_optional_body(
        self, *, id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[PostValidationOptionalBodyResponse]]:
        """
        Parameters
        ----------
        id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[PostValidationOptionalBodyResponse]]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "validation/optional-body",
            method="POST",
            json={
                "id": id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[PostValidationOptionalBodyResponse],
                    parse_obj_as(
                        type_=typing.Optional[PostValidationOptionalBodyResponse],
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

    def post_validation_objects_discriminated_union(
        self, *, request: Animal, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Animal]:
        """
        Parameters
        ----------
        request : Animal

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Animal]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "validation/objects/discriminated-union",
            method="POST",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Animal, direction="write"),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Animal,
                    parse_obj_as(
                        type_=Animal,
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

    def get_responses500(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "responses/500",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 500:
                raise InternalServerError(
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

    def get_responses_default(
        self, *, status: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetResponsesDefaultResponse]:
        """
        Parameters
        ----------
        status : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetResponsesDefaultResponse]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "responses/default",
            method="GET",
            params={
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetResponsesDefaultResponse,
                    parse_obj_as(
                        type_=GetResponsesDefaultResponse,
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

    def get_responses_empty(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "responses/empty",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawValidationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_validation_numbers_random_number(
        self,
        *,
        max: typing.Optional[float] = None,
        min: typing.Optional[float] = None,
        forbidden: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RandomNumber]:
        """
        Parameters
        ----------
        max : typing.Optional[float]

        min : typing.Optional[float]

        forbidden : typing.Optional[typing.Union[float, typing.Sequence[float]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RandomNumber]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "validation/numbers/random-number",
            method="GET",
            params={
                "max": max,
                "min": min,
                "forbidden": forbidden,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RandomNumber,
                    parse_obj_as(
                        type_=RandomNumber,
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

    async def post_validation_enums(
        self,
        *,
        colors: EnumerationsColors,
        star_ratings: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Enumerations]:
        """
        Parameters
        ----------
        colors : EnumerationsColors

        star_ratings : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Enumerations]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "validation/enums",
            method="POST",
            json={
                "colors": colors,
                "starRatings": star_ratings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Enumerations,
                    parse_obj_as(
                        type_=Enumerations,
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

    async def post_validation_optional_body(
        self, *, id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[PostValidationOptionalBodyResponse]]:
        """
        Parameters
        ----------
        id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[PostValidationOptionalBodyResponse]]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "validation/optional-body",
            method="POST",
            json={
                "id": id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[PostValidationOptionalBodyResponse],
                    parse_obj_as(
                        type_=typing.Optional[PostValidationOptionalBodyResponse],
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

    async def post_validation_objects_discriminated_union(
        self, *, request: Animal, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Animal]:
        """
        Parameters
        ----------
        request : Animal

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Animal]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "validation/objects/discriminated-union",
            method="POST",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Animal, direction="write"),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Animal,
                    parse_obj_as(
                        type_=Animal,
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

    async def get_responses500(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "responses/500",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def get_responses_default(
        self, *, status: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetResponsesDefaultResponse]:
        """
        Parameters
        ----------
        status : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetResponsesDefaultResponse]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "responses/default",
            method="GET",
            params={
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetResponsesDefaultResponse,
                    parse_obj_as(
                        type_=GetResponsesDefaultResponse,
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

    async def get_responses_empty(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "responses/empty",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
