

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.anchore_image_tag_summary_list import AnchoreImageTagSummaryList
from .raw_client import AsyncRawSummariesClient, RawSummariesClient
from .types.list_imagetags_request_image_status_item import ListImagetagsRequestImageStatusItem


class SummariesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSummariesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSummariesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSummariesClient
        """
        return self._raw_client

    def list_imagetags(
        self,
        *,
        image_status: typing.Optional[
            typing.Union[ListImagetagsRequestImageStatusItem, typing.Sequence[ListImagetagsRequestImageStatusItem]]
        ] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AnchoreImageTagSummaryList:
        """
        List all image tags visible to the user

        Parameters
        ----------
        image_status : typing.Optional[typing.Union[ListImagetagsRequestImageStatusItem, typing.Sequence[ListImagetagsRequestImageStatusItem]]]
            Filter images in one or more states such as active, deleting. Defaults to active images only if unspecified

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnchoreImageTagSummaryList
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.summaries.list_imagetags()
        """
        _response = self._raw_client.list_imagetags(
            image_status=image_status, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data


class AsyncSummariesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSummariesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSummariesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSummariesClient
        """
        return self._raw_client

    async def list_imagetags(
        self,
        *,
        image_status: typing.Optional[
            typing.Union[ListImagetagsRequestImageStatusItem, typing.Sequence[ListImagetagsRequestImageStatusItem]]
        ] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AnchoreImageTagSummaryList:
        """
        List all image tags visible to the user

        Parameters
        ----------
        image_status : typing.Optional[typing.Union[ListImagetagsRequestImageStatusItem, typing.Sequence[ListImagetagsRequestImageStatusItem]]]
            Filter images in one or more states such as active, deleting. Defaults to active images only if unspecified

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnchoreImageTagSummaryList
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.summaries.list_imagetags()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_imagetags(
            image_status=image_status, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data
