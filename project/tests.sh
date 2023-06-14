#!/bin/bash

# Check if files exist
#cd ..

if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

cd data

python data_pull.py

if [ $? -eq 0 ]; then
    echo "data_pull.py executed successfully."
else
    echo "data_pull.py execution failed."
    exit 1
fi

if [ -f "data.sqlite" ]; then
    echo "data.sqlite File check test passed."
else
    echo "File check test failed."
    exit 1
fi

# Execute pytest.py
cd ..
cd project

python tests.py

# Check if test.py executed successfully
if [ $? -eq 0 ]; then
    echo "All tests passed."
    exit 0
else
    echo "Some tests failed."
    exit 1
fi