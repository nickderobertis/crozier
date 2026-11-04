

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bad_request_error_workflow_launch_code import BadRequestErrorWorkflowLaunchCode


class BadRequestErrorWorkflowLaunch(UniversalBaseModel):
    """ """

    code: typing.Optional[BadRequestErrorWorkflowLaunchCode] = pydantic.Field(default=None)
    """
    A unique code to identify why the workflow cannot be launched.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    A message indicating why the workflow cannot be launched.
    """

    param: typing.Optional[str] = pydantic.Field(default=None)
    """
    The required or expected parameter(s) that may be missing in order to launch the workflow.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
