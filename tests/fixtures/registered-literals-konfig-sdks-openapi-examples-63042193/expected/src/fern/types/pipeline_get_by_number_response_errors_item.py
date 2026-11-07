

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pipeline_get_by_number_response_errors_item_type import PipelineGetByNumberResponseErrorsItemType


class PipelineGetByNumberResponseErrorsItem(UniversalBaseModel):
    """
    An error with a type and message.
    """

    type: PipelineGetByNumberResponseErrorsItemType = pydantic.Field()
    """
    The type of error.
    """

    message: str = pydantic.Field()
    """
    A human-readable error message.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
