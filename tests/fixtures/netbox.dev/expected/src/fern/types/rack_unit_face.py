

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .rack_unit_face_label import RackUnitFaceLabel
from .rack_unit_face_value import RackUnitFaceValue


class RackUnitFace(UniversalBaseModel):
    label: RackUnitFaceLabel
    value: RackUnitFaceValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
