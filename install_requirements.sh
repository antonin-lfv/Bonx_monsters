# Install requirements for the project from requirements.txt
echo "Installing requirements..."
# test if pip or pip3 is installed
if command -v pip3 &>/dev/null; then
    pip3 install -r requirements.txt
elif command -v pip &>/dev/null; then
    pip install -r requirements.txt
else
    echo "pip or pip3 not found. Please install pip or pip3."
    exit 1
fi
