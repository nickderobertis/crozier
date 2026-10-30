

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTenantsClient, RawTenantsClient
from .types.tenants_complete_image_upload_response import TenantsCompleteImageUploadResponse
from .types.tenants_create_image_upload_url_request_content_type import TenantsCreateImageUploadUrlRequestContentType
from .types.tenants_create_image_upload_url_response import TenantsCreateImageUploadUrlResponse
from .types.tenants_delete_image_response import TenantsDeleteImageResponse


OMIT = typing.cast(typing.Any, ...)


class TenantsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTenantsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTenantsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTenantsClient
        """
        return self._raw_client

    def createimageuploadurl(
        self,
        id: int,
        *,
        content_type: TenantsCreateImageUploadUrlRequestContentType,
        file_size: int,
        file_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenantsCreateImageUploadUrlResponse:
        """
        Parameters
        ----------
        id : int

        content_type : TenantsCreateImageUploadUrlRequestContentType

        file_size : int

        file_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantsCreateImageUploadUrlResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tenants.createimageuploadurl(
            id=1,
            content_type="image/jpeg",
            file_size=1,
            file_name="fileName",
        )
        """
        _response = self._raw_client.createimageuploadurl(
            id, content_type=content_type, file_size=file_size, file_name=file_name, request_options=request_options
        )
        return _response.data

    def completeimageupload(
        self, id: int, *, object_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TenantsCompleteImageUploadResponse:
        """
        Parameters
        ----------
        id : int

        object_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantsCompleteImageUploadResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tenants.completeimageupload(
            id=1,
            object_key="objectKey",
        )
        """
        _response = self._raw_client.completeimageupload(id, object_key=object_key, request_options=request_options)
        return _response.data

    def deleteimage(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TenantsDeleteImageResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantsDeleteImageResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tenants.deleteimage(
            id=1,
        )
        """
        _response = self._raw_client.deleteimage(id, request_options=request_options)
        return _response.data


class AsyncTenantsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTenantsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTenantsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTenantsClient
        """
        return self._raw_client

    async def createimageuploadurl(
        self,
        id: int,
        *,
        content_type: TenantsCreateImageUploadUrlRequestContentType,
        file_size: int,
        file_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenantsCreateImageUploadUrlResponse:
        """
        Parameters
        ----------
        id : int

        content_type : TenantsCreateImageUploadUrlRequestContentType

        file_size : int

        file_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantsCreateImageUploadUrlResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tenants.createimageuploadurl(
                id=1,
                content_type="image/jpeg",
                file_size=1,
                file_name="fileName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createimageuploadurl(
            id, content_type=content_type, file_size=file_size, file_name=file_name, request_options=request_options
        )
        return _response.data

    async def completeimageupload(
        self, id: int, *, object_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TenantsCompleteImageUploadResponse:
        """
        Parameters
        ----------
        id : int

        object_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantsCompleteImageUploadResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tenants.completeimageupload(
                id=1,
                object_key="objectKey",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.completeimageupload(
            id, object_key=object_key, request_options=request_options
        )
        return _response.data

    async def deleteimage(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TenantsDeleteImageResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantsDeleteImageResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tenants.deleteimage(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deleteimage(id, request_options=request_options)
        return _response.data
