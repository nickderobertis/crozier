

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.envelope_list_service_get import EnvelopeListServiceGet
from ..types.envelope_list_viewer import EnvelopeListViewer
from .raw_client import AsyncRawNihSparcClient, RawNihSparcClient


class NihSparcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNihSparcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNihSparcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNihSparcClient
        """
        return self._raw_client

    def list_latest_services(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListServiceGet:
        """
        Returns a list latest version of services

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListServiceGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nih_sparc.list_latest_services()
        """
        _response = self._raw_client.list_latest_services(request_options=request_options)
        return _response.data

    def list_viewers(
        self, *, file_type: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListViewer:
        """
        Lists all publicly available viewers

        Notice that this might contain multiple services for the same filetype

        If file_type is provided, then it filters viewer for that filetype

        Parameters
        ----------
        file_type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListViewer
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nih_sparc.list_viewers()
        """
        _response = self._raw_client.list_viewers(file_type=file_type, request_options=request_options)
        return _response.data

    def list_default_viewers(
        self, *, file_type: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListViewer:
        """
        Lists the default viewer for each supported filetype

        This was interfaced as a subcollection of viewers because it is a very common use-case

        Only publicly available viewers

        If file_type is provided, then it filters viewer for that filetype

        Parameters
        ----------
        file_type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListViewer
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nih_sparc.list_default_viewers()
        """
        _response = self._raw_client.list_default_viewers(file_type=file_type, request_options=request_options)
        return _response.data

    def get_redirection_to_viewer(
        self,
        *,
        file_type: str,
        viewer_key: str,
        viewer_version: str,
        file_size: int,
        download_link: str,
        file_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Opens a viewer in osparc for data in the NIH-sparc portal

        Parameters
        ----------
        file_type : str

        viewer_key : str

        viewer_version : str

        file_size : int

        download_link : str

        file_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nih_sparc.get_redirection_to_viewer(
            file_type="file_type",
            viewer_key="viewer_key",
            viewer_version="viewer_version",
            file_size=1,
            download_link="download_link",
        )
        """
        _response = self._raw_client.get_redirection_to_viewer(
            file_type=file_type,
            viewer_key=viewer_key,
            viewer_version=viewer_version,
            file_size=file_size,
            download_link=download_link,
            file_name=file_name,
            request_options=request_options,
        )
        return _response.data

    def get_redirection_to_study_page(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Opens a study published in osparc

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nih_sparc.get_redirection_to_study_page(
            id="id",
        )
        """
        _response = self._raw_client.get_redirection_to_study_page(id, request_options=request_options)
        return _response.data


class AsyncNihSparcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNihSparcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNihSparcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNihSparcClient
        """
        return self._raw_client

    async def list_latest_services(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListServiceGet:
        """
        Returns a list latest version of services

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListServiceGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nih_sparc.list_latest_services()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_latest_services(request_options=request_options)
        return _response.data

    async def list_viewers(
        self, *, file_type: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListViewer:
        """
        Lists all publicly available viewers

        Notice that this might contain multiple services for the same filetype

        If file_type is provided, then it filters viewer for that filetype

        Parameters
        ----------
        file_type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListViewer
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nih_sparc.list_viewers()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_viewers(file_type=file_type, request_options=request_options)
        return _response.data

    async def list_default_viewers(
        self, *, file_type: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListViewer:
        """
        Lists the default viewer for each supported filetype

        This was interfaced as a subcollection of viewers because it is a very common use-case

        Only publicly available viewers

        If file_type is provided, then it filters viewer for that filetype

        Parameters
        ----------
        file_type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListViewer
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nih_sparc.list_default_viewers()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_default_viewers(file_type=file_type, request_options=request_options)
        return _response.data

    async def get_redirection_to_viewer(
        self,
        *,
        file_type: str,
        viewer_key: str,
        viewer_version: str,
        file_size: int,
        download_link: str,
        file_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Opens a viewer in osparc for data in the NIH-sparc portal

        Parameters
        ----------
        file_type : str

        viewer_key : str

        viewer_version : str

        file_size : int

        download_link : str

        file_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nih_sparc.get_redirection_to_viewer(
                file_type="file_type",
                viewer_key="viewer_key",
                viewer_version="viewer_version",
                file_size=1,
                download_link="download_link",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_redirection_to_viewer(
            file_type=file_type,
            viewer_key=viewer_key,
            viewer_version=viewer_version,
            file_size=file_size,
            download_link=download_link,
            file_name=file_name,
            request_options=request_options,
        )
        return _response.data

    async def get_redirection_to_study_page(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Opens a study published in osparc

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nih_sparc.get_redirection_to_study_page(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_redirection_to_study_page(id, request_options=request_options)
        return _response.data
