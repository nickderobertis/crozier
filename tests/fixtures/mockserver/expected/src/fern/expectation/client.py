

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.expectation import Expectation
from ..types.expectations import Expectations
from ..types.http_request import HttpRequest
from ..types.open_api_expectations import OpenApiExpectations
from .raw_client import AsyncRawExpectationClient, RawExpectationClient
from .types.put_mockserver_generate_expectation_response import PutMockserverGenerateExpectationResponse


OMIT = typing.cast(typing.Any, ...)


class ExpectationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawExpectationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawExpectationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawExpectationClient
        """
        return self._raw_client

    def create_expectation(
        self, *, request: Expectations, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Expectation]:
        """
        Parameters
        ----------
        request : Expectations

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Expectation]
            expectations created

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.expectation.create_expectation(
            request={
                "httpRequest": {
                    "method": "GET",
                    "path": "/api/users",
                    "queryStringParameters": {"page": ["1"], "limit": ["10"]},
                },
                "httpResponse": {
                    "statusCode": 200,
                    "headers": {"Content-Type": ["application/json"]},
                    "body": '{"users":[{"id":1,"name":"John Doe"}],"total":1}',
                },
            },
        )
        """
        _response = self._raw_client.create_expectation(request=request, request_options=request_options)
        return _response.data

    def create_expectations_from_open_api_or_swagger(
        self, *, request: OpenApiExpectations, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Expectation]:
        """
        Parameters
        ----------
        request : OpenApiExpectations

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Expectation]
            expectations created

        Examples
        --------
        from fern import FernApi, OpenApiExpectation

        client = FernApi()
        client.expectation.create_expectations_from_open_api_or_swagger(
            request=OpenApiExpectation(
                spec_url_or_payload="https://raw.githubusercontent.com/mock-server/mockserver-monorepo/master/mockserver/mockserver-integration-testing/src/main/resources/org/mockserver/openapi/openapi_petstore_example.json",
                operations_and_responses={"listPets": "200", "showPetById": "200"},
            ),
        )
        """
        _response = self._raw_client.create_expectations_from_open_api_or_swagger(
            request=request, request_options=request_options
        )
        return _response.data

    def generate_expectation_suggestion_s_from_an_unmatched_request(
        self,
        *,
        request: HttpRequest,
        preview: typing.Optional[bool] = OMIT,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverGenerateExpectationResponse:
        """
        Generates one or more suggested expectations for an unmatched HttpRequest. When 'preview' is true (the default) the suggestions are only returned; when false they are also added. If an LLM backend is configured it is used, otherwise a simple template-based stub is generated.

        Parameters
        ----------
        request : HttpRequest

        preview : typing.Optional[bool]
            when true (default) only return suggestions; when false also add them

        limit : typing.Optional[int]
            maximum number of suggestions to generate (1-5)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverGenerateExpectationResponse
            expectation suggestion(s) returned

        Examples
        --------
        from fern import FernApi, HttpRequest

        client = FernApi()
        client.expectation.generate_expectation_suggestion_s_from_an_unmatched_request(
            request=HttpRequest(
                method="POST",
                path="/api/orders",
            ),
            preview=True,
            limit=1,
        )
        """
        _response = self._raw_client.generate_expectation_suggestion_s_from_an_unmatched_request(
            request=request, preview=preview, limit=limit, request_options=request_options
        )
        return _response.data

    def create_expectations_from_a_wsdl(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Expectation]:
        """
        generates expectations from a WSDL document (the request body is the raw WSDL) and adds them

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Expectation]
            expectations created from the WSDL

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.expectation.create_expectations_from_a_wsdl()
        """
        _response = self._raw_client.create_expectations_from_a_wsdl(request_options=request_options)
        return _response.data

    def create_expectations_from_a_graph_ql_schema(
        self, *, path: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Expectation]:
        """
        Generates expectations from a GraphQL schema (the request body is a GraphQL SDL document or an introspection JSON result) and adds them. One expectation is created per root operation type (query / mutation / subscription); each matches any operation of that kind and synthesizes a schema-valid response per request. The optional "path" query parameter overrides the default "/graphql" request path the generated expectations match.

        Parameters
        ----------
        path : typing.Optional[str]
            request path the generated GraphQL expectations match (default "/graphql")

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Expectation]
            expectations created from the GraphQL schema

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.expectation.create_expectations_from_a_graph_ql_schema()
        """
        _response = self._raw_client.create_expectations_from_a_graph_ql_schema(
            path=path, request_options=request_options
        )
        return _response.data

    def create_http_expectations_from_an_async_api_spec(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Expectation]:
        """
        Generates HTTP expectations from an AsyncAPI 2.x/3.x spec (JSON/YAML, or a {spec, channelPathPrefix} wrapper) so each channel's example message can be served over plain HTTP without a live broker. One GET expectation is created per channel returning that channel's schema-aware example payload. This is distinct from PUT /mockserver/asyncapi, which loads a spec into the broker-publishing mock. Requires the mockserver-async module on the classpath (501 otherwise).

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Expectation]
            HTTP expectations created from the AsyncAPI spec

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.expectation.create_http_expectations_from_an_async_api_spec(
            request={
                "spec": "asyncapi: 2.6.0\ninfo:\n  title: Test Service\n  version: 1.0.0\nchannels:\n  user/signedup:\n    publish:\n      message:\n        payload:\n          type: object\n          properties:\n            userId:\n              type: string",
                "channelPathPrefix": "/events",
            },
        )
        """
        _response = self._raw_client.create_http_expectations_from_an_async_api_spec(
            request=request, request_options=request_options
        )
        return _response.data


class AsyncExpectationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawExpectationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawExpectationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawExpectationClient
        """
        return self._raw_client

    async def create_expectation(
        self, *, request: Expectations, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Expectation]:
        """
        Parameters
        ----------
        request : Expectations

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Expectation]
            expectations created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.expectation.create_expectation(
                request={
                    "httpRequest": {
                        "method": "GET",
                        "path": "/api/users",
                        "queryStringParameters": {"page": ["1"], "limit": ["10"]},
                    },
                    "httpResponse": {
                        "statusCode": 200,
                        "headers": {"Content-Type": ["application/json"]},
                        "body": '{"users":[{"id":1,"name":"John Doe"}],"total":1}',
                    },
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_expectation(request=request, request_options=request_options)
        return _response.data

    async def create_expectations_from_open_api_or_swagger(
        self, *, request: OpenApiExpectations, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Expectation]:
        """
        Parameters
        ----------
        request : OpenApiExpectations

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Expectation]
            expectations created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OpenApiExpectation

        client = AsyncFernApi()


        async def main() -> None:
            await client.expectation.create_expectations_from_open_api_or_swagger(
                request=OpenApiExpectation(
                    spec_url_or_payload="https://raw.githubusercontent.com/mock-server/mockserver-monorepo/master/mockserver/mockserver-integration-testing/src/main/resources/org/mockserver/openapi/openapi_petstore_example.json",
                    operations_and_responses={"listPets": "200", "showPetById": "200"},
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_expectations_from_open_api_or_swagger(
            request=request, request_options=request_options
        )
        return _response.data

    async def generate_expectation_suggestion_s_from_an_unmatched_request(
        self,
        *,
        request: HttpRequest,
        preview: typing.Optional[bool] = OMIT,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverGenerateExpectationResponse:
        """
        Generates one or more suggested expectations for an unmatched HttpRequest. When 'preview' is true (the default) the suggestions are only returned; when false they are also added. If an LLM backend is configured it is used, otherwise a simple template-based stub is generated.

        Parameters
        ----------
        request : HttpRequest

        preview : typing.Optional[bool]
            when true (default) only return suggestions; when false also add them

        limit : typing.Optional[int]
            maximum number of suggestions to generate (1-5)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverGenerateExpectationResponse
            expectation suggestion(s) returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, HttpRequest

        client = AsyncFernApi()


        async def main() -> None:
            await client.expectation.generate_expectation_suggestion_s_from_an_unmatched_request(
                request=HttpRequest(
                    method="POST",
                    path="/api/orders",
                ),
                preview=True,
                limit=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.generate_expectation_suggestion_s_from_an_unmatched_request(
            request=request, preview=preview, limit=limit, request_options=request_options
        )
        return _response.data

    async def create_expectations_from_a_wsdl(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Expectation]:
        """
        generates expectations from a WSDL document (the request body is the raw WSDL) and adds them

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Expectation]
            expectations created from the WSDL

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.expectation.create_expectations_from_a_wsdl()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_expectations_from_a_wsdl(request_options=request_options)
        return _response.data

    async def create_expectations_from_a_graph_ql_schema(
        self, *, path: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Expectation]:
        """
        Generates expectations from a GraphQL schema (the request body is a GraphQL SDL document or an introspection JSON result) and adds them. One expectation is created per root operation type (query / mutation / subscription); each matches any operation of that kind and synthesizes a schema-valid response per request. The optional "path" query parameter overrides the default "/graphql" request path the generated expectations match.

        Parameters
        ----------
        path : typing.Optional[str]
            request path the generated GraphQL expectations match (default "/graphql")

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Expectation]
            expectations created from the GraphQL schema

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.expectation.create_expectations_from_a_graph_ql_schema()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_expectations_from_a_graph_ql_schema(
            path=path, request_options=request_options
        )
        return _response.data

    async def create_http_expectations_from_an_async_api_spec(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Expectation]:
        """
        Generates HTTP expectations from an AsyncAPI 2.x/3.x spec (JSON/YAML, or a {spec, channelPathPrefix} wrapper) so each channel's example message can be served over plain HTTP without a live broker. One GET expectation is created per channel returning that channel's schema-aware example payload. This is distinct from PUT /mockserver/asyncapi, which loads a spec into the broker-publishing mock. Requires the mockserver-async module on the classpath (501 otherwise).

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Expectation]
            HTTP expectations created from the AsyncAPI spec

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.expectation.create_http_expectations_from_an_async_api_spec(
                request={
                    "spec": "asyncapi: 2.6.0\ninfo:\n  title: Test Service\n  version: 1.0.0\nchannels:\n  user/signedup:\n    publish:\n      message:\n        payload:\n          type: object\n          properties:\n            userId:\n              type: string",
                    "channelPathPrefix": "/events",
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_http_expectations_from_an_async_api_spec(
            request=request, request_options=request_options
        )
        return _response.data
