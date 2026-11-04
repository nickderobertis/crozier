

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class WorkflowAsyncLaunchSuccessResponseWorkflowUrls(UniversalBaseModel):
    """ """

    browser_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="browserUrl"),
        pydantic.Field(alias="browserUrl", description="The URL for accessing the workflow in a browser."),
    ] = None
    """
    The URL for accessing the workflow in a browser.
    """

    api_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="apiUrl"),
        pydantic.Field(alias="apiUrl", description="The URL for accessing workflow data via the REST API."),
    ] = None
    """
    The URL for accessing workflow data via the REST API.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
