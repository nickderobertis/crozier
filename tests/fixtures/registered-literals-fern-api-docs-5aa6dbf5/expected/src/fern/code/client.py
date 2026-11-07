

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_code_record_response import CreateCodeRecordResponse
from ..types.delete_code_record_response import DeleteCodeRecordResponse
from ..types.get_code_record_response import GetCodeRecordResponse
from ..types.get_code_records_response import GetCodeRecordsResponse
from .raw_client import AsyncRawCodeClient, RawCodeClient


OMIT = typing.cast(typing.Any, ...)


class CodeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCodeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCodeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCodeClient
        """
        return self._raw_client

    def create_code_record(
        self, domain: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CreateCodeRecordResponse]:
        """
        Parameters
        ----------
        domain : str

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CreateCodeRecordResponse]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.code.create_code_record(
            domain="domain",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.create_code_record(domain, request=request, request_options=request_options)
        return _response.data

    def batch_create_code_records(
        self,
        domain: str,
        *,
        request: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[CreateCodeRecordResponse]:
        """
        Parameters
        ----------
        domain : str

        request : typing.Sequence[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CreateCodeRecordResponse]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.code.batch_create_code_records(
            domain="domain",
            request=[],
        )
        """
        _response = self._raw_client.batch_create_code_records(domain, request=request, request_options=request_options)
        return _response.data

    def get_code_record_by_id(
        self, domain: str, code_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCodeRecordResponse:
        """
        Parameters
        ----------
        domain : str

        code_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCodeRecordResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.code.get_code_record_by_id(
            domain="domain",
            code_id="code_id",
        )
        """
        _response = self._raw_client.get_code_record_by_id(domain, code_id, request_options=request_options)
        return _response.data

    def get_code_records(
        self,
        domain: str,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCodeRecordsResponse:
        """
        Parameters
        ----------
        domain : str

        page : typing.Optional[int]
            The page number for pagination

        limit : typing.Optional[int]
            The number of code entries per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCodeRecordsResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.code.get_code_records(
            domain="domain",
        )
        """
        _response = self._raw_client.get_code_records(domain, page=page, limit=limit, request_options=request_options)
        return _response.data

    def delete_code_record_by_id(
        self, domain: str, *, code_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteCodeRecordResponse:
        """
        Parameters
        ----------
        domain : str

        code_id : str
            The unique identifier of the code to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteCodeRecordResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.code.delete_code_record_by_id(
            domain="domain",
            code_id="code_id",
        )
        """
        _response = self._raw_client.delete_code_record_by_id(domain, code_id=code_id, request_options=request_options)
        return _response.data

    def delete_all_code_records(
        self, domain: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteCodeRecordResponse:
        """
        Parameters
        ----------
        domain : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteCodeRecordResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.code.delete_all_code_records(
            domain="domain",
        )
        """
        _response = self._raw_client.delete_all_code_records(domain, request_options=request_options)
        return _response.data


class AsyncCodeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCodeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCodeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCodeClient
        """
        return self._raw_client

    async def create_code_record(
        self, domain: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CreateCodeRecordResponse]:
        """
        Parameters
        ----------
        domain : str

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CreateCodeRecordResponse]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.code.create_code_record(
                domain="domain",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_code_record(domain, request=request, request_options=request_options)
        return _response.data

    async def batch_create_code_records(
        self,
        domain: str,
        *,
        request: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[CreateCodeRecordResponse]:
        """
        Parameters
        ----------
        domain : str

        request : typing.Sequence[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CreateCodeRecordResponse]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.code.batch_create_code_records(
                domain="domain",
                request=[],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.batch_create_code_records(
            domain, request=request, request_options=request_options
        )
        return _response.data

    async def get_code_record_by_id(
        self, domain: str, code_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCodeRecordResponse:
        """
        Parameters
        ----------
        domain : str

        code_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCodeRecordResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.code.get_code_record_by_id(
                domain="domain",
                code_id="code_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_code_record_by_id(domain, code_id, request_options=request_options)
        return _response.data

    async def get_code_records(
        self,
        domain: str,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCodeRecordsResponse:
        """
        Parameters
        ----------
        domain : str

        page : typing.Optional[int]
            The page number for pagination

        limit : typing.Optional[int]
            The number of code entries per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCodeRecordsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.code.get_code_records(
                domain="domain",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_code_records(
            domain, page=page, limit=limit, request_options=request_options
        )
        return _response.data

    async def delete_code_record_by_id(
        self, domain: str, *, code_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteCodeRecordResponse:
        """
        Parameters
        ----------
        domain : str

        code_id : str
            The unique identifier of the code to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteCodeRecordResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.code.delete_code_record_by_id(
                domain="domain",
                code_id="code_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_code_record_by_id(
            domain, code_id=code_id, request_options=request_options
        )
        return _response.data

    async def delete_all_code_records(
        self, domain: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteCodeRecordResponse:
        """
        Parameters
        ----------
        domain : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteCodeRecordResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.code.delete_all_code_records(
                domain="domain",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_all_code_records(domain, request_options=request_options)
        return _response.data
