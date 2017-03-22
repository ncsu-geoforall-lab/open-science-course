#!/bin/bash

remote=$(git config --get remote.origin.url)

build_dir="build"

rm -r $build_dir

git clone $remote $build_dir

cd $build_dir

git checkout --orphan gh-pages

git rm -rf .

# we need to have something to be able to commit
cd ..
./build.sh

cd $build_dir

git add -A
git commit -a -m "Initial commit of the website"

# commit is required to push the branch
git push --set-upstream origin gh-pages
