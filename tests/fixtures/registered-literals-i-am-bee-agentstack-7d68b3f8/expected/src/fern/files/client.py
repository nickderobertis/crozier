

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output8 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput8,
)
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output9 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput9,
)
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output10 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput10,
)
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output11 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput11,
)
from ..types.file_list_query import FileListQuery
from ..types.paginated_result_file import PaginatedResultFile
from ..types.text_extraction_request import TextExtractionRequest
from .raw_client import AsyncRawFilesClient, RawFilesClient


OMIT = typing.cast(typing.Any, ...)


class FilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFilesClient
        """
        return self._raw_client

    def list_files(
        self,
        *,
        query: FileListQuery,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResultFile:
        """
        Parameters
        ----------
        query : FileListQuery

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResultFile
            Successful Response

        Examples
        --------
        from fern import FernApi, FileListQuery

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.files.list_files(
            query=FileListQuery(),
        )
        """
        _response = self._raw_client.list_files(query=query, context_id=context_id, request_options=request_options)
        return _response.data

    def upload_file(
        self,
        *,
        file: core.File,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput8:
        """
        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput8
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.files.upload_file()
        """
        _response = self._raw_client.upload_file(file=file, context_id=context_id, request_options=request_options)
        return _response.data

    def get_file(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput9:
        """
        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput9
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.files.get_file(
            file_id="file_id",
        )
        """
        _response = self._raw_client.get_file(file_id, context_id=context_id, request_options=request_options)
        return _response.data

    def delete_file(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.files.delete_file(
            file_id="file_id",
        )
        """
        _response = self._raw_client.delete_file(file_id, context_id=context_id, request_options=request_options)
        return _response.data

    def get_file_content(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.files.get_file_content(
            file_id="file_id",
        )
        """
        _response = self._raw_client.get_file_content(file_id, context_id=context_id, request_options=request_options)
        return _response.data

    def get_text_file_content(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.files.get_text_file_content(
            file_id="file_id",
        )
        """
        _response = self._raw_client.get_text_file_content(
            file_id, context_id=context_id, request_options=request_options
        )
        return _response.data

    def get_text_extraction(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput11:
        """
        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput11
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.files.get_text_extraction(
            file_id="file_id",
        )
        """
        _response = self._raw_client.get_text_extraction(
            file_id, context_id=context_id, request_options=request_options
        )
        return _response.data

    def create_text_extraction(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request: typing.Optional[TextExtractionRequest] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput10:
        """
        Create or return text extraction for a file.

        - If extraction is completed, returns existing result
        - If extraction failed, retries the extraction
        - If extraction is pending/in-progress, returns current status
        - If no extraction exists, creates a new one

        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

        request : typing.Optional[TextExtractionRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput10
            Successful Response

        Examples
        --------
        from fern import FernApi, TextExtractionRequest

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.files.create_text_extraction(
            file_id="file_id",
            request=TextExtractionRequest(),
        )
        """
        _response = self._raw_client.create_text_extraction(
            file_id, context_id=context_id, request=request, request_options=request_options
        )
        return _response.data

    def delete_text_extraction(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.files.delete_text_extraction(
            file_id="file_id",
        )
        """
        _response = self._raw_client.delete_text_extraction(
            file_id, context_id=context_id, request_options=request_options
        )
        return _response.data


class AsyncFilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFilesClient
        """
        return self._raw_client

    async def list_files(
        self,
        *,
        query: FileListQuery,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResultFile:
        """
        Parameters
        ----------
        query : FileListQuery

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResultFile
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FileListQuery

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.files.list_files(
                query=FileListQuery(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_files(
            query=query, context_id=context_id, request_options=request_options
        )
        return _response.data

    async def upload_file(
        self,
        *,
        file: core.File,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput8:
        """
        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput8
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.files.upload_file()


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_file(
            file=file, context_id=context_id, request_options=request_options
        )
        return _response.data

    async def get_file(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput9:
        """
        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput9
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.files.get_file(
                file_id="file_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_file(file_id, context_id=context_id, request_options=request_options)
        return _response.data

    async def delete_file(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.files.delete_file(
                file_id="file_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_file(file_id, context_id=context_id, request_options=request_options)
        return _response.data

    async def get_file_content(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.files.get_file_content(
                file_id="file_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_file_content(
            file_id, context_id=context_id, request_options=request_options
        )
        return _response.data

    async def get_text_file_content(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.files.get_text_file_content(
                file_id="file_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_text_file_content(
            file_id, context_id=context_id, request_options=request_options
        )
        return _response.data

    async def get_text_extraction(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput11:
        """
        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput11
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.files.get_text_extraction(
                file_id="file_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_text_extraction(
            file_id, context_id=context_id, request_options=request_options
        )
        return _response.data

    async def create_text_extraction(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request: typing.Optional[TextExtractionRequest] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput10:
        """
        Create or return text extraction for a file.

        - If extraction is completed, returns existing result
        - If extraction failed, retries the extraction
        - If extraction is pending/in-progress, returns current status
        - If no extraction exists, creates a new one

        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

        request : typing.Optional[TextExtractionRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput10
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, TextExtractionRequest

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.files.create_text_extraction(
                file_id="file_id",
                request=TextExtractionRequest(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_text_extraction(
            file_id, context_id=context_id, request=request, request_options=request_options
        )
        return _response.data

    async def delete_text_extraction(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.files.delete_text_extraction(
                file_id="file_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_text_extraction(
            file_id, context_id=context_id, request_options=request_options
        )
        return _response.data
