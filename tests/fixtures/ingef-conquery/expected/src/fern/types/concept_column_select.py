

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .select_base import SelectBase


class ConceptColumnSelect(SelectBase):
    """
    Emits the values of the Concepts column. If `asIds` is true, it will instead emit the resolved ids.
    """

    as_ids: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="asIds"), pydantic.Field(alias="asIds")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
