

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MarimoMplInteractiveData(UniversalBaseModel):
    mpl_js_url: typing_extensions.Annotated[str, FieldMetadata(alias="mplJsUrl"), pydantic.Field(alias="mplJsUrl")]
    css_url: typing_extensions.Annotated[str, FieldMetadata(alias="cssUrl"), pydantic.Field(alias="cssUrl")]
    toolbar_images: typing_extensions.Annotated[
        typing.Dict[str, str], FieldMetadata(alias="toolbarImages"), pydantic.Field(alias="toolbarImages")
    ]
    width: float
    height: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
