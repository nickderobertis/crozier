

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_party_relationships1account import ObPartyRelationships1Account


class ObPartyRelationships1(UniversalBaseModel):
    """
    The Party's relationships with other resources.
    """

    account: typing_extensions.Annotated[
        typing.Optional[ObPartyRelationships1Account],
        FieldMetadata(alias="Account"),
        pydantic.Field(alias="Account", description="Relationship to the Account resource."),
    ] = None
    """
    Relationship to the Account resource.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
