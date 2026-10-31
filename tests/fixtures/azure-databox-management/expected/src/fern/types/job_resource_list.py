

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .job_resource import JobResource


class JobResourceList(UniversalBaseModel):
    """
    Job Resource Collection
    """

    next_link: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextLink"),
        pydantic.Field(alias="nextLink", description="Link for the next set of job resources."),
    ] = None
    """
    Link for the next set of job resources.
    """

    value: typing.Optional[typing.List[JobResource]] = pydantic.Field(default=None)
    """
    List of job resources.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
