import os

# See Apple's documentation:
# https://developer.apple.com/design/human-interface-guidelines/macos/icons-and-images/app-icon#app-icon-sizes
ICON_SIZES = (
    # These are the @1x sizes
    { "size" : 16,   "scale" : 1},
    { "size" : 32,   "scale" : 1},
    { "size" : 64,   "scale" : 1},
    { "size" : 128,  "scale" : 1},
    { "size" : 256,  "scale" : 1},
    { "size" : 512,  "scale" : 1},
    { "size" : 1024, "scale" : 1},

    # These are the @2x retina sizes
    { "size" : 16,   "scale" : 2},
    { "size" : 32,   "scale" : 2},
    { "size" : 64,   "scale" : 2},
    { "size" : 128,  "scale" : 2},
    { "size" : 256,  "scale" : 2},
    { "size" : 512,  "scale" : 2},
    { "size" : 1024, "scale" : 2},
)

LOGOS = (
    "debian",
)

if __name__ == "__main__":
    for logo in LOGOS:
        icns_dir = f"{logo}.iconset"

        try:
            os.mkdir(icns_dir)
        except FileExistsError:
            print(f"Can't create {icns_dir} for {logo} -- skipping")
            continue

        # Create the PNG files from the SVG source
        for icon in ICON_SIZES:
            pixels = icon.get("size")
            scale = icon.get("scale")

            # Retina icons are labeled 128x128@2, but are 256x256px of data
            if scale > 1:
                label_size = int(pixels / scale)
                scale = f"@{scale}x"
            else:
                label_size = pixels
                scale = ""

            cmd = f"rsvg-convert -f png -h {pixels} -w {pixels} " \
                  f"-o {logo}.iconset/icon_{label_size}x{label_size}{scale}.png " \
                  f"sources/{logo}.svg"

            print(cmd)
            os.system(cmd)
