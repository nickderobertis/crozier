

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSequenceTemplatesClient, RawSequenceTemplatesClient
from .types.sequence_template_create_request_data import SequenceTemplateCreateRequestData


OMIT = typing.cast(typing.Any, ...)


class SequenceTemplatesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSequenceTemplatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSequenceTemplatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSequenceTemplatesClient
        """
        return self._raw_client

    def list_sequence_templates(
        self,
        *,
        page_offset: typing.Optional[int] = None,
        page_limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        page_offset : typing.Optional[int]
            Page offset for pagination

        page_limit : typing.Optional[int]
            Page limit for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sequence_templates.list_sequence_templates()
        """
        _response = self._raw_client.list_sequence_templates(
            page_offset=page_offset, page_limit=page_limit, request_options=request_options
        )
        return _response.data

    def create_sequence_template(
        self,
        *,
        data: typing.Optional[SequenceTemplateCreateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        data : typing.Optional[SequenceTemplateCreateRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sequence_templates.create_sequence_template()
        """
        _response = self._raw_client.create_sequence_template(data=data, request_options=request_options)
        return _response.data


class AsyncSequenceTemplatesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSequenceTemplatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSequenceTemplatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSequenceTemplatesClient
        """
        return self._raw_client

    async def list_sequence_templates(
        self,
        *,
        page_offset: typing.Optional[int] = None,
        page_limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        page_offset : typing.Optional[int]
            Page offset for pagination

        page_limit : typing.Optional[int]
            Page limit for pagination

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sequence_templates.list_sequence_templates()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_sequence_templates(
            page_offset=page_offset, page_limit=page_limit, request_options=request_options
        )
        return _response.data

    async def create_sequence_template(
        self,
        *,
        data: typing.Optional[SequenceTemplateCreateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        data : typing.Optional[SequenceTemplateCreateRequestData]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sequence_templates.create_sequence_template()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_sequence_template(data=data, request_options=request_options)
        return _response.data
