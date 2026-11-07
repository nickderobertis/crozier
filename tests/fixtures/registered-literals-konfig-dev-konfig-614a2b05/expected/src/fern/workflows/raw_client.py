

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
from ..types.comment_activity_model import CommentActivityModel
from ..types.creator_email_model import CreatorEmailModel
from ..types.email_response_model import EmailResponseModel
from ..types.launched_workflow_model import LaunchedWorkflowModel
from ..types.workflow_response_model import WorkflowResponseModel
from ..types.workflow_template_id_model import WorkflowTemplateIdModel
from .types.approval_requests_response import ApprovalRequestsResponse
from .types.create_a_new_workflow_async_response import CreateANewWorkflowAsyncResponse
from .types.deprecated_create_a_comment_on_a_workflow_response import DeprecatedCreateACommentOnAWorkflowResponse
from .types.list_all_workflow_approvals_response import ListAllWorkflowApprovalsResponse
from .types.list_all_workflow_participants_response import ListAllWorkflowParticipantsResponse
from .types.list_all_workflow_schemas_response import ListAllWorkflowSchemasResponse
from .types.list_all_workflow_signers_response import ListAllWorkflowSignersResponse
from .types.list_all_workflows_request_status import ListAllWorkflowsRequestStatus
from .types.list_all_workflows_response import ListAllWorkflowsResponse
from .types.retrieve_a_workflow_document_response import RetrieveAWorkflowDocumentResponse
from .types.retrieve_a_workflow_schema_response import RetrieveAWorkflowSchemaResponse
from .types.retrieve_asynchronous_workflow_status_response import RetrieveAsynchronousWorkflowStatusResponse
from .types.retrieve_attachment_from_email_thread_response import RetrieveAttachmentFromEmailThreadResponse
from .types.retrieve_email_threads_from_workflow_response import RetrieveEmailThreadsFromWorkflowResponse
from .types.revert_to_review_request_user import RevertToReviewRequestUser
from .types.turn_history_response import TurnHistoryResponse
from .types.update_workflow_approval_request_status import UpdateWorkflowApprovalRequestStatus
from .types.update_workflow_approval_request_user import UpdateWorkflowApprovalRequestUser
from .types.update_workflow_metadata_request_updates_item import UpdateWorkflowMetadataRequestUpdatesItem
from .types.update_workflow_metadata_response import UpdateWorkflowMetadataResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawWorkflowsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_workflows(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        status: typing.Optional[ListAllWorkflowsRequestStatus] = None,
        template: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListAllWorkflowsResponse]:
        """
        List all workflows in your Ironclad account.

        Parameters
        ----------
        page : typing.Optional[int]
            The page number used when paginating through a list of results.

        page_size : typing.Optional[int]
            A limit of the number of results to return.

        status : typing.Optional[ListAllWorkflowsRequestStatus]
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
        HttpResponse[ListAllWorkflowsResponse]
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
                    ListAllWorkflowsResponse,
                    parse_obj_as(
                        type_=ListAllWorkflowsResponse,
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

    def launch_a_new_workflow(
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

    def create_a_new_workflow_async(
        self,
        *,
        template: WorkflowTemplateIdModel,
        creator: CreatorEmailModel,
        attributes: AttributesModel,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateANewWorkflowAsyncResponse]:
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
        HttpResponse[CreateANewWorkflowAsyncResponse]
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
                    CreateANewWorkflowAsyncResponse,
                    parse_obj_as(
                        type_=CreateANewWorkflowAsyncResponse,
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

    def retrieve_asynchronous_workflow_status(
        self, async_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveAsynchronousWorkflowStatusResponse]:
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
        HttpResponse[RetrieveAsynchronousWorkflowStatusResponse]
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
                    RetrieveAsynchronousWorkflowStatusResponse,
                    parse_obj_as(
                        type_=RetrieveAsynchronousWorkflowStatusResponse,
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

    def retrieve_a_workflow(
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

    def list_all_workflow_approvals(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListAllWorkflowApprovalsResponse]:
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
        HttpResponse[ListAllWorkflowApprovalsResponse]
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
                    ListAllWorkflowApprovalsResponse,
                    parse_obj_as(
                        type_=ListAllWorkflowApprovalsResponse,
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

    def approval_requests(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        actor_details: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApprovalRequestsResponse]:
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
        HttpResponse[ApprovalRequestsResponse]
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
                    ApprovalRequestsResponse,
                    parse_obj_as(
                        type_=ApprovalRequestsResponse,
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

    def update_workflow_approval(
        self,
        id: str,
        role_id: str,
        *,
        user: UpdateWorkflowApprovalRequestUser,
        status: UpdateWorkflowApprovalRequestStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
        """
        Updates an approval to the specified status. Approvals can only be updated during the Review step.

        Parameters
        ----------
        id : str
            The unique identifier or Ironclad ID of a workflow.

        role_id : str
            The unique identifier of the approver role whose status should be changed. This identifier can be retrieved using the `GET /workflows/{id}/approvals` endpoint.

        user : UpdateWorkflowApprovalRequestUser
            The Ironclad user approving the workflow. The user must be currently assigned as the approver.

        status : UpdateWorkflowApprovalRequestStatus
            The new approval status.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[bool]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/approvals/{encode_path_param(role_id)}",
            method="PATCH",
            json={
                "user": convert_and_respect_annotation_metadata(
                    object_=user, annotation=UpdateWorkflowApprovalRequestUser, direction="write"
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
                    bool,
                    parse_obj_as(
                        type_=bool,
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

    def turn_history(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TurnHistoryResponse]:
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
        HttpResponse[TurnHistoryResponse]
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
                    TurnHistoryResponse,
                    parse_obj_as(
                        type_=TurnHistoryResponse,
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

    def list_all_workflow_signers(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListAllWorkflowSignersResponse]:
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
        HttpResponse[ListAllWorkflowSignersResponse]
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
                    ListAllWorkflowSignersResponse,
                    parse_obj_as(
                        type_=ListAllWorkflowSignersResponse,
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

    def list_all_workflow_participants(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        email: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListAllWorkflowParticipantsResponse]:
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
        HttpResponse[ListAllWorkflowParticipantsResponse]
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
                    ListAllWorkflowParticipantsResponse,
                    parse_obj_as(
                        type_=ListAllWorkflowParticipantsResponse,
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

    def revert_to_review(
        self,
        id: str,
        *,
        user: RevertToReviewRequestUser,
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

        user : RevertToReviewRequestUser
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
                    object_=user, annotation=RevertToReviewRequestUser, direction="write"
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

    def deprecated_create_a_comment_on_a_workflow(
        self,
        id: str,
        *,
        creator: CreatorEmailModel,
        comment: str,
        add_users_to_workflow: typing.Optional[bool] = OMIT,
        replied_to_activity_feed_message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeprecatedCreateACommentOnAWorkflowResponse]:
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
        HttpResponse[DeprecatedCreateACommentOnAWorkflowResponse]
            204
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/comment",
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
                    DeprecatedCreateACommentOnAWorkflowResponse,
                    parse_obj_as(
                        type_=DeprecatedCreateACommentOnAWorkflowResponse,
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

    def create_a_comment_on_a_workflow(
        self,
        id: str,
        *,
        creator: CreatorEmailModel,
        comment: str,
        add_users_to_workflow: typing.Optional[bool] = OMIT,
        replied_to_activity_feed_message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CommentActivityModel]:
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
        HttpResponse[CommentActivityModel]
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
                    CommentActivityModel,
                    parse_obj_as(
                        type_=CommentActivityModel,
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

    def update_workflow_metadata(
        self,
        id: str,
        *,
        updates: typing.Sequence[UpdateWorkflowMetadataRequestUpdatesItem],
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateWorkflowMetadataResponse]:
        """
        The workflow must be in the Review step in order for its data to be updated. Use the `remove` action to clear field values and the `set` action to add or modify values. Form validation is enforced; required fields cannot be removed and any required fields triggered by conditions must be populated.

        Parameters
        ----------
        id : str
            The unique identifier or Ironclad ID of a workflow.

        updates : typing.Sequence[UpdateWorkflowMetadataRequestUpdatesItem]

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
        HttpResponse[UpdateWorkflowMetadataResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/attributes",
            method="PATCH",
            json={
                "updates": convert_and_respect_annotation_metadata(
                    object_=updates,
                    annotation=typing.Sequence[UpdateWorkflowMetadataRequestUpdatesItem],
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
                    UpdateWorkflowMetadataResponse,
                    parse_obj_as(
                        type_=UpdateWorkflowMetadataResponse,
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

    def retrieve_a_workflow_document(
        self, id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveAWorkflowDocumentResponse]:
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
        HttpResponse[RetrieveAWorkflowDocumentResponse]
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
                    RetrieveAWorkflowDocumentResponse,
                    parse_obj_as(
                        type_=RetrieveAWorkflowDocumentResponse,
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

    def retrieve_email_threads_from_workflow(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RetrieveEmailThreadsFromWorkflowResponse]:
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
        HttpResponse[RetrieveEmailThreadsFromWorkflowResponse]
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
                    RetrieveEmailThreadsFromWorkflowResponse,
                    parse_obj_as(
                        type_=RetrieveEmailThreadsFromWorkflowResponse,
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

    def retrieve_email_thread_from_workflow(
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

    def retrieve_attachment_from_email_thread(
        self,
        id: str,
        email_thread_id: str,
        attachment_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RetrieveAttachmentFromEmailThreadResponse]:
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
        HttpResponse[RetrieveAttachmentFromEmailThreadResponse]
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
                    RetrieveAttachmentFromEmailThreadResponse,
                    parse_obj_as(
                        type_=RetrieveAttachmentFromEmailThreadResponse,
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

    def list_all_workflow_schemas(
        self,
        *,
        form: str,
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListAllWorkflowSchemasResponse]:
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
        HttpResponse[ListAllWorkflowSchemasResponse]
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
                    ListAllWorkflowSchemasResponse,
                    parse_obj_as(
                        type_=ListAllWorkflowSchemasResponse,
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

    def retrieve_a_workflow_schema(
        self,
        id: str,
        *,
        form: typing.Optional[str] = None,
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RetrieveAWorkflowSchemaResponse]:
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
        HttpResponse[RetrieveAWorkflowSchemaResponse]
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
                    RetrieveAWorkflowSchemaResponse,
                    parse_obj_as(
                        type_=RetrieveAWorkflowSchemaResponse,
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

    async def list_all_workflows(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        status: typing.Optional[ListAllWorkflowsRequestStatus] = None,
        template: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListAllWorkflowsResponse]:
        """
        List all workflows in your Ironclad account.

        Parameters
        ----------
        page : typing.Optional[int]
            The page number used when paginating through a list of results.

        page_size : typing.Optional[int]
            A limit of the number of results to return.

        status : typing.Optional[ListAllWorkflowsRequestStatus]
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
        AsyncHttpResponse[ListAllWorkflowsResponse]
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
                    ListAllWorkflowsResponse,
                    parse_obj_as(
                        type_=ListAllWorkflowsResponse,
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

    async def launch_a_new_workflow(
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

    async def create_a_new_workflow_async(
        self,
        *,
        template: WorkflowTemplateIdModel,
        creator: CreatorEmailModel,
        attributes: AttributesModel,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateANewWorkflowAsyncResponse]:
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
        AsyncHttpResponse[CreateANewWorkflowAsyncResponse]
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
                    CreateANewWorkflowAsyncResponse,
                    parse_obj_as(
                        type_=CreateANewWorkflowAsyncResponse,
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

    async def retrieve_asynchronous_workflow_status(
        self, async_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveAsynchronousWorkflowStatusResponse]:
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
        AsyncHttpResponse[RetrieveAsynchronousWorkflowStatusResponse]
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
                    RetrieveAsynchronousWorkflowStatusResponse,
                    parse_obj_as(
                        type_=RetrieveAsynchronousWorkflowStatusResponse,
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

    async def retrieve_a_workflow(
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

    async def list_all_workflow_approvals(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListAllWorkflowApprovalsResponse]:
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
        AsyncHttpResponse[ListAllWorkflowApprovalsResponse]
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
                    ListAllWorkflowApprovalsResponse,
                    parse_obj_as(
                        type_=ListAllWorkflowApprovalsResponse,
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

    async def approval_requests(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        actor_details: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApprovalRequestsResponse]:
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
        AsyncHttpResponse[ApprovalRequestsResponse]
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
                    ApprovalRequestsResponse,
                    parse_obj_as(
                        type_=ApprovalRequestsResponse,
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

    async def update_workflow_approval(
        self,
        id: str,
        role_id: str,
        *,
        user: UpdateWorkflowApprovalRequestUser,
        status: UpdateWorkflowApprovalRequestStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
        """
        Updates an approval to the specified status. Approvals can only be updated during the Review step.

        Parameters
        ----------
        id : str
            The unique identifier or Ironclad ID of a workflow.

        role_id : str
            The unique identifier of the approver role whose status should be changed. This identifier can be retrieved using the `GET /workflows/{id}/approvals` endpoint.

        user : UpdateWorkflowApprovalRequestUser
            The Ironclad user approving the workflow. The user must be currently assigned as the approver.

        status : UpdateWorkflowApprovalRequestStatus
            The new approval status.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[bool]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/approvals/{encode_path_param(role_id)}",
            method="PATCH",
            json={
                "user": convert_and_respect_annotation_metadata(
                    object_=user, annotation=UpdateWorkflowApprovalRequestUser, direction="write"
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
                    bool,
                    parse_obj_as(
                        type_=bool,
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

    async def turn_history(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TurnHistoryResponse]:
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
        AsyncHttpResponse[TurnHistoryResponse]
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
                    TurnHistoryResponse,
                    parse_obj_as(
                        type_=TurnHistoryResponse,
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

    async def list_all_workflow_signers(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListAllWorkflowSignersResponse]:
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
        AsyncHttpResponse[ListAllWorkflowSignersResponse]
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
                    ListAllWorkflowSignersResponse,
                    parse_obj_as(
                        type_=ListAllWorkflowSignersResponse,
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

    async def list_all_workflow_participants(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        email: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListAllWorkflowParticipantsResponse]:
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
        AsyncHttpResponse[ListAllWorkflowParticipantsResponse]
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
                    ListAllWorkflowParticipantsResponse,
                    parse_obj_as(
                        type_=ListAllWorkflowParticipantsResponse,
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

    async def revert_to_review(
        self,
        id: str,
        *,
        user: RevertToReviewRequestUser,
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

        user : RevertToReviewRequestUser
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
                    object_=user, annotation=RevertToReviewRequestUser, direction="write"
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

    async def deprecated_create_a_comment_on_a_workflow(
        self,
        id: str,
        *,
        creator: CreatorEmailModel,
        comment: str,
        add_users_to_workflow: typing.Optional[bool] = OMIT,
        replied_to_activity_feed_message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeprecatedCreateACommentOnAWorkflowResponse]:
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
        AsyncHttpResponse[DeprecatedCreateACommentOnAWorkflowResponse]
            204
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/comment",
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
                    DeprecatedCreateACommentOnAWorkflowResponse,
                    parse_obj_as(
                        type_=DeprecatedCreateACommentOnAWorkflowResponse,
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

    async def create_a_comment_on_a_workflow(
        self,
        id: str,
        *,
        creator: CreatorEmailModel,
        comment: str,
        add_users_to_workflow: typing.Optional[bool] = OMIT,
        replied_to_activity_feed_message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CommentActivityModel]:
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
        AsyncHttpResponse[CommentActivityModel]
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
                    CommentActivityModel,
                    parse_obj_as(
                        type_=CommentActivityModel,
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

    async def update_workflow_metadata(
        self,
        id: str,
        *,
        updates: typing.Sequence[UpdateWorkflowMetadataRequestUpdatesItem],
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateWorkflowMetadataResponse]:
        """
        The workflow must be in the Review step in order for its data to be updated. Use the `remove` action to clear field values and the `set` action to add or modify values. Form validation is enforced; required fields cannot be removed and any required fields triggered by conditions must be populated.

        Parameters
        ----------
        id : str
            The unique identifier or Ironclad ID of a workflow.

        updates : typing.Sequence[UpdateWorkflowMetadataRequestUpdatesItem]

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
        AsyncHttpResponse[UpdateWorkflowMetadataResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(id)}/attributes",
            method="PATCH",
            json={
                "updates": convert_and_respect_annotation_metadata(
                    object_=updates,
                    annotation=typing.Sequence[UpdateWorkflowMetadataRequestUpdatesItem],
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
                    UpdateWorkflowMetadataResponse,
                    parse_obj_as(
                        type_=UpdateWorkflowMetadataResponse,
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

    async def retrieve_a_workflow_document(
        self, id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveAWorkflowDocumentResponse]:
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
        AsyncHttpResponse[RetrieveAWorkflowDocumentResponse]
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
                    RetrieveAWorkflowDocumentResponse,
                    parse_obj_as(
                        type_=RetrieveAWorkflowDocumentResponse,
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

    async def retrieve_email_threads_from_workflow(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RetrieveEmailThreadsFromWorkflowResponse]:
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
        AsyncHttpResponse[RetrieveEmailThreadsFromWorkflowResponse]
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
                    RetrieveEmailThreadsFromWorkflowResponse,
                    parse_obj_as(
                        type_=RetrieveEmailThreadsFromWorkflowResponse,
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

    async def retrieve_email_thread_from_workflow(
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

    async def retrieve_attachment_from_email_thread(
        self,
        id: str,
        email_thread_id: str,
        attachment_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RetrieveAttachmentFromEmailThreadResponse]:
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
        AsyncHttpResponse[RetrieveAttachmentFromEmailThreadResponse]
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
                    RetrieveAttachmentFromEmailThreadResponse,
                    parse_obj_as(
                        type_=RetrieveAttachmentFromEmailThreadResponse,
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

    async def list_all_workflow_schemas(
        self,
        *,
        form: str,
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListAllWorkflowSchemasResponse]:
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
        AsyncHttpResponse[ListAllWorkflowSchemasResponse]
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
                    ListAllWorkflowSchemasResponse,
                    parse_obj_as(
                        type_=ListAllWorkflowSchemasResponse,
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

    async def retrieve_a_workflow_schema(
        self,
        id: str,
        *,
        form: typing.Optional[str] = None,
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RetrieveAWorkflowSchemaResponse]:
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
        AsyncHttpResponse[RetrieveAWorkflowSchemaResponse]
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
                    RetrieveAWorkflowSchemaResponse,
                    parse_obj_as(
                        type_=RetrieveAWorkflowSchemaResponse,
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
