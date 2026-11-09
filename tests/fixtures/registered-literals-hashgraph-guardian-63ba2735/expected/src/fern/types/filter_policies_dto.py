

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FilterPoliciesDto(UniversalBaseModel):
    policy_id1: typing_extensions.Annotated[str, FieldMetadata(alias="policyId1"), pydantic.Field(alias="policyId1")]
    policy_id2: typing_extensions.Annotated[str, FieldMetadata(alias="policyId2"), pydantic.Field(alias="policyId2")]
    policy_ids: typing_extensions.Annotated[str, FieldMetadata(alias="policyIds"), pydantic.Field(alias="policyIds")]
    events_lvl: typing_extensions.Annotated[float, FieldMetadata(alias="eventsLvl"), pydantic.Field(alias="eventsLvl")]
    prop_lvl: typing_extensions.Annotated[float, FieldMetadata(alias="propLvl"), pydantic.Field(alias="propLvl")]
    children_lvl: typing_extensions.Annotated[
        float, FieldMetadata(alias="childrenLvl"), pydantic.Field(alias="childrenLvl")
    ]
    id_lvl: typing_extensions.Annotated[float, FieldMetadata(alias="idLvl"), pydantic.Field(alias="idLvl")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
