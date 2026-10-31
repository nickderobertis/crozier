

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.complex_types_any_and_unknown_response import ComplexTypesAnyAndUnknownResponse
from .types.complex_types_branded_response import ComplexTypesBrandedResponse
from .types.complex_types_complex_arrays_response import ComplexTypesComplexArraysResponse
from .types.complex_types_create_content_response import ComplexTypesCreateContentResponse
from .types.complex_types_date_type_response import ComplexTypesDateTypeResponse
from .types.complex_types_deeply_nested_response import ComplexTypesDeeplyNestedResponse
from .types.complex_types_defaults_response import ComplexTypesDefaultsResponse
from .types.complex_types_discriminated_union_request import ComplexTypesDiscriminatedUnionRequest
from .types.complex_types_discriminated_union_response import ComplexTypesDiscriminatedUnionResponse
from .types.complex_types_intersection_response import ComplexTypesIntersectionResponse
from .types.complex_types_literal_response import ComplexTypesLiteralResponse
from .types.complex_types_literal_union_response import ComplexTypesLiteralUnionResponse
from .types.complex_types_native_enum_response import ComplexTypesNativeEnumResponse
from .types.complex_types_nullable_union_response import ComplexTypesNullableUnionResponse
from .types.complex_types_passthrough_response import ComplexTypesPassthroughResponse
from .types.complex_types_piped_response import ComplexTypesPipedResponse
from .types.complex_types_record_response import ComplexTypesRecordResponse
from .types.complex_types_refined_response import ComplexTypesRefinedResponse
from .types.complex_types_search_response import ComplexTypesSearchResponse
from .types.complex_types_strict_response import ComplexTypesStrictResponse
from .types.complex_types_tuple_response import ComplexTypesTupleResponse
from .types.complex_types_union_response import ComplexTypesUnionResponse
from .types.complex_types_with_catch_response import ComplexTypesWithCatchResponse
from .types.complex_types_zod_enum_response import ComplexTypesZodEnumResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawComplexTypesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def complex_types_zod_enum(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ComplexTypesZodEnumResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ComplexTypesZodEnumResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "complexTypes.zodEnum",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesZodEnumResponse,
                    parse_obj_as(
                        type_=ComplexTypesZodEnumResponse,
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

    def complex_types_native_enum(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ComplexTypesNativeEnumResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ComplexTypesNativeEnumResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "complexTypes.nativeEnum",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesNativeEnumResponse,
                    parse_obj_as(
                        type_=ComplexTypesNativeEnumResponse,
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

    def complex_types_literal(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ComplexTypesLiteralResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ComplexTypesLiteralResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "complexTypes.literal",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesLiteralResponse,
                    parse_obj_as(
                        type_=ComplexTypesLiteralResponse,
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

    def complex_types_literal_union(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ComplexTypesLiteralUnionResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ComplexTypesLiteralUnionResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "complexTypes.literalUnion",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesLiteralUnionResponse,
                    parse_obj_as(
                        type_=ComplexTypesLiteralUnionResponse,
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

    def complex_types_discriminated_union(
        self, *, request: ComplexTypesDiscriminatedUnionRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ComplexTypesDiscriminatedUnionResponse]:
        """
        Parameters
        ----------
        request : ComplexTypesDiscriminatedUnionRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ComplexTypesDiscriminatedUnionResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "complexTypes.discriminatedUnion",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=ComplexTypesDiscriminatedUnionRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesDiscriminatedUnionResponse,
                    parse_obj_as(
                        type_=ComplexTypesDiscriminatedUnionResponse,
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

    def complex_types_union(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ComplexTypesUnionResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ComplexTypesUnionResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "complexTypes.union",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesUnionResponse,
                    parse_obj_as(
                        type_=ComplexTypesUnionResponse,
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

    def complex_types_intersection(
        self, *, id: float, name: str, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ComplexTypesIntersectionResponse]:
        """
        Parameters
        ----------
        id : float

        name : str

        email : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ComplexTypesIntersectionResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "complexTypes.intersection",
            method="POST",
            json={
                "id": id,
                "name": name,
                "email": email,
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
                    ComplexTypesIntersectionResponse,
                    parse_obj_as(
                        type_=ComplexTypesIntersectionResponse,
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

    def complex_types_tuple(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ComplexTypesTupleResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ComplexTypesTupleResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "complexTypes.tuple",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesTupleResponse,
                    parse_obj_as(
                        type_=ComplexTypesTupleResponse,
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

    def complex_types_record(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ComplexTypesRecordResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ComplexTypesRecordResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "complexTypes.record",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesRecordResponse,
                    parse_obj_as(
                        type_=ComplexTypesRecordResponse,
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

    def complex_types_complex_arrays(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ComplexTypesComplexArraysResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ComplexTypesComplexArraysResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "complexTypes.complexArrays",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesComplexArraysResponse,
                    parse_obj_as(
                        type_=ComplexTypesComplexArraysResponse,
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

    def complex_types_deeply_nested(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ComplexTypesDeeplyNestedResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ComplexTypesDeeplyNestedResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "complexTypes.deeplyNested",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesDeeplyNestedResponse,
                    parse_obj_as(
                        type_=ComplexTypesDeeplyNestedResponse,
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

    def complex_types_date_type(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ComplexTypesDateTypeResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ComplexTypesDateTypeResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "complexTypes.dateType",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesDateTypeResponse,
                    parse_obj_as(
                        type_=ComplexTypesDateTypeResponse,
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

    def complex_types_any_and_unknown(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ComplexTypesAnyAndUnknownResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ComplexTypesAnyAndUnknownResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "complexTypes.anyAndUnknown",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesAnyAndUnknownResponse,
                    parse_obj_as(
                        type_=ComplexTypesAnyAndUnknownResponse,
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

    def complex_types_defaults(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ComplexTypesDefaultsResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ComplexTypesDefaultsResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "complexTypes.defaults",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesDefaultsResponse,
                    parse_obj_as(
                        type_=ComplexTypesDefaultsResponse,
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

    def complex_types_refined(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ComplexTypesRefinedResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ComplexTypesRefinedResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "complexTypes.refined",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesRefinedResponse,
                    parse_obj_as(
                        type_=ComplexTypesRefinedResponse,
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

    def complex_types_nullable_union(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ComplexTypesNullableUnionResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ComplexTypesNullableUnionResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "complexTypes.nullableUnion",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesNullableUnionResponse,
                    parse_obj_as(
                        type_=ComplexTypesNullableUnionResponse,
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

    def complex_types_passthrough(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ComplexTypesPassthroughResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ComplexTypesPassthroughResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "complexTypes.passthrough",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesPassthroughResponse,
                    parse_obj_as(
                        type_=ComplexTypesPassthroughResponse,
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

    def complex_types_strict(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ComplexTypesStrictResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ComplexTypesStrictResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "complexTypes.strict",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesStrictResponse,
                    parse_obj_as(
                        type_=ComplexTypesStrictResponse,
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

    def complex_types_branded(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ComplexTypesBrandedResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ComplexTypesBrandedResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "complexTypes.branded",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesBrandedResponse,
                    parse_obj_as(
                        type_=ComplexTypesBrandedResponse,
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

    def complex_types_with_catch(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ComplexTypesWithCatchResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ComplexTypesWithCatchResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "complexTypes.withCatch",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesWithCatchResponse,
                    parse_obj_as(
                        type_=ComplexTypesWithCatchResponse,
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

    def complex_types_piped(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ComplexTypesPipedResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ComplexTypesPipedResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "complexTypes.piped",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesPipedResponse,
                    parse_obj_as(
                        type_=ComplexTypesPipedResponse,
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

    def complex_types_create_content(
        self,
        *,
        title: str,
        body: str,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ComplexTypesCreateContentResponse]:
        """
        Parameters
        ----------
        title : str

        body : str

        tags : typing.Optional[typing.Sequence[str]]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ComplexTypesCreateContentResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "complexTypes.createContent",
            method="POST",
            json={
                "title": title,
                "body": body,
                "tags": tags,
                "metadata": metadata,
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
                    ComplexTypesCreateContentResponse,
                    parse_obj_as(
                        type_=ComplexTypesCreateContentResponse,
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

    def complex_types_search(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ComplexTypesSearchResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ComplexTypesSearchResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "complexTypes.search",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesSearchResponse,
                    parse_obj_as(
                        type_=ComplexTypesSearchResponse,
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


class AsyncRawComplexTypesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def complex_types_zod_enum(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ComplexTypesZodEnumResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ComplexTypesZodEnumResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "complexTypes.zodEnum",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesZodEnumResponse,
                    parse_obj_as(
                        type_=ComplexTypesZodEnumResponse,
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

    async def complex_types_native_enum(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ComplexTypesNativeEnumResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ComplexTypesNativeEnumResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "complexTypes.nativeEnum",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesNativeEnumResponse,
                    parse_obj_as(
                        type_=ComplexTypesNativeEnumResponse,
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

    async def complex_types_literal(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ComplexTypesLiteralResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ComplexTypesLiteralResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "complexTypes.literal",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesLiteralResponse,
                    parse_obj_as(
                        type_=ComplexTypesLiteralResponse,
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

    async def complex_types_literal_union(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ComplexTypesLiteralUnionResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ComplexTypesLiteralUnionResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "complexTypes.literalUnion",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesLiteralUnionResponse,
                    parse_obj_as(
                        type_=ComplexTypesLiteralUnionResponse,
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

    async def complex_types_discriminated_union(
        self, *, request: ComplexTypesDiscriminatedUnionRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ComplexTypesDiscriminatedUnionResponse]:
        """
        Parameters
        ----------
        request : ComplexTypesDiscriminatedUnionRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ComplexTypesDiscriminatedUnionResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "complexTypes.discriminatedUnion",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=ComplexTypesDiscriminatedUnionRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesDiscriminatedUnionResponse,
                    parse_obj_as(
                        type_=ComplexTypesDiscriminatedUnionResponse,
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

    async def complex_types_union(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ComplexTypesUnionResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ComplexTypesUnionResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "complexTypes.union",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesUnionResponse,
                    parse_obj_as(
                        type_=ComplexTypesUnionResponse,
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

    async def complex_types_intersection(
        self, *, id: float, name: str, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ComplexTypesIntersectionResponse]:
        """
        Parameters
        ----------
        id : float

        name : str

        email : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ComplexTypesIntersectionResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "complexTypes.intersection",
            method="POST",
            json={
                "id": id,
                "name": name,
                "email": email,
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
                    ComplexTypesIntersectionResponse,
                    parse_obj_as(
                        type_=ComplexTypesIntersectionResponse,
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

    async def complex_types_tuple(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ComplexTypesTupleResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ComplexTypesTupleResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "complexTypes.tuple",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesTupleResponse,
                    parse_obj_as(
                        type_=ComplexTypesTupleResponse,
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

    async def complex_types_record(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ComplexTypesRecordResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ComplexTypesRecordResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "complexTypes.record",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesRecordResponse,
                    parse_obj_as(
                        type_=ComplexTypesRecordResponse,
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

    async def complex_types_complex_arrays(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ComplexTypesComplexArraysResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ComplexTypesComplexArraysResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "complexTypes.complexArrays",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesComplexArraysResponse,
                    parse_obj_as(
                        type_=ComplexTypesComplexArraysResponse,
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

    async def complex_types_deeply_nested(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ComplexTypesDeeplyNestedResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ComplexTypesDeeplyNestedResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "complexTypes.deeplyNested",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesDeeplyNestedResponse,
                    parse_obj_as(
                        type_=ComplexTypesDeeplyNestedResponse,
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

    async def complex_types_date_type(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ComplexTypesDateTypeResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ComplexTypesDateTypeResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "complexTypes.dateType",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesDateTypeResponse,
                    parse_obj_as(
                        type_=ComplexTypesDateTypeResponse,
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

    async def complex_types_any_and_unknown(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ComplexTypesAnyAndUnknownResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ComplexTypesAnyAndUnknownResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "complexTypes.anyAndUnknown",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesAnyAndUnknownResponse,
                    parse_obj_as(
                        type_=ComplexTypesAnyAndUnknownResponse,
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

    async def complex_types_defaults(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ComplexTypesDefaultsResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ComplexTypesDefaultsResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "complexTypes.defaults",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesDefaultsResponse,
                    parse_obj_as(
                        type_=ComplexTypesDefaultsResponse,
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

    async def complex_types_refined(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ComplexTypesRefinedResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ComplexTypesRefinedResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "complexTypes.refined",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesRefinedResponse,
                    parse_obj_as(
                        type_=ComplexTypesRefinedResponse,
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

    async def complex_types_nullable_union(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ComplexTypesNullableUnionResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ComplexTypesNullableUnionResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "complexTypes.nullableUnion",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesNullableUnionResponse,
                    parse_obj_as(
                        type_=ComplexTypesNullableUnionResponse,
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

    async def complex_types_passthrough(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ComplexTypesPassthroughResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ComplexTypesPassthroughResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "complexTypes.passthrough",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesPassthroughResponse,
                    parse_obj_as(
                        type_=ComplexTypesPassthroughResponse,
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

    async def complex_types_strict(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ComplexTypesStrictResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ComplexTypesStrictResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "complexTypes.strict",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesStrictResponse,
                    parse_obj_as(
                        type_=ComplexTypesStrictResponse,
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

    async def complex_types_branded(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ComplexTypesBrandedResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ComplexTypesBrandedResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "complexTypes.branded",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesBrandedResponse,
                    parse_obj_as(
                        type_=ComplexTypesBrandedResponse,
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

    async def complex_types_with_catch(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ComplexTypesWithCatchResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ComplexTypesWithCatchResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "complexTypes.withCatch",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesWithCatchResponse,
                    parse_obj_as(
                        type_=ComplexTypesWithCatchResponse,
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

    async def complex_types_piped(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ComplexTypesPipedResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ComplexTypesPipedResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "complexTypes.piped",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesPipedResponse,
                    parse_obj_as(
                        type_=ComplexTypesPipedResponse,
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

    async def complex_types_create_content(
        self,
        *,
        title: str,
        body: str,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ComplexTypesCreateContentResponse]:
        """
        Parameters
        ----------
        title : str

        body : str

        tags : typing.Optional[typing.Sequence[str]]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ComplexTypesCreateContentResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "complexTypes.createContent",
            method="POST",
            json={
                "title": title,
                "body": body,
                "tags": tags,
                "metadata": metadata,
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
                    ComplexTypesCreateContentResponse,
                    parse_obj_as(
                        type_=ComplexTypesCreateContentResponse,
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

    async def complex_types_search(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ComplexTypesSearchResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ComplexTypesSearchResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "complexTypes.search",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComplexTypesSearchResponse,
                    parse_obj_as(
                        type_=ComplexTypesSearchResponse,
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
