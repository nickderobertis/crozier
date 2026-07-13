

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destiny_components_plug_sets_destiny_plug_sets_component import DestinyComponentsPlugSetsDestinyPlugSetsComponent


class DictionaryComponentResponseOfint64AndDestinyPlugSetsComponent(UniversalBaseModel):
    data: typing.Optional[typing.Dict[str, DestinyComponentsPlugSetsDestinyPlugSetsComponent]] = None
    disabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, this component is disabled.
    """

    privacy: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
