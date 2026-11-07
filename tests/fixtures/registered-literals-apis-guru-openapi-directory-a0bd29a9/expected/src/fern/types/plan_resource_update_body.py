

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .plan_resource_identity import PlanResourceIdentity
from .plan_resource_properties import PlanResourceProperties


class PlanResourceUpdateBody(UniversalBaseModel):
    identity: typing.Optional[PlanResourceIdentity] = None
    properties: typing.Optional[PlanResourceProperties] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
