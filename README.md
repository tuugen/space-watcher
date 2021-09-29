
# doccker
docker build . -t spacewatcher
# docker m1 mac
docker build --platform linux/amd64 --no-cache . -t spacewatcher

## docker
docker run -it --workdir /usr/workspace -v $(pwd):/usr/workspace --entrypoint=sh spacewatcher

## run outside of container
docker run -it --workdir /usr/workspace -v $(pwd):/usr/workspace spacewatcher python3 test_script.py

## testing from cli  (no docker)
`make sure your chromedriver is on path, and matches installed chrome version`
<https://chromedriver.chromium.org/downloads>

python3 test_script_local.py

## test single case
python -m unittest test_script_local.TestTemplate.test_case_1


## setting up...
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m unittest test_script_local.TestTemplate.test_case_1
etc...
```

https://devhints.io/xpath

