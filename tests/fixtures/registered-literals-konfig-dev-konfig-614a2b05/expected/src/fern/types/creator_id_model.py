

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreatorIdModel(UniversalBaseModel):
    """
    The Ironclad user (must be a user in your Ironclad account) used to launch the workflow by using the user's ID.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of value used to identify the user.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user ID of the Ironclad user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
