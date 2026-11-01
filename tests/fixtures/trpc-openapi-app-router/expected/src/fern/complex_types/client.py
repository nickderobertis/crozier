

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawComplexTypesClient, RawComplexTypesClient
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


OMIT = typing.cast(typing.Any, ...)


class ComplexTypesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawComplexTypesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawComplexTypesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawComplexTypesClient
        """
        return self._raw_client

    def complex_types_zod_enum(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesZodEnumResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesZodEnumResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.complex_types.complex_types_zod_enum(
            input="input",
        )
        """
        _response = self._raw_client.complex_types_zod_enum(input=input, request_options=request_options)
        return _response.data

    def complex_types_native_enum(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesNativeEnumResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesNativeEnumResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.complex_types.complex_types_native_enum(
            input="input",
        )
        """
        _response = self._raw_client.complex_types_native_enum(input=input, request_options=request_options)
        return _response.data

    def complex_types_literal(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesLiteralResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesLiteralResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.complex_types.complex_types_literal(
            input="input",
        )
        """
        _response = self._raw_client.complex_types_literal(input=input, request_options=request_options)
        return _response.data

    def complex_types_literal_union(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesLiteralUnionResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesLiteralUnionResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.complex_types.complex_types_literal_union(
            input="input",
        )
        """
        _response = self._raw_client.complex_types_literal_union(input=input, request_options=request_options)
        return _response.data

    def complex_types_discriminated_union(
        self, *, request: ComplexTypesDiscriminatedUnionRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesDiscriminatedUnionResponse:
        """
        Parameters
        ----------
        request : ComplexTypesDiscriminatedUnionRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesDiscriminatedUnionResponse
            Successful response

        Examples
        --------
        from fern.complex_types import ComplexTypesDiscriminatedUnionRequest_Text

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.complex_types.complex_types_discriminated_union(
            request=ComplexTypesDiscriminatedUnionRequest_Text(
                content="content",
            ),
        )
        """
        _response = self._raw_client.complex_types_discriminated_union(request=request, request_options=request_options)
        return _response.data

    def complex_types_union(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesUnionResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesUnionResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.complex_types.complex_types_union(
            input="input",
        )
        """
        _response = self._raw_client.complex_types_union(input=input, request_options=request_options)
        return _response.data

    def complex_types_intersection(
        self, *, id: float, name: str, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesIntersectionResponse:
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
        ComplexTypesIntersectionResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.complex_types.complex_types_intersection(
            id=1.1,
            name="name",
            email="email",
        )
        """
        _response = self._raw_client.complex_types_intersection(
            id=id, name=name, email=email, request_options=request_options
        )
        return _response.data

    def complex_types_tuple(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesTupleResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesTupleResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.complex_types.complex_types_tuple(
            input="input",
        )
        """
        _response = self._raw_client.complex_types_tuple(input=input, request_options=request_options)
        return _response.data

    def complex_types_record(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesRecordResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesRecordResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.complex_types.complex_types_record(
            input="input",
        )
        """
        _response = self._raw_client.complex_types_record(input=input, request_options=request_options)
        return _response.data

    def complex_types_complex_arrays(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesComplexArraysResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesComplexArraysResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.complex_types.complex_types_complex_arrays(
            input="input",
        )
        """
        _response = self._raw_client.complex_types_complex_arrays(input=input, request_options=request_options)
        return _response.data

    def complex_types_deeply_nested(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesDeeplyNestedResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesDeeplyNestedResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.complex_types.complex_types_deeply_nested(
            input="input",
        )
        """
        _response = self._raw_client.complex_types_deeply_nested(input=input, request_options=request_options)
        return _response.data

    def complex_types_date_type(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesDateTypeResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesDateTypeResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.complex_types.complex_types_date_type(
            input="input",
        )
        """
        _response = self._raw_client.complex_types_date_type(input=input, request_options=request_options)
        return _response.data

    def complex_types_any_and_unknown(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesAnyAndUnknownResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesAnyAndUnknownResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.complex_types.complex_types_any_and_unknown(
            input="input",
        )
        """
        _response = self._raw_client.complex_types_any_and_unknown(input=input, request_options=request_options)
        return _response.data

    def complex_types_defaults(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesDefaultsResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesDefaultsResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.complex_types.complex_types_defaults(
            input="input",
        )
        """
        _response = self._raw_client.complex_types_defaults(input=input, request_options=request_options)
        return _response.data

    def complex_types_refined(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesRefinedResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesRefinedResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.complex_types.complex_types_refined(
            input="input",
        )
        """
        _response = self._raw_client.complex_types_refined(input=input, request_options=request_options)
        return _response.data

    def complex_types_nullable_union(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesNullableUnionResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesNullableUnionResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.complex_types.complex_types_nullable_union(
            input="input",
        )
        """
        _response = self._raw_client.complex_types_nullable_union(input=input, request_options=request_options)
        return _response.data

    def complex_types_passthrough(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesPassthroughResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesPassthroughResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.complex_types.complex_types_passthrough(
            input="input",
        )
        """
        _response = self._raw_client.complex_types_passthrough(input=input, request_options=request_options)
        return _response.data

    def complex_types_strict(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesStrictResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesStrictResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.complex_types.complex_types_strict(
            input="input",
        )
        """
        _response = self._raw_client.complex_types_strict(input=input, request_options=request_options)
        return _response.data

    def complex_types_branded(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesBrandedResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesBrandedResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.complex_types.complex_types_branded(
            input="input",
        )
        """
        _response = self._raw_client.complex_types_branded(input=input, request_options=request_options)
        return _response.data

    def complex_types_with_catch(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesWithCatchResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesWithCatchResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.complex_types.complex_types_with_catch(
            input="input",
        )
        """
        _response = self._raw_client.complex_types_with_catch(input=input, request_options=request_options)
        return _response.data

    def complex_types_piped(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesPipedResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesPipedResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.complex_types.complex_types_piped(
            input="input",
        )
        """
        _response = self._raw_client.complex_types_piped(input=input, request_options=request_options)
        return _response.data

    def complex_types_create_content(
        self,
        *,
        title: str,
        body: str,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ComplexTypesCreateContentResponse:
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
        ComplexTypesCreateContentResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.complex_types.complex_types_create_content(
            title="title",
            body="body",
        )
        """
        _response = self._raw_client.complex_types_create_content(
            title=title, body=body, tags=tags, metadata=metadata, request_options=request_options
        )
        return _response.data

    def complex_types_search(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesSearchResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesSearchResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.complex_types.complex_types_search(
            input="input",
        )
        """
        _response = self._raw_client.complex_types_search(input=input, request_options=request_options)
        return _response.data


class AsyncComplexTypesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawComplexTypesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawComplexTypesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawComplexTypesClient
        """
        return self._raw_client

    async def complex_types_zod_enum(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesZodEnumResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesZodEnumResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.complex_types.complex_types_zod_enum(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complex_types_zod_enum(input=input, request_options=request_options)
        return _response.data

    async def complex_types_native_enum(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesNativeEnumResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesNativeEnumResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.complex_types.complex_types_native_enum(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complex_types_native_enum(input=input, request_options=request_options)
        return _response.data

    async def complex_types_literal(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesLiteralResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesLiteralResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.complex_types.complex_types_literal(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complex_types_literal(input=input, request_options=request_options)
        return _response.data

    async def complex_types_literal_union(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesLiteralUnionResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesLiteralUnionResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.complex_types.complex_types_literal_union(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complex_types_literal_union(input=input, request_options=request_options)
        return _response.data

    async def complex_types_discriminated_union(
        self, *, request: ComplexTypesDiscriminatedUnionRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesDiscriminatedUnionResponse:
        """
        Parameters
        ----------
        request : ComplexTypesDiscriminatedUnionRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesDiscriminatedUnionResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern.complex_types import ComplexTypesDiscriminatedUnionRequest_Text

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.complex_types.complex_types_discriminated_union(
                request=ComplexTypesDiscriminatedUnionRequest_Text(
                    content="content",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complex_types_discriminated_union(
            request=request, request_options=request_options
        )
        return _response.data

    async def complex_types_union(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesUnionResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesUnionResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.complex_types.complex_types_union(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complex_types_union(input=input, request_options=request_options)
        return _response.data

    async def complex_types_intersection(
        self, *, id: float, name: str, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesIntersectionResponse:
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
        ComplexTypesIntersectionResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.complex_types.complex_types_intersection(
                id=1.1,
                name="name",
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complex_types_intersection(
            id=id, name=name, email=email, request_options=request_options
        )
        return _response.data

    async def complex_types_tuple(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesTupleResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesTupleResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.complex_types.complex_types_tuple(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complex_types_tuple(input=input, request_options=request_options)
        return _response.data

    async def complex_types_record(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesRecordResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesRecordResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.complex_types.complex_types_record(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complex_types_record(input=input, request_options=request_options)
        return _response.data

    async def complex_types_complex_arrays(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesComplexArraysResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesComplexArraysResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.complex_types.complex_types_complex_arrays(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complex_types_complex_arrays(input=input, request_options=request_options)
        return _response.data

    async def complex_types_deeply_nested(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesDeeplyNestedResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesDeeplyNestedResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.complex_types.complex_types_deeply_nested(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complex_types_deeply_nested(input=input, request_options=request_options)
        return _response.data

    async def complex_types_date_type(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesDateTypeResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesDateTypeResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.complex_types.complex_types_date_type(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complex_types_date_type(input=input, request_options=request_options)
        return _response.data

    async def complex_types_any_and_unknown(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesAnyAndUnknownResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesAnyAndUnknownResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.complex_types.complex_types_any_and_unknown(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complex_types_any_and_unknown(input=input, request_options=request_options)
        return _response.data

    async def complex_types_defaults(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesDefaultsResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesDefaultsResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.complex_types.complex_types_defaults(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complex_types_defaults(input=input, request_options=request_options)
        return _response.data

    async def complex_types_refined(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesRefinedResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesRefinedResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.complex_types.complex_types_refined(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complex_types_refined(input=input, request_options=request_options)
        return _response.data

    async def complex_types_nullable_union(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesNullableUnionResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesNullableUnionResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.complex_types.complex_types_nullable_union(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complex_types_nullable_union(input=input, request_options=request_options)
        return _response.data

    async def complex_types_passthrough(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesPassthroughResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesPassthroughResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.complex_types.complex_types_passthrough(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complex_types_passthrough(input=input, request_options=request_options)
        return _response.data

    async def complex_types_strict(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesStrictResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesStrictResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.complex_types.complex_types_strict(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complex_types_strict(input=input, request_options=request_options)
        return _response.data

    async def complex_types_branded(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesBrandedResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesBrandedResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.complex_types.complex_types_branded(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complex_types_branded(input=input, request_options=request_options)
        return _response.data

    async def complex_types_with_catch(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesWithCatchResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesWithCatchResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.complex_types.complex_types_with_catch(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complex_types_with_catch(input=input, request_options=request_options)
        return _response.data

    async def complex_types_piped(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesPipedResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesPipedResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.complex_types.complex_types_piped(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complex_types_piped(input=input, request_options=request_options)
        return _response.data

    async def complex_types_create_content(
        self,
        *,
        title: str,
        body: str,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ComplexTypesCreateContentResponse:
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
        ComplexTypesCreateContentResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.complex_types.complex_types_create_content(
                title="title",
                body="body",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complex_types_create_content(
            title=title, body=body, tags=tags, metadata=metadata, request_options=request_options
        )
        return _response.data

    async def complex_types_search(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ComplexTypesSearchResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComplexTypesSearchResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.complex_types.complex_types_search(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complex_types_search(input=input, request_options=request_options)
        return _response.data
