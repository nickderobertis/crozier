

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .workflow_request_model import WorkflowRequestModel


class WorkflowAsyncInProgressResponse(UniversalBaseModel):
    """ """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    
    """

    request_payload: typing_extensions.Annotated[
        WorkflowRequestModel, FieldMetadata(alias="requestPayload"), pydantic.Field(alias="requestPayload")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
