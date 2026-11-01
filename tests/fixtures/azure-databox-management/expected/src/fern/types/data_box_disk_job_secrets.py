

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .disk_secret import DiskSecret
from .job_secrets import JobSecrets


class DataBoxDiskJobSecrets(JobSecrets):
    """
    The secrets related to disk job.
    """

    disk_secrets: typing_extensions.Annotated[
        typing.Optional[typing.List[DiskSecret]],
        FieldMetadata(alias="diskSecrets"),
        pydantic.Field(alias="diskSecrets", description="Contains the list of secrets object for that device."),
    ] = None
    """
    Contains the list of secrets object for that device.
    """

    is_passkey_user_defined: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isPasskeyUserDefined"),
        pydantic.Field(alias="isPasskeyUserDefined", description="Whether passkey was provided by user."),
    ] = None
    """
    Whether passkey was provided by user.
    """

    pass_key: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="passKey"),
        pydantic.Field(alias="passKey", description="PassKey for the disk Job."),
    ] = None
    """
    PassKey for the disk Job.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
