from richchk.io.mpq.starcraft_mpq_io_helper import StarCraftMpqIoHelper
from richchk.model.chk.dim.decoded_dim_section import DecodedDimSection
from richchk.model.richchk.dim.rich_dim_section import RichDimSection
from richchk.model.richchk.mrgn.rich_mrgn_section import RichMrgnSection

# Initialize
PATH_TO_STORMLIB_DLL = None
MAP_FILE_PATH = "./examples/maps/(8)The Hunters.scm"

# Create MPQ I/O handler and load map
mpq_io = StarCraftMpqIoHelper.create_mpq_io(PATH_TO_STORMLIB_DLL)
chk = mpq_io.read_chk_from_mpq(MAP_FILE_PATH)

# Print available sections for debugging
print("Available sections in the CHK file:")
for section in chk.chk_sections:
    print(f"- {section.__class__.__name__}")

# Try to get dimensions more safely
try:
    # For RichChk objects we need to find the RichDimSection
    dim_section = None
    for section in chk.chk_sections:
        if isinstance(section, RichDimSection):
            dim_section = section
            break
    
    if dim_section:
        width = dim_section.width
        height = dim_section.height
        print(f"Map dimensions: {width}x{height} tiles")
        print(f"Map dimensions in pixels: {width*32}x{height*32} pixels")
    else:
        raise ValueError("No DIM section found")
except ValueError as e:
    print(f"Error: {e}")
    print("Trying alternate approach...")
    
    # Try to find dimension information from another section like MRGN
    # Note: This is a fallback approach and may not be accurate
    try:
        mrgn_section = None
        for section in chk.chk_sections:
            if isinstance(section, RichMrgnSection):
                mrgn_section = section
                break
        
        if mrgn_section:
            # Find maximum x and y coordinates from locations
            max_x = 0
            max_y = 0
            for loc in mrgn_section.locations:
                if loc.right_x2 > max_x:
                    max_x = loc.right_x2
                if loc.bottom_y2 > max_y:
                    max_y = loc.bottom_y2
            
            # Convert pixels to tiles (32 pixels per tile)
            width_tiles = max_x // 32
            height_tiles = max_y // 32
            
            print(f"Estimated map dimensions (from locations): {width_tiles}x{height_tiles} tiles")
            print(f"Map dimensions in pixels: {max_x}x{max_y} pixels")
        else:
            print("No MRGN section found")
    except Exception as e2:
        print(f"Could not determine map dimensions: {e2}")