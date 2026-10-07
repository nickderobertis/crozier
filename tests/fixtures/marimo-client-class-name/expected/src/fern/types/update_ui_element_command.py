

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .http_request import HttpRequest
from .ui_element_id import UiElementId
from .update_ui_element_command_type import UpdateUiElementCommandType


class UpdateUiElementCommand(UniversalBaseModel):
    """
    Update UI element values.

        Triggered when users interact with UI elements (sliders, inputs, dropdowns, etc.).
        Updates element values and re-executes dependent cells.

        Attributes:
            object_ids: UI elements to update.
            values: New values for the elements. Must match length of object_ids.
            request: HTTP request context if available.
            token: Unique request identifier for deduplication.
    """

    object_ids: typing_extensions.Annotated[
        typing.List[UiElementId], FieldMetadata(alias="objectIds"), pydantic.Field(alias="objectIds")
    ]
    request: typing.Optional[HttpRequest] = None
    token: typing.Optional[str] = None
    type: UpdateUiElementCommandType
    values: typing.List[typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
