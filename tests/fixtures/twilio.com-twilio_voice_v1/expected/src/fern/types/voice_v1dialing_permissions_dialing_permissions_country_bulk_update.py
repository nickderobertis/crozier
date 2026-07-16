

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class VoiceV1DialingPermissionsDialingPermissionsCountryBulkUpdate(UniversalBaseModel):
    update_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of countries updated
    """

    update_request: typing.Optional[str] = pydantic.Field(default=None)
    """
    A bulk update request to change voice dialing country permissions stored as a URL-encoded, JSON array of update objects. For example : `[ { "iso_code": "GB", "low_risk_numbers_enabled": "true", "high_risk_special_numbers_enabled":"true", "high_risk_tollfraud_numbers_enabled": "false" } ]`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
