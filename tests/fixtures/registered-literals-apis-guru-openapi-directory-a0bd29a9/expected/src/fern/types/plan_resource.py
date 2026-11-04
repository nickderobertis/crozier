

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .plan_resource_identity import PlanResourceIdentity
from .plan_resource_properties import PlanResourceProperties


class PlanResource(UniversalBaseModel):
    id: typing.Optional[str] = None
    identity: typing.Optional[PlanResourceIdentity] = None
    location: typing.Optional[str] = None
    name: typing.Optional[str] = None
    properties: typing.Optional[PlanResourceProperties] = None
    provisioning_state: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="provisioningState"), pydantic.Field(alias="provisioningState")
    ] = None
    tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
