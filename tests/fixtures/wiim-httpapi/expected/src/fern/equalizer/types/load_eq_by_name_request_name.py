

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class LoadEqByNameRequestName(enum.StrEnum):
    FLAT = "Flat"
    ACOUSTIC = "Acoustic"
    BASS_BOOSTER = "Bass Booster"
    BASS_REDUCER = "Bass Reducer"
    CLASSICAL = "Classical"
    DANCE = "Dance"
    DEEP = "Deep"
    ELECTRONIC = "Electronic"
    HIP_HOP = "Hip-Hop"
    JAZZ = "Jazz"
    LATIN = "Latin"
    LOUDNESS = "Loudness"
    LOUNGE = "Lounge"
    PIANO = "Piano"
    POP = "Pop"
    RB = "R&B"
    ROCK = "Rock"
    SMALL_SPEAKERS = "Small Speakers"
    SPOKEN_WORD = "Spoken Word"
    TREBLE_BOOSTER = "Treble Booster"
    TREBLE_REDUCER = "Treble Reducer"
    VOCAL_BOOSTER = "Vocal Booster"

    def visit(
        self,
        flat: typing.Callable[[], T_Result],
        acoustic: typing.Callable[[], T_Result],
        bass_booster: typing.Callable[[], T_Result],
        bass_reducer: typing.Callable[[], T_Result],
        classical: typing.Callable[[], T_Result],
        dance: typing.Callable[[], T_Result],
        deep: typing.Callable[[], T_Result],
        electronic: typing.Callable[[], T_Result],
        hip_hop: typing.Callable[[], T_Result],
        jazz: typing.Callable[[], T_Result],
        latin: typing.Callable[[], T_Result],
        loudness: typing.Callable[[], T_Result],
        lounge: typing.Callable[[], T_Result],
        piano: typing.Callable[[], T_Result],
        pop: typing.Callable[[], T_Result],
        rb: typing.Callable[[], T_Result],
        rock: typing.Callable[[], T_Result],
        small_speakers: typing.Callable[[], T_Result],
        spoken_word: typing.Callable[[], T_Result],
        treble_booster: typing.Callable[[], T_Result],
        treble_reducer: typing.Callable[[], T_Result],
        vocal_booster: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LoadEqByNameRequestName.FLAT:
            return flat()
        if self is LoadEqByNameRequestName.ACOUSTIC:
            return acoustic()
        if self is LoadEqByNameRequestName.BASS_BOOSTER:
            return bass_booster()
        if self is LoadEqByNameRequestName.BASS_REDUCER:
            return bass_reducer()
        if self is LoadEqByNameRequestName.CLASSICAL:
            return classical()
        if self is LoadEqByNameRequestName.DANCE:
            return dance()
        if self is LoadEqByNameRequestName.DEEP:
            return deep()
        if self is LoadEqByNameRequestName.ELECTRONIC:
            return electronic()
        if self is LoadEqByNameRequestName.HIP_HOP:
            return hip_hop()
        if self is LoadEqByNameRequestName.JAZZ:
            return jazz()
        if self is LoadEqByNameRequestName.LATIN:
            return latin()
        if self is LoadEqByNameRequestName.LOUDNESS:
            return loudness()
        if self is LoadEqByNameRequestName.LOUNGE:
            return lounge()
        if self is LoadEqByNameRequestName.PIANO:
            return piano()
        if self is LoadEqByNameRequestName.POP:
            return pop()
        if self is LoadEqByNameRequestName.RB:
            return rb()
        if self is LoadEqByNameRequestName.ROCK:
            return rock()
        if self is LoadEqByNameRequestName.SMALL_SPEAKERS:
            return small_speakers()
        if self is LoadEqByNameRequestName.SPOKEN_WORD:
            return spoken_word()
        if self is LoadEqByNameRequestName.TREBLE_BOOSTER:
            return treble_booster()
        if self is LoadEqByNameRequestName.TREBLE_REDUCER:
            return treble_reducer()
        if self is LoadEqByNameRequestName.VOCAL_BOOSTER:
            return vocal_booster()
