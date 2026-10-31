

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.axis_section_treeless import AxisSectionTreeless
from .raw_client import AsyncRawAxisSectionsClient, RawAxisSectionsClient
from .types.get_api_v3axes_response import GetApiV3AxesResponse
from .types.get_api_v3axis_sections_axis_section_id_response import GetApiV3AxisSectionsAxisSectionIdResponse
from .types.get_api_v3axissections_response import GetApiV3AxissectionsResponse
from .types.post_api_v3axis_sections_response import PostApiV3AxisSectionsResponse
from .types.put_api_v3axis_sections_axis_section_id_response import PutApiV3AxisSectionsAxisSectionIdResponse


OMIT = typing.cast(typing.Any, ...)


class AxisSectionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAxisSectionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAxisSectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAxisSectionsClient
        """
        return self._raw_client

    def get_api_v3axes(
        self,
        *,
        paging: str,
        id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        is_active: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetApiV3AxesResponse:
        """
        List all Axes satisfying query filters.

        Parameters
        ----------
        paging : str
            {offset},{limit}. Defaults to 0,1000.

        id : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            Filter on axes unique identifiers.

        is_active : typing.Optional[bool]
            Filter on axes active status.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiV3AxesResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.axis_sections.get_api_v3axes(
            paging="100,0",
        )
        """
        _response = self._raw_client.get_api_v3axes(
            paging=paging, id=id, is_active=is_active, request_options=request_options
        )
        return _response.data

    def get_api_v3axissections(
        self,
        *,
        paging: str,
        axis_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        owner_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        active: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetApiV3AxissectionsResponse:
        """
        List all AxisSections satisfying query filters.

        Parameters
        ----------
        paging : str
            {offset},{limit}. Defaults to 0,1000.

        axis_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            Filter on the axis it belongs to.

        owner_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            Filter on the owner managing it.

        active : typing.Optional[bool]
            Filter on active status.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiV3AxissectionsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.axis_sections.get_api_v3axissections(
            paging="100,0",
        )
        """
        _response = self._raw_client.get_api_v3axissections(
            paging=paging, axis_id=axis_id, owner_id=owner_id, active=active, request_options=request_options
        )
        return _response.data

    def post_api_v3axis_sections(
        self,
        *,
        code: str,
        multilingual_name: str,
        axis_id: int,
        parent_axis_sections: typing.Optional[typing.Sequence[AxisSectionTreeless]] = OMIT,
        children_axis_sections: typing.Optional[typing.Sequence[AxisSectionTreeless]] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[int] = OMIT,
        start_on: typing.Optional[dt.datetime] = OMIT,
        end_on: typing.Optional[dt.datetime] = OMIT,
        active: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostApiV3AxisSectionsResponse:
        """
        Create a new AxisSection.

        Parameters
        ----------
        code : str

        multilingual_name : str

        axis_id : int

        parent_axis_sections : typing.Optional[typing.Sequence[AxisSectionTreeless]]

        children_axis_sections : typing.Optional[typing.Sequence[AxisSectionTreeless]]

        id : typing.Optional[int]

        name : typing.Optional[str]

        url : typing.Optional[str]

        description : typing.Optional[str]

        owner_id : typing.Optional[int]

        start_on : typing.Optional[dt.datetime]

        end_on : typing.Optional[dt.datetime]

        active : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostApiV3AxisSectionsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.axis_sections.post_api_v3axis_sections(
            code="code",
            multilingual_name="multilingualName",
            axis_id=1,
        )
        """
        _response = self._raw_client.post_api_v3axis_sections(
            code=code,
            multilingual_name=multilingual_name,
            axis_id=axis_id,
            parent_axis_sections=parent_axis_sections,
            children_axis_sections=children_axis_sections,
            id=id,
            name=name,
            url=url,
            description=description,
            owner_id=owner_id,
            start_on=start_on,
            end_on=end_on,
            active=active,
            request_options=request_options,
        )
        return _response.data

    def get_api_v3axis_sections_axis_section_id(
        self, axis_section_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetApiV3AxisSectionsAxisSectionIdResponse:
        """
        Retrieve a single AxisSection by its unique identifier.

        Parameters
        ----------
        axis_section_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiV3AxisSectionsAxisSectionIdResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.axis_sections.get_api_v3axis_sections_axis_section_id(
            axis_section_id=1,
        )
        """
        _response = self._raw_client.get_api_v3axis_sections_axis_section_id(
            axis_section_id, request_options=request_options
        )
        return _response.data

    def put_api_v3axis_sections_axis_section_id(
        self,
        axis_section_id: int,
        *,
        code: str,
        multilingual_name: str,
        axis_id: int,
        parent_axis_sections: typing.Optional[typing.Sequence[AxisSectionTreeless]] = OMIT,
        children_axis_sections: typing.Optional[typing.Sequence[AxisSectionTreeless]] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[int] = OMIT,
        start_on: typing.Optional[dt.datetime] = OMIT,
        end_on: typing.Optional[dt.datetime] = OMIT,
        active: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutApiV3AxisSectionsAxisSectionIdResponse:
        """
        Partial or complete update to an existing AxisSection.

        Parameters
        ----------
        axis_section_id : int

        code : str

        multilingual_name : str

        axis_id : int

        parent_axis_sections : typing.Optional[typing.Sequence[AxisSectionTreeless]]

        children_axis_sections : typing.Optional[typing.Sequence[AxisSectionTreeless]]

        id : typing.Optional[int]

        name : typing.Optional[str]

        url : typing.Optional[str]

        description : typing.Optional[str]

        owner_id : typing.Optional[int]

        start_on : typing.Optional[dt.datetime]

        end_on : typing.Optional[dt.datetime]

        active : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutApiV3AxisSectionsAxisSectionIdResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.axis_sections.put_api_v3axis_sections_axis_section_id(
            axis_section_id=1,
            code="code",
            multilingual_name="multilingualName",
            axis_id=1,
        )
        """
        _response = self._raw_client.put_api_v3axis_sections_axis_section_id(
            axis_section_id,
            code=code,
            multilingual_name=multilingual_name,
            axis_id=axis_id,
            parent_axis_sections=parent_axis_sections,
            children_axis_sections=children_axis_sections,
            id=id,
            name=name,
            url=url,
            description=description,
            owner_id=owner_id,
            start_on=start_on,
            end_on=end_on,
            active=active,
            request_options=request_options,
        )
        return _response.data

    def delete_api_v3axis_sections_axis_section_id(
        self, axis_section_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


        Parameters
        ----------
        axis_section_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.axis_sections.delete_api_v3axis_sections_axis_section_id(
            axis_section_id=1,
        )
        """
        _response = self._raw_client.delete_api_v3axis_sections_axis_section_id(
            axis_section_id, request_options=request_options
        )
        return _response.data


class AsyncAxisSectionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAxisSectionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAxisSectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAxisSectionsClient
        """
        return self._raw_client

    async def get_api_v3axes(
        self,
        *,
        paging: str,
        id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        is_active: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetApiV3AxesResponse:
        """
        List all Axes satisfying query filters.

        Parameters
        ----------
        paging : str
            {offset},{limit}. Defaults to 0,1000.

        id : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            Filter on axes unique identifiers.

        is_active : typing.Optional[bool]
            Filter on axes active status.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiV3AxesResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.axis_sections.get_api_v3axes(
                paging="100,0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v3axes(
            paging=paging, id=id, is_active=is_active, request_options=request_options
        )
        return _response.data

    async def get_api_v3axissections(
        self,
        *,
        paging: str,
        axis_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        owner_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        active: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetApiV3AxissectionsResponse:
        """
        List all AxisSections satisfying query filters.

        Parameters
        ----------
        paging : str
            {offset},{limit}. Defaults to 0,1000.

        axis_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            Filter on the axis it belongs to.

        owner_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            Filter on the owner managing it.

        active : typing.Optional[bool]
            Filter on active status.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiV3AxissectionsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.axis_sections.get_api_v3axissections(
                paging="100,0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v3axissections(
            paging=paging, axis_id=axis_id, owner_id=owner_id, active=active, request_options=request_options
        )
        return _response.data

    async def post_api_v3axis_sections(
        self,
        *,
        code: str,
        multilingual_name: str,
        axis_id: int,
        parent_axis_sections: typing.Optional[typing.Sequence[AxisSectionTreeless]] = OMIT,
        children_axis_sections: typing.Optional[typing.Sequence[AxisSectionTreeless]] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[int] = OMIT,
        start_on: typing.Optional[dt.datetime] = OMIT,
        end_on: typing.Optional[dt.datetime] = OMIT,
        active: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostApiV3AxisSectionsResponse:
        """
        Create a new AxisSection.

        Parameters
        ----------
        code : str

        multilingual_name : str

        axis_id : int

        parent_axis_sections : typing.Optional[typing.Sequence[AxisSectionTreeless]]

        children_axis_sections : typing.Optional[typing.Sequence[AxisSectionTreeless]]

        id : typing.Optional[int]

        name : typing.Optional[str]

        url : typing.Optional[str]

        description : typing.Optional[str]

        owner_id : typing.Optional[int]

        start_on : typing.Optional[dt.datetime]

        end_on : typing.Optional[dt.datetime]

        active : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostApiV3AxisSectionsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.axis_sections.post_api_v3axis_sections(
                code="code",
                multilingual_name="multilingualName",
                axis_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v3axis_sections(
            code=code,
            multilingual_name=multilingual_name,
            axis_id=axis_id,
            parent_axis_sections=parent_axis_sections,
            children_axis_sections=children_axis_sections,
            id=id,
            name=name,
            url=url,
            description=description,
            owner_id=owner_id,
            start_on=start_on,
            end_on=end_on,
            active=active,
            request_options=request_options,
        )
        return _response.data

    async def get_api_v3axis_sections_axis_section_id(
        self, axis_section_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetApiV3AxisSectionsAxisSectionIdResponse:
        """
        Retrieve a single AxisSection by its unique identifier.

        Parameters
        ----------
        axis_section_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiV3AxisSectionsAxisSectionIdResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.axis_sections.get_api_v3axis_sections_axis_section_id(
                axis_section_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v3axis_sections_axis_section_id(
            axis_section_id, request_options=request_options
        )
        return _response.data

    async def put_api_v3axis_sections_axis_section_id(
        self,
        axis_section_id: int,
        *,
        code: str,
        multilingual_name: str,
        axis_id: int,
        parent_axis_sections: typing.Optional[typing.Sequence[AxisSectionTreeless]] = OMIT,
        children_axis_sections: typing.Optional[typing.Sequence[AxisSectionTreeless]] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[int] = OMIT,
        start_on: typing.Optional[dt.datetime] = OMIT,
        end_on: typing.Optional[dt.datetime] = OMIT,
        active: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutApiV3AxisSectionsAxisSectionIdResponse:
        """
        Partial or complete update to an existing AxisSection.

        Parameters
        ----------
        axis_section_id : int

        code : str

        multilingual_name : str

        axis_id : int

        parent_axis_sections : typing.Optional[typing.Sequence[AxisSectionTreeless]]

        children_axis_sections : typing.Optional[typing.Sequence[AxisSectionTreeless]]

        id : typing.Optional[int]

        name : typing.Optional[str]

        url : typing.Optional[str]

        description : typing.Optional[str]

        owner_id : typing.Optional[int]

        start_on : typing.Optional[dt.datetime]

        end_on : typing.Optional[dt.datetime]

        active : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutApiV3AxisSectionsAxisSectionIdResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.axis_sections.put_api_v3axis_sections_axis_section_id(
                axis_section_id=1,
                code="code",
                multilingual_name="multilingualName",
                axis_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_api_v3axis_sections_axis_section_id(
            axis_section_id,
            code=code,
            multilingual_name=multilingual_name,
            axis_id=axis_id,
            parent_axis_sections=parent_axis_sections,
            children_axis_sections=children_axis_sections,
            id=id,
            name=name,
            url=url,
            description=description,
            owner_id=owner_id,
            start_on=start_on,
            end_on=end_on,
            active=active,
            request_options=request_options,
        )
        return _response.data

    async def delete_api_v3axis_sections_axis_section_id(
        self, axis_section_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


        Parameters
        ----------
        axis_section_id : int

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.axis_sections.delete_api_v3axis_sections_axis_section_id(
                axis_section_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_api_v3axis_sections_axis_section_id(
            axis_section_id, request_options=request_options
        )
        return _response.data
