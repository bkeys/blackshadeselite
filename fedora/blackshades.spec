Name:           blackshades
Version:        0.9
Release:        1%{?dist}
Summary:        First person shooter - protect the VIP

License:        GPLv3
URL:            https://github.com/ComradeKeys/blackshadeselite
Source0:        %{name}-%{version}.tar.gz

BuildRequires: openal-soft-devel SDL-devel libtool automake autoconf
Requires:openal-soft mesa-libGL SDL

%description
In this FPS the objective is to project the person wearing the white shirt from random assassins trying to kill him. Feauturing different weapons, and game modes for the user to try.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%doc README AUTHORS COPYING NEWS TODO
/usr/bin/%{name}

%changelog
* Sat Nov 14 2015 Comrade Brigham Henry Keys, Esq <bkeys@bkeys.org> .9-1
- submitting package for fedora
