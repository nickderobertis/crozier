

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetPricingv2StatusResponse(UniversalBaseModel):
    has_migrated: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasMigrated"),
        pydantic.Field(alias="hasMigrated", description="Defines if the account has migrated to Pricing V2."),
    ] = None
    """
    Defines if the account has migrated to Pricing V2.
    """

    is_active: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isActive"),
        pydantic.Field(alias="isActive", description="Defines if the account is active."),
    ] = None
    """
    Defines if the account is active.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
