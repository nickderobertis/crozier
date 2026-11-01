

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.family_name import FamilyName
from ..types.test_cases_response import TestCasesResponse
from ..types.test_reported_issue_response import TestReportedIssueResponse
from .raw_client import AsyncRawTestCasesClient, RawTestCasesClient


OMIT = typing.cast(typing.Any, ...)


class TestCasesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTestCasesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTestCasesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTestCasesClient
        """
        return self._raw_client

    def get_reported_issues(
        self,
        *,
        template_id: typing.Optional[str] = None,
        case_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[TestReportedIssueResponse]:
        """
        Parameters
        ----------
        template_id : typing.Optional[str]

        case_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TestReportedIssueResponse]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.test_cases.get_reported_issues()
        """
        _response = self._raw_client.get_reported_issues(
            template_id=template_id, case_name=case_name, request_options=request_options
        )
        return _response.data

    def create_reported_issue(
        self,
        *,
        description: str,
        url: str,
        template_id: typing.Optional[str] = OMIT,
        case_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestReportedIssueResponse:
        """
        Parameters
        ----------
        description : str

        url : str

        template_id : typing.Optional[str]

        case_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestReportedIssueResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.test_cases.create_reported_issue(
            description="description",
            url="url",
        )
        """
        _response = self._raw_client.create_reported_issue(
            description=description,
            url=url,
            template_id=template_id,
            case_name=case_name,
            request_options=request_options,
        )
        return _response.data

    def update_reported_issue(
        self,
        issue_id: int,
        *,
        description: str,
        url: str,
        template_id: typing.Optional[str] = OMIT,
        case_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestReportedIssueResponse:
        """
        Parameters
        ----------
        issue_id : int

        description : str

        url : str

        template_id : typing.Optional[str]

        case_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestReportedIssueResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.test_cases.update_reported_issue(
            issue_id=1,
            description="description",
            url="url",
        )
        """
        _response = self._raw_client.update_reported_issue(
            issue_id,
            description=description,
            url=url,
            template_id=template_id,
            case_name=case_name,
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
        client.test_cases.delete_reported_issue(
            issue_id=1,
        )
        """
        _response = self._raw_client.delete_reported_issue(issue_id, request_options=request_options)
        return _response.data

    def get_test_cases(
        self,
        *,
        q: typing.Optional[str] = None,
        families: typing.Optional[typing.Sequence[FamilyName]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestCasesResponse:
        """
        Returns test cases as a flat list with their template IDs.

        Template ID represents the generic test (e.g., "disk/stats_name")
        Test case name is the specific instance (e.g., "disk/stats_nvme0n1")
        Multiple test cases can share the same template ID but have different names.

        Parameters
        ----------
        q : typing.Optional[str]
            Search term for test case names

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
        TestCasesResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.test_cases.get_test_cases()
        """
        _response = self._raw_client.get_test_cases(
            q=q, families=families, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data


class AsyncTestCasesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTestCasesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTestCasesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTestCasesClient
        """
        return self._raw_client

    async def get_reported_issues(
        self,
        *,
        template_id: typing.Optional[str] = None,
        case_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[TestReportedIssueResponse]:
        """
        Parameters
        ----------
        template_id : typing.Optional[str]

        case_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TestReportedIssueResponse]
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
            await client.test_cases.get_reported_issues()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_reported_issues(
            template_id=template_id, case_name=case_name, request_options=request_options
        )
        return _response.data

    async def create_reported_issue(
        self,
        *,
        description: str,
        url: str,
        template_id: typing.Optional[str] = OMIT,
        case_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestReportedIssueResponse:
        """
        Parameters
        ----------
        description : str

        url : str

        template_id : typing.Optional[str]

        case_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestReportedIssueResponse
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
            await client.test_cases.create_reported_issue(
                description="description",
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_reported_issue(
            description=description,
            url=url,
            template_id=template_id,
            case_name=case_name,
            request_options=request_options,
        )
        return _response.data

    async def update_reported_issue(
        self,
        issue_id: int,
        *,
        description: str,
        url: str,
        template_id: typing.Optional[str] = OMIT,
        case_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestReportedIssueResponse:
        """
        Parameters
        ----------
        issue_id : int

        description : str

        url : str

        template_id : typing.Optional[str]

        case_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestReportedIssueResponse
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
            await client.test_cases.update_reported_issue(
                issue_id=1,
                description="description",
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_reported_issue(
            issue_id,
            description=description,
            url=url,
            template_id=template_id,
            case_name=case_name,
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
            await client.test_cases.delete_reported_issue(
                issue_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_reported_issue(issue_id, request_options=request_options)
        return _response.data

    async def get_test_cases(
        self,
        *,
        q: typing.Optional[str] = None,
        families: typing.Optional[typing.Sequence[FamilyName]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestCasesResponse:
        """
        Returns test cases as a flat list with their template IDs.

        Template ID represents the generic test (e.g., "disk/stats_name")
        Test case name is the specific instance (e.g., "disk/stats_nvme0n1")
        Multiple test cases can share the same template ID but have different names.

        Parameters
        ----------
        q : typing.Optional[str]
            Search term for test case names

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
        TestCasesResponse
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
            await client.test_cases.get_test_cases()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_test_cases(
            q=q, families=families, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data
