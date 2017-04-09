BUILD_DIR=../build/lectures

mkdir -p $BUILD_DIR

./copy-common-files.py --dst-dir=$BUILD_DIR


# TODO: split code for special presentations
for FILE in `ls *.html|grep -v foot|grep -v head`
do
    ./build-slides.py --outdir=$BUILD_DIR \
        --title "How to make your research reproducible" \
        --meta-description "US-IALE 2017 talk about open science" \
        --meta-author "Vaclav Petras" \
        --outfile=$FILE $FILE
done
