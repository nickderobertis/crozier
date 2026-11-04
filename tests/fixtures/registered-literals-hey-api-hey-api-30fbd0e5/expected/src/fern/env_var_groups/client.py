

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.t_environment_variable import TEnvironmentVariable
from .raw_client import AsyncRawEnvVarGroupsClient, RawEnvVarGroupsClient
from .types.environment_variable_groups_create_response import EnvironmentVariableGroupsCreateResponse
from .types.environment_variable_groups_list_response import EnvironmentVariableGroupsListResponse


OMIT = typing.cast(typing.Any, ...)


class EnvVarGroupsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEnvVarGroupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEnvVarGroupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEnvVarGroupsClient
        """
        return self._raw_client

    def environment_variable_groups_list(
        self,
        *,
        offset: int,
        limit: int,
        org_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvironmentVariableGroupsListResponse:
        """
        List environment variable groups

        Parameters
        ----------
        offset : int
            Number of items to skip in order to deliver paginated results

        limit : int
            Maximum items to return in each paginated response

        org_id : typing.Optional[str]
            Organization to act in. Defaults to the organization that owns the API token. List the organizations you belong to with GET /v2/orgs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentVariableGroupsListResponse
            A paginated result set

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.env_var_groups.environment_variable_groups_list(
            offset=1,
            limit=1,
        )
        """
        _response = self._raw_client.environment_variable_groups_list(
            offset=offset, limit=limit, org_id=org_id, request_options=request_options
        )
        return _response.data

    def environment_variable_groups_create(
        self, *, name: str, org_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvironmentVariableGroupsCreateResponse:
        """
        Create a new environment variable group

        Parameters
        ----------
        name : str

        org_id : typing.Optional[str]
            Organization to act in. Defaults to the organization that owns the API token. List the organizations you belong to with GET /v2/orgs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentVariableGroupsCreateResponse
            An environment variable group

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.env_var_groups.environment_variable_groups_create(
            name="name",
        )
        """
        _response = self._raw_client.environment_variable_groups_create(
            name=name, org_id=org_id, request_options=request_options
        )
        return _response.data

    def environment_variable_groups_rename(
        self, id: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Rename an environment variable group

        Parameters
        ----------
        id : str
            Environment variable group ID

        name : str
            New name for group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.env_var_groups.environment_variable_groups_rename(
            id="id",
            name="name",
        )
        """
        _response = self._raw_client.environment_variable_groups_rename(id, name=name, request_options=request_options)
        return _response.data

    def environment_variable_groups_delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete an environment variable group

        Parameters
        ----------
        id : str
            Environment variable group ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.env_var_groups.environment_variable_groups_delete(
            id="id",
        )
        """
        _response = self._raw_client.environment_variable_groups_delete(id, request_options=request_options)
        return _response.data

    def environment_variable_groups_get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TEnvironmentVariable]:
        """
        List variables in an environment variable group

        Parameters
        ----------
        id : str
            Environment variable group ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TEnvironmentVariable]
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.env_var_groups.environment_variable_groups_get(
            id="id",
        )
        """
        _response = self._raw_client.environment_variable_groups_get(id, request_options=request_options)
        return _response.data

    def environment_variable_groups_create_variable(
        self,
        id: str,
        *,
        value: str,
        key: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TEnvironmentVariable:
        """
        Create an environment variable in a group

        Parameters
        ----------
        id : str
            Environment variable group ID

        value : str
            Value of the environment variable.

        key : str
            Name or key of the environment variable, accessible via Deno.env or process.env

        description : typing.Optional[str]
            Optional description of the environment variable. Send null to clear an existing description; omit it to leave the description unchanged.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TEnvironmentVariable
            An environment variable

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.env_var_groups.environment_variable_groups_create_variable(
            id="id",
            value="value",
            key="key",
        )
        """
        _response = self._raw_client.environment_variable_groups_create_variable(
            id, value=value, key=key, description=description, request_options=request_options
        )
        return _response.data

    def environment_variable_groups_upsert_variable(
        self,
        id: str,
        key: str,
        *,
        value: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TEnvironmentVariable:
        """
        Create or update an environment variable in a group

        Parameters
        ----------
        id : str
            Environment variable group ID

        key : str
            Environment variable key

        value : str
            Value of the environment variable.

        description : typing.Optional[str]
            Optional description of the environment variable. Send null to clear an existing description; omit it to leave the description unchanged.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TEnvironmentVariable
            An environment variable

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.env_var_groups.environment_variable_groups_upsert_variable(
            id="id",
            key="key",
            value="value",
        )
        """
        _response = self._raw_client.environment_variable_groups_upsert_variable(
            id, key, value=value, description=description, request_options=request_options
        )
        return _response.data

    def environment_variable_groups_variable_delete(
        self, id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete an environment variable in a group

        Parameters
        ----------
        id : str
            Environment variable group ID

        key : str
            Environment variable key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.env_var_groups.environment_variable_groups_variable_delete(
            id="id",
            key="key",
        )
        """
        _response = self._raw_client.environment_variable_groups_variable_delete(
            id, key, request_options=request_options
        )
        return _response.data


class AsyncEnvVarGroupsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEnvVarGroupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEnvVarGroupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEnvVarGroupsClient
        """
        return self._raw_client

    async def environment_variable_groups_list(
        self,
        *,
        offset: int,
        limit: int,
        org_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvironmentVariableGroupsListResponse:
        """
        List environment variable groups

        Parameters
        ----------
        offset : int
            Number of items to skip in order to deliver paginated results

        limit : int
            Maximum items to return in each paginated response

        org_id : typing.Optional[str]
            Organization to act in. Defaults to the organization that owns the API token. List the organizations you belong to with GET /v2/orgs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentVariableGroupsListResponse
            A paginated result set

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.env_var_groups.environment_variable_groups_list(
                offset=1,
                limit=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.environment_variable_groups_list(
            offset=offset, limit=limit, org_id=org_id, request_options=request_options
        )
        return _response.data

    async def environment_variable_groups_create(
        self, *, name: str, org_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvironmentVariableGroupsCreateResponse:
        """
        Create a new environment variable group

        Parameters
        ----------
        name : str

        org_id : typing.Optional[str]
            Organization to act in. Defaults to the organization that owns the API token. List the organizations you belong to with GET /v2/orgs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentVariableGroupsCreateResponse
            An environment variable group

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.env_var_groups.environment_variable_groups_create(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.environment_variable_groups_create(
            name=name, org_id=org_id, request_options=request_options
        )
        return _response.data

    async def environment_variable_groups_rename(
        self, id: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Rename an environment variable group

        Parameters
        ----------
        id : str
            Environment variable group ID

        name : str
            New name for group

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.env_var_groups.environment_variable_groups_rename(
                id="id",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.environment_variable_groups_rename(
            id, name=name, request_options=request_options
        )
        return _response.data

    async def environment_variable_groups_delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete an environment variable group

        Parameters
        ----------
        id : str
            Environment variable group ID

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.env_var_groups.environment_variable_groups_delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.environment_variable_groups_delete(id, request_options=request_options)
        return _response.data

    async def environment_variable_groups_get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TEnvironmentVariable]:
        """
        List variables in an environment variable group

        Parameters
        ----------
        id : str
            Environment variable group ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TEnvironmentVariable]
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.env_var_groups.environment_variable_groups_get(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.environment_variable_groups_get(id, request_options=request_options)
        return _response.data

    async def environment_variable_groups_create_variable(
        self,
        id: str,
        *,
        value: str,
        key: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TEnvironmentVariable:
        """
        Create an environment variable in a group

        Parameters
        ----------
        id : str
            Environment variable group ID

        value : str
            Value of the environment variable.

        key : str
            Name or key of the environment variable, accessible via Deno.env or process.env

        description : typing.Optional[str]
            Optional description of the environment variable. Send null to clear an existing description; omit it to leave the description unchanged.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TEnvironmentVariable
            An environment variable

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.env_var_groups.environment_variable_groups_create_variable(
                id="id",
                value="value",
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.environment_variable_groups_create_variable(
            id, value=value, key=key, description=description, request_options=request_options
        )
        return _response.data

    async def environment_variable_groups_upsert_variable(
        self,
        id: str,
        key: str,
        *,
        value: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TEnvironmentVariable:
        """
        Create or update an environment variable in a group

        Parameters
        ----------
        id : str
            Environment variable group ID

        key : str
            Environment variable key

        value : str
            Value of the environment variable.

        description : typing.Optional[str]
            Optional description of the environment variable. Send null to clear an existing description; omit it to leave the description unchanged.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TEnvironmentVariable
            An environment variable

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.env_var_groups.environment_variable_groups_upsert_variable(
                id="id",
                key="key",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.environment_variable_groups_upsert_variable(
            id, key, value=value, description=description, request_options=request_options
        )
        return _response.data

    async def environment_variable_groups_variable_delete(
        self, id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete an environment variable in a group

        Parameters
        ----------
        id : str
            Environment variable group ID

        key : str
            Environment variable key

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.env_var_groups.environment_variable_groups_variable_delete(
                id="id",
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.environment_variable_groups_variable_delete(
            id, key, request_options=request_options
        )
        return _response.data
