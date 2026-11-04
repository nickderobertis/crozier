

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeactivatedWorkflowResponseObject(UniversalBaseModel):
    workflow_id: str = pydantic.Field()
    """
    The workflow ID.
    """

    n_taskforces: int = pydantic.Field()
    """
    Number of taskforces to be stopped.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
