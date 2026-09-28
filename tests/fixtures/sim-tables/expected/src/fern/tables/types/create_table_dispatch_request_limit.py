

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_table_dispatch_request_limit_type import CreateTableDispatchRequestLimitType


class CreateTableDispatchRequestLimit(UniversalBaseModel):
    """
    Optional cap on eligible rows to run.
    """

    type: CreateTableDispatchRequestLimitType = pydantic.Field()
    """
    Unit constrained by the run cap.
    """

    max: int = pydantic.Field()
    """
    Maximum eligible rows to run.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
