

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawInferredReturnsClient, RawInferredReturnsClient
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


OMIT = typing.cast(typing.Any, ...)


class InferredReturnsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInferredReturnsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInferredReturnsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInferredReturnsClient
        """
        return self._raw_client

    def inferred_returns_enum_like(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsEnumLikeResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsEnumLikeResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_enum_like()
        """
        _response = self._raw_client.inferred_returns_enum_like(request_options=request_options)
        return _response.data

    def inferred_returns_string_literal(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsStringLiteralResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsStringLiteralResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_string_literal()
        """
        _response = self._raw_client.inferred_returns_string_literal(request_options=request_options)
        return _response.data

    def inferred_returns_number_literal(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsNumberLiteralResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsNumberLiteralResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_number_literal()
        """
        _response = self._raw_client.inferred_returns_number_literal(request_options=request_options)
        return _response.data

    def inferred_returns_boolean_literal(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsBooleanLiteralResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsBooleanLiteralResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_boolean_literal()
        """
        _response = self._raw_client.inferred_returns_boolean_literal(request_options=request_options)
        return _response.data

    def inferred_returns_discriminated_result(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsDiscriminatedResultResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsDiscriminatedResultResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_discriminated_result()
        """
        _response = self._raw_client.inferred_returns_discriminated_result(request_options=request_options)
        return _response.data

    def inferred_returns_primitive_union(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsPrimitiveUnionResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsPrimitiveUnionResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_primitive_union()
        """
        _response = self._raw_client.inferred_returns_primitive_union(request_options=request_options)
        return _response.data

    def inferred_returns_tuple_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsTupleReturnResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsTupleReturnResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_tuple_return()
        """
        _response = self._raw_client.inferred_returns_tuple_return(request_options=request_options)
        return _response.data

    def inferred_returns_record_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsRecordReturnResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsRecordReturnResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_record_return()
        """
        _response = self._raw_client.inferred_returns_record_return(request_options=request_options)
        return _response.data

    def inferred_returns_array_of_objects(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsArrayOfObjectsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsArrayOfObjectsResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_array_of_objects()
        """
        _response = self._raw_client.inferred_returns_array_of_objects(request_options=request_options)
        return _response.data

    def inferred_returns_matrix(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsMatrixResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsMatrixResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_matrix()
        """
        _response = self._raw_client.inferred_returns_matrix(request_options=request_options)
        return _response.data

    def inferred_returns_deeply_nested(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsDeeplyNestedResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsDeeplyNestedResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_deeply_nested()
        """
        _response = self._raw_client.inferred_returns_deeply_nested(request_options=request_options)
        return _response.data

    def inferred_returns_date_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsDateReturnResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsDateReturnResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_date_return()
        """
        _response = self._raw_client.inferred_returns_date_return(request_options=request_options)
        return _response.data

    def inferred_returns_bigint_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsBigintReturnResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsBigintReturnResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_bigint_return()
        """
        _response = self._raw_client.inferred_returns_bigint_return(request_options=request_options)
        return _response.data

    def inferred_returns_nullable_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsNullableReturnResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsNullableReturnResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_nullable_return()
        """
        _response = self._raw_client.inferred_returns_nullable_return(request_options=request_options)
        return _response.data

    def inferred_returns_optional_fields(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsOptionalFieldsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsOptionalFieldsResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_optional_fields()
        """
        _response = self._raw_client.inferred_returns_optional_fields(request_options=request_options)
        return _response.data

    def inferred_returns_mixed_object(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsMixedObjectResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsMixedObjectResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_mixed_object()
        """
        _response = self._raw_client.inferred_returns_mixed_object(request_options=request_options)
        return _response.data

    def inferred_returns_void_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsVoidReturnResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsVoidReturnResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_void_return()
        """
        _response = self._raw_client.inferred_returns_void_return(request_options=request_options)
        return _response.data

    def inferred_returns_null_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsNullReturnResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsNullReturnResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_null_return()
        """
        _response = self._raw_client.inferred_returns_null_return(request_options=request_options)
        return _response.data

    def inferred_returns_merged_object(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsMergedObjectResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsMergedObjectResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_merged_object()
        """
        _response = self._raw_client.inferred_returns_merged_object(request_options=request_options)
        return _response.data

    def inferred_returns_literal_array(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsLiteralArrayResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsLiteralArrayResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_literal_array()
        """
        _response = self._raw_client.inferred_returns_literal_array(request_options=request_options)
        return _response.data

    def inferred_returns_nested_nullable(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsNestedNullableResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsNestedNullableResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_nested_nullable()
        """
        _response = self._raw_client.inferred_returns_nested_nullable(request_options=request_options)
        return _response.data

    def inferred_returns_bool_return_false(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsBoolReturnFalseResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsBoolReturnFalseResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_bool_return_false()
        """
        _response = self._raw_client.inferred_returns_bool_return_false(request_options=request_options)
        return _response.data

    def inferred_returns_bool_return_true(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsBoolReturnTrueResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsBoolReturnTrueResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_bool_return_true()
        """
        _response = self._raw_client.inferred_returns_bool_return_true(request_options=request_options)
        return _response.data

    def inferred_returns_bool_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsBoolReturnResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsBoolReturnResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_bool_return()
        """
        _response = self._raw_client.inferred_returns_bool_return(request_options=request_options)
        return _response.data

    def inferred_returns_num_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsNumReturnResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsNumReturnResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_num_return()
        """
        _response = self._raw_client.inferred_returns_num_return(request_options=request_options)
        return _response.data

    def inferred_returns_str_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsStrReturnResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsStrReturnResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_str_return()
        """
        _response = self._raw_client.inferred_returns_str_return(request_options=request_options)
        return _response.data

    def inferred_returns_create_item(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsCreateItemResponse:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsCreateItemResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_create_item(
            name="name",
        )
        """
        _response = self._raw_client.inferred_returns_create_item(name=name, request_options=request_options)
        return _response.data

    def inferred_returns_string_enum(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsStringEnumResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsStringEnumResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_string_enum()
        """
        _response = self._raw_client.inferred_returns_string_enum(request_options=request_options)
        return _response.data

    def inferred_returns_numeric_enum(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsNumericEnumResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsNumericEnumResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_numeric_enum()
        """
        _response = self._raw_client.inferred_returns_numeric_enum(request_options=request_options)
        return _response.data

    def inferred_returns_mixed_enum(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsMixedEnumResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsMixedEnumResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_mixed_enum()
        """
        _response = self._raw_client.inferred_returns_mixed_enum(request_options=request_options)
        return _response.data

    def inferred_returns_branded_returns(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsBrandedReturnsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsBrandedReturnsResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inferred_returns.inferred_returns_branded_returns()
        """
        _response = self._raw_client.inferred_returns_branded_returns(request_options=request_options)
        return _response.data


class AsyncInferredReturnsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInferredReturnsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInferredReturnsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInferredReturnsClient
        """
        return self._raw_client

    async def inferred_returns_enum_like(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsEnumLikeResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsEnumLikeResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_enum_like()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_enum_like(request_options=request_options)
        return _response.data

    async def inferred_returns_string_literal(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsStringLiteralResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsStringLiteralResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_string_literal()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_string_literal(request_options=request_options)
        return _response.data

    async def inferred_returns_number_literal(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsNumberLiteralResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsNumberLiteralResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_number_literal()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_number_literal(request_options=request_options)
        return _response.data

    async def inferred_returns_boolean_literal(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsBooleanLiteralResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsBooleanLiteralResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_boolean_literal()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_boolean_literal(request_options=request_options)
        return _response.data

    async def inferred_returns_discriminated_result(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsDiscriminatedResultResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsDiscriminatedResultResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_discriminated_result()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_discriminated_result(request_options=request_options)
        return _response.data

    async def inferred_returns_primitive_union(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsPrimitiveUnionResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsPrimitiveUnionResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_primitive_union()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_primitive_union(request_options=request_options)
        return _response.data

    async def inferred_returns_tuple_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsTupleReturnResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsTupleReturnResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_tuple_return()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_tuple_return(request_options=request_options)
        return _response.data

    async def inferred_returns_record_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsRecordReturnResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsRecordReturnResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_record_return()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_record_return(request_options=request_options)
        return _response.data

    async def inferred_returns_array_of_objects(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsArrayOfObjectsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsArrayOfObjectsResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_array_of_objects()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_array_of_objects(request_options=request_options)
        return _response.data

    async def inferred_returns_matrix(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsMatrixResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsMatrixResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_matrix()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_matrix(request_options=request_options)
        return _response.data

    async def inferred_returns_deeply_nested(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsDeeplyNestedResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsDeeplyNestedResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_deeply_nested()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_deeply_nested(request_options=request_options)
        return _response.data

    async def inferred_returns_date_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsDateReturnResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsDateReturnResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_date_return()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_date_return(request_options=request_options)
        return _response.data

    async def inferred_returns_bigint_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsBigintReturnResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsBigintReturnResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_bigint_return()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_bigint_return(request_options=request_options)
        return _response.data

    async def inferred_returns_nullable_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsNullableReturnResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsNullableReturnResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_nullable_return()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_nullable_return(request_options=request_options)
        return _response.data

    async def inferred_returns_optional_fields(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsOptionalFieldsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsOptionalFieldsResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_optional_fields()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_optional_fields(request_options=request_options)
        return _response.data

    async def inferred_returns_mixed_object(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsMixedObjectResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsMixedObjectResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_mixed_object()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_mixed_object(request_options=request_options)
        return _response.data

    async def inferred_returns_void_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsVoidReturnResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsVoidReturnResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_void_return()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_void_return(request_options=request_options)
        return _response.data

    async def inferred_returns_null_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsNullReturnResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsNullReturnResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_null_return()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_null_return(request_options=request_options)
        return _response.data

    async def inferred_returns_merged_object(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsMergedObjectResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsMergedObjectResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_merged_object()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_merged_object(request_options=request_options)
        return _response.data

    async def inferred_returns_literal_array(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsLiteralArrayResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsLiteralArrayResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_literal_array()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_literal_array(request_options=request_options)
        return _response.data

    async def inferred_returns_nested_nullable(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsNestedNullableResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsNestedNullableResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_nested_nullable()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_nested_nullable(request_options=request_options)
        return _response.data

    async def inferred_returns_bool_return_false(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsBoolReturnFalseResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsBoolReturnFalseResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_bool_return_false()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_bool_return_false(request_options=request_options)
        return _response.data

    async def inferred_returns_bool_return_true(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsBoolReturnTrueResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsBoolReturnTrueResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_bool_return_true()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_bool_return_true(request_options=request_options)
        return _response.data

    async def inferred_returns_bool_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsBoolReturnResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsBoolReturnResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_bool_return()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_bool_return(request_options=request_options)
        return _response.data

    async def inferred_returns_num_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsNumReturnResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsNumReturnResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_num_return()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_num_return(request_options=request_options)
        return _response.data

    async def inferred_returns_str_return(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsStrReturnResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsStrReturnResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_str_return()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_str_return(request_options=request_options)
        return _response.data

    async def inferred_returns_create_item(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsCreateItemResponse:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsCreateItemResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_create_item(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_create_item(name=name, request_options=request_options)
        return _response.data

    async def inferred_returns_string_enum(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsStringEnumResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsStringEnumResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_string_enum()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_string_enum(request_options=request_options)
        return _response.data

    async def inferred_returns_numeric_enum(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsNumericEnumResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsNumericEnumResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_numeric_enum()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_numeric_enum(request_options=request_options)
        return _response.data

    async def inferred_returns_mixed_enum(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsMixedEnumResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsMixedEnumResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_mixed_enum()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_mixed_enum(request_options=request_options)
        return _response.data

    async def inferred_returns_branded_returns(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InferredReturnsBrandedReturnsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferredReturnsBrandedReturnsResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inferred_returns.inferred_returns_branded_returns()


        asyncio.run(main())
        """
        _response = await self._raw_client.inferred_returns_branded_returns(request_options=request_options)
        return _response.data
