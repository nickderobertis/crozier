

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class StrataRawActionsResponse(UniversalBaseModel):
    strata_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="strataId"), pydantic.Field(alias="strataId", description="The strata server ID")
    ]
    """
    The strata server ID
    """

    server: str = pydantic.Field()
    """
    The requested server name
    """

    result: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Map of categories to raw actions
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
