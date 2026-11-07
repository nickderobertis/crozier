

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class CreateANewWorkflowAsyncResponse(UniversalBaseModel):
    """ """

    async_job_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="asyncJobId"), pydantic.Field(alias="asyncJobId", description="")
    ] = None
    """
    
    """

    async_job_status_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="asyncJobStatusUrl"),
        pydantic.Field(alias="asyncJobStatusUrl", description=""),
    ] = None
    """
    
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
