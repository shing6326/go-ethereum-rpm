Name:    go-ethereum
Version: 1.8.17
Release: 1%{?dist}
Summary: Official golang implementation of the Ethereum protocol

License: GPLv3 and LGPLv3
URL:     https://geth.ethereum.org/
Source0: https://github.com/ethereum/%{name}/archive/v%{version}.tar.gz

BuildRequires: golang
BuildRequires: make

%description
Ethereum is a decentralized platform that runs smart contracts, applications
that run exactly as programmed without possibility of downtime, censorship,
fraud or third party interference.

Go Ethereum is one of the three original implementations
(along with C++ and Python) of the Ethereum protocol.
It is written in Go, fully open source and licensed under the GNU LGPL v3.

%prep
%setup -q


%build
make %{?_smp_mflags} geth


%install
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 build/bin/geth %{buildroot}%{_bindir}


%files
%{_bindir}/geth
%doc AUTHORS
%doc README.md
%license COPYING
%license COPYING.LESSER

%changelog
