

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..types.attributes_model import AttributesModel
from ..types.base_activity_feed_item_model import BaseActivityFeedItemModel
from ..types.creator_email_model import CreatorEmailModel
from ..types.email_response_model import EmailResponseModel
from ..types.launched_workflow_model import LaunchedWorkflowModel
from ..types.workflow_response_model import WorkflowResponseModel
from ..types.workflow_template_id_model import WorkflowTemplateIdModel
from ..types.workflows_get_approval_requests_response import WorkflowsGetApprovalRequestsResponse
from ..types.workflows_get_async_job_status_response import WorkflowsGetAsyncJobStatusResponse
from ..types.workflows_get_attachment_from_email_thread_response import WorkflowsGetAttachmentFromEmailThreadResponse
from ..types.workflows_get_document_by_key_response import WorkflowsGetDocumentByKeyResponse
from ..types.workflows_get_email_threads_response import WorkflowsGetEmailThreadsResponse
from ..types.workflows_get_turn_history_response import WorkflowsGetTurnHistoryResponse
from ..types.workflows_get_workflow_schema_response import WorkflowsGetWorkflowSchemaResponse
from ..types.workflows_launch_asynchronously_response import WorkflowsLaunchAsynchronouslyResponse
from ..types.workflows_list_all_participants_response import WorkflowsListAllParticipantsResponse
from ..types.workflows_list_all_response import WorkflowsListAllResponse
from ..types.workflows_list_all_workflow_schemas_response import WorkflowsListAllWorkflowSchemasResponse
from ..types.workflows_list_approvals_response import WorkflowsListApprovalsResponse
from ..types.workflows_list_signatures_response import WorkflowsListSignaturesResponse
from ..types.workflows_update_approval_status_response import WorkflowsUpdateApprovalStatusResponse
from ..types.workflows_update_metadata_response import WorkflowsUpdateMetadataResponse
from .types.workflows_list_all_request_status import WorkflowsListAllRequestStatus
from .types.workflows_revert_to_review_request_user import WorkflowsRevertToReviewRequestUser
from .types.workflows_update_approval_status_request_status import WorkflowsUpdateApprovalStatusRequestStatus
from .types.workflows_update_approval_status_request_user import WorkflowsUpdateApprovalStatusRequestUser
from .types.workflows_update_metadata_request_updates_item import WorkflowsUpdateMetadataRequestUpdatesItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawWorkflowsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def listall(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        status: typing.Optional[WorkflowsListAllRequestStatus] = None,
        template: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkflowsListAllResponse]:
        """
        List all workflows in your Ironclad account.

        Parameters
        ----------
        page : typing.Optional[int]
            The page number used when paginating through a list of results.

        page_size : typing.Optional[int]
            A limit of the number of results to return.

        status : typing.Optional[WorkflowsListAllRequestStatus]
            Filter the workflows that are listed based on their status. If this parameter is omitted, `active` workflows will be returned. Active workflows include workflows in the Create, Review, Sign, and Archive stages.

        template : typing.Optional[str]
            Filter workflows to a specific Template ID.

        last_updated : typing.Optional[str]
            Retrieve workflows that have been updated since a UTC date.

        filter : typing.Optional[str]
            Filter workflows using a formula. The workflow attribute ID should be enclosed in brackets `[ ]` and the value should be enclosed in single quotes `' '`.

            Workflow attributes for a specific workflow design can be identified using the [List All Workflow Schemas](https://developer.ironcladapp.com/reference/list-all-workflow-schemas) endpoint.

            Supported formula operations include:

            <ul>
              <li><code>Equals</code></li>
              <li><code>Contains</code></li>
              <li><code>And</code></li>
              <li><code>Or</code></li>
            </ul>
            For more information on writing formulas, please refer to
            <a href="https://ironcladapp.com/formulas/#company%20display%20name">this article</a>.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkflowsListAllResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            "workflows",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
                "status": status,
                "template": template,
                "lastUpdated": last_updated,
                "filter": filter,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsListAllResponse,
                    parse_obj_as(
                        type_=WorkflowsListAllResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def createsyncworkflow(
        self,
        *,
        template: WorkflowTemplateIdModel,
        creator: CreatorEmailModel,
        attributes: AttributesModel,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LaunchedWorkflowModel]:
        """
        Launch a new Workflow synchronously.

        Parameters
        ----------
        template : WorkflowTemplateIdModel

        creator : CreatorEmailModel

        attributes : AttributesModel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LaunchedWorkflowModel]
            Launched Workflow Response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "workflows",
            method="POST",
            json={
                "template": template,
                "creator": convert_and_respect_annotation_metadata(
                    object_=creator, annotation=CreatorEmailModel, direction="write"
                ),
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=AttributesModel, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LaunchedWorkflowModel,
                    parse_obj_as(
                        type_=LaunchedWorkflowModel,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def launchasynchronously(
        self,
        *,
        template: WorkflowTemplateIdModel,
        creator: CreatorEmailModel,
        attributes: AttributesModel,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkflowsLaunchAsynchronouslyResponse]:
        """
        Launch a new Workflow asynchronously for non-blocking performance, which is helpful when/if you provide files to the Workflow.

        Parameters
        ----------
        template : WorkflowTemplateIdModel

        creator : CreatorEmailModel

        attributes : AttributesModel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkflowsLaunchAsynchronouslyResponse]
            The response of the initiated async workflow launch.
        """
        _response = self._client_wrapper.httpx_client.request(
            "workflows/async",
            method="POST",
            json={
                "template": template,
                "creator": convert_and_respect_annotation_metadata(
                    object_=creator, annotation=CreatorEmailModel, direction="write"
                ),
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=AttributesModel, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsLaunchAsynchronouslyResponse,
                    parse_obj_as(
                        type_=WorkflowsLaunchAsynchronouslyResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getasyncjobstatus(
        self, async_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WorkflowsGetAsyncJobStatusResponse]:
        """
        Check the status of a Workflow you created while using the [Create a Workflow Async](https://developer.ironcladapp.com/reference/create-a-workflow-sync-vs-async#create-a-new-workflow-async) route.

        Parameters
        ----------
        async_job_id : str
            The identifier provided in the response of creating a Workflow asynchronously.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkflowsGetAsyncJobStatusResponse]
            The status of the workflow launch.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflows/async/{encode_path_param(async_job_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsGetAsyncJobStatusResponse,
                    parse_obj_as(
                        type_=WorkflowsGetAsyncJobStatusResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getworkflow(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WorkflowResponseModel]:
        """
        View the data associated with a specific workflow

        Parameters
        ----------
        id : str
            The unique identifier or Ironclad ID of a workflow.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkflowResponseModel]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowResponseModel,
                    parse_obj_as(
                        type_=WorkflowResponseModel,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def listapprovals(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WorkflowsListApprovalsResponse]:
        """
        Returns a list of approvals for the workflow. The `approvalGroups` property will display only triggered approvals (i.e. conditional approvals that have not been triggered will not appear).

        Parameters
        ----------
        id : str
            The unique identifier or Ironclad ID of a workflow.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkflowsListApprovalsResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/approvals",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsListApprovalsResponse,
                    parse_obj_as(
                        type_=WorkflowsListApprovalsResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getapprovalrequests(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        actor_details: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkflowsGetApprovalRequestsResponse]:
        """
        Returns a list of approval requests that have taken place on the workflow.

        Parameters
        ----------
        id : str
            The unique identifier or Ironclad ID of a workflow.

        page : typing.Optional[int]
            The page number used when paginating through a list of results.

        page_size : typing.Optional[int]
            A limit of the number of results to return.

        actor_details : typing.Optional[bool]
            An optional boolean parameter that adds additional information about the actor to each item in the response. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkflowsGetApprovalRequestsResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/approval-requests",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
                "actorDetails": actor_details,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsGetApprovalRequestsResponse,
                    parse_obj_as(
                        type_=WorkflowsGetApprovalRequestsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def updateapprovalstatus(
        self,
        id: str,
        role_id: str,
        *,
        user: WorkflowsUpdateApprovalStatusRequestUser,
        status: WorkflowsUpdateApprovalStatusRequestStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkflowsUpdateApprovalStatusResponse]:
        """
        Updates an approval to the specified status. Approvals can only be updated during the Review step.

        Parameters
        ----------
        id : str
            The unique identifier or Ironclad ID of a workflow.

        role_id : str
            The unique identifier of the approver role whose status should be changed. This identifier can be retrieved using the `GET /workflows/{id}/approvals` endpoint.

        user : WorkflowsUpdateApprovalStatusRequestUser
            The Ironclad user approving the workflow. The user must be currently assigned as the approver.

        status : WorkflowsUpdateApprovalStatusRequestStatus
            The new approval status.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkflowsUpdateApprovalStatusResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/approvals/{encode_path_param(role_id)}",
            method="PATCH",
            json={
                "user": convert_and_respect_annotation_metadata(
                    object_=user, annotation=WorkflowsUpdateApprovalStatusRequestUser, direction="write"
                ),
                "status": status,
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
                    WorkflowsUpdateApprovalStatusResponse,
                    parse_obj_as(
                        type_=WorkflowsUpdateApprovalStatusResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getturnhistory(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkflowsGetTurnHistoryResponse]:
        """
        An array of objects for each turn on a workflow.

        Parameters
        ----------
        id : str
            The unique identifier or Ironclad ID of a workflow.

        page : typing.Optional[int]
            The page number used when paginating through a list of results.

        page_size : typing.Optional[int]
            A limit of the number of results to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkflowsGetTurnHistoryResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/turn-history",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsGetTurnHistoryResponse,
                    parse_obj_as(
                        type_=WorkflowsGetTurnHistoryResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def listsignatures(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WorkflowsListSignaturesResponse]:
        """
        Returns a list of workflow signers and the status of their signature.

        Parameters
        ----------
        id : str
            The unique identifier or Ironclad ID of a workflow.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkflowsListSignaturesResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/signatures",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsListSignaturesResponse,
                    parse_obj_as(
                        type_=WorkflowsListSignaturesResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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

    def listallparticipants(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        email: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkflowsListAllParticipantsResponse]:
        """
        Returns a list of workflow participants.

        Parameters
        ----------
        id : str
            The unique identifier or Ironclad ID of a workflow.

        page : typing.Optional[int]
            The page number used when paginating through a list of results.

        page_size : typing.Optional[int]
            A limit of the number of results to return.

        email : typing.Optional[str]
            The Ironclad user's email address.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkflowsListAllParticipantsResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/participants",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
                "email": email,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsListAllParticipantsResponse,
                    parse_obj_as(
                        type_=WorkflowsListAllParticipantsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def reverttoreview(
        self,
        id: str,
        *,
        user: WorkflowsRevertToReviewRequestUser,
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Reverts a workflow to the Review step. Only workflows sourced from Workflow Designer and in the Sign step can be reverted.

        Parameters
        ----------
        id : str
            The unique identifier or Ironclad ID of a workflow.

        user : WorkflowsRevertToReviewRequestUser
            The Ironclad user reverting the workflow to the Review step. The user must be a participant on the workflow.

        as_user_email : typing.Optional[str]
            Filters the list of workflow schemas based on the permissions of a user associated with the specified user email. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions

        as_user_id : typing.Optional[str]
            Filters the list of workflow schemas based on the permissions of a user associated with the specified user id. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/revert-to-review",
            method="PATCH",
            json={
                "user": convert_and_respect_annotation_metadata(
                    object_=user, annotation=WorkflowsRevertToReviewRequestUser, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "x-as-user-email": str(as_user_email) if as_user_email is not None else None,
                "x-as-user-id": str(as_user_id) if as_user_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def createcomment(
        self,
        id: str,
        *,
        creator: CreatorEmailModel,
        comment: str,
        add_users_to_workflow: typing.Optional[bool] = OMIT,
        replied_to_activity_feed_message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BaseActivityFeedItemModel]:
        """
        Creates a comment in the specified workflow's activity feed.

        Parameters
        ----------
        id : str
            The unique identifier or Ironclad ID of a workflow.

        creator : CreatorEmailModel

        comment : str
            The comment text to add, accepts user mentions in the form of <@user_id_or_email>.

        add_users_to_workflow : typing.Optional[bool]
            Must be set to true if mentioning users who are not participants on the workflow.

        replied_to_activity_feed_message_id : typing.Optional[str]
            Use to specify the comment to reply to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BaseActivityFeedItemModel]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/comments",
            method="POST",
            json={
                "creator": convert_and_respect_annotation_metadata(
                    object_=creator, annotation=CreatorEmailModel, direction="write"
                ),
                "comment": comment,
                "addUsersToWorkflow": add_users_to_workflow,
                "repliedToActivityFeedMessageId": replied_to_activity_feed_message_id,
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
                    BaseActivityFeedItemModel,
                    parse_obj_as(
                        type_=BaseActivityFeedItemModel,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def updatemetadata(
        self,
        id: str,
        *,
        updates: typing.Sequence[WorkflowsUpdateMetadataRequestUpdatesItem],
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkflowsUpdateMetadataResponse]:
        """
        The workflow must be in the Review step in order for its data to be updated. Use the `remove` action to clear field values and the `set` action to add or modify values. Form validation is enforced; required fields cannot be removed and any required fields triggered by conditions must be populated.

        Parameters
        ----------
        id : str
            The unique identifier or Ironclad ID of a workflow.

        updates : typing.Sequence[WorkflowsUpdateMetadataRequestUpdatesItem]

        as_user_email : typing.Optional[str]
            Filters the list of workflow schemas based on the permissions of a user associated with the specified user email. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions

        as_user_id : typing.Optional[str]
            Filters the list of workflow schemas based on the permissions of a user associated with the specified user id. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions

        comment : typing.Optional[str]
            A comment that explains the updates you are making to the workflow.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkflowsUpdateMetadataResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/attributes",
            method="PATCH",
            json={
                "updates": convert_and_respect_annotation_metadata(
                    object_=updates,
                    annotation=typing.Sequence[WorkflowsUpdateMetadataRequestUpdatesItem],
                    direction="write",
                ),
                "comment": comment,
            },
            headers={
                "content-type": "application/json",
                "x-as-user-email": str(as_user_email) if as_user_email is not None else None,
                "x-as-user-id": str(as_user_id) if as_user_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsUpdateMetadataResponse,
                    parse_obj_as(
                        type_=WorkflowsUpdateMetadataResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getdocumentbykey(
        self, id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WorkflowsGetDocumentByKeyResponse]:
        """
        Download a document associated with a specific workflow via a reference to its document key

        Parameters
        ----------
        id : str
            The unique identifier or Ironclad ID of a workflow.

        key : str
            The unique identifier for the attachment. This key can be located using the [Retrieve a Workflow](https://developer.ironcladapp.com/reference/retrieve-a-workflow) endpoint. In the response, locate the file attribute (e.g., `draft`) and look at its `download` parameter. The download parameter includes the key at the end of the URL `.../document/{ATTACHMENT_KEY}/download`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkflowsGetDocumentByKeyResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/document/{encode_path_param(key)}/download",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsGetDocumentByKeyResponse,
                    parse_obj_as(
                        type_=WorkflowsGetDocumentByKeyResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getemailthreads(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkflowsGetEmailThreadsResponse]:
        """
        List all email threads in the specified workflow

        Parameters
        ----------
        id : str
            The unique identifier of a workflow

        page : typing.Optional[int]
            The page number used when paginating through a list of results.

        page_size : typing.Optional[int]
            A limit of the number of results to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkflowsGetEmailThreadsResponse]
            GET Emails Response.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/emails",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsGetEmailThreadsResponse,
                    parse_obj_as(
                        type_=WorkflowsGetEmailThreadsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getemailthread(
        self, id: str, email_thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EmailResponseModel]:
        """
        List a single email thread for a specified workflow

        Parameters
        ----------
        id : str
            The unique identifier of a workflow

        email_thread_id : str
            The unique identifier of an email thread

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EmailResponseModel]
            GET Email Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/emails/{encode_path_param(email_thread_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmailResponseModel,
                    parse_obj_as(
                        type_=EmailResponseModel,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getattachmentfromemailthread(
        self,
        id: str,
        email_thread_id: str,
        attachment_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkflowsGetAttachmentFromEmailThreadResponse]:
        """
        Retrieve an attachment from the specified email thread

        Parameters
        ----------
        id : str
            The unique identifier of a workflow

        email_thread_id : str
            The unique identifier of an email thread

        attachment_id : str
            The unique identifier for the attachment. This key can be located using the [Retrieve email threads from workflow](https://developer.ironcladapp.com/reference/retrieve-emails) endpoint. In the response, locate the file attribute (e.g., `attachments`) and look at its `download` parameter. The download parameter includes the key at the end of the URL `...emails/{emailThreadId}/attachment/{ATTACHMENT_ID}`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkflowsGetAttachmentFromEmailThreadResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/emails/{encode_path_param(email_thread_id)}/attachments/{encode_path_param(attachment_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsGetAttachmentFromEmailThreadResponse,
                    parse_obj_as(
                        type_=WorkflowsGetAttachmentFromEmailThreadResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def listallworkflowschemas(
        self,
        *,
        form: str,
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkflowsListAllWorkflowSchemasResponse]:
        """
        Returns a list of workflow schemas. Each schema specifies the fields used in the workflow's launch form.

        Parameters
        ----------
        form : str
            The launch form is the only form supported at this time.

        as_user_email : typing.Optional[str]
            Filters the list of workflow schemas based on the permissions of a user associated with the specified user email. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions

        as_user_id : typing.Optional[str]
            Filters the list of workflow schemas based on the permissions of a user associated with the specified user id. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkflowsListAllWorkflowSchemasResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            "workflow-schemas",
            method="GET",
            params={
                "form": form,
            },
            headers={
                "x-as-user-email": str(as_user_email) if as_user_email is not None else None,
                "x-as-user-id": str(as_user_id) if as_user_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsListAllWorkflowSchemasResponse,
                    parse_obj_as(
                        type_=WorkflowsListAllWorkflowSchemasResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getworkflowschema(
        self,
        id: str,
        *,
        form: typing.Optional[str] = None,
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkflowsGetWorkflowSchemaResponse]:
        """
        Returns the fields used in the workflow's launch form.

        Parameters
        ----------
        id : str
            The unique identifier of a schema (see explanation of [Template ID](https://developer.ironcladapp.com/reference/getting-started-api)). A list of identifiers can be retrieved using the `GET /workflow-schemas` endpoint. Only published workflows will have an identifier.

        form : typing.Optional[str]

        as_user_email : typing.Optional[str]
            Filters the list of workflow schemas based on the permissions of a user associated with the specified user email. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions

        as_user_id : typing.Optional[str]
            Filters the list of workflow schemas based on the permissions of a user associated with the specified user id. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkflowsGetWorkflowSchemaResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflow-schemas/{encode_path_param(id)}",
            method="GET",
            params={
                "form": form,
            },
            headers={
                "x-as-user-email": str(as_user_email) if as_user_email is not None else None,
                "x-as-user-id": str(as_user_id) if as_user_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsGetWorkflowSchemaResponse,
                    parse_obj_as(
                        type_=WorkflowsGetWorkflowSchemaResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawWorkflowsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def listall(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        status: typing.Optional[WorkflowsListAllRequestStatus] = None,
        template: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WorkflowsListAllResponse]:
        """
        List all workflows in your Ironclad account.

        Parameters
        ----------
        page : typing.Optional[int]
            The page number used when paginating through a list of results.

        page_size : typing.Optional[int]
            A limit of the number of results to return.

        status : typing.Optional[WorkflowsListAllRequestStatus]
            Filter the workflows that are listed based on their status. If this parameter is omitted, `active` workflows will be returned. Active workflows include workflows in the Create, Review, Sign, and Archive stages.

        template : typing.Optional[str]
            Filter workflows to a specific Template ID.

        last_updated : typing.Optional[str]
            Retrieve workflows that have been updated since a UTC date.

        filter : typing.Optional[str]
            Filter workflows using a formula. The workflow attribute ID should be enclosed in brackets `[ ]` and the value should be enclosed in single quotes `' '`.

            Workflow attributes for a specific workflow design can be identified using the [List All Workflow Schemas](https://developer.ironcladapp.com/reference/list-all-workflow-schemas) endpoint.

            Supported formula operations include:

            <ul>
              <li><code>Equals</code></li>
              <li><code>Contains</code></li>
              <li><code>And</code></li>
              <li><code>Or</code></li>
            </ul>
            For more information on writing formulas, please refer to
            <a href="https://ironcladapp.com/formulas/#company%20display%20name">this article</a>.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkflowsListAllResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "workflows",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
                "status": status,
                "template": template,
                "lastUpdated": last_updated,
                "filter": filter,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsListAllResponse,
                    parse_obj_as(
                        type_=WorkflowsListAllResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def createsyncworkflow(
        self,
        *,
        template: WorkflowTemplateIdModel,
        creator: CreatorEmailModel,
        attributes: AttributesModel,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LaunchedWorkflowModel]:
        """
        Launch a new Workflow synchronously.

        Parameters
        ----------
        template : WorkflowTemplateIdModel

        creator : CreatorEmailModel

        attributes : AttributesModel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LaunchedWorkflowModel]
            Launched Workflow Response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "workflows",
            method="POST",
            json={
                "template": template,
                "creator": convert_and_respect_annotation_metadata(
                    object_=creator, annotation=CreatorEmailModel, direction="write"
                ),
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=AttributesModel, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LaunchedWorkflowModel,
                    parse_obj_as(
                        type_=LaunchedWorkflowModel,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def launchasynchronously(
        self,
        *,
        template: WorkflowTemplateIdModel,
        creator: CreatorEmailModel,
        attributes: AttributesModel,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WorkflowsLaunchAsynchronouslyResponse]:
        """
        Launch a new Workflow asynchronously for non-blocking performance, which is helpful when/if you provide files to the Workflow.

        Parameters
        ----------
        template : WorkflowTemplateIdModel

        creator : CreatorEmailModel

        attributes : AttributesModel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkflowsLaunchAsynchronouslyResponse]
            The response of the initiated async workflow launch.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "workflows/async",
            method="POST",
            json={
                "template": template,
                "creator": convert_and_respect_annotation_metadata(
                    object_=creator, annotation=CreatorEmailModel, direction="write"
                ),
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=AttributesModel, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsLaunchAsynchronouslyResponse,
                    parse_obj_as(
                        type_=WorkflowsLaunchAsynchronouslyResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getasyncjobstatus(
        self, async_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WorkflowsGetAsyncJobStatusResponse]:
        """
        Check the status of a Workflow you created while using the [Create a Workflow Async](https://developer.ironcladapp.com/reference/create-a-workflow-sync-vs-async#create-a-new-workflow-async) route.

        Parameters
        ----------
        async_job_id : str
            The identifier provided in the response of creating a Workflow asynchronously.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkflowsGetAsyncJobStatusResponse]
            The status of the workflow launch.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflows/async/{encode_path_param(async_job_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsGetAsyncJobStatusResponse,
                    parse_obj_as(
                        type_=WorkflowsGetAsyncJobStatusResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getworkflow(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WorkflowResponseModel]:
        """
        View the data associated with a specific workflow

        Parameters
        ----------
        id : str
            The unique identifier or Ironclad ID of a workflow.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkflowResponseModel]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowResponseModel,
                    parse_obj_as(
                        type_=WorkflowResponseModel,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def listapprovals(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WorkflowsListApprovalsResponse]:
        """
        Returns a list of approvals for the workflow. The `approvalGroups` property will display only triggered approvals (i.e. conditional approvals that have not been triggered will not appear).

        Parameters
        ----------
        id : str
            The unique identifier or Ironclad ID of a workflow.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkflowsListApprovalsResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/approvals",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsListApprovalsResponse,
                    parse_obj_as(
                        type_=WorkflowsListApprovalsResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getapprovalrequests(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        actor_details: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WorkflowsGetApprovalRequestsResponse]:
        """
        Returns a list of approval requests that have taken place on the workflow.

        Parameters
        ----------
        id : str
            The unique identifier or Ironclad ID of a workflow.

        page : typing.Optional[int]
            The page number used when paginating through a list of results.

        page_size : typing.Optional[int]
            A limit of the number of results to return.

        actor_details : typing.Optional[bool]
            An optional boolean parameter that adds additional information about the actor to each item in the response. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkflowsGetApprovalRequestsResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/approval-requests",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
                "actorDetails": actor_details,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsGetApprovalRequestsResponse,
                    parse_obj_as(
                        type_=WorkflowsGetApprovalRequestsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def updateapprovalstatus(
        self,
        id: str,
        role_id: str,
        *,
        user: WorkflowsUpdateApprovalStatusRequestUser,
        status: WorkflowsUpdateApprovalStatusRequestStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WorkflowsUpdateApprovalStatusResponse]:
        """
        Updates an approval to the specified status. Approvals can only be updated during the Review step.

        Parameters
        ----------
        id : str
            The unique identifier or Ironclad ID of a workflow.

        role_id : str
            The unique identifier of the approver role whose status should be changed. This identifier can be retrieved using the `GET /workflows/{id}/approvals` endpoint.

        user : WorkflowsUpdateApprovalStatusRequestUser
            The Ironclad user approving the workflow. The user must be currently assigned as the approver.

        status : WorkflowsUpdateApprovalStatusRequestStatus
            The new approval status.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkflowsUpdateApprovalStatusResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/approvals/{encode_path_param(role_id)}",
            method="PATCH",
            json={
                "user": convert_and_respect_annotation_metadata(
                    object_=user, annotation=WorkflowsUpdateApprovalStatusRequestUser, direction="write"
                ),
                "status": status,
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
                    WorkflowsUpdateApprovalStatusResponse,
                    parse_obj_as(
                        type_=WorkflowsUpdateApprovalStatusResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getturnhistory(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WorkflowsGetTurnHistoryResponse]:
        """
        An array of objects for each turn on a workflow.

        Parameters
        ----------
        id : str
            The unique identifier or Ironclad ID of a workflow.

        page : typing.Optional[int]
            The page number used when paginating through a list of results.

        page_size : typing.Optional[int]
            A limit of the number of results to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkflowsGetTurnHistoryResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/turn-history",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsGetTurnHistoryResponse,
                    parse_obj_as(
                        type_=WorkflowsGetTurnHistoryResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def listsignatures(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WorkflowsListSignaturesResponse]:
        """
        Returns a list of workflow signers and the status of their signature.

        Parameters
        ----------
        id : str
            The unique identifier or Ironclad ID of a workflow.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkflowsListSignaturesResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/signatures",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsListSignaturesResponse,
                    parse_obj_as(
                        type_=WorkflowsListSignaturesResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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

    async def listallparticipants(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        email: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WorkflowsListAllParticipantsResponse]:
        """
        Returns a list of workflow participants.

        Parameters
        ----------
        id : str
            The unique identifier or Ironclad ID of a workflow.

        page : typing.Optional[int]
            The page number used when paginating through a list of results.

        page_size : typing.Optional[int]
            A limit of the number of results to return.

        email : typing.Optional[str]
            The Ironclad user's email address.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkflowsListAllParticipantsResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/participants",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
                "email": email,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsListAllParticipantsResponse,
                    parse_obj_as(
                        type_=WorkflowsListAllParticipantsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def reverttoreview(
        self,
        id: str,
        *,
        user: WorkflowsRevertToReviewRequestUser,
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Reverts a workflow to the Review step. Only workflows sourced from Workflow Designer and in the Sign step can be reverted.

        Parameters
        ----------
        id : str
            The unique identifier or Ironclad ID of a workflow.

        user : WorkflowsRevertToReviewRequestUser
            The Ironclad user reverting the workflow to the Review step. The user must be a participant on the workflow.

        as_user_email : typing.Optional[str]
            Filters the list of workflow schemas based on the permissions of a user associated with the specified user email. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions

        as_user_id : typing.Optional[str]
            Filters the list of workflow schemas based on the permissions of a user associated with the specified user id. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/revert-to-review",
            method="PATCH",
            json={
                "user": convert_and_respect_annotation_metadata(
                    object_=user, annotation=WorkflowsRevertToReviewRequestUser, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "x-as-user-email": str(as_user_email) if as_user_email is not None else None,
                "x-as-user-id": str(as_user_id) if as_user_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def createcomment(
        self,
        id: str,
        *,
        creator: CreatorEmailModel,
        comment: str,
        add_users_to_workflow: typing.Optional[bool] = OMIT,
        replied_to_activity_feed_message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BaseActivityFeedItemModel]:
        """
        Creates a comment in the specified workflow's activity feed.

        Parameters
        ----------
        id : str
            The unique identifier or Ironclad ID of a workflow.

        creator : CreatorEmailModel

        comment : str
            The comment text to add, accepts user mentions in the form of <@user_id_or_email>.

        add_users_to_workflow : typing.Optional[bool]
            Must be set to true if mentioning users who are not participants on the workflow.

        replied_to_activity_feed_message_id : typing.Optional[str]
            Use to specify the comment to reply to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BaseActivityFeedItemModel]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/comments",
            method="POST",
            json={
                "creator": convert_and_respect_annotation_metadata(
                    object_=creator, annotation=CreatorEmailModel, direction="write"
                ),
                "comment": comment,
                "addUsersToWorkflow": add_users_to_workflow,
                "repliedToActivityFeedMessageId": replied_to_activity_feed_message_id,
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
                    BaseActivityFeedItemModel,
                    parse_obj_as(
                        type_=BaseActivityFeedItemModel,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def updatemetadata(
        self,
        id: str,
        *,
        updates: typing.Sequence[WorkflowsUpdateMetadataRequestUpdatesItem],
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WorkflowsUpdateMetadataResponse]:
        """
        The workflow must be in the Review step in order for its data to be updated. Use the `remove` action to clear field values and the `set` action to add or modify values. Form validation is enforced; required fields cannot be removed and any required fields triggered by conditions must be populated.

        Parameters
        ----------
        id : str
            The unique identifier or Ironclad ID of a workflow.

        updates : typing.Sequence[WorkflowsUpdateMetadataRequestUpdatesItem]

        as_user_email : typing.Optional[str]
            Filters the list of workflow schemas based on the permissions of a user associated with the specified user email. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions

        as_user_id : typing.Optional[str]
            Filters the list of workflow schemas based on the permissions of a user associated with the specified user id. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions

        comment : typing.Optional[str]
            A comment that explains the updates you are making to the workflow.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkflowsUpdateMetadataResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/attributes",
            method="PATCH",
            json={
                "updates": convert_and_respect_annotation_metadata(
                    object_=updates,
                    annotation=typing.Sequence[WorkflowsUpdateMetadataRequestUpdatesItem],
                    direction="write",
                ),
                "comment": comment,
            },
            headers={
                "content-type": "application/json",
                "x-as-user-email": str(as_user_email) if as_user_email is not None else None,
                "x-as-user-id": str(as_user_id) if as_user_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsUpdateMetadataResponse,
                    parse_obj_as(
                        type_=WorkflowsUpdateMetadataResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getdocumentbykey(
        self, id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WorkflowsGetDocumentByKeyResponse]:
        """
        Download a document associated with a specific workflow via a reference to its document key

        Parameters
        ----------
        id : str
            The unique identifier or Ironclad ID of a workflow.

        key : str
            The unique identifier for the attachment. This key can be located using the [Retrieve a Workflow](https://developer.ironcladapp.com/reference/retrieve-a-workflow) endpoint. In the response, locate the file attribute (e.g., `draft`) and look at its `download` parameter. The download parameter includes the key at the end of the URL `.../document/{ATTACHMENT_KEY}/download`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkflowsGetDocumentByKeyResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/document/{encode_path_param(key)}/download",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsGetDocumentByKeyResponse,
                    parse_obj_as(
                        type_=WorkflowsGetDocumentByKeyResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getemailthreads(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WorkflowsGetEmailThreadsResponse]:
        """
        List all email threads in the specified workflow

        Parameters
        ----------
        id : str
            The unique identifier of a workflow

        page : typing.Optional[int]
            The page number used when paginating through a list of results.

        page_size : typing.Optional[int]
            A limit of the number of results to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkflowsGetEmailThreadsResponse]
            GET Emails Response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/emails",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsGetEmailThreadsResponse,
                    parse_obj_as(
                        type_=WorkflowsGetEmailThreadsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getemailthread(
        self, id: str, email_thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EmailResponseModel]:
        """
        List a single email thread for a specified workflow

        Parameters
        ----------
        id : str
            The unique identifier of a workflow

        email_thread_id : str
            The unique identifier of an email thread

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EmailResponseModel]
            GET Email Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/emails/{encode_path_param(email_thread_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmailResponseModel,
                    parse_obj_as(
                        type_=EmailResponseModel,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getattachmentfromemailthread(
        self,
        id: str,
        email_thread_id: str,
        attachment_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WorkflowsGetAttachmentFromEmailThreadResponse]:
        """
        Retrieve an attachment from the specified email thread

        Parameters
        ----------
        id : str
            The unique identifier of a workflow

        email_thread_id : str
            The unique identifier of an email thread

        attachment_id : str
            The unique identifier for the attachment. This key can be located using the [Retrieve email threads from workflow](https://developer.ironcladapp.com/reference/retrieve-emails) endpoint. In the response, locate the file attribute (e.g., `attachments`) and look at its `download` parameter. The download parameter includes the key at the end of the URL `...emails/{emailThreadId}/attachment/{ATTACHMENT_ID}`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkflowsGetAttachmentFromEmailThreadResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/emails/{encode_path_param(email_thread_id)}/attachments/{encode_path_param(attachment_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsGetAttachmentFromEmailThreadResponse,
                    parse_obj_as(
                        type_=WorkflowsGetAttachmentFromEmailThreadResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def listallworkflowschemas(
        self,
        *,
        form: str,
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WorkflowsListAllWorkflowSchemasResponse]:
        """
        Returns a list of workflow schemas. Each schema specifies the fields used in the workflow's launch form.

        Parameters
        ----------
        form : str
            The launch form is the only form supported at this time.

        as_user_email : typing.Optional[str]
            Filters the list of workflow schemas based on the permissions of a user associated with the specified user email. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions

        as_user_id : typing.Optional[str]
            Filters the list of workflow schemas based on the permissions of a user associated with the specified user id. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkflowsListAllWorkflowSchemasResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "workflow-schemas",
            method="GET",
            params={
                "form": form,
            },
            headers={
                "x-as-user-email": str(as_user_email) if as_user_email is not None else None,
                "x-as-user-id": str(as_user_id) if as_user_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsListAllWorkflowSchemasResponse,
                    parse_obj_as(
                        type_=WorkflowsListAllWorkflowSchemasResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getworkflowschema(
        self,
        id: str,
        *,
        form: typing.Optional[str] = None,
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WorkflowsGetWorkflowSchemaResponse]:
        """
        Returns the fields used in the workflow's launch form.

        Parameters
        ----------
        id : str
            The unique identifier of a schema (see explanation of [Template ID](https://developer.ironcladapp.com/reference/getting-started-api)). A list of identifiers can be retrieved using the `GET /workflow-schemas` endpoint. Only published workflows will have an identifier.

        form : typing.Optional[str]

        as_user_email : typing.Optional[str]
            Filters the list of workflow schemas based on the permissions of a user associated with the specified user email. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions

        as_user_id : typing.Optional[str]
            Filters the list of workflow schemas based on the permissions of a user associated with the specified user id. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkflowsGetWorkflowSchemaResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflow-schemas/{encode_path_param(id)}",
            method="GET",
            params={
                "form": form,
            },
            headers={
                "x-as-user-email": str(as_user_email) if as_user_email is not None else None,
                "x-as-user-id": str(as_user_id) if as_user_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowsGetWorkflowSchemaResponse,
                    parse_obj_as(
                        type_=WorkflowsGetWorkflowSchemaResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
