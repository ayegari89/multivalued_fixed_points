# multivalued_fixed_points

This instructions are made for an Ubuntu installation

Conda enviroment

Install miniconda

mkdir -p ~/miniconda3

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh

bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3

rm -rf ~/miniconda3/miniconda.sh



~/miniconda3/bin/conda init bash

y abrir una nueva consola

Create enviroment

conda create --name fixed_points python=3.11

conda activate fixed_points

Download project

mkdir fixed_points

cd fixed_points

git clone git@github.com:ayegari89/multivalued_fixed_points.git

Install requirements

conda install pip

cd multivalued_fixed_points

pip install -r requirements.txt 

sudo apt install autoconf libtool automake



Install requirements for Barvinok (we need to install glpk, gmp and ntl)

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

cd ..

python frontend.py



