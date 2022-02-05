#!/bin/bash

parent="$(dirname "$(pwd)")"

if [ ! -f "${parent}/models/research/object_detection/builders/preprocessor_builder.py.orig" ]; then
    mv "${parent}/models/research/object_detection/builders/preprocessor_builder.py" "${parent}/models/research/object_detection/builders/preprocessor_builder.py.orig"
fi
if [ ! -f "${parent}/models/research/object_detection/core/preprocessor.py.orig" ]; then
    mv "${parent}/models/research/object_detection/core/preprocessor.py"             "${parent}/models/research/object_detection/core/preprocessor.py.orig"
fi
if [ ! -f "${parent}/models/research/object_detection/core/preprocessor_cache.py.orig" ]; then
    mv "${parent}/models/research/object_detection/core/preprocessor_cache.py"       "${parent}/models/research/object_detection/core/preprocessor_cache.py.orig"
fi
if [ ! -f "${parent}/models/research/object_detection/protos/preprocessor.proto.orig" ]; then
    mv "${parent}/models/research/object_detection/protos/preprocessor.proto"        "${parent}/models/research/object_detection/protos/preprocessor.proto.orig"
fi

cp ./object_detection/builders/preprocessor_builder.py "${parent}/models/research/object_detection/builders/"
cp ./object_detection/core/preprocessor.py "${parent}/models/research/object_detection/core/"
cp ./object_detection/core/imgaug_utils.py "${parent}/models/research/object_detection/core/"
cp ./object_detection/core/preprocessor_cache.py "${parent}/models/research/object_detection/core/"
cp ./object_detection/protos/preprocessor.proto "${parent}/models/research/object_detection/protos/"
