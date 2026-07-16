

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_dialing_permissions_hrs_prefixes_response_meta import ListDialingPermissionsHrsPrefixesResponseMeta
from .voice_v1dialing_permissions_dialing_permissions_country_dialing_permissions_hrs_prefixes import (
    VoiceV1DialingPermissionsDialingPermissionsCountryDialingPermissionsHrsPrefixes,
)


class ListDialingPermissionsHrsPrefixesResponse(UniversalBaseModel):
    content: typing.Optional[
        typing.List[VoiceV1DialingPermissionsDialingPermissionsCountryDialingPermissionsHrsPrefixes]
    ] = None
    meta: typing.Optional[ListDialingPermissionsHrsPrefixesResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
