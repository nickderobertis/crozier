

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .copy_log_details_copy_log_details_type import CopyLogDetailsCopyLogDetailsType


class CopyLogDetails(UniversalBaseModel):
    """
    Details for log generated during copy.
    """

    copy_log_details_type: typing_extensions.Annotated[
        CopyLogDetailsCopyLogDetailsType,
        FieldMetadata(alias="copyLogDetailsType"),
        pydantic.Field(alias="copyLogDetailsType", description="Indicates the type of job details."),
    ]
    """
    Indicates the type of job details.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
