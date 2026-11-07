

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
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
from .raw_client import AsyncRawWorkflowsClient, RawWorkflowsClient
from .types.workflows_list_all_request_status import WorkflowsListAllRequestStatus
from .types.workflows_revert_to_review_request_user import WorkflowsRevertToReviewRequestUser
from .types.workflows_update_approval_status_request_status import WorkflowsUpdateApprovalStatusRequestStatus
from .types.workflows_update_approval_status_request_user import WorkflowsUpdateApprovalStatusRequestUser
from .types.workflows_update_metadata_request_updates_item import WorkflowsUpdateMetadataRequestUpdatesItem


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
    ) -> WorkflowsListAllResponse:
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
        WorkflowsListAllResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.listall(
            filter="Equals([counterpartyName], 'Harley Quinn')",
        )
        """
        _response = self._raw_client.listall(
            page=page,
            page_size=page_size,
            status=status,
            template=template,
            last_updated=last_updated,
            filter=filter,
            request_options=request_options,
        )
        return _response.data

    def createsyncworkflow(
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
        client.workflows.createsyncworkflow(
            template="600b296c3e15a234ab88f884",
            creator=CreatorEmailModel(),
            attributes=AttributesModel(
                counterparty_name="Example Company",
            ),
        )
        """
        _response = self._raw_client.createsyncworkflow(
            template=template, creator=creator, attributes=attributes, request_options=request_options
        )
        return _response.data

    def launchasynchronously(
        self,
        *,
        template: WorkflowTemplateIdModel,
        creator: CreatorEmailModel,
        attributes: AttributesModel,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowsLaunchAsynchronouslyResponse:
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
        WorkflowsLaunchAsynchronouslyResponse
            The response of the initiated async workflow launch.

        Examples
        --------
        from fern import AttributesModel, CreatorEmailModel, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.launchasynchronously(
            template="600b296c3e15a234ab88f884",
            creator=CreatorEmailModel(),
            attributes=AttributesModel(
                counterparty_name="Example Company",
            ),
        )
        """
        _response = self._raw_client.launchasynchronously(
            template=template, creator=creator, attributes=attributes, request_options=request_options
        )
        return _response.data

    def getasyncjobstatus(
        self, async_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkflowsGetAsyncJobStatusResponse:
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
        WorkflowsGetAsyncJobStatusResponse
            The status of the workflow launch.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.getasyncjobstatus(
            async_job_id="asyncJobId",
        )
        """
        _response = self._raw_client.getasyncjobstatus(async_job_id, request_options=request_options)
        return _response.data

    def getworkflow(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> WorkflowResponseModel:
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
        client.workflows.getworkflow(
            id="abcd1234",
        )
        """
        _response = self._raw_client.getworkflow(id, request_options=request_options)
        return _response.data

    def listapprovals(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkflowsListApprovalsResponse:
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
        WorkflowsListApprovalsResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.listapprovals(
            id="abcd1234",
        )
        """
        _response = self._raw_client.listapprovals(id, request_options=request_options)
        return _response.data

    def getapprovalrequests(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        actor_details: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowsGetApprovalRequestsResponse:
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
        WorkflowsGetApprovalRequestsResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.getapprovalrequests(
            id="id",
            actor_details=False,
        )
        """
        _response = self._raw_client.getapprovalrequests(
            id, page=page, page_size=page_size, actor_details=actor_details, request_options=request_options
        )
        return _response.data

    def updateapprovalstatus(
        self,
        id: str,
        role_id: str,
        *,
        user: WorkflowsUpdateApprovalStatusRequestUser,
        status: WorkflowsUpdateApprovalStatusRequestStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowsUpdateApprovalStatusResponse:
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
        WorkflowsUpdateApprovalStatusResponse
            200

        Examples
        --------
        from fern.workflows import (
            WorkflowsUpdateApprovalStatusRequestStatus,
            WorkflowsUpdateApprovalStatusRequestUser,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.updateapprovalstatus(
            id="abcd1234",
            role_id="roleId",
            user=WorkflowsUpdateApprovalStatusRequestUser(),
            status=WorkflowsUpdateApprovalStatusRequestStatus.APPROVED,
        )
        """
        _response = self._raw_client.updateapprovalstatus(
            id, role_id, user=user, status=status, request_options=request_options
        )
        return _response.data

    def getturnhistory(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowsGetTurnHistoryResponse:
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
        WorkflowsGetTurnHistoryResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.getturnhistory(
            id="id",
        )
        """
        _response = self._raw_client.getturnhistory(id, page=page, page_size=page_size, request_options=request_options)
        return _response.data

    def listsignatures(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkflowsListSignaturesResponse:
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
        WorkflowsListSignaturesResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.listsignatures(
            id="id",
        )
        """
        _response = self._raw_client.listsignatures(id, request_options=request_options)
        return _response.data

    def listallparticipants(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        email: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowsListAllParticipantsResponse:
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
        WorkflowsListAllParticipantsResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.listallparticipants(
            id="id",
        )
        """
        _response = self._raw_client.listallparticipants(
            id, page=page, page_size=page_size, email=email, request_options=request_options
        )
        return _response.data

    def reverttoreview(
        self,
        id: str,
        *,
        user: WorkflowsRevertToReviewRequestUser,
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
        None

        Examples
        --------
        from fern.workflows import WorkflowsRevertToReviewRequestUser

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.reverttoreview(
            id="id",
            as_user_email="jane.doe@test.com",
            as_user_id="5f0375c4cdc1927a3c5edcd3",
            user=WorkflowsRevertToReviewRequestUser(),
        )
        """
        _response = self._raw_client.reverttoreview(
            id, user=user, as_user_email=as_user_email, as_user_id=as_user_id, request_options=request_options
        )
        return _response.data

    def createcomment(
        self,
        id: str,
        *,
        creator: CreatorEmailModel,
        comment: str,
        add_users_to_workflow: typing.Optional[bool] = OMIT,
        replied_to_activity_feed_message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseActivityFeedItemModel:
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
        BaseActivityFeedItemModel
            200

        Examples
        --------
        from fern import CreatorEmailModel, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.createcomment(
            id="id",
            creator=CreatorEmailModel(),
            comment="comment",
        )
        """
        _response = self._raw_client.createcomment(
            id,
            creator=creator,
            comment=comment,
            add_users_to_workflow=add_users_to_workflow,
            replied_to_activity_feed_message_id=replied_to_activity_feed_message_id,
            request_options=request_options,
        )
        return _response.data

    def updatemetadata(
        self,
        id: str,
        *,
        updates: typing.Sequence[WorkflowsUpdateMetadataRequestUpdatesItem],
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowsUpdateMetadataResponse:
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
        WorkflowsUpdateMetadataResponse
            200

        Examples
        --------
        from fern.workflows import (
            WorkflowsUpdateMetadataRequestUpdatesItem,
            WorkflowsUpdateMetadataRequestUpdatesItemAction,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.updatemetadata(
            id="id",
            as_user_email="jane.doe@test.com",
            as_user_id="5f0375c4cdc1927a3c5edcd3",
            updates=[
                WorkflowsUpdateMetadataRequestUpdatesItem(
                    action=WorkflowsUpdateMetadataRequestUpdatesItemAction.SET,
                    path="counterpartyName",
                )
            ],
        )
        """
        _response = self._raw_client.updatemetadata(
            id,
            updates=updates,
            as_user_email=as_user_email,
            as_user_id=as_user_id,
            comment=comment,
            request_options=request_options,
        )
        return _response.data

    def getdocumentbykey(
        self, id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkflowsGetDocumentByKeyResponse:
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
        WorkflowsGetDocumentByKeyResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.getdocumentbykey(
            id="id",
            key="key",
        )
        """
        _response = self._raw_client.getdocumentbykey(id, key, request_options=request_options)
        return _response.data

    def getemailthreads(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowsGetEmailThreadsResponse:
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
        WorkflowsGetEmailThreadsResponse
            GET Emails Response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.getemailthreads(
            id="id",
        )
        """
        _response = self._raw_client.getemailthreads(
            id, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    def getemailthread(
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
        client.workflows.getemailthread(
            id="id",
            email_thread_id="emailThreadId",
        )
        """
        _response = self._raw_client.getemailthread(id, email_thread_id, request_options=request_options)
        return _response.data

    def getattachmentfromemailthread(
        self,
        id: str,
        email_thread_id: str,
        attachment_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowsGetAttachmentFromEmailThreadResponse:
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
        WorkflowsGetAttachmentFromEmailThreadResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.getattachmentfromemailthread(
            id="id",
            email_thread_id="emailThreadId",
            attachment_id="attachmentId",
        )
        """
        _response = self._raw_client.getattachmentfromemailthread(
            id, email_thread_id, attachment_id, request_options=request_options
        )
        return _response.data

    def listallworkflowschemas(
        self,
        *,
        form: str,
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowsListAllWorkflowSchemasResponse:
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
        WorkflowsListAllWorkflowSchemasResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.listallworkflowschemas(
            as_user_email="jane.doe@test.com",
            as_user_id="5f0375c4cdc1927a3c5edcd3",
            form="form",
        )
        """
        _response = self._raw_client.listallworkflowschemas(
            form=form, as_user_email=as_user_email, as_user_id=as_user_id, request_options=request_options
        )
        return _response.data

    def getworkflowschema(
        self,
        id: str,
        *,
        form: typing.Optional[str] = None,
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowsGetWorkflowSchemaResponse:
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
        WorkflowsGetWorkflowSchemaResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflows.getworkflowschema(
            id="id",
            as_user_email="jane.doe@test.com",
            as_user_id="5f0375c4cdc1927a3c5edcd3",
        )
        """
        _response = self._raw_client.getworkflowschema(
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
    ) -> WorkflowsListAllResponse:
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
        WorkflowsListAllResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.listall(
                filter="Equals([counterpartyName], 'Harley Quinn')",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listall(
            page=page,
            page_size=page_size,
            status=status,
            template=template,
            last_updated=last_updated,
            filter=filter,
            request_options=request_options,
        )
        return _response.data

    async def createsyncworkflow(
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
            await client.workflows.createsyncworkflow(
                template="600b296c3e15a234ab88f884",
                creator=CreatorEmailModel(),
                attributes=AttributesModel(
                    counterparty_name="Example Company",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createsyncworkflow(
            template=template, creator=creator, attributes=attributes, request_options=request_options
        )
        return _response.data

    async def launchasynchronously(
        self,
        *,
        template: WorkflowTemplateIdModel,
        creator: CreatorEmailModel,
        attributes: AttributesModel,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowsLaunchAsynchronouslyResponse:
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
        WorkflowsLaunchAsynchronouslyResponse
            The response of the initiated async workflow launch.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, AttributesModel, CreatorEmailModel

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.launchasynchronously(
                template="600b296c3e15a234ab88f884",
                creator=CreatorEmailModel(),
                attributes=AttributesModel(
                    counterparty_name="Example Company",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.launchasynchronously(
            template=template, creator=creator, attributes=attributes, request_options=request_options
        )
        return _response.data

    async def getasyncjobstatus(
        self, async_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkflowsGetAsyncJobStatusResponse:
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
        WorkflowsGetAsyncJobStatusResponse
            The status of the workflow launch.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.getasyncjobstatus(
                async_job_id="asyncJobId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getasyncjobstatus(async_job_id, request_options=request_options)
        return _response.data

    async def getworkflow(
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
            await client.workflows.getworkflow(
                id="abcd1234",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getworkflow(id, request_options=request_options)
        return _response.data

    async def listapprovals(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkflowsListApprovalsResponse:
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
        WorkflowsListApprovalsResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.listapprovals(
                id="abcd1234",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listapprovals(id, request_options=request_options)
        return _response.data

    async def getapprovalrequests(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        actor_details: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowsGetApprovalRequestsResponse:
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
        WorkflowsGetApprovalRequestsResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.getapprovalrequests(
                id="id",
                actor_details=False,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getapprovalrequests(
            id, page=page, page_size=page_size, actor_details=actor_details, request_options=request_options
        )
        return _response.data

    async def updateapprovalstatus(
        self,
        id: str,
        role_id: str,
        *,
        user: WorkflowsUpdateApprovalStatusRequestUser,
        status: WorkflowsUpdateApprovalStatusRequestStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowsUpdateApprovalStatusResponse:
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
        WorkflowsUpdateApprovalStatusResponse
            200

        Examples
        --------
        import asyncio

        from fern.workflows import (
            WorkflowsUpdateApprovalStatusRequestStatus,
            WorkflowsUpdateApprovalStatusRequestUser,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.updateapprovalstatus(
                id="abcd1234",
                role_id="roleId",
                user=WorkflowsUpdateApprovalStatusRequestUser(),
                status=WorkflowsUpdateApprovalStatusRequestStatus.APPROVED,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updateapprovalstatus(
            id, role_id, user=user, status=status, request_options=request_options
        )
        return _response.data

    async def getturnhistory(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowsGetTurnHistoryResponse:
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
        WorkflowsGetTurnHistoryResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.getturnhistory(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getturnhistory(
            id, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def listsignatures(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkflowsListSignaturesResponse:
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
        WorkflowsListSignaturesResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.listsignatures(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listsignatures(id, request_options=request_options)
        return _response.data

    async def listallparticipants(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        email: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowsListAllParticipantsResponse:
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
        WorkflowsListAllParticipantsResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.listallparticipants(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listallparticipants(
            id, page=page, page_size=page_size, email=email, request_options=request_options
        )
        return _response.data

    async def reverttoreview(
        self,
        id: str,
        *,
        user: WorkflowsRevertToReviewRequestUser,
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
        None

        Examples
        --------
        import asyncio

        from fern.workflows import WorkflowsRevertToReviewRequestUser

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.reverttoreview(
                id="id",
                as_user_email="jane.doe@test.com",
                as_user_id="5f0375c4cdc1927a3c5edcd3",
                user=WorkflowsRevertToReviewRequestUser(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reverttoreview(
            id, user=user, as_user_email=as_user_email, as_user_id=as_user_id, request_options=request_options
        )
        return _response.data

    async def createcomment(
        self,
        id: str,
        *,
        creator: CreatorEmailModel,
        comment: str,
        add_users_to_workflow: typing.Optional[bool] = OMIT,
        replied_to_activity_feed_message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseActivityFeedItemModel:
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
        BaseActivityFeedItemModel
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CreatorEmailModel

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.createcomment(
                id="id",
                creator=CreatorEmailModel(),
                comment="comment",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createcomment(
            id,
            creator=creator,
            comment=comment,
            add_users_to_workflow=add_users_to_workflow,
            replied_to_activity_feed_message_id=replied_to_activity_feed_message_id,
            request_options=request_options,
        )
        return _response.data

    async def updatemetadata(
        self,
        id: str,
        *,
        updates: typing.Sequence[WorkflowsUpdateMetadataRequestUpdatesItem],
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowsUpdateMetadataResponse:
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
        WorkflowsUpdateMetadataResponse
            200

        Examples
        --------
        import asyncio

        from fern.workflows import (
            WorkflowsUpdateMetadataRequestUpdatesItem,
            WorkflowsUpdateMetadataRequestUpdatesItemAction,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.updatemetadata(
                id="id",
                as_user_email="jane.doe@test.com",
                as_user_id="5f0375c4cdc1927a3c5edcd3",
                updates=[
                    WorkflowsUpdateMetadataRequestUpdatesItem(
                        action=WorkflowsUpdateMetadataRequestUpdatesItemAction.SET,
                        path="counterpartyName",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatemetadata(
            id,
            updates=updates,
            as_user_email=as_user_email,
            as_user_id=as_user_id,
            comment=comment,
            request_options=request_options,
        )
        return _response.data

    async def getdocumentbykey(
        self, id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkflowsGetDocumentByKeyResponse:
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
        WorkflowsGetDocumentByKeyResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.getdocumentbykey(
                id="id",
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getdocumentbykey(id, key, request_options=request_options)
        return _response.data

    async def getemailthreads(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowsGetEmailThreadsResponse:
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
        WorkflowsGetEmailThreadsResponse
            GET Emails Response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.getemailthreads(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getemailthreads(
            id, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def getemailthread(
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
            await client.workflows.getemailthread(
                id="id",
                email_thread_id="emailThreadId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getemailthread(id, email_thread_id, request_options=request_options)
        return _response.data

    async def getattachmentfromemailthread(
        self,
        id: str,
        email_thread_id: str,
        attachment_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowsGetAttachmentFromEmailThreadResponse:
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
        WorkflowsGetAttachmentFromEmailThreadResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.getattachmentfromemailthread(
                id="id",
                email_thread_id="emailThreadId",
                attachment_id="attachmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getattachmentfromemailthread(
            id, email_thread_id, attachment_id, request_options=request_options
        )
        return _response.data

    async def listallworkflowschemas(
        self,
        *,
        form: str,
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowsListAllWorkflowSchemasResponse:
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
        WorkflowsListAllWorkflowSchemasResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.listallworkflowschemas(
                as_user_email="jane.doe@test.com",
                as_user_id="5f0375c4cdc1927a3c5edcd3",
                form="form",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listallworkflowschemas(
            form=form, as_user_email=as_user_email, as_user_id=as_user_id, request_options=request_options
        )
        return _response.data

    async def getworkflowschema(
        self,
        id: str,
        *,
        form: typing.Optional[str] = None,
        as_user_email: typing.Optional[str] = None,
        as_user_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowsGetWorkflowSchemaResponse:
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
        WorkflowsGetWorkflowSchemaResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.getworkflowschema(
                id="id",
                as_user_email="jane.doe@test.com",
                as_user_id="5f0375c4cdc1927a3c5edcd3",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getworkflowschema(
            id, form=form, as_user_email=as_user_email, as_user_id=as_user_id, request_options=request_options
        )
        return _response.data
