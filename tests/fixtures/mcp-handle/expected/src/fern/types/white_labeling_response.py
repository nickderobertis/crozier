

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WhiteLabelingResponse(UniversalBaseModel):
    success: bool = pydantic.Field()
    """
    Whether the operation was successful
    """

    data: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The white labeling data if successful
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error message if unsuccessful
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
