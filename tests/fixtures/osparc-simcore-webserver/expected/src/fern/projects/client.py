

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.boot_options import BootOptions
from ..types.conversation_message_type import ConversationMessageType
from ..types.conversation_type import ConversationType
from ..types.envelope_conversation_message_rest_get import EnvelopeConversationMessageRestGet
from ..types.envelope_conversation_rest_get import EnvelopeConversationRestGet
from ..types.envelope_dict_annotated_str_string_constraints_image_resources import (
    EnvelopeDictAnnotatedStrStringConstraintsImageResources,
)
from ..types.envelope_dict_uuid_project_input_get import EnvelopeDictUuidProjectInputGet
from ..types.envelope_dict_uuid_project_output_get import EnvelopeDictUuidProjectOutputGet
from ..types.envelope_get_project_inactivity_response import EnvelopeGetProjectInactivityResponse
from ..types.envelope_list_project_group_get import EnvelopeListProjectGroupGet
from ..types.envelope_list_project_metadata_port_get import EnvelopeListProjectMetadataPortGet
from ..types.envelope_list_project_node_preview import EnvelopeListProjectNodePreview
from ..types.envelope_node_created import EnvelopeNodeCreated
from ..types.envelope_node_retrieved import EnvelopeNodeRetrieved
from ..types.envelope_project_get import EnvelopeProjectGet
from ..types.envelope_project_group_access import EnvelopeProjectGroupAccess
from ..types.envelope_project_group_get import EnvelopeProjectGroupGet
from ..types.envelope_project_metadata_get import EnvelopeProjectMetadataGet
from ..types.envelope_project_node_preview import EnvelopeProjectNodePreview
from ..types.envelope_project_node_services_get import EnvelopeProjectNodeServicesGet
from ..types.envelope_project_share_accepted import EnvelopeProjectShareAccepted
from ..types.envelope_project_state_output_schema import EnvelopeProjectStateOutputSchema
from ..types.envelope_task_get import EnvelopeTaskGet
from ..types.envelope_union_node_get_idle_node_get_unknown_running_dynamic_service_details_node_get import (
    EnvelopeUnionNodeGetIdleNodeGetUnknownRunningDynamicServiceDetailsNodeGet,
)
from ..types.envelope_union_pricing_unit_get_none_type import EnvelopeUnionPricingUnitGetNoneType
from ..types.envelope_union_wallet_get_none_type import EnvelopeUnionWalletGetNoneType
from ..types.envelope_wallet_get import EnvelopeWalletGet
from ..types.group_id_int import GroupIdInt
from ..types.input_id import InputId
from ..types.inputs_dict_input import InputsDictInput
from ..types.long_truncated_str import LongTruncatedStr
from ..types.node_ui_patch import NodeUiPatch
from ..types.page_conversation_message_rest_get import PageConversationMessageRestGet
from ..types.page_conversation_rest_get import PageConversationRestGet
from ..types.page_project_list_item import PageProjectListItem
from ..types.project_input_update import ProjectInputUpdate
from ..types.project_template_type import ProjectTemplateType
from ..types.project_type_api import ProjectTypeApi
from ..types.short_truncated_str import ShortTruncatedStr
from ..types.study_ui_input import StudyUiInput
from ..types.unit_str import UnitStr
from ..types.wallet_id_int import WalletIdInt
from .raw_client import AsyncRawProjectsClient, RawProjectsClient
from .types.create_project_request_body import CreateProjectRequestBody
from .types.pay_project_debt_request_amount import PayProjectDebtRequestAmount
from .types.project_metadata_update_custom_value import ProjectMetadataUpdateCustomValue


OMIT = typing.cast(typing.Any, ...)


class ProjectsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProjectsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProjectsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProjectsClient
        """
        return self._raw_client

    def export_project(self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        creates an archive of the project and downloads it

        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.export_project(
            project_id="project_id",
        )
        """
        _response = self._raw_client.export_project(project_id, request_options=request_options)
        return _response.data

    def list_projects(
        self,
        *,
        type: typing.Optional[ProjectTypeApi] = None,
        template_type: typing.Optional[ProjectTemplateType] = None,
        show_hidden: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        folder_id: typing.Optional[int] = None,
        workspace_id: typing.Optional[int] = None,
        filters: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageProjectListItem:
        """
        Parameters
        ----------
        type : typing.Optional[ProjectTypeApi]

        template_type : typing.Optional[ProjectTemplateType]

        show_hidden : typing.Optional[bool]

        search : typing.Optional[str]

        folder_id : typing.Optional[int]

        workspace_id : typing.Optional[int]

        filters : typing.Optional[str]

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageProjectListItem
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.list_projects()
        """
        _response = self._raw_client.list_projects(
            type=type,
            template_type=template_type,
            show_hidden=show_hidden,
            search=search,
            folder_id=folder_id,
            workspace_id=workspace_id,
            filters=filters,
            order_by=order_by,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def create_project(
        self,
        *,
        request: CreateProjectRequestBody,
        x_simcore_user_agent: typing.Optional[str] = None,
        x_simcore_parent_project_uuid: typing.Optional[str] = None,
        x_simcore_parent_node_id: typing.Optional[str] = None,
        from_study: typing.Optional[str] = None,
        as_template: typing.Optional[bool] = None,
        copy_data: typing.Optional[bool] = None,
        hidden: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeTaskGet:
        """
        Creates a new project or copies an existing one. NOTE: implemented as a long running task, i.e. requires polling `status_href` (HTTP_200_OK) to get status and `result_href` (HTTP_201_CREATED) to get created project

        Parameters
        ----------
        request : CreateProjectRequestBody

        x_simcore_user_agent : typing.Optional[str]

        x_simcore_parent_project_uuid : typing.Optional[str]

        x_simcore_parent_node_id : typing.Optional[str]

        from_study : typing.Optional[str]

        as_template : typing.Optional[bool]

        copy_data : typing.Optional[bool]

        hidden : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTaskGet
            Successful Response

        Examples
        --------
        from fern import AccessRights, FernApi, ProjectCreateNew

        client = FernApi()
        client.projects.create_project(
            request=ProjectCreateNew(
                name="name",
                workbench={"key": "value"},
                access_rights={
                    "key": AccessRights(
                        read=True,
                        write=True,
                        delete=True,
                    )
                },
            ),
        )
        """
        _response = self._raw_client.create_project(
            request=request,
            x_simcore_user_agent=x_simcore_user_agent,
            x_simcore_parent_project_uuid=x_simcore_parent_project_uuid,
            x_simcore_parent_node_id=x_simcore_parent_node_id,
            from_study=from_study,
            as_template=as_template,
            copy_data=copy_data,
            hidden=hidden,
            request_options=request_options,
        )
        return _response.data

    def get_active_project(
        self, *, client_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeProjectGet:
        """
        Parameters
        ----------
        client_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.get_active_project(
            client_session_id="client_session_id",
        )
        """
        _response = self._raw_client.get_active_project(
            client_session_id=client_session_id, request_options=request_options
        )
        return _response.data

    def get_project(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeProjectGet:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.get_project(
            project_id="project_id",
        )
        """
        _response = self._raw_client.get_project(project_id, request_options=request_options)
        return _response.data

    def delete_project(self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.delete_project(
            project_id="project_id",
        )
        """
        _response = self._raw_client.delete_project(project_id, request_options=request_options)
        return _response.data

    def patch_project(
        self,
        project_id: str,
        *,
        name: typing.Optional[ShortTruncatedStr] = OMIT,
        description: typing.Optional[LongTruncatedStr] = OMIT,
        thumbnail: typing.Optional[str] = OMIT,
        classifiers: typing.Optional[typing.Sequence[str]] = OMIT,
        dev: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        ui: typing.Optional[StudyUiInput] = OMIT,
        quality: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        template_type: typing.Optional[ProjectTemplateType] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        project_id : str

        name : typing.Optional[ShortTruncatedStr]

        description : typing.Optional[LongTruncatedStr]

        thumbnail : typing.Optional[str]

        classifiers : typing.Optional[typing.Sequence[str]]

        dev : typing.Optional[typing.Dict[str, typing.Any]]

        ui : typing.Optional[StudyUiInput]

        quality : typing.Optional[typing.Dict[str, typing.Any]]

        template_type : typing.Optional[ProjectTemplateType]

        hidden : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.patch_project(
            project_id="project_id",
        )
        """
        _response = self._raw_client.patch_project(
            project_id,
            name=name,
            description=description,
            thumbnail=thumbnail,
            classifiers=classifiers,
            dev=dev,
            ui=ui,
            quality=quality,
            template_type=template_type,
            hidden=hidden,
            request_options=request_options,
        )
        return _response.data

    def clone_project(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeTaskGet:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTaskGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.clone_project(
            project_id="project_id",
        )
        """
        _response = self._raw_client.clone_project(project_id, request_options=request_options)
        return _response.data

    def list_projects_full_search(
        self,
        *,
        filters: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        type: typing.Optional[ProjectTypeApi] = None,
        template_type: typing.Optional[ProjectTemplateType] = None,
        text: typing.Optional[str] = None,
        tag_ids: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageProjectListItem:
        """
        Parameters
        ----------
        filters : typing.Optional[str]

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        type : typing.Optional[ProjectTypeApi]

        template_type : typing.Optional[ProjectTemplateType]

        text : typing.Optional[str]

        tag_ids : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageProjectListItem
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.list_projects_full_search()
        """
        _response = self._raw_client.list_projects_full_search(
            filters=filters,
            order_by=order_by,
            limit=limit,
            offset=offset,
            type=type,
            template_type=template_type,
            text=text,
            tag_ids=tag_ids,
            request_options=request_options,
        )
        return _response.data

    def get_project_inactivity(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeGetProjectInactivityResponse:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeGetProjectInactivityResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.get_project_inactivity(
            project_id="project_id",
        )
        """
        _response = self._raw_client.get_project_inactivity(project_id, request_options=request_options)
        return _response.data

    def share_project(
        self,
        project_id: str,
        *,
        sharee_email: str,
        read: bool,
        write: bool,
        delete: bool,
        sharer_message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeProjectShareAccepted:
        """
        Parameters
        ----------
        project_id : str

        sharee_email : str

        read : bool

        write : bool

        delete : bool

        sharer_message : typing.Optional[str]
            An optional message from sharer to sharee

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectShareAccepted
            The request to share the project has been accepted, but the actual sharing process has to be confirmed.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.share_project(
            project_id="project_id",
            sharee_email="shareeEmail",
            read=True,
            write=True,
            delete=True,
        )
        """
        _response = self._raw_client.share_project(
            project_id,
            sharee_email=sharee_email,
            read=read,
            write=write,
            delete=delete,
            sharer_message=sharer_message,
            request_options=request_options,
        )
        return _response.data

    def create_project_group(
        self,
        project_id: str,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        delete: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeProjectGroupGet:
        """
        Parameters
        ----------
        project_id : str

        group_id : GroupIdInt

        read : bool

        write : bool

        delete : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectGroupGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.create_project_group(
            project_id="project_id",
            group_id=1,
            read=True,
            write=True,
            delete=True,
        )
        """
        _response = self._raw_client.create_project_group(
            project_id, group_id, read=read, write=write, delete=delete, request_options=request_options
        )
        return _response.data

    def replace_project_group(
        self,
        project_id: str,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        delete: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeProjectGroupGet:
        """
        Parameters
        ----------
        project_id : str

        group_id : GroupIdInt

        read : bool

        write : bool

        delete : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectGroupGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.replace_project_group(
            project_id="project_id",
            group_id=1,
            read=True,
            write=True,
            delete=True,
        )
        """
        _response = self._raw_client.replace_project_group(
            project_id, group_id, read=read, write=write, delete=delete, request_options=request_options
        )
        return _response.data

    def delete_project_group(
        self, project_id: str, group_id: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        project_id : str

        group_id : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.delete_project_group(
            project_id="project_id",
            group_id=1,
        )
        """
        _response = self._raw_client.delete_project_group(project_id, group_id, request_options=request_options)
        return _response.data

    def list_project_groups(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListProjectGroupGet:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListProjectGroupGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.list_project_groups(
            project_id="project_id",
        )
        """
        _response = self._raw_client.list_project_groups(project_id, request_options=request_options)
        return _response.data

    def list_project_conversations(
        self,
        project_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageConversationRestGet:
        """
        Parameters
        ----------
        project_id : str

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageConversationRestGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.list_project_conversations(
            project_id="project_id",
        )
        """
        _response = self._raw_client.list_project_conversations(
            project_id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def create_project_conversation(
        self,
        project_id: str,
        *,
        name: str,
        type: ConversationType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeConversationRestGet:
        """
        Parameters
        ----------
        project_id : str

        name : str

        type : ConversationType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeConversationRestGet
            Successful Response

        Examples
        --------
        from fern import ConversationType, FernApi

        client = FernApi()
        client.projects.create_project_conversation(
            project_id="project_id",
            name="name",
            type=ConversationType.PROJECT_STATIC,
        )
        """
        _response = self._raw_client.create_project_conversation(
            project_id, name=name, type=type, request_options=request_options
        )
        return _response.data

    def get_project_conversation(
        self, project_id: str, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeConversationRestGet:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeConversationRestGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.get_project_conversation(
            project_id="project_id",
            conversation_id="conversation_id",
        )
        """
        _response = self._raw_client.get_project_conversation(
            project_id, conversation_id, request_options=request_options
        )
        return _response.data

    def update_project_conversation(
        self,
        project_id: str,
        conversation_id: str,
        *,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeConversationRestGet:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeConversationRestGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.update_project_conversation(
            project_id="project_id",
            conversation_id="conversation_id",
            name="name",
        )
        """
        _response = self._raw_client.update_project_conversation(
            project_id, conversation_id, name=name, request_options=request_options
        )
        return _response.data

    def delete_project_conversation(
        self, project_id: str, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.delete_project_conversation(
            project_id="project_id",
            conversation_id="conversation_id",
        )
        """
        _response = self._raw_client.delete_project_conversation(
            project_id, conversation_id, request_options=request_options
        )
        return _response.data

    def list_project_conversation_messages(
        self,
        project_id: str,
        conversation_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageConversationMessageRestGet:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageConversationMessageRestGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.list_project_conversation_messages(
            project_id="project_id",
            conversation_id="conversation_id",
        )
        """
        _response = self._raw_client.list_project_conversation_messages(
            project_id, conversation_id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def create_project_conversation_message(
        self,
        project_id: str,
        conversation_id: str,
        *,
        content: str,
        type: ConversationMessageType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeConversationMessageRestGet:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        content : str

        type : ConversationMessageType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeConversationMessageRestGet
            Successful Response

        Examples
        --------
        from fern import ConversationMessageType, FernApi

        client = FernApi()
        client.projects.create_project_conversation_message(
            project_id="project_id",
            conversation_id="conversation_id",
            content="content",
            type=ConversationMessageType.MESSAGE,
        )
        """
        _response = self._raw_client.create_project_conversation_message(
            project_id, conversation_id, content=content, type=type, request_options=request_options
        )
        return _response.data

    def get_project_conversation_message(
        self,
        project_id: str,
        conversation_id: str,
        message_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeConversationMessageRestGet:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeConversationMessageRestGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.get_project_conversation_message(
            project_id="project_id",
            conversation_id="conversation_id",
            message_id="message_id",
        )
        """
        _response = self._raw_client.get_project_conversation_message(
            project_id, conversation_id, message_id, request_options=request_options
        )
        return _response.data

    def update_project_conversation_message(
        self,
        project_id: str,
        conversation_id: str,
        message_id: str,
        *,
        content: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeConversationMessageRestGet:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        message_id : str

        content : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeConversationMessageRestGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.update_project_conversation_message(
            project_id="project_id",
            conversation_id="conversation_id",
            message_id="message_id",
            content="content",
        )
        """
        _response = self._raw_client.update_project_conversation_message(
            project_id, conversation_id, message_id, content=content, request_options=request_options
        )
        return _response.data

    def delete_project_conversation_message(
        self,
        project_id: str,
        conversation_id: str,
        message_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.delete_project_conversation_message(
            project_id="project_id",
            conversation_id="conversation_id",
            message_id="message_id",
        )
        """
        _response = self._raw_client.delete_project_conversation_message(
            project_id, conversation_id, message_id, request_options=request_options
        )
        return _response.data

    def replace_project_folder(
        self,
        project_id: str,
        folder_id: typing.Optional[int],
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Move project to the folder

        Parameters
        ----------
        project_id : str

        folder_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.replace_project_folder(
            project_id="project_id",
            folder_id=1,
        )
        """
        _response = self._raw_client.replace_project_folder(project_id, folder_id, request_options=request_options)
        return _response.data

    def get_project_metadata(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeProjectMetadataGet:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectMetadataGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.get_project_metadata(
            project_id="project_id",
        )
        """
        _response = self._raw_client.get_project_metadata(project_id, request_options=request_options)
        return _response.data

    def update_project_metadata(
        self,
        project_id: str,
        *,
        custom: typing.Dict[str, ProjectMetadataUpdateCustomValue],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeProjectMetadataGet:
        """
        Parameters
        ----------
        project_id : str

        custom : typing.Dict[str, ProjectMetadataUpdateCustomValue]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectMetadataGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.update_project_metadata(
            project_id="project_id",
            custom={"key": True},
        )
        """
        _response = self._raw_client.update_project_metadata(project_id, custom=custom, request_options=request_options)
        return _response.data

    def create_node(
        self,
        project_id: str,
        *,
        service_key: str,
        service_version: str,
        service_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeNodeCreated:
        """
        Parameters
        ----------
        project_id : str

        service_key : str

        service_version : str

        service_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeNodeCreated
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.create_node(
            project_id="project_id",
            service_key="service_key",
            service_version="service_version",
        )
        """
        _response = self._raw_client.create_node(
            project_id,
            service_key=service_key,
            service_version=service_version,
            service_id=service_id,
            request_options=request_options,
        )
        return _response.data

    def get_node(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeUnionNodeGetIdleNodeGetUnknownRunningDynamicServiceDetailsNodeGet:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeUnionNodeGetIdleNodeGetUnknownRunningDynamicServiceDetailsNodeGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.get_node(
            project_id="project_id",
            node_id="node_id",
        )
        """
        _response = self._raw_client.get_node(project_id, node_id, request_options=request_options)
        return _response.data

    def delete_node(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.delete_node(
            project_id="project_id",
            node_id="node_id",
        )
        """
        _response = self._raw_client.delete_node(project_id, node_id, request_options=request_options)
        return _response.data

    def patch_project_node(
        self,
        project_id: str,
        node_id: str,
        *,
        key: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        label: typing.Optional[str] = OMIT,
        inputs: typing.Optional[InputsDictInput] = OMIT,
        inputs_required: typing.Optional[typing.Sequence[InputId]] = OMIT,
        inputs_units: typing.Optional[typing.Dict[str, typing.Optional[UnitStr]]] = OMIT,
        input_nodes: typing.Optional[typing.Sequence[str]] = OMIT,
        progress: typing.Optional[float] = OMIT,
        boot_options: typing.Optional[BootOptions] = OMIT,
        outputs: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        ui: typing.Optional[NodeUiPatch] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        key : typing.Optional[str]

        version : typing.Optional[str]

        label : typing.Optional[str]

        inputs : typing.Optional[InputsDictInput]

        inputs_required : typing.Optional[typing.Sequence[InputId]]

        inputs_units : typing.Optional[typing.Dict[str, typing.Optional[UnitStr]]]

        input_nodes : typing.Optional[typing.Sequence[str]]

        progress : typing.Optional[float]

        boot_options : typing.Optional[BootOptions]

        outputs : typing.Optional[typing.Dict[str, typing.Any]]

        ui : typing.Optional[NodeUiPatch]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.patch_project_node(
            project_id="project_id",
            node_id="node_id",
        )
        """
        _response = self._raw_client.patch_project_node(
            project_id,
            node_id,
            key=key,
            version=version,
            label=label,
            inputs=inputs,
            inputs_required=inputs_required,
            inputs_units=inputs_units,
            input_nodes=input_nodes,
            progress=progress,
            boot_options=boot_options,
            outputs=outputs,
            ui=ui,
            request_options=request_options,
        )
        return _response.data

    def retrieve_node(
        self,
        project_id: str,
        node_id: str,
        *,
        port_keys: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeNodeRetrieved:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        port_keys : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeNodeRetrieved
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.retrieve_node(
            project_id="project_id",
            node_id="node_id",
        )
        """
        _response = self._raw_client.retrieve_node(
            project_id, node_id, port_keys=port_keys, request_options=request_options
        )
        return _response.data

    def start_node(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.start_node(
            project_id="project_id",
            node_id="node_id",
        )
        """
        _response = self._raw_client.start_node(project_id, node_id, request_options=request_options)
        return _response.data

    def stop_node(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeTaskGet:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTaskGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.stop_node(
            project_id="project_id",
            node_id="node_id",
        )
        """
        _response = self._raw_client.stop_node(project_id, node_id, request_options=request_options)
        return _response.data

    def restart_node(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Note that it has only effect on nodes associated to dynamic services

        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.restart_node(
            project_id="project_id",
            node_id="node_id",
        )
        """
        _response = self._raw_client.restart_node(project_id, node_id, request_options=request_options)
        return _response.data

    def update_node_outputs(
        self,
        project_id: str,
        node_id: str,
        *,
        outputs: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        outputs : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.update_node_outputs(
            project_id="project_id",
            node_id="node_id",
            outputs={"key": "value"},
        )
        """
        _response = self._raw_client.update_node_outputs(
            project_id, node_id, outputs=outputs, request_options=request_options
        )
        return _response.data

    def get_node_resources(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeDictAnnotatedStrStringConstraintsImageResources:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeDictAnnotatedStrStringConstraintsImageResources
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.get_node_resources(
            project_id="project_id",
            node_id="node_id",
        )
        """
        _response = self._raw_client.get_node_resources(project_id, node_id, request_options=request_options)
        return _response.data

    def replace_node_resources(
        self,
        project_id: str,
        node_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeDictAnnotatedStrStringConstraintsImageResources:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeDictAnnotatedStrStringConstraintsImageResources
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.replace_node_resources(
            project_id="project_id",
            node_id="node_id",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.replace_node_resources(
            project_id, node_id, request=request, request_options=request_options
        )
        return _response.data

    def get_project_services(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeProjectNodeServicesGet:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectNodeServicesGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.get_project_services(
            project_id="project_id",
        )
        """
        _response = self._raw_client.get_project_services(project_id, request_options=request_options)
        return _response.data

    def get_project_services_access_for_gid(
        self, project_id: str, *, for_gid: GroupIdInt, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeProjectGroupAccess:
        """
        Check whether provided group has access to the project services

        Parameters
        ----------
        project_id : str

        for_gid : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectGroupAccess
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.get_project_services_access_for_gid(
            project_id="project_id",
            for_gid=1,
        )
        """
        _response = self._raw_client.get_project_services_access_for_gid(
            project_id, for_gid=for_gid, request_options=request_options
        )
        return _response.data

    def list_project_nodes_previews(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListProjectNodePreview:
        """
        Lists all previews in the node's project

        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListProjectNodePreview
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.list_project_nodes_previews(
            project_id="project_id",
        )
        """
        _response = self._raw_client.list_project_nodes_previews(project_id, request_options=request_options)
        return _response.data

    def get_project_node_preview(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeProjectNodePreview:
        """
        Gets a give node's preview

        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectNodePreview
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.get_project_node_preview(
            project_id="project_id",
            node_id="node_id",
        )
        """
        _response = self._raw_client.get_project_node_preview(project_id, node_id, request_options=request_options)
        return _response.data

    def get_project_node_pricing_unit(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeUnionPricingUnitGetNoneType:
        """
        Get currently connected pricing unit to the project node.

        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeUnionPricingUnitGetNoneType
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.get_project_node_pricing_unit(
            project_id="project_id",
            node_id="node_id",
        )
        """
        _response = self._raw_client.get_project_node_pricing_unit(project_id, node_id, request_options=request_options)
        return _response.data

    def connect_pricing_unit_to_project_node(
        self,
        project_id: str,
        node_id: str,
        pricing_plan_id: int,
        pricing_unit_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Connect pricing unit to the project node (Project node can have only one pricing unit)

        Parameters
        ----------
        project_id : str

        node_id : str

        pricing_plan_id : int

        pricing_unit_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.connect_pricing_unit_to_project_node(
            project_id="project_id",
            node_id="node_id",
            pricing_plan_id=1,
            pricing_unit_id=1,
        )
        """
        _response = self._raw_client.connect_pricing_unit_to_project_node(
            project_id, node_id, pricing_plan_id, pricing_unit_id, request_options=request_options
        )
        return _response.data

    def get_project_inputs(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeDictUuidProjectInputGet:
        """
        New in version *0.10*

        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeDictUuidProjectInputGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.get_project_inputs(
            project_id="project_id",
        )
        """
        _response = self._raw_client.get_project_inputs(project_id, request_options=request_options)
        return _response.data

    def update_project_inputs(
        self,
        project_id: str,
        *,
        request: typing.Sequence[ProjectInputUpdate],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeDictUuidProjectInputGet:
        """
        New in version *0.10*

        Parameters
        ----------
        project_id : str

        request : typing.Sequence[ProjectInputUpdate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeDictUuidProjectInputGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.update_project_inputs(
            project_id="project_id",
            request=[],
        )
        """
        _response = self._raw_client.update_project_inputs(project_id, request=request, request_options=request_options)
        return _response.data

    def get_project_outputs(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeDictUuidProjectOutputGet:
        """
        New in version *0.10*

        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeDictUuidProjectOutputGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.get_project_outputs(
            project_id="project_id",
        )
        """
        _response = self._raw_client.get_project_outputs(project_id, request_options=request_options)
        return _response.data

    def list_project_metadata_ports(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListProjectMetadataPortGet:
        """
        New in version *0.12*

        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListProjectMetadataPortGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.list_project_metadata_ports(
            project_id="project_id",
        )
        """
        _response = self._raw_client.list_project_metadata_ports(project_id, request_options=request_options)
        return _response.data

    def open_project(
        self,
        project_id: str,
        *,
        request: str,
        disable_service_auto_start: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeProjectGet:
        """
        Parameters
        ----------
        project_id : str

        request : str

        disable_service_auto_start : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.open_project(
            project_id="project_id",
            request="string",
        )
        """
        _response = self._raw_client.open_project(
            project_id,
            request=request,
            disable_service_auto_start=disable_service_auto_start,
            request_options=request_options,
        )
        return _response.data

    def close_project(
        self, project_id: str, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        project_id : str

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.close_project(
            project_id="project_id",
            request="string",
        )
        """
        _response = self._raw_client.close_project(project_id, request=request, request_options=request_options)
        return _response.data

    def get_project_state(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeProjectStateOutputSchema:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectStateOutputSchema
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.get_project_state(
            project_id="project_id",
        )
        """
        _response = self._raw_client.get_project_state(project_id, request_options=request_options)
        return _response.data

    def add_project_tag(
        self, project_uuid: str, tag_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeProjectGet:
        """
        Links an existing label with an existing study

        NOTE: that the tag is not created here

        Parameters
        ----------
        project_uuid : str

        tag_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.add_project_tag(
            project_uuid="project_uuid",
            tag_id=1,
        )
        """
        _response = self._raw_client.add_project_tag(project_uuid, tag_id, request_options=request_options)
        return _response.data

    def remove_project_tag(
        self, project_uuid: str, tag_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeProjectGet:
        """
        Removes an existing link between a label and a study

        NOTE: that the tag is not deleted here

        Parameters
        ----------
        project_uuid : str

        tag_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.remove_project_tag(
            project_uuid="project_uuid",
            tag_id=1,
        )
        """
        _response = self._raw_client.remove_project_tag(project_uuid, tag_id, request_options=request_options)
        return _response.data

    def get_project_wallet(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeUnionWalletGetNoneType:
        """
        Get current connected wallet to the project.

        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeUnionWalletGetNoneType
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.get_project_wallet(
            project_id="project_id",
        )
        """
        _response = self._raw_client.get_project_wallet(project_id, request_options=request_options)
        return _response.data

    def connect_wallet_to_project(
        self, project_id: str, wallet_id: WalletIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeWalletGet:
        """
        Connect wallet to the project (Project can have only one wallet)

        Parameters
        ----------
        project_id : str

        wallet_id : WalletIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWalletGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.connect_wallet_to_project(
            project_id="project_id",
            wallet_id=1,
        )
        """
        _response = self._raw_client.connect_wallet_to_project(project_id, wallet_id, request_options=request_options)
        return _response.data

    def pay_project_debt(
        self,
        project_id: str,
        wallet_id: WalletIdInt,
        *,
        amount: PayProjectDebtRequestAmount,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        project_id : str

        wallet_id : WalletIdInt

        amount : PayProjectDebtRequestAmount

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.pay_project_debt(
            project_id="project_id",
            wallet_id=1,
            amount=1.1,
        )
        """
        _response = self._raw_client.pay_project_debt(
            project_id, wallet_id, amount=amount, request_options=request_options
        )
        return _response.data

    def move_project_to_workspace(
        self,
        project_id: str,
        workspace_id: typing.Optional[int],
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Move project to the workspace

        Parameters
        ----------
        project_id : str

        workspace_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.move_project_to_workspace(
            project_id="project_id",
            workspace_id=1,
        )
        """
        _response = self._raw_client.move_project_to_workspace(
            project_id, workspace_id, request_options=request_options
        )
        return _response.data


class AsyncProjectsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProjectsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProjectsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProjectsClient
        """
        return self._raw_client

    async def export_project(self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        creates an archive of the project and downloads it

        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.export_project(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.export_project(project_id, request_options=request_options)
        return _response.data

    async def list_projects(
        self,
        *,
        type: typing.Optional[ProjectTypeApi] = None,
        template_type: typing.Optional[ProjectTemplateType] = None,
        show_hidden: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        folder_id: typing.Optional[int] = None,
        workspace_id: typing.Optional[int] = None,
        filters: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageProjectListItem:
        """
        Parameters
        ----------
        type : typing.Optional[ProjectTypeApi]

        template_type : typing.Optional[ProjectTemplateType]

        show_hidden : typing.Optional[bool]

        search : typing.Optional[str]

        folder_id : typing.Optional[int]

        workspace_id : typing.Optional[int]

        filters : typing.Optional[str]

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageProjectListItem
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.list_projects()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_projects(
            type=type,
            template_type=template_type,
            show_hidden=show_hidden,
            search=search,
            folder_id=folder_id,
            workspace_id=workspace_id,
            filters=filters,
            order_by=order_by,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def create_project(
        self,
        *,
        request: CreateProjectRequestBody,
        x_simcore_user_agent: typing.Optional[str] = None,
        x_simcore_parent_project_uuid: typing.Optional[str] = None,
        x_simcore_parent_node_id: typing.Optional[str] = None,
        from_study: typing.Optional[str] = None,
        as_template: typing.Optional[bool] = None,
        copy_data: typing.Optional[bool] = None,
        hidden: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeTaskGet:
        """
        Creates a new project or copies an existing one. NOTE: implemented as a long running task, i.e. requires polling `status_href` (HTTP_200_OK) to get status and `result_href` (HTTP_201_CREATED) to get created project

        Parameters
        ----------
        request : CreateProjectRequestBody

        x_simcore_user_agent : typing.Optional[str]

        x_simcore_parent_project_uuid : typing.Optional[str]

        x_simcore_parent_node_id : typing.Optional[str]

        from_study : typing.Optional[str]

        as_template : typing.Optional[bool]

        copy_data : typing.Optional[bool]

        hidden : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTaskGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AccessRights, AsyncFernApi, ProjectCreateNew

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.create_project(
                request=ProjectCreateNew(
                    name="name",
                    workbench={"key": "value"},
                    access_rights={
                        "key": AccessRights(
                            read=True,
                            write=True,
                            delete=True,
                        )
                    },
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_project(
            request=request,
            x_simcore_user_agent=x_simcore_user_agent,
            x_simcore_parent_project_uuid=x_simcore_parent_project_uuid,
            x_simcore_parent_node_id=x_simcore_parent_node_id,
            from_study=from_study,
            as_template=as_template,
            copy_data=copy_data,
            hidden=hidden,
            request_options=request_options,
        )
        return _response.data

    async def get_active_project(
        self, *, client_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeProjectGet:
        """
        Parameters
        ----------
        client_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.get_active_project(
                client_session_id="client_session_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_active_project(
            client_session_id=client_session_id, request_options=request_options
        )
        return _response.data

    async def get_project(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeProjectGet:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.get_project(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project(project_id, request_options=request_options)
        return _response.data

    async def delete_project(self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.delete_project(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_project(project_id, request_options=request_options)
        return _response.data

    async def patch_project(
        self,
        project_id: str,
        *,
        name: typing.Optional[ShortTruncatedStr] = OMIT,
        description: typing.Optional[LongTruncatedStr] = OMIT,
        thumbnail: typing.Optional[str] = OMIT,
        classifiers: typing.Optional[typing.Sequence[str]] = OMIT,
        dev: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        ui: typing.Optional[StudyUiInput] = OMIT,
        quality: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        template_type: typing.Optional[ProjectTemplateType] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        project_id : str

        name : typing.Optional[ShortTruncatedStr]

        description : typing.Optional[LongTruncatedStr]

        thumbnail : typing.Optional[str]

        classifiers : typing.Optional[typing.Sequence[str]]

        dev : typing.Optional[typing.Dict[str, typing.Any]]

        ui : typing.Optional[StudyUiInput]

        quality : typing.Optional[typing.Dict[str, typing.Any]]

        template_type : typing.Optional[ProjectTemplateType]

        hidden : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.patch_project(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_project(
            project_id,
            name=name,
            description=description,
            thumbnail=thumbnail,
            classifiers=classifiers,
            dev=dev,
            ui=ui,
            quality=quality,
            template_type=template_type,
            hidden=hidden,
            request_options=request_options,
        )
        return _response.data

    async def clone_project(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeTaskGet:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTaskGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.clone_project(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.clone_project(project_id, request_options=request_options)
        return _response.data

    async def list_projects_full_search(
        self,
        *,
        filters: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        type: typing.Optional[ProjectTypeApi] = None,
        template_type: typing.Optional[ProjectTemplateType] = None,
        text: typing.Optional[str] = None,
        tag_ids: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageProjectListItem:
        """
        Parameters
        ----------
        filters : typing.Optional[str]

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        type : typing.Optional[ProjectTypeApi]

        template_type : typing.Optional[ProjectTemplateType]

        text : typing.Optional[str]

        tag_ids : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageProjectListItem
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.list_projects_full_search()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_projects_full_search(
            filters=filters,
            order_by=order_by,
            limit=limit,
            offset=offset,
            type=type,
            template_type=template_type,
            text=text,
            tag_ids=tag_ids,
            request_options=request_options,
        )
        return _response.data

    async def get_project_inactivity(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeGetProjectInactivityResponse:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeGetProjectInactivityResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.get_project_inactivity(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_inactivity(project_id, request_options=request_options)
        return _response.data

    async def share_project(
        self,
        project_id: str,
        *,
        sharee_email: str,
        read: bool,
        write: bool,
        delete: bool,
        sharer_message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeProjectShareAccepted:
        """
        Parameters
        ----------
        project_id : str

        sharee_email : str

        read : bool

        write : bool

        delete : bool

        sharer_message : typing.Optional[str]
            An optional message from sharer to sharee

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectShareAccepted
            The request to share the project has been accepted, but the actual sharing process has to be confirmed.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.share_project(
                project_id="project_id",
                sharee_email="shareeEmail",
                read=True,
                write=True,
                delete=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.share_project(
            project_id,
            sharee_email=sharee_email,
            read=read,
            write=write,
            delete=delete,
            sharer_message=sharer_message,
            request_options=request_options,
        )
        return _response.data

    async def create_project_group(
        self,
        project_id: str,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        delete: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeProjectGroupGet:
        """
        Parameters
        ----------
        project_id : str

        group_id : GroupIdInt

        read : bool

        write : bool

        delete : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectGroupGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.create_project_group(
                project_id="project_id",
                group_id=1,
                read=True,
                write=True,
                delete=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_project_group(
            project_id, group_id, read=read, write=write, delete=delete, request_options=request_options
        )
        return _response.data

    async def replace_project_group(
        self,
        project_id: str,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        delete: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeProjectGroupGet:
        """
        Parameters
        ----------
        project_id : str

        group_id : GroupIdInt

        read : bool

        write : bool

        delete : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectGroupGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.replace_project_group(
                project_id="project_id",
                group_id=1,
                read=True,
                write=True,
                delete=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_project_group(
            project_id, group_id, read=read, write=write, delete=delete, request_options=request_options
        )
        return _response.data

    async def delete_project_group(
        self, project_id: str, group_id: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        project_id : str

        group_id : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.delete_project_group(
                project_id="project_id",
                group_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_project_group(project_id, group_id, request_options=request_options)
        return _response.data

    async def list_project_groups(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListProjectGroupGet:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListProjectGroupGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.list_project_groups(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_project_groups(project_id, request_options=request_options)
        return _response.data

    async def list_project_conversations(
        self,
        project_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageConversationRestGet:
        """
        Parameters
        ----------
        project_id : str

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageConversationRestGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.list_project_conversations(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_project_conversations(
            project_id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def create_project_conversation(
        self,
        project_id: str,
        *,
        name: str,
        type: ConversationType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeConversationRestGet:
        """
        Parameters
        ----------
        project_id : str

        name : str

        type : ConversationType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeConversationRestGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ConversationType

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.create_project_conversation(
                project_id="project_id",
                name="name",
                type=ConversationType.PROJECT_STATIC,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_project_conversation(
            project_id, name=name, type=type, request_options=request_options
        )
        return _response.data

    async def get_project_conversation(
        self, project_id: str, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeConversationRestGet:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeConversationRestGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.get_project_conversation(
                project_id="project_id",
                conversation_id="conversation_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_conversation(
            project_id, conversation_id, request_options=request_options
        )
        return _response.data

    async def update_project_conversation(
        self,
        project_id: str,
        conversation_id: str,
        *,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeConversationRestGet:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeConversationRestGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.update_project_conversation(
                project_id="project_id",
                conversation_id="conversation_id",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_project_conversation(
            project_id, conversation_id, name=name, request_options=request_options
        )
        return _response.data

    async def delete_project_conversation(
        self, project_id: str, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.delete_project_conversation(
                project_id="project_id",
                conversation_id="conversation_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_project_conversation(
            project_id, conversation_id, request_options=request_options
        )
        return _response.data

    async def list_project_conversation_messages(
        self,
        project_id: str,
        conversation_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageConversationMessageRestGet:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageConversationMessageRestGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.list_project_conversation_messages(
                project_id="project_id",
                conversation_id="conversation_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_project_conversation_messages(
            project_id, conversation_id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def create_project_conversation_message(
        self,
        project_id: str,
        conversation_id: str,
        *,
        content: str,
        type: ConversationMessageType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeConversationMessageRestGet:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        content : str

        type : ConversationMessageType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeConversationMessageRestGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ConversationMessageType

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.create_project_conversation_message(
                project_id="project_id",
                conversation_id="conversation_id",
                content="content",
                type=ConversationMessageType.MESSAGE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_project_conversation_message(
            project_id, conversation_id, content=content, type=type, request_options=request_options
        )
        return _response.data

    async def get_project_conversation_message(
        self,
        project_id: str,
        conversation_id: str,
        message_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeConversationMessageRestGet:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeConversationMessageRestGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.get_project_conversation_message(
                project_id="project_id",
                conversation_id="conversation_id",
                message_id="message_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_conversation_message(
            project_id, conversation_id, message_id, request_options=request_options
        )
        return _response.data

    async def update_project_conversation_message(
        self,
        project_id: str,
        conversation_id: str,
        message_id: str,
        *,
        content: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeConversationMessageRestGet:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        message_id : str

        content : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeConversationMessageRestGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.update_project_conversation_message(
                project_id="project_id",
                conversation_id="conversation_id",
                message_id="message_id",
                content="content",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_project_conversation_message(
            project_id, conversation_id, message_id, content=content, request_options=request_options
        )
        return _response.data

    async def delete_project_conversation_message(
        self,
        project_id: str,
        conversation_id: str,
        message_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.delete_project_conversation_message(
                project_id="project_id",
                conversation_id="conversation_id",
                message_id="message_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_project_conversation_message(
            project_id, conversation_id, message_id, request_options=request_options
        )
        return _response.data

    async def replace_project_folder(
        self,
        project_id: str,
        folder_id: typing.Optional[int],
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Move project to the folder

        Parameters
        ----------
        project_id : str

        folder_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.replace_project_folder(
                project_id="project_id",
                folder_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_project_folder(
            project_id, folder_id, request_options=request_options
        )
        return _response.data

    async def get_project_metadata(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeProjectMetadataGet:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectMetadataGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.get_project_metadata(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_metadata(project_id, request_options=request_options)
        return _response.data

    async def update_project_metadata(
        self,
        project_id: str,
        *,
        custom: typing.Dict[str, ProjectMetadataUpdateCustomValue],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeProjectMetadataGet:
        """
        Parameters
        ----------
        project_id : str

        custom : typing.Dict[str, ProjectMetadataUpdateCustomValue]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectMetadataGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.update_project_metadata(
                project_id="project_id",
                custom={"key": True},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_project_metadata(
            project_id, custom=custom, request_options=request_options
        )
        return _response.data

    async def create_node(
        self,
        project_id: str,
        *,
        service_key: str,
        service_version: str,
        service_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeNodeCreated:
        """
        Parameters
        ----------
        project_id : str

        service_key : str

        service_version : str

        service_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeNodeCreated
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.create_node(
                project_id="project_id",
                service_key="service_key",
                service_version="service_version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_node(
            project_id,
            service_key=service_key,
            service_version=service_version,
            service_id=service_id,
            request_options=request_options,
        )
        return _response.data

    async def get_node(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeUnionNodeGetIdleNodeGetUnknownRunningDynamicServiceDetailsNodeGet:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeUnionNodeGetIdleNodeGetUnknownRunningDynamicServiceDetailsNodeGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.get_node(
                project_id="project_id",
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_node(project_id, node_id, request_options=request_options)
        return _response.data

    async def delete_node(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.delete_node(
                project_id="project_id",
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_node(project_id, node_id, request_options=request_options)
        return _response.data

    async def patch_project_node(
        self,
        project_id: str,
        node_id: str,
        *,
        key: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        label: typing.Optional[str] = OMIT,
        inputs: typing.Optional[InputsDictInput] = OMIT,
        inputs_required: typing.Optional[typing.Sequence[InputId]] = OMIT,
        inputs_units: typing.Optional[typing.Dict[str, typing.Optional[UnitStr]]] = OMIT,
        input_nodes: typing.Optional[typing.Sequence[str]] = OMIT,
        progress: typing.Optional[float] = OMIT,
        boot_options: typing.Optional[BootOptions] = OMIT,
        outputs: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        ui: typing.Optional[NodeUiPatch] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        key : typing.Optional[str]

        version : typing.Optional[str]

        label : typing.Optional[str]

        inputs : typing.Optional[InputsDictInput]

        inputs_required : typing.Optional[typing.Sequence[InputId]]

        inputs_units : typing.Optional[typing.Dict[str, typing.Optional[UnitStr]]]

        input_nodes : typing.Optional[typing.Sequence[str]]

        progress : typing.Optional[float]

        boot_options : typing.Optional[BootOptions]

        outputs : typing.Optional[typing.Dict[str, typing.Any]]

        ui : typing.Optional[NodeUiPatch]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.patch_project_node(
                project_id="project_id",
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_project_node(
            project_id,
            node_id,
            key=key,
            version=version,
            label=label,
            inputs=inputs,
            inputs_required=inputs_required,
            inputs_units=inputs_units,
            input_nodes=input_nodes,
            progress=progress,
            boot_options=boot_options,
            outputs=outputs,
            ui=ui,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_node(
        self,
        project_id: str,
        node_id: str,
        *,
        port_keys: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeNodeRetrieved:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        port_keys : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeNodeRetrieved
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.retrieve_node(
                project_id="project_id",
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_node(
            project_id, node_id, port_keys=port_keys, request_options=request_options
        )
        return _response.data

    async def start_node(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.start_node(
                project_id="project_id",
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_node(project_id, node_id, request_options=request_options)
        return _response.data

    async def stop_node(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeTaskGet:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTaskGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.stop_node(
                project_id="project_id",
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stop_node(project_id, node_id, request_options=request_options)
        return _response.data

    async def restart_node(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Note that it has only effect on nodes associated to dynamic services

        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.restart_node(
                project_id="project_id",
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.restart_node(project_id, node_id, request_options=request_options)
        return _response.data

    async def update_node_outputs(
        self,
        project_id: str,
        node_id: str,
        *,
        outputs: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        outputs : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.update_node_outputs(
                project_id="project_id",
                node_id="node_id",
                outputs={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_node_outputs(
            project_id, node_id, outputs=outputs, request_options=request_options
        )
        return _response.data

    async def get_node_resources(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeDictAnnotatedStrStringConstraintsImageResources:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeDictAnnotatedStrStringConstraintsImageResources
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.get_node_resources(
                project_id="project_id",
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_node_resources(project_id, node_id, request_options=request_options)
        return _response.data

    async def replace_node_resources(
        self,
        project_id: str,
        node_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeDictAnnotatedStrStringConstraintsImageResources:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeDictAnnotatedStrStringConstraintsImageResources
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.replace_node_resources(
                project_id="project_id",
                node_id="node_id",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_node_resources(
            project_id, node_id, request=request, request_options=request_options
        )
        return _response.data

    async def get_project_services(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeProjectNodeServicesGet:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectNodeServicesGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.get_project_services(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_services(project_id, request_options=request_options)
        return _response.data

    async def get_project_services_access_for_gid(
        self, project_id: str, *, for_gid: GroupIdInt, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeProjectGroupAccess:
        """
        Check whether provided group has access to the project services

        Parameters
        ----------
        project_id : str

        for_gid : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectGroupAccess
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.get_project_services_access_for_gid(
                project_id="project_id",
                for_gid=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_services_access_for_gid(
            project_id, for_gid=for_gid, request_options=request_options
        )
        return _response.data

    async def list_project_nodes_previews(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListProjectNodePreview:
        """
        Lists all previews in the node's project

        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListProjectNodePreview
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.list_project_nodes_previews(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_project_nodes_previews(project_id, request_options=request_options)
        return _response.data

    async def get_project_node_preview(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeProjectNodePreview:
        """
        Gets a give node's preview

        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectNodePreview
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.get_project_node_preview(
                project_id="project_id",
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_node_preview(
            project_id, node_id, request_options=request_options
        )
        return _response.data

    async def get_project_node_pricing_unit(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeUnionPricingUnitGetNoneType:
        """
        Get currently connected pricing unit to the project node.

        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeUnionPricingUnitGetNoneType
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.get_project_node_pricing_unit(
                project_id="project_id",
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_node_pricing_unit(
            project_id, node_id, request_options=request_options
        )
        return _response.data

    async def connect_pricing_unit_to_project_node(
        self,
        project_id: str,
        node_id: str,
        pricing_plan_id: int,
        pricing_unit_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Connect pricing unit to the project node (Project node can have only one pricing unit)

        Parameters
        ----------
        project_id : str

        node_id : str

        pricing_plan_id : int

        pricing_unit_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.connect_pricing_unit_to_project_node(
                project_id="project_id",
                node_id="node_id",
                pricing_plan_id=1,
                pricing_unit_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.connect_pricing_unit_to_project_node(
            project_id, node_id, pricing_plan_id, pricing_unit_id, request_options=request_options
        )
        return _response.data

    async def get_project_inputs(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeDictUuidProjectInputGet:
        """
        New in version *0.10*

        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeDictUuidProjectInputGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.get_project_inputs(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_inputs(project_id, request_options=request_options)
        return _response.data

    async def update_project_inputs(
        self,
        project_id: str,
        *,
        request: typing.Sequence[ProjectInputUpdate],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeDictUuidProjectInputGet:
        """
        New in version *0.10*

        Parameters
        ----------
        project_id : str

        request : typing.Sequence[ProjectInputUpdate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeDictUuidProjectInputGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.update_project_inputs(
                project_id="project_id",
                request=[],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_project_inputs(
            project_id, request=request, request_options=request_options
        )
        return _response.data

    async def get_project_outputs(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeDictUuidProjectOutputGet:
        """
        New in version *0.10*

        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeDictUuidProjectOutputGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.get_project_outputs(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_outputs(project_id, request_options=request_options)
        return _response.data

    async def list_project_metadata_ports(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListProjectMetadataPortGet:
        """
        New in version *0.12*

        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListProjectMetadataPortGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.list_project_metadata_ports(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_project_metadata_ports(project_id, request_options=request_options)
        return _response.data

    async def open_project(
        self,
        project_id: str,
        *,
        request: str,
        disable_service_auto_start: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeProjectGet:
        """
        Parameters
        ----------
        project_id : str

        request : str

        disable_service_auto_start : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.open_project(
                project_id="project_id",
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.open_project(
            project_id,
            request=request,
            disable_service_auto_start=disable_service_auto_start,
            request_options=request_options,
        )
        return _response.data

    async def close_project(
        self, project_id: str, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        project_id : str

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.close_project(
                project_id="project_id",
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.close_project(project_id, request=request, request_options=request_options)
        return _response.data

    async def get_project_state(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeProjectStateOutputSchema:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectStateOutputSchema
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.get_project_state(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_state(project_id, request_options=request_options)
        return _response.data

    async def add_project_tag(
        self, project_uuid: str, tag_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeProjectGet:
        """
        Links an existing label with an existing study

        NOTE: that the tag is not created here

        Parameters
        ----------
        project_uuid : str

        tag_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.add_project_tag(
                project_uuid="project_uuid",
                tag_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_project_tag(project_uuid, tag_id, request_options=request_options)
        return _response.data

    async def remove_project_tag(
        self, project_uuid: str, tag_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeProjectGet:
        """
        Removes an existing link between a label and a study

        NOTE: that the tag is not deleted here

        Parameters
        ----------
        project_uuid : str

        tag_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProjectGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.remove_project_tag(
                project_uuid="project_uuid",
                tag_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_project_tag(project_uuid, tag_id, request_options=request_options)
        return _response.data

    async def get_project_wallet(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeUnionWalletGetNoneType:
        """
        Get current connected wallet to the project.

        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeUnionWalletGetNoneType
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.get_project_wallet(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_wallet(project_id, request_options=request_options)
        return _response.data

    async def connect_wallet_to_project(
        self, project_id: str, wallet_id: WalletIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeWalletGet:
        """
        Connect wallet to the project (Project can have only one wallet)

        Parameters
        ----------
        project_id : str

        wallet_id : WalletIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWalletGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.connect_wallet_to_project(
                project_id="project_id",
                wallet_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.connect_wallet_to_project(
            project_id, wallet_id, request_options=request_options
        )
        return _response.data

    async def pay_project_debt(
        self,
        project_id: str,
        wallet_id: WalletIdInt,
        *,
        amount: PayProjectDebtRequestAmount,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        project_id : str

        wallet_id : WalletIdInt

        amount : PayProjectDebtRequestAmount

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.pay_project_debt(
                project_id="project_id",
                wallet_id=1,
                amount=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pay_project_debt(
            project_id, wallet_id, amount=amount, request_options=request_options
        )
        return _response.data

    async def move_project_to_workspace(
        self,
        project_id: str,
        workspace_id: typing.Optional[int],
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Move project to the workspace

        Parameters
        ----------
        project_id : str

        workspace_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.move_project_to_workspace(
                project_id="project_id",
                workspace_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.move_project_to_workspace(
            project_id, workspace_id, request_options=request_options
        )
        return _response.data
