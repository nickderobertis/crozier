

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MutateStdComment(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the standard comment.
    Required if update is TRUE.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the standard comment.
    Required if update is FALSE.
    """

    comment: typing.Optional[str] = pydantic.Field(default=None)
    """
    The standard comment text.
    Required if update is FALSE.
    """

    toggle: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean indicating the toggle state.
    """

    update: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean indicating if an update is needed.
    If TRUE, update the given standard comment.
    if FALSE, add new standard comment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
