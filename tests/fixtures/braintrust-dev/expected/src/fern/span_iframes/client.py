

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_limit_param import AppLimitParam
from ..types.ending_before import EndingBefore
from ..types.ids import Ids
from ..types.org_name import OrgName
from ..types.span_i_frame import SpanIFrame
from ..types.span_iframe_id_param import SpanIframeIdParam
from ..types.span_iframe_name import SpanIframeName
from ..types.starting_after import StartingAfter
from .raw_client import AsyncRawSpanIframesClient, RawSpanIframesClient
from .types.get_span_iframe_response import GetSpanIframeResponse


OMIT = typing.cast(typing.Any, ...)


class SpanIframesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSpanIframesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSpanIframesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSpanIframesClient
        """
        return self._raw_client

    def get_span_iframe(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        span_iframe_name: typing.Optional[SpanIframeName] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetSpanIframeResponse:
        """
        List out all span_iframes. The span_iframes are sorted by creation date, with the most recently-created span_iframes coming first

        Parameters
        ----------
        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        span_iframe_name : typing.Optional[SpanIframeName]
            Name of the span_iframe to search for

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSpanIframeResponse
            Returns a list of span_iframe objects

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.span_iframes.get_span_iframe()
        """
        _response = self._raw_client.get_span_iframe(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            span_iframe_name=span_iframe_name,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    def post_span_iframe(
        self,
        *,
        project_id: str,
        name: str,
        url: str,
        description: typing.Optional[str] = OMIT,
        post_message: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SpanIFrame:
        """
        Create a new span_iframe. If there is an existing span_iframe with the same name as the one specified in the request, will return the existing span_iframe unmodified

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the span iframe belongs under

        name : str
            Name of the span iframe

        url : str
            URL to embed the project viewer in an iframe

        description : typing.Optional[str]
            Textual description of the span iframe

        post_message : typing.Optional[bool]
            Whether to post messages to the iframe containing the span's data. This is useful when you want to render more data than fits in the URL.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpanIFrame
            Returns the new span_iframe object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.span_iframes.post_span_iframe(
            project_id="project_id",
            name="name",
            url="url",
        )
        """
        _response = self._raw_client.post_span_iframe(
            project_id=project_id,
            name=name,
            url=url,
            description=description,
            post_message=post_message,
            request_options=request_options,
        )
        return _response.data

    def put_span_iframe(
        self,
        *,
        project_id: str,
        name: str,
        url: str,
        description: typing.Optional[str] = OMIT,
        post_message: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SpanIFrame:
        """
        Create or replace span_iframe. If there is an existing span_iframe with the same name as the one specified in the request, will replace the existing span_iframe with the provided fields

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the span iframe belongs under

        name : str
            Name of the span iframe

        url : str
            URL to embed the project viewer in an iframe

        description : typing.Optional[str]
            Textual description of the span iframe

        post_message : typing.Optional[bool]
            Whether to post messages to the iframe containing the span's data. This is useful when you want to render more data than fits in the URL.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpanIFrame
            Returns the new span_iframe object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.span_iframes.put_span_iframe(
            project_id="project_id",
            name="name",
            url="url",
        )
        """
        _response = self._raw_client.put_span_iframe(
            project_id=project_id,
            name=name,
            url=url,
            description=description,
            post_message=post_message,
            request_options=request_options,
        )
        return _response.data

    def get_span_iframe_id(
        self, span_iframe_id: SpanIframeIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SpanIFrame:
        """
        Get a span_iframe object by its id

        Parameters
        ----------
        span_iframe_id : SpanIframeIdParam
            SpanIframe id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpanIFrame
            Returns the span_iframe object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.span_iframes.get_span_iframe_id(
            span_iframe_id="span_iframe_id",
        )
        """
        _response = self._raw_client.get_span_iframe_id(span_iframe_id, request_options=request_options)
        return _response.data

    def delete_span_iframe_id(
        self, span_iframe_id: SpanIframeIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SpanIFrame:
        """
        Delete a span_iframe object by its id

        Parameters
        ----------
        span_iframe_id : SpanIframeIdParam
            SpanIframe id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpanIFrame
            Returns the deleted span_iframe object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.span_iframes.delete_span_iframe_id(
            span_iframe_id="span_iframe_id",
        )
        """
        _response = self._raw_client.delete_span_iframe_id(span_iframe_id, request_options=request_options)
        return _response.data

    def patch_span_iframe_id(
        self,
        span_iframe_id: SpanIframeIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        post_message: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SpanIFrame:
        """
        Partially update a span_iframe object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        span_iframe_id : SpanIframeIdParam
            SpanIframe id

        name : typing.Optional[str]
            Name of the span iframe

        url : typing.Optional[str]
            URL to embed the project viewer in an iframe

        post_message : typing.Optional[bool]
            Whether to post messages to the iframe containing the span's data. This is useful when you want to render more data than fits in the URL.

        description : typing.Optional[str]
            Textual description of the span iframe

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpanIFrame
            Returns the span_iframe object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.span_iframes.patch_span_iframe_id(
            span_iframe_id="span_iframe_id",
        )
        """
        _response = self._raw_client.patch_span_iframe_id(
            span_iframe_id,
            name=name,
            url=url,
            post_message=post_message,
            description=description,
            request_options=request_options,
        )
        return _response.data


class AsyncSpanIframesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSpanIframesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSpanIframesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSpanIframesClient
        """
        return self._raw_client

    async def get_span_iframe(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        span_iframe_name: typing.Optional[SpanIframeName] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetSpanIframeResponse:
        """
        List out all span_iframes. The span_iframes are sorted by creation date, with the most recently-created span_iframes coming first

        Parameters
        ----------
        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        span_iframe_name : typing.Optional[SpanIframeName]
            Name of the span_iframe to search for

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSpanIframeResponse
            Returns a list of span_iframe objects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.span_iframes.get_span_iframe()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_span_iframe(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            span_iframe_name=span_iframe_name,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    async def post_span_iframe(
        self,
        *,
        project_id: str,
        name: str,
        url: str,
        description: typing.Optional[str] = OMIT,
        post_message: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SpanIFrame:
        """
        Create a new span_iframe. If there is an existing span_iframe with the same name as the one specified in the request, will return the existing span_iframe unmodified

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the span iframe belongs under

        name : str
            Name of the span iframe

        url : str
            URL to embed the project viewer in an iframe

        description : typing.Optional[str]
            Textual description of the span iframe

        post_message : typing.Optional[bool]
            Whether to post messages to the iframe containing the span's data. This is useful when you want to render more data than fits in the URL.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpanIFrame
            Returns the new span_iframe object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.span_iframes.post_span_iframe(
                project_id="project_id",
                name="name",
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_span_iframe(
            project_id=project_id,
            name=name,
            url=url,
            description=description,
            post_message=post_message,
            request_options=request_options,
        )
        return _response.data

    async def put_span_iframe(
        self,
        *,
        project_id: str,
        name: str,
        url: str,
        description: typing.Optional[str] = OMIT,
        post_message: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SpanIFrame:
        """
        Create or replace span_iframe. If there is an existing span_iframe with the same name as the one specified in the request, will replace the existing span_iframe with the provided fields

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the span iframe belongs under

        name : str
            Name of the span iframe

        url : str
            URL to embed the project viewer in an iframe

        description : typing.Optional[str]
            Textual description of the span iframe

        post_message : typing.Optional[bool]
            Whether to post messages to the iframe containing the span's data. This is useful when you want to render more data than fits in the URL.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpanIFrame
            Returns the new span_iframe object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.span_iframes.put_span_iframe(
                project_id="project_id",
                name="name",
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_span_iframe(
            project_id=project_id,
            name=name,
            url=url,
            description=description,
            post_message=post_message,
            request_options=request_options,
        )
        return _response.data

    async def get_span_iframe_id(
        self, span_iframe_id: SpanIframeIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SpanIFrame:
        """
        Get a span_iframe object by its id

        Parameters
        ----------
        span_iframe_id : SpanIframeIdParam
            SpanIframe id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpanIFrame
            Returns the span_iframe object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.span_iframes.get_span_iframe_id(
                span_iframe_id="span_iframe_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_span_iframe_id(span_iframe_id, request_options=request_options)
        return _response.data

    async def delete_span_iframe_id(
        self, span_iframe_id: SpanIframeIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SpanIFrame:
        """
        Delete a span_iframe object by its id

        Parameters
        ----------
        span_iframe_id : SpanIframeIdParam
            SpanIframe id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpanIFrame
            Returns the deleted span_iframe object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.span_iframes.delete_span_iframe_id(
                span_iframe_id="span_iframe_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_span_iframe_id(span_iframe_id, request_options=request_options)
        return _response.data

    async def patch_span_iframe_id(
        self,
        span_iframe_id: SpanIframeIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        post_message: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SpanIFrame:
        """
        Partially update a span_iframe object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        span_iframe_id : SpanIframeIdParam
            SpanIframe id

        name : typing.Optional[str]
            Name of the span iframe

        url : typing.Optional[str]
            URL to embed the project viewer in an iframe

        post_message : typing.Optional[bool]
            Whether to post messages to the iframe containing the span's data. This is useful when you want to render more data than fits in the URL.

        description : typing.Optional[str]
            Textual description of the span iframe

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpanIFrame
            Returns the span_iframe object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.span_iframes.patch_span_iframe_id(
                span_iframe_id="span_iframe_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_span_iframe_id(
            span_iframe_id,
            name=name,
            url=url,
            post_message=post_message,
            description=description,
            request_options=request_options,
        )
        return _response.data
