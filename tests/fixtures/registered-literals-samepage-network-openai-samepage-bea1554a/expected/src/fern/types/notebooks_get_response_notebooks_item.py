

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NotebooksGetResponseNotebooksItem(UniversalBaseModel):
    uuid_: typing_extensions.Annotated[
        str, FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid", description="The notebook's UUID")
    ]
    """
    The notebook's UUID
    """

    workspace: str = pydantic.Field()
    """
    The name of the workspace this notebook represents.
    """

    app_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="appName"),
        pydantic.Field(alias="appName", description="The name of the application this notebook is a part of."),
    ]
    """
    The name of the application this notebook is a part of.
    """

    email: str = pydantic.Field()
    """
    The email address of the user who owns this notebook.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
