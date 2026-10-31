

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .copy_progress import CopyProgress
from .job_details import JobDetails


class DataBoxHeavyJobDetails(JobDetails):
    """
    Databox Heavy Device Job Details
    """

    copy_progress: typing_extensions.Annotated[
        typing.Optional[typing.List[CopyProgress]],
        FieldMetadata(alias="copyProgress"),
        pydantic.Field(alias="copyProgress", description="Copy progress per account."),
    ] = None
    """
    Copy progress per account.
    """

    device_password: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="devicePassword"),
        pydantic.Field(alias="devicePassword", description="Set Device password for unlocking Databox Heavy"),
    ] = None
    """
    Set Device password for unlocking Databox Heavy
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
