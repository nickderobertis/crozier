

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .file_download_block_data_schema import FileDownloadBlockDataSchema
from .file_download_block_parameters_item import FileDownloadBlockParametersItem
from .file_download_target import FileDownloadTarget
from .output_parameter import OutputParameter
from .run_engine import RunEngine


class FileDownloadBlock(UniversalBaseModel):
    label: str = pydantic.Field()
    """
    Author-facing identifier for a block; unique within a workflow.
    """

    next_block_label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional pointer to the next block label when constructing a DAG. Defaults to sequential order when omitted.
    """

    output_parameter: OutputParameter
    continue_on_failure: typing.Optional[bool] = None
    model: typing.Optional[typing.Dict[str, typing.Any]] = None
    disable_cache: typing.Optional[bool] = None
    ignore_workflow_system_prompt: typing.Optional[bool] = None
    next_loop_on_failure: typing.Optional[bool] = None
    s3bucket: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="s3_bucket"), pydantic.Field(alias="s3_bucket")
    ] = None
    aws_access_key_id: typing.Optional[str] = None
    aws_secret_access_key: typing.Optional[str] = None
    region_name: typing.Optional[str] = None
    endpoint_url: typing.Optional[str] = None
    azure_storage_account_name: typing.Optional[str] = None
    azure_storage_account_key: typing.Optional[str] = None
    azure_blob_container_name: typing.Optional[str] = None
    google_credential_id: typing.Optional[str] = None
    google_drive_folder_id: typing.Optional[str] = None
    sftp_host: typing.Optional[str] = None
    sftp_port: typing.Optional[int] = None
    sftp_username: typing.Optional[str] = None
    sftp_password: typing.Optional[str] = None
    sftp_private_key: typing.Optional[str] = None
    sftp_private_key_passphrase: typing.Optional[str] = None
    sftp_remote_path: typing.Optional[str] = None
    sftp_host_key: typing.Optional[str] = None
    prompt: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional natural-language control over which downloaded files are uploaded; empty means upload all.
    """

    path: typing.Optional[str] = None
    continue_on_empty: typing.Optional[bool] = pydantic.Field(default=None)
    """
    When the run download directory has no files, allow the empty upload only after confirming no registered, browser-session, or alternate candidate downloads exist (False, default). Set True to always allow an empty upload.
    """

    task_type: typing.Optional[str] = None
    url: typing.Optional[str] = None
    title: typing.Optional[str] = None
    engine: typing.Optional[RunEngine] = None
    complete_criterion: typing.Optional[str] = None
    complete_criterion_is_untrusted: typing.Optional[bool] = None
    terminate_criterion: typing.Optional[str] = None
    navigation_goal: typing.Optional[str] = None
    data_extraction_goal: typing.Optional[str] = None
    data_schema: typing.Optional[FileDownloadBlockDataSchema] = None
    error_code_mapping: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    max_retries: typing.Optional[int] = None
    max_steps_per_run: typing.Optional[int] = None
    parameters: typing.Optional[typing.List[FileDownloadBlockParametersItem]] = None
    complete_on_download: typing.Optional[bool] = None
    download_suffix: typing.Optional[str] = None
    totp_verification_url: typing.Optional[str] = None
    totp_identifier: typing.Optional[str] = None
    complete_verification: typing.Optional[bool] = None
    include_action_history_in_verification: typing.Optional[bool] = None
    download_timeout: typing.Optional[float] = None
    include_extracted_text: typing.Optional[bool] = None
    download_target: typing.Optional[FileDownloadTarget] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(FileDownloadBlock)
