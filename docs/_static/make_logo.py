# /// script
# requires-python = ">=3.11"
# dependencies = ["resvg-py"]
# ///
"""Draw the galactic_dynamics_interoperability logo: a galaxy, converted.

A two-armed spiral galaxy inside two circular arrows, one teal and one purple,
chasing each other round it: objects converted from one galactic dynamics
library to another and back, on GalacticDynamics' dark square. The shapes are
vector, so the logo is written as an SVG, sharp at any size; for a bitmap, name
a .png and give its size::

    uv run docs/_static/make_logo.py                     # favicon.svg
    uv run docs/_static/make_logo.py --size 2048 big.png
"""

import argparse
import math
from pathlib import Path

NAVY, TEAL, PURPLE = "#030a23", "#66a19a", "#7738eb"  # GalacticDynamics' colours
ARM, CORE = "#4fb8e8", "#e8ffff"  # the galaxy's arms and core

CENTRE = 32  # of the 64-unit square
GALAXY = 12  # the arms' outer radius
TURNS = 1.3  # how far each arm winds
RING = 23  # the arrows' radius
ARROWS = ((TEAL, 200), (PURPLE, 20))  # each arrow's colour and starting angle
SWEEP = 140  # degrees each arrow runs, clockwise in the picture

SVG = """\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="512" height="512">
  <rect width="64" height="64" rx="14" fill="{navy}"/>
  <g fill="none" stroke-linecap="round">
{arms}
{arcs}
  </g>
  <circle cx="{c:g}" cy="{c:g}" r="{core:g}" fill="{core_colour}"/>
{heads}
</svg>
"""


def arm(phase: float) -> str:
    """Return one spiral arm, starting at angle ``phase``, as an SVG path."""
    points = []
    for i in range(40):
        t = i / 39
        angle = phase + t * TURNS * 2 * math.pi
        r = GALAXY * (0.12 + 0.88 * t)
        points.append(
            f"{CENTRE + r * math.cos(angle):.2f} {CENTRE + r * math.sin(angle):.2f}",
        )
    return "M" + "L".join(points)


def arrow(start: float) -> tuple[str, str]:
    """Return an arrow's arc as an SVG path, and its head as polygon points."""
    a0, a1 = math.radians(start), math.radians(start + SWEEP)
    x0, y0 = CENTRE + RING * math.cos(a0), CENTRE + RING * math.sin(a0)
    x1, y1 = CENTRE + RING * math.cos(a1), CENTRE + RING * math.sin(a1)
    arc = f"M{x0:.2f} {y0:.2f}A{RING} {RING} 0 0 1 {x1:.2f} {y1:.2f}"
    # The head: a tip ahead along the circle, and a base across it.
    tx, ty = -math.sin(a1), math.cos(a1)
    nx, ny = math.cos(a1), math.sin(a1)
    head = [(x1 + 4.5 * tx, y1 + 4.5 * ty), (x1 - 4 * nx, y1 - 4 * ny)]
    head.append((x1 + 4 * nx, y1 + 4 * ny))
    return arc, " ".join(f"{x:.2f},{y:.2f}" for x, y in head)


def svg() -> str:
    """Return the logo as SVG text."""
    arms = "\n".join(
        f'    <path d="{arm(phase)}" stroke="{ARM}" stroke-width="3"/>'
        for phase in (0, math.pi)
    )
    arcs, heads = [], []
    for colour, start in ARROWS:
        arc, head = arrow(start)
        arcs.append(f'    <path d="{arc}" stroke="{colour}" stroke-width="4"/>')
        heads.append(f'  <polygon points="{head}" fill="{colour}"/>')
    return SVG.format(
        navy=NAVY,
        arms=arms,
        arcs="\n".join(arcs),
        heads="\n".join(heads),
        c=CENTRE,
        core=0.18 * GALAXY,
        core_colour=CORE,
    )


def main() -> None:
    """Parse the command line and save the logo."""
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "out",
        nargs="?",
        type=Path,
        default=Path(__file__).with_name("favicon.svg"),
        help="output file, SVG or PNG by its extension (default: favicon.svg)",
    )
    parser.add_argument(
        "--size",
        type=int,
        default=512,
        help="pixels per side, for a PNG",
    )
    args = parser.parse_args()

    if args.out.suffix == ".svg":
        args.out.write_text(svg())
    else:
        import resvg_py  # noqa: PLC0415  # only a PNG needs a renderer

        png = resvg_py.svg_to_bytes(svg_string=svg(), width=args.size)
        args.out.write_bytes(bytes(png))


if __name__ == "__main__":
    main()
