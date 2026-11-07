

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.attachment import Attachment
from ..types.attachment_list import AttachmentList
from ..types.attachment_permalink_match_list import AttachmentPermalinkMatchList
from .raw_client import AsyncRawAttachmentV1Alpha1ConsoleClient, RawAttachmentV1Alpha1ConsoleClient


OMIT = typing.cast(typing.Any, ...)


class AttachmentV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAttachmentV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAttachmentV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAttachmentV1Alpha1ConsoleClient
        """
        return self._raw_client

    def search_attachments(
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
        Search attachments with pagination, sorting, keyword, grouping, and media type filters.

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
        client.attachment_v1alpha1console.search_attachments()
        """
        _response = self._raw_client.search_attachments(
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

    def external_transfer_attachment(
        self,
        *,
        policy_name: str,
        url: str,
        filename: typing.Optional[str] = OMIT,
        group_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Attachment:
        """
        Create an attachment by transferring a remote file from the provided URL to the specified storage policy.

        Parameters
        ----------
        policy_name : str
            storage policy <code>metadata.name</code>

        url : str
            remote file URL to transfer into storage

        filename : typing.Optional[str]
            custom file name

        group_name : typing.Optional[str]
            attachment group <code>metadata.name</code>

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
        client.attachment_v1alpha1console.external_transfer_attachment(
            policy_name="policyName",
            url="url",
        )
        """
        _response = self._raw_client.external_transfer_attachment(
            policy_name=policy_name, url=url, filename=filename, group_name=group_name, request_options=request_options
        )
        return _response.data

    def upload_attachment(
        self,
        *,
        file: core.File,
        policy_name: str,
        group_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Attachment:
        """
        Upload an attachment from a multipart file with the specified storage policy and optional group.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        policy_name : str
            Storage policy <code>metadata.name</code>.

        group_name : typing.Optional[str]
            Attachment group <code>metadata.name</code>.

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
        client.attachment_v1alpha1console.upload_attachment(
            policy_name="policyName",
        )
        """
        _response = self._raw_client.upload_attachment(
            file=file, policy_name=policy_name, group_name=group_name, request_options=request_options
        )
        return _response.data

    def match_attachment_permalinks_for_console(
        self, *, urls: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> AttachmentPermalinkMatchList:
        """
        Match URL strings against Attachment permalinks for console.

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
        client.attachment_v1alpha1console.match_attachment_permalinks_for_console(
            urls=["urls"],
        )
        """
        _response = self._raw_client.match_attachment_permalinks_for_console(urls=urls, request_options=request_options)
        return _response.data

    def upload_attachment_for_console(
        self,
        *,
        file: typing.Optional[core.File] = OMIT,
        filename: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Attachment:
        """
        Upload attachment endpoint for console.

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
        client.attachment_v1alpha1console.upload_attachment_for_console()
        """
        _response = self._raw_client.upload_attachment_for_console(
            file=file, filename=filename, url=url, request_options=request_options
        )
        return _response.data


class AsyncAttachmentV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAttachmentV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAttachmentV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAttachmentV1Alpha1ConsoleClient
        """
        return self._raw_client

    async def search_attachments(
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
        Search attachments with pagination, sorting, keyword, grouping, and media type filters.

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
            await client.attachment_v1alpha1console.search_attachments()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_attachments(
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

    async def external_transfer_attachment(
        self,
        *,
        policy_name: str,
        url: str,
        filename: typing.Optional[str] = OMIT,
        group_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Attachment:
        """
        Create an attachment by transferring a remote file from the provided URL to the specified storage policy.

        Parameters
        ----------
        policy_name : str
            storage policy <code>metadata.name</code>

        url : str
            remote file URL to transfer into storage

        filename : typing.Optional[str]
            custom file name

        group_name : typing.Optional[str]
            attachment group <code>metadata.name</code>

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
            await client.attachment_v1alpha1console.external_transfer_attachment(
                policy_name="policyName",
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.external_transfer_attachment(
            policy_name=policy_name, url=url, filename=filename, group_name=group_name, request_options=request_options
        )
        return _response.data

    async def upload_attachment(
        self,
        *,
        file: core.File,
        policy_name: str,
        group_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Attachment:
        """
        Upload an attachment from a multipart file with the specified storage policy and optional group.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        policy_name : str
            Storage policy <code>metadata.name</code>.

        group_name : typing.Optional[str]
            Attachment group <code>metadata.name</code>.

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
            await client.attachment_v1alpha1console.upload_attachment(
                policy_name="policyName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_attachment(
            file=file, policy_name=policy_name, group_name=group_name, request_options=request_options
        )
        return _response.data

    async def match_attachment_permalinks_for_console(
        self, *, urls: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> AttachmentPermalinkMatchList:
        """
        Match URL strings against Attachment permalinks for console.

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
            await client.attachment_v1alpha1console.match_attachment_permalinks_for_console(
                urls=["urls"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.match_attachment_permalinks_for_console(
            urls=urls, request_options=request_options
        )
        return _response.data

    async def upload_attachment_for_console(
        self,
        *,
        file: typing.Optional[core.File] = OMIT,
        filename: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Attachment:
        """
        Upload attachment endpoint for console.

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
            await client.attachment_v1alpha1console.upload_attachment_for_console()


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_attachment_for_console(
            file=file, filename=filename, url=url, request_options=request_options
        )
        return _response.data
