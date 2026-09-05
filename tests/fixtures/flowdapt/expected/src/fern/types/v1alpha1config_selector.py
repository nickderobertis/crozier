

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1alpha1config_selector_type import V1Alpha1ConfigSelectorType
from .v1alpha1config_selector_value import V1Alpha1ConfigSelectorValue


class V1Alpha1ConfigSelector(UniversalBaseModel):
    kind: typing.Optional[str] = None
    type: typing.Optional[V1Alpha1ConfigSelectorType] = None
    value: typing.Optional[V1Alpha1ConfigSelectorValue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
