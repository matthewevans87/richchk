from dataclasses import dataclass
from richchk.model.chk.dim.decoded_dim_section import DecodedDimSection

@dataclass(frozen=True)
class RichDimSection:
    # Represent the rich (enhanced) DIM section
    _width: int
    _height: int

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @classmethod
    def from_decoded(cls, decoded_dim_section: DecodedDimSection) -> "RichDimSection":
        # Create a RichDimSection from a decoded DIM section
        return cls(_width=decoded_dim_section.width, _height=decoded_dim_section.height)