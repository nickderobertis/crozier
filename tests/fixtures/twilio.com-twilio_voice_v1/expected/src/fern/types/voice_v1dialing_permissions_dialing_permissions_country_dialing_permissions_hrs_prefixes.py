

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class VoiceV1DialingPermissionsDialingPermissionsCountryDialingPermissionsHrsPrefixes(UniversalBaseModel):
    prefix: typing.Optional[str] = pydantic.Field(default=None)
    """
    A prefix is a contiguous number range for a block of E.164 numbers that includes the E.164 assigned country code. For example, a North American Numbering Plan prefix like `+1510720` written like `+1(510) 720` matches all numbers inclusive from `+1(510) 720-0000` to `+1(510) 720-9999`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
