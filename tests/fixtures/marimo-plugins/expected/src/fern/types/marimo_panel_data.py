

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .marimo_panel_data_render_json import MarimoPanelDataRenderJson


class MarimoPanelData(UniversalBaseModel):
    extension_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="extensionUrl"), pydantic.Field(alias="extensionUrl")
    ] = None
    docs_json: typing.Dict[str, typing.Any]
    render_json: MarimoPanelDataRenderJson

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
