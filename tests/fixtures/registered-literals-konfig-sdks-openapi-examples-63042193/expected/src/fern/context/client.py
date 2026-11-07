

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.context_create_new_context_response import ContextCreateNewContextResponse
from ..types.context_get_information_response import ContextGetInformationResponse
from ..types.context_list_environment_variables_response import ContextListEnvironmentVariablesResponse
from ..types.context_list_owner_contexts_response import ContextListOwnerContextsResponse
from ..types.context_project_restrictions_list import ContextProjectRestrictionsList
from ..types.context_remove_context_response import ContextRemoveContextResponse
from ..types.context_remove_environment_variable_response import ContextRemoveEnvironmentVariableResponse
from ..types.context_update_environment_variable_response import ContextUpdateEnvironmentVariableResponse
from ..types.restriction_created import RestrictionCreated
from ..types.restriction_deleted import RestrictionDeleted
from .raw_client import AsyncRawContextClient, RawContextClient
from .types.context_create_new_context_request_owner import ContextCreateNewContextRequestOwner
from .types.context_list_owner_contexts_request_owner_type import ContextListOwnerContextsRequestOwnerType


OMIT = typing.cast(typing.Any, ...)


class ContextClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawContextClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawContextClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawContextClient
        """
        return self._raw_client

    def listownercontexts(
        self,
        *,
        owner_id: typing.Optional[str] = None,
        owner_slug: typing.Optional[str] = None,
        owner_type: typing.Optional[ContextListOwnerContextsRequestOwnerType] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContextListOwnerContextsResponse:
        """
        List all contexts for an owner.

        Parameters
        ----------
        owner_id : typing.Optional[str]
            The unique ID of the owner of the context. Specify either this or owner-slug.

        owner_slug : typing.Optional[str]
            A string that represents an organization. Specify either this or owner-id. Cannot be used for accounts.

        owner_type : typing.Optional[ContextListOwnerContextsRequestOwnerType]
            The type of the owner. Defaults to "organization". Accounts are only used as context owners in server.

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContextListOwnerContextsResponse
            A paginated list of contexts

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.context.listownercontexts()
        """
        _response = self._raw_client.listownercontexts(
            owner_id=owner_id,
            owner_slug=owner_slug,
            owner_type=owner_type,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    def createnewcontext(
        self,
        *,
        name: str,
        owner: ContextCreateNewContextRequestOwner,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContextCreateNewContextResponse:
        """
        Creates a new context.

        Parameters
        ----------
        name : str
            The user defined name of the context.

        owner : ContextCreateNewContextRequestOwner

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContextCreateNewContextResponse
            The new context

        Examples
        --------
        from fern.context import ContextCreateNewContextRequestOwnerId

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.context.createnewcontext(
            name="name",
            owner=ContextCreateNewContextRequestOwnerId(
                id="id",
            ),
        )
        """
        _response = self._raw_client.createnewcontext(name=name, owner=owner, request_options=request_options)
        return _response.data

    def getinformation(
        self, context_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContextGetInformationResponse:
        """
        Returns basic information about a context.

        Parameters
        ----------
        context_id : str
            ID of the context (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContextGetInformationResponse
            The context

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.context.getinformation(
            context_id="context-id",
        )
        """
        _response = self._raw_client.getinformation(context_id, request_options=request_options)
        return _response.data

    def removecontext(
        self, context_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContextRemoveContextResponse:
        """
        Parameters
        ----------
        context_id : str
            ID of the context (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContextRemoveContextResponse
            A confirmation message

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.context.removecontext(
            context_id="context-id",
        )
        """
        _response = self._raw_client.removecontext(context_id, request_options=request_options)
        return _response.data

    def listenvironmentvariables(
        self,
        context_id: str,
        *,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContextListEnvironmentVariablesResponse:
        """
        List information about environment variables in a context, not including their values.

        Parameters
        ----------
        context_id : str
            ID of the context (UUID)

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContextListEnvironmentVariablesResponse
            A paginated list of environment variables

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.context.listenvironmentvariables(
            context_id="context-id",
        )
        """
        _response = self._raw_client.listenvironmentvariables(
            context_id, page_token=page_token, request_options=request_options
        )
        return _response.data

    def updateenvironmentvariable(
        self, context_id: str, env_var_name: str, *, value: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ContextUpdateEnvironmentVariableResponse:
        """
        Create or update an environment variable within a context. Returns information about the environment variable, not including its value.

        Parameters
        ----------
        context_id : str
            ID of the context (UUID)

        env_var_name : str
            The name of the environment variable

        value : str
            The value of the environment variable

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContextUpdateEnvironmentVariableResponse
            The new environment variable

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.context.updateenvironmentvariable(
            context_id="context-id",
            env_var_name="POSTGRES_USER",
            value="some-secret-value",
        )
        """
        _response = self._raw_client.updateenvironmentvariable(
            context_id, env_var_name, value=value, request_options=request_options
        )
        return _response.data

    def removeenvironmentvariable(
        self, context_id: str, env_var_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContextRemoveEnvironmentVariableResponse:
        """
        Delete an environment variable from a context.

        Parameters
        ----------
        context_id : str
            ID of the context (UUID)

        env_var_name : str
            The name of the environment variable

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContextRemoveEnvironmentVariableResponse
            A confirmation message

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.context.removeenvironmentvariable(
            context_id="context-id",
            env_var_name="POSTGRES_USER",
        )
        """
        _response = self._raw_client.removeenvironmentvariable(
            context_id, env_var_name, request_options=request_options
        )
        return _response.data

    def getrestrictions(
        self, context_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContextProjectRestrictionsList:
        """
        [__EXPERIMENTAL__] Gets a list of project restrictions associated with a context.

        Parameters
        ----------
        context_id : str
            An opaque identifier of a context.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContextProjectRestrictionsList
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.context.getrestrictions(
            context_id="be8bb2e3-c3d6-4098-89f4-572ff976ba9a",
        )
        """
        _response = self._raw_client.getrestrictions(context_id, request_options=request_options)
        return _response.data

    def createrestriction(
        self,
        context_id: str,
        *,
        project_id: typing.Optional[str] = OMIT,
        restriction_type: typing.Optional[str] = OMIT,
        restriction_value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RestrictionCreated:
        """
        [__EXPERIMENTAL__] Creates project restriction on a context.

        Parameters
        ----------
        context_id : str
            An opaque identifier of a context.

        project_id : typing.Optional[str]
            Deprecated - Use "restriction_type" and "restriction_value"
            instead.

            The project ID to use for a project restriction. This is
            mutually exclusive with restriction_type and restriction_value
            and implies restriction_type is "project".

        restriction_type : typing.Optional[str]

        restriction_value : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RestrictionCreated
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.context.createrestriction(
            context_id="be8bb2e3-c3d6-4098-89f4-572ff976ba9a",
            restriction_type="project",
            restriction_value="405d8375-3514-403b-8c43-83ae74cfe0e9",
        )
        """
        _response = self._raw_client.createrestriction(
            context_id,
            project_id=project_id,
            restriction_type=restriction_type,
            restriction_value=restriction_value,
            request_options=request_options,
        )
        return _response.data

    def deleterestriction(
        self, context_id: str, restriction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RestrictionDeleted:
        """
        [__EXPERIMENTAL__] Deletes a project restriction on a context.

        Parameters
        ----------
        context_id : str
            An opaque identifier of a context.

        restriction_id : str
            An opaque identifier of a context restriction.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RestrictionDeleted
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.context.deleterestriction(
            context_id="be8bb2e3-c3d6-4098-89f4-572ff976ba9a",
            restriction_id="1c23d2cb-07b1-4a28-8af3-e369732050ed",
        )
        """
        _response = self._raw_client.deleterestriction(context_id, restriction_id, request_options=request_options)
        return _response.data


class AsyncContextClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawContextClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawContextClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawContextClient
        """
        return self._raw_client

    async def listownercontexts(
        self,
        *,
        owner_id: typing.Optional[str] = None,
        owner_slug: typing.Optional[str] = None,
        owner_type: typing.Optional[ContextListOwnerContextsRequestOwnerType] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContextListOwnerContextsResponse:
        """
        List all contexts for an owner.

        Parameters
        ----------
        owner_id : typing.Optional[str]
            The unique ID of the owner of the context. Specify either this or owner-slug.

        owner_slug : typing.Optional[str]
            A string that represents an organization. Specify either this or owner-id. Cannot be used for accounts.

        owner_type : typing.Optional[ContextListOwnerContextsRequestOwnerType]
            The type of the owner. Defaults to "organization". Accounts are only used as context owners in server.

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContextListOwnerContextsResponse
            A paginated list of contexts

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.context.listownercontexts()


        asyncio.run(main())
        """
        _response = await self._raw_client.listownercontexts(
            owner_id=owner_id,
            owner_slug=owner_slug,
            owner_type=owner_type,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    async def createnewcontext(
        self,
        *,
        name: str,
        owner: ContextCreateNewContextRequestOwner,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContextCreateNewContextResponse:
        """
        Creates a new context.

        Parameters
        ----------
        name : str
            The user defined name of the context.

        owner : ContextCreateNewContextRequestOwner

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContextCreateNewContextResponse
            The new context

        Examples
        --------
        import asyncio

        from fern.context import ContextCreateNewContextRequestOwnerId

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.context.createnewcontext(
                name="name",
                owner=ContextCreateNewContextRequestOwnerId(
                    id="id",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createnewcontext(name=name, owner=owner, request_options=request_options)
        return _response.data

    async def getinformation(
        self, context_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContextGetInformationResponse:
        """
        Returns basic information about a context.

        Parameters
        ----------
        context_id : str
            ID of the context (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContextGetInformationResponse
            The context

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.context.getinformation(
                context_id="context-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getinformation(context_id, request_options=request_options)
        return _response.data

    async def removecontext(
        self, context_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContextRemoveContextResponse:
        """
        Parameters
        ----------
        context_id : str
            ID of the context (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContextRemoveContextResponse
            A confirmation message

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.context.removecontext(
                context_id="context-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.removecontext(context_id, request_options=request_options)
        return _response.data

    async def listenvironmentvariables(
        self,
        context_id: str,
        *,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContextListEnvironmentVariablesResponse:
        """
        List information about environment variables in a context, not including their values.

        Parameters
        ----------
        context_id : str
            ID of the context (UUID)

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContextListEnvironmentVariablesResponse
            A paginated list of environment variables

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.context.listenvironmentvariables(
                context_id="context-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listenvironmentvariables(
            context_id, page_token=page_token, request_options=request_options
        )
        return _response.data

    async def updateenvironmentvariable(
        self, context_id: str, env_var_name: str, *, value: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ContextUpdateEnvironmentVariableResponse:
        """
        Create or update an environment variable within a context. Returns information about the environment variable, not including its value.

        Parameters
        ----------
        context_id : str
            ID of the context (UUID)

        env_var_name : str
            The name of the environment variable

        value : str
            The value of the environment variable

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContextUpdateEnvironmentVariableResponse
            The new environment variable

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.context.updateenvironmentvariable(
                context_id="context-id",
                env_var_name="POSTGRES_USER",
                value="some-secret-value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updateenvironmentvariable(
            context_id, env_var_name, value=value, request_options=request_options
        )
        return _response.data

    async def removeenvironmentvariable(
        self, context_id: str, env_var_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContextRemoveEnvironmentVariableResponse:
        """
        Delete an environment variable from a context.

        Parameters
        ----------
        context_id : str
            ID of the context (UUID)

        env_var_name : str
            The name of the environment variable

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContextRemoveEnvironmentVariableResponse
            A confirmation message

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.context.removeenvironmentvariable(
                context_id="context-id",
                env_var_name="POSTGRES_USER",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.removeenvironmentvariable(
            context_id, env_var_name, request_options=request_options
        )
        return _response.data

    async def getrestrictions(
        self, context_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContextProjectRestrictionsList:
        """
        [__EXPERIMENTAL__] Gets a list of project restrictions associated with a context.

        Parameters
        ----------
        context_id : str
            An opaque identifier of a context.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContextProjectRestrictionsList
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.context.getrestrictions(
                context_id="be8bb2e3-c3d6-4098-89f4-572ff976ba9a",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getrestrictions(context_id, request_options=request_options)
        return _response.data

    async def createrestriction(
        self,
        context_id: str,
        *,
        project_id: typing.Optional[str] = OMIT,
        restriction_type: typing.Optional[str] = OMIT,
        restriction_value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RestrictionCreated:
        """
        [__EXPERIMENTAL__] Creates project restriction on a context.

        Parameters
        ----------
        context_id : str
            An opaque identifier of a context.

        project_id : typing.Optional[str]
            Deprecated - Use "restriction_type" and "restriction_value"
            instead.

            The project ID to use for a project restriction. This is
            mutually exclusive with restriction_type and restriction_value
            and implies restriction_type is "project".

        restriction_type : typing.Optional[str]

        restriction_value : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RestrictionCreated
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.context.createrestriction(
                context_id="be8bb2e3-c3d6-4098-89f4-572ff976ba9a",
                restriction_type="project",
                restriction_value="405d8375-3514-403b-8c43-83ae74cfe0e9",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createrestriction(
            context_id,
            project_id=project_id,
            restriction_type=restriction_type,
            restriction_value=restriction_value,
            request_options=request_options,
        )
        return _response.data

    async def deleterestriction(
        self, context_id: str, restriction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RestrictionDeleted:
        """
        [__EXPERIMENTAL__] Deletes a project restriction on a context.

        Parameters
        ----------
        context_id : str
            An opaque identifier of a context.

        restriction_id : str
            An opaque identifier of a context restriction.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RestrictionDeleted
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.context.deleterestriction(
                context_id="be8bb2e3-c3d6-4098-89f4-572ff976ba9a",
                restriction_id="1c23d2cb-07b1-4a28-8af3-e369732050ed",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deleterestriction(
            context_id, restriction_id, request_options=request_options
        )
        return _response.data
