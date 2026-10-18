

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .network_restrictions_v2response_output_old_config_db_allowed_cidrs_item import (
    NetworkRestrictionsV2ResponseOutputOldConfigDbAllowedCidrsItem,
)


class NetworkRestrictionsV2ResponseOutputOldConfig(UniversalBaseModel):
    """
    Populated when a new config has been received, but not registered as successfully applied to a project.
    """

    db_allowed_cidrs: typing_extensions.Annotated[
        typing.Optional[typing.List[NetworkRestrictionsV2ResponseOutputOldConfigDbAllowedCidrsItem]],
        FieldMetadata(alias="dbAllowedCidrs"),
        pydantic.Field(alias="dbAllowedCidrs"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
