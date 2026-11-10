

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_object_incomplete_details_reason import RunObjectIncompleteDetailsReason


class RunObjectIncompleteDetails(UniversalBaseModel):
    """
    Details on why the run is incomplete. Will be `null` if the run is not incomplete.
    """

    reason: typing.Optional[RunObjectIncompleteDetailsReason] = pydantic.Field(default=None)
    """
    The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
