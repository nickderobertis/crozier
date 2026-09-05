

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .api_version import ApiVersion
from .marker import Marker
from .max_jobs import MaxJobs


class ListJobsInput(UniversalBaseModel):
    """
    Input structure for the ListJobs operation.
    """

    max_jobs: typing_extensions.Annotated[
        typing.Optional[MaxJobs], FieldMetadata(alias="MaxJobs"), pydantic.Field(alias="MaxJobs")
    ] = None
    marker: typing_extensions.Annotated[
        typing.Optional[Marker], FieldMetadata(alias="Marker"), pydantic.Field(alias="Marker")
    ] = None
    api_version: typing_extensions.Annotated[
        typing.Optional[ApiVersion], FieldMetadata(alias="APIVersion"), pydantic.Field(alias="APIVersion")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
