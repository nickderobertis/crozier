

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .creation_date import CreationDate
from .is_canceled import IsCanceled
from .job_id import JobId
from .job_type import JobType


class Job(UniversalBaseModel):
    """
    Representation of a job returned by the ListJobs operation.
    """

    job_id: typing_extensions.Annotated[
        typing.Optional[JobId], FieldMetadata(alias="JobId"), pydantic.Field(alias="JobId")
    ] = None
    creation_date: typing_extensions.Annotated[
        typing.Optional[CreationDate], FieldMetadata(alias="CreationDate"), pydantic.Field(alias="CreationDate")
    ] = None
    is_canceled: typing_extensions.Annotated[
        typing.Optional[IsCanceled], FieldMetadata(alias="IsCanceled"), pydantic.Field(alias="IsCanceled")
    ] = None
    job_type: typing_extensions.Annotated[
        typing.Optional[JobType], FieldMetadata(alias="JobType"), pydantic.Field(alias="JobType")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
