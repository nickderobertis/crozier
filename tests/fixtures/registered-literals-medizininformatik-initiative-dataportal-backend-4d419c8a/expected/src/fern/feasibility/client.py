

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.criterion_list import CriterionList
from ..types.query_quota import QueryQuota
from ..types.query_result import QueryResult
from ..types.query_result_obfuscated import QueryResultObfuscated
from ..types.query_result_rate_limit import QueryResultRateLimit
from .raw_client import AsyncRawFeasibilityClient, RawFeasibilityClient


OMIT = typing.cast(typing.Any, ...)


class FeasibilityClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFeasibilityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFeasibilityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFeasibilityClient
        """
        return self._raw_client

    def run_query(
        self,
        *,
        version: str,
        inclusion_criteria: typing.Sequence[CriterionList],
        display: typing.Optional[str] = OMIT,
        exclusion_criteria: typing.Optional[typing.Sequence[CriterionList]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        The query will be spawned in the broker and directly be dispatched.

        Parameters
        ----------
        version : str
            The json schema version

        inclusion_criteria : typing.Sequence[CriterionList]

        display : typing.Optional[str]

        exclusion_criteria : typing.Optional[typing.Sequence[CriterionList]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import Criterion, FernApi, TermCode

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.feasibility.run_query(
            version="http://to_be_decided.com/draft-1/schema#",
            inclusion_criteria=[
                [
                    Criterion(
                        term_codes=[
                            TermCode(
                                code="code",
                                system="http://snomed.info/sct",
                                display="Amniotic fluid specimen (specimen)",
                            )
                        ],
                    )
                ]
            ],
        )
        """
        _response = self._raw_client.run_query(
            version=version,
            inclusion_criteria=inclusion_criteria,
            display=display,
            exclusion_criteria=exclusion_criteria,
            request_options=request_options,
        )
        return _response.data

    def get_query_result_summary(
        self, query_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> QueryResult:
        """
        Returns the aggregated results to a query. There is no breakdown by site. So, the resultLines parameter of the response is de facto an array of QueryResultLines, but it will always be empty in this case.

        Parameters
        ----------
        query_id : int
            ID of query for which the results are requested

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryResult
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.feasibility.get_query_result_summary(
            query_id=1000000,
        )
        """
        _response = self._raw_client.get_query_result_summary(query_id, request_options=request_options)
        return _response.data

    def get_query_result_detailed(
        self, query_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> QueryResult:
        """
        Returns results to query with the real site names - admin rights required

        Parameters
        ----------
        query_id : int
            ID of query for which the results are requested

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryResult
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.feasibility.get_query_result_detailed(
            query_id=1000000,
        )
        """
        _response = self._raw_client.get_query_result_detailed(query_id, request_options=request_options)
        return _response.data

    def get_query_result_detailed_obfuscated(
        self, query_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> QueryResultObfuscated:
        """
        Returns all results to query with the site names obfuscated.

        Parameters
        ----------
        query_id : int
            ID of query for which the results are requested

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryResultObfuscated
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.feasibility.get_query_result_detailed_obfuscated(
            query_id=1000000,
        )
        """
        _response = self._raw_client.get_query_result_detailed_obfuscated(query_id, request_options=request_options)
        return _response.data

    def get_detailed_obfuscated_result_rate_limit(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> QueryResultRateLimit:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryResultRateLimit
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.feasibility.get_detailed_obfuscated_result_rate_limit()
        """
        _response = self._raw_client.get_detailed_obfuscated_result_rate_limit(request_options=request_options)
        return _response.data

    def get_quota(self, *, request_options: typing.Optional[RequestOptions] = None) -> QueryQuota:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryQuota
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.feasibility.get_quota()
        """
        _response = self._raw_client.get_quota(request_options=request_options)
        return _response.data

    def sq2cql(
        self,
        *,
        version: str,
        inclusion_criteria: typing.Sequence[CriterionList],
        display: typing.Optional[str] = OMIT,
        exclusion_criteria: typing.Optional[typing.Sequence[CriterionList]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Nothing will be persisted in the backend. It simply returns the cql.

        Parameters
        ----------
        version : str
            The json schema version

        inclusion_criteria : typing.Sequence[CriterionList]

        display : typing.Optional[str]

        exclusion_criteria : typing.Optional[typing.Sequence[CriterionList]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import Criterion, FernApi, TermCode

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.feasibility.sq2cql(
            version="http://to_be_decided.com/draft-1/schema#",
            inclusion_criteria=[
                [
                    Criterion(
                        term_codes=[
                            TermCode(
                                code="code",
                                system="http://snomed.info/sct",
                                display="Amniotic fluid specimen (specimen)",
                            )
                        ],
                    )
                ]
            ],
        )
        """
        _response = self._raw_client.sq2cql(
            version=version,
            inclusion_criteria=inclusion_criteria,
            display=display,
            exclusion_criteria=exclusion_criteria,
            request_options=request_options,
        )
        return _response.data


class AsyncFeasibilityClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFeasibilityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFeasibilityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFeasibilityClient
        """
        return self._raw_client

    async def run_query(
        self,
        *,
        version: str,
        inclusion_criteria: typing.Sequence[CriterionList],
        display: typing.Optional[str] = OMIT,
        exclusion_criteria: typing.Optional[typing.Sequence[CriterionList]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        The query will be spawned in the broker and directly be dispatched.

        Parameters
        ----------
        version : str
            The json schema version

        inclusion_criteria : typing.Sequence[CriterionList]

        display : typing.Optional[str]

        exclusion_criteria : typing.Optional[typing.Sequence[CriterionList]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Criterion, TermCode

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.feasibility.run_query(
                version="http://to_be_decided.com/draft-1/schema#",
                inclusion_criteria=[
                    [
                        Criterion(
                            term_codes=[
                                TermCode(
                                    code="code",
                                    system="http://snomed.info/sct",
                                    display="Amniotic fluid specimen (specimen)",
                                )
                            ],
                        )
                    ]
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.run_query(
            version=version,
            inclusion_criteria=inclusion_criteria,
            display=display,
            exclusion_criteria=exclusion_criteria,
            request_options=request_options,
        )
        return _response.data

    async def get_query_result_summary(
        self, query_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> QueryResult:
        """
        Returns the aggregated results to a query. There is no breakdown by site. So, the resultLines parameter of the response is de facto an array of QueryResultLines, but it will always be empty in this case.

        Parameters
        ----------
        query_id : int
            ID of query for which the results are requested

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryResult
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.feasibility.get_query_result_summary(
                query_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_query_result_summary(query_id, request_options=request_options)
        return _response.data

    async def get_query_result_detailed(
        self, query_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> QueryResult:
        """
        Returns results to query with the real site names - admin rights required

        Parameters
        ----------
        query_id : int
            ID of query for which the results are requested

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryResult
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.feasibility.get_query_result_detailed(
                query_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_query_result_detailed(query_id, request_options=request_options)
        return _response.data

    async def get_query_result_detailed_obfuscated(
        self, query_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> QueryResultObfuscated:
        """
        Returns all results to query with the site names obfuscated.

        Parameters
        ----------
        query_id : int
            ID of query for which the results are requested

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryResultObfuscated
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.feasibility.get_query_result_detailed_obfuscated(
                query_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_query_result_detailed_obfuscated(
            query_id, request_options=request_options
        )
        return _response.data

    async def get_detailed_obfuscated_result_rate_limit(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> QueryResultRateLimit:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryResultRateLimit
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.feasibility.get_detailed_obfuscated_result_rate_limit()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_detailed_obfuscated_result_rate_limit(request_options=request_options)
        return _response.data

    async def get_quota(self, *, request_options: typing.Optional[RequestOptions] = None) -> QueryQuota:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryQuota
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.feasibility.get_quota()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_quota(request_options=request_options)
        return _response.data

    async def sq2cql(
        self,
        *,
        version: str,
        inclusion_criteria: typing.Sequence[CriterionList],
        display: typing.Optional[str] = OMIT,
        exclusion_criteria: typing.Optional[typing.Sequence[CriterionList]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Nothing will be persisted in the backend. It simply returns the cql.

        Parameters
        ----------
        version : str
            The json schema version

        inclusion_criteria : typing.Sequence[CriterionList]

        display : typing.Optional[str]

        exclusion_criteria : typing.Optional[typing.Sequence[CriterionList]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Criterion, TermCode

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.feasibility.sq2cql(
                version="http://to_be_decided.com/draft-1/schema#",
                inclusion_criteria=[
                    [
                        Criterion(
                            term_codes=[
                                TermCode(
                                    code="code",
                                    system="http://snomed.info/sct",
                                    display="Amniotic fluid specimen (specimen)",
                                )
                            ],
                        )
                    ]
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sq2cql(
            version=version,
            inclusion_criteria=inclusion_criteria,
            display=display,
            exclusion_criteria=exclusion_criteria,
            request_options=request_options,
        )
        return _response.data
