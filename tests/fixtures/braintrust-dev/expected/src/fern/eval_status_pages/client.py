

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_limit_param import AppLimitParam
from ..types.ending_before import EndingBefore
from ..types.eval_status_page import EvalStatusPage
from ..types.eval_status_page_config import EvalStatusPageConfig
from ..types.eval_status_page_id_param import EvalStatusPageIdParam
from ..types.eval_status_page_name import EvalStatusPageName
from ..types.eval_status_page_theme import EvalStatusPageTheme
from ..types.ids import Ids
from ..types.org_name import OrgName
from ..types.starting_after import StartingAfter
from .raw_client import AsyncRawEvalStatusPagesClient, RawEvalStatusPagesClient
from .types.get_eval_status_page_response import GetEvalStatusPageResponse


OMIT = typing.cast(typing.Any, ...)


class EvalStatusPagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEvalStatusPagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEvalStatusPagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEvalStatusPagesClient
        """
        return self._raw_client

    def get_eval_status_page(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        eval_status_page_name: typing.Optional[EvalStatusPageName] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetEvalStatusPageResponse:
        """
        List out all eval_status_pages. The eval_status_pages are sorted by creation date, with the most recently-created eval_status_pages coming first

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

        eval_status_page_name : typing.Optional[EvalStatusPageName]
            Name of the eval_status_page to search for

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEvalStatusPageResponse
            Returns a list of eval_status_page objects

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.eval_status_pages.get_eval_status_page()
        """
        _response = self._raw_client.get_eval_status_page(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            eval_status_page_name=eval_status_page_name,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    def post_eval_status_page(
        self,
        *,
        project_id: str,
        name: str,
        theme: EvalStatusPageTheme,
        config: EvalStatusPageConfig,
        description: typing.Optional[str] = OMIT,
        logo_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EvalStatusPage:
        """
        Create a new eval_status_page. If there is an existing eval_status_page with the same name as the one specified in the request, will return the existing eval_status_page unmodified

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the eval status page belongs under

        name : str
            Name of the eval status page

        theme : EvalStatusPageTheme

        config : EvalStatusPageConfig

        description : typing.Optional[str]
            Textual description of the eval status page

        logo_url : typing.Optional[str]
            URL of the logo to display on the page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EvalStatusPage
            Returns the new eval_status_page object

        Examples
        --------
        from fern import EvalStatusPageConfig, EvalStatusPageTheme, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.eval_status_pages.post_eval_status_page(
            project_id="project_id",
            name="name",
            theme=EvalStatusPageTheme.LIGHT,
            config=EvalStatusPageConfig(),
        )
        """
        _response = self._raw_client.post_eval_status_page(
            project_id=project_id,
            name=name,
            theme=theme,
            config=config,
            description=description,
            logo_url=logo_url,
            request_options=request_options,
        )
        return _response.data

    def put_eval_status_page(
        self,
        *,
        project_id: str,
        name: str,
        theme: EvalStatusPageTheme,
        config: EvalStatusPageConfig,
        description: typing.Optional[str] = OMIT,
        logo_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EvalStatusPage:
        """
        Create or replace eval_status_page. If there is an existing eval_status_page with the same name as the one specified in the request, will replace the existing eval_status_page with the provided fields

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the eval status page belongs under

        name : str
            Name of the eval status page

        theme : EvalStatusPageTheme

        config : EvalStatusPageConfig

        description : typing.Optional[str]
            Textual description of the eval status page

        logo_url : typing.Optional[str]
            URL of the logo to display on the page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EvalStatusPage
            Returns the new eval_status_page object

        Examples
        --------
        from fern import EvalStatusPageConfig, EvalStatusPageTheme, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.eval_status_pages.put_eval_status_page(
            project_id="project_id",
            name="name",
            theme=EvalStatusPageTheme.LIGHT,
            config=EvalStatusPageConfig(),
        )
        """
        _response = self._raw_client.put_eval_status_page(
            project_id=project_id,
            name=name,
            theme=theme,
            config=config,
            description=description,
            logo_url=logo_url,
            request_options=request_options,
        )
        return _response.data

    def get_eval_status_page_id(
        self, eval_status_page_id: EvalStatusPageIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EvalStatusPage:
        """
        Get a eval_status_page object by its id

        Parameters
        ----------
        eval_status_page_id : EvalStatusPageIdParam
            EvalStatusPage id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EvalStatusPage
            Returns the eval_status_page object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.eval_status_pages.get_eval_status_page_id(
            eval_status_page_id="eval_status_page_id",
        )
        """
        _response = self._raw_client.get_eval_status_page_id(eval_status_page_id, request_options=request_options)
        return _response.data

    def delete_eval_status_page_id(
        self, eval_status_page_id: EvalStatusPageIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EvalStatusPage:
        """
        Delete a eval_status_page object by its id

        Parameters
        ----------
        eval_status_page_id : EvalStatusPageIdParam
            EvalStatusPage id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EvalStatusPage
            Returns the deleted eval_status_page object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.eval_status_pages.delete_eval_status_page_id(
            eval_status_page_id="eval_status_page_id",
        )
        """
        _response = self._raw_client.delete_eval_status_page_id(eval_status_page_id, request_options=request_options)
        return _response.data

    def patch_eval_status_page_id(
        self,
        eval_status_page_id: EvalStatusPageIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        logo_url: typing.Optional[str] = OMIT,
        theme: typing.Optional[EvalStatusPageTheme] = OMIT,
        config: typing.Optional[EvalStatusPageConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EvalStatusPage:
        """
        Partially update a eval_status_page object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        eval_status_page_id : EvalStatusPageIdParam
            EvalStatusPage id

        name : typing.Optional[str]
            Name of the eval status page

        description : typing.Optional[str]
            Textual description of the eval status page

        logo_url : typing.Optional[str]
            URL of the logo to display on the page

        theme : typing.Optional[EvalStatusPageTheme]

        config : typing.Optional[EvalStatusPageConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EvalStatusPage
            Returns the eval_status_page object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.eval_status_pages.patch_eval_status_page_id(
            eval_status_page_id="eval_status_page_id",
        )
        """
        _response = self._raw_client.patch_eval_status_page_id(
            eval_status_page_id,
            name=name,
            description=description,
            logo_url=logo_url,
            theme=theme,
            config=config,
            request_options=request_options,
        )
        return _response.data


class AsyncEvalStatusPagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEvalStatusPagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEvalStatusPagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEvalStatusPagesClient
        """
        return self._raw_client

    async def get_eval_status_page(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        eval_status_page_name: typing.Optional[EvalStatusPageName] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetEvalStatusPageResponse:
        """
        List out all eval_status_pages. The eval_status_pages are sorted by creation date, with the most recently-created eval_status_pages coming first

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

        eval_status_page_name : typing.Optional[EvalStatusPageName]
            Name of the eval_status_page to search for

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEvalStatusPageResponse
            Returns a list of eval_status_page objects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.eval_status_pages.get_eval_status_page()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_eval_status_page(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            eval_status_page_name=eval_status_page_name,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    async def post_eval_status_page(
        self,
        *,
        project_id: str,
        name: str,
        theme: EvalStatusPageTheme,
        config: EvalStatusPageConfig,
        description: typing.Optional[str] = OMIT,
        logo_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EvalStatusPage:
        """
        Create a new eval_status_page. If there is an existing eval_status_page with the same name as the one specified in the request, will return the existing eval_status_page unmodified

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the eval status page belongs under

        name : str
            Name of the eval status page

        theme : EvalStatusPageTheme

        config : EvalStatusPageConfig

        description : typing.Optional[str]
            Textual description of the eval status page

        logo_url : typing.Optional[str]
            URL of the logo to display on the page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EvalStatusPage
            Returns the new eval_status_page object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, EvalStatusPageConfig, EvalStatusPageTheme

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.eval_status_pages.post_eval_status_page(
                project_id="project_id",
                name="name",
                theme=EvalStatusPageTheme.LIGHT,
                config=EvalStatusPageConfig(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_eval_status_page(
            project_id=project_id,
            name=name,
            theme=theme,
            config=config,
            description=description,
            logo_url=logo_url,
            request_options=request_options,
        )
        return _response.data

    async def put_eval_status_page(
        self,
        *,
        project_id: str,
        name: str,
        theme: EvalStatusPageTheme,
        config: EvalStatusPageConfig,
        description: typing.Optional[str] = OMIT,
        logo_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EvalStatusPage:
        """
        Create or replace eval_status_page. If there is an existing eval_status_page with the same name as the one specified in the request, will replace the existing eval_status_page with the provided fields

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the eval status page belongs under

        name : str
            Name of the eval status page

        theme : EvalStatusPageTheme

        config : EvalStatusPageConfig

        description : typing.Optional[str]
            Textual description of the eval status page

        logo_url : typing.Optional[str]
            URL of the logo to display on the page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EvalStatusPage
            Returns the new eval_status_page object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, EvalStatusPageConfig, EvalStatusPageTheme

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.eval_status_pages.put_eval_status_page(
                project_id="project_id",
                name="name",
                theme=EvalStatusPageTheme.LIGHT,
                config=EvalStatusPageConfig(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_eval_status_page(
            project_id=project_id,
            name=name,
            theme=theme,
            config=config,
            description=description,
            logo_url=logo_url,
            request_options=request_options,
        )
        return _response.data

    async def get_eval_status_page_id(
        self, eval_status_page_id: EvalStatusPageIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EvalStatusPage:
        """
        Get a eval_status_page object by its id

        Parameters
        ----------
        eval_status_page_id : EvalStatusPageIdParam
            EvalStatusPage id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EvalStatusPage
            Returns the eval_status_page object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.eval_status_pages.get_eval_status_page_id(
                eval_status_page_id="eval_status_page_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_eval_status_page_id(eval_status_page_id, request_options=request_options)
        return _response.data

    async def delete_eval_status_page_id(
        self, eval_status_page_id: EvalStatusPageIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EvalStatusPage:
        """
        Delete a eval_status_page object by its id

        Parameters
        ----------
        eval_status_page_id : EvalStatusPageIdParam
            EvalStatusPage id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EvalStatusPage
            Returns the deleted eval_status_page object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.eval_status_pages.delete_eval_status_page_id(
                eval_status_page_id="eval_status_page_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_eval_status_page_id(
            eval_status_page_id, request_options=request_options
        )
        return _response.data

    async def patch_eval_status_page_id(
        self,
        eval_status_page_id: EvalStatusPageIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        logo_url: typing.Optional[str] = OMIT,
        theme: typing.Optional[EvalStatusPageTheme] = OMIT,
        config: typing.Optional[EvalStatusPageConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EvalStatusPage:
        """
        Partially update a eval_status_page object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        eval_status_page_id : EvalStatusPageIdParam
            EvalStatusPage id

        name : typing.Optional[str]
            Name of the eval status page

        description : typing.Optional[str]
            Textual description of the eval status page

        logo_url : typing.Optional[str]
            URL of the logo to display on the page

        theme : typing.Optional[EvalStatusPageTheme]

        config : typing.Optional[EvalStatusPageConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EvalStatusPage
            Returns the eval_status_page object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.eval_status_pages.patch_eval_status_page_id(
                eval_status_page_id="eval_status_page_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_eval_status_page_id(
            eval_status_page_id,
            name=name,
            description=description,
            logo_url=logo_url,
            theme=theme,
            config=config,
            request_options=request_options,
        )
        return _response.data
