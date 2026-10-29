

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .cq_element_base import CqElementBase
from .cq_external_format_item import CqExternalFormatItem


class CqExternal(CqElementBase):
    """
    Allows uploading of externally defined cohorts, with additional data. As a list of included entities, with additional options to specify durations or auxiliary virtual selects. The data is uploaded as array of rows as rows of strings. The rows are required to have the same length. The first row is always skipped. As header. Produces an error, when no entities can be resolved.
    """

    format: typing.Optional[typing.List[CqExternalFormatItem]] = None
    values: typing.Optional[typing.List[typing.List[str]]] = None
    only_singles: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="onlySingles"),
        pydantic.Field(
            alias="onlySingles",
            description="If true, throw an error when an entity is resolved multiple times. Additionally, in a result table EXTRA columns will be emitted as STRING instead of LIST[STRING]",
        ),
    ] = None
    """
    If true, throw an error when an entity is resolved multiple times. Additionally, in a result table EXTRA columns will be emitted as STRING instead of LIST[STRING]
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
