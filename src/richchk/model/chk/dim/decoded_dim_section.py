"""DIM - Map dimensions.

Required for all versions and game types. Validation: Must be size of 4 bytes.

This section contains the dimensions of the map.

u16: Width of map in tiles (32 pixels per tile)
u16: Height of map in tiles (32 pixels per tile)
"""

import dataclasses

from ...chk_section_name import ChkSectionName
from ..decoded_chk_section import DecodedChkSection


@dataclasses.dataclass(frozen=True)
class DecodedDimSection(DecodedChkSection):
    """Represent DIM section for map dimensions.

    :param _width: u16 width of map in tiles (32 pixels per tile)
    :param _height: u16 height of map in tiles (32 pixels per tile)
    """

    _width: int
    _height: int

    @classmethod
    def section_name(cls) -> ChkSectionName:
        return ChkSectionName.DIM

    @property
    def width(self) -> int:
        """Width of the map in tiles."""
        return self._width

    @property
    def height(self) -> int:
        """Height of the map in tiles."""
        return self._height

    def get_pixel_dimensions(self) -> tuple[int, int]:
        """
        Returns the map dimensions in pixels.
        Each tile is 32x32 pixels.
        """
        return self.width * 32, self.height * 32