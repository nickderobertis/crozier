

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marimo_data_editor_data_initial_value_edits_item import MarimoDataEditorDataInitialValueEditsItem


class MarimoDataEditorDataInitialValue(UniversalBaseModel):
    edits: typing.List[MarimoDataEditorDataInitialValueEditsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
