

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CommonTaskAssociation(UniversalBaseModel):
    deal_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="dealId"),
        pydantic.Field(alias="dealId", description="The id of the deal to associate with task"),
    ] = None
    """
    The id of the deal to associate with task
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
