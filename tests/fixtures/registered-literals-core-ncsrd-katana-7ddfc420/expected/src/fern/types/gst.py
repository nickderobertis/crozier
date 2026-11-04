

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .base_slice_des import BaseSliceDes
from .service_descriptor import ServiceDescriptor
from .test_descriptor import TestDescriptor


class Gst(UniversalBaseModel):
    base_slice_descriptor: typing.Optional[BaseSliceDes] = None
    service_descriptor: typing.Optional[ServiceDescriptor] = None
    test_descriptor: typing.Optional[TestDescriptor] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
