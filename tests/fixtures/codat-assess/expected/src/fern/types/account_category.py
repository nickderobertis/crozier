

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AccountCategory(UniversalBaseModel):
    detail_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="detailType"),
        pydantic.Field(alias="detailType", description="Most granular chart of account type."),
    ] = None
    """
    Most granular chart of account type.
    """

    subtype: typing.Optional[str] = pydantic.Field(default=None)
    """
    The account subtype.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The top level account type.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
