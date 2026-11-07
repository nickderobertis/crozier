

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .launched_workflow_model_signatures_state import LaunchedWorkflowModelSignaturesState


class LaunchedWorkflowModelSignatures(UniversalBaseModel):
    state: typing.Optional[LaunchedWorkflowModelSignaturesState] = pydantic.Field(default=None)
    """
    The state of the signatures.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The url where signature information is located if it exists.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
