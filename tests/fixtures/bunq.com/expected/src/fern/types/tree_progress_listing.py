

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .label_user import LabelUser


class TreeProgressListing(UniversalBaseModel):
    label_user: typing.Optional[LabelUser] = pydantic.Field(default=None)
    """
    The label of the user the progress belongs to.
    """

    number_of_tree: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of trees this user and all users have planted.
    """

    progress_tree_next: typing.Optional[int] = pydantic.Field(default=None)
    """
    The progress towards the next tree.
    """

    url_invite_profile: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the invite profile.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
