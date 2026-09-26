

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ThreePieceOut(UniversalBaseModel):
    """
    Output mirror of ThreePieceIn in kits.py.

    Uses validation_alias + serialization_alias on ``copy_text`` so the public
    JSON key is ``copy`` (matching the SpecIn contract) while the Python
    field name avoids shadowing ``BaseModel.copy()``.
    """

    copy_: typing_extensions.Annotated[str, FieldMetadata(alias="copy"), pydantic.Field(alias="copy")]
    design_note: str
    visual: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
