

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .alert_event_response import AlertEventResponse


class PagedAlertEventResponse(UniversalBaseModel):
    events: typing.Optional[typing.List[AlertEventResponse]] = None
    page: typing.Optional[int] = None
    size: typing.Optional[int] = None
    total_elements: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalElements"), pydantic.Field(alias="totalElements")
    ] = None
    total_pages: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalPages"), pydantic.Field(alias="totalPages")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
