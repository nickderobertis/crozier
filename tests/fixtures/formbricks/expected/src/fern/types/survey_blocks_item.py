

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .survey_blocks_item_elements_item import SurveyBlocksItemElementsItem
from .survey_blocks_item_logic_item import SurveyBlocksItemLogicItem


class SurveyBlocksItem(UniversalBaseModel):
    id: str
    name: str
    elements: typing.List[SurveyBlocksItemElementsItem]
    logic: typing.Optional[typing.List[SurveyBlocksItemLogicItem]] = None
    logic_fallback: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="logicFallback"), pydantic.Field(alias="logicFallback")
    ] = None
    button_label: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]], FieldMetadata(alias="buttonLabel"), pydantic.Field(alias="buttonLabel")
    ] = None
    back_button_label: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="backButtonLabel"),
        pydantic.Field(alias="backButtonLabel"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(SurveyBlocksItem)
