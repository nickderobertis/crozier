

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ResponseIncompleteStreamingEventResponseIncompleteDetails(UniversalBaseModel):
    """
    Details about why the response was incomplete, if applicable.
    """

    reason: str = pydantic.Field()
    """
    The reason the response could not be completed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
