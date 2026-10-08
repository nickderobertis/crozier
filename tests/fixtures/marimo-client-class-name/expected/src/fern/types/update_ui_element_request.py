

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .http_request import HttpRequest
from .ui_element_id import UiElementId


class UpdateUiElementRequest(UniversalBaseModel):
    object_ids: typing_extensions.Annotated[
        typing.List[UiElementId], FieldMetadata(alias="objectIds"), pydantic.Field(alias="objectIds")
    ]
    request: typing.Optional[HttpRequest] = None
    token: typing.Optional[str] = None
    values: typing.List[typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
