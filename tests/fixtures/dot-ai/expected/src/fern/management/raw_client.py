

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.tool_execution_response import ToolExecutionResponse
from .types.manage_org_data_request_data_type import ManageOrgDataRequestDataType
from .types.manage_org_data_request_mode import ManageOrgDataRequestMode
from .types.manage_org_data_request_operation import ManageOrgDataRequestOperation
from .types.manage_org_data_request_resource import ManageOrgDataRequestResource
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawManagementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[ToolExecutionResponse]:
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
        HttpResponse[ToolExecutionResponse]
            Tool execution result
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/tools/manageOrgData",
            method="POST",
            json={
                "dataType": data_type,
                "operation": operation,
                "sessionId": session_id,
                "step": step,
                "response": response,
                "id": id,
                "limit": limit,
                "identityOnly": identity_only,
                "resource": convert_and_respect_annotation_metadata(
                    object_=resource, annotation=ManageOrgDataRequestResource, direction="write"
                ),
                "resourceList": resource_list,
                "mode": mode,
                "collection": collection,
                "interaction_id": interaction_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ToolExecutionResponse,
                    parse_obj_as(
                        type_=ToolExecutionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawManagementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[ToolExecutionResponse]:
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
        AsyncHttpResponse[ToolExecutionResponse]
            Tool execution result
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/tools/manageOrgData",
            method="POST",
            json={
                "dataType": data_type,
                "operation": operation,
                "sessionId": session_id,
                "step": step,
                "response": response,
                "id": id,
                "limit": limit,
                "identityOnly": identity_only,
                "resource": convert_and_respect_annotation_metadata(
                    object_=resource, annotation=ManageOrgDataRequestResource, direction="write"
                ),
                "resourceList": resource_list,
                "mode": mode,
                "collection": collection,
                "interaction_id": interaction_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ToolExecutionResponse,
                    parse_obj_as(
                        type_=ToolExecutionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
