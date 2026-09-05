

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_limit_param import AppLimitParam
from ..types.create_project_automation_config import CreateProjectAutomationConfig
from ..types.ending_before import EndingBefore
from ..types.ids import Ids
from ..types.org_name import OrgName
from ..types.project_automation import ProjectAutomation
from ..types.project_automation_id_param import ProjectAutomationIdParam
from ..types.project_automation_name import ProjectAutomationName
from ..types.starting_after import StartingAfter
from .raw_client import AsyncRawProjectAutomationsClient, RawProjectAutomationsClient
from .types.get_project_automation_response import GetProjectAutomationResponse
from .types.patch_project_automation_config import PatchProjectAutomationConfig


OMIT = typing.cast(typing.Any, ...)


class ProjectAutomationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProjectAutomationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProjectAutomationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProjectAutomationsClient
        """
        return self._raw_client

    def get_project_automation(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        project_automation_name: typing.Optional[ProjectAutomationName] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetProjectAutomationResponse:
        """
        List out all project_automations. The project_automations are sorted by creation date, with the most recently-created project_automations coming first

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

        project_automation_name : typing.Optional[ProjectAutomationName]
            Name of the project_automation to search for

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectAutomationResponse
            Returns a list of project_automation objects

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project_automations.get_project_automation()
        """
        _response = self._raw_client.get_project_automation(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            project_automation_name=project_automation_name,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    def post_project_automation(
        self,
        *,
        project_id: str,
        name: str,
        config: CreateProjectAutomationConfig,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectAutomation:
        """
        Create a new project_automation. If there is an existing project_automation with the same name as the one specified in the request, will return the existing project_automation unmodified

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the project automation belongs under

        name : str
            Name of the project automation

        config : CreateProjectAutomationConfig
            The configuration for the automation rule

        description : typing.Optional[str]
            Textual description of the project automation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectAutomation
            Returns the new project_automation object

        Examples
        --------
        from fern import (
            CreateProjectAutomationConfig_Logs,
            CreateProjectAutomationConfigLogsAction_Webhook,
            FernApi,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project_automations.post_project_automation(
            project_id="project_id",
            name="name",
            config=CreateProjectAutomationConfig_Logs(
                btql_filter="btql_filter",
                interval_seconds=1.1,
                action=CreateProjectAutomationConfigLogsAction_Webhook(
                    url="url",
                ),
            ),
        )
        """
        _response = self._raw_client.post_project_automation(
            project_id=project_id, name=name, config=config, description=description, request_options=request_options
        )
        return _response.data

    def put_project_automation(
        self,
        *,
        project_id: str,
        name: str,
        config: CreateProjectAutomationConfig,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectAutomation:
        """
        Create or replace project_automation. If there is an existing project_automation with the same name as the one specified in the request, will replace the existing project_automation with the provided fields

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the project automation belongs under

        name : str
            Name of the project automation

        config : CreateProjectAutomationConfig
            The configuration for the automation rule

        description : typing.Optional[str]
            Textual description of the project automation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectAutomation
            Returns the new project_automation object

        Examples
        --------
        from fern import (
            CreateProjectAutomationConfig_Logs,
            CreateProjectAutomationConfigLogsAction_Webhook,
            FernApi,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project_automations.put_project_automation(
            project_id="project_id",
            name="name",
            config=CreateProjectAutomationConfig_Logs(
                btql_filter="btql_filter",
                interval_seconds=1.1,
                action=CreateProjectAutomationConfigLogsAction_Webhook(
                    url="url",
                ),
            ),
        )
        """
        _response = self._raw_client.put_project_automation(
            project_id=project_id, name=name, config=config, description=description, request_options=request_options
        )
        return _response.data

    def get_project_automation_id(
        self,
        project_automation_id: ProjectAutomationIdParam,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectAutomation:
        """
        Get a project_automation object by its id

        Parameters
        ----------
        project_automation_id : ProjectAutomationIdParam
            ProjectAutomation id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectAutomation
            Returns the project_automation object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project_automations.get_project_automation_id(
            project_automation_id="project_automation_id",
        )
        """
        _response = self._raw_client.get_project_automation_id(project_automation_id, request_options=request_options)
        return _response.data

    def delete_project_automation_id(
        self,
        project_automation_id: ProjectAutomationIdParam,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectAutomation:
        """
        Delete a project_automation object by its id

        Parameters
        ----------
        project_automation_id : ProjectAutomationIdParam
            ProjectAutomation id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectAutomation
            Returns the deleted project_automation object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project_automations.delete_project_automation_id(
            project_automation_id="project_automation_id",
        )
        """
        _response = self._raw_client.delete_project_automation_id(
            project_automation_id, request_options=request_options
        )
        return _response.data

    def patch_project_automation_id(
        self,
        project_automation_id: ProjectAutomationIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        config: typing.Optional[PatchProjectAutomationConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectAutomation:
        """
        Partially update a project_automation object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        project_automation_id : ProjectAutomationIdParam
            ProjectAutomation id

        name : typing.Optional[str]
            Name of the project automation

        description : typing.Optional[str]
            Textual description of the project automation

        config : typing.Optional[PatchProjectAutomationConfig]
            The configuration for the automation rule

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectAutomation
            Returns the project_automation object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project_automations.patch_project_automation_id(
            project_automation_id="project_automation_id",
        )
        """
        _response = self._raw_client.patch_project_automation_id(
            project_automation_id, name=name, description=description, config=config, request_options=request_options
        )
        return _response.data


class AsyncProjectAutomationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProjectAutomationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProjectAutomationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProjectAutomationsClient
        """
        return self._raw_client

    async def get_project_automation(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        project_automation_name: typing.Optional[ProjectAutomationName] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetProjectAutomationResponse:
        """
        List out all project_automations. The project_automations are sorted by creation date, with the most recently-created project_automations coming first

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

        project_automation_name : typing.Optional[ProjectAutomationName]
            Name of the project_automation to search for

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectAutomationResponse
            Returns a list of project_automation objects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project_automations.get_project_automation()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_automation(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            project_automation_name=project_automation_name,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    async def post_project_automation(
        self,
        *,
        project_id: str,
        name: str,
        config: CreateProjectAutomationConfig,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectAutomation:
        """
        Create a new project_automation. If there is an existing project_automation with the same name as the one specified in the request, will return the existing project_automation unmodified

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the project automation belongs under

        name : str
            Name of the project automation

        config : CreateProjectAutomationConfig
            The configuration for the automation rule

        description : typing.Optional[str]
            Textual description of the project automation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectAutomation
            Returns the new project_automation object

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            CreateProjectAutomationConfig_Logs,
            CreateProjectAutomationConfigLogsAction_Webhook,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project_automations.post_project_automation(
                project_id="project_id",
                name="name",
                config=CreateProjectAutomationConfig_Logs(
                    btql_filter="btql_filter",
                    interval_seconds=1.1,
                    action=CreateProjectAutomationConfigLogsAction_Webhook(
                        url="url",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_project_automation(
            project_id=project_id, name=name, config=config, description=description, request_options=request_options
        )
        return _response.data

    async def put_project_automation(
        self,
        *,
        project_id: str,
        name: str,
        config: CreateProjectAutomationConfig,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectAutomation:
        """
        Create or replace project_automation. If there is an existing project_automation with the same name as the one specified in the request, will replace the existing project_automation with the provided fields

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the project automation belongs under

        name : str
            Name of the project automation

        config : CreateProjectAutomationConfig
            The configuration for the automation rule

        description : typing.Optional[str]
            Textual description of the project automation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectAutomation
            Returns the new project_automation object

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            CreateProjectAutomationConfig_Logs,
            CreateProjectAutomationConfigLogsAction_Webhook,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project_automations.put_project_automation(
                project_id="project_id",
                name="name",
                config=CreateProjectAutomationConfig_Logs(
                    btql_filter="btql_filter",
                    interval_seconds=1.1,
                    action=CreateProjectAutomationConfigLogsAction_Webhook(
                        url="url",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_project_automation(
            project_id=project_id, name=name, config=config, description=description, request_options=request_options
        )
        return _response.data

    async def get_project_automation_id(
        self,
        project_automation_id: ProjectAutomationIdParam,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectAutomation:
        """
        Get a project_automation object by its id

        Parameters
        ----------
        project_automation_id : ProjectAutomationIdParam
            ProjectAutomation id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectAutomation
            Returns the project_automation object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project_automations.get_project_automation_id(
                project_automation_id="project_automation_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_automation_id(
            project_automation_id, request_options=request_options
        )
        return _response.data

    async def delete_project_automation_id(
        self,
        project_automation_id: ProjectAutomationIdParam,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectAutomation:
        """
        Delete a project_automation object by its id

        Parameters
        ----------
        project_automation_id : ProjectAutomationIdParam
            ProjectAutomation id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectAutomation
            Returns the deleted project_automation object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project_automations.delete_project_automation_id(
                project_automation_id="project_automation_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_project_automation_id(
            project_automation_id, request_options=request_options
        )
        return _response.data

    async def patch_project_automation_id(
        self,
        project_automation_id: ProjectAutomationIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        config: typing.Optional[PatchProjectAutomationConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectAutomation:
        """
        Partially update a project_automation object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        project_automation_id : ProjectAutomationIdParam
            ProjectAutomation id

        name : typing.Optional[str]
            Name of the project automation

        description : typing.Optional[str]
            Textual description of the project automation

        config : typing.Optional[PatchProjectAutomationConfig]
            The configuration for the automation rule

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectAutomation
            Returns the project_automation object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project_automations.patch_project_automation_id(
                project_automation_id="project_automation_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_project_automation_id(
            project_automation_id, name=name, description=description, config=config, request_options=request_options
        )
        return _response.data
