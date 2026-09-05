

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .is_truncated import IsTruncated
from .jobs_list import JobsList


class ListJobsOutput(UniversalBaseModel):
    """
    Output structure for the ListJobs operation.
    """

    jobs: typing_extensions.Annotated[
        typing.Optional[JobsList], FieldMetadata(alias="Jobs"), pydantic.Field(alias="Jobs")
    ] = None
    is_truncated: typing_extensions.Annotated[
        typing.Optional[IsTruncated], FieldMetadata(alias="IsTruncated"), pydantic.Field(alias="IsTruncated")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
