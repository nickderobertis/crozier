

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RunStepDetailsToolCallsRetrievalObject(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The ID of the tool call object.
    """

    retrieval: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    For now, this is always going to be an empty object.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
