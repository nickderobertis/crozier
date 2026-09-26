

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2table_run_dispatch import V2TableRunDispatch


class V2CancelTableDispatchResponse(UniversalBaseModel):
    """
    The dispatch in its post-cancellation state.
    """

    data: V2TableRunDispatch = pydantic.Field()
    """
    Response data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
