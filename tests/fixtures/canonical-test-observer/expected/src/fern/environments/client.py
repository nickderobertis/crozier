

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.environment_reported_issue_response import EnvironmentReportedIssueResponse
from ..types.environments_response import EnvironmentsResponse
from ..types.family_name import FamilyName
from .raw_client import AsyncRawEnvironmentsClient, RawEnvironmentsClient


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

    def get_reported_issues(
        self, *, is_confirmed: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[EnvironmentReportedIssueResponse]:
        """
        Parameters
        ----------
        is_confirmed : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EnvironmentReportedIssueResponse]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.environments.get_reported_issues()
        """
        _response = self._raw_client.get_reported_issues(is_confirmed=is_confirmed, request_options=request_options)
        return _response.data

    def create_reported_issue(
        self,
        *,
        environment_name: str,
        description: str,
        is_confirmed: bool,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvironmentReportedIssueResponse:
        """
        Parameters
        ----------
        environment_name : str

        description : str

        is_confirmed : bool

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentReportedIssueResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.environments.create_reported_issue(
            environment_name="environment_name",
            description="description",
            is_confirmed=True,
        )
        """
        _response = self._raw_client.create_reported_issue(
            environment_name=environment_name,
            description=description,
            is_confirmed=is_confirmed,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def update_reported_issue(
        self,
        issue_id: int,
        *,
        environment_name: str,
        description: str,
        is_confirmed: bool,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvironmentReportedIssueResponse:
        """
        Parameters
        ----------
        issue_id : int

        environment_name : str

        description : str

        is_confirmed : bool

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentReportedIssueResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.environments.update_reported_issue(
            issue_id=1,
            environment_name="environment_name",
            description="description",
            is_confirmed=True,
        )
        """
        _response = self._raw_client.update_reported_issue(
            issue_id,
            environment_name=environment_name,
            description=description,
            is_confirmed=is_confirmed,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def delete_reported_issue(
        self, issue_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        issue_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.environments.delete_reported_issue(
            issue_id=1,
        )
        """
        _response = self._raw_client.delete_reported_issue(issue_id, request_options=request_options)
        return _response.data

    def get_environments(
        self,
        *,
        q: typing.Optional[str] = None,
        families: typing.Optional[typing.Sequence[FamilyName]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvironmentsResponse:
        """
        Returns list of distinct environments that have been used in test executions.

        Supports pagination and search filtering.

        Parameters
        ----------
        q : typing.Optional[str]
            Search term for environment names

        families : typing.Optional[typing.Sequence[FamilyName]]
            Filter by artefact families

        limit : typing.Optional[int]
            Maximum number of results (defaults to 50 if not specified)

        offset : typing.Optional[int]
            Number of results to skip for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentsResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.environments.get_environments()
        """
        _response = self._raw_client.get_environments(
            q=q, families=families, limit=limit, offset=offset, request_options=request_options
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

    async def get_reported_issues(
        self, *, is_confirmed: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[EnvironmentReportedIssueResponse]:
        """
        Parameters
        ----------
        is_confirmed : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EnvironmentReportedIssueResponse]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.environments.get_reported_issues()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_reported_issues(
            is_confirmed=is_confirmed, request_options=request_options
        )
        return _response.data

    async def create_reported_issue(
        self,
        *,
        environment_name: str,
        description: str,
        is_confirmed: bool,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvironmentReportedIssueResponse:
        """
        Parameters
        ----------
        environment_name : str

        description : str

        is_confirmed : bool

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentReportedIssueResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.environments.create_reported_issue(
                environment_name="environment_name",
                description="description",
                is_confirmed=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_reported_issue(
            environment_name=environment_name,
            description=description,
            is_confirmed=is_confirmed,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def update_reported_issue(
        self,
        issue_id: int,
        *,
        environment_name: str,
        description: str,
        is_confirmed: bool,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvironmentReportedIssueResponse:
        """
        Parameters
        ----------
        issue_id : int

        environment_name : str

        description : str

        is_confirmed : bool

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentReportedIssueResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.environments.update_reported_issue(
                issue_id=1,
                environment_name="environment_name",
                description="description",
                is_confirmed=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_reported_issue(
            issue_id,
            environment_name=environment_name,
            description=description,
            is_confirmed=is_confirmed,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def delete_reported_issue(
        self, issue_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        issue_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.environments.delete_reported_issue(
                issue_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_reported_issue(issue_id, request_options=request_options)
        return _response.data

    async def get_environments(
        self,
        *,
        q: typing.Optional[str] = None,
        families: typing.Optional[typing.Sequence[FamilyName]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvironmentsResponse:
        """
        Returns list of distinct environments that have been used in test executions.

        Supports pagination and search filtering.

        Parameters
        ----------
        q : typing.Optional[str]
            Search term for environment names

        families : typing.Optional[typing.Sequence[FamilyName]]
            Filter by artefact families

        limit : typing.Optional[int]
            Maximum number of results (defaults to 50 if not specified)

        offset : typing.Optional[int]
            Number of results to skip for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.environments.get_environments()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_environments(
            q=q, families=families, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data
