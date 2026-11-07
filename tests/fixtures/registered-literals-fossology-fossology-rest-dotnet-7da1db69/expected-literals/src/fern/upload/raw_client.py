

import contextlib
import typing
from json.decoder import JSONDecodeError

from .. import core
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
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.precondition_failed_error import PreconditionFailedError
from ..errors.service_unavailable_error import ServiceUnavailableError
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUploadClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_upload_by_id(
        self,
        id: int,
        *,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Upload]:
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
        HttpResponse[Upload]
            Get upload
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}",
            method="GET",
            headers={
                "groupName": str(group_name) if group_name is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Upload,
                    parse_obj_as(
                        type_=Upload,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    def move_upload_by_id(
        self,
        id: int,
        *,
        folder_id: int,
        action: MoveUploadByIdRequestAction,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
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
        HttpResponse[Info]
            Upload will be copied/moved
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}",
            method="PUT",
            headers={
                "groupName": str(group_name) if group_name is not None else None,
                "folderId": str(folder_id) if folder_id is not None else None,
                "action": str(action) if action is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
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

    def delete_upload_by_id(
        self,
        id: int,
        *,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
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
        HttpResponse[Info]
            Upload will be deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}",
            method="DELETE",
            headers={
                "groupName": str(group_name) if group_name is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
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

    def update_upload_by_id(
        self,
        id: int,
        *,
        status: typing.Optional[UpdateUploadByIdRequestStatus] = None,
        assignee: typing.Optional[int] = None,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
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
        HttpResponse[Info]
            Upload will be updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}",
            method="PATCH",
            params={
                "status": status,
                "assignee": assignee,
            },
            headers={
                "groupName": str(group_name) if group_name is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
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
    ) -> HttpResponse[typing.List[Upload]]:
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
        HttpResponse[typing.List[Upload]]
            An array of uploads
        """
        _response = self._client_wrapper.httpx_client.request(
            "uploads",
            method="GET",
            params={
                "folderId": folder_id,
                "recursive": recursive,
                "name": name,
                "status": status,
                "assignee": assignee,
                "since": since,
            },
            headers={
                "groupName": str(group_name) if group_name is not None else None,
                "page": str(page) if page is not None else None,
                "limit": str(limit) if limit is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Upload],
                    parse_obj_as(
                        type_=typing.List[Upload],
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
    ) -> HttpResponse[Info]:
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
        HttpResponse[Info]
            Upload is created
        """
        _response = self._client_wrapper.httpx_client.request(
            "uploads",
            method="POST",
            json={
                "location": convert_and_respect_annotation_metadata(
                    object_=location, annotation=CreateUploadRequestLocation, direction="write"
                ),
                "scanOptions": convert_and_respect_annotation_metadata(
                    object_=scan_options, annotation=ScanOptions, direction="write"
                ),
                "mainLicense": main_license,
            },
            headers={
                "content-type": "application/json",
                "groupName": str(group_name) if group_name is not None else None,
                "folderId": str(folder_id) if folder_id is not None else None,
                "uploadDescription": str(upload_description) if upload_description is not None else None,
                "public": "protected",
                "applyGlobal": str(apply_global) if apply_global is not None else None,
                "ignoreScm": str(ignore_scm) if ignore_scm is not None else None,
                "uploadType": "vcs",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
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

    @contextlib.contextmanager
    def get_upload_file_by_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
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
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            Required report
        """
        with self._client_wrapper.httpx_client.stream(
            f"uploads/{encode_path_param(id)}/download",
            method="GET",
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    if _response.status_code == 403:
                        raise ForbiddenError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Info,
                                parse_obj_as(
                                    type_=Info,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def get_summary_by_upload_id(
        self,
        id: int,
        *,
        agent_id: typing.Optional[int] = None,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UploadSummary]:
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
        HttpResponse[UploadSummary]
            Get summary
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/summary",
            method="GET",
            params={
                "agentId": agent_id,
            },
            headers={
                "groupName": str(group_name) if group_name is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadSummary,
                    parse_obj_as(
                        type_=UploadSummary,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    def get_item_info(
        self, id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Fileinfo]:
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
        HttpResponse[Fileinfo]
            Get info
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/info",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Fileinfo,
                    parse_obj_as(
                        type_=Fileinfo,
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
    ) -> HttpResponse[UploadLicenses]:
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
        HttpResponse[UploadLicenses]
            Get licenses
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/licenses",
            method="GET",
            params={
                "agent": ",".join(map(str, agent)) if isinstance(agent, (list, tuple, set)) else agent,
                "containers": containers,
                "license": license,
                "copyright": copyright,
            },
            headers={
                "page": str(page) if page is not None else None,
                "limit": str(limit) if limit is not None else None,
                "groupName": str(group_name) if group_name is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadLicenses,
                    parse_obj_as(
                        type_=UploadLicenses,
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
            if _response.status_code == 412:
                raise PreconditionFailedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    def get_copyrights_by_upload_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UploadCopyrights]:
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
        HttpResponse[UploadCopyrights]
            Get copyrights
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/copyrights",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadCopyrights,
                    parse_obj_as(
                        type_=UploadCopyrights,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 412:
                raise PreconditionFailedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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
    ) -> HttpResponse[typing.List[Info]]:
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
        HttpResponse[typing.List[Info]]
            Permissions updated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/permissions",
            method="PUT",
            json={
                "folderId": folder_id,
                "allUploadsPermission": all_uploads_permission,
                "groupId": group_id,
                "newPermission": new_permission,
                "publicPermission": public_permission,
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
                    typing.List[Info],
                    parse_obj_as(
                        type_=typing.List[Info],
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
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    def get_groups_with_permissions(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UploadPermGroups]:
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
        HttpResponse[UploadPermGroups]
            Get Groups with permissions
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/perm-groups",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadPermGroups,
                    parse_obj_as(
                        type_=UploadPermGroups,
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
    ) -> HttpResponse[typing.List[HighlightInfo]]:
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
        HttpResponse[typing.List[HighlightInfo]]
            List of the data about highlight entries
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/highlight",
            method="GET",
            params={
                "clearingId": clearing_id,
                "licenseId": license_id,
                "highlightId": highlight_id,
                "agentId": agent_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[HighlightInfo],
                    parse_obj_as(
                        type_=typing.List[HighlightInfo],
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
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def view_the_content_of_the_file(
        self, id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
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
        HttpResponse[str]
            Get contents
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/view",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
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
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def set_clearing_decision(
        self,
        id: int,
        item_id: int,
        *,
        decision_type: typing.Optional[int] = OMIT,
        global_decision: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
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
        HttpResponse[Info]
            Clearing decision set successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/clearing-decision",
            method="PUT",
            json={
                "decisionType": decision_type,
                "globalDecision": global_decision,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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
    ) -> HttpResponse[Info]:
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
        HttpResponse[Info]
            Bulk scan scheduled successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/bulk-scan",
            method="POST",
            json={
                "bulkActions": convert_and_respect_annotation_metadata(
                    object_=bulk_actions, annotation=typing.Sequence[ScheduleBulkScanBulkActionsItem], direction="write"
                ),
                "refText": ref_text,
                "bulkScope": bulk_scope,
                "forceDecision": force_decision,
                "ignoreIrre": ignore_irre,
                "delimiters": delimiters,
                "scanOnlyFindings": scan_only_findings,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_bulk_history(
        self, id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[GetBulkHistory]]:
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
        HttpResponse[typing.List[GetBulkHistory]]
            List of the data about the bulk history
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/bulk-history",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetBulkHistory],
                    parse_obj_as(
                        type_=typing.List[GetBulkHistory],
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_license_decisions(
        self, id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[LicenseDecision]]:
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
        HttpResponse[typing.List[LicenseDecision]]
            List of the license decisions for the upload-tree id
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/licenses",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[LicenseDecision],
                    parse_obj_as(
                        type_=typing.List[LicenseDecision],
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def add_edit_delete_license_decision(
        self,
        id: int,
        item_id: int,
        *,
        request: typing.Sequence[AddEditDeleteLicenseDecision],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AddEditDeleteLicenseDecisionResponse]:
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
        HttpResponse[AddEditDeleteLicenseDecisionResponse]
            Request processed successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/licenses",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[AddEditDeleteLicenseDecision], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AddEditDeleteLicenseDecisionResponse,
                    parse_obj_as(
                        type_=AddEditDeleteLicenseDecisionResponse,
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
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_main_licenses(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[License]]:
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
        HttpResponse[typing.List[License]]
            All main licenses from an upload
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/licenses/main",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[License],
                    parse_obj_as(
                        type_=typing.List[License],
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def set_main_license(
        self,
        id: int,
        *,
        short_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
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
        HttpResponse[Info]
            Main license set successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/licenses/main",
            method="POST",
            json={
                "shortName": short_name,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
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
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def delete_main_license(
        self, id: int, short_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
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
        HttpResponse[Info]
            License is removed successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/licenses/{encode_path_param(short_name)}/main",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_previous_and_next_item(
        self,
        id: int,
        item_id: int,
        *,
        selection: typing.Optional[GetPreviousAndNextItemRequestSelection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetPrevNextItem]:
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
        HttpResponse[GetPrevNextItem]
            List of the data about clearing history
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/prev-next",
            method="GET",
            params={
                "selection": selection,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPrevNextItem,
                    parse_obj_as(
                        type_=GetPrevNextItem,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_clearing_history(
        self, id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetClearingHistory]:
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
        HttpResponse[GetClearingHistory]
            List of the data about clearing history
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/clearing-history",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetClearingHistory,
                    parse_obj_as(
                        type_=GetClearingHistory,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_clearing_progress_info(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ClearingProgressInfo]:
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
        HttpResponse[ClearingProgressInfo]
            Get clearing progress info
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/clearing-progress",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ClearingProgressInfo,
                    parse_obj_as(
                        type_=ClearingProgressInfo,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_licenses_histogram(
        self, id: int, *, agent_id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[LicenseHistogram]]:
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
        HttpResponse[typing.List[LicenseHistogram]]
            Get the licenses histogram for the upload
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/licenses/histogram",
            method="GET",
            params={
                "agentId": agent_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[LicenseHistogram],
                    parse_obj_as(
                        type_=typing.List[LicenseHistogram],
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_agents_by_upload_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[AgentOfUpload]]:
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
        HttpResponse[typing.List[AgentOfUpload]]
            Get agents
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/agents",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AgentOfUpload],
                    parse_obj_as(
                        type_=typing.List[AgentOfUpload],
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_all_edited_licenses(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[EditedLicense]]:
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
        HttpResponse[typing.List[EditedLicense]]
            List of the edited licenses in the upload
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/licenses/edited",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[EditedLicense],
                    parse_obj_as(
                        type_=typing.List[EditedLicense],
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_all_scanned_licenses(
        self, id: int, *, agent_id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ScannedLicense]]:
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
        HttpResponse[typing.List[ScannedLicense]]
            List of the scanned licenses in the upload
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/licenses/scanned",
            method="GET",
            params={
                "agentId": agent_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ScannedLicense],
                    parse_obj_as(
                        type_=typing.List[ScannedLicense],
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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
    ) -> HttpResponse[typing.List[TreeViewModel]]:
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
        HttpResponse[typing.List[TreeViewModel]]
            Tree view for the given upload and item id
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/tree/view",
            method="GET",
            params={
                "agentId": agent_id,
                "tagId": tag_id,
                "scanLicenseFilter": scan_license_filter,
                "editedLicenseFilter": edited_license_filter,
                "flatten": flatten,
                "sort": sort,
                "search": search,
                "showQuick": show_quick,
                "filterOpen": filter_open,
            },
            headers={
                "page": str(page) if page is not None else None,
                "limit": str(limit) if limit is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TreeViewModel],
                    parse_obj_as(
                        type_=typing.List[TreeViewModel],
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_top_item_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Info]]:
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
        HttpResponse[typing.List[Info]]
            Top item id
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/topitem",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Info],
                    parse_obj_as(
                        type_=typing.List[Info],
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

    def get_licenses_reuse_summary(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetReuseReportSummary]:
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
        HttpResponse[GetReuseReportSummary]
            Get licenses reuse summary
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/licenses/reuse",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetReuseReportSummary,
                    parse_obj_as(
                        type_=GetReuseReportSummary,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_revisions_for_agents(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[AgentsRevision]]:
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
        HttpResponse[typing.List[AgentsRevision]]
            Get successful agents with revisions
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/agents/revision",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AgentsRevision],
                    parse_obj_as(
                        type_=typing.List[AgentsRevision],
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def run_one_shot_nomos(
        self, *, file_input: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OneShotInfo]:
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
        HttpResponse[OneShotInfo]
            Scanner result
        """
        _response = self._client_wrapper.httpx_client.request(
            "uploads/oneshot/nomos",
            method="POST",
            data={},
            files={
                "fileInput": file_input,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OneShotInfo,
                    parse_obj_as(
                        type_=OneShotInfo,
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

    def run_one_shot_monk(
        self, *, file_input: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OneShotInfo]:
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
        HttpResponse[OneShotInfo]
            Scanner result
        """
        _response = self._client_wrapper.httpx_client.request(
            "uploads/oneshot/monk",
            method="POST",
            data={},
            files={
                "fileInput": file_input,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OneShotInfo,
                    parse_obj_as(
                        type_=OneShotInfo,
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

    def run_one_shot_ceu(
        self, *, file_input: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OneShotInfo]:
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
        HttpResponse[OneShotInfo]
            Scanner result
        """
        _response = self._client_wrapper.httpx_client.request(
            "uploads/oneshot/ceu",
            method="POST",
            data={},
            files={
                "fileInput": file_input,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OneShotInfo,
                    parse_obj_as(
                        type_=OneShotInfo,
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

    def get_files(
        self,
        *,
        request: typing.Sequence[Hash],
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[File]]:
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
        HttpResponse[typing.List[File]]
            List of matching files
        """
        _response = self._client_wrapper.httpx_client.request(
            "filesearch",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[Hash], direction="write"
            ),
            headers={
                "content-type": "application/json",
                "groupName": str(group_name) if group_name is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[File],
                    parse_obj_as(
                        type_=typing.List[File],
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

    def get_conf_info(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ConfResponse]]:
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
        HttpResponse[typing.List[ConfResponse]]
            current conf information
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/conf",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ConfResponse],
                    parse_obj_as(
                        type_=typing.List[ConfResponse],
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

    def update_conf_data(
        self,
        id: int,
        *,
        key: typing.Optional[str] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Info]]:
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
        HttpResponse[typing.List[Info]]
            Config data
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/conf",
            method="PUT",
            json={
                "key": key,
                "value": value,
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
                    typing.List[Info],
                    parse_obj_as(
                        type_=typing.List[Info],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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


class AsyncRawUploadClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_upload_by_id(
        self,
        id: int,
        *,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Upload]:
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
        AsyncHttpResponse[Upload]
            Get upload
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}",
            method="GET",
            headers={
                "groupName": str(group_name) if group_name is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Upload,
                    parse_obj_as(
                        type_=Upload,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    async def move_upload_by_id(
        self,
        id: int,
        *,
        folder_id: int,
        action: MoveUploadByIdRequestAction,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
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
        AsyncHttpResponse[Info]
            Upload will be copied/moved
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}",
            method="PUT",
            headers={
                "groupName": str(group_name) if group_name is not None else None,
                "folderId": str(folder_id) if folder_id is not None else None,
                "action": str(action) if action is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
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

    async def delete_upload_by_id(
        self,
        id: int,
        *,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
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
        AsyncHttpResponse[Info]
            Upload will be deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}",
            method="DELETE",
            headers={
                "groupName": str(group_name) if group_name is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
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

    async def update_upload_by_id(
        self,
        id: int,
        *,
        status: typing.Optional[UpdateUploadByIdRequestStatus] = None,
        assignee: typing.Optional[int] = None,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
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
        AsyncHttpResponse[Info]
            Upload will be updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}",
            method="PATCH",
            params={
                "status": status,
                "assignee": assignee,
            },
            headers={
                "groupName": str(group_name) if group_name is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
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
    ) -> AsyncHttpResponse[typing.List[Upload]]:
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
        AsyncHttpResponse[typing.List[Upload]]
            An array of uploads
        """
        _response = await self._client_wrapper.httpx_client.request(
            "uploads",
            method="GET",
            params={
                "folderId": folder_id,
                "recursive": recursive,
                "name": name,
                "status": status,
                "assignee": assignee,
                "since": since,
            },
            headers={
                "groupName": str(group_name) if group_name is not None else None,
                "page": str(page) if page is not None else None,
                "limit": str(limit) if limit is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Upload],
                    parse_obj_as(
                        type_=typing.List[Upload],
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
    ) -> AsyncHttpResponse[Info]:
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
        AsyncHttpResponse[Info]
            Upload is created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "uploads",
            method="POST",
            json={
                "location": convert_and_respect_annotation_metadata(
                    object_=location, annotation=CreateUploadRequestLocation, direction="write"
                ),
                "scanOptions": convert_and_respect_annotation_metadata(
                    object_=scan_options, annotation=ScanOptions, direction="write"
                ),
                "mainLicense": main_license,
            },
            headers={
                "content-type": "application/json",
                "groupName": str(group_name) if group_name is not None else None,
                "folderId": str(folder_id) if folder_id is not None else None,
                "uploadDescription": str(upload_description) if upload_description is not None else None,
                "public": "protected",
                "applyGlobal": str(apply_global) if apply_global is not None else None,
                "ignoreScm": str(ignore_scm) if ignore_scm is not None else None,
                "uploadType": "vcs",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
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

    @contextlib.asynccontextmanager
    async def get_upload_file_by_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
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
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            Required report
        """
        async with self._client_wrapper.httpx_client.stream(
            f"uploads/{encode_path_param(id)}/download",
            method="GET",
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    if _response.status_code == 403:
                        raise ForbiddenError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Info,
                                parse_obj_as(
                                    type_=Info,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def get_summary_by_upload_id(
        self,
        id: int,
        *,
        agent_id: typing.Optional[int] = None,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UploadSummary]:
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
        AsyncHttpResponse[UploadSummary]
            Get summary
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/summary",
            method="GET",
            params={
                "agentId": agent_id,
            },
            headers={
                "groupName": str(group_name) if group_name is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadSummary,
                    parse_obj_as(
                        type_=UploadSummary,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    async def get_item_info(
        self, id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Fileinfo]:
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
        AsyncHttpResponse[Fileinfo]
            Get info
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/info",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Fileinfo,
                    parse_obj_as(
                        type_=Fileinfo,
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
    ) -> AsyncHttpResponse[UploadLicenses]:
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
        AsyncHttpResponse[UploadLicenses]
            Get licenses
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/licenses",
            method="GET",
            params={
                "agent": ",".join(map(str, agent)) if isinstance(agent, (list, tuple, set)) else agent,
                "containers": containers,
                "license": license,
                "copyright": copyright,
            },
            headers={
                "page": str(page) if page is not None else None,
                "limit": str(limit) if limit is not None else None,
                "groupName": str(group_name) if group_name is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadLicenses,
                    parse_obj_as(
                        type_=UploadLicenses,
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
            if _response.status_code == 412:
                raise PreconditionFailedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    async def get_copyrights_by_upload_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UploadCopyrights]:
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
        AsyncHttpResponse[UploadCopyrights]
            Get copyrights
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/copyrights",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadCopyrights,
                    parse_obj_as(
                        type_=UploadCopyrights,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 412:
                raise PreconditionFailedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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
    ) -> AsyncHttpResponse[typing.List[Info]]:
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
        AsyncHttpResponse[typing.List[Info]]
            Permissions updated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/permissions",
            method="PUT",
            json={
                "folderId": folder_id,
                "allUploadsPermission": all_uploads_permission,
                "groupId": group_id,
                "newPermission": new_permission,
                "publicPermission": public_permission,
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
                    typing.List[Info],
                    parse_obj_as(
                        type_=typing.List[Info],
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
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    async def get_groups_with_permissions(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UploadPermGroups]:
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
        AsyncHttpResponse[UploadPermGroups]
            Get Groups with permissions
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/perm-groups",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadPermGroups,
                    parse_obj_as(
                        type_=UploadPermGroups,
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
    ) -> AsyncHttpResponse[typing.List[HighlightInfo]]:
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
        AsyncHttpResponse[typing.List[HighlightInfo]]
            List of the data about highlight entries
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/highlight",
            method="GET",
            params={
                "clearingId": clearing_id,
                "licenseId": license_id,
                "highlightId": highlight_id,
                "agentId": agent_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[HighlightInfo],
                    parse_obj_as(
                        type_=typing.List[HighlightInfo],
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
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def view_the_content_of_the_file(
        self, id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
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
        AsyncHttpResponse[str]
            Get contents
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/view",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
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
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def set_clearing_decision(
        self,
        id: int,
        item_id: int,
        *,
        decision_type: typing.Optional[int] = OMIT,
        global_decision: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
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
        AsyncHttpResponse[Info]
            Clearing decision set successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/clearing-decision",
            method="PUT",
            json={
                "decisionType": decision_type,
                "globalDecision": global_decision,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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
    ) -> AsyncHttpResponse[Info]:
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
        AsyncHttpResponse[Info]
            Bulk scan scheduled successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/bulk-scan",
            method="POST",
            json={
                "bulkActions": convert_and_respect_annotation_metadata(
                    object_=bulk_actions, annotation=typing.Sequence[ScheduleBulkScanBulkActionsItem], direction="write"
                ),
                "refText": ref_text,
                "bulkScope": bulk_scope,
                "forceDecision": force_decision,
                "ignoreIrre": ignore_irre,
                "delimiters": delimiters,
                "scanOnlyFindings": scan_only_findings,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_bulk_history(
        self, id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[GetBulkHistory]]:
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
        AsyncHttpResponse[typing.List[GetBulkHistory]]
            List of the data about the bulk history
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/bulk-history",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetBulkHistory],
                    parse_obj_as(
                        type_=typing.List[GetBulkHistory],
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_license_decisions(
        self, id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[LicenseDecision]]:
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
        AsyncHttpResponse[typing.List[LicenseDecision]]
            List of the license decisions for the upload-tree id
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/licenses",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[LicenseDecision],
                    parse_obj_as(
                        type_=typing.List[LicenseDecision],
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def add_edit_delete_license_decision(
        self,
        id: int,
        item_id: int,
        *,
        request: typing.Sequence[AddEditDeleteLicenseDecision],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AddEditDeleteLicenseDecisionResponse]:
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
        AsyncHttpResponse[AddEditDeleteLicenseDecisionResponse]
            Request processed successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/licenses",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[AddEditDeleteLicenseDecision], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AddEditDeleteLicenseDecisionResponse,
                    parse_obj_as(
                        type_=AddEditDeleteLicenseDecisionResponse,
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
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_main_licenses(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[License]]:
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
        AsyncHttpResponse[typing.List[License]]
            All main licenses from an upload
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/licenses/main",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[License],
                    parse_obj_as(
                        type_=typing.List[License],
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def set_main_license(
        self,
        id: int,
        *,
        short_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
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
        AsyncHttpResponse[Info]
            Main license set successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/licenses/main",
            method="POST",
            json={
                "shortName": short_name,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
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
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def delete_main_license(
        self, id: int, short_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
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
        AsyncHttpResponse[Info]
            License is removed successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/licenses/{encode_path_param(short_name)}/main",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_previous_and_next_item(
        self,
        id: int,
        item_id: int,
        *,
        selection: typing.Optional[GetPreviousAndNextItemRequestSelection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetPrevNextItem]:
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
        AsyncHttpResponse[GetPrevNextItem]
            List of the data about clearing history
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/prev-next",
            method="GET",
            params={
                "selection": selection,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPrevNextItem,
                    parse_obj_as(
                        type_=GetPrevNextItem,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_clearing_history(
        self, id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetClearingHistory]:
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
        AsyncHttpResponse[GetClearingHistory]
            List of the data about clearing history
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/clearing-history",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetClearingHistory,
                    parse_obj_as(
                        type_=GetClearingHistory,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_clearing_progress_info(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ClearingProgressInfo]:
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
        AsyncHttpResponse[ClearingProgressInfo]
            Get clearing progress info
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/clearing-progress",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ClearingProgressInfo,
                    parse_obj_as(
                        type_=ClearingProgressInfo,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_licenses_histogram(
        self, id: int, *, agent_id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[LicenseHistogram]]:
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
        AsyncHttpResponse[typing.List[LicenseHistogram]]
            Get the licenses histogram for the upload
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/licenses/histogram",
            method="GET",
            params={
                "agentId": agent_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[LicenseHistogram],
                    parse_obj_as(
                        type_=typing.List[LicenseHistogram],
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_agents_by_upload_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[AgentOfUpload]]:
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
        AsyncHttpResponse[typing.List[AgentOfUpload]]
            Get agents
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/agents",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AgentOfUpload],
                    parse_obj_as(
                        type_=typing.List[AgentOfUpload],
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_all_edited_licenses(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[EditedLicense]]:
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
        AsyncHttpResponse[typing.List[EditedLicense]]
            List of the edited licenses in the upload
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/licenses/edited",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[EditedLicense],
                    parse_obj_as(
                        type_=typing.List[EditedLicense],
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_all_scanned_licenses(
        self, id: int, *, agent_id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ScannedLicense]]:
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
        AsyncHttpResponse[typing.List[ScannedLicense]]
            List of the scanned licenses in the upload
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/licenses/scanned",
            method="GET",
            params={
                "agentId": agent_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ScannedLicense],
                    parse_obj_as(
                        type_=typing.List[ScannedLicense],
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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
    ) -> AsyncHttpResponse[typing.List[TreeViewModel]]:
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
        AsyncHttpResponse[typing.List[TreeViewModel]]
            Tree view for the given upload and item id
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/tree/view",
            method="GET",
            params={
                "agentId": agent_id,
                "tagId": tag_id,
                "scanLicenseFilter": scan_license_filter,
                "editedLicenseFilter": edited_license_filter,
                "flatten": flatten,
                "sort": sort,
                "search": search,
                "showQuick": show_quick,
                "filterOpen": filter_open,
            },
            headers={
                "page": str(page) if page is not None else None,
                "limit": str(limit) if limit is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TreeViewModel],
                    parse_obj_as(
                        type_=typing.List[TreeViewModel],
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_top_item_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Info]]:
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
        AsyncHttpResponse[typing.List[Info]]
            Top item id
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/topitem",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Info],
                    parse_obj_as(
                        type_=typing.List[Info],
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

    async def get_licenses_reuse_summary(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetReuseReportSummary]:
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
        AsyncHttpResponse[GetReuseReportSummary]
            Get licenses reuse summary
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/licenses/reuse",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetReuseReportSummary,
                    parse_obj_as(
                        type_=GetReuseReportSummary,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_revisions_for_agents(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[AgentsRevision]]:
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
        AsyncHttpResponse[typing.List[AgentsRevision]]
            Get successful agents with revisions
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/agents/revision",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AgentsRevision],
                    parse_obj_as(
                        type_=typing.List[AgentsRevision],
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def run_one_shot_nomos(
        self, *, file_input: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OneShotInfo]:
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
        AsyncHttpResponse[OneShotInfo]
            Scanner result
        """
        _response = await self._client_wrapper.httpx_client.request(
            "uploads/oneshot/nomos",
            method="POST",
            data={},
            files={
                "fileInput": file_input,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OneShotInfo,
                    parse_obj_as(
                        type_=OneShotInfo,
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

    async def run_one_shot_monk(
        self, *, file_input: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OneShotInfo]:
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
        AsyncHttpResponse[OneShotInfo]
            Scanner result
        """
        _response = await self._client_wrapper.httpx_client.request(
            "uploads/oneshot/monk",
            method="POST",
            data={},
            files={
                "fileInput": file_input,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OneShotInfo,
                    parse_obj_as(
                        type_=OneShotInfo,
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

    async def run_one_shot_ceu(
        self, *, file_input: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OneShotInfo]:
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
        AsyncHttpResponse[OneShotInfo]
            Scanner result
        """
        _response = await self._client_wrapper.httpx_client.request(
            "uploads/oneshot/ceu",
            method="POST",
            data={},
            files={
                "fileInput": file_input,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OneShotInfo,
                    parse_obj_as(
                        type_=OneShotInfo,
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

    async def get_files(
        self,
        *,
        request: typing.Sequence[Hash],
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[File]]:
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
        AsyncHttpResponse[typing.List[File]]
            List of matching files
        """
        _response = await self._client_wrapper.httpx_client.request(
            "filesearch",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[Hash], direction="write"
            ),
            headers={
                "content-type": "application/json",
                "groupName": str(group_name) if group_name is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[File],
                    parse_obj_as(
                        type_=typing.List[File],
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

    async def get_conf_info(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ConfResponse]]:
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
        AsyncHttpResponse[typing.List[ConfResponse]]
            current conf information
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/conf",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ConfResponse],
                    parse_obj_as(
                        type_=typing.List[ConfResponse],
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

    async def update_conf_data(
        self,
        id: int,
        *,
        key: typing.Optional[str] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Info]]:
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
        AsyncHttpResponse[typing.List[Info]]
            Config data
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/conf",
            method="PUT",
            json={
                "key": key,
                "value": value,
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
                    typing.List[Info],
                    parse_obj_as(
                        type_=typing.List[Info],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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
