"""Galax interoperability."""

from __future__ import annotations

__all__ = ["GalaxLibrary"]


from typing import Any, final

from plum import conversion_method

from galactic_dynamics_interoperability._base import AbstractInteroperableLibrary
from galactic_dynamics_interoperability._core import convert_potential


@final
class GalaxLibrary(AbstractInteroperableLibrary):
    """The :mod:`galax` library."""


# plum support
@conversion_method(type_from=object, type_to=GalaxLibrary)  # type: ignore[misc]
def convert_to_galax_library(obj: object) -> Any:
    """Convert to an :class:`GalaxLibrary` object."""
    convert_potential(GalaxLibrary, obj)
