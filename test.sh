#!/bin/bash

# comp  - stdout and stderr from compilation
# eval  - stdout and stderr from evaluation
# stack - compiled stack code

TESTD="test"
STAKD="$TESTD/stack"
COMPD="$TESTD/comp"
EVALD="$TESTD/eval"

comp() {
    for f in $(ls test/ | grep .pjp); do
        SRC_FILE="$TESTD/$f"

        if [[ -f $SRC_FILE ]]; then
            SRC_STRIP=$(echo $f | sed s/\.pjp$//)
            OUT_FILE="$STAKD/$SRC_STRIP.stack"
            COMP_DUMP="$COMPD/$SRC_STRIP.dump"

            echo "Compiling '$SRC_FILE' into '$OUT_FILE' and dumping '$COMP_DUMP'..."
            python compile.py $SRC_FILE $OUT_FILE &> $COMP_DUMP
        fi
    done
}

eval() {
    for f in $(ls $STAKD); do
        STAK_FILE="$STAKD/$f"
        STAK_STRIP=$(echo $f | sed s/\.stack$//)

        EVAL_DUMP="$EVALD/$STAK_STRIP.out"
        STDIN_FILE="$TESTD/$STAK_STRIP.in"

        if [[ -f $STDIN_FILE ]]; then
            echo "Evaling '$STAK_FILE' using '$STDIN_FILE' into '$EVAL_DUMP'..."
            python eval.py $STAK_FILE < $STDIN_FILE &> $EVAL_DUMP
        else
            echo "Evaling '$STAK_FILE' into '$EVAL_DUMP'..."
            python eval.py $STAK_FILE &> $EVAL_DUMP
        fi
    done
}

remove() {
    DIRS="$COMPD $EVALD $STAKD"

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

