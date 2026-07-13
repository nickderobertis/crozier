

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .label_user import LabelUser


class ExportAnnualOverviewRead(UniversalBaseModel):
    alias_user: typing.Optional[LabelUser] = pydantic.Field(default=None)
    """
    The user to which this annual overview belongs.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the annual overview 's creation.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the annual overview as created on the server.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the annual overview 's last update.
    """

    year: typing.Optional[int] = pydantic.Field(default=None)
    """
    The year for which the overview is.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
