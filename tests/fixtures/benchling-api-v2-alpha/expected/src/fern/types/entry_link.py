

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .entry_link_type import EntryLinkType


class EntryLink(UniversalBaseModel):
    """
    Links are contained within notes to reference resources that live outside of the entry. A link can target an external resource via an http(s):// hyperlink or a Benchling resource via @-mentions and drag-n-drop.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    For linked Benchling resources, this will be the ID of that resource (e.g., 'seq_RhYGVnHF'). Omitted for "link" types.
    """

    type: typing.Optional[EntryLinkType] = pydantic.Field(default=None)
    """
    The type of resource being linked. For hyperlinks: 'link'. For linked Benchling resources, one of: 'user', 'request', 'entry', 'stage_entry', 'protocol', 'workflow', 'custom_entity', 'aa_sequence', 'dna_sequence', 'batch', 'box', 'container', 'location', 'plate', 'sql_dashboard'; and (for legacy support) 'insights_dashboard', 'folder'.
    """

    web_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="webURL"),
        pydantic.Field(
            alias="webURL",
            description='Canonical URL of the linked Benchling resource (if you have at least READ authorization for that resource), or the explicit URL provided as hyperlink for "link" types. Note: locations do not currently have a URL.',
        ),
    ] = None
    """
    Canonical URL of the linked Benchling resource (if you have at least READ authorization for that resource), or the explicit URL provided as hyperlink for "link" types. Note: locations do not currently have a URL.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
