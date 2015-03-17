Name:		droid-hal-tools
Version:	0.0.1
Release:	1%{?dist}
Summary:	Some tools from android

Group:		Tools
License:	ASL 2.0
URL:		https://android.googlesource.com/
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(zlib)

%description
This package contains some tools that some hardware adaptations need for
handling the android style content. This package is intended to be such
that it can be installed on the device and is not meant to be used in host/sdk
environment.

%prep
%setup -q

%build
make -f %{_builddir}/mkbootimg.mk -C droid-core/mkbootimg/
make -f %{_builddir}/simg2img.mk -C droid-core/libsparse/
make -f %{_builddir}/img2simg.mk -C droid-core/libsparse/

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_bindir}/
cp droid-core/mkbootimg/mkbootimg %{buildroot}/%{_bindir}/
cp droid-core/libsparse/simg2img %{buildroot}/%{_bindir}/
cp droid-core/libsparse/img2simg %{buildroot}/%{_bindir}/

%files
%defattr(-,root,root,-)
%{_bindir}/mkbootimg
%{_bindir}/img2simg
%{_bindir}/simg2img

