



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .note_data import NoteData
    from .packet import Packet
    from .packet_note_create_request import PacketNoteCreateRequest
    from .photo_note import PhotoNote
    from .text_note import TextNote
_dynamic_imports: typing.Dict[str, str] = {
    "NoteData": ".note_data",
    "Packet": ".packet",
    "PacketNoteCreateRequest": ".packet_note_create_request",
    "PhotoNote": ".photo_note",
    "TextNote": ".text_note",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = ["NoteData", "Packet", "PacketNoteCreateRequest", "PhotoNote", "TextNote"]
