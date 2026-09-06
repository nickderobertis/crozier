

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EventActionIdpAccountCheck(UniversalBaseModel):
    mode: typing.Optional[int] = pydantic.Field(default=None)
    """
    Account check mode:
      * `0` Create or update the account
      * `1` Create the account if it doesn't exist
    """

    template_user: typing.Optional[str] = pydantic.Field(default=None)
    """
    SFTPGo user template in JSON format
    """

    template_admin: typing.Optional[str] = pydantic.Field(default=None)
    """
    SFTPGo admin template in JSON format
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
