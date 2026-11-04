

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_detection_response_item_intelligence_description import GetDetectionResponseItemIntelligenceDescription


class GetDetectionResponseItemIntelligence(UniversalBaseModel):
    """
    Intelligence results when requested
    """

    uuid_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")
    ] = None
    description: typing.Optional[GetDetectionResponseItemIntelligenceDescription] = None
    created_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
