

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.company import Company
from .raw_client import AsyncRawCompanyEndpointsClient, RawCompanyEndpointsClient


OMIT = typing.cast(typing.Any, ...)


class CompanyEndpointsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCompanyEndpointsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCompanyEndpointsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCompanyEndpointsClient
        """
        return self._raw_client

    def company_enrich(
        self,
        *,
        pdl_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        profile: typing.Optional[str] = None,
        ticker: typing.Optional[str] = None,
        website: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        street_address: typing.Optional[str] = None,
        locality: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        pretty: typing.Optional[bool] = None,
        titlecase: typing.Optional[bool] = None,
        include_if_matched: typing.Optional[bool] = None,
        min_likelihood: typing.Optional[int] = None,
        required: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Company:
        """
        Parameters
        ----------
        pdl_id : typing.Optional[str]
            The PDL ID of the company to enrich.

        name : typing.Optional[str]
            The name of the company.

        profile : typing.Optional[str]
            A social profile of the company (linkedin/facebook/twitter/crunchbase).

        ticker : typing.Optional[str]
            The company's stock ticker, if publicly traded.

        website : typing.Optional[str]
            A website the company uses.

        location : typing.Optional[str]
            The location of the company's headquarters. This can be anything from a street address to a country name.

        street_address : typing.Optional[str]
            The company HQ's street address.

        locality : typing.Optional[str]
            The company HQ's locality. e.g. San Francisco

        region : typing.Optional[str]
            The company HQ's region. e.g. California

        country : typing.Optional[str]
            The company HQ's country.

        postal_code : typing.Optional[str]
            The company HQ's postal code.

        pretty : typing.Optional[bool]
            Whether the output should have human-readable indentation.

        titlecase : typing.Optional[bool]
            All text in API responses returns as lowercase by default. Setting titlecase to true will titlecase response data instead.

        include_if_matched : typing.Optional[bool]
            If true, the response will include the top-level field matched that contains a list of every input that matched this profile.

        min_likelihood : typing.Optional[int]
            The minimum likelihood score a response must possess in order to return a 200.

        required : typing.Optional[str]
            The fields a response must have in order to count as a match.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Company
            Company Found

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.company_endpoints.company_enrich(
            required="location AND (website OR linkedin_url)",
        )
        """
        _response = self._raw_client.company_enrich(
            pdl_id=pdl_id,
            name=name,
            profile=profile,
            ticker=ticker,
            website=website,
            location=location,
            street_address=street_address,
            locality=locality,
            region=region,
            country=country,
            postal_code=postal_code,
            pretty=pretty,
            titlecase=titlecase,
            include_if_matched=include_if_matched,
            min_likelihood=min_likelihood,
            required=required,
            request_options=request_options,
        )
        return _response.data

    def company_search(
        self,
        *,
        query: typing.Optional[str] = OMIT,
        sql: typing.Optional[str] = OMIT,
        size: typing.Optional[int] = OMIT,
        from_: typing.Optional[int] = OMIT,
        scroll_token: typing.Optional[str] = OMIT,
        titlecase: typing.Optional[bool] = OMIT,
        pretty: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Company:
        """
        Parameters
        ----------
        query : typing.Optional[str]
            An Elasticsearch (v7.7) query. See our underlying Elasticsearch mapping for reference

        sql : typing.Optional[str]
            A SQL query of the format: SELECT * FROM company WHERE XXX, where XXX is a standard SQL boolean query involving our company fields

        size : typing.Optional[int]
            The number of matched records to return for this query if they exist*. Must be between 1 and 100

        from_ : typing.Optional[int]
            An offset value for pagination. Can be a number between 0 and 9999. Pagination can be executed up to a maximum of 10,000 records per query. Be sure to use the "total" response field to help discover how many total records exist in the dataset for your query

        scroll_token : typing.Optional[str]
            Each search API response returns a scroll_token. Include it in the next request to fetch the next size matching records

        titlecase : typing.Optional[bool]
            Setting titlecase to true will titlecase any records returned

        pretty : typing.Optional[bool]
            Whether the output should have human-readable indentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Company
            Company Found

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.company_endpoints.company_search()
        """
        _response = self._raw_client.company_search(
            query=query,
            sql=sql,
            size=size,
            from_=from_,
            scroll_token=scroll_token,
            titlecase=titlecase,
            pretty=pretty,
            request_options=request_options,
        )
        return _response.data


class AsyncCompanyEndpointsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCompanyEndpointsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCompanyEndpointsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCompanyEndpointsClient
        """
        return self._raw_client

    async def company_enrich(
        self,
        *,
        pdl_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        profile: typing.Optional[str] = None,
        ticker: typing.Optional[str] = None,
        website: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        street_address: typing.Optional[str] = None,
        locality: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        pretty: typing.Optional[bool] = None,
        titlecase: typing.Optional[bool] = None,
        include_if_matched: typing.Optional[bool] = None,
        min_likelihood: typing.Optional[int] = None,
        required: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Company:
        """
        Parameters
        ----------
        pdl_id : typing.Optional[str]
            The PDL ID of the company to enrich.

        name : typing.Optional[str]
            The name of the company.

        profile : typing.Optional[str]
            A social profile of the company (linkedin/facebook/twitter/crunchbase).

        ticker : typing.Optional[str]
            The company's stock ticker, if publicly traded.

        website : typing.Optional[str]
            A website the company uses.

        location : typing.Optional[str]
            The location of the company's headquarters. This can be anything from a street address to a country name.

        street_address : typing.Optional[str]
            The company HQ's street address.

        locality : typing.Optional[str]
            The company HQ's locality. e.g. San Francisco

        region : typing.Optional[str]
            The company HQ's region. e.g. California

        country : typing.Optional[str]
            The company HQ's country.

        postal_code : typing.Optional[str]
            The company HQ's postal code.

        pretty : typing.Optional[bool]
            Whether the output should have human-readable indentation.

        titlecase : typing.Optional[bool]
            All text in API responses returns as lowercase by default. Setting titlecase to true will titlecase response data instead.

        include_if_matched : typing.Optional[bool]
            If true, the response will include the top-level field matched that contains a list of every input that matched this profile.

        min_likelihood : typing.Optional[int]
            The minimum likelihood score a response must possess in order to return a 200.

        required : typing.Optional[str]
            The fields a response must have in order to count as a match.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Company
            Company Found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.company_endpoints.company_enrich(
                required="location AND (website OR linkedin_url)",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.company_enrich(
            pdl_id=pdl_id,
            name=name,
            profile=profile,
            ticker=ticker,
            website=website,
            location=location,
            street_address=street_address,
            locality=locality,
            region=region,
            country=country,
            postal_code=postal_code,
            pretty=pretty,
            titlecase=titlecase,
            include_if_matched=include_if_matched,
            min_likelihood=min_likelihood,
            required=required,
            request_options=request_options,
        )
        return _response.data

    async def company_search(
        self,
        *,
        query: typing.Optional[str] = OMIT,
        sql: typing.Optional[str] = OMIT,
        size: typing.Optional[int] = OMIT,
        from_: typing.Optional[int] = OMIT,
        scroll_token: typing.Optional[str] = OMIT,
        titlecase: typing.Optional[bool] = OMIT,
        pretty: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Company:
        """
        Parameters
        ----------
        query : typing.Optional[str]
            An Elasticsearch (v7.7) query. See our underlying Elasticsearch mapping for reference

        sql : typing.Optional[str]
            A SQL query of the format: SELECT * FROM company WHERE XXX, where XXX is a standard SQL boolean query involving our company fields

        size : typing.Optional[int]
            The number of matched records to return for this query if they exist*. Must be between 1 and 100

        from_ : typing.Optional[int]
            An offset value for pagination. Can be a number between 0 and 9999. Pagination can be executed up to a maximum of 10,000 records per query. Be sure to use the "total" response field to help discover how many total records exist in the dataset for your query

        scroll_token : typing.Optional[str]
            Each search API response returns a scroll_token. Include it in the next request to fetch the next size matching records

        titlecase : typing.Optional[bool]
            Setting titlecase to true will titlecase any records returned

        pretty : typing.Optional[bool]
            Whether the output should have human-readable indentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Company
            Company Found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.company_endpoints.company_search()


        asyncio.run(main())
        """
        _response = await self._raw_client.company_search(
            query=query,
            sql=sql,
            size=size,
            from_=from_,
            scroll_token=scroll_token,
            titlecase=titlecase,
            pretty=pretty,
            request_options=request_options,
        )
        return _response.data
