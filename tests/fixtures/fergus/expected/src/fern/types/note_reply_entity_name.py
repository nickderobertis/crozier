

import typing

from .note_reply_entity_name_five import NoteReplyEntityNameFive
from .note_reply_entity_name_four import NoteReplyEntityNameFour
from .note_reply_entity_name_one import NoteReplyEntityNameOne
from .note_reply_entity_name_seven import NoteReplyEntityNameSeven
from .note_reply_entity_name_six import NoteReplyEntityNameSix
from .note_reply_entity_name_three import NoteReplyEntityNameThree
from .note_reply_entity_name_two import NoteReplyEntityNameTwo
from .note_reply_entity_name_zero import NoteReplyEntityNameZero

NoteReplyEntityName = typing.Union[
    NoteReplyEntityNameZero,
    NoteReplyEntityNameOne,
    NoteReplyEntityNameTwo,
    NoteReplyEntityNameThree,
    NoteReplyEntityNameFour,
    NoteReplyEntityNameFive,
    NoteReplyEntityNameSix,
    NoteReplyEntityNameSeven,
]
