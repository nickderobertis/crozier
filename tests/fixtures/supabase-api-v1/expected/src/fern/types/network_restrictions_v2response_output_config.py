

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .network_restrictions_v2response_output_config_db_allowed_cidrs_item import (
    NetworkRestrictionsV2ResponseOutputConfigDbAllowedCidrsItem,
)


class NetworkRestrictionsV2ResponseOutputConfig(UniversalBaseModel):
    """
    At any given point in time, this is the config that the user has requested be applied to their project. The `status` field indicates if it has been applied to the project, or is pending. When an updated config is received, the applied config is moved to `old_config`.
    """

    db_allowed_cidrs: typing_extensions.Annotated[
        typing.Optional[typing.List[NetworkRestrictionsV2ResponseOutputConfigDbAllowedCidrsItem]],
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
