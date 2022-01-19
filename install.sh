#!/bin/bash

parent="$(dirname "$(pwd)")"

mv "${parent}/models/research/object_detection/builders/preprocessor_builder.py" "${parent}/models/research/object_detection/builders/preprocessor_builder_orig.py"
mv "${parent}/models/research/object_detection/core/preprocessor.py"             "${parent}/models/research/object_detection/core/preprocessor_orig.py"
mv "${parent}/models/research/object_detection/core/preprocessor_cache.py"       "${parent}/models/research/object_detection/core/preprocessor_cache_orig.py"
mv "${parent}/models/research/object_detection/protos/preprocessor.proto"        "${parent}/models/research/object_detection/protos/preprocessor_orig.proto"

cp ./object_detection/builders/preprocessor_builder.py "${parent}/models/research/object_detection/builders/"
cp ./object_detection/core/preprocessor.py "${parent}/models/research/object_detection/core/"
cp ./object_detection/core/preprocessor_cache.py "${parent}/models/research/object_detection/core/"
cp ./object_detection/protos/preprocessor.proto "${parent}/models/research/object_detection/protos/"