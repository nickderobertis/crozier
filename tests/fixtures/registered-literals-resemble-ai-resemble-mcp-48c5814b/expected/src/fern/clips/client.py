

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawClipsClient, RawClipsClient
from .types.delete_clip_response import DeleteClipResponse
from .types.get_clip_response import GetClipResponse
from .types.list_clips_response import ListClipsResponse
from .types.update_clip_response import UpdateClipResponse


OMIT = typing.cast(typing.Any, ...)


class ClipsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawClipsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawClipsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawClipsClient
        """
        return self._raw_client

    def list_clips(
        self,
        project_uuid: str,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListClipsResponse:
        """
        List clips in a project

        Parameters
        ----------
        project_uuid : str

        page : int

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListClipsResponse
            List of clips

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.clips.list_clips(
            project_uuid="project_uuid",
            page=1,
        )
        """
        _response = self._raw_client.list_clips(
            project_uuid, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    def get_clip(
        self, project_uuid: str, clip_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetClipResponse:
        """
        Get clip details

        Parameters
        ----------
        project_uuid : str

        clip_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetClipResponse
            Clip details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.clips.get_clip(
            project_uuid="project_uuid",
            clip_uuid="clip_uuid",
        )
        """
        _response = self._raw_client.get_clip(project_uuid, clip_uuid, request_options=request_options)
        return _response.data

    def delete_clip(
        self, project_uuid: str, clip_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteClipResponse:
        """
        Delete a clip

        Parameters
        ----------
        project_uuid : str

        clip_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteClipResponse
            Clip deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.clips.delete_clip(
            project_uuid="project_uuid",
            clip_uuid="clip_uuid",
        )
        """
        _response = self._raw_client.delete_clip(project_uuid, clip_uuid, request_options=request_options)
        return _response.data

    def update_clip(
        self,
        project_uuid: str,
        clip_uuid: str,
        *,
        title: typing.Optional[str] = OMIT,
        body: typing.Optional[str] = OMIT,
        is_archived: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateClipResponse:
        """
        Update a clip

        Parameters
        ----------
        project_uuid : str

        clip_uuid : str

        title : typing.Optional[str]

        body : typing.Optional[str]

        is_archived : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateClipResponse
            Clip updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.clips.update_clip(
            project_uuid="project_uuid",
            clip_uuid="clip_uuid",
        )
        """
        _response = self._raw_client.update_clip(
            project_uuid, clip_uuid, title=title, body=body, is_archived=is_archived, request_options=request_options
        )
        return _response.data


class AsyncClipsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawClipsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawClipsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawClipsClient
        """
        return self._raw_client

    async def list_clips(
        self,
        project_uuid: str,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListClipsResponse:
        """
        List clips in a project

        Parameters
        ----------
        project_uuid : str

        page : int

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListClipsResponse
            List of clips

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.clips.list_clips(
                project_uuid="project_uuid",
                page=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_clips(
            project_uuid, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def get_clip(
        self, project_uuid: str, clip_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetClipResponse:
        """
        Get clip details

        Parameters
        ----------
        project_uuid : str

        clip_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetClipResponse
            Clip details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.clips.get_clip(
                project_uuid="project_uuid",
                clip_uuid="clip_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_clip(project_uuid, clip_uuid, request_options=request_options)
        return _response.data

    async def delete_clip(
        self, project_uuid: str, clip_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteClipResponse:
        """
        Delete a clip

        Parameters
        ----------
        project_uuid : str

        clip_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteClipResponse
            Clip deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.clips.delete_clip(
                project_uuid="project_uuid",
                clip_uuid="clip_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_clip(project_uuid, clip_uuid, request_options=request_options)
        return _response.data

    async def update_clip(
        self,
        project_uuid: str,
        clip_uuid: str,
        *,
        title: typing.Optional[str] = OMIT,
        body: typing.Optional[str] = OMIT,
        is_archived: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateClipResponse:
        """
        Update a clip

        Parameters
        ----------
        project_uuid : str

        clip_uuid : str

        title : typing.Optional[str]

        body : typing.Optional[str]

        is_archived : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateClipResponse
            Clip updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.clips.update_clip(
                project_uuid="project_uuid",
                clip_uuid="clip_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_clip(
            project_uuid, clip_uuid, title=title, body=body, is_archived=is_archived, request_options=request_options
        )
        return _response.data
