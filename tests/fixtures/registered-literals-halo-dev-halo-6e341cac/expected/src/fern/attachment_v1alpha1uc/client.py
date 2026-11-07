

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.attachment import Attachment
from ..types.attachment_list import AttachmentList
from ..types.attachment_permalink_match_list import AttachmentPermalinkMatchList
from .raw_client import AsyncRawAttachmentV1Alpha1UcClient, RawAttachmentV1Alpha1UcClient


OMIT = typing.cast(typing.Any, ...)


class AttachmentV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAttachmentV1Alpha1UcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAttachmentV1Alpha1UcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAttachmentV1Alpha1UcClient
        """
        return self._raw_client

    def list_my_attachments(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        ungrouped: typing.Optional[bool] = None,
        keyword: typing.Optional[str] = None,
        accepts: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AttachmentList:
        """
        List attachments of the current user uploaded.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number. Default is 0.

        size : typing.Optional[int]
            Size number. Default is 0.

        label_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Label selector. e.g.: hidden!=true

        field_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Field selector. e.g.: metadata.name==halo

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        ungrouped : typing.Optional[bool]
            Filter attachments without group. This parameter will ignore group parameter.

        keyword : typing.Optional[str]
            Keyword for searching.

        accepts : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Acceptable media types.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttachmentList
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.attachment_v1alpha1uc.list_my_attachments()
        """
        _response = self._raw_client.list_my_attachments(
            page=page,
            size=size,
            label_selector=label_selector,
            field_selector=field_selector,
            sort=sort,
            ungrouped=ungrouped,
            keyword=keyword,
            accepts=accepts,
            request_options=request_options,
        )
        return _response.data

    def create_attachment_for_post(
        self,
        *,
        file: core.File,
        wait_for_permalink: typing.Optional[bool] = None,
        post_name: typing.Optional[str] = OMIT,
        single_page_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Attachment:
        """
        Create attachment for the given post. Deprecated in favor of /attachments/-/upload.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        wait_for_permalink : typing.Optional[bool]
            Wait for permalink.

        post_name : typing.Optional[str]
            post <code>metadata.name</code>

        single_page_name : typing.Optional[str]
            single page <code>metadata.name</code>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Attachment
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.attachment_v1alpha1uc.create_attachment_for_post()
        """
        _response = self._raw_client.create_attachment_for_post(
            file=file,
            wait_for_permalink=wait_for_permalink,
            post_name=post_name,
            single_page_name=single_page_name,
            request_options=request_options,
        )
        return _response.data

    def match_attachment_permalinks_for_uc(
        self, *, urls: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> AttachmentPermalinkMatchList:
        """
        Match URL strings against Attachment permalinks for user center.

        Parameters
        ----------
        urls : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttachmentPermalinkMatchList
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.attachment_v1alpha1uc.match_attachment_permalinks_for_uc(
            urls=["urls"],
        )
        """
        _response = self._raw_client.match_attachment_permalinks_for_uc(urls=urls, request_options=request_options)
        return _response.data

    def upload_attachment_for_uc(
        self,
        *,
        file: typing.Optional[core.File] = OMIT,
        filename: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Attachment:
        """
        Upload attachment to user center storage.

        Parameters
        ----------
        file : typing.Optional[core.File]
            See core.File for more documentation

        filename : typing.Optional[str]
            The filename to use when uploading from url. If not provided, the filename will be extracted from the url.

        url : typing.Optional[str]
            The url to upload from. If not provided, the file will be used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Attachment
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.attachment_v1alpha1uc.upload_attachment_for_uc()
        """
        _response = self._raw_client.upload_attachment_for_uc(
            file=file, filename=filename, url=url, request_options=request_options
        )
        return _response.data

    def external_transfer_attachment1(
        self,
        *,
        url: str,
        wait_for_permalink: typing.Optional[bool] = None,
        filename: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Attachment:
        """
        Upload attachment from the given URL.
        Deprecated in favor of /attachments/-/upload.

        Parameters
        ----------
        url : str
            remote file URL to transfer into user-center storage

        wait_for_permalink : typing.Optional[bool]
            Wait for permalink.

        filename : typing.Optional[str]
            custom file name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Attachment
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.attachment_v1alpha1uc.external_transfer_attachment1(
            url="url",
        )
        """
        _response = self._raw_client.external_transfer_attachment1(
            url=url, wait_for_permalink=wait_for_permalink, filename=filename, request_options=request_options
        )
        return _response.data


class AsyncAttachmentV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAttachmentV1Alpha1UcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAttachmentV1Alpha1UcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAttachmentV1Alpha1UcClient
        """
        return self._raw_client

    async def list_my_attachments(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        ungrouped: typing.Optional[bool] = None,
        keyword: typing.Optional[str] = None,
        accepts: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AttachmentList:
        """
        List attachments of the current user uploaded.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number. Default is 0.

        size : typing.Optional[int]
            Size number. Default is 0.

        label_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Label selector. e.g.: hidden!=true

        field_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Field selector. e.g.: metadata.name==halo

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        ungrouped : typing.Optional[bool]
            Filter attachments without group. This parameter will ignore group parameter.

        keyword : typing.Optional[str]
            Keyword for searching.

        accepts : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Acceptable media types.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttachmentList
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.attachment_v1alpha1uc.list_my_attachments()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_my_attachments(
            page=page,
            size=size,
            label_selector=label_selector,
            field_selector=field_selector,
            sort=sort,
            ungrouped=ungrouped,
            keyword=keyword,
            accepts=accepts,
            request_options=request_options,
        )
        return _response.data

    async def create_attachment_for_post(
        self,
        *,
        file: core.File,
        wait_for_permalink: typing.Optional[bool] = None,
        post_name: typing.Optional[str] = OMIT,
        single_page_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Attachment:
        """
        Create attachment for the given post. Deprecated in favor of /attachments/-/upload.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        wait_for_permalink : typing.Optional[bool]
            Wait for permalink.

        post_name : typing.Optional[str]
            post <code>metadata.name</code>

        single_page_name : typing.Optional[str]
            single page <code>metadata.name</code>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Attachment
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.attachment_v1alpha1uc.create_attachment_for_post()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_attachment_for_post(
            file=file,
            wait_for_permalink=wait_for_permalink,
            post_name=post_name,
            single_page_name=single_page_name,
            request_options=request_options,
        )
        return _response.data

    async def match_attachment_permalinks_for_uc(
        self, *, urls: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> AttachmentPermalinkMatchList:
        """
        Match URL strings against Attachment permalinks for user center.

        Parameters
        ----------
        urls : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttachmentPermalinkMatchList
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.attachment_v1alpha1uc.match_attachment_permalinks_for_uc(
                urls=["urls"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.match_attachment_permalinks_for_uc(
            urls=urls, request_options=request_options
        )
        return _response.data

    async def upload_attachment_for_uc(
        self,
        *,
        file: typing.Optional[core.File] = OMIT,
        filename: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Attachment:
        """
        Upload attachment to user center storage.

        Parameters
        ----------
        file : typing.Optional[core.File]
            See core.File for more documentation

        filename : typing.Optional[str]
            The filename to use when uploading from url. If not provided, the filename will be extracted from the url.

        url : typing.Optional[str]
            The url to upload from. If not provided, the file will be used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Attachment
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.attachment_v1alpha1uc.upload_attachment_for_uc()


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_attachment_for_uc(
            file=file, filename=filename, url=url, request_options=request_options
        )
        return _response.data

    async def external_transfer_attachment1(
        self,
        *,
        url: str,
        wait_for_permalink: typing.Optional[bool] = None,
        filename: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Attachment:
        """
        Upload attachment from the given URL.
        Deprecated in favor of /attachments/-/upload.

        Parameters
        ----------
        url : str
            remote file URL to transfer into user-center storage

        wait_for_permalink : typing.Optional[bool]
            Wait for permalink.

        filename : typing.Optional[str]
            custom file name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Attachment
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.attachment_v1alpha1uc.external_transfer_attachment1(
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.external_transfer_attachment1(
            url=url, wait_for_permalink=wait_for_permalink, filename=filename, request_options=request_options
        )
        return _response.data
