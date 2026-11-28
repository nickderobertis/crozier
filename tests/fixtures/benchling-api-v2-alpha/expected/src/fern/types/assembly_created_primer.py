

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AssemblyCreatedPrimer(UniversalBaseModel):
    created_oligo_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createdOligoId"),
        pydantic.Field(
            alias="createdOligoId", description="API identifier of the Benchling oligo created by the assembly."
        ),
    ] = None
    """
    API identifier of the Benchling oligo created by the assembly.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
