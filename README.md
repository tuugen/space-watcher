
# doccker
docker build . -t spacewatcher

## docker
docker run -it --workdir /usr/workspace -v $(pwd):/usr/workspace --entrypoint=sh spacewatcher

## run outside of container
docker run -it --workdir /usr/workspace -v $(pwd):/usr/workspace spacewatcher python3 test_script.py


https://devhints.io/xpath