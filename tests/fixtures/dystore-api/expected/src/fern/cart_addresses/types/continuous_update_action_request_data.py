

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .continuous_update_action_request_data_attributes import ContinuousUpdateActionRequestDataAttributes
from .continuous_update_action_request_data_relationships import ContinuousUpdateActionRequestDataRelationships


class ContinuousUpdateActionRequestData(UniversalBaseModel):
    attributes: typing.Optional[ContinuousUpdateActionRequestDataAttributes] = None
    id: typing.Optional[str] = None
    relationships: typing.Optional[ContinuousUpdateActionRequestDataRelationships] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
