

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.ro_crate import RoCrate


class ListRoCratesResponse(UniversalBaseModel):
    """
    A list of RO-Crates visible to the caller.
    """

    total: int = pydantic.Field()
    """
    Total number of RO-Crates (before pagination) visible to the caller.
    """

    ro_crates: typing_extensions.Annotated[
        typing.List[RoCrate], FieldMetadata(alias="roCrates"), pydantic.Field(alias="roCrates")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
