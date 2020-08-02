# libreicns
A collection of Free Software logos packaged into full macOS/Apple iconsets.

## Problem
macOS and Apple systems use .icns files for a variety of things. While
there's libicns in the Free world, it doesn't support the newest sizes
and formats, plus you still have to figure out sizes, filenames, and
then generate the PNG icons yourself.

This is specially bothersome for things like adding a `.VolumeIcon.icns`
file to a partition so that macOS shows a nice icon, either in Finder,
or in the bootloader.

The Free world has `libicns` but it's unmaintained and does not support
the newer formats. Of special importance is that it doesn't know how to
properly output an `.icns` that properly works as a volume icon.

See:
* https://ericfromcanada.github.io/output/2020/multi-macos-install-drive-diskmaker.html
* https://en.wikipedia.org/wiki/Apple_Icon_Image_format#Icon_types


## Solution
This repo hosts the packaged .icns files for the corresponding PNGs and
SVGs of a bunch of Free Software logos. The PNGs are created with
`rsvg-convert` in Linux, and then packaged with `iconutil` in macOS.

See: https://retifrav.github.io/blog/2018/10/09/macos-convert-png-to-icns/


## License
Whatever code is here is GPLv3+, but obviously each logo carries a
different license or trademark. See the corresponding
"$logo-license.txt" file next to each one, or the `git log` for each.

Note that some logos don't have a "license" but are published together
with "brand guidelines". Read the source URL for each logo before using
these for anything that is not casual personal use.


## Want your logo removed? Added?
Just file an issue and I'll drop it, or add it, from the repo.
