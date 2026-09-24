

import typing

from .note_entity_name_five import NoteEntityNameFive
from .note_entity_name_four import NoteEntityNameFour
from .note_entity_name_one import NoteEntityNameOne
from .note_entity_name_seven import NoteEntityNameSeven
from .note_entity_name_six import NoteEntityNameSix
from .note_entity_name_three import NoteEntityNameThree
from .note_entity_name_two import NoteEntityNameTwo
from .note_entity_name_zero import NoteEntityNameZero

NoteEntityName = typing.Union[
    NoteEntityNameZero,
    NoteEntityNameOne,
    NoteEntityNameTwo,
    NoteEntityNameThree,
    NoteEntityNameFour,
    NoteEntityNameFive,
    NoteEntityNameSix,
    NoteEntityNameSeven,
]
