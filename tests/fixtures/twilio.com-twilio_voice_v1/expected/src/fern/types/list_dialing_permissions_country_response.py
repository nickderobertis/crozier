

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_dialing_permissions_country_response_meta import ListDialingPermissionsCountryResponseMeta
from .voice_v1dialing_permissions_dialing_permissions_country import VoiceV1DialingPermissionsDialingPermissionsCountry


class ListDialingPermissionsCountryResponse(UniversalBaseModel):
    content: typing.Optional[typing.List[VoiceV1DialingPermissionsDialingPermissionsCountry]] = None
    meta: typing.Optional[ListDialingPermissionsCountryResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
