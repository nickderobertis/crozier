

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.compare_documents_dto import CompareDocumentsDto
from ..types.compare_modules_dto import CompareModulesDto
from ..types.compare_policies_dto import ComparePoliciesDto
from ..types.compare_schemas_dto import CompareSchemasDto
from ..types.compare_tools_dto import CompareToolsDto
from ..types.search_policies_dto import SearchPoliciesDto
from .raw_client import AsyncRawAnalyticsClient, RawAnalyticsClient


OMIT = typing.cast(typing.Any, ...)


class AnalyticsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAnalyticsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAnalyticsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAnalyticsClient
        """
        return self._raw_client

    def analytics_api_search_policies(
        self, *, policy_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SearchPoliciesDto:
        """
        Search policies. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchPoliciesDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analytics.analytics_api_search_policies(
            policy_id="000000000000000000000000",
        )
        """
        _response = self._raw_client.analytics_api_search_policies(policy_id=policy_id, request_options=request_options)
        return _response.data

    def analytics_api_compare_policies(
        self,
        *,
        policy_id1: str,
        policy_id2: str,
        policy_ids: str,
        events_lvl: float,
        prop_lvl: float,
        children_lvl: float,
        id_lvl: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ComparePoliciesDto:
        """
        Compare policies. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id1 : str

        policy_id2 : str

        policy_ids : str

        events_lvl : float

        prop_lvl : float

        children_lvl : float

        id_lvl : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComparePoliciesDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analytics.analytics_api_compare_policies(
            policy_id1="000000000000000000000001",
            policy_id2="000000000000000000000002",
            policy_ids="policyIds",
            events_lvl=1.1,
            prop_lvl=1.1,
            children_lvl=1.1,
            id_lvl=1.1,
        )
        """
        _response = self._raw_client.analytics_api_compare_policies(
            policy_id1=policy_id1,
            policy_id2=policy_id2,
            policy_ids=policy_ids,
            events_lvl=events_lvl,
            prop_lvl=prop_lvl,
            children_lvl=children_lvl,
            id_lvl=id_lvl,
            request_options=request_options,
        )
        return _response.data

    def analytics_api_compare_modules(
        self,
        *,
        module_id1: str,
        module_id2: str,
        events_lvl: float,
        prop_lvl: float,
        children_lvl: float,
        id_lvl: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompareModulesDto:
        """
        Compare modules. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        module_id1 : str

        module_id2 : str

        events_lvl : float

        prop_lvl : float

        children_lvl : float

        id_lvl : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompareModulesDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analytics.analytics_api_compare_modules(
            module_id1="000000000000000000000001",
            module_id2="000000000000000000000002",
            events_lvl=1.1,
            prop_lvl=1.1,
            children_lvl=1.1,
            id_lvl=1.1,
        )
        """
        _response = self._raw_client.analytics_api_compare_modules(
            module_id1=module_id1,
            module_id2=module_id2,
            events_lvl=events_lvl,
            prop_lvl=prop_lvl,
            children_lvl=children_lvl,
            id_lvl=id_lvl,
            request_options=request_options,
        )
        return _response.data

    def analytics_api_compare_schemas(
        self,
        *,
        schema_id1: str,
        schema_id2: str,
        id_lvl: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompareSchemasDto:
        """
        Compare schemas. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        schema_id1 : str

        schema_id2 : str

        id_lvl : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompareSchemasDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analytics.analytics_api_compare_schemas(
            schema_id1="000000000000000000000001",
            schema_id2="000000000000000000000002",
            id_lvl=1.1,
        )
        """
        _response = self._raw_client.analytics_api_compare_schemas(
            schema_id1=schema_id1, schema_id2=schema_id2, id_lvl=id_lvl, request_options=request_options
        )
        return _response.data

    def analytics_api_compare_documents(
        self,
        *,
        document_id1: str,
        document_id2: str,
        document_ids: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompareDocumentsDto:
        """
        Compare documents. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        document_id1 : str

        document_id2 : str

        document_ids : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompareDocumentsDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analytics.analytics_api_compare_documents(
            document_id1="000000000000000000000001",
            document_id2="000000000000000000000002",
            document_ids="documentIds",
        )
        """
        _response = self._raw_client.analytics_api_compare_documents(
            document_id1=document_id1,
            document_id2=document_id2,
            document_ids=document_ids,
            request_options=request_options,
        )
        return _response.data

    def analytics_api_compare_tools(
        self, *, tool_id1: str, tool_id2: str, tool_ids: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CompareToolsDto:
        """
        Compare tools. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        tool_id1 : str

        tool_id2 : str

        tool_ids : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompareToolsDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analytics.analytics_api_compare_tools(
            tool_id1="000000000000000000000001",
            tool_id2="000000000000000000000002",
            tool_ids="toolIds",
        )
        """
        _response = self._raw_client.analytics_api_compare_tools(
            tool_id1=tool_id1, tool_id2=tool_id2, tool_ids=tool_ids, request_options=request_options
        )
        return _response.data

    def analytics_api_compare_policies_export(
        self,
        *,
        policy_id1: str,
        policy_id2: str,
        policy_ids: str,
        events_lvl: float,
        prop_lvl: float,
        children_lvl: float,
        id_lvl: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Compare policies. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id1 : str

        policy_id2 : str

        policy_ids : str

        events_lvl : float

        prop_lvl : float

        children_lvl : float

        id_lvl : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analytics.analytics_api_compare_policies_export(
            policy_id1="000000000000000000000001",
            policy_id2="000000000000000000000002",
            policy_ids="policyIds",
            events_lvl=1.1,
            prop_lvl=1.1,
            children_lvl=1.1,
            id_lvl=1.1,
        )
        """
        _response = self._raw_client.analytics_api_compare_policies_export(
            policy_id1=policy_id1,
            policy_id2=policy_id2,
            policy_ids=policy_ids,
            events_lvl=events_lvl,
            prop_lvl=prop_lvl,
            children_lvl=children_lvl,
            id_lvl=id_lvl,
            request_options=request_options,
        )
        return _response.data

    def analytics_api_compare_modules_export(
        self,
        *,
        module_id1: str,
        module_id2: str,
        events_lvl: float,
        prop_lvl: float,
        children_lvl: float,
        id_lvl: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Compare modules. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        module_id1 : str

        module_id2 : str

        events_lvl : float

        prop_lvl : float

        children_lvl : float

        id_lvl : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analytics.analytics_api_compare_modules_export(
            module_id1="000000000000000000000001",
            module_id2="000000000000000000000002",
            events_lvl=1.1,
            prop_lvl=1.1,
            children_lvl=1.1,
            id_lvl=1.1,
        )
        """
        _response = self._raw_client.analytics_api_compare_modules_export(
            module_id1=module_id1,
            module_id2=module_id2,
            events_lvl=events_lvl,
            prop_lvl=prop_lvl,
            children_lvl=children_lvl,
            id_lvl=id_lvl,
            request_options=request_options,
        )
        return _response.data

    def analytics_api_compare_schemas_export(
        self,
        *,
        schema_id1: str,
        schema_id2: str,
        id_lvl: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Compare schemas. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        schema_id1 : str

        schema_id2 : str

        id_lvl : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analytics.analytics_api_compare_schemas_export(
            schema_id1="000000000000000000000001",
            schema_id2="000000000000000000000002",
            id_lvl=1.1,
        )
        """
        _response = self._raw_client.analytics_api_compare_schemas_export(
            schema_id1=schema_id1, schema_id2=schema_id2, id_lvl=id_lvl, request_options=request_options
        )
        return _response.data

    def analytics_api_compare_documents_export(
        self,
        *,
        document_id1: str,
        document_id2: str,
        document_ids: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Compare documents. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        document_id1 : str

        document_id2 : str

        document_ids : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analytics.analytics_api_compare_documents_export(
            document_id1="000000000000000000000001",
            document_id2="000000000000000000000002",
            document_ids="documentIds",
        )
        """
        _response = self._raw_client.analytics_api_compare_documents_export(
            document_id1=document_id1,
            document_id2=document_id2,
            document_ids=document_ids,
            request_options=request_options,
        )
        return _response.data

    def analytics_api_compare_tools_export(
        self, *, tool_id1: str, tool_id2: str, tool_ids: str, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Compare tools. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        tool_id1 : str

        tool_id2 : str

        tool_ids : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analytics.analytics_api_compare_tools_export(
            tool_id1="000000000000000000000001",
            tool_id2="000000000000000000000002",
            tool_ids="toolIds",
        )
        """
        _response = self._raw_client.analytics_api_compare_tools_export(
            tool_id1=tool_id1, tool_id2=tool_id2, tool_ids=tool_ids, request_options=request_options
        )
        return _response.data

    def analytics_api_search_blocks(
        self, *, policy_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SearchPoliciesDto:
        """
        Search same blocks. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchPoliciesDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analytics.analytics_api_search_blocks(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.analytics_api_search_blocks(policy_id=policy_id, request_options=request_options)
        return _response.data


class AsyncAnalyticsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAnalyticsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAnalyticsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAnalyticsClient
        """
        return self._raw_client

    async def analytics_api_search_policies(
        self, *, policy_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SearchPoliciesDto:
        """
        Search policies. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchPoliciesDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analytics.analytics_api_search_policies(
                policy_id="000000000000000000000000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.analytics_api_search_policies(
            policy_id=policy_id, request_options=request_options
        )
        return _response.data

    async def analytics_api_compare_policies(
        self,
        *,
        policy_id1: str,
        policy_id2: str,
        policy_ids: str,
        events_lvl: float,
        prop_lvl: float,
        children_lvl: float,
        id_lvl: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ComparePoliciesDto:
        """
        Compare policies. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id1 : str

        policy_id2 : str

        policy_ids : str

        events_lvl : float

        prop_lvl : float

        children_lvl : float

        id_lvl : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComparePoliciesDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analytics.analytics_api_compare_policies(
                policy_id1="000000000000000000000001",
                policy_id2="000000000000000000000002",
                policy_ids="policyIds",
                events_lvl=1.1,
                prop_lvl=1.1,
                children_lvl=1.1,
                id_lvl=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.analytics_api_compare_policies(
            policy_id1=policy_id1,
            policy_id2=policy_id2,
            policy_ids=policy_ids,
            events_lvl=events_lvl,
            prop_lvl=prop_lvl,
            children_lvl=children_lvl,
            id_lvl=id_lvl,
            request_options=request_options,
        )
        return _response.data

    async def analytics_api_compare_modules(
        self,
        *,
        module_id1: str,
        module_id2: str,
        events_lvl: float,
        prop_lvl: float,
        children_lvl: float,
        id_lvl: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompareModulesDto:
        """
        Compare modules. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        module_id1 : str

        module_id2 : str

        events_lvl : float

        prop_lvl : float

        children_lvl : float

        id_lvl : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompareModulesDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analytics.analytics_api_compare_modules(
                module_id1="000000000000000000000001",
                module_id2="000000000000000000000002",
                events_lvl=1.1,
                prop_lvl=1.1,
                children_lvl=1.1,
                id_lvl=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.analytics_api_compare_modules(
            module_id1=module_id1,
            module_id2=module_id2,
            events_lvl=events_lvl,
            prop_lvl=prop_lvl,
            children_lvl=children_lvl,
            id_lvl=id_lvl,
            request_options=request_options,
        )
        return _response.data

    async def analytics_api_compare_schemas(
        self,
        *,
        schema_id1: str,
        schema_id2: str,
        id_lvl: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompareSchemasDto:
        """
        Compare schemas. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        schema_id1 : str

        schema_id2 : str

        id_lvl : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompareSchemasDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analytics.analytics_api_compare_schemas(
                schema_id1="000000000000000000000001",
                schema_id2="000000000000000000000002",
                id_lvl=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.analytics_api_compare_schemas(
            schema_id1=schema_id1, schema_id2=schema_id2, id_lvl=id_lvl, request_options=request_options
        )
        return _response.data

    async def analytics_api_compare_documents(
        self,
        *,
        document_id1: str,
        document_id2: str,
        document_ids: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompareDocumentsDto:
        """
        Compare documents. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        document_id1 : str

        document_id2 : str

        document_ids : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompareDocumentsDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analytics.analytics_api_compare_documents(
                document_id1="000000000000000000000001",
                document_id2="000000000000000000000002",
                document_ids="documentIds",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.analytics_api_compare_documents(
            document_id1=document_id1,
            document_id2=document_id2,
            document_ids=document_ids,
            request_options=request_options,
        )
        return _response.data

    async def analytics_api_compare_tools(
        self, *, tool_id1: str, tool_id2: str, tool_ids: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CompareToolsDto:
        """
        Compare tools. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        tool_id1 : str

        tool_id2 : str

        tool_ids : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompareToolsDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analytics.analytics_api_compare_tools(
                tool_id1="000000000000000000000001",
                tool_id2="000000000000000000000002",
                tool_ids="toolIds",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.analytics_api_compare_tools(
            tool_id1=tool_id1, tool_id2=tool_id2, tool_ids=tool_ids, request_options=request_options
        )
        return _response.data

    async def analytics_api_compare_policies_export(
        self,
        *,
        policy_id1: str,
        policy_id2: str,
        policy_ids: str,
        events_lvl: float,
        prop_lvl: float,
        children_lvl: float,
        id_lvl: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Compare policies. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id1 : str

        policy_id2 : str

        policy_ids : str

        events_lvl : float

        prop_lvl : float

        children_lvl : float

        id_lvl : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analytics.analytics_api_compare_policies_export(
                policy_id1="000000000000000000000001",
                policy_id2="000000000000000000000002",
                policy_ids="policyIds",
                events_lvl=1.1,
                prop_lvl=1.1,
                children_lvl=1.1,
                id_lvl=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.analytics_api_compare_policies_export(
            policy_id1=policy_id1,
            policy_id2=policy_id2,
            policy_ids=policy_ids,
            events_lvl=events_lvl,
            prop_lvl=prop_lvl,
            children_lvl=children_lvl,
            id_lvl=id_lvl,
            request_options=request_options,
        )
        return _response.data

    async def analytics_api_compare_modules_export(
        self,
        *,
        module_id1: str,
        module_id2: str,
        events_lvl: float,
        prop_lvl: float,
        children_lvl: float,
        id_lvl: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Compare modules. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        module_id1 : str

        module_id2 : str

        events_lvl : float

        prop_lvl : float

        children_lvl : float

        id_lvl : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analytics.analytics_api_compare_modules_export(
                module_id1="000000000000000000000001",
                module_id2="000000000000000000000002",
                events_lvl=1.1,
                prop_lvl=1.1,
                children_lvl=1.1,
                id_lvl=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.analytics_api_compare_modules_export(
            module_id1=module_id1,
            module_id2=module_id2,
            events_lvl=events_lvl,
            prop_lvl=prop_lvl,
            children_lvl=children_lvl,
            id_lvl=id_lvl,
            request_options=request_options,
        )
        return _response.data

    async def analytics_api_compare_schemas_export(
        self,
        *,
        schema_id1: str,
        schema_id2: str,
        id_lvl: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Compare schemas. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        schema_id1 : str

        schema_id2 : str

        id_lvl : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analytics.analytics_api_compare_schemas_export(
                schema_id1="000000000000000000000001",
                schema_id2="000000000000000000000002",
                id_lvl=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.analytics_api_compare_schemas_export(
            schema_id1=schema_id1, schema_id2=schema_id2, id_lvl=id_lvl, request_options=request_options
        )
        return _response.data

    async def analytics_api_compare_documents_export(
        self,
        *,
        document_id1: str,
        document_id2: str,
        document_ids: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Compare documents. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        document_id1 : str

        document_id2 : str

        document_ids : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analytics.analytics_api_compare_documents_export(
                document_id1="000000000000000000000001",
                document_id2="000000000000000000000002",
                document_ids="documentIds",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.analytics_api_compare_documents_export(
            document_id1=document_id1,
            document_id2=document_id2,
            document_ids=document_ids,
            request_options=request_options,
        )
        return _response.data

    async def analytics_api_compare_tools_export(
        self, *, tool_id1: str, tool_id2: str, tool_ids: str, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Compare tools. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        tool_id1 : str

        tool_id2 : str

        tool_ids : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analytics.analytics_api_compare_tools_export(
                tool_id1="000000000000000000000001",
                tool_id2="000000000000000000000002",
                tool_ids="toolIds",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.analytics_api_compare_tools_export(
            tool_id1=tool_id1, tool_id2=tool_id2, tool_ids=tool_ids, request_options=request_options
        )
        return _response.data

    async def analytics_api_search_blocks(
        self, *, policy_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SearchPoliciesDto:
        """
        Search same blocks. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchPoliciesDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analytics.analytics_api_search_blocks(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.analytics_api_search_blocks(
            policy_id=policy_id, request_options=request_options
        )
        return _response.data
