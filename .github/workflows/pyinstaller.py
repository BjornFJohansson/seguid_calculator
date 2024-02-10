name: Pyinstaller
on:
  release:
    types: [published]
    branches:
      - master
  workflow_dispatch:
jobs:
  build:
    name: Pyinstaller (${{ matrix.python-version }}, ${{ matrix.os }})
    strategy:
      fail-fast: false
      matrix:
        os: ['ubuntu-latest', 'macos-latest', 'windows-latest']
        python-version: ["3.10"]

    runs-on: ${{ matrix.os }}
    steps:

      - name: 🛑 Cancel Previous Runs
        uses: styfle/cancel-workflow-action@0.11.0

      - name: ⬇️ Checkout
        uses: actions/checkout@v3

      - name: 🌍 Install conda environment
        uses: mamba-org/provision-with-micromamba@main
        with:
          environment-file: pyinstaller_env.yml
          environment-name: pyinstaller_env
          extra-specs: python=${{ matrix.python-version }}
          cache-downloads: true
          cache-env: true

      - name: 🐍 micromamba info
        shell: bash -l {0}
        run: micromamba info

      - name: 🐍 micromamba list
        shell: bash -l {0}
        run: micromamba list

      - name: Install upx on Linux # https://stackoverflow.com/questions/57982945/how-to-apt-get-install-in-a-github-actions-workflow
        shell: bash -l {0}
        if: matrix.os == 'ubuntu-latest'
        run: sudo apt-get install -y upx

      - name: generate _version.py
        shell: bash -l {0}
        run: python setup.py --version

      - name: pyinstaller
        shell: bash -l {0}
        run: pyinstaller --onefile --disable-windowed-traceback --windowed --icon=calc.ico --name seguid_calculator src/gui.py

      - name: ls in dist folder
        shell: bash -l {0}
        run: ls dist

      - name: zip the app for Mac
        shell: bash -l {0}
        if: matrix.os == 'macos-latest'
        run: zip -r dist/seguid_calculator_for_mac.zip dist/seguid_calculator.app

      - name: Upload Mac
        uses: softprops/action-gh-release@v1
        if: matrix.os == 'macos-latest'
        with:
          files: |
            dist/seguid_calculator_for_mac.zip

      - name: Upload Win Lin
        uses: softprops/action-gh-release@v1
        if: matrix.os != 'macos-latest'
        with:
          files: |
            dist/seguid_calculator.exe
            dist/seguid_calculator
