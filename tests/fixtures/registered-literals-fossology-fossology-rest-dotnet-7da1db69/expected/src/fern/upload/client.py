

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.add_edit_delete_license_decision import AddEditDeleteLicenseDecision
from ..types.agent_of_upload import AgentOfUpload
from ..types.agents_revision import AgentsRevision
from ..types.clearing_progress_info import ClearingProgressInfo
from ..types.conf_response import ConfResponse
from ..types.edited_license import EditedLicense
from ..types.file import File
from ..types.fileinfo import Fileinfo
from ..types.get_bulk_history import GetBulkHistory
from ..types.get_clearing_history import GetClearingHistory
from ..types.get_prev_next_item import GetPrevNextItem
from ..types.get_reuse_report_summary import GetReuseReportSummary
from ..types.hash import Hash
from ..types.highlight_info import HighlightInfo
from ..types.info import Info
from ..types.license import License
from ..types.license_decision import LicenseDecision
from ..types.license_histogram import LicenseHistogram
from ..types.one_shot_info import OneShotInfo
from ..types.scan_options import ScanOptions
from ..types.scanned_license import ScannedLicense
from ..types.tree_view_model import TreeViewModel
from ..types.upload import Upload
from ..types.upload_copyrights import UploadCopyrights
from ..types.upload_licenses import UploadLicenses
from ..types.upload_perm_groups import UploadPermGroups
from ..types.upload_summary import UploadSummary
from .raw_client import AsyncRawUploadClient, RawUploadClient
from .types.add_edit_delete_license_decision_response import AddEditDeleteLicenseDecisionResponse
from .types.create_upload_request_location import CreateUploadRequestLocation
from .types.get_item_tree_view_request_sort import GetItemTreeViewRequestSort
from .types.get_licenses_by_upload_id_request_agent_item import GetLicensesByUploadIdRequestAgentItem
from .types.get_previous_and_next_item_request_selection import GetPreviousAndNextItemRequestSelection
from .types.get_uploads_request_status import GetUploadsRequestStatus
from .types.move_upload_by_id_request_action import MoveUploadByIdRequestAction
from .types.schedule_bulk_scan_bulk_actions_item import ScheduleBulkScanBulkActionsItem
from .types.schedule_bulk_scan_bulk_scope import ScheduleBulkScanBulkScope
from .types.set_upload_permissions_request_new_permission import SetUploadPermissionsRequestNewPermission
from .types.set_upload_permissions_request_public_permission import SetUploadPermissionsRequestPublicPermission
from .types.update_upload_by_id_request_status import UpdateUploadByIdRequestStatus


OMIT = typing.cast(typing.Any, ...)


class UploadClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUploadClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUploadClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUploadClient
        """
        return self._raw_client

    def get_upload_by_id(
        self,
        id: int,
        *,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Upload:
        """
        Returns a single upload

        Parameters
        ----------
        id : int
            Id of the upload

        group_name : typing.Optional[str]
            The group name to chose while accessing the package

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Upload
            Get upload

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.get_upload_by_id(
            id=1,
        )
        """
        _response = self._raw_client.get_upload_by_id(id, group_name=group_name, request_options=request_options)
        return _response.data

    def move_upload_by_id(
        self,
        id: int,
        *,
        folder_id: int,
        action: MoveUploadByIdRequestAction,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Copy or move an upload by id

        Parameters
        ----------
        id : int
            Id of the upload

        folder_id : int
            Folder Id, where upload should be copied to

        action : MoveUploadByIdRequestAction
            Action to be performed

        group_name : typing.Optional[str]
            The group name to chose while accessing the package

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Upload will be copied/moved

        Examples
        --------
        from fern.upload import MoveUploadByIdRequestAction

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.move_upload_by_id(
            id=1,
            folder_id=1,
            action=MoveUploadByIdRequestAction.COPY,
        )
        """
        _response = self._raw_client.move_upload_by_id(
            id, folder_id=folder_id, action=action, group_name=group_name, request_options=request_options
        )
        return _response.data

    def delete_upload_by_id(
        self,
        id: int,
        *,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Delete a single upload by id

        Parameters
        ----------
        id : int
            Id of the upload

        group_name : typing.Optional[str]
            The group name to chose while accessing the package

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Upload will be deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.delete_upload_by_id(
            id=1,
        )
        """
        _response = self._raw_client.delete_upload_by_id(id, group_name=group_name, request_options=request_options)
        return _response.data

    def update_upload_by_id(
        self,
        id: int,
        *,
        status: typing.Optional[UpdateUploadByIdRequestStatus] = None,
        assignee: typing.Optional[int] = None,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Update an upload information

        Parameters
        ----------
        id : int
            Id of the upload

        status : typing.Optional[UpdateUploadByIdRequestStatus]
            New status of the upload

        assignee : typing.Optional[int]
            New assignee for the project

        group_name : typing.Optional[str]
            The group name to chose while accessing the package

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Upload will be updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.update_upload_by_id(
            id=1,
        )
        """
        _response = self._raw_client.update_upload_by_id(
            id, status=status, assignee=assignee, group_name=group_name, request_options=request_options
        )
        return _response.data

    def get_uploads(
        self,
        *,
        folder_id: typing.Optional[int] = None,
        recursive: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        status: typing.Optional[GetUploadsRequestStatus] = None,
        assignee: typing.Optional[str] = None,
        since: typing.Optional[str] = None,
        group_name: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Upload]:
        """
        The uploads endpoint returns all uploads

        Parameters
        ----------
        folder_id : typing.Optional[int]
            Folder ID to limit the uploads to

        recursive : typing.Optional[bool]
            Load uploads from child folders as well

        name : typing.Optional[str]
            Filter pattern for name and description

        status : typing.Optional[GetUploadsRequestStatus]
            Status of uploads

        assignee : typing.Optional[str]
            User name to which uploads are assigned to or -me- or -unassigned-

        since : typing.Optional[str]
            Uploads since given date in YYYY-MM-DD format

        group_name : typing.Optional[str]
            The group name to chose while accessing the package

        page : typing.Optional[int]
            Page number to fetch

        limit : typing.Optional[int]
            Limits of responses per request

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Upload]
            An array of uploads

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.get_uploads()
        """
        _response = self._raw_client.get_uploads(
            folder_id=folder_id,
            recursive=recursive,
            name=name,
            status=status,
            assignee=assignee,
            since=since,
            group_name=group_name,
            page=page,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    def create_upload(
        self,
        *,
        folder_id: int,
        group_name: typing.Optional[str] = None,
        upload_description: typing.Optional[str] = None,
        apply_global: typing.Optional[bool] = None,
        ignore_scm: typing.Optional[bool] = None,
        location: typing.Optional[CreateUploadRequestLocation] = OMIT,
        scan_options: typing.Optional[ScanOptions] = OMIT,
        main_license: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Endpoint to create a new upload in FOSSology

        Parameters
        ----------
        folder_id : int
            Folder Id, where upload should be created

        group_name : typing.Optional[str]
            The group name to chose while accessing the package

        upload_description : typing.Optional[str]
            Visible description of the file

        apply_global : typing.Optional[bool]
            Apply global decisions for current upload

        ignore_scm : typing.Optional[bool]
            Ignore SCM files (Git, SVN, TFS) and files with particular Mimetype

        location : typing.Optional[CreateUploadRequestLocation]

        scan_options : typing.Optional[ScanOptions]

        main_license : typing.Optional[str]
            Main license shortname for the upload.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Upload is created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.create_upload(
            folder_id=1,
        )
        """
        _response = self._raw_client.create_upload(
            folder_id=folder_id,
            group_name=group_name,
            upload_description=upload_description,
            apply_global=apply_global,
            ignore_scm=ignore_scm,
            location=location,
            scan_options=scan_options,
            main_license=main_license,
            request_options=request_options,
        )
        return _response.data

    def get_upload_file_by_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Get a file by upload id

        Parameters
        ----------
        id : int
            Download file using Upload ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Required report

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.get_upload_file_by_id(
            id=1,
        )
        """
        with self._raw_client.get_upload_file_by_id(id, request_options=request_options) as r:
            yield from r.data

    def get_summary_by_upload_id(
        self,
        id: int,
        *,
        agent_id: typing.Optional[int] = None,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadSummary:
        """
        Returns summary for single upload

        Parameters
        ----------
        id : int
            Id of the upload

        agent_id : typing.Optional[int]
            Id of the agent

        group_name : typing.Optional[str]
            The group name to chose while accessing the package

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadSummary
            Get summary

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.get_summary_by_upload_id(
            id=1,
        )
        """
        _response = self._raw_client.get_summary_by_upload_id(
            id, agent_id=agent_id, group_name=group_name, request_options=request_options
        )
        return _response.data

    def get_item_info(
        self, id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Fileinfo:
        """
        Returns info for single file

        Parameters
        ----------
        id : int
            Id of the upload

        item_id : int
            Upload tree Id of the file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Fileinfo
            Get info

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.get_item_info(
            id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.get_item_info(id, item_id, request_options=request_options)
        return _response.data

    def get_licenses_by_upload_id(
        self,
        id: int,
        *,
        agent: typing.Optional[
            typing.Union[GetLicensesByUploadIdRequestAgentItem, typing.Sequence[GetLicensesByUploadIdRequestAgentItem]]
        ] = None,
        containers: typing.Optional[bool] = None,
        license: typing.Optional[bool] = None,
        copyright: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadLicenses:
        """
        Returns the list of licenses found by requested agent

        Parameters
        ----------
        id : int
            Id of the upload

        agent : typing.Optional[typing.Union[GetLicensesByUploadIdRequestAgentItem, typing.Sequence[GetLicensesByUploadIdRequestAgentItem]]]
            Name of the agent

        containers : typing.Optional[bool]
            Show directories and containers

        license : typing.Optional[bool]
            Show license in response

        copyright : typing.Optional[bool]
            Show copyrights in response

        page : typing.Optional[int]
            Page number (starts from 1)

        limit : typing.Optional[int]
            Limits of responses per request

        group_name : typing.Optional[str]
            The group name to chose while accessing the package

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadLicenses
            Get licenses

        Examples
        --------
        from fern.upload import GetLicensesByUploadIdRequestAgentItem

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.get_licenses_by_upload_id(
            id=1,
            agent=[GetLicensesByUploadIdRequestAgentItem.NOMOS],
        )
        """
        _response = self._raw_client.get_licenses_by_upload_id(
            id,
            agent=agent,
            containers=containers,
            license=license,
            copyright=copyright,
            page=page,
            limit=limit,
            group_name=group_name,
            request_options=request_options,
        )
        return _response.data

    def get_copyrights_by_upload_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UploadCopyrights:
        """
        Returns the list of copyrights found on the requested upload.

        Parameters
        ----------
        id : int
            Id of the upload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadCopyrights
            Get copyrights

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.get_copyrights_by_upload_id(
            id=1,
        )
        """
        _response = self._raw_client.get_copyrights_by_upload_id(id, request_options=request_options)
        return _response.data

    def set_upload_permissions(
        self,
        id: int,
        *,
        all_uploads_permission: bool,
        folder_id: typing.Optional[int] = OMIT,
        group_id: typing.Optional[int] = OMIT,
        new_permission: typing.Optional[SetUploadPermissionsRequestNewPermission] = OMIT,
        public_permission: typing.Optional[SetUploadPermissionsRequestPublicPermission] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Info]:
        """
        Set permissions for a upload in a folder for different groups

        Parameters
        ----------
        id : int
            Enter any upload id

        all_uploads_permission : bool
            Apply same permissions to all uploads in this folder

        folder_id : typing.Optional[int]
            Enter a folder id

        group_id : typing.Optional[int]
            Enter the id of the group you want to add or edit permission for this upload

        new_permission : typing.Optional[SetUploadPermissionsRequestNewPermission]
            Select the permission for selected group

        public_permission : typing.Optional[SetUploadPermissionsRequestPublicPermission]
            Select the public permission for this upload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Info]
            Permissions updated successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.set_upload_permissions(
            id=1,
            all_uploads_permission=True,
        )
        """
        _response = self._raw_client.set_upload_permissions(
            id,
            all_uploads_permission=all_uploads_permission,
            folder_id=folder_id,
            group_id=group_id,
            new_permission=new_permission,
            public_permission=public_permission,
            request_options=request_options,
        )
        return _response.data

    def get_groups_with_permissions(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UploadPermGroups:
        """
        Returns the list of all the groups with their respective permissions for a upload

        Parameters
        ----------
        id : int
            Id of the upload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadPermGroups
            Get Groups with permissions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.get_groups_with_permissions(
            id=1,
        )
        """
        _response = self._raw_client.get_groups_with_permissions(id, request_options=request_options)
        return _response.data

    def get_highlight_entries(
        self,
        id: int,
        item_id: int,
        *,
        clearing_id: typing.Optional[int] = None,
        license_id: typing.Optional[int] = None,
        highlight_id: typing.Optional[int] = None,
        agent_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[HighlightInfo]:
        """
        Get highlight entries of the content for the given upload and item id.

        Parameters
        ----------
        id : int
            Id of the upload

        item_id : int
            Id of the item

        clearing_id : typing.Optional[int]
            Id of the clearing event

        license_id : typing.Optional[int]
            Id of the license

        highlight_id : typing.Optional[int]
            Id of the highlight

        agent_id : typing.Optional[int]
            Id of the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[HighlightInfo]
            List of the data about highlight entries

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.get_highlight_entries(
            id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.get_highlight_entries(
            id,
            item_id,
            clearing_id=clearing_id,
            license_id=license_id,
            highlight_id=highlight_id,
            agent_id=agent_id,
            request_options=request_options,
        )
        return _response.data

    def view_the_content_of_the_file(
        self, id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Returns the contents of a specific file

        Parameters
        ----------
        id : int
            Id of the upload

        item_id : int
            Id of the item

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Get contents

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.view_the_content_of_the_file(
            id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.view_the_content_of_the_file(id, item_id, request_options=request_options)
        return _response.data

    def set_clearing_decision(
        self,
        id: int,
        item_id: int,
        *,
        decision_type: typing.Optional[int] = OMIT,
        global_decision: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Set the clearing decision for a particular upload tree item.

        Parameters
        ----------
        id : int
            Id of the upload

        item_id : int
            Id of the itemId

        decision_type : typing.Optional[int]
            Type of decision.
            0: WIP
            3: To be discussed
            4: Irrelevant
            5: Identified
            6: Do not use
            7: Non functional

        global_decision : typing.Optional[bool]
            Is the decision global?
            If true, the decision is applied to all occurrence of the file on the server!

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Clearing decision set successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.set_clearing_decision(
            id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.set_clearing_decision(
            id, item_id, decision_type=decision_type, global_decision=global_decision, request_options=request_options
        )
        return _response.data

    def schedule_bulk_scan(
        self,
        id: int,
        item_id: int,
        *,
        bulk_actions: typing.Optional[typing.Sequence[ScheduleBulkScanBulkActionsItem]] = OMIT,
        ref_text: typing.Optional[str] = OMIT,
        bulk_scope: typing.Optional[ScheduleBulkScanBulkScope] = OMIT,
        force_decision: typing.Optional[bool] = OMIT,
        ignore_irre: typing.Optional[bool] = OMIT,
        delimiters: typing.Optional[str] = OMIT,
        scan_only_findings: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Schedule the bulk scan for the item

        Parameters
        ----------
        id : int
            Id of the upload

        item_id : int
            Id of the itemId

        bulk_actions : typing.Optional[typing.Sequence[ScheduleBulkScanBulkActionsItem]]

        ref_text : typing.Optional[str]

        bulk_scope : typing.Optional[ScheduleBulkScanBulkScope]

        force_decision : typing.Optional[bool]

        ignore_irre : typing.Optional[bool]

        delimiters : typing.Optional[str]

        scan_only_findings : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Bulk scan scheduled successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.schedule_bulk_scan(
            id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.schedule_bulk_scan(
            id,
            item_id,
            bulk_actions=bulk_actions,
            ref_text=ref_text,
            bulk_scope=bulk_scope,
            force_decision=force_decision,
            ignore_irre=ignore_irre,
            delimiters=delimiters,
            scan_only_findings=scan_only_findings,
            request_options=request_options,
        )
        return _response.data

    def get_bulk_history(
        self, id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetBulkHistory]:
        """
        Get the bulk history for a specific upload item

        Parameters
        ----------
        id : int
            Id of the upload

        item_id : int
            Id of the itemId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetBulkHistory]
            List of the data about the bulk history

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.get_bulk_history(
            id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.get_bulk_history(id, item_id, request_options=request_options)
        return _response.data

    def get_license_decisions(
        self, id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[LicenseDecision]:
        """
        Get the license decisions list for the given upload and item id

        Parameters
        ----------
        id : int
            Id of the upload

        item_id : int
            Id of the itemId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LicenseDecision]
            List of the license decisions for the upload-tree id

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.get_license_decisions(
            id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.get_license_decisions(id, item_id, request_options=request_options)
        return _response.data

    def add_edit_delete_license_decision(
        self,
        id: int,
        item_id: int,
        *,
        request: typing.Sequence[AddEditDeleteLicenseDecision],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AddEditDeleteLicenseDecisionResponse:
        """
        Add, update or delete a license decision for a particular upload tree item.

        Parameters
        ----------
        id : int
            Id of the upload

        item_id : int
            Id of the itemId

        request : typing.Sequence[AddEditDeleteLicenseDecision]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddEditDeleteLicenseDecisionResponse
            Request processed successfully

        Examples
        --------
        from fern import AddEditDeleteLicenseDecision, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.add_edit_delete_license_decision(
            id=1,
            item_id=1,
            request=[AddEditDeleteLicenseDecision()],
        )
        """
        _response = self._raw_client.add_edit_delete_license_decision(
            id, item_id, request=request, request_options=request_options
        )
        return _response.data

    def get_main_licenses(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[License]:
        """
        Get main licenses assigned on a particular upload

        Parameters
        ----------
        id : int
            Id of the upload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[License]
            All main licenses from an upload

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.get_main_licenses(
            id=1,
        )
        """
        _response = self._raw_client.get_main_licenses(id, request_options=request_options)
        return _response.data

    def set_main_license(
        self,
        id: int,
        *,
        short_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Set the main license for a particular upload.

        Parameters
        ----------
        id : int
            Id of the upload

        short_name : typing.Optional[str]
            short name of the license

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Main license set successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.set_main_license(
            id=1,
        )
        """
        _response = self._raw_client.set_main_license(id, short_name=short_name, request_options=request_options)
        return _response.data

    def delete_main_license(
        self, id: int, short_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
        """
        Delete a main license from an upload.

        Parameters
        ----------
        id : int
            Id of the upload

        short_name : str
            shortName of the main license to be deleted

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            License is removed successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.delete_main_license(
            id=1,
            short_name="shortName",
        )
        """
        _response = self._raw_client.delete_main_license(id, short_name, request_options=request_options)
        return _response.data

    def get_previous_and_next_item(
        self,
        id: int,
        item_id: int,
        *,
        selection: typing.Optional[GetPreviousAndNextItemRequestSelection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPrevNextItem:
        """
        Get the index of the previous and the next time for an upload

        Parameters
        ----------
        id : int
            Id of the upload

        item_id : int
            Id of the itemId

        selection : typing.Optional[GetPreviousAndNextItemRequestSelection]
            Return jobs for the given upload id only

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPrevNextItem
            List of the data about clearing history

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.get_previous_and_next_item(
            id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.get_previous_and_next_item(
            id, item_id, selection=selection, request_options=request_options
        )
        return _response.data

    def get_clearing_history(
        self, id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetClearingHistory:
        """
        Get the clearing history for a specific upload item

        Parameters
        ----------
        id : int
            Id of the upload

        item_id : int
            Id of the itemId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetClearingHistory
            List of the data about clearing history

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.get_clearing_history(
            id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.get_clearing_history(id, item_id, request_options=request_options)
        return _response.data

    def get_clearing_progress_info(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ClearingProgressInfo:
        """
        Get the clearing progress information for an upload

        Parameters
        ----------
        id : int
            Id of the upload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClearingProgressInfo
            Get clearing progress info

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.get_clearing_progress_info(
            id=1,
        )
        """
        _response = self._raw_client.get_clearing_progress_info(id, request_options=request_options)
        return _response.data

    def get_licenses_histogram(
        self, id: int, *, agent_id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[LicenseHistogram]:
        """
        Get the licenses histogram for a specific upload

        Parameters
        ----------
        id : int
            Id of the upload

        agent_id : typing.Optional[int]
            Id of the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LicenseHistogram]
            Get the licenses histogram for the upload

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.get_licenses_histogram(
            id=1,
        )
        """
        _response = self._raw_client.get_licenses_histogram(id, agent_id=agent_id, request_options=request_options)
        return _response.data

    def get_agents_by_upload_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AgentOfUpload]:
        """
        Returns the list of agents for a upload.

        Parameters
        ----------
        id : int
            Id of the upload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AgentOfUpload]
            Get agents

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.get_agents_by_upload_id(
            id=1,
        )
        """
        _response = self._raw_client.get_agents_by_upload_id(id, request_options=request_options)
        return _response.data

    def get_all_edited_licenses(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[EditedLicense]:
        """
        Get the edited licenses list for a specific upload

        Parameters
        ----------
        id : int
            Id of the upload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EditedLicense]
            List of the edited licenses in the upload

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.get_all_edited_licenses(
            id=1,
        )
        """
        _response = self._raw_client.get_all_edited_licenses(id, request_options=request_options)
        return _response.data

    def get_all_scanned_licenses(
        self, id: int, *, agent_id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ScannedLicense]:
        """
        Get the scanned licenses list for a specific upload

        Parameters
        ----------
        id : int
            Id of the upload

        agent_id : typing.Optional[int]
            Id of the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ScannedLicense]
            List of the scanned licenses in the upload

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.get_all_scanned_licenses(
            id=1,
        )
        """
        _response = self._raw_client.get_all_scanned_licenses(id, agent_id=agent_id, request_options=request_options)
        return _response.data

    def get_item_tree_view(
        self,
        id: int,
        item_id: int,
        *,
        agent_id: typing.Optional[int] = None,
        tag_id: typing.Optional[int] = None,
        scan_license_filter: typing.Optional[int] = None,
        edited_license_filter: typing.Optional[int] = None,
        flatten: typing.Optional[bool] = None,
        sort: typing.Optional[GetItemTreeViewRequestSort] = None,
        search: typing.Optional[str] = None,
        show_quick: typing.Optional[bool] = None,
        filter_open: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[TreeViewModel]:
        """
        Get the tree view for the given upload and item id

        Parameters
        ----------
        id : int
            Id of the upload

        item_id : int
            Id of the itemId

        agent_id : typing.Optional[int]
            Id of the agent

        tag_id : typing.Optional[int]
            Id of the tag

        scan_license_filter : typing.Optional[int]
            ShortName of the selected scan license filter

        edited_license_filter : typing.Optional[int]
            ShortName of the selected edited license filter

        flatten : typing.Optional[bool]
            Flatten the tree

        sort : typing.Optional[GetItemTreeViewRequestSort]
            Sort the tree

        search : typing.Optional[str]
            Filter the list according to the search string

        show_quick : typing.Optional[bool]
            Show all the items of the current container

        filter_open : typing.Optional[bool]
            openCBox Filter is checked

        page : typing.Optional[int]
            Page number (starts from 1)

        limit : typing.Optional[int]
            Limits of responses per request

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TreeViewModel]
            Tree view for the given upload and item id

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.get_item_tree_view(
            id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.get_item_tree_view(
            id,
            item_id,
            agent_id=agent_id,
            tag_id=tag_id,
            scan_license_filter=scan_license_filter,
            edited_license_filter=edited_license_filter,
            flatten=flatten,
            sort=sort,
            search=search,
            show_quick=show_quick,
            filter_open=filter_open,
            page=page,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    def get_top_item_id(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Info]:
        """
        Get the item id for the top level item in a given upload.

        Parameters
        ----------
        id : int
            Id of the upload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Info]
            Top item id

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.get_top_item_id(
            id=1,
        )
        """
        _response = self._raw_client.get_top_item_id(id, request_options=request_options)
        return _response.data

    def get_licenses_reuse_summary(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetReuseReportSummary:
        """
        Get the overall licenses reuse summary for an upload

        Parameters
        ----------
        id : int
            Id of the upload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetReuseReportSummary
            Get licenses reuse summary

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.get_licenses_reuse_summary(
            id=1,
        )
        """
        _response = self._raw_client.get_licenses_reuse_summary(id, request_options=request_options)
        return _response.data

    def get_revisions_for_agents(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AgentsRevision]:
        """
        Returns the list of revisions for the successful agents for the upload

        Parameters
        ----------
        id : int
            Id of the upload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AgentsRevision]
            Get successful agents with revisions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.get_revisions_for_agents(
            id=1,
        )
        """
        _response = self._raw_client.get_revisions_for_agents(id, request_options=request_options)
        return _response.data

    def run_one_shot_nomos(
        self, *, file_input: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> OneShotInfo:
        """
        Run one-shot nomos analysis on the upload without storing the results.

        Parameters
        ----------
        file_input : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OneShotInfo
            Scanner result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.run_one_shot_nomos()
        """
        _response = self._raw_client.run_one_shot_nomos(file_input=file_input, request_options=request_options)
        return _response.data

    def run_one_shot_monk(
        self, *, file_input: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> OneShotInfo:
        """
        Run one-shot monk analysis on the upload without storing the results.

        Parameters
        ----------
        file_input : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OneShotInfo
            Scanner result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.run_one_shot_monk()
        """
        _response = self._raw_client.run_one_shot_monk(file_input=file_input, request_options=request_options)
        return _response.data

    def run_one_shot_ceu(
        self, *, file_input: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> OneShotInfo:
        """
        Run one-shot Copyright/Email/URL analysis on the upload without storing the results.

        Parameters
        ----------
        file_input : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OneShotInfo
            Scanner result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.run_one_shot_ceu()
        """
        _response = self._raw_client.run_one_shot_ceu(file_input=file_input, request_options=request_options)
        return _response.data

    def get_files(
        self,
        *,
        request: typing.Sequence[Hash],
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[File]:
        """
        Get a list of files by hashes

        Parameters
        ----------
        request : typing.Sequence[Hash]

        group_name : typing.Optional[str]
            The group name to chose while downloading specific report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[File]
            List of matching files

        Examples
        --------
        from fern import FernApi, Hash

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.get_files(
            request=[Hash()],
        )
        """
        _response = self._raw_client.get_files(request=request, group_name=group_name, request_options=request_options)
        return _response.data

    def get_conf_info(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ConfResponse]:
        """
        Get conf information

        Parameters
        ----------
        id : int
            Upload Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ConfResponse]
            current conf information

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.get_conf_info(
            id=1,
        )
        """
        _response = self._raw_client.get_conf_info(id, request_options=request_options)
        return _response.data

    def update_conf_data(
        self,
        id: int,
        *,
        key: typing.Optional[str] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Info]:
        """
        Updates the conf page data from the server

        Parameters
        ----------
        id : int
            Upload Id

        key : typing.Optional[str]
            Key of the field to be updated

        value : typing.Optional[str]
            Value of the field to be updated. If value is a JSON, it should be
            sent as an encoded string.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Info]
            Config data

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.upload.update_conf_data(
            id=1,
        )
        """
        _response = self._raw_client.update_conf_data(id, key=key, value=value, request_options=request_options)
        return _response.data


class AsyncUploadClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUploadClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUploadClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUploadClient
        """
        return self._raw_client

    async def get_upload_by_id(
        self,
        id: int,
        *,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Upload:
        """
        Returns a single upload

        Parameters
        ----------
        id : int
            Id of the upload

        group_name : typing.Optional[str]
            The group name to chose while accessing the package

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Upload
            Get upload

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.get_upload_by_id(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_upload_by_id(id, group_name=group_name, request_options=request_options)
        return _response.data

    async def move_upload_by_id(
        self,
        id: int,
        *,
        folder_id: int,
        action: MoveUploadByIdRequestAction,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Copy or move an upload by id

        Parameters
        ----------
        id : int
            Id of the upload

        folder_id : int
            Folder Id, where upload should be copied to

        action : MoveUploadByIdRequestAction
            Action to be performed

        group_name : typing.Optional[str]
            The group name to chose while accessing the package

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Upload will be copied/moved

        Examples
        --------
        import asyncio

        from fern.upload import MoveUploadByIdRequestAction

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.move_upload_by_id(
                id=1,
                folder_id=1,
                action=MoveUploadByIdRequestAction.COPY,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.move_upload_by_id(
            id, folder_id=folder_id, action=action, group_name=group_name, request_options=request_options
        )
        return _response.data

    async def delete_upload_by_id(
        self,
        id: int,
        *,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Delete a single upload by id

        Parameters
        ----------
        id : int
            Id of the upload

        group_name : typing.Optional[str]
            The group name to chose while accessing the package

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Upload will be deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.delete_upload_by_id(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_upload_by_id(
            id, group_name=group_name, request_options=request_options
        )
        return _response.data

    async def update_upload_by_id(
        self,
        id: int,
        *,
        status: typing.Optional[UpdateUploadByIdRequestStatus] = None,
        assignee: typing.Optional[int] = None,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Update an upload information

        Parameters
        ----------
        id : int
            Id of the upload

        status : typing.Optional[UpdateUploadByIdRequestStatus]
            New status of the upload

        assignee : typing.Optional[int]
            New assignee for the project

        group_name : typing.Optional[str]
            The group name to chose while accessing the package

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Upload will be updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.update_upload_by_id(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_upload_by_id(
            id, status=status, assignee=assignee, group_name=group_name, request_options=request_options
        )
        return _response.data

    async def get_uploads(
        self,
        *,
        folder_id: typing.Optional[int] = None,
        recursive: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        status: typing.Optional[GetUploadsRequestStatus] = None,
        assignee: typing.Optional[str] = None,
        since: typing.Optional[str] = None,
        group_name: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Upload]:
        """
        The uploads endpoint returns all uploads

        Parameters
        ----------
        folder_id : typing.Optional[int]
            Folder ID to limit the uploads to

        recursive : typing.Optional[bool]
            Load uploads from child folders as well

        name : typing.Optional[str]
            Filter pattern for name and description

        status : typing.Optional[GetUploadsRequestStatus]
            Status of uploads

        assignee : typing.Optional[str]
            User name to which uploads are assigned to or -me- or -unassigned-

        since : typing.Optional[str]
            Uploads since given date in YYYY-MM-DD format

        group_name : typing.Optional[str]
            The group name to chose while accessing the package

        page : typing.Optional[int]
            Page number to fetch

        limit : typing.Optional[int]
            Limits of responses per request

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Upload]
            An array of uploads

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.get_uploads()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_uploads(
            folder_id=folder_id,
            recursive=recursive,
            name=name,
            status=status,
            assignee=assignee,
            since=since,
            group_name=group_name,
            page=page,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    async def create_upload(
        self,
        *,
        folder_id: int,
        group_name: typing.Optional[str] = None,
        upload_description: typing.Optional[str] = None,
        apply_global: typing.Optional[bool] = None,
        ignore_scm: typing.Optional[bool] = None,
        location: typing.Optional[CreateUploadRequestLocation] = OMIT,
        scan_options: typing.Optional[ScanOptions] = OMIT,
        main_license: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Endpoint to create a new upload in FOSSology

        Parameters
        ----------
        folder_id : int
            Folder Id, where upload should be created

        group_name : typing.Optional[str]
            The group name to chose while accessing the package

        upload_description : typing.Optional[str]
            Visible description of the file

        apply_global : typing.Optional[bool]
            Apply global decisions for current upload

        ignore_scm : typing.Optional[bool]
            Ignore SCM files (Git, SVN, TFS) and files with particular Mimetype

        location : typing.Optional[CreateUploadRequestLocation]

        scan_options : typing.Optional[ScanOptions]

        main_license : typing.Optional[str]
            Main license shortname for the upload.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Upload is created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.create_upload(
                folder_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_upload(
            folder_id=folder_id,
            group_name=group_name,
            upload_description=upload_description,
            apply_global=apply_global,
            ignore_scm=ignore_scm,
            location=location,
            scan_options=scan_options,
            main_license=main_license,
            request_options=request_options,
        )
        return _response.data

    async def get_upload_file_by_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Get a file by upload id

        Parameters
        ----------
        id : int
            Download file using Upload ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Required report

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.get_upload_file_by_id(
                id=1,
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_upload_file_by_id(id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_summary_by_upload_id(
        self,
        id: int,
        *,
        agent_id: typing.Optional[int] = None,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadSummary:
        """
        Returns summary for single upload

        Parameters
        ----------
        id : int
            Id of the upload

        agent_id : typing.Optional[int]
            Id of the agent

        group_name : typing.Optional[str]
            The group name to chose while accessing the package

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadSummary
            Get summary

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.get_summary_by_upload_id(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_summary_by_upload_id(
            id, agent_id=agent_id, group_name=group_name, request_options=request_options
        )
        return _response.data

    async def get_item_info(
        self, id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Fileinfo:
        """
        Returns info for single file

        Parameters
        ----------
        id : int
            Id of the upload

        item_id : int
            Upload tree Id of the file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Fileinfo
            Get info

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.get_item_info(
                id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_item_info(id, item_id, request_options=request_options)
        return _response.data

    async def get_licenses_by_upload_id(
        self,
        id: int,
        *,
        agent: typing.Optional[
            typing.Union[GetLicensesByUploadIdRequestAgentItem, typing.Sequence[GetLicensesByUploadIdRequestAgentItem]]
        ] = None,
        containers: typing.Optional[bool] = None,
        license: typing.Optional[bool] = None,
        copyright: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadLicenses:
        """
        Returns the list of licenses found by requested agent

        Parameters
        ----------
        id : int
            Id of the upload

        agent : typing.Optional[typing.Union[GetLicensesByUploadIdRequestAgentItem, typing.Sequence[GetLicensesByUploadIdRequestAgentItem]]]
            Name of the agent

        containers : typing.Optional[bool]
            Show directories and containers

        license : typing.Optional[bool]
            Show license in response

        copyright : typing.Optional[bool]
            Show copyrights in response

        page : typing.Optional[int]
            Page number (starts from 1)

        limit : typing.Optional[int]
            Limits of responses per request

        group_name : typing.Optional[str]
            The group name to chose while accessing the package

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadLicenses
            Get licenses

        Examples
        --------
        import asyncio

        from fern.upload import GetLicensesByUploadIdRequestAgentItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.get_licenses_by_upload_id(
                id=1,
                agent=[GetLicensesByUploadIdRequestAgentItem.NOMOS],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_licenses_by_upload_id(
            id,
            agent=agent,
            containers=containers,
            license=license,
            copyright=copyright,
            page=page,
            limit=limit,
            group_name=group_name,
            request_options=request_options,
        )
        return _response.data

    async def get_copyrights_by_upload_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UploadCopyrights:
        """
        Returns the list of copyrights found on the requested upload.

        Parameters
        ----------
        id : int
            Id of the upload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadCopyrights
            Get copyrights

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.get_copyrights_by_upload_id(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_copyrights_by_upload_id(id, request_options=request_options)
        return _response.data

    async def set_upload_permissions(
        self,
        id: int,
        *,
        all_uploads_permission: bool,
        folder_id: typing.Optional[int] = OMIT,
        group_id: typing.Optional[int] = OMIT,
        new_permission: typing.Optional[SetUploadPermissionsRequestNewPermission] = OMIT,
        public_permission: typing.Optional[SetUploadPermissionsRequestPublicPermission] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Info]:
        """
        Set permissions for a upload in a folder for different groups

        Parameters
        ----------
        id : int
            Enter any upload id

        all_uploads_permission : bool
            Apply same permissions to all uploads in this folder

        folder_id : typing.Optional[int]
            Enter a folder id

        group_id : typing.Optional[int]
            Enter the id of the group you want to add or edit permission for this upload

        new_permission : typing.Optional[SetUploadPermissionsRequestNewPermission]
            Select the permission for selected group

        public_permission : typing.Optional[SetUploadPermissionsRequestPublicPermission]
            Select the public permission for this upload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Info]
            Permissions updated successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.set_upload_permissions(
                id=1,
                all_uploads_permission=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_upload_permissions(
            id,
            all_uploads_permission=all_uploads_permission,
            folder_id=folder_id,
            group_id=group_id,
            new_permission=new_permission,
            public_permission=public_permission,
            request_options=request_options,
        )
        return _response.data

    async def get_groups_with_permissions(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UploadPermGroups:
        """
        Returns the list of all the groups with their respective permissions for a upload

        Parameters
        ----------
        id : int
            Id of the upload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadPermGroups
            Get Groups with permissions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.get_groups_with_permissions(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_groups_with_permissions(id, request_options=request_options)
        return _response.data

    async def get_highlight_entries(
        self,
        id: int,
        item_id: int,
        *,
        clearing_id: typing.Optional[int] = None,
        license_id: typing.Optional[int] = None,
        highlight_id: typing.Optional[int] = None,
        agent_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[HighlightInfo]:
        """
        Get highlight entries of the content for the given upload and item id.

        Parameters
        ----------
        id : int
            Id of the upload

        item_id : int
            Id of the item

        clearing_id : typing.Optional[int]
            Id of the clearing event

        license_id : typing.Optional[int]
            Id of the license

        highlight_id : typing.Optional[int]
            Id of the highlight

        agent_id : typing.Optional[int]
            Id of the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[HighlightInfo]
            List of the data about highlight entries

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.get_highlight_entries(
                id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_highlight_entries(
            id,
            item_id,
            clearing_id=clearing_id,
            license_id=license_id,
            highlight_id=highlight_id,
            agent_id=agent_id,
            request_options=request_options,
        )
        return _response.data

    async def view_the_content_of_the_file(
        self, id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Returns the contents of a specific file

        Parameters
        ----------
        id : int
            Id of the upload

        item_id : int
            Id of the item

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Get contents

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.view_the_content_of_the_file(
                id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.view_the_content_of_the_file(id, item_id, request_options=request_options)
        return _response.data

    async def set_clearing_decision(
        self,
        id: int,
        item_id: int,
        *,
        decision_type: typing.Optional[int] = OMIT,
        global_decision: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Set the clearing decision for a particular upload tree item.

        Parameters
        ----------
        id : int
            Id of the upload

        item_id : int
            Id of the itemId

        decision_type : typing.Optional[int]
            Type of decision.
            0: WIP
            3: To be discussed
            4: Irrelevant
            5: Identified
            6: Do not use
            7: Non functional

        global_decision : typing.Optional[bool]
            Is the decision global?
            If true, the decision is applied to all occurrence of the file on the server!

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Clearing decision set successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.set_clearing_decision(
                id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_clearing_decision(
            id, item_id, decision_type=decision_type, global_decision=global_decision, request_options=request_options
        )
        return _response.data

    async def schedule_bulk_scan(
        self,
        id: int,
        item_id: int,
        *,
        bulk_actions: typing.Optional[typing.Sequence[ScheduleBulkScanBulkActionsItem]] = OMIT,
        ref_text: typing.Optional[str] = OMIT,
        bulk_scope: typing.Optional[ScheduleBulkScanBulkScope] = OMIT,
        force_decision: typing.Optional[bool] = OMIT,
        ignore_irre: typing.Optional[bool] = OMIT,
        delimiters: typing.Optional[str] = OMIT,
        scan_only_findings: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Schedule the bulk scan for the item

        Parameters
        ----------
        id : int
            Id of the upload

        item_id : int
            Id of the itemId

        bulk_actions : typing.Optional[typing.Sequence[ScheduleBulkScanBulkActionsItem]]

        ref_text : typing.Optional[str]

        bulk_scope : typing.Optional[ScheduleBulkScanBulkScope]

        force_decision : typing.Optional[bool]

        ignore_irre : typing.Optional[bool]

        delimiters : typing.Optional[str]

        scan_only_findings : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Bulk scan scheduled successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.schedule_bulk_scan(
                id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.schedule_bulk_scan(
            id,
            item_id,
            bulk_actions=bulk_actions,
            ref_text=ref_text,
            bulk_scope=bulk_scope,
            force_decision=force_decision,
            ignore_irre=ignore_irre,
            delimiters=delimiters,
            scan_only_findings=scan_only_findings,
            request_options=request_options,
        )
        return _response.data

    async def get_bulk_history(
        self, id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetBulkHistory]:
        """
        Get the bulk history for a specific upload item

        Parameters
        ----------
        id : int
            Id of the upload

        item_id : int
            Id of the itemId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetBulkHistory]
            List of the data about the bulk history

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.get_bulk_history(
                id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_bulk_history(id, item_id, request_options=request_options)
        return _response.data

    async def get_license_decisions(
        self, id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[LicenseDecision]:
        """
        Get the license decisions list for the given upload and item id

        Parameters
        ----------
        id : int
            Id of the upload

        item_id : int
            Id of the itemId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LicenseDecision]
            List of the license decisions for the upload-tree id

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.get_license_decisions(
                id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_license_decisions(id, item_id, request_options=request_options)
        return _response.data

    async def add_edit_delete_license_decision(
        self,
        id: int,
        item_id: int,
        *,
        request: typing.Sequence[AddEditDeleteLicenseDecision],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AddEditDeleteLicenseDecisionResponse:
        """
        Add, update or delete a license decision for a particular upload tree item.

        Parameters
        ----------
        id : int
            Id of the upload

        item_id : int
            Id of the itemId

        request : typing.Sequence[AddEditDeleteLicenseDecision]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddEditDeleteLicenseDecisionResponse
            Request processed successfully

        Examples
        --------
        import asyncio

        from fern import AddEditDeleteLicenseDecision, AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.add_edit_delete_license_decision(
                id=1,
                item_id=1,
                request=[AddEditDeleteLicenseDecision()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_edit_delete_license_decision(
            id, item_id, request=request, request_options=request_options
        )
        return _response.data

    async def get_main_licenses(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[License]:
        """
        Get main licenses assigned on a particular upload

        Parameters
        ----------
        id : int
            Id of the upload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[License]
            All main licenses from an upload

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.get_main_licenses(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_main_licenses(id, request_options=request_options)
        return _response.data

    async def set_main_license(
        self,
        id: int,
        *,
        short_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Set the main license for a particular upload.

        Parameters
        ----------
        id : int
            Id of the upload

        short_name : typing.Optional[str]
            short name of the license

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Main license set successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.set_main_license(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_main_license(id, short_name=short_name, request_options=request_options)
        return _response.data

    async def delete_main_license(
        self, id: int, short_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
        """
        Delete a main license from an upload.

        Parameters
        ----------
        id : int
            Id of the upload

        short_name : str
            shortName of the main license to be deleted

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            License is removed successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.delete_main_license(
                id=1,
                short_name="shortName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_main_license(id, short_name, request_options=request_options)
        return _response.data

    async def get_previous_and_next_item(
        self,
        id: int,
        item_id: int,
        *,
        selection: typing.Optional[GetPreviousAndNextItemRequestSelection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPrevNextItem:
        """
        Get the index of the previous and the next time for an upload

        Parameters
        ----------
        id : int
            Id of the upload

        item_id : int
            Id of the itemId

        selection : typing.Optional[GetPreviousAndNextItemRequestSelection]
            Return jobs for the given upload id only

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPrevNextItem
            List of the data about clearing history

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.get_previous_and_next_item(
                id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_previous_and_next_item(
            id, item_id, selection=selection, request_options=request_options
        )
        return _response.data

    async def get_clearing_history(
        self, id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetClearingHistory:
        """
        Get the clearing history for a specific upload item

        Parameters
        ----------
        id : int
            Id of the upload

        item_id : int
            Id of the itemId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetClearingHistory
            List of the data about clearing history

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.get_clearing_history(
                id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_clearing_history(id, item_id, request_options=request_options)
        return _response.data

    async def get_clearing_progress_info(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ClearingProgressInfo:
        """
        Get the clearing progress information for an upload

        Parameters
        ----------
        id : int
            Id of the upload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClearingProgressInfo
            Get clearing progress info

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.get_clearing_progress_info(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_clearing_progress_info(id, request_options=request_options)
        return _response.data

    async def get_licenses_histogram(
        self, id: int, *, agent_id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[LicenseHistogram]:
        """
        Get the licenses histogram for a specific upload

        Parameters
        ----------
        id : int
            Id of the upload

        agent_id : typing.Optional[int]
            Id of the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LicenseHistogram]
            Get the licenses histogram for the upload

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.get_licenses_histogram(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_licenses_histogram(
            id, agent_id=agent_id, request_options=request_options
        )
        return _response.data

    async def get_agents_by_upload_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AgentOfUpload]:
        """
        Returns the list of agents for a upload.

        Parameters
        ----------
        id : int
            Id of the upload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AgentOfUpload]
            Get agents

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.get_agents_by_upload_id(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_agents_by_upload_id(id, request_options=request_options)
        return _response.data

    async def get_all_edited_licenses(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[EditedLicense]:
        """
        Get the edited licenses list for a specific upload

        Parameters
        ----------
        id : int
            Id of the upload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EditedLicense]
            List of the edited licenses in the upload

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.get_all_edited_licenses(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_edited_licenses(id, request_options=request_options)
        return _response.data

    async def get_all_scanned_licenses(
        self, id: int, *, agent_id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ScannedLicense]:
        """
        Get the scanned licenses list for a specific upload

        Parameters
        ----------
        id : int
            Id of the upload

        agent_id : typing.Optional[int]
            Id of the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ScannedLicense]
            List of the scanned licenses in the upload

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.get_all_scanned_licenses(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_scanned_licenses(
            id, agent_id=agent_id, request_options=request_options
        )
        return _response.data

    async def get_item_tree_view(
        self,
        id: int,
        item_id: int,
        *,
        agent_id: typing.Optional[int] = None,
        tag_id: typing.Optional[int] = None,
        scan_license_filter: typing.Optional[int] = None,
        edited_license_filter: typing.Optional[int] = None,
        flatten: typing.Optional[bool] = None,
        sort: typing.Optional[GetItemTreeViewRequestSort] = None,
        search: typing.Optional[str] = None,
        show_quick: typing.Optional[bool] = None,
        filter_open: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[TreeViewModel]:
        """
        Get the tree view for the given upload and item id

        Parameters
        ----------
        id : int
            Id of the upload

        item_id : int
            Id of the itemId

        agent_id : typing.Optional[int]
            Id of the agent

        tag_id : typing.Optional[int]
            Id of the tag

        scan_license_filter : typing.Optional[int]
            ShortName of the selected scan license filter

        edited_license_filter : typing.Optional[int]
            ShortName of the selected edited license filter

        flatten : typing.Optional[bool]
            Flatten the tree

        sort : typing.Optional[GetItemTreeViewRequestSort]
            Sort the tree

        search : typing.Optional[str]
            Filter the list according to the search string

        show_quick : typing.Optional[bool]
            Show all the items of the current container

        filter_open : typing.Optional[bool]
            openCBox Filter is checked

        page : typing.Optional[int]
            Page number (starts from 1)

        limit : typing.Optional[int]
            Limits of responses per request

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TreeViewModel]
            Tree view for the given upload and item id

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.get_item_tree_view(
                id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_item_tree_view(
            id,
            item_id,
            agent_id=agent_id,
            tag_id=tag_id,
            scan_license_filter=scan_license_filter,
            edited_license_filter=edited_license_filter,
            flatten=flatten,
            sort=sort,
            search=search,
            show_quick=show_quick,
            filter_open=filter_open,
            page=page,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    async def get_top_item_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Info]:
        """
        Get the item id for the top level item in a given upload.

        Parameters
        ----------
        id : int
            Id of the upload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Info]
            Top item id

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.get_top_item_id(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_top_item_id(id, request_options=request_options)
        return _response.data

    async def get_licenses_reuse_summary(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetReuseReportSummary:
        """
        Get the overall licenses reuse summary for an upload

        Parameters
        ----------
        id : int
            Id of the upload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetReuseReportSummary
            Get licenses reuse summary

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.get_licenses_reuse_summary(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_licenses_reuse_summary(id, request_options=request_options)
        return _response.data

    async def get_revisions_for_agents(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AgentsRevision]:
        """
        Returns the list of revisions for the successful agents for the upload

        Parameters
        ----------
        id : int
            Id of the upload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AgentsRevision]
            Get successful agents with revisions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.get_revisions_for_agents(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_revisions_for_agents(id, request_options=request_options)
        return _response.data

    async def run_one_shot_nomos(
        self, *, file_input: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> OneShotInfo:
        """
        Run one-shot nomos analysis on the upload without storing the results.

        Parameters
        ----------
        file_input : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OneShotInfo
            Scanner result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.run_one_shot_nomos()


        asyncio.run(main())
        """
        _response = await self._raw_client.run_one_shot_nomos(file_input=file_input, request_options=request_options)
        return _response.data

    async def run_one_shot_monk(
        self, *, file_input: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> OneShotInfo:
        """
        Run one-shot monk analysis on the upload without storing the results.

        Parameters
        ----------
        file_input : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OneShotInfo
            Scanner result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.run_one_shot_monk()


        asyncio.run(main())
        """
        _response = await self._raw_client.run_one_shot_monk(file_input=file_input, request_options=request_options)
        return _response.data

    async def run_one_shot_ceu(
        self, *, file_input: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> OneShotInfo:
        """
        Run one-shot Copyright/Email/URL analysis on the upload without storing the results.

        Parameters
        ----------
        file_input : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OneShotInfo
            Scanner result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.run_one_shot_ceu()


        asyncio.run(main())
        """
        _response = await self._raw_client.run_one_shot_ceu(file_input=file_input, request_options=request_options)
        return _response.data

    async def get_files(
        self,
        *,
        request: typing.Sequence[Hash],
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[File]:
        """
        Get a list of files by hashes

        Parameters
        ----------
        request : typing.Sequence[Hash]

        group_name : typing.Optional[str]
            The group name to chose while downloading specific report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[File]
            List of matching files

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Hash

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.get_files(
                request=[Hash()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_files(
            request=request, group_name=group_name, request_options=request_options
        )
        return _response.data

    async def get_conf_info(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ConfResponse]:
        """
        Get conf information

        Parameters
        ----------
        id : int
            Upload Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ConfResponse]
            current conf information

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.get_conf_info(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_conf_info(id, request_options=request_options)
        return _response.data

    async def update_conf_data(
        self,
        id: int,
        *,
        key: typing.Optional[str] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Info]:
        """
        Updates the conf page data from the server

        Parameters
        ----------
        id : int
            Upload Id

        key : typing.Optional[str]
            Key of the field to be updated

        value : typing.Optional[str]
            Value of the field to be updated. If value is a JSON, it should be
            sent as an encoded string.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Info]
            Config data

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.upload.update_conf_data(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_conf_data(id, key=key, value=value, request_options=request_options)
        return _response.data
