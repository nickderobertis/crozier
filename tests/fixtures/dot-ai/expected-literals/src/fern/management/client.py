

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tool_execution_response import ToolExecutionResponse
from .raw_client import AsyncRawManagementClient, RawManagementClient
from .types.manage_org_data_request_data_type import ManageOrgDataRequestDataType
from .types.manage_org_data_request_mode import ManageOrgDataRequestMode
from .types.manage_org_data_request_operation import ManageOrgDataRequestOperation
from .types.manage_org_data_request_resource import ManageOrgDataRequestResource


OMIT = typing.cast(typing.Any, ...)


class ManagementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawManagementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawManagementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawManagementClient
        """
        return self._raw_client

    def execute_manage_org_data_tool(
        self,
        *,
        data_type: ManageOrgDataRequestDataType,
        operation: ManageOrgDataRequestOperation,
        session_id: typing.Optional[str] = OMIT,
        step: typing.Optional[str] = OMIT,
        response: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        identity_only: typing.Optional[bool] = OMIT,
        resource: typing.Optional[ManageOrgDataRequestResource] = OMIT,
        resource_list: typing.Optional[str] = OMIT,
        mode: typing.Optional[ManageOrgDataRequestMode] = OMIT,
        collection: typing.Optional[str] = OMIT,
        interaction_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolExecutionResponse:
        """
        Tool for managing cluster resource capabilities. Supports scan, list, get, search, delete, deleteAll, and progress operations for cluster resource capability discovery and management. Use dataType="capabilities" to manage cluster capabilities. NOTE: Organizational patterns and policies are now managed via manageKnowledge tool (ingest documents, search, deleteByUri) with automatic AI classification.

        Parameters
        ----------
        data_type : ManageOrgDataRequestDataType
            Type of cluster data to manage: "capabilities" for resource capabilities. (Note: organizational knowledge/patterns/policies are managed via manageKnowledge tool)

        operation : ManageOrgDataRequestOperation
            Operation to perform on the cluster data

        session_id : typing.Optional[str]
            Session ID (required for continuing workflow steps, optional for progress - uses latest session if omitted)

        step : typing.Optional[str]
            Current workflow step (required when sessionId is provided)

        response : typing.Optional[str]
            User response to previous workflow step question

        id : typing.Optional[str]
            Capability ID (required for get/delete operations) or search query (required for search operations)

        limit : typing.Optional[int]
            Maximum number of items to return (must be an integer; default: 10, maximum: 10000). The response carries an explicit truncated flag, the authoritative completeness signal; totalCount equals returnedCount when not truncated and is a best-effort figure otherwise.

        identity_only : typing.Optional[bool]
            For list: return only identity fields (id, resourceName) instead of full capability records. Keeps the payload proportional to the number of resources for machine consumers such as the controller.

        resource : typing.Optional[ManageOrgDataRequestResource]
            Kubernetes resource reference (for capabilities operations)

        resource_list : typing.Optional[str]
            Comma-separated list of resources to scan (format: Kind.group or Kind for core resources). When provided without sessionId, triggers a fire-and-forget targeted scan.

        mode : typing.Optional[ManageOrgDataRequestMode]
            Scan mode: "full" triggers a fire-and-forget full cluster scan that returns immediately and scans all resources in the cluster. Mutually exclusive with resourceList.

        collection : typing.Optional[str]
            Collection name for capabilities operations (default: "capabilities", use "capabilities-policies" for pre-populated test data)

        interaction_id : typing.Optional[str]
            INTERNAL ONLY - Do not populate. Used for evaluation dataset generation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolExecutionResponse
            Tool execution result

        Examples
        --------
        from fern.management import ManageOrgDataRequestResource

        from fern import FernApi

        client = FernApi()
        client.management.execute_manage_org_data_tool(
            data_type="capabilities",
            operation="list",
            session_id="example sessionId",
            step="example step",
            response="example response",
            id="example id",
            limit=42,
            identity_only=False,
            resource=ManageOrgDataRequestResource(
                kind="example kind",
                group="example group",
                api_version="example apiVersion",
            ),
            resource_list="example resourceList",
            mode="full",
            collection="example collection",
            interaction_id="example interaction_id",
        )
        """
        _response = self._raw_client.execute_manage_org_data_tool(
            data_type=data_type,
            operation=operation,
            session_id=session_id,
            step=step,
            response=response,
            id=id,
            limit=limit,
            identity_only=identity_only,
            resource=resource,
            resource_list=resource_list,
            mode=mode,
            collection=collection,
            interaction_id=interaction_id,
            request_options=request_options,
        )
        return _response.data


class AsyncManagementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawManagementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawManagementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawManagementClient
        """
        return self._raw_client

    async def execute_manage_org_data_tool(
        self,
        *,
        data_type: ManageOrgDataRequestDataType,
        operation: ManageOrgDataRequestOperation,
        session_id: typing.Optional[str] = OMIT,
        step: typing.Optional[str] = OMIT,
        response: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        identity_only: typing.Optional[bool] = OMIT,
        resource: typing.Optional[ManageOrgDataRequestResource] = OMIT,
        resource_list: typing.Optional[str] = OMIT,
        mode: typing.Optional[ManageOrgDataRequestMode] = OMIT,
        collection: typing.Optional[str] = OMIT,
        interaction_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolExecutionResponse:
        """
        Tool for managing cluster resource capabilities. Supports scan, list, get, search, delete, deleteAll, and progress operations for cluster resource capability discovery and management. Use dataType="capabilities" to manage cluster capabilities. NOTE: Organizational patterns and policies are now managed via manageKnowledge tool (ingest documents, search, deleteByUri) with automatic AI classification.

        Parameters
        ----------
        data_type : ManageOrgDataRequestDataType
            Type of cluster data to manage: "capabilities" for resource capabilities. (Note: organizational knowledge/patterns/policies are managed via manageKnowledge tool)

        operation : ManageOrgDataRequestOperation
            Operation to perform on the cluster data

        session_id : typing.Optional[str]
            Session ID (required for continuing workflow steps, optional for progress - uses latest session if omitted)

        step : typing.Optional[str]
            Current workflow step (required when sessionId is provided)

        response : typing.Optional[str]
            User response to previous workflow step question

        id : typing.Optional[str]
            Capability ID (required for get/delete operations) or search query (required for search operations)

        limit : typing.Optional[int]
            Maximum number of items to return (must be an integer; default: 10, maximum: 10000). The response carries an explicit truncated flag, the authoritative completeness signal; totalCount equals returnedCount when not truncated and is a best-effort figure otherwise.

        identity_only : typing.Optional[bool]
            For list: return only identity fields (id, resourceName) instead of full capability records. Keeps the payload proportional to the number of resources for machine consumers such as the controller.

        resource : typing.Optional[ManageOrgDataRequestResource]
            Kubernetes resource reference (for capabilities operations)

        resource_list : typing.Optional[str]
            Comma-separated list of resources to scan (format: Kind.group or Kind for core resources). When provided without sessionId, triggers a fire-and-forget targeted scan.

        mode : typing.Optional[ManageOrgDataRequestMode]
            Scan mode: "full" triggers a fire-and-forget full cluster scan that returns immediately and scans all resources in the cluster. Mutually exclusive with resourceList.

        collection : typing.Optional[str]
            Collection name for capabilities operations (default: "capabilities", use "capabilities-policies" for pre-populated test data)

        interaction_id : typing.Optional[str]
            INTERNAL ONLY - Do not populate. Used for evaluation dataset generation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolExecutionResponse
            Tool execution result

        Examples
        --------
        import asyncio

        from fern.management import ManageOrgDataRequestResource

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.management.execute_manage_org_data_tool(
                data_type="capabilities",
                operation="list",
                session_id="example sessionId",
                step="example step",
                response="example response",
                id="example id",
                limit=42,
                identity_only=False,
                resource=ManageOrgDataRequestResource(
                    kind="example kind",
                    group="example group",
                    api_version="example apiVersion",
                ),
                resource_list="example resourceList",
                mode="full",
                collection="example collection",
                interaction_id="example interaction_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_manage_org_data_tool(
            data_type=data_type,
            operation=operation,
            session_id=session_id,
            step=step,
            response=response,
            id=id,
            limit=limit,
            identity_only=identity_only,
            resource=resource,
            resource_list=resource_list,
            mode=mode,
            collection=collection,
            interaction_id=interaction_id,
            request_options=request_options,
        )
        return _response.data
