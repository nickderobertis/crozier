

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .attribution_event_model import AttributionEventModel


class AlertAttributionModel(UniversalBaseModel):
    """
    Model for AlertAttribution
    """

    attribution_event_list: typing_extensions.Annotated[
        typing.Optional[typing.List[AttributionEventModel]],
        FieldMetadata(alias="attributionEventList"),
        pydantic.Field(alias="attributionEventList"),
    ] = None
    resource_created_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="resourceCreatedBy"),
        pydantic.Field(alias="resourceCreatedBy", description="Resource Created By"),
    ] = None
    """
    Resource Created By
    """

    resource_created_on: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="resourceCreatedOn"),
        pydantic.Field(alias="resourceCreatedOn", description="Resource Created On"),
    ] = None
    """
    Resource Created On
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
