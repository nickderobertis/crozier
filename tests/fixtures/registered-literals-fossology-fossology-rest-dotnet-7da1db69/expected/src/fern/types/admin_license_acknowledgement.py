

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AdminLicenseAcknowledgement(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The primary key of the AdminAcknowledgement
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the AdminAcknowledgement
    """

    acknowledgement: typing.Optional[str] = pydantic.Field(default=None)
    """
    The acknowledgement text of the AdminAcknowledgement
    """

    is_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates if the AdminAcknowledgement is enabled
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
