

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.inferred_returns_array_of_objects_response import InferredReturnsArrayOfObjectsResponse
from .types.inferred_returns_bigint_return_response import InferredReturnsBigintReturnResponse
from .types.inferred_returns_bool_return_false_response import InferredReturnsBoolReturnFalseResponse
from .types.inferred_returns_bool_return_response import InferredReturnsBoolReturnResponse
from .types.inferred_returns_bool_return_true_response import InferredReturnsBoolReturnTrueResponse
from .types.inferred_returns_boolean_literal_response import InferredReturnsBooleanLiteralResponse
from .types.inferred_returns_branded_returns_response import InferredReturnsBrandedReturnsResponse
from .types.inferred_returns_create_item_response import InferredReturnsCreateItemResponse
from .types.inferred_returns_date_return_response import InferredReturnsDateReturnResponse
from .types.inferred_returns_deeply_nested_response import InferredReturnsDeeplyNestedResponse
from .types.inferred_returns_discriminated_result_response import InferredReturnsDiscriminatedResultResponse
from .types.inferred_returns_enum_like_response import InferredReturnsEnumLikeResponse
from .types.inferred_returns_literal_array_response import InferredReturnsLiteralArrayResponse
from .types.inferred_returns_matrix_response import InferredReturnsMatrixResponse
from .types.inferred_returns_merged_object_response import InferredReturnsMergedObjectResponse
from .types.inferred_returns_mixed_enum_response import InferredReturnsMixedEnumResponse
from .types.inferred_returns_mixed_object_response import InferredReturnsMixedObjectResponse
from .types.inferred_returns_nested_nullable_response import InferredReturnsNestedNullableResponse
from .types.inferred_returns_null_return_response import InferredReturnsNullReturnResponse
from .types.inferred_returns_nullable_return_response import InferredReturnsNullableReturnResponse
from .types.inferred_returns_num_return_response import InferredReturnsNumReturnResponse
from .types.inferred_returns_number_literal_response import InferredReturnsNumberLiteralResponse
from .types.inferred_returns_numeric_enum_response import InferredReturnsNumericEnumResponse
from .types.inferred_returns_optional_fields_response import InferredReturnsOptionalFieldsResponse
from .types.inferred_returns_primitive_union_response import InferredReturnsPrimitiveUnionResponse
from .types.inferred_returns_record_return_response import InferredReturnsRecordReturnResponse
from .types.inferred_returns_str_return_response import InferredReturnsStrReturnResponse
from .types.inferred_returns_string_enum_response import InferredReturnsStringEnumResponse
from .types.inferred_returns_string_literal_response import InferredReturnsStringLiteralResponse
from .types.inferred_returns_tuple_return_response import InferredReturnsTupleReturnResponse
from .types.inferred_returns_void_return_response import InferredReturnsVoidReturnResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawInferredReturnsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def inferred_returns_enum_like(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsEnumLikeResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsEnumLikeResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.enumLike",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsEnumLikeResponse,
                    parse_obj_as(
                        type_=InferredReturnsEnumLikeResponse,
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

    def inferred_returns_string_literal(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsStringLiteralResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsStringLiteralResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.stringLiteral",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsStringLiteralResponse,
                    parse_obj_as(
                        type_=InferredReturnsStringLiteralResponse,
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

    def inferred_returns_number_literal(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsNumberLiteralResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsNumberLiteralResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.numberLiteral",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsNumberLiteralResponse,
                    parse_obj_as(
                        type_=InferredReturnsNumberLiteralResponse,
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

    def inferred_returns_boolean_literal(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsBooleanLiteralResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsBooleanLiteralResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.booleanLiteral",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsBooleanLiteralResponse,
                    parse_obj_as(
                        type_=InferredReturnsBooleanLiteralResponse,
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

    def inferred_returns_discriminated_result(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsDiscriminatedResultResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsDiscriminatedResultResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.discriminatedResult",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsDiscriminatedResultResponse,
                    parse_obj_as(
                        type_=InferredReturnsDiscriminatedResultResponse,
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

    def inferred_returns_primitive_union(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsPrimitiveUnionResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsPrimitiveUnionResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.primitiveUnion",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsPrimitiveUnionResponse,
                    parse_obj_as(
                        type_=InferredReturnsPrimitiveUnionResponse,
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

    def inferred_returns_tuple_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsTupleReturnResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsTupleReturnResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.tupleReturn",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsTupleReturnResponse,
                    parse_obj_as(
                        type_=InferredReturnsTupleReturnResponse,
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

    def inferred_returns_record_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsRecordReturnResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsRecordReturnResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.recordReturn",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsRecordReturnResponse,
                    parse_obj_as(
                        type_=InferredReturnsRecordReturnResponse,
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

    def inferred_returns_array_of_objects(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsArrayOfObjectsResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsArrayOfObjectsResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.arrayOfObjects",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsArrayOfObjectsResponse,
                    parse_obj_as(
                        type_=InferredReturnsArrayOfObjectsResponse,
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

    def inferred_returns_matrix(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsMatrixResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsMatrixResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.matrix",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsMatrixResponse,
                    parse_obj_as(
                        type_=InferredReturnsMatrixResponse,
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

    def inferred_returns_deeply_nested(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsDeeplyNestedResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsDeeplyNestedResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.deeplyNested",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsDeeplyNestedResponse,
                    parse_obj_as(
                        type_=InferredReturnsDeeplyNestedResponse,
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

    def inferred_returns_date_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsDateReturnResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsDateReturnResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.dateReturn",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsDateReturnResponse,
                    parse_obj_as(
                        type_=InferredReturnsDateReturnResponse,
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

    def inferred_returns_bigint_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsBigintReturnResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsBigintReturnResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.bigintReturn",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsBigintReturnResponse,
                    parse_obj_as(
                        type_=InferredReturnsBigintReturnResponse,
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

    def inferred_returns_nullable_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsNullableReturnResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsNullableReturnResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.nullableReturn",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsNullableReturnResponse,
                    parse_obj_as(
                        type_=InferredReturnsNullableReturnResponse,
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

    def inferred_returns_optional_fields(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsOptionalFieldsResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsOptionalFieldsResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.optionalFields",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsOptionalFieldsResponse,
                    parse_obj_as(
                        type_=InferredReturnsOptionalFieldsResponse,
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

    def inferred_returns_mixed_object(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsMixedObjectResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsMixedObjectResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.mixedObject",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsMixedObjectResponse,
                    parse_obj_as(
                        type_=InferredReturnsMixedObjectResponse,
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

    def inferred_returns_void_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsVoidReturnResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsVoidReturnResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.voidReturn",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsVoidReturnResponse,
                    parse_obj_as(
                        type_=InferredReturnsVoidReturnResponse,
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

    def inferred_returns_null_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsNullReturnResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsNullReturnResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.nullReturn",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsNullReturnResponse,
                    parse_obj_as(
                        type_=InferredReturnsNullReturnResponse,
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

    def inferred_returns_merged_object(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsMergedObjectResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsMergedObjectResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.mergedObject",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsMergedObjectResponse,
                    parse_obj_as(
                        type_=InferredReturnsMergedObjectResponse,
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

    def inferred_returns_literal_array(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsLiteralArrayResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsLiteralArrayResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.literalArray",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsLiteralArrayResponse,
                    parse_obj_as(
                        type_=InferredReturnsLiteralArrayResponse,
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

    def inferred_returns_nested_nullable(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsNestedNullableResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsNestedNullableResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.nestedNullable",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsNestedNullableResponse,
                    parse_obj_as(
                        type_=InferredReturnsNestedNullableResponse,
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

    def inferred_returns_bool_return_false(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsBoolReturnFalseResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsBoolReturnFalseResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.boolReturnFalse",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsBoolReturnFalseResponse,
                    parse_obj_as(
                        type_=InferredReturnsBoolReturnFalseResponse,
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

    def inferred_returns_bool_return_true(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsBoolReturnTrueResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsBoolReturnTrueResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.boolReturnTrue",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsBoolReturnTrueResponse,
                    parse_obj_as(
                        type_=InferredReturnsBoolReturnTrueResponse,
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

    def inferred_returns_bool_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsBoolReturnResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsBoolReturnResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.boolReturn",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsBoolReturnResponse,
                    parse_obj_as(
                        type_=InferredReturnsBoolReturnResponse,
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

    def inferred_returns_num_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsNumReturnResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsNumReturnResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.numReturn",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsNumReturnResponse,
                    parse_obj_as(
                        type_=InferredReturnsNumReturnResponse,
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

    def inferred_returns_str_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsStrReturnResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsStrReturnResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.strReturn",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsStrReturnResponse,
                    parse_obj_as(
                        type_=InferredReturnsStrReturnResponse,
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

    def inferred_returns_create_item(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsCreateItemResponse]:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsCreateItemResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.createItem",
            method="POST",
            json={
                "name": name,
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
                    InferredReturnsCreateItemResponse,
                    parse_obj_as(
                        type_=InferredReturnsCreateItemResponse,
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

    def inferred_returns_string_enum(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsStringEnumResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsStringEnumResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.stringEnum",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsStringEnumResponse,
                    parse_obj_as(
                        type_=InferredReturnsStringEnumResponse,
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

    def inferred_returns_numeric_enum(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsNumericEnumResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsNumericEnumResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.numericEnum",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsNumericEnumResponse,
                    parse_obj_as(
                        type_=InferredReturnsNumericEnumResponse,
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

    def inferred_returns_mixed_enum(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsMixedEnumResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsMixedEnumResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.mixedEnum",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsMixedEnumResponse,
                    parse_obj_as(
                        type_=InferredReturnsMixedEnumResponse,
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

    def inferred_returns_branded_returns(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InferredReturnsBrandedReturnsResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InferredReturnsBrandedReturnsResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "inferredReturns.brandedReturns",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsBrandedReturnsResponse,
                    parse_obj_as(
                        type_=InferredReturnsBrandedReturnsResponse,
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


class AsyncRawInferredReturnsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def inferred_returns_enum_like(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsEnumLikeResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsEnumLikeResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.enumLike",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsEnumLikeResponse,
                    parse_obj_as(
                        type_=InferredReturnsEnumLikeResponse,
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

    async def inferred_returns_string_literal(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsStringLiteralResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsStringLiteralResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.stringLiteral",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsStringLiteralResponse,
                    parse_obj_as(
                        type_=InferredReturnsStringLiteralResponse,
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

    async def inferred_returns_number_literal(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsNumberLiteralResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsNumberLiteralResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.numberLiteral",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsNumberLiteralResponse,
                    parse_obj_as(
                        type_=InferredReturnsNumberLiteralResponse,
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

    async def inferred_returns_boolean_literal(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsBooleanLiteralResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsBooleanLiteralResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.booleanLiteral",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsBooleanLiteralResponse,
                    parse_obj_as(
                        type_=InferredReturnsBooleanLiteralResponse,
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

    async def inferred_returns_discriminated_result(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsDiscriminatedResultResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsDiscriminatedResultResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.discriminatedResult",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsDiscriminatedResultResponse,
                    parse_obj_as(
                        type_=InferredReturnsDiscriminatedResultResponse,
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

    async def inferred_returns_primitive_union(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsPrimitiveUnionResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsPrimitiveUnionResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.primitiveUnion",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsPrimitiveUnionResponse,
                    parse_obj_as(
                        type_=InferredReturnsPrimitiveUnionResponse,
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

    async def inferred_returns_tuple_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsTupleReturnResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsTupleReturnResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.tupleReturn",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsTupleReturnResponse,
                    parse_obj_as(
                        type_=InferredReturnsTupleReturnResponse,
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

    async def inferred_returns_record_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsRecordReturnResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsRecordReturnResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.recordReturn",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsRecordReturnResponse,
                    parse_obj_as(
                        type_=InferredReturnsRecordReturnResponse,
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

    async def inferred_returns_array_of_objects(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsArrayOfObjectsResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsArrayOfObjectsResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.arrayOfObjects",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsArrayOfObjectsResponse,
                    parse_obj_as(
                        type_=InferredReturnsArrayOfObjectsResponse,
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

    async def inferred_returns_matrix(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsMatrixResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsMatrixResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.matrix",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsMatrixResponse,
                    parse_obj_as(
                        type_=InferredReturnsMatrixResponse,
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

    async def inferred_returns_deeply_nested(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsDeeplyNestedResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsDeeplyNestedResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.deeplyNested",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsDeeplyNestedResponse,
                    parse_obj_as(
                        type_=InferredReturnsDeeplyNestedResponse,
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

    async def inferred_returns_date_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsDateReturnResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsDateReturnResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.dateReturn",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsDateReturnResponse,
                    parse_obj_as(
                        type_=InferredReturnsDateReturnResponse,
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

    async def inferred_returns_bigint_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsBigintReturnResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsBigintReturnResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.bigintReturn",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsBigintReturnResponse,
                    parse_obj_as(
                        type_=InferredReturnsBigintReturnResponse,
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

    async def inferred_returns_nullable_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsNullableReturnResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsNullableReturnResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.nullableReturn",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsNullableReturnResponse,
                    parse_obj_as(
                        type_=InferredReturnsNullableReturnResponse,
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

    async def inferred_returns_optional_fields(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsOptionalFieldsResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsOptionalFieldsResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.optionalFields",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsOptionalFieldsResponse,
                    parse_obj_as(
                        type_=InferredReturnsOptionalFieldsResponse,
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

    async def inferred_returns_mixed_object(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsMixedObjectResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsMixedObjectResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.mixedObject",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsMixedObjectResponse,
                    parse_obj_as(
                        type_=InferredReturnsMixedObjectResponse,
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

    async def inferred_returns_void_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsVoidReturnResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsVoidReturnResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.voidReturn",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsVoidReturnResponse,
                    parse_obj_as(
                        type_=InferredReturnsVoidReturnResponse,
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

    async def inferred_returns_null_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsNullReturnResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsNullReturnResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.nullReturn",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsNullReturnResponse,
                    parse_obj_as(
                        type_=InferredReturnsNullReturnResponse,
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

    async def inferred_returns_merged_object(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsMergedObjectResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsMergedObjectResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.mergedObject",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsMergedObjectResponse,
                    parse_obj_as(
                        type_=InferredReturnsMergedObjectResponse,
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

    async def inferred_returns_literal_array(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsLiteralArrayResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsLiteralArrayResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.literalArray",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsLiteralArrayResponse,
                    parse_obj_as(
                        type_=InferredReturnsLiteralArrayResponse,
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

    async def inferred_returns_nested_nullable(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsNestedNullableResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsNestedNullableResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.nestedNullable",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsNestedNullableResponse,
                    parse_obj_as(
                        type_=InferredReturnsNestedNullableResponse,
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

    async def inferred_returns_bool_return_false(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsBoolReturnFalseResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsBoolReturnFalseResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.boolReturnFalse",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsBoolReturnFalseResponse,
                    parse_obj_as(
                        type_=InferredReturnsBoolReturnFalseResponse,
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

    async def inferred_returns_bool_return_true(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsBoolReturnTrueResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsBoolReturnTrueResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.boolReturnTrue",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsBoolReturnTrueResponse,
                    parse_obj_as(
                        type_=InferredReturnsBoolReturnTrueResponse,
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

    async def inferred_returns_bool_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsBoolReturnResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsBoolReturnResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.boolReturn",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsBoolReturnResponse,
                    parse_obj_as(
                        type_=InferredReturnsBoolReturnResponse,
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

    async def inferred_returns_num_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsNumReturnResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsNumReturnResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.numReturn",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsNumReturnResponse,
                    parse_obj_as(
                        type_=InferredReturnsNumReturnResponse,
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

    async def inferred_returns_str_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsStrReturnResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsStrReturnResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.strReturn",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsStrReturnResponse,
                    parse_obj_as(
                        type_=InferredReturnsStrReturnResponse,
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

    async def inferred_returns_create_item(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsCreateItemResponse]:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsCreateItemResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.createItem",
            method="POST",
            json={
                "name": name,
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
                    InferredReturnsCreateItemResponse,
                    parse_obj_as(
                        type_=InferredReturnsCreateItemResponse,
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

    async def inferred_returns_string_enum(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsStringEnumResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsStringEnumResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.stringEnum",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsStringEnumResponse,
                    parse_obj_as(
                        type_=InferredReturnsStringEnumResponse,
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

    async def inferred_returns_numeric_enum(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsNumericEnumResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsNumericEnumResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.numericEnum",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsNumericEnumResponse,
                    parse_obj_as(
                        type_=InferredReturnsNumericEnumResponse,
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

    async def inferred_returns_mixed_enum(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsMixedEnumResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsMixedEnumResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.mixedEnum",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsMixedEnumResponse,
                    parse_obj_as(
                        type_=InferredReturnsMixedEnumResponse,
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

    async def inferred_returns_branded_returns(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InferredReturnsBrandedReturnsResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InferredReturnsBrandedReturnsResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inferredReturns.brandedReturns",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InferredReturnsBrandedReturnsResponse,
                    parse_obj_as(
                        type_=InferredReturnsBrandedReturnsResponse,
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
