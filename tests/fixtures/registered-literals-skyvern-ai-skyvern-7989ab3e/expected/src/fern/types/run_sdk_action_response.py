

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RunSdkActionResponse(UniversalBaseModel):
    """
    Response from running an SDK action.
    """

    workflow_run_id: str = pydantic.Field()
    """
    The workflow run ID used for this action
    """

    result: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    The result from the action (e.g., selector, value, extracted data)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
