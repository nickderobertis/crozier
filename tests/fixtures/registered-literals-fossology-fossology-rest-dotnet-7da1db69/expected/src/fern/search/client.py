

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.search_results import SearchResults
from .raw_client import AsyncRawSearchClient, RawSearchClient


class SearchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSearchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSearchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSearchClient
        """
        return self._raw_client

    def file(
        self,
        *,
        group_name: typing.Optional[str] = None,
        upload_id: typing.Optional[int] = None,
        filename: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        filesizemin: typing.Optional[int] = None,
        filesizemax: typing.Optional[int] = None,
        license: typing.Optional[str] = None,
        copyright: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[SearchResults]:
        """
        Search the FOSSology for a specific file

        Parameters
        ----------
        group_name : typing.Optional[str]
            The group name to chose while performing search

        upload_id : typing.Optional[int]
            Id of the upload to search files into

        filename : typing.Optional[str]
            Filename to find, can contain % as wild-card

        tag : typing.Optional[str]
            Tag to find

        page : typing.Optional[int]
            Page number (starts from 1)

        limit : typing.Optional[int]
            Limits of responses per request

        filesizemin : typing.Optional[int]
            Min filesize in bytes

        filesizemax : typing.Optional[int]
            Max filesize in bytes

        license : typing.Optional[str]
            License search filter

        copyright : typing.Optional[str]
            Copyright search filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SearchResults]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.search.file()
        """
        _response = self._raw_client.file(
            group_name=group_name,
            upload_id=upload_id,
            filename=filename,
            tag=tag,
            page=page,
            limit=limit,
            filesizemin=filesizemin,
            filesizemax=filesizemax,
            license=license,
            copyright=copyright,
            request_options=request_options,
        )
        return _response.data


class AsyncSearchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSearchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSearchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSearchClient
        """
        return self._raw_client

    async def file(
        self,
        *,
        group_name: typing.Optional[str] = None,
        upload_id: typing.Optional[int] = None,
        filename: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        filesizemin: typing.Optional[int] = None,
        filesizemax: typing.Optional[int] = None,
        license: typing.Optional[str] = None,
        copyright: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[SearchResults]:
        """
        Search the FOSSology for a specific file

        Parameters
        ----------
        group_name : typing.Optional[str]
            The group name to chose while performing search

        upload_id : typing.Optional[int]
            Id of the upload to search files into

        filename : typing.Optional[str]
            Filename to find, can contain % as wild-card

        tag : typing.Optional[str]
            Tag to find

        page : typing.Optional[int]
            Page number (starts from 1)

        limit : typing.Optional[int]
            Limits of responses per request

        filesizemin : typing.Optional[int]
            Min filesize in bytes

        filesizemax : typing.Optional[int]
            Max filesize in bytes

        license : typing.Optional[str]
            License search filter

        copyright : typing.Optional[str]
            Copyright search filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SearchResults]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.search.file()


        asyncio.run(main())
        """
        _response = await self._raw_client.file(
            group_name=group_name,
            upload_id=upload_id,
            filename=filename,
            tag=tag,
            page=page,
            limit=limit,
            filesizemin=filesizemin,
            filesizemax=filesizemax,
            license=license,
            copyright=copyright,
            request_options=request_options,
        )
        return _response.data
