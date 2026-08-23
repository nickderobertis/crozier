

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .data_element_base import DataElementBase
from .single_valued_data_element_value import SingleValuedDataElementValue


class SingleValuedDataElement(DataElementBase):
    """
    Single scalar value (EN 18223 clause 4.1.2.5).
    """

    value_data_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="valueDataType"),
        pydantic.Field(alias="valueDataType", description="XSD type of the value (e.g. `xsd:string`, `xsd:decimal`)."),
    ] = None
    """
    XSD type of the value (e.g. `xsd:string`, `xsd:decimal`).
    """

    value: typing.Optional[SingleValuedDataElementValue] = pydantic.Field(default=None)
    """
    The scalar value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
