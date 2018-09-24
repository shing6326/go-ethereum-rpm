## Go Ethereum

The rpm source for office golang implementation of the Ethereum protocol.
For more details of go-ethereum, please visit https://github.com/ethereum/go-ethereum

## Building the source rpm

Install rpmspectool to download the source files inside rpm spec
```bash
yum install rpmspectool
```

Install mock environment to build the rpm
https://github.com/rpm-software-management/mock/wiki

Copy the spec file from repository
```bash
cd ~
mkdir rpmbuild/SPECS
cp SPECS/go-ethereum.spec rpmbuild/SPECS/
```

Download the source file and build source rpm
```bash
spectool -g -R rpmbuild/SPECS/go-ethereum.spec
```

Build the source rpm using mock
```bash
mock --resultdir=$HOME --buildsrpm --spec rpmbuild/SPECS/go-ethereum.spec --sources rpmbuild/SOURCES -v
```

Compile
```bash
mock -v go-ethereum-1.8.15-1.el7.src.rpm
```
