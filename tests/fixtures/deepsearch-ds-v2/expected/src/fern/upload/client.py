

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.project_scratch_files import ProjectScratchFiles
from ..types.project_scratch_files_paginated import ProjectScratchFilesPaginated
from ..types.temporary_upload_file_result import TemporaryUploadFileResult
from .raw_client import AsyncRawUploadClient, RawUploadClient


class UploadClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUploadClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUploadClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUploadClient
        """
        return self._raw_client

    def list_project_scratch_files(
        self,
        proj_key: str,
        *,
        scratch_ids: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ProjectScratchFiles]:
        """
        Get temporary files uploaded to a project.

        Parameters
        ----------
        proj_key : str

        scratch_ids : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ProjectScratchFiles]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.upload.list_project_scratch_files(
            proj_key="proj_key",
        )
        """
        _response = self._raw_client.list_project_scratch_files(
            proj_key, scratch_ids=scratch_ids, request_options=request_options
        )
        return _response.data

    def list_project_scratch_files_paginated(
        self,
        proj_key: str,
        *,
        page: typing.Optional[int] = None,
        items_per_page: typing.Optional[int] = None,
        search_string: typing.Optional[str] = None,
        begin_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectScratchFilesPaginated:
        """
        Get paginated list of temporary files uploaded to a project.

        Parameters
        ----------
        proj_key : str

        page : typing.Optional[int]

        items_per_page : typing.Optional[int]

        search_string : typing.Optional[str]

        begin_date : typing.Optional[int]

        end_date : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectScratchFilesPaginated
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.upload.list_project_scratch_files_paginated(
            proj_key="proj_key",
        )
        """
        _response = self._raw_client.list_project_scratch_files_paginated(
            proj_key,
            page=page,
            items_per_page=items_per_page,
            search_string=search_string,
            begin_date=begin_date,
            end_date=end_date,
            request_options=request_options,
        )
        return _response.data

    def create_project_scratch_file(
        self, proj_key: str, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TemporaryUploadFileResult:
        """
        Create file pointers for temporary storage.

        Parameters
        ----------
        proj_key : str

        filename : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TemporaryUploadFileResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.upload.create_project_scratch_file(
            proj_key="proj_key",
            filename="filename",
        )
        """
        _response = self._raw_client.create_project_scratch_file(proj_key, filename, request_options=request_options)
        return _response.data


class AsyncUploadClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUploadClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUploadClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUploadClient
        """
        return self._raw_client

    async def list_project_scratch_files(
        self,
        proj_key: str,
        *,
        scratch_ids: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ProjectScratchFiles]:
        """
        Get temporary files uploaded to a project.

        Parameters
        ----------
        proj_key : str

        scratch_ids : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ProjectScratchFiles]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.upload.list_project_scratch_files(
                proj_key="proj_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_project_scratch_files(
            proj_key, scratch_ids=scratch_ids, request_options=request_options
        )
        return _response.data

    async def list_project_scratch_files_paginated(
        self,
        proj_key: str,
        *,
        page: typing.Optional[int] = None,
        items_per_page: typing.Optional[int] = None,
        search_string: typing.Optional[str] = None,
        begin_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectScratchFilesPaginated:
        """
        Get paginated list of temporary files uploaded to a project.

        Parameters
        ----------
        proj_key : str

        page : typing.Optional[int]

        items_per_page : typing.Optional[int]

        search_string : typing.Optional[str]

        begin_date : typing.Optional[int]

        end_date : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectScratchFilesPaginated
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.upload.list_project_scratch_files_paginated(
                proj_key="proj_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_project_scratch_files_paginated(
            proj_key,
            page=page,
            items_per_page=items_per_page,
            search_string=search_string,
            begin_date=begin_date,
            end_date=end_date,
            request_options=request_options,
        )
        return _response.data

    async def create_project_scratch_file(
        self, proj_key: str, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TemporaryUploadFileResult:
        """
        Create file pointers for temporary storage.

        Parameters
        ----------
        proj_key : str

        filename : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TemporaryUploadFileResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.upload.create_project_scratch_file(
                proj_key="proj_key",
                filename="filename",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_project_scratch_file(
            proj_key, filename, request_options=request_options
        )
        return _response.data
