#!/bin/bash

parent="$(dirname "$(pwd)")"

mv "${parent}/models/research/object_detection/builders/preprocessor_builder.py" "${parent}/models/research/object_detection/builders/preprocessor_builder.py.orig"
mv "${parent}/models/research/object_detection/core/preprocessor.py"             "${parent}/models/research/object_detection/core/preprocessor.py.orig"
mv "${parent}/models/research/object_detection/core/preprocessor_cache.py"       "${parent}/models/research/object_detection/core/preprocessor_cache.py.orig"
mv "${parent}/models/research/object_detection/protos/preprocessor.proto"        "${parent}/models/research/object_detection/protos/preprocessor.proto.orig"

cp ./object_detection/builders/preprocessor_builder.py "${parent}/models/research/object_detection/builders/"
cp ./object_detection/core/preprocessor.py "${parent}/models/research/object_detection/core/"
cp ./object_detection/core/imgaug_utils.py "${parent}/models/research/object_detection/core/"
cp ./object_detection/core/preprocessor_cache.py "${parent}/models/research/object_detection/core/"
cp ./object_detection/protos/preprocessor.proto "${parent}/models/research/object_detection/protos/"
