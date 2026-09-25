

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegisterQueueResponseGifRatingPolicyOptionsValue(UniversalBaseModel):
    """
    `{rating_name}`: Dictionary containing the details of the
    rating with the name of the rating as
    the key.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the rating option.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the rating option.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
