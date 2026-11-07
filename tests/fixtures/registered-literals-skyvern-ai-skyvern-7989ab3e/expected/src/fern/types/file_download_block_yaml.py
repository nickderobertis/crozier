

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .file_download_target import FileDownloadTarget
from .run_engine import RunEngine


class FileDownloadBlockYaml(UniversalBaseModel):
    label: str = pydantic.Field()
    """
    Author-facing identifier; must be unique per workflow.
    """

    next_block_label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional pointer to the label of the next block. When omitted, it will default to sequential order. See [[s-4bnl]].
    """

    continue_on_failure: typing.Optional[bool] = None
    model: typing.Optional[typing.Dict[str, typing.Any]] = None
    ignore_workflow_system_prompt: typing.Optional[bool] = None
    next_loop_on_failure: typing.Optional[bool] = None
    download_target: typing.Optional[FileDownloadTarget] = None
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
    path: typing.Optional[str] = None
    prompt: typing.Optional[str] = None
    continue_on_empty: typing.Optional[bool] = None
    navigation_goal: str
    url: typing.Optional[str] = None
    title: typing.Optional[str] = None
    engine: typing.Optional[RunEngine] = None
    error_code_mapping: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    max_retries: typing.Optional[int] = None
    max_steps_per_run: typing.Optional[int] = None
    parameter_keys: typing.Optional[typing.List[str]] = None
    download_suffix: typing.Optional[str] = None
    totp_verification_url: typing.Optional[str] = None
    totp_identifier: typing.Optional[str] = None
    disable_cache: typing.Optional[bool] = None
    download_timeout: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
