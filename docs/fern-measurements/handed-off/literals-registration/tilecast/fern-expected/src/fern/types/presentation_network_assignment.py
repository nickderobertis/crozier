

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PresentationNetworkAssignment(UniversalBaseModel):
    screen_id: typing_extensions.Annotated[str, FieldMetadata(alias="screenId"), pydantic.Field(alias="screenId")]
    screen_name: typing_extensions.Annotated[str, FieldMetadata(alias="screenName"), pydantic.Field(alias="screenName")]
    platform: str
    presentation_network_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="presentationNetworkId"),
        pydantic.Field(alias="presentationNetworkId"),
    ] = None
    presentation_network_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="presentationNetworkName"),
        pydantic.Field(alias="presentationNetworkName"),
    ] = None
    assigned_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="assignedAt"), pydantic.Field(alias="assignedAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
