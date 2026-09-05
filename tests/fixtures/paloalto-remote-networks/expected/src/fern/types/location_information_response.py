

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error_detail_cause_infos import ErrorDetailCauseInfos
from .location_information_set import LocationInformationSet


class LocationInformationResponse(UniversalBaseModel):
    """
    Location Information Response
    """

    errors: typing.Optional[ErrorDetailCauseInfos] = None
    result: typing.Optional[LocationInformationSet] = None
    status: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
