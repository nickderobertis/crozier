

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_detection_response_item_intelligence_description import CreateDetectionResponseItemIntelligenceDescription


class CreateDetectionResponseItemIntelligence(UniversalBaseModel):
    """
    Intelligence results when requested
    """

    description: typing.Optional[CreateDetectionResponseItemIntelligenceDescription] = None
    created_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
