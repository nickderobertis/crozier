

import typing

from .assay_run_note_part import AssayRunNotePart
from .box_creation_table_note_part import BoxCreationTableNotePart
from .checkbox_note_part import CheckboxNotePart
from .external_file_note_part import ExternalFileNotePart
from .lookup_table_note_part import LookupTableNotePart
from .mixture_prep_table_note_part import MixturePrepTableNotePart
from .plate_creation_table_note_part import PlateCreationTableNotePart
from .registration_table_note_part import RegistrationTableNotePart
from .results_table_note_part import ResultsTableNotePart
from .simple_note_part import SimpleNotePart
from .table_note_part import TableNotePart
from .text_box_note_part import TextBoxNotePart

EntryTemplateDayNotesItem = typing.Union[
    SimpleNotePart,
    TableNotePart,
    TextBoxNotePart,
    CheckboxNotePart,
    ExternalFileNotePart,
    AssayRunNotePart,
    LookupTableNotePart,
    ResultsTableNotePart,
    RegistrationTableNotePart,
    PlateCreationTableNotePart,
    BoxCreationTableNotePart,
    MixturePrepTableNotePart,
]
