

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .output_description import OutputDescription


class ImportInputsItem(UniversalBaseModel):
    source_file: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sourceFile"),
        pydantic.Field(
            alias="sourceFile",
            description="Filename of the to preprocess file, relative to the path supplied in `preprocess`.",
        ),
    ] = None
    """
    Filename of the to preprocess file, relative to the path supplied in `preprocess`.
    """

    filter: typing.Optional[str] = pydantic.Field(default=None)
    """
    Groovy script which can be used to filter the csv rows. The row is passed as `row` array, the fields can be accessed as integer variables to the index in the file. For example accessing `value` in `id,value` can be done with `row[value]` (no string up-ticks), or `row[1]`.
    """

    primary: typing.Optional[OutputDescription] = None
    output: typing.Optional[typing.List[OutputDescription]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
