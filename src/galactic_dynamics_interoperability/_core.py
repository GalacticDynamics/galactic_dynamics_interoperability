"""Input/output/conversion of potential objects.

This module contains the machinery for I/O and conversion of potential objects.
Conversion is useful for e.g. converting a `galax.potential.AbstractPotential`
object to a `gala.potential.PotentialBase` object.
"""

from __future__ import annotations

__all__ = ["convert_potential"]


from typing import Annotated as Ann, Any
from typing_extensions import Doc

from plum import dispatch

from ._base import AbstractInteroperableLibrary


@dispatch.abstract  # type: ignore[misc]
def convert_potential(
    to_: Ann[
        AbstractInteroperableLibrary | Any,
        Doc("The type (or library) to which to convert the potential"),
    ],
    from_: Ann[Any, Doc("The potential object to be converted")],
    /,
    **_: Ann[Any, Doc("extra arguments used in the conversion process")],
) -> object:
    msg = f"cannot convert {from_} to {to_}"  # pragma: no cover
    raise NotImplementedError(msg)  # pragma: no cover
