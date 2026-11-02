

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.photo import Photo
from .raw_client import AsyncRawPhotosClient, RawPhotosClient
from .types.proof_response import ProofResponse
from .types.retouch_photo_request_options import RetouchPhotoRequestOptions


OMIT = typing.cast(typing.Any, ...)


class PhotosClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPhotosClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPhotosClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPhotosClient
        """
        return self._raw_client

    def retouch_photo(
        self,
        *,
        brief: str,
        options: typing.Optional[RetouchPhotoRequestOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Photo:
        """
        Parameters
        ----------
        brief : str

        options : typing.Optional[RetouchPhotoRequestOptions]
            How to retouch the photo.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Photo
            The retouched photo

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.photos.retouch_photo(
            brief="brief",
        )
        """
        _response = self._raw_client.retouch_photo(brief=brief, options=options, request_options=request_options)
        return _response.data

    def get_proof(self, photo_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ProofResponse:
        """
        Parameters
        ----------
        photo_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProofResponse
            The proof of the photo

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.photos.get_proof(
            photo_id="photoId",
        )
        """
        _response = self._raw_client.get_proof(photo_id, request_options=request_options)
        return _response.data


class AsyncPhotosClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPhotosClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPhotosClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPhotosClient
        """
        return self._raw_client

    async def retouch_photo(
        self,
        *,
        brief: str,
        options: typing.Optional[RetouchPhotoRequestOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Photo:
        """
        Parameters
        ----------
        brief : str

        options : typing.Optional[RetouchPhotoRequestOptions]
            How to retouch the photo.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Photo
            The retouched photo

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.photos.retouch_photo(
                brief="brief",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retouch_photo(brief=brief, options=options, request_options=request_options)
        return _response.data

    async def get_proof(
        self, photo_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProofResponse:
        """
        Parameters
        ----------
        photo_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProofResponse
            The proof of the photo

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.photos.get_proof(
                photo_id="photoId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_proof(photo_id, request_options=request_options)
        return _response.data
