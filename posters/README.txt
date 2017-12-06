# Poster instructions

## Dependencies

This poster requires pdflatex been installed.
In addition, some styles are needed.

Fedora:

    dnf install texlive texlive-a0poster texlive-wrapfig \
        texlive-standalone texlive-tikzposter texlive-xstring

Debian/Ubuntu:

    sudo apt-get install texlive-latex-extra texlive-pictures pgf

## Rasterization

To create a rasterized version (some plotters have trouble with the PDF)
use

    make rasterize

You can use this file to create a small PNG of the poster. It is best
rescaled in Gimp using Sinc (Lanczos3) method.

To create a minimum size image which will be still readable (although
not necessarily nice) use:

    # renders fonts with low quality
    gs -sDEVICE=png16m -dDownScaleFactor=2 -r50 \
        -o poster.png poster.pdf
    # optimizes compression
    optipng -o9 poster.png
    # simplify colors (destroys some colors, esp. gradients)
    pngnq -n 128 -s 3 poster.png
    # overwrite the original file
    mv poster-nq8.png poster.png

## Conversions

To convert SVGs to PDFs use:

    inkscape -z --export-pdf=file.pdf --export-area-drawing --export-dpi=300 file.svg

## Git and publishing

## Git, build, and publishing

Standard LaTeX source files are tracked by Git, compiled results are not
but are published through the gh-pages branch (build directory).
Compilation can be done using make or manually. However, the build
script calls make (which in turn calls LaTeX) to do the job.
