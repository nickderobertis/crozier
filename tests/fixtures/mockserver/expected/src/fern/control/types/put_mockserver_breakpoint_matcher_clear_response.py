

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PutMockserverBreakpointMatcherClearResponse(UniversalBaseModel):
    status: typing.Optional[str] = None
    count: typing.Optional[int] = pydantic.Field(default=None)
    """
    number of matchers that were removed
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
