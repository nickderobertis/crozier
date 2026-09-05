

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.environment import Environment
from ..types.org_name import OrgName
from .raw_client import AsyncRawEnvironmentsClient, RawEnvironmentsClient
from .types.list_environments_response import ListEnvironmentsResponse


OMIT = typing.cast(typing.Any, ...)


class EnvironmentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEnvironmentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEnvironmentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEnvironmentsClient
        """
        return self._raw_client

    def list_environments(
        self,
        *,
        ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        name: typing.Optional[str] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListEnvironmentsResponse:
        """
        List out all environments. The environments are sorted by creation date, with the most recently-created environments first.

        Parameters
        ----------
        ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        name : typing.Optional[str]

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEnvironmentsResponse
            List of environments

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.list_environments()
        """
        _response = self._raw_client.list_environments(
            ids=ids, name=name, org_name=org_name, request_options=request_options
        )
        return _response.data

    def create_environment(
        self,
        *,
        name: str,
        slug: str,
        description: typing.Optional[str] = OMIT,
        org_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Environment:
        """
        Create a new environment

        Parameters
        ----------
        name : str
            Name of the environment

        slug : str
            A url-friendly, unique identifier for the environment within an organization

        description : typing.Optional[str]
            Textual description of the environment

        org_name : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the environment belongs in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Environment
            Created environment

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.create_environment(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.create_environment(
            name=name, slug=slug, description=description, org_name=org_name, request_options=request_options
        )
        return _response.data

    def get_environment(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Environment:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Environment
            Environment object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.get_environment(
            environment_id="environment_id",
        )
        """
        _response = self._raw_client.get_environment(environment_id, request_options=request_options)
        return _response.data

    def delete_environment(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Environment:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Environment
            Deleted environment

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.delete_environment(
            environment_id="environment_id",
        )
        """
        _response = self._raw_client.delete_environment(environment_id, request_options=request_options)
        return _response.data

    def update_environment(
        self,
        environment_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        slug: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Environment:
        """
        Parameters
        ----------
        environment_id : str

        name : typing.Optional[str]
            Name of the environment

        slug : typing.Optional[str]
            A url-friendly, unique identifier for the environment within an organization

        description : typing.Optional[str]
            Textual description of the environment

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Environment
            Updated environment

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.update_environment(
            environment_id="environment_id",
        )
        """
        _response = self._raw_client.update_environment(
            environment_id, name=name, slug=slug, description=description, request_options=request_options
        )
        return _response.data


class AsyncEnvironmentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEnvironmentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEnvironmentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEnvironmentsClient
        """
        return self._raw_client

    async def list_environments(
        self,
        *,
        ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        name: typing.Optional[str] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListEnvironmentsResponse:
        """
        List out all environments. The environments are sorted by creation date, with the most recently-created environments first.

        Parameters
        ----------
        ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        name : typing.Optional[str]

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEnvironmentsResponse
            List of environments

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.list_environments()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_environments(
            ids=ids, name=name, org_name=org_name, request_options=request_options
        )
        return _response.data

    async def create_environment(
        self,
        *,
        name: str,
        slug: str,
        description: typing.Optional[str] = OMIT,
        org_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Environment:
        """
        Create a new environment

        Parameters
        ----------
        name : str
            Name of the environment

        slug : str
            A url-friendly, unique identifier for the environment within an organization

        description : typing.Optional[str]
            Textual description of the environment

        org_name : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the environment belongs in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Environment
            Created environment

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.create_environment(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_environment(
            name=name, slug=slug, description=description, org_name=org_name, request_options=request_options
        )
        return _response.data

    async def get_environment(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Environment:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Environment
            Environment object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.get_environment(
                environment_id="environment_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_environment(environment_id, request_options=request_options)
        return _response.data

    async def delete_environment(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Environment:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Environment
            Deleted environment

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.delete_environment(
                environment_id="environment_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_environment(environment_id, request_options=request_options)
        return _response.data

    async def update_environment(
        self,
        environment_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        slug: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Environment:
        """
        Parameters
        ----------
        environment_id : str

        name : typing.Optional[str]
            Name of the environment

        slug : typing.Optional[str]
            A url-friendly, unique identifier for the environment within an organization

        description : typing.Optional[str]
            Textual description of the environment

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Environment
            Updated environment

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.update_environment(
                environment_id="environment_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_environment(
            environment_id, name=name, slug=slug, description=description, request_options=request_options
        )
        return _response.data
