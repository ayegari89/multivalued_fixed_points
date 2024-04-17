# multivalued_fixed_points

This instructions are made based on an Ubuntu installation. They are a list of commands required to run in a Bash console.

## General system prerequisites

autoconf libtool automake (if not installed, could be installed with: sudo apt install autoconf libtool automake) 

Conda (if not installed, could be installed as miniconda, as suggested in next section)

### Install miniconda (optional, if Conda is not installed)

mkdir -p ~/miniconda3

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh

bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3

rm -rf ~/miniconda3/miniconda.sh

~/miniconda3/bin/conda init bash

and open a new console window before next steps.


## Create Conda environment

conda create --name fixed_points python=3.11

conda activate fixed_points

## Download project

BASE_DIR=~ #you can change the BASE_DIR to fit your preference

cd $BASE_DIR

mkdir fixed_points

cd fixed_points

git clone git@github.com:ayegari89/multivalued_fixed_points.git #this uses ssh for downloading from github. you can use other means to download the project, but make sure to preserve the same directory structure that would have been using git clone.

## Install requirements

conda install pip

cd multivalued_fixed_points

pip install -r requirements.txt 


## Install requirements for Barvinok (we need to install glpk, gmp and ntl)

cd ..

wget https://ftp.gnu.org/gnu/glpk/glpk-4.35.tar.gz

tar -xaf glpk-4.35.tar.gz

cd glpk-4.35/

./configure

make

sudo make install

cd ..

wget https://libntl.org/ntl-11.5.1.tar.gz

tar -xaf ntl-11.5.1.tar.gz

wget https://gmplib.org/download/gmp/gmp-6.3.0.tar.xz

tar -xaf gmp-6.3.0.tar.xz 

cd gmp-6.3.0/

./configure && make && sudo make install

make check

cd ..

cd ntl-11.5.1/

cd src/

./configure NTL_GMP_LIP=on PREFIX=/opt GMP_PREFIX=/usr/local/lib

sudo ldconfig 

make

sudo make install

cd ../..

cd multivalued_fixed_points/

git clone https://repo.or.cz/barvinok.git

cd barvinok

cp ../barvinok_modificado/polytope_scan.c .

cp ../barvinok_modificado/Makefile.am .

./get_submodules.sh 

sh autogen.sh 

./configure --prefix=/opt --with-gmp-prefix=/usr/local/lib --with-ntl-prefix=/opt

make

sudo make install

# How to run

conda activate fixed_points #make sure you are in the conda environment that we created to run the program

BASE_DIR=~ #you can change the BASE_DIR to fit your preference (make it consistent with the installation)

cd $BASE_DIR/fixed_points/multivalued_fixed_points

python frontend.py



Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

