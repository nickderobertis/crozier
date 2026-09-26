

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTemplatesClient, RawTemplatesClient
from .types.template_create_request_data import TemplateCreateRequestData
from .types.template_update_request_data import TemplateUpdateRequestData


OMIT = typing.cast(typing.Any, ...)


class TemplatesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTemplatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTemplatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTemplatesClient
        """
        return self._raw_client

    def list_templates(
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
        client.templates.list_templates()
        """
        _response = self._raw_client.list_templates(
            page_offset=page_offset, page_limit=page_limit, request_options=request_options
        )
        return _response.data

    def create_template(
        self,
        *,
        data: typing.Optional[TemplateCreateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        data : typing.Optional[TemplateCreateRequestData]

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
        client.templates.create_template()
        """
        _response = self._raw_client.create_template(data=data, request_options=request_options)
        return _response.data

    def get_template(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int
            Resource ID

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
        client.templates.get_template(
            id=1,
        )
        """
        _response = self._raw_client.get_template(id, request_options=request_options)
        return _response.data

    def delete_template(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int
            Resource ID

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
        client.templates.delete_template(
            id=1,
        )
        """
        _response = self._raw_client.delete_template(id, request_options=request_options)
        return _response.data

    def update_template(
        self,
        id: int,
        *,
        data: typing.Optional[TemplateUpdateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int
            Resource ID

        data : typing.Optional[TemplateUpdateRequestData]

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
        client.templates.update_template(
            id=1,
        )
        """
        _response = self._raw_client.update_template(id, data=data, request_options=request_options)
        return _response.data


class AsyncTemplatesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTemplatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTemplatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTemplatesClient
        """
        return self._raw_client

    async def list_templates(
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
            await client.templates.list_templates()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_templates(
            page_offset=page_offset, page_limit=page_limit, request_options=request_options
        )
        return _response.data

    async def create_template(
        self,
        *,
        data: typing.Optional[TemplateCreateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        data : typing.Optional[TemplateCreateRequestData]

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
            await client.templates.create_template()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_template(data=data, request_options=request_options)
        return _response.data

    async def get_template(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int
            Resource ID

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
            await client.templates.get_template(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_template(id, request_options=request_options)
        return _response.data

    async def delete_template(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int
            Resource ID

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
            await client.templates.delete_template(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_template(id, request_options=request_options)
        return _response.data

    async def update_template(
        self,
        id: int,
        *,
        data: typing.Optional[TemplateUpdateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int
            Resource ID

        data : typing.Optional[TemplateUpdateRequestData]

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
            await client.templates.update_template(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_template(id, data=data, request_options=request_options)
        return _response.data
