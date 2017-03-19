%global commit0 %{COMMIT_ID}
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           gamelift-cpp-server-sdk
Version:        3.1.5
Release:	%{shortcommit0}%{dist}
Summary:	Amazon GameLift CPP server SDK
Group:		Development/Libraries
License:	Apache
URL:      https://aws.amazon.com/gamelift/
Source0:	gamelift-cpp-server-sdk-%{commit0}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}%{dist}-XXXXXX)
BuildRequires:	boost-date-time, boost-random, boost-system, boost-thread, cmake, make, rpm-build
Requires:	boost-date-time, boost-random, boost-system, boost-thread

%description
Amazon GameLift CPP server SDK
Originally maintained here: https://aws.amazon.com/gamelift
For details, please refer to the site.
For the packaging of shared library version is by https://github.com/iFunFactory/GameLift-Cpp-ServerSDK


#%define debug_package %{nil}


%prep
%setup -q -n gamelift


%build
mkdir rpm_build_result
pushd rpm_build_result
cmake -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS=ON -DUSE_SYSTEM_BOOST=ON -DUSE_SYSTEM_PROTOBUF=ON -DUSE_SYSTEM_SIOCLIENT=ON ..
make
popd


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr
mkdir -p %{buildroot}/usr/include
mkdir -p %{buildroot}/usr/share/aws/gamelift
pushd rpm_build_result
pushd prefix
tar cf - include/aws/gamelift | (cd %{buildroot}/usr; tar xf - )
tar cf - lib/libaws-cpp-sdk-gamelift-server.so | (cd %{buildroot}/usr; tar xf - )
tar cf - cmake/aws-cpp-sdk-gamelift-serverConfig.cmake | (cd %{buildroot}/usr/share/aws/gamelift; tar xf - )
popd
popd


%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,root,0755)
/usr/include/aws/gamelift
/usr/lib/libaws-cpp-sdk-gamelift-server.so
/usr/share/aws/gamelift


%post
/sbin/ldconfig


%postun
/sbin/ldconfig



#%changelog
