pip uninstall object_detection -y
cd models/research
cp object_detection/packages/tf2/setup.py .
python -m pip install --use-feature=2020-resolver .