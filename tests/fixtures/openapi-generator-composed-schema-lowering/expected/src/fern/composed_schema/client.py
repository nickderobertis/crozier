

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.input_param import InputParam
from ..types.model_ids_responses import ModelIdsResponses
from ..types.response_stream_event import ResponseStreamEvent
from ..types.timestamp_container import TimestampContainer
from ..types.variant_payload import VariantPayload
from .raw_client import AsyncRawComposedSchemaClient, RawComposedSchemaClient
from .types.get_inline_any_of_response_response import GetInlineAnyOfResponseResponse
from .types.get_inline_one_of_events_response import GetInlineOneOfEventsResponse


OMIT = typing.cast(typing.Any, ...)


class ComposedSchemaClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawComposedSchemaClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawComposedSchemaClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawComposedSchemaClient
        """
        return self._raw_client

    def post_variant_body(
        self, *, request: InputParam, request_options: typing.Optional[RequestOptions] = None
    ) -> InputParam:
        """
        Parameters
        ----------
        request : InputParam

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InputParam
            Variant request/response round-trip

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.composed_schema.post_variant_body(
            request="string",
        )
        """
        _response = self._raw_client.post_variant_body(request=request, request_options=request_options)
        return _response.data

    def post_alias_body(
        self, *, request: ModelIdsResponses, request_options: typing.Optional[RequestOptions] = None
    ) -> ModelIdsResponses:
        """
        Parameters
        ----------
        request : ModelIdsResponses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelIdsResponses
            Alias request/response round-trip

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.composed_schema.post_alias_body(
            request="ids",
        )
        """
        _response = self._raw_client.post_alias_body(request=request, request_options=request_options)
        return _response.data

    def get_stream_events(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[ResponseStreamEvent]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[ResponseStreamEvent]
            SSE streaming response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.composed_schema.get_stream_events()
        for chunk in response:
            yield chunk
        """
        with self._raw_client.get_stream_events(request_options=request_options) as r:
            yield from r.data

    def upload_file(
        self,
        *,
        file: typing.Optional[core.File] = OMIT,
        metadata: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        file : typing.Optional[core.File]
            See core.File for more documentation

        metadata : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            File upload response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.composed_schema.upload_file()
        """
        _response = self._raw_client.upload_file(file=file, metadata=metadata, request_options=request_options)
        return _response.data

    def upload_variant_data(
        self,
        *,
        payload: typing.Optional[VariantPayload] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        payload : typing.Optional[VariantPayload]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Variant upload response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.composed_schema.upload_variant_data()
        """
        _response = self._raw_client.upload_variant_data(payload=payload, request_options=request_options)
        return _response.data

    def get_dual_stream(
        self, *, stream: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> TimestampContainer:
        """
        Dual-content shape: a single 200 response with both application/json and text/event-stream media types. The stream query parameter toggles between JSON (default) and SSE streaming.

        Parameters
        ----------
        stream : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TimestampContainer
            Normal JSON or SSE streaming response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.composed_schema.get_dual_stream()
        """
        _response = self._raw_client.get_dual_stream(stream=stream, request_options=request_options)
        return _response.data

    def get_inline_any_of_response(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetInlineAnyOfResponseResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetInlineAnyOfResponseResponse
            Inline anyOf response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.composed_schema.get_inline_any_of_response()
        """
        _response = self._raw_client.get_inline_any_of_response(request_options=request_options)
        return _response.data

    def get_inline_one_of_events(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[GetInlineOneOfEventsResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[GetInlineOneOfEventsResponse]
            Inline oneOf SSE response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.composed_schema.get_inline_one_of_events()
        for chunk in response:
            yield chunk
        """
        with self._raw_client.get_inline_one_of_events(request_options=request_options) as r:
            yield from r.data

    def get_dual_primitive_stream(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Primitive JSON or SSE response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.composed_schema.get_dual_primitive_stream()
        """
        _response = self._raw_client.get_dual_primitive_stream(request_options=request_options)
        return _response.data

    def delete_without_content(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.composed_schema.delete_without_content()
        """
        _response = self._raw_client.delete_without_content(request_options=request_options)
        return _response.data


class AsyncComposedSchemaClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawComposedSchemaClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawComposedSchemaClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawComposedSchemaClient
        """
        return self._raw_client

    async def post_variant_body(
        self, *, request: InputParam, request_options: typing.Optional[RequestOptions] = None
    ) -> InputParam:
        """
        Parameters
        ----------
        request : InputParam

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InputParam
            Variant request/response round-trip

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.composed_schema.post_variant_body(
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_variant_body(request=request, request_options=request_options)
        return _response.data

    async def post_alias_body(
        self, *, request: ModelIdsResponses, request_options: typing.Optional[RequestOptions] = None
    ) -> ModelIdsResponses:
        """
        Parameters
        ----------
        request : ModelIdsResponses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelIdsResponses
            Alias request/response round-trip

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.composed_schema.post_alias_body(
                request="ids",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_alias_body(request=request, request_options=request_options)
        return _response.data

    async def get_stream_events(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[ResponseStreamEvent]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[ResponseStreamEvent]
            SSE streaming response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = client.composed_schema.get_stream_events()
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.get_stream_events(request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def upload_file(
        self,
        *,
        file: typing.Optional[core.File] = OMIT,
        metadata: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        file : typing.Optional[core.File]
            See core.File for more documentation

        metadata : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            File upload response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.composed_schema.upload_file()


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_file(file=file, metadata=metadata, request_options=request_options)
        return _response.data

    async def upload_variant_data(
        self,
        *,
        payload: typing.Optional[VariantPayload] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        payload : typing.Optional[VariantPayload]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Variant upload response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.composed_schema.upload_variant_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_variant_data(payload=payload, request_options=request_options)
        return _response.data

    async def get_dual_stream(
        self, *, stream: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> TimestampContainer:
        """
        Dual-content shape: a single 200 response with both application/json and text/event-stream media types. The stream query parameter toggles between JSON (default) and SSE streaming.

        Parameters
        ----------
        stream : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TimestampContainer
            Normal JSON or SSE streaming response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.composed_schema.get_dual_stream()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_dual_stream(stream=stream, request_options=request_options)
        return _response.data

    async def get_inline_any_of_response(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetInlineAnyOfResponseResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetInlineAnyOfResponseResponse
            Inline anyOf response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.composed_schema.get_inline_any_of_response()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_inline_any_of_response(request_options=request_options)
        return _response.data

    async def get_inline_one_of_events(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[GetInlineOneOfEventsResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[GetInlineOneOfEventsResponse]
            Inline oneOf SSE response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = client.composed_schema.get_inline_one_of_events()
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.get_inline_one_of_events(request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_dual_primitive_stream(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Primitive JSON or SSE response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.composed_schema.get_dual_primitive_stream()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_dual_primitive_stream(request_options=request_options)
        return _response.data

    async def delete_without_content(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.composed_schema.delete_without_content()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_without_content(request_options=request_options)
        return _response.data
