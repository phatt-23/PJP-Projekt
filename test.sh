#!/bin/bash

# comp  - stdout and stderr from compilation
# eval  - stdout and stderr from evaluation
# stack - compiled stack code




comp() {
    for f in $(ls test/); do
        echo "Compiling test/$f..."
        OUT_FILE="test/stack/$f.stack"
        SRC_FILE="test/$f"
        
        if [[ -f $SRC_FILE ]]; then
            python compile.py $SRC_FILE $OUT_FILE &> test/comp/$f.dump
        fi
    done
}

eval() {
    for f in $(ls test/stack/); do
        STCK_FILE=test/stack/$f
        STCK_OUT=test/eval/$(echo $f | sed s/\.stack$/\.out/)
        echo "Evaling $STCK_FILE into $STCK_OUT..."
        python eval.py $STCK_FILE &> $STCK_OUT
    done
}

remove() {
    DIRS="test/comp/ test/eval/ test/stack/"

    echo "Removing $DIRS..."
    for d in $DIRS; do rm -r $d 2> /dev/null; done
    for d in $DIRS; do mkdir -p $d 2> /dev/null; done
}

case "$1" in
    "c")
        comp
        ;;
    "e")
        eval
        ;;
    "ce")
        comp
        eval
        ;;
    "rm")
        remove
        ;;
    *)
        echo "$0 [c, e, ce]"
        ;;
esac

