from PIL import Image
import io

# All icon variants required by Payload/Application.app/Info.plist
IOS_ICON_SIZES = [
    ("AppIcon29x29.png",     29),
    ("AppIcon29x29@2x.png",  58),
    ("AppIcon29x29@3x.png",  87),
    ("AppIcon40x40.png",     40),
    ("AppIcon40x40@2x.png",  80),
    ("AppIcon40x40@3x.png",  120),
    ("AppIcon57x57.png",     57),
    ("AppIcon57x57@2x.png",  114),
    ("AppIcon60x60.png",     60),
    ("AppIcon60x60@2x.png",  120),
    ("AppIcon60x60@3x.png",  180),
    ("AppIcon50x50.png",     50),
    ("AppIcon50x50@2x.png",  100),
    ("AppIcon72x72.png",     72),
    ("AppIcon72x72@2x.png",  144),
    ("AppIcon76x76.png",     76),
    ("AppIcon76x76@2x.png",  152),
]


def generate_icons(image_bytes: bytes) -> dict:
    """
    Accepts raw bytes of any common image format (PNG, JPEG, WEBP, …).
    Returns {filename: png_bytes} for every required iOS icon size.
    """
    source = Image.open(io.BytesIO(image_bytes)).convert("RGBA")
    icons = {}
    for filename, size in IOS_ICON_SIZES:
        resized = source.resize((size, size), Image.LANCZOS)
        buf = io.BytesIO()
        resized.save(buf, format="PNG")
        icons[filename] = buf.getvalue()
    return icons
