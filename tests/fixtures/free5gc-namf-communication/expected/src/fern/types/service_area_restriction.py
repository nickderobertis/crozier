

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .area import Area
from .restriction_type import RestrictionType


class ServiceAreaRestriction(UniversalBaseModel):
    restriction_type: typing_extensions.Annotated[
        typing.Optional[RestrictionType],
        FieldMetadata(alias="restrictionType"),
        pydantic.Field(alias="restrictionType"),
    ] = None
    areas: typing.Optional[typing.List[Area]] = None
    max_num_of_t_as: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxNumOfTAs"), pydantic.Field(alias="maxNumOfTAs")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
