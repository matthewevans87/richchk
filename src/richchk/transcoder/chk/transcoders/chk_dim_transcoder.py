"""Decode and encode the DIM section which contains map dimensions data.

Required for all versions and game types. Validation: Must be size of 4 bytes.

This section contains the dimensions of the map.

u16: Width of map in tiles (32 pixels per tile)
u16: Height of map in tiles (32 pixels per tile)
"""

import struct
from io import BytesIO

from ....model.chk.dim.decoded_dim_section import DecodedDimSection
from ....transcoder.chk.chk_section_transcoder import ChkSectionTranscoder
from ....transcoder.chk.chk_section_transcoder_factory import _RegistrableTranscoder


class ChkDimTranscoder(
    ChkSectionTranscoder[DecodedDimSection],
    _RegistrableTranscoder,
    chk_section_name=DecodedDimSection.section_name(),
):
    def decode(self, chk_section_binary_data: bytes) -> DecodedDimSection:
        bytes_stream: BytesIO = BytesIO(chk_section_binary_data)
        width = struct.unpack("H", bytes_stream.read(2))[0]
        height = struct.unpack("H", bytes_stream.read(2))[0]
        return DecodedDimSection(_width=width, _height=height)

    def _encode(self, decoded_chk_section: DecodedDimSection) -> bytes:
        data: bytes = b""
        data += struct.pack("H", decoded_chk_section.width)
        data += struct.pack("H", decoded_chk_section.height)
        return data
