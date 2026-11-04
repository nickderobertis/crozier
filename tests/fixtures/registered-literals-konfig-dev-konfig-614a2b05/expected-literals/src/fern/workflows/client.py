

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.attributes_model import AttributesModel
from ..types.comment_activity_model import CommentActivityModel
from ..types.creator_email_model import CreatorEmailModel
from ..types.email_response_model import EmailResponseModel
from ..types.launched_workflow_model import LaunchedWorkflowModel
from ..types.workflow_response_model import WorkflowResponseModel
from ..types.workflow_template_id_model import WorkflowTemplateIdModel
from .raw_client import AsyncRawWorkflowsClient, RawWorkflowsClient
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


OMIT = typing.cast(typing.Any, ...)


class WorkflowsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWorkflowsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWorkflowsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWorkflowsClient
        """
        return self._raw_client

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
    ) -> ListAllWorkflowsResponse:
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
        ListAllWorkflowsResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.list_all_workflows(
            filter="Equals([counterpartyName], 'Harley Quinn')",
        )
        """
        _response = self._raw_client.list_all_workflows(
            page=page,
            page_size=page_size,
            status=status,
            template=template,
            last_updated=last_updated,
            filter=filter,
            request_options=request_options,
        )
        return _response.data

    def launch_a_new_workflow(
        self,
        *,
        template: WorkflowTemplateIdModel,
        creator: CreatorEmailModel,
        attributes: AttributesModel,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LaunchedWorkflowModel:
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
        LaunchedWorkflowModel
            Launched Workflow Response.

        Examples
        --------
        from fern import AttributesModel, CreatorEmailModel, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.launch_a_new_workflow(
            template="600b296c3e15a234ab88f884",
            creator=CreatorEmailModel(),
            attributes=AttributesModel(
                counterparty_name="Example Company",
            ),
        )
        """
        _response = self._raw_client.launch_a_new_workflow(
            template=template, creator=creator, attributes=attributes, request_options=request_options
        )
        return _response.data

    def create_a_new_workflow_async(
        self,
        *,
        template: WorkflowTemplateIdModel,
        creator: CreatorEmailModel,
        attributes: AttributesModel,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateANewWorkflowAsyncResponse:
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
        CreateANewWorkflowAsyncResponse
            The response of the initiated async workflow launch.

        Examples
        --------
        from fern import AttributesModel, CreatorEmailModel, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.create_a_new_workflow_async(
            template="600b296c3e15a234ab88f884",
            creator=CreatorEmailModel(),
            attributes=AttributesModel(
                counterparty_name="Example Company",
            ),
        )
        """
        _response = self._raw_client.create_a_new_workflow_async(
            template=template, creator=creator, attributes=attributes, request_options=request_options
        )
        return _response.data

    def retrieve_asynchronous_workflow_status(
        self, async_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveAsynchronousWorkflowStatusResponse:
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
        RetrieveAsynchronousWorkflowStatusResponse
            The status of the workflow launch.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.retrieve_asynchronous_workflow_status(
            async_job_id="asyncJobId",
        )
        """
        _response = self._raw_client.retrieve_asynchronous_workflow_status(
            async_job_id, request_options=request_options
        )
        return _response.data

    def retrieve_a_workflow(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkflowResponseModel:
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
        WorkflowResponseModel
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.retrieve_a_workflow(
            id="abcd1234",
        )
        """
        _response = self._raw_client.retrieve_a_workflow(id, request_options=request_options)
        return _response.data

    def list_all_workflow_approvals(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListAllWorkflowApprovalsResponse:
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
        ListAllWorkflowApprovalsResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.list_all_workflow_approvals(
            id="abcd1234",
        )
        """
        _response = self._raw_client.list_all_workflow_approvals(id, request_options=request_options)
        return _response.data

    def approval_requests(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        actor_details: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApprovalRequestsResponse:
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
        ApprovalRequestsResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.approval_requests(
            id="id",
            actor_details=False,
        )
        """
        _response = self._raw_client.approval_requests(
            id, page=page, page_size=page_size, actor_details=actor_details, request_options=request_options
        )
        return _response.data

    def update_workflow_approval(
        self,
        id: str,
        role_id: str,
        *,
        user: UpdateWorkflowApprovalRequestUser,
        status: UpdateWorkflowApprovalRequestStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
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
        bool
            200

        Examples
        --------
        from fern.workflows import UpdateWorkflowApprovalRequestUser

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.update_workflow_approval(
            id="abcd1234",
            role_id="roleId",
            user=UpdateWorkflowApprovalRequestUser(),
            status="approved",
        )
        """
        _response = self._raw_client.update_workflow_approval(
            id, role_id, user=user, status=status, request_options=request_options
        )
        return _response.data

    def turn_history(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TurnHistoryResponse:
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
        TurnHistoryResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.turn_history(
            id="id",
        )
        """
        _response = self._raw_client.turn_history(id, page=page, page_size=page_size, request_options=request_options)
        return _response.data

    def list_all_workflow_signers(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListAllWorkflowSignersResponse:
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
        ListAllWorkflowSignersResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.list_all_workflow_signers(
            id="id",
        )
        """
        _response = self._raw_client.list_all_workflow_signers(id, request_options=request_options)
        return _response.data

    def list_all_workflow_participants(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        email: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAllWorkflowParticipantsResponse:
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
        ListAllWorkflowParticipantsResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.list_all_workflow_participants(
            id="id",
        )
        """
        _response = self._raw_client.list_all_workflow_participants(
            id, page=page, page_size=page_size, email=email, request_options=request_options
        )
        return _response.data

    def revert_to_review(
        self,
        id: str,
        *,
        user: RevertToReviewRequestUser,
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        from fern.workflows import RevertToReviewRequestUser

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.revert_to_review(
            id="id",
            as_user_email="jane.doe@test.com",
            as_user_id="5f0375c4cdc1927a3c5edcd3",
            user=RevertToReviewRequestUser(),
        )
        """
        _response = self._raw_client.revert_to_review(
            id, user=user, as_user_email=as_user_email, as_user_id=as_user_id, request_options=request_options
        )
        return _response.data

    def deprecated_create_a_comment_on_a_workflow(
        self,
        id: str,
        *,
        creator: CreatorEmailModel,
        comment: str,
        add_users_to_workflow: typing.Optional[bool] = OMIT,
        replied_to_activity_feed_message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeprecatedCreateACommentOnAWorkflowResponse:
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
        DeprecatedCreateACommentOnAWorkflowResponse
            204

        Examples
        --------
        from fern import CreatorEmailModel, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.deprecated_create_a_comment_on_a_workflow(
            id="id",
            creator=CreatorEmailModel(),
            comment="comment",
        )
        """
        _response = self._raw_client.deprecated_create_a_comment_on_a_workflow(
            id,
            creator=creator,
            comment=comment,
            add_users_to_workflow=add_users_to_workflow,
            replied_to_activity_feed_message_id=replied_to_activity_feed_message_id,
            request_options=request_options,
        )
        return _response.data

    def create_a_comment_on_a_workflow(
        self,
        id: str,
        *,
        creator: CreatorEmailModel,
        comment: str,
        add_users_to_workflow: typing.Optional[bool] = OMIT,
        replied_to_activity_feed_message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CommentActivityModel:
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
        CommentActivityModel
            200

        Examples
        --------
        from fern import CreatorEmailModel, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.create_a_comment_on_a_workflow(
            id="id",
            creator=CreatorEmailModel(),
            comment="comment",
        )
        """
        _response = self._raw_client.create_a_comment_on_a_workflow(
            id,
            creator=creator,
            comment=comment,
            add_users_to_workflow=add_users_to_workflow,
            replied_to_activity_feed_message_id=replied_to_activity_feed_message_id,
            request_options=request_options,
        )
        return _response.data

    def update_workflow_metadata(
        self,
        id: str,
        *,
        updates: typing.Sequence[UpdateWorkflowMetadataRequestUpdatesItem],
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateWorkflowMetadataResponse:
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
        UpdateWorkflowMetadataResponse
            200

        Examples
        --------
        from fern.workflows import UpdateWorkflowMetadataRequestUpdatesItem

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.update_workflow_metadata(
            id="id",
            as_user_email="jane.doe@test.com",
            as_user_id="5f0375c4cdc1927a3c5edcd3",
            updates=[
                UpdateWorkflowMetadataRequestUpdatesItem(
                    action="set",
                    path="counterpartyName",
                )
            ],
        )
        """
        _response = self._raw_client.update_workflow_metadata(
            id,
            updates=updates,
            as_user_email=as_user_email,
            as_user_id=as_user_id,
            comment=comment,
            request_options=request_options,
        )
        return _response.data

    def retrieve_a_workflow_document(
        self, id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveAWorkflowDocumentResponse:
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
        RetrieveAWorkflowDocumentResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.retrieve_a_workflow_document(
            id="id",
            key="key",
        )
        """
        _response = self._raw_client.retrieve_a_workflow_document(id, key, request_options=request_options)
        return _response.data

    def retrieve_email_threads_from_workflow(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetrieveEmailThreadsFromWorkflowResponse:
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
        RetrieveEmailThreadsFromWorkflowResponse
            GET Emails Response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.retrieve_email_threads_from_workflow(
            id="id",
        )
        """
        _response = self._raw_client.retrieve_email_threads_from_workflow(
            id, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    def retrieve_email_thread_from_workflow(
        self, id: str, email_thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EmailResponseModel:
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
        EmailResponseModel
            GET Email Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.retrieve_email_thread_from_workflow(
            id="id",
            email_thread_id="emailThreadId",
        )
        """
        _response = self._raw_client.retrieve_email_thread_from_workflow(
            id, email_thread_id, request_options=request_options
        )
        return _response.data

    def retrieve_attachment_from_email_thread(
        self,
        id: str,
        email_thread_id: str,
        attachment_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetrieveAttachmentFromEmailThreadResponse:
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
        RetrieveAttachmentFromEmailThreadResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.retrieve_attachment_from_email_thread(
            id="id",
            email_thread_id="emailThreadId",
            attachment_id="attachmentId",
        )
        """
        _response = self._raw_client.retrieve_attachment_from_email_thread(
            id, email_thread_id, attachment_id, request_options=request_options
        )
        return _response.data

    def list_all_workflow_schemas(
        self,
        *,
        form: str,
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAllWorkflowSchemasResponse:
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
        ListAllWorkflowSchemasResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.list_all_workflow_schemas(
            as_user_email="jane.doe@test.com",
            as_user_id="5f0375c4cdc1927a3c5edcd3",
            form="form",
        )
        """
        _response = self._raw_client.list_all_workflow_schemas(
            form=form, as_user_email=as_user_email, as_user_id=as_user_id, request_options=request_options
        )
        return _response.data

    def retrieve_a_workflow_schema(
        self,
        id: str,
        *,
        form: typing.Optional[str] = None,
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetrieveAWorkflowSchemaResponse:
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
        RetrieveAWorkflowSchemaResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.retrieve_a_workflow_schema(
            id="id",
            as_user_email="jane.doe@test.com",
            as_user_id="5f0375c4cdc1927a3c5edcd3",
        )
        """
        _response = self._raw_client.retrieve_a_workflow_schema(
            id, form=form, as_user_email=as_user_email, as_user_id=as_user_id, request_options=request_options
        )
        return _response.data


class AsyncWorkflowsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWorkflowsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWorkflowsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWorkflowsClient
        """
        return self._raw_client

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
    ) -> ListAllWorkflowsResponse:
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
        ListAllWorkflowsResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.list_all_workflows(
                filter="Equals([counterpartyName], 'Harley Quinn')",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_workflows(
            page=page,
            page_size=page_size,
            status=status,
            template=template,
            last_updated=last_updated,
            filter=filter,
            request_options=request_options,
        )
        return _response.data

    async def launch_a_new_workflow(
        self,
        *,
        template: WorkflowTemplateIdModel,
        creator: CreatorEmailModel,
        attributes: AttributesModel,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LaunchedWorkflowModel:
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
        LaunchedWorkflowModel
            Launched Workflow Response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, AttributesModel, CreatorEmailModel

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.launch_a_new_workflow(
                template="600b296c3e15a234ab88f884",
                creator=CreatorEmailModel(),
                attributes=AttributesModel(
                    counterparty_name="Example Company",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.launch_a_new_workflow(
            template=template, creator=creator, attributes=attributes, request_options=request_options
        )
        return _response.data

    async def create_a_new_workflow_async(
        self,
        *,
        template: WorkflowTemplateIdModel,
        creator: CreatorEmailModel,
        attributes: AttributesModel,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateANewWorkflowAsyncResponse:
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
        CreateANewWorkflowAsyncResponse
            The response of the initiated async workflow launch.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, AttributesModel, CreatorEmailModel

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.create_a_new_workflow_async(
                template="600b296c3e15a234ab88f884",
                creator=CreatorEmailModel(),
                attributes=AttributesModel(
                    counterparty_name="Example Company",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_new_workflow_async(
            template=template, creator=creator, attributes=attributes, request_options=request_options
        )
        return _response.data

    async def retrieve_asynchronous_workflow_status(
        self, async_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveAsynchronousWorkflowStatusResponse:
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
        RetrieveAsynchronousWorkflowStatusResponse
            The status of the workflow launch.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.retrieve_asynchronous_workflow_status(
                async_job_id="asyncJobId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_asynchronous_workflow_status(
            async_job_id, request_options=request_options
        )
        return _response.data

    async def retrieve_a_workflow(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkflowResponseModel:
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
        WorkflowResponseModel
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.retrieve_a_workflow(
                id="abcd1234",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_workflow(id, request_options=request_options)
        return _response.data

    async def list_all_workflow_approvals(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListAllWorkflowApprovalsResponse:
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
        ListAllWorkflowApprovalsResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.list_all_workflow_approvals(
                id="abcd1234",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_workflow_approvals(id, request_options=request_options)
        return _response.data

    async def approval_requests(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        actor_details: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApprovalRequestsResponse:
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
        ApprovalRequestsResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.approval_requests(
                id="id",
                actor_details=False,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.approval_requests(
            id, page=page, page_size=page_size, actor_details=actor_details, request_options=request_options
        )
        return _response.data

    async def update_workflow_approval(
        self,
        id: str,
        role_id: str,
        *,
        user: UpdateWorkflowApprovalRequestUser,
        status: UpdateWorkflowApprovalRequestStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
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
        bool
            200

        Examples
        --------
        import asyncio

        from fern.workflows import UpdateWorkflowApprovalRequestUser

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.update_workflow_approval(
                id="abcd1234",
                role_id="roleId",
                user=UpdateWorkflowApprovalRequestUser(),
                status="approved",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_workflow_approval(
            id, role_id, user=user, status=status, request_options=request_options
        )
        return _response.data

    async def turn_history(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TurnHistoryResponse:
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
        TurnHistoryResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.turn_history(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.turn_history(
            id, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def list_all_workflow_signers(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListAllWorkflowSignersResponse:
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
        ListAllWorkflowSignersResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.list_all_workflow_signers(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_workflow_signers(id, request_options=request_options)
        return _response.data

    async def list_all_workflow_participants(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        email: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAllWorkflowParticipantsResponse:
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
        ListAllWorkflowParticipantsResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.list_all_workflow_participants(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_workflow_participants(
            id, page=page, page_size=page_size, email=email, request_options=request_options
        )
        return _response.data

    async def revert_to_review(
        self,
        id: str,
        *,
        user: RevertToReviewRequestUser,
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern.workflows import RevertToReviewRequestUser

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.revert_to_review(
                id="id",
                as_user_email="jane.doe@test.com",
                as_user_id="5f0375c4cdc1927a3c5edcd3",
                user=RevertToReviewRequestUser(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revert_to_review(
            id, user=user, as_user_email=as_user_email, as_user_id=as_user_id, request_options=request_options
        )
        return _response.data

    async def deprecated_create_a_comment_on_a_workflow(
        self,
        id: str,
        *,
        creator: CreatorEmailModel,
        comment: str,
        add_users_to_workflow: typing.Optional[bool] = OMIT,
        replied_to_activity_feed_message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeprecatedCreateACommentOnAWorkflowResponse:
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
        DeprecatedCreateACommentOnAWorkflowResponse
            204

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CreatorEmailModel

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.deprecated_create_a_comment_on_a_workflow(
                id="id",
                creator=CreatorEmailModel(),
                comment="comment",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deprecated_create_a_comment_on_a_workflow(
            id,
            creator=creator,
            comment=comment,
            add_users_to_workflow=add_users_to_workflow,
            replied_to_activity_feed_message_id=replied_to_activity_feed_message_id,
            request_options=request_options,
        )
        return _response.data

    async def create_a_comment_on_a_workflow(
        self,
        id: str,
        *,
        creator: CreatorEmailModel,
        comment: str,
        add_users_to_workflow: typing.Optional[bool] = OMIT,
        replied_to_activity_feed_message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CommentActivityModel:
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
        CommentActivityModel
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CreatorEmailModel

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.create_a_comment_on_a_workflow(
                id="id",
                creator=CreatorEmailModel(),
                comment="comment",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_comment_on_a_workflow(
            id,
            creator=creator,
            comment=comment,
            add_users_to_workflow=add_users_to_workflow,
            replied_to_activity_feed_message_id=replied_to_activity_feed_message_id,
            request_options=request_options,
        )
        return _response.data

    async def update_workflow_metadata(
        self,
        id: str,
        *,
        updates: typing.Sequence[UpdateWorkflowMetadataRequestUpdatesItem],
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateWorkflowMetadataResponse:
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
        UpdateWorkflowMetadataResponse
            200

        Examples
        --------
        import asyncio

        from fern.workflows import UpdateWorkflowMetadataRequestUpdatesItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.update_workflow_metadata(
                id="id",
                as_user_email="jane.doe@test.com",
                as_user_id="5f0375c4cdc1927a3c5edcd3",
                updates=[
                    UpdateWorkflowMetadataRequestUpdatesItem(
                        action="set",
                        path="counterpartyName",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_workflow_metadata(
            id,
            updates=updates,
            as_user_email=as_user_email,
            as_user_id=as_user_id,
            comment=comment,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_a_workflow_document(
        self, id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveAWorkflowDocumentResponse:
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
        RetrieveAWorkflowDocumentResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.retrieve_a_workflow_document(
                id="id",
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_workflow_document(id, key, request_options=request_options)
        return _response.data

    async def retrieve_email_threads_from_workflow(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetrieveEmailThreadsFromWorkflowResponse:
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
        RetrieveEmailThreadsFromWorkflowResponse
            GET Emails Response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.retrieve_email_threads_from_workflow(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_email_threads_from_workflow(
            id, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def retrieve_email_thread_from_workflow(
        self, id: str, email_thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EmailResponseModel:
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
        EmailResponseModel
            GET Email Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.retrieve_email_thread_from_workflow(
                id="id",
                email_thread_id="emailThreadId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_email_thread_from_workflow(
            id, email_thread_id, request_options=request_options
        )
        return _response.data

    async def retrieve_attachment_from_email_thread(
        self,
        id: str,
        email_thread_id: str,
        attachment_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetrieveAttachmentFromEmailThreadResponse:
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
        RetrieveAttachmentFromEmailThreadResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.retrieve_attachment_from_email_thread(
                id="id",
                email_thread_id="emailThreadId",
                attachment_id="attachmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_attachment_from_email_thread(
            id, email_thread_id, attachment_id, request_options=request_options
        )
        return _response.data

    async def list_all_workflow_schemas(
        self,
        *,
        form: str,
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAllWorkflowSchemasResponse:
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
        ListAllWorkflowSchemasResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.list_all_workflow_schemas(
                as_user_email="jane.doe@test.com",
                as_user_id="5f0375c4cdc1927a3c5edcd3",
                form="form",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_workflow_schemas(
            form=form, as_user_email=as_user_email, as_user_id=as_user_id, request_options=request_options
        )
        return _response.data

    async def retrieve_a_workflow_schema(
        self,
        id: str,
        *,
        form: typing.Optional[str] = None,
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetrieveAWorkflowSchemaResponse:
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
        RetrieveAWorkflowSchemaResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.retrieve_a_workflow_schema(
                id="id",
                as_user_email="jane.doe@test.com",
                as_user_id="5f0375c4cdc1927a3c5edcd3",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_workflow_schema(
            id, form=form, as_user_email=as_user_email, as_user_id=as_user_id, request_options=request_options
        )
        return _response.data
