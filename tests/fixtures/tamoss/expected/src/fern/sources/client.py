

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.content_format import ContentFormat
from ..types.source import Source
from ..types.tags import Tags
from ..types.url_tag_list import UrlTagList
from ..types.uuid_ import Uuid
from .raw_client import AsyncRawSourcesClient, RawSourcesClient


OMIT = typing.cast(typing.Any, ...)


class SourcesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSourcesClient
        """
        return self._raw_client

    def get_sources(
        self,
        *,
        label: typing.Optional[str] = None,
        tag_name: typing.Optional[UrlTagList] = None,
        tag_exists_name: typing.Optional[bool] = None,
        format: typing.Optional[ContentFormat] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Source]:
        """
        List the Sources registered in the TAMS service instance and their details.

        Parameters
        ----------
        label : typing.Optional[str]
            Filter on Sources that have the given label.

        tag_name : typing.Optional[UrlTagList]
            Filter on Sources that have a tag named {name} with a value in the given comma-separated list of values.
            The {name} and the value MUST be URL encoded where special characters are present.
            Where the tag's value is a string, at least one of the given values will match.
            Where the tag's value is an array, at least one value in the array will match at least one of the given values.
            Partial string matches of the values are not valid.

        tag_exists_name : typing.Optional[bool]
            Filter on Sources that have a tag named {name} regardless of value.
            {name} MUST be URL encoded where special characters are present.
            If set to true then the presence of the tag is filtered for.
            If set to false then its absence is.
            If left out then no filtering on tag presence is performed.

        format : typing.Optional[ContentFormat]
            Filter on Source format.

        page : typing.Optional[str]
            Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.

        limit : typing.Optional[int]
            Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Source]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.sources.get_sources()
        """
        _response = self._raw_client.get_sources(
            label=label,
            tag_name=tag_name,
            tag_exists_name=tag_exists_name,
            format=format,
            page=page,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    def head_sources(
        self,
        *,
        label: typing.Optional[str] = None,
        tag_name: typing.Optional[UrlTagList] = None,
        tag_exists_name: typing.Optional[bool] = None,
        format: typing.Optional[ContentFormat] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Return Sources path headers

        Parameters
        ----------
        label : typing.Optional[str]
            Filter on Sources that have the given label.

        tag_name : typing.Optional[UrlTagList]
            Filter on Sources that have a tag named {name} with a value in the given comma-separated list of values.
            The {name} and the value MUST be URL encoded where special characters are present.
            Where the tag's value is a string, at least one of the given values will match.
            Where the tag's value is an array, at least one value in the array will match at least one of the given values.
            Partial string matches of the values are not valid.

        tag_exists_name : typing.Optional[bool]
            Filter on Sources that have a tag named {name} regardless of value.
            {name} MUST be URL encoded where special characters are present.
            If set to true then the presence of the tag is filtered for.
            If set to false then its absence is.
            If left out then no filtering on tag presence is performed.

        format : typing.Optional[ContentFormat]
            Filter on Source format.

        page : typing.Optional[str]
            Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.

        limit : typing.Optional[int]
            Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.sources.head_sources()
        """
        _response = self._raw_client.head_sources(
            label=label,
            tag_name=tag_name,
            tag_exists_name=tag_exists_name,
            format=format,
            page=page,
            limit=limit,
            request_options=request_options,
        )
        return _response.headers

    def get_sources_source_id(
        self, source_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Source:
        """
        Returns Source metadata.

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Source


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.sources.get_sources_source_id(
            source_id="sourceId",
        )
        """
        _response = self._raw_client.get_sources_source_id(source_id, request_options=request_options)
        return _response.data

    def head_sources_source_id(
        self, source_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return Source headers

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.sources.head_sources_source_id(
            source_id="sourceId",
        )
        """
        _response = self._raw_client.head_sources_source_id(source_id, request_options=request_options)
        return _response.headers

    def get_sources_source_id_tags(
        self, source_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Tags:
        """
        Returns the Source tags.

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tags


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.sources.get_sources_source_id_tags(
            source_id="sourceId",
        )
        """
        _response = self._raw_client.get_sources_source_id_tags(source_id, request_options=request_options)
        return _response.data

    def head_sources_source_id_tags(
        self, source_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return Source tags path headers

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.sources.head_sources_source_id_tags(
            source_id="sourceId",
        )
        """
        _response = self._raw_client.head_sources_source_id_tags(source_id, request_options=request_options)
        return _response.headers

    def get_sources_source_id_tags_name(
        self, source_id: Uuid, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Return the tag value associated with the tag name.

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        name : str
            The tag name. {name} MUST be URL encoded where special characters are present.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.sources.get_sources_source_id_tags_name(
            source_id="sourceId",
            name="name",
        )
        """
        _response = self._raw_client.get_sources_source_id_tags_name(source_id, name, request_options=request_options)
        return _response.data

    def put_sources_source_id_tags_name(
        self, source_id: Uuid, name: str, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Create or update the Source tag

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        name : str
            The tag name. {name} MUST be URL encoded where special characters are present.

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.sources.put_sources_source_id_tags_name(
            source_id="sourceId",
            name="name",
            request='"new_value"\n',
        )
        """
        _response = self._raw_client.put_sources_source_id_tags_name(
            source_id, name, request=request, request_options=request_options
        )
        return _response.data

    def delete_sources_source_id_tags_name(
        self, source_id: Uuid, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a specific tag on a Source

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        name : str
            The tag name. {name} MUST be URL encoded where special characters are present.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.sources.delete_sources_source_id_tags_name(
            source_id="sourceId",
            name="name",
        )
        """
        _response = self._raw_client.delete_sources_source_id_tags_name(
            source_id, name, request_options=request_options
        )
        return _response.data

    def head_sources_source_id_tags_name(
        self, source_id: Uuid, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return Source tag path headers

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        name : str
            The tag name. {name} MUST be URL encoded where special characters are present.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.sources.head_sources_source_id_tags_name(
            source_id="sourceId",
            name="name",
        )
        """
        _response = self._raw_client.head_sources_source_id_tags_name(source_id, name, request_options=request_options)
        return _response.headers

    def get_sources_source_id_description(
        self, source_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Returns the Source description property. This should be a human-readable description that may be showed in detailed views of Sources. The description should be longer and more detailed than `label`.

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.sources.get_sources_source_id_description(
            source_id="sourceId",
        )
        """
        _response = self._raw_client.get_sources_source_id_description(source_id, request_options=request_options)
        return _response.data

    def put_sources_source_id_description(
        self, source_id: Uuid, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Create or update the description property. This should be a human-readable description that may be showed in detailed views of Sources. The description should be longer and more detailed than `label`.

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.sources.put_sources_source_id_description(
            source_id="sourceId",
            request='"Big Buck Bunny Movie"\n',
        )
        """
        _response = self._raw_client.put_sources_source_id_description(
            source_id, request=request, request_options=request_options
        )
        return _response.data

    def delete_sources_source_id_description(
        self, source_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete the description property.

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.sources.delete_sources_source_id_description(
            source_id="sourceId",
        )
        """
        _response = self._raw_client.delete_sources_source_id_description(source_id, request_options=request_options)
        return _response.data

    def head_sources_source_id_description(
        self, source_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return Source description path headers

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.sources.head_sources_source_id_description(
            source_id="sourceId",
        )
        """
        _response = self._raw_client.head_sources_source_id_description(source_id, request_options=request_options)
        return _response.headers

    def get_sources_source_id_label(
        self, source_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Returns the Source label property. This should be a very short, human-readable label that may be displayed in listings of Sources.

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.sources.get_sources_source_id_label(
            source_id="sourceId",
        )
        """
        _response = self._raw_client.get_sources_source_id_label(source_id, request_options=request_options)
        return _response.data

    def put_sources_source_id_label(
        self, source_id: Uuid, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Create or update the label property. This should be a very short, human-readable label that may be displayed in listings of Sources.

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.sources.put_sources_source_id_label(
            source_id="sourceId",
            request='"Big Buck Bunny Movie"\n',
        )
        """
        _response = self._raw_client.put_sources_source_id_label(
            source_id, request=request, request_options=request_options
        )
        return _response.data

    def delete_sources_source_id_label(
        self, source_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete the label property.

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.sources.delete_sources_source_id_label(
            source_id="sourceId",
        )
        """
        _response = self._raw_client.delete_sources_source_id_label(source_id, request_options=request_options)
        return _response.data

    def head_sources_source_id_label(
        self, source_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return Source label path headers

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.sources.head_sources_source_id_label(
            source_id="sourceId",
        )
        """
        _response = self._raw_client.head_sources_source_id_label(source_id, request_options=request_options)
        return _response.headers


class AsyncSourcesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSourcesClient
        """
        return self._raw_client

    async def get_sources(
        self,
        *,
        label: typing.Optional[str] = None,
        tag_name: typing.Optional[UrlTagList] = None,
        tag_exists_name: typing.Optional[bool] = None,
        format: typing.Optional[ContentFormat] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Source]:
        """
        List the Sources registered in the TAMS service instance and their details.

        Parameters
        ----------
        label : typing.Optional[str]
            Filter on Sources that have the given label.

        tag_name : typing.Optional[UrlTagList]
            Filter on Sources that have a tag named {name} with a value in the given comma-separated list of values.
            The {name} and the value MUST be URL encoded where special characters are present.
            Where the tag's value is a string, at least one of the given values will match.
            Where the tag's value is an array, at least one value in the array will match at least one of the given values.
            Partial string matches of the values are not valid.

        tag_exists_name : typing.Optional[bool]
            Filter on Sources that have a tag named {name} regardless of value.
            {name} MUST be URL encoded where special characters are present.
            If set to true then the presence of the tag is filtered for.
            If set to false then its absence is.
            If left out then no filtering on tag presence is performed.

        format : typing.Optional[ContentFormat]
            Filter on Source format.

        page : typing.Optional[str]
            Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.

        limit : typing.Optional[int]
            Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Source]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.sources.get_sources()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sources(
            label=label,
            tag_name=tag_name,
            tag_exists_name=tag_exists_name,
            format=format,
            page=page,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    async def head_sources(
        self,
        *,
        label: typing.Optional[str] = None,
        tag_name: typing.Optional[UrlTagList] = None,
        tag_exists_name: typing.Optional[bool] = None,
        format: typing.Optional[ContentFormat] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Return Sources path headers

        Parameters
        ----------
        label : typing.Optional[str]
            Filter on Sources that have the given label.

        tag_name : typing.Optional[UrlTagList]
            Filter on Sources that have a tag named {name} with a value in the given comma-separated list of values.
            The {name} and the value MUST be URL encoded where special characters are present.
            Where the tag's value is a string, at least one of the given values will match.
            Where the tag's value is an array, at least one value in the array will match at least one of the given values.
            Partial string matches of the values are not valid.

        tag_exists_name : typing.Optional[bool]
            Filter on Sources that have a tag named {name} regardless of value.
            {name} MUST be URL encoded where special characters are present.
            If set to true then the presence of the tag is filtered for.
            If set to false then its absence is.
            If left out then no filtering on tag presence is performed.

        format : typing.Optional[ContentFormat]
            Filter on Source format.

        page : typing.Optional[str]
            Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.

        limit : typing.Optional[int]
            Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.sources.head_sources()


        asyncio.run(main())
        """
        _response = await self._raw_client.head_sources(
            label=label,
            tag_name=tag_name,
            tag_exists_name=tag_exists_name,
            format=format,
            page=page,
            limit=limit,
            request_options=request_options,
        )
        return _response.headers

    async def get_sources_source_id(
        self, source_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Source:
        """
        Returns Source metadata.

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Source


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.sources.get_sources_source_id(
                source_id="sourceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sources_source_id(source_id, request_options=request_options)
        return _response.data

    async def head_sources_source_id(
        self, source_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return Source headers

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.sources.head_sources_source_id(
                source_id="sourceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_sources_source_id(source_id, request_options=request_options)
        return _response.headers

    async def get_sources_source_id_tags(
        self, source_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Tags:
        """
        Returns the Source tags.

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tags


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.sources.get_sources_source_id_tags(
                source_id="sourceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sources_source_id_tags(source_id, request_options=request_options)
        return _response.data

    async def head_sources_source_id_tags(
        self, source_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return Source tags path headers

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.sources.head_sources_source_id_tags(
                source_id="sourceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_sources_source_id_tags(source_id, request_options=request_options)
        return _response.headers

    async def get_sources_source_id_tags_name(
        self, source_id: Uuid, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Return the tag value associated with the tag name.

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        name : str
            The tag name. {name} MUST be URL encoded where special characters are present.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.sources.get_sources_source_id_tags_name(
                source_id="sourceId",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sources_source_id_tags_name(
            source_id, name, request_options=request_options
        )
        return _response.data

    async def put_sources_source_id_tags_name(
        self, source_id: Uuid, name: str, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Create or update the Source tag

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        name : str
            The tag name. {name} MUST be URL encoded where special characters are present.

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.sources.put_sources_source_id_tags_name(
                source_id="sourceId",
                name="name",
                request='"new_value"\n',
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_sources_source_id_tags_name(
            source_id, name, request=request, request_options=request_options
        )
        return _response.data

    async def delete_sources_source_id_tags_name(
        self, source_id: Uuid, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a specific tag on a Source

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        name : str
            The tag name. {name} MUST be URL encoded where special characters are present.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.sources.delete_sources_source_id_tags_name(
                source_id="sourceId",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_sources_source_id_tags_name(
            source_id, name, request_options=request_options
        )
        return _response.data

    async def head_sources_source_id_tags_name(
        self, source_id: Uuid, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return Source tag path headers

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        name : str
            The tag name. {name} MUST be URL encoded where special characters are present.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.sources.head_sources_source_id_tags_name(
                source_id="sourceId",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_sources_source_id_tags_name(
            source_id, name, request_options=request_options
        )
        return _response.headers

    async def get_sources_source_id_description(
        self, source_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Returns the Source description property. This should be a human-readable description that may be showed in detailed views of Sources. The description should be longer and more detailed than `label`.

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.sources.get_sources_source_id_description(
                source_id="sourceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sources_source_id_description(source_id, request_options=request_options)
        return _response.data

    async def put_sources_source_id_description(
        self, source_id: Uuid, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Create or update the description property. This should be a human-readable description that may be showed in detailed views of Sources. The description should be longer and more detailed than `label`.

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.sources.put_sources_source_id_description(
                source_id="sourceId",
                request='"Big Buck Bunny Movie"\n',
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_sources_source_id_description(
            source_id, request=request, request_options=request_options
        )
        return _response.data

    async def delete_sources_source_id_description(
        self, source_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete the description property.

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.sources.delete_sources_source_id_description(
                source_id="sourceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_sources_source_id_description(
            source_id, request_options=request_options
        )
        return _response.data

    async def head_sources_source_id_description(
        self, source_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return Source description path headers

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.sources.head_sources_source_id_description(
                source_id="sourceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_sources_source_id_description(
            source_id, request_options=request_options
        )
        return _response.headers

    async def get_sources_source_id_label(
        self, source_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Returns the Source label property. This should be a very short, human-readable label that may be displayed in listings of Sources.

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.sources.get_sources_source_id_label(
                source_id="sourceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sources_source_id_label(source_id, request_options=request_options)
        return _response.data

    async def put_sources_source_id_label(
        self, source_id: Uuid, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Create or update the label property. This should be a very short, human-readable label that may be displayed in listings of Sources.

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.sources.put_sources_source_id_label(
                source_id="sourceId",
                request='"Big Buck Bunny Movie"\n',
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_sources_source_id_label(
            source_id, request=request, request_options=request_options
        )
        return _response.data

    async def delete_sources_source_id_label(
        self, source_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete the label property.

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.sources.delete_sources_source_id_label(
                source_id="sourceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_sources_source_id_label(source_id, request_options=request_options)
        return _response.data

    async def head_sources_source_id_label(
        self, source_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return Source label path headers

        Parameters
        ----------
        source_id : Uuid
            The Source identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.sources.head_sources_source_id_label(
                source_id="sourceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_sources_source_id_label(source_id, request_options=request_options)
        return _response.headers
