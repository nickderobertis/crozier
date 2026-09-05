

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .api_version import ApiVersion
from .job_id import JobId


class CancelJobInput(UniversalBaseModel):
    """
    Input structure for the CancelJob operation.
    """

    job_id: typing_extensions.Annotated[JobId, FieldMetadata(alias="JobId"), pydantic.Field(alias="JobId")]
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
