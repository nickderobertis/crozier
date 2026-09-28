

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MarimoFileBrowserData(UniversalBaseModel):
    initial_path: typing_extensions.Annotated[
        str, FieldMetadata(alias="initialPath"), pydantic.Field(alias="initialPath")
    ]
    filetypes: typing.List[str]
    selection_mode: typing_extensions.Annotated[
        str, FieldMetadata(alias="selectionMode"), pydantic.Field(alias="selectionMode")
    ]
    multiple: bool
    label: typing.Optional[str] = None
    restrict_navigation: typing_extensions.Annotated[
        bool, FieldMetadata(alias="restrictNavigation"), pydantic.Field(alias="restrictNavigation")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
