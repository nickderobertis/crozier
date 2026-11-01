

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .copy_progress import CopyProgress
from .job_details import JobDetails


class DataBoxJobDetails(JobDetails):
    """
    Databox Job Details
    """

    copy_progress: typing_extensions.Annotated[
        typing.Optional[typing.List[CopyProgress]],
        FieldMetadata(alias="copyProgress"),
        pydantic.Field(alias="copyProgress", description="Copy progress per storage account."),
    ] = None
    """
    Copy progress per storage account.
    """

    device_password: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="devicePassword"),
        pydantic.Field(alias="devicePassword", description="Set Device password for unlocking Databox"),
    ] = None
    """
    Set Device password for unlocking Databox
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
