#!/usr/bin/env bash
echo "=============================================================="
echo "BASH_VERSION" $BASH_VERSION
echo $(git --version)
tagname="$(git describe --abbrev=0 --tags)"
tag="$(git rev-list $tagname | head -n 1)"
com="$(git rev-parse HEAD)"
dirty=$(git describe --tags --dirty --always)
msg=$(git log -1 --pretty=%B)
echo "=============================================================="
echo "Establish git variables:"
echo "=============================================================="
echo "Current commit hash : $com"
echo "Dirty tag           : $dirty"
echo "Commit msg          : $msg"
echo "=============================================================="
echo "Environment variables:"
echo "=============================================================="
echo "CI                   = $CI"
echo "APPVEYOR             = $APPVEYOR"
echo "CIRCLECI             = $CIRCLECI"
echo "TRAVIS               = $TRAVIS"
echo "CODESHIP             = $CI_NAME"
echo "=============================================================="
echo "Build information:"
echo "=============================================================="
if [[ "$com" = "$tag" ]]&&[[ $dirty = $tagname ]]
then
    echo "Tagged commit      : $tagname"
    tagged_commit=true
    re_final="^[0-9]\.[0-9]\.[0-9]$"
    re_pre="^[0-9]\.[0-9]\.[0-9](a|b|rc)[0-9]+$"
    if [[ $tagname =~  $re_final ]]
    then
        echo "Tag indicate Final release"
        echo "deploy to pypi and anaconda.org with label 'main'."
        pypiserver="pypi"
        condalabel="main"
    elif  [[ $tagname =~ $re_pre ]]
    then
        echo "Release tag indicate pre release"
        echo "deploy sdist zip package to pypi "
        echo "conda package anaconda.org with label 'test'."
        pypiserver="testpypi"
        condalabel="test"
    else
        echo "Build cancelled because"
        echo "release tag ($tagname) was not recognized"
        echo "or"
        echo "$dirty != $tagname"
        exit 0
    fi
elif [[ $msg = *"skip"* ]]
then
    echo "Not a tagged commit"
    echo "'skip' found in commit msg: '$msg'"
    echo "tests and builds skipped."
    echo "=============================================================="
    exit 0 
else
    echo "'skip' not found in commit msg: '$msg'"
    echo "but commit not tagged or tag dirty"
    echo "test suit will be run."
    tagged_commit=false

unset VIRTUAL_ENV
