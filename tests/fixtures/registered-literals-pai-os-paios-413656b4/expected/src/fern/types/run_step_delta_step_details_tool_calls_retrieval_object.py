

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RunStepDeltaStepDetailsToolCallsRetrievalObject(UniversalBaseModel):
    index: int = pydantic.Field()
    """
    The index of the tool call in the tool calls array.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the tool call object.
    """

    retrieval: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
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
