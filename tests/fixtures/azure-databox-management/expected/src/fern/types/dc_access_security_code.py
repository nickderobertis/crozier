

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DcAccessSecurityCode(UniversalBaseModel):
    """
    Dc Access Security code for device.
    """

    forward_dc_access_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="forwardDcAccessCode"),
        pydantic.Field(alias="forwardDcAccessCode", description="Dc Access Code for dispatching from DC."),
    ] = None
    """
    Dc Access Code for dispatching from DC.
    """

    reverse_dc_access_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="reverseDcAccessCode"),
        pydantic.Field(alias="reverseDcAccessCode", description="Dc Access code for dropping off at DC."),
    ] = None
    """
    Dc Access code for dropping off at DC.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
