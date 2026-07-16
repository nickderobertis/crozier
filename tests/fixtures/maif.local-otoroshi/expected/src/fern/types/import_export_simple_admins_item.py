

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ImportExportSimpleAdminsItem(UniversalBaseModel):
    """
    Administrator using just login/password tuple to access Otoroshi
    """

    created_at: typing_extensions.Annotated[int, FieldMetadata(alias="createdAt")] = pydantic.Field()
    """
    The creation date of the user
    """

    label: str = pydantic.Field()
    """
    The label for the user
    """

    password: str = pydantic.Field()
    """
    The hashed password of the user
    """

    username: str = pydantic.Field()
    """
    The email address of the user
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
