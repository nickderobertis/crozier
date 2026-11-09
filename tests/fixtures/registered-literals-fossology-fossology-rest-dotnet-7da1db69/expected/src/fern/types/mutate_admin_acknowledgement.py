

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MutateAdminAcknowledgement(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the acknowledgement.
    Required if update is TRUE.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the acknowledgement.
    Not required if update is TRUE and toggle is set.
    """

    ack: typing.Optional[str] = pydantic.Field(default=None)
    """
    The acknowledgement text.
    Not required if update is TRUE and toggle is set.
    """

    toggle: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean indicating the toggle state.
    """

    update: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean indicating if an update is needed.
    If true, update the given admin acknowledgement.
    if false, add new admin acknowledgement.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
