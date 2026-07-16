

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .wage_setting import WageSetting


class UpdateWageSettingResponse(UniversalBaseModel):
    """
    Represents a response from an update request containing the updated `WageSetting` object
    or error messages.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    The errors that occurred during the request.
    """

    wage_setting: typing.Optional[WageSetting] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
